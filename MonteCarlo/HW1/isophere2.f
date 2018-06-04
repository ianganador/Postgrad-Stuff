	module coord
	real x,y,z,nx,ny,nz,theta,phi
	real x0,y0,z0,a,b,c, mu1, del, quad
	real,parameter:: pi=4.*atan(1.)
	end module	
	!forced first scatter, peeling off, and imaging for isotropic sphere
	program sphere
	use coord
	implicit none

	real Xi,s,Rmax,TAUmax,TAU, TAUe, counts
	real  dx,dy,dz, weight,xim,yim
	integer packet,j,npix, iy, ix,i,k
	integer, allocatable :: image(:,:)
	npix=200
	!populate image array
	allocate(image(npix,npix))
	do i=1,npix
		do k=1,npix
			image(i,k)=0
		enddo
	enddo
	
	packet=10000	!number of MC packets
	TAUmax=50	!optical depth
	open(6, file='prob2_tau=50.dat')	!open file to write

	do j=1, packet		!loop over number of packets
		x=0.		!set initial positions and counters to 0.
		y=0.			
		z=0.

		counts=0.
		weight=1.
		TAUe=TAUmax	!set initial tau-escape to taumax
			do
				call random_number(Xi)
				if (counts==0.) then	!forced first scatter if first emission
					TAU=-log(1-Xi*(1-exp(-TAUe)))
					weight=weight*(1-exp(-TAUe))/(4*pi)
				else			!else scatter normally
					TAU=-log(Xi)
					weight=weight*(exp(-TAUe))/(4*pi)
				endif
	
				s=TAU/TAUmax
				x0=x		!bank position values
				y0=y
				z0=z
				call scatter(Xi)
				x=x+s*nx	!calculate new position
				y=y+s*ny
				z=z+s*nz

				if((x*x+y*y+z*z)>1.) then 
					exit	!exit if new value outside of sphere
				endif

				!calculate tau escape from last position to escape using current trajectory
				a = (0-x0)**2. + (0-y0)**2. + (1-z0)**2.
				b = 2.*( x0*(0-x0) + y0*(0-y0) + z0*(1-z0))
				c = x0**2. + y0**2. + z0**2. - 1.
				quad=b*b-4.*a*c
				mu1=(-b+sqrt(quad))/(2*a)
				del=mu1*s
				TAUe=TAUe*del

				!set viewing angle
				theta=0
				phi=0

				!project to image plane
				xim=y*cos(phi)-x*sin(phi)
				yim=z*sin(theta)-y*cos(theta)*sin(phi)-x*cos(theta)*cos(phi)
	
				!convert position to integer in pixels
			        ix=int((xim+1)*npix/2)+1
        			iy=int((yim+1)*npix/2)+1

				!weight pixels
				if(weight==0)then
					image(ix,iy)=image(ix,iy)
				else
         				image(ix,iy)=image(ix,iy)+weight
				endif
				print*, ix, iy, image(ix,iy)
				counts=counts+1
			enddo
	
	enddo	
	end

	!scattering light
	subroutine scatter(Xi)
	use coord

	!generate angles
	call random_number(Xi)
	phi=2.*PI*Xi
	call random_number(Xi)
	theta=acos(2*Xi-1)

	!calculate new direction vector
	nx=sin(theta)*cos(phi)
	ny=sin(theta)*sin(phi)
	nz=cos(theta)

	return
	end


	

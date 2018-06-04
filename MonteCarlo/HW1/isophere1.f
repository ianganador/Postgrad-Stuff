	module coord
	real x,y,z,nx,ny,nz,theta,phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program isotrope sphere
	use coord
	implicit none

	real Xi,s,Rmax,TAUmax,TAU
	real distance, counts, x0,y0,z0, quad, mu1,mu2
	real a,b,c, dx,dy,dz,del, weight
	integer packet,j
	
	packet=10000 !number of MC packets
	Rmax=200.
	TAUmax=100.
	open(6, file='test.dat')

	do j=1, packet
		x=0.
		y=0.
		z=0.
		distance=0.
		counts=0.
		weight=1.
		do while((x*x+y*y+z*z)<(1.))
			TAU=-log(Xi)
			call random_number(Xi)
			s=TAU/TAUmax
			x0=x
			y0=y
			z0=z
			call scatter(Xi)
			x=x+s*nx
			y=y+s*ny
			z=z+s*nz
			
			!if photon packet escapes
			if ((x*x+y*y+z*z)>1.) then
				!use previous and current positions to calculate 
				!distance to exit point
				a = (x-x0)**2. + (y-y0)**2. + (z-z0)**2.
				b = 2.*( x0*(x-x0) + y0*(y-y0) + z0*(z-z0))
				c = x0**2. + y0**2. + z0**2. - 1.
				quad=b*b-4.*a*c
				mu1=(-b+sqrt(quad))/(2*a)
				
				del=mu1*s				
				distance=distance+del
			else
			!otherwise add distance travelled
				distance=distance+s
			endif
		
		enddo
		!print out the time it took for jth photon packet to escape in days 
		print*, distance*Rmax*1.496E11/(24*3600*3E8)
	enddo	
	end

! 	scattering light
	subroutine scatter(Xi)
	use coord

	call random_number(Xi)
	phi=2.*PI*Xi
	call random_number(Xi)
	theta=acos(2*Xi-1)

	nx=sin(theta)*cos(phi)
	ny=sin(theta)*sin(phi)
	nz=cos(theta)

	return
	end
	
	

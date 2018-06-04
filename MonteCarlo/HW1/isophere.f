	module coord
	real x,y,z,nx,ny,nz,theta,phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program isotrope sphere
	use coord
	implicit none

	real Xi,s,Rmax,TAUmax,TAU,sigma,step,avgscatt,scatters,i,n
	real distance, albedo, counts
	integer packet,j

	albedo=1.
	packet=10000 !number of MC packets
	Rmax=1.
	TAUmax=.1
	step=1.
	sigma=1.
	i=.5
	n=1.
	TAU=1.
	open(6, file='test.dat')
	counts=0
	do while (taumax<10.)
		scatters=0.
		do j=1, packet
			x=0.
			y=0.
			z=0.
			distance=0.
			do while((x*x+y*y+z*z).lt.(1.))
				call random_number(Xi)
				TAU=-log(Xi)
				s=TAU*Rmax/TAUmax

				call scatter(Xi)
				x=x+s*nx	!calculate new position
				y=y+s*ny
				z=z+s*nz
				scatters=scatters+1
				distance=distance+s
				

			enddo
		enddo
		avgscatt=scatters/packet
		print*, TAUmax, avgscatt
		!print*, distance*1.496E11/(24*3600*3E8)
		taumax=taumax+step
		!print*, counts
	enddo	
	stop 
	end
	



! scattering light
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
	
	

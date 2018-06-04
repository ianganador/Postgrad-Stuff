	module coord
	real x, y, z, nx, ny, nz, theta, phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program isotrope sphere
	use coord
	implicit none

	real Xi,s,Rmax, taumax, tau,sigma,step, avgscatt, scatters,i, mu
	integer Ntaus, Nmc,j

	Ntaus=25	!number of optical depths to loop over
	Nmc=100000	
	Rmax=1.		
	taumax=0.	!starting taumax
	step=.1		!taumax step size
	sigma=1.	!interaction cross section
	i=.5		!
	!open(6, file='scattau.dat')
	
	do while (taumax<10.)
		scatters=0.
		taumax=taumax+1
		do j=1, Nmc
			x=0.
			y=0.
			z=0.
			call random_number(Xi)
			mu=sqrt(Xi)
			do while((z).lt.(1.))
				call random_number(Xi)
				tau=-log(Xi)
				s=tau/taumax
				call scatter(Xi)
				z=z+s*nz
				x=x+s*nx
				y=y+s*ny
			!	if(z<0.)then
			!		goto 1
			!	endif
				scatters=scatters+1
			enddo
		print*, taumax, phi
		enddo
		avgscatt=scatters/Nmc
		print*, taumax, phi

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
	
	

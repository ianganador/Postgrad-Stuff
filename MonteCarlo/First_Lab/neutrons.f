	module coord
	real x, y, z, nx, ny, nz, theta, phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program isotrope sphere
	use coord
	implicit none

	real Xi,s,Rmax, taumax, tau,sigma,step, avgscatt, scatters,i
	integer Ntaus, Nmc,j

	Ntrials=25
	Nmc=1000
	Rmax=1.
	taumax=1.
	step=.5
	sigA=.1
	sigS=4.
	sigF=1.
	i=.5
	open(6, file='scattau.dat')
	
	do while (i<Ntrials)
		taumax=i*sigma*Rmax
		scatters=0.
		do j=1, Nmc
			x=0.
			y=0.
			z=0.
			do while((x*x+y*y+z*z).lt.(Rmax**2))
				call random_number(Xi)
				tau=-log(Xi)
				s=tau*Rmax/taumax
				call scatter(Xi)
				z=z+s*nz
				x=x+s*nx
				y=y+s*ny
				scatters=scatters+1
			enddo
		enddo
		avgscatt=scatters/Nmc
		print*, taumax, avgscatt
		i=i+step
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
	
	

	module coord
	real x, y, z, nx, ny, nz, theta, phi
	real,parameter:: pi=4.*atan(1.)
	end module

	program sphere
	use coord
	implicit none	

	integer seed, Nmc, i
	real ran2, prob, tau, taumax, n, sigma, rmax, ran1, ran3,l
	real nscatt, avgscatt
	!open(unit=1,file="scatterdata")
	n = 0.5
	sigma = 1.
	rmax = 10.
	Nmc = 100
	seed = -99

	do while (n<10)
		taumax = n*sigma*rmax
		nscatt=0.
		do i=1, Nmc
			x=0.
			y=0.
			z=0.
			do while((x**2 + y**2 + z**2).lt.(rmax**2))
			
				ran1=ran2(seed)
				ran3=ran2(seed)
				call scatter(ran1,ran3)
				tau = -log(ran2(seed))
				l=(rmax/taumax) * tau
				x=x+(nx*l)
				y=y+(ny*l)
				z=z+(nz*l)
				nscatt=nscatt+1
			end do
		end do
		avgscatt=nscatt/Nmc
		!print*, avgscatt
		print*,taumax,avgscatt
		n=n+0.5
	end do
	end program

	subroutine scatter(ran1, ran3)
	use coord
	real ran1, ran3
	theta=acos(2*ran1 - 1)
	phi=ran3*2*pi 

	nx = sin(theta)*cos(phi)
	ny = sin(theta)*sin(phi)
	nz=cos(theta)
	end subroutine

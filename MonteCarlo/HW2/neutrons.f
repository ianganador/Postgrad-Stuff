	module coord
	real x, y, z, nx, ny, nz, theta, phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program neutron transport
	use coord
	implicit none

	real Xi,s, tau,sigA,sigF,sigS,sigT
	real ro, mass, radius,p2,p3,p, n_Ur, keff
	integer NGen, Nneutron,j,i,k, absorb, ibank, scatters, current
	integer next, v, q
	real, allocatable :: xbank(:,:), ybank(:,:), zbank(:,:)

	NGen=100	!number of generations
	Nneutron=1000000		!number of neutrons

	sigA=.1E-24	!absorption cross section in cm^2
	sigS=4.2E-24	!scattering cross section in cm^2
	sigF=1.3E-24	!fission cross section in cm^2
	sigT=sigA+sigS+sigF	!total interaction cross section
	
	ro=19.1
	mass=60000.
	radius=((mass/ro)*(.75/pi))**(1./3.)
	n_Ur=ro*(6.023E23/235)
	

	i=0			!iteration index
	p2=.56
	p3=.44
	open(6, file='cri60d.dat') !open file for output

	allocate(xbank(Nneutron*10,2))
	allocate(ybank(Nneutron*10,2))
	allocate(zbank(Nneutron*10,2))	
	do i=1,Nneutron*10
		do k=1,2
			xbank(i,k)=0
			ybank(i,k)=0
			zbank(i,k)=0
		enddo
	enddo
	ibank=1
	do i=1,NGen
	
		scatters=0
		absorb=0
		ibank=1
		do j=1, Nneutron

			if(mod(i,2)==0)then
				current=1
				next=2
			else
				current=2
				next=1
			endif
			if (i==1) then
				x=0.
				y=0.
				z=0.
				!do while((x*x+y*y+z*z)>1.)
				!	call random_number(Xi)
				!	x=1.-2.*Xi
				!	call random_number(Xi)
				!	y=1.-2.*Xi
				!	call random_number(Xi)	
				!	z=1.-2.*Xi
				!enddo
			else 
				x=xbank(j,current)
				y=ybank(j,current)
				z=zbank(j,current)
			endif
			
			call random_number(Xi)
			tau=-log(Xi)
			s=tau/(sigT*n_Ur*radius)
			
			call scatter(Xi)
			z=z+s*nz
			x=x+s*nx
			y=y+s*ny
			do while((x*x+y*y+z*z)<(1.))
				call random_number(Xi)
				tau=-log(Xi)
				s=tau*3.72/radius
				
           			call random_number(Xi)
				if (Xi<(sigA/sigT))then
					!absorb=absorb+1
					exit
				elseif(Xi<(sigA+sigS)/sigT)then
					call scatter(Xi)
					z=z+s*nz
					x=x+s*nx
					y=y+s*ny
					scatters=scatters+1
				else
					call random_number(Xi)
					if(Xi<p2)then
						do k=1,2
							ibank=ibank+1
							xbank(ibank,next)=x
							ybank(ibank,next)=y
							zbank(ibank,next)=z
						enddo
						exit
					elseif(Xi<(p2+p3))then
						do k=1,3
							ibank=ibank+1
							xbank(ibank,next)=x
							ybank(ibank,next)=y
							zbank(ibank,next)=z
						enddo
						exit
					endif
				endif
			enddo
		enddo
	keff=float(ibank)/float(Nneutron)
	print*, i, ibank,keff
	if (ibank<Nneutron)then
		q=Nneutron-ibank
		do v=q,Nneutron
			ibank=ibank+1
			xbank(ibank,next)=xbank(v,next)
			ybank(ibank,next)=ybank(v,next)			
			zbank(ibank,next)=zbank(v,next)
		enddo
	endif
	enddo	

	stop 
	end


! scattering light
	subroutine scatter(Xi)
	use coord
	
	call random_number(Xi)
	phi=2.*PI*Xi
	call random_number(Xi)
	theta=acos(2.*Xi-1.)

	nx=sin(theta)*cos(phi)
	ny=sin(theta)*sin(phi)
	nz=cos(theta)

	return
	end

	
	
	
	
	
	
	
	
	
	
	
	
	

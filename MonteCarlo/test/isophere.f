	module coord
	real x,y,z,nx,ny,nz,theta,phi
	real,parameter:: pi=4.*atan(1.)
	end module	

	program isotrope sphere
	use coord
	implicit none

	real Xi,s,TAUmax,TAU,scatters, a2, TAU2
	real distance, albedo
	integer packet,j, lambda, count, count2
	count=0
	count2=0

	albedo=.65	!albedo_1
	packet=1E6 	!number of MC packets
	TAUmax=3.0	!tau_1
	TAU2=1.0
	a2=.55


	do j=1, packet
		x=0.
		y=0.
		z=0.
		lambda=1	!toggle variable
		do while((x*x+y*y+z*z).lt.(1.))
			call random_number(Xi)
			TAU=-log(Xi)
			s=TAU/TAUmax
			x=x+s*nx	!calculate new position
			y=y+s*ny
			z=z+s*nz
			call random_number(Xi)
			if((Xi<albedo).and.(lambda==1))then	!if lambda_1 and <albedo, scatter
				call scatter(Xi)		
			elseif((Xi>albedo).and.(lambda==1))then	!if lambda_1 and >albedo, absorb and process
				albedo=a2
				TAUmax=TAU2
				lambda=2
			elseif((Xi<albedo).and.(lambda==2))then !if lambda_2 and < albedo_2, scatter
				call scatter(Xi)
			else
				exit				!if lambda_2 and > albedo_2, terminate
			endif	
		enddo
		if(lambda==1)then	
			count=count+1
		else
			count2=count2+1
		endif
	enddo
	print*, float(count)/float(packet), float(count2)/float(packet) !print fraction of escaping lambda_1, lambda_2 respectively

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
	
	

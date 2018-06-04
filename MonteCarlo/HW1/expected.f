	program isotrope sphere
	implicit none

	real x,y,i
	i=0
	open(6, file='expected.dat')
	do while (i<100)
		x=i
		y=x + x*x/2
		print*,x,y
		i=i+.01
	enddo
	end


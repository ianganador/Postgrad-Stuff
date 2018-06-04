	program power spectrum
	real X1, X2, X3, X4
	integer i
	integer, allocatable :: narray(:)
	open(6, file='test.dat')
	
	do i=0,100000
		call random_number(X1)	
		call random_number(X2)	
		call random_number(X3)	
		call random_number(X4)	
		x=-log(X1*X2*X3*X4)
		print*,x
	enddo
	end

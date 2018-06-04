	program optical
	implicit none 

c	define variables
	real*8 p, tau, r
	integer i, N, hits, counter

c	uncomment this block and write in loop for full output to file
!	open file, set hits=0
	open(6, file='taus.dat')
	hits=0
	counter=0
	N=10000

c	execute
	do i=1, N
		call random_number(r) 
		tau=-log(r)
        	print *, tau
		
	enddo
 	stop
 	end	

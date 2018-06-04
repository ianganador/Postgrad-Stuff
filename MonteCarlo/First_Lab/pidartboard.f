c	monte carlo method for pi: throwing darts
	program darts
	implicit none

c	define variables
	real*8 pi, x, y, r
	integer i, N, hits, counter

c	uncomment this block and write in loop for full output to file
!	open file, set hits=0
!	open(6, file='dartguess.dat')
	hits=0
	counter=0
	N=1000

c	execute
	do i=1, N
		call random_number(r) 
		x = r*2-1
		call random_number(r)
		y = r*2-1
        	counter=counter+1
		if ((x*x + y*y) .lt. 1) then
			hits = hits+1
		endif
		pi = 4.0 * hits/real(i)
	 
!		write(6,*) pi, hits, counter

	enddo
	print*, "estimate=", pi, "hits=", hits, "N=", counter
	stop
	end

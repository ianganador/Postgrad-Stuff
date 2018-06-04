c	monte carlo method for pi: buffon
	program buffon
	implicit none

c	define variables
	real*8 pi, s, l, x, theta, p,r, y
	integer i, N, hits, counter
	
	hits=0.
	N=100000
	s=4.
	l=1.
	
	
c	execute
	do 2 i=1, N
		call random_number(r) 
		x = r*s/2.
		call random_number(r)
		theta = r*.5*3.14159
		p=.5*sin(theta)
		
		if (x.le.p) then
			hits = hits+1
		endif
!		pi = 2 * real(i)/hits
!		write(6,*) pi


2 	continue
	pi = real(i)/hits
	write(6,*) pi
 	stop
 	end

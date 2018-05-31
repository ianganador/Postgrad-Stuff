#include <stdlib.h>
#include <stdio.h>
#include <math.h>
// Box Muller RNG with gaussian selected random number 
// input:standard deviation, mean of gaussian
// output:random gaussian number
double boxy(double stdv, double me){  
	double x, y, r, G1, G2;
	do{
		x=2.*drand48()-1.; //random number 0-1.
		y=2.*drand48()-1.; //random number 0-1.
		r=x*x+y*y; 
	}
	while(r>=1.);
	r=sqrt((-2.*log(r))/r);
	G1=x*r;
	G2=y*r;
	return(me+G1*stdv);
}

// Exponential RNG
// input:exponential lambda
// output: random exponential number
double exporand(double tau){
	double x;
	x = drand48();
	return -log(1-x)/tau;
}

// Uniform RNG
// input:upper limit, lower limit of boxcar
// output: random uniform number
double unirand(double ul, double ll){
	double stretch, x;
	stretch=ul-ll;
	x=(stretch*drand48())+ll;
	return x;
}

#include <stdio.h>
#include <stdlib.h>

float * randomizer(int N, int seed)
{	
	float * number = malloc(sizeof(int) * N);
	int i; //dummy var
	float ul=1., ll=0.; //upper limit and lower limit of boxcar
	float stretch=ul-ll; //range of numbers
	
	srand48(seed);
	for (i=0 ; i<N ; i++){
		number[i]=(stretch*drand48())+ll;
		}
	
	return number;
}

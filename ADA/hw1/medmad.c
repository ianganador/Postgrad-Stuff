#include<stdlib.h>
double median(int n, double *x) {
	double holder;
	int i, j;
    	//sort array
	for(i=0; i<n-1; i++) {
		for(j=i+1; j<n; j++) {
			if(x[j] < x[i]) {
				holder = x[i];
				x[i] = x[j];
				x[j] = holder;
			}
		}
	}
	//if array is even, take midpoint between closest values
	if(n%2==0) {
		return((x[n/2] + x[n/2-1]) / 2.0);
	} 
	else {
        //otherwise return median
		return x[n/2];
	}
}
double made(int n, double *x, double med){
	double mad=0.;
	int i;
	for(i=0;i<n;i++){
		mad=mad+abs(x[i]-med);
	}
	return mad/(n);
}

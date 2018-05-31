#include <stdio.h>
#include <stdlib.h>
#include<math.h>
//Median Calculator
//input:size of array, array
//output: median of given array
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
//MAD Calculator
//input:size of array, array, median
//output: MAD of given array
double made(int n, double *x, double med){
	double mad=0.;
	int i;
	for(i=0;i<n;i++){
		mad=mad+abs(x[i]-med);
	}
	return mad/(n);
}
//Mean Calculator
//input:size of array, array
//output:mean of given array
double mean(int n, double *x){
	double ave=0;
	int i;
	for(i=0;i<n;i++){
		ave+=x[i];
	}
	ave=ave/n;
	return ave;
}
//Mean Calculator
//input:size of array, array, mean
//output:variance of array
double variance(int n, double *x, double ave){
	double diff=0;
	double var=0;
	int i;
	for(i=0;i<n;i++){
		diff=(x[i]-ave)*(x[i]-ave);
		var+=diff;
	}
	var=var/(n-1);
	
	return var;
}
//Moment Calculator
//input:size of array, array, mean, standard deviation, moment order
//output:specifiedd moment of given array
double moment(int n, double *x, double ave, double sig, int m){
	double diff=0;
	double mom=0;
	int i;
	for(i=0;i<n;i++){
		diff=pow(((x[i]-ave)/sig),m);
		mom+=diff;
	}
	mom=mom/n;
}







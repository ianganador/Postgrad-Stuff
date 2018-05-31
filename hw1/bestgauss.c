#include <stdlib.h>
#include <stdio.h>
#include <math.h>
double boxy(double stdv, double mean);
double mean(int n, double *x);
double variance(int n, double *x, double ave);
double median(int n, double *x);

int main(){
	FILE *fp;
	int i, N, randtype, seed, M,j,k, P;
	double me, stdev, x, keeper;
	M=100;
	double samplemean[M], media[N], medium[M];
	P=100;
	N=1;	//number of samples
	seed=1;
	srand(seed); 	// set seed
	me=0.;	//set gauss mean
	stdev=1.;	//set gauss stdev

	char data[20];  //file writing
	sprintf(data, "monteavesample.dat");  
	fp=fopen(data,"w");
	for(k=0;k<P;k++){
		for(j=0;j<M;j++){
			keeper=0;
			
			for(i=0; i<N; i++){
					x=boxy(stdev,me);
					keeper+=x;
					media[i]=x;
			}
			samplemean[j]=keeper/N;
			medium[j]=median(N,media);
		}
		double Xave=mean(M, samplemean);
		double varXave=variance(M, samplemean, Xave);
		//double meanXmed=mean(M,medium);
		//double varXmed=variance(M,medium, meanXmed);
		fprintf(fp,"%lf %d\n", sqrt(varXave), N);
		N++;
	}
}

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



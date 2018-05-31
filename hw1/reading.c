#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double mean(int n, double *x);
double variance(int n, double *x, double ave);
double median(int n, double *x);
double made(int n, double *x, double med);
double variance(int n, double *x, double ave);
double moment(int n, double *x, double ave, double sig, int m);
int main(){
	int n=100000, i, lines=0;
	double bias[n], x[n], y[n];
	double ave=0, var=0,med=0,mad=0, skew, kurt;
	int ch;

	FILE *file = fopen("0_1000000.dat", "r");
	for (int i = 0; i < n; i++){
    		if (feof(file))
        		break;
    		fscanf(file, "%lf %lf %lf", &(x[i]), &(y[i]), &(bias[i]));
	}

	ave=mean(n,bias);
	var=variance(n,bias,ave);
	//med=median(n,bias);
	//mad=made(n,bias,med);
	skew=moment(n,bias,ave,sqrt(var),3);
	kurt=moment(n,bias,ave,sqrt(var),4);

	printf("mean=%lf\nvariance=%lf\nskew=%lf\nkurtosis=%lf\n",ave , var, skew, kurt);
	fclose(file);
}


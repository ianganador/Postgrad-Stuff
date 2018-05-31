#include <stdlib.h>
#include <stdio.h>
#include <math.h>
//RNGs 
double unirand(double ul, double ll);
double boxy(double stdv, double me);

int main(){
	double P, Kc, Vsini, cosi,i,X, B,C,q,Fx, Mx, Mc;
	// initialize everything, including file writing
	int k;
	FILE *fp;
	char data[20];
	sprintf(data, "test.dat");  
	fp=fopen(data,"w");
	srand(10);
	//loop over k trials and generate a data set of Mx, Mc
	for(k=0; k<100000; k++){
		P=boxy(.0001,6.4714)*3600*24;
		Kc=boxy(.7,208.5);
		Vsini=boxy(1.1,38.8);
		cosi=unirand(.643296,.173648);// uniform cosi between 50 and 80 degrees
		i=acos(cosi);
		
		//geting q parameter from cubic
		X=pow((Vsini/(Kc*.462)),3.);
		B=(3.*sqrt(3.)*sqrt(27.*X*X+4.*X)+27.*X+2.)/2.;
		C=pow(B,1./3.);
		q=((C+1./C)-2.)/3.;
		
		//plugging q into F, Mx, Mc calculations
		Fx=pow(Kc,3.)*P/(2.*M_PI*6.67E-20)/2E30;
		Mx=pow((1.+q),2.)*Fx/pow(sin(i),3.);
		Mc=Mx*q;
		fprintf(fp,"%lf %lf\n", Mx, Mc);
	}
}

	

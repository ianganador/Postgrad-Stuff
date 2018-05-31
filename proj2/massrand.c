#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double unirand(double ul, double ll);
double boxy(double stdv, double me);

int main(){
	double P, K, sini,i,X, B,C,q,F, Mx, M, G;
	G=6.67E-11;
	int k;
	FILE *fp;
	char data[20];
	sprintf(data, "MC_Mx.dat");  
	fp=fopen(data,"w");
	srand(10);
	for(k=0; k<100000; k++){
		P=boxy(.1,8.3)*3600;
		K=boxy(8.9,510)*1000;
		sini=unirand(.866,.9848);// uniform cosi between 50 and 80 degrees	
		M=unirand(.3,.6);
		
		F=pow(K,3.)*P/(2.*M_PI*G)/1.99E30;
		F=F/pow(sini,3.);

	
	
		Mx=pow((2.*pow(F,3.)+18.*F*F*M+3.*sqrt(3.)*sqrt(4.*pow(F,3.)*pow(M,3.)+27.*F*F*pow(M,4.)) + 27.*F*M*M),1./3.)/(3.*pow(2.,1./3.)) - (pow(2.,1./3.)*(-729.*F*F - 4374.*F*M))/(2187.*pow((2.*pow(F,3.) + 18.*F*F*M + 3.*sqrt(3.)*sqrt(4.*pow(F,3.)*pow(M,3.) + 27.*F*F*pow(M,4.)) + 27.*F*M*M),1./3.)) + F/3.;

		fprintf(fp,"%lf\n", Mx);

	}
}

	

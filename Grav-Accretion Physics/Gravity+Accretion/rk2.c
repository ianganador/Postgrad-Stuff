#include <stdio.h>
#include <math.h>

/*----------------------------------------------------------------------------
Author:Ian Winner
To compile: gcc two_body.c -o executable -lm

Notes: 
1) Set flag=0 for a 1st Order Eulerian integration method,
flag=1 for 2nd Order Runge Kutta.
2) For this project all calculations and outputs are in code units,
to change to physical: modify Mscale, Rscale, and G appropriately and multiply 
outputs by scale factors.
3) 
-----------------------------------------------------------------------------*/
void RK2(double t, double m, double h, double var[6]); 
double f(double t, double m, double var[6], int i);
void Euler(double t, double m, double h, double *var);
int main(){ 
	FILE *fp;
	double ti,tf,t,z,y,x,vz,vx,vy,h,m; //initial t, final t, t, position vars, velocity vars, timestep var, point mass value
	double Rscale, G, Mscale, tscale,Vscale; //scale factors
	double rtemp, abserror, bank;
	int n, flag;	
	m=1.; //initial point mass in solar units
	ti=0.; //initial time=0
	tf=16.; //final t in code units
	
	flag=0; //0 for euler, 1 for rk
	
 	if (flag==0){ 
		fp=fopen("keplereuler.dat", "w");
	}
	else{
		fp=fopen("keplerrk2.dat", "w");
	}
	
	x=1.; 
	y=0.; 	//initial position coords 
	z=0.; 
	vy=1.; 	
	vz=0.; 	//initial velocity magnitudes
	vx=0.; 	 
	double var[6]={x,y,z,vx,vy,vz}; //initialize variables array
	
	n=pow(2,10);		//number of steps
	h=(tf-ti)/(double)n;  	//size of step
	printf("%lf\n", h);		//print step size check

	t=ti; 	//set t at t-init
	
	bank=0;	//initialized variables for error analysis
	rtemp=0;
	abserror=0;
	
	Mscale=1.; //1.99E30; uncomment values for earth/sun scale system in mks
	Rscale=1. ;//1.496E11;
	G=1. ;//6.674E-11;
	tscale=pow(pow(Rscale,3)/(G*Mscale),.5);
	Vscale=Rscale/tscale;
	
	

	while(t<tf){ 	//loop over t until final t

		if (flag==0){ 
			Euler(t,m,h,var); 	//1st order euler
		}
		else{
			RK2(t,m,h,var); 	//2nd order Runge Kutta
		}
		//calculations for error comparisons (only works for circular orbit)
		//rtemp=(var[0]*var[0]+var[1]*var[1]+var[2]*var[2]);
		//abserror=fabs(1.-rtemp);
		//bank=bank+abserror;
		

		t+=h; 				//increase time
		fprintf(fp,"%.10lf %lf %lf %lf %lf %lf %lf\n",t,var[0],var[1],var[2],var[3],var[4],var[5]);
	}
	fclose(fp);
}
void Euler(double t, double m, double h, double *var){ 
	double fuvar[6];	//full step variables
	int i;  		//index over variables

	for(i=0;i<6;i++){	//loop over variables
		fuvar[i]=var[i]+h*f(t, m, var, i); 	//evaluate each full step increase
		var[i]=fuvar[i];			 //set new var to evaluated full step
	}
}

void RK2(double t, double m, double h, double *var){ 
	double havar[6];		//half step variables
	double fuvar[6];		//full step variables
	int i;  			//index over variables

	for(i=0;i<6;i++){		//loop over variables
		havar[i]=var[i]+.5*h*f(t, m, var, i);	 //evaluate each half step increase   
	}
	for(i=0;i<6;i++){		//loop over variables
		var[i]=var[i]+h*f(t+h/2, m, havar, i);	 //evaluate each full step increase including half-step weight
	}
}

double f(double t,double m, double var[6], int i){ //derivatives
	double x=var[0];	 //setting variables for readability in terms of x, x', x''
	double y=var[1];
	double z=var[2];
	double vx=var[3];
	double vy=var[4];
	double vz=var[5];
	if (i==0){ 		//if evaluating new x
		return vx; 	//return x'
	}
	if (i==1){ 		//if evaluating new y
		return vy; 	//return y'
	}
	if (i==2){ 		//if evaluating new y
		return vz;	//return z'
	}
	if (i==3){					//if evaluating new Vx
		return -x*m/pow(x*x+y*y+z*z, 1.5); 	//return Vx'
	}
	if (i==4){ 					//if evaluating new Vy
		return-y*m/pow(x*x+y*y+z*z,1.5);	//return Vy'
	}
	if (i==5){ 					//if evaluating new Vy
		return-z*m/pow(x*x+y*y+z*z,1.5); 	//return Vz'
	}
}

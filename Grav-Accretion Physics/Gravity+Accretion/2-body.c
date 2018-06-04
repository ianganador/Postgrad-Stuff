#include <stdio.h>
#include <math.h>

void RK2(double t, double m, double h, double var[6]); 
double f(double t, double m, double var[6], int i);
void Euler(double t, double m, double h, double *var);
int main()
{ 
  FILE *fp;
  double ti,tf,t,z,y,x,vz,vx,vy,h,m;
  double Rscale, G, Mscale, tscale,Vscale, time;
  int n, flag;	
  
  flag=1; //0 for euler, 1 for rk
  m=1.; //initial point mass in solar units
  ti=0.; //initial time=0
  tf=6.5; //final t in code units
  y=0.; //initial y in AU
  z=0.; //initial z in AU
  x=1.; //intial x in AU
  vy=1.; //initial vy
  vz=0.; //initiazl vz 
  vx=0.; //initial vx 
  n=1000; //how many time steps (higher = more accurate but slower)
  h=(tf-ti)/(double)n;  //size of step
  printf("%lf\n", h);
  double var[6]={x,y,z,vx,vy,vz}; //initialize variables array
  t=ti; //set t at t-init
  
  //scaling relations for converting output from code units to physical
  Mscale=1;//1.99E30;
  Rscale=1;//1.496E11;
  G=1;//6.674E-11;
  tscale=pow(pow(Rscale,3)/(G*Mscale),.5);
  Vscale=Rscale/tscale;
  if (flag==0){ 
    fp=fopen("orbitdataeuler.dat", "w");
    }
  else{
    fp=fopen("orbitdatark2.dat", "w");
  }
  //fp=fopen("orbitdataeuler.dat", "w");
  while(t<tf) //loop over t until final t
    {
	if (flag==0){ 
		Euler(t,m,h,var); //1st order euler
	}
	else{
		RK2(t,m,h,var); //2nd order Runge Kutta
	}

	t+=h; //increase time
	
	//convert variables to physical units and print to file
	x=var[0]*Rscale;
	y=var[1]*Rscale;
	z=var[2]*Rscale;
	vx=var[3]*Vscale;
	vy=var[4]*Vscale;
	vz=var[5]*Vscale;
	time=t*tscale;
	
	fprintf(fp, "%lf %lf %lf %lf %lf %lf %lf\n", time, x,y,z,vx,vy,vz);
    }
  fclose(fp);
}

void Euler(double t, double m, double h, double *var)
{ 
  double fuvar[6];//full step variables
  int i;  //index over variables
  
  for(i=0;i<6;i++){//loop over variables
     fuvar[i]=var[i]+h*f(t, m, var, i); //evaluate each full step increase
     var[i]=fuvar[i]; //set new var to evaluated full step
    }
}

void RK2(double t, double m, double h, double *var){ 
  double havar[6];//half step variables
  double fuvar[6];//full step variables
  int i;  //index over variables
  
  for(i=0;i<6;i++){//loop over variables
      havar[i]=var[i]+.5*h*f(t, m, var, i); //evaluate each half step increase   
    }
  for(i=0;i<6;i++){//loop over variables
     fuvar[i]=var[i]+h*f(t+h/2, m, havar, i); //evaluate each full step increase
     var[i]=fuvar[i]; //set new var to evaluated full step
    }
}

double f(double t,double m, double var[6], int i){ //derivatives
	double x=var[0];
	double y=var[1];
	double z=var[2];
	double vx=var[3];
	double vy=var[4];
	double vz=var[5];
	if (i==0){ //if evaluating new x
			return vx; //return x
		 }
	if (i==1){ //if evaluating new y
			return vy; //return y
		 }
	if (i==2){ //if evaluating new y
			return vz; //return z
		 }
	if (i==3){ //if evaluating new Vx
			return -x*m/pow(x*x+y*y+z*z, 1.5); //return Vx
		 }
	if (i==4){ //if evaluating new Vy
			return-y*m/pow(x*x+y*y+z*z,1.5); //return Vy
		 }
	if (i==5){ //if evaluating new Vy
			return-z*m/pow(x*x+y*y+z*z,1.5); //return Vy
		 }
}

#include<stdio.h>
#include<math.h>

int main(){
int n,i;
scanf("%d",&n);
char motif[n];
float time[n];
i=0;
while(i<n){
scanf("%f",&time[i]);
i++;

}
i = 0;
char c;
while(i<n){
scanf("%c",&c);
if(c == '\n') continue;
else{
	motif[i] = c;
	i++;
	}
}
//for(i=0;i<n;i++){
//printf("%c	%f\n",motif[i],time[i]);
//}
int maxtime = floor(time[n-1]) + 1;
char timestamp[maxtime];
int j = 0;
timestamp[0] = 'Z';
for(i=1;i<maxtime;i++){
	//printf("%d\n",i);
	if(floor(time[j]) >= i){
		timestamp[i] = 'Z';
		 //printf("if %d %d %f\n",i,j,time[j]);
	}	
	else{
		while(floor(time[j]) < i){
			j++;
		}
		j--;
		//printf("else%d %d %f\n",i,j,time[j]);
		timestamp[i] = motif[j];	
	}
}

for(i=0;i<maxtime;i++){
	printf("%d	%c\n",i+1,timestamp[i]);
}

return 0;
}

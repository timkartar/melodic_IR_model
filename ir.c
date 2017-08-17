#include<stdio.h>
#include<math.h>
char findirtype(int a, int b, int c);

int main(){
	int n,i;
	scanf("%d",&n);
	int arr[n];
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	i = 0;
	char irarr[n-2];
	while(i < n-2){
		irarr[i] = findirtype(arr[i],arr[i+1],arr[i+2]);
		printf("%c\n",irarr[i]);
		i++;
	}

	return 0;
}
char findirtype(int a,int b, int c){
	int i1 = b - a;
	int i2 = c - b;
	if(i1 == 0 && i2 == 0) return 'A'; // D --> A  
	if(i1 == 0 && i2 != 0) return 'B'; // (D) --> B doubtful :-(
	if(abs(i1) < 6){ //can be P,(R),IP,VP,(IR),(VR),ID
		if(abs(i2) < 6){
			//can be P, IP,ID,(IR),(R)
			if(i1 + i2 == 0) return 'C'; // ID --> 2
			if((i2 < 0 && i1 < 0) || (i2 > 0 && i1 > 0) && abs(i1 - i2) > 3) return 'H';//(IR)
			if((i2 <= 0 && i1 > 0) || (i2 >= 0 && i1 < 0) && abs(abs(i1) - abs(i2)) > 3) return 'F';//(R)
			if((i2 <= 0 && i1 > 0) || (i2 >= 0 && i1 < 0)) return 'D'; // IP --> D
			if((i2 < 0 && i1 < 0) || (i2 > 0 && i1 > 0)) return 'E'; // P --> E
		}
		else{
			//can be VP, (VR)
			
			if((i2 < 0 && i1 < 0) || (i2 > 0 && i1 > 0)) return 'G'; // VP -->  G
			if((i2 <= 0 && i1 > 0) || (i2 >= 0 && i1 < 0)) return 'I'; // (VR) -- > I
		}
	}
	else{  // (P),R,(IP),(VP),IR,VR,(ID)
		if((i2 < 0 && i1 < 0) || (i2 > 0 && i1 > 0)){
			//(P),(VP),IR
			if(abs(i2-i1) == 0) return 'J';//(P) --> J
			if(abs(i2) > abs(i1)) return 'K';//(VP) --> K
			if(abs(i2) < abs(i1)) return 'L';//IR --> L
		}
		else{
			//(ID),R,(IP),VR
			if(abs(i2 - i1)==0) return 'M';//(ID) --> M
			if(abs(abs(i2) - abs(i1)) < 3) return 'P';//(IP) --> P
			if(abs(i2) < abs(i1)) return 'N';//R --> N
			if(abs(i2) > abs(i1)) return 'O';//VR --> O
		}		
		
	}
	return '?';
}



#include<iostream>
#include<math.h>
using namespace std;

int check_prime(long int A);  // Function to check the number A is prime or not.

int main(){

    int T;                      // Number of test cases.
    cin>>T;
    while(T!=0){

        long int Num1;
	long int Num2;

	cin>>Num1>>Num2;
	
	for(long int i = Num1;i<=Num2;i++){

	  if(check_prime(i)==1){
	    cout<<i<<"\n";
	  }
	}
	T--;
    }
    return 0;
}

int check_prime(long int A){
  if(A<=1){
    return 0;
  }
  else{

    for(int i =2;i<=sqrt(A);i++){
      if(A%i==0 && A!=i){
	return 0;
      }
    }
    return 1;
  }
}

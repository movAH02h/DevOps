#include <iostream>

int main(){
	long long answ=1, n;
	std::cin >> n;
	for (int i=0;i<n;i++){
		answ *= (i+1);
	}
	std::cout<<answ;
	return 0;
}
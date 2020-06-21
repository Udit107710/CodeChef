#include <bits/stdc++.h>

using namespace std;
const int N = 50000;
bool isPowerOfTwo(long n) 
{ 
   return ((n & (n - 1)) == 0); 
}

bool check_prime(int n){
	for(int i = 2; i < min(N, n); i++)
		if(n % i == 0)
			return 0;
	return 1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--){
        long n;
        cin >> n;
        
        if(n == 1){ cout << "FastestFinger\n"; continue; }
        if(n == 2){ cout << "Ashishgup\n"; continue; }
        
        if(n%2){ cout << "Ashishgup\n"; continue; }
        
        bool r = isPowerOfTwo(n);
        if(r){ cout << "FastestFinger\n"; continue; }
        
        r = (n % 4 != 0 && check_prime(n / 2));
        if(r){ cout << "FastestFinger\n"; continue; }
        else { cout << "Ashishgup\n"; continue; }
    }
    return 0;
}
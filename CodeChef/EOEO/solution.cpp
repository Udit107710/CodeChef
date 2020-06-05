#include <bits/stdc++.h>

using namespace std;

bool isPowerOfTwo(long long n) 
{ 
   if(n==0) 
   return false; 
  
   return (ceil(log2(n)) == floor(log2(n))); 
}

long long CountTrailingZeros(long long n) 
{ 
    bitset<64> bit; 
  
    bit |= n; 
  
    long long zero = 0; 
  
    for (int i = 0; i < 64; i++) { 
        if (bit[i] == 0) 
            zero++; 
        else
            break; 
    } 
  
    return zero; 
} 

int main(){
    long long t;
    cin >> t;
    while(t--){
        long long n;
        cin >> n;

        if(isPowerOfTwo(n)){
            cout << "0\n";
            continue;
        }
        if(n&1){
            cout << (n-1)/2 << "\n";
            continue;
        }
        long long num=0;
        long long x = n;
        num = CountTrailingZeros(n);
        ++num;        
        cout << n/(1<<num) << "\n";
    }

    return 0;
}
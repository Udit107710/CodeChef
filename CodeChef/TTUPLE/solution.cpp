#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){

        long long int p, q, r, a, b, c, sum1, sum2, sum3, prod1, prod2, prod3; 
        int count=0, zeros=0, same=0;
        cin >> p >> q >> r >> a >> b >> c;
        
        if(a == p && b == q && r == c){
            cout << "0\n";
            continue;
        }

        sum1 = a-p;
        sum2 = b-q;
        sum3 = c-r;
        int flag1 = 1, flag2= 1, flag3 = 1;

        if(p != 0 && a%p == 0) prod1 = a/p; else flag1 = 0;
        if(q != 0 && b%q == 0) prod2 = b/q; else flag2 = 0;
        if(r != 0 && c%r == 0) prod3 = c/r; else flag3 = 0;

        if(a == 0) ++zeros;
        if(b == 0) ++zeros;
        if(c == 0) ++zeros;

        if(a == p) ++same;
        if(b == q) ++same;
        if(c == r) ++same; 

        if(same == 2 || zeros == 3 || (sum1 == sum2 && sum2 == sum3) || (prod1 == prod2 && prod2 == prod3 && (flag1 && flag2 && flag3)) || 
        (same == 1 && (sum2 == sum1 || sum2 == sum3 || sum3 == sum1)) || (same == 1 && zeros == 2) || (same == 1 && ((prod3 == prod1 && (flag1 && flag3)) || 
        (prod3 == prod2 && (flag3 && flag2)) || (prod2 == prod1 && (flag1 && flag2))))){
            cout << "1\n";
            continue;
        }
        else if(zeros == 2){
            count = 2;
        }
        else if((sum1 == sum3) || (sum3 == sum2) || (sum1 == sum2)){
            count = 2;
        }
        else if(sum1 + sum2 == sum3 || sum1 + sum3 == sum2 || sum3 + sum2 == sum1){
            count = 2;
        }
         else if((prod3 == prod2 && (flag2 && flag3)) || (prod3 == prod1 && (flag1 && flag3)) || (prod1 == prod2 && (flag1 && flag2))){
             count = 2;
         }
        else if(prod3 * prod2 == prod1  && (flag3 && flag2 && flag1) || prod3 * prod1 == prod2 && (flag3 && flag2 && flag1) || prod2 * prod1 == prod3 && (flag3 && flag2 && flag1)){
            count = 2;
        }
        else if(
            (flag2 && ((sum1 == sum3 + p*prod2) || (sum3 == sum1 + r*prod2) || (sum1 == (sum3+p)*prod2) || (sum3 == (r+sum1)*prod2))) || 
            (flag1 && ((sum2 == prod1*q + sum3) || (sum3 == prod1*r + sum2) || (sum2 == (q+sum3)*prod1) || (sum3 == (r+sum2)*prod1))) || 
            (flag3 && ((sum1 == p*prod3 + sum2) || (sum2 == q*prod3 + sum1) || (sum1 == (p+sum1)*prod3) || (sum2 == (sum1+q)*prod3)))){
            count = 2;
        }
        else if(same == 1){
            count = 2;
        }
        else{
            count = 3;
        }

        cout << count << "\n";
        
    }

    return 0;
}
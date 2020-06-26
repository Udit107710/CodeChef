#include <bits/stdc++.h>

using namespace std;

int gcd(int a , int b){
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

void solve(int a, int b, int c, int d, int &sol, int &numerator, int &denominator ){
    sol = 0;

    float x = float(a)/float(b);
    float y = float(c)/float(d);

    if(x < y){
        sol = 1;
        numerator = (b*c-a*d);
        denominator = (b*c);
        int g = gcd(numerator, denominator);
        numerator = numerator/g;
        denominator = denominator/g;
    }
    else if (x > y){
        sol = 1;
        numerator = (a*d-b*c);
        denominator = (a*d);
        int g = gcd(numerator, denominator);
        numerator = numerator/g;
        denominator = denominator/g;
    }
}


int main(){
    int a, b, c, d;
    int sol=0, numerator, denominator;
    cin >> a >> b >> c >> d;
    solve(a, b, c, d, sol, numerator, denominator);
    if(sol) printf("%d/%d", numerator, denominator);
    else printf("0");
    return 0;
}
#include <bits/stdc++.h>

using namespace std;


long sumDigits(long a){
    long answer =0;

    while(a > 0){
        answer += a%10;
        a = a/10;
    }

    return answer;

}

long long power(int i, int a){
    long answer = 1;
    for(int j=1; j <= a; ++j){
        answer*=i;
    }
    return answer;
}

vector<long long> solve(int a, int b, int c){
    vector<long long> answer;

    for(long i =1; i < 82; ++i){
        long long d = b*power(i, a) + c;
        if(sumDigits(d) == i && d < 1000000000){
            answer.push_back(d);
        }
    }
    return answer;
}

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    vector<long long> result = solve(a, b, c);
    cout << result.size() << "\n";
    for(auto x: result) cout << x << " ";
    return 0;
}
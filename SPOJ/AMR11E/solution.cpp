#include <iostream>
#include <vector>

using namespace std;

vector<int> prime(3000, 0);
vector<int> result;

int main(){
    int t;
    scanf("%d", &t);

    for(int i=2; i < 3000; ++i){
        if (prime[i] == 0){
            for(int j = i*2; j < 3000; j+=i){
                --prime[j];
            }
        }
        if(prime[i]+3 <= 0)
            result.push_back(i);
    }

    while(t--){
        int n;
        scanf("%d", &n);
        printf("%d\n", result[n-1]);
    }       
    return 0;
}
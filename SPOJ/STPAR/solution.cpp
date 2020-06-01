#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    while(n > 0){
        vector<int> array;
        stack<int> s;
        int result[n];
        int x;
        for(int i=0; i <n; ++i){
            cin >> x;
            array.emplace_back(x);
        }
            

        cout << "Hello";
        for(int i=0; i <n; ++i)
            cout << array[i];
        for(int i=0, j = 0; i < n, j < n; ++i, ++j){
            if(j+1 == array[i])
                result[j] = array[i];
            else{
                while(s.top() == j+1){
                    result[j] = s.top();
                    s.pop();
                    ++j;
                }
            }
        }
        if(s.size())
            cout << "no\n";
        else
            cout << "yes\n";
        cin >> n;
    }

    return 0;
}
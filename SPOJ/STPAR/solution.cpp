#include <bits/stdc++.h>

using namespace std;

int main(){

    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);

    int n;
    cin >> n;
    while(n > 0){
        vector<int> array(n);
        stack<int> s;
        int result[n];
        for(int i=0; i < n; ++i){
            cin >> array[i];
        }
        int j, i;
        for(i=0, j = 0; i < n && j < n; ++i, ++j){
            if(j+1 == array[i])
                result[j] = array[i];
            else{
                int flag = 1;
                while(s.size() > 0 && s.top() == j+1){
                    result[j] = s.top();
                    s.pop();
                    flag = 0;
                    ++j;
                }
                if(flag){
                    s.push(array[i]);
                }
                else 
                    --i;
                --j;
            }
        }
        while(s.size() > 0 && s.top() == j+1){
            result[j] = s.top();
            s.pop();
            ++j;
        }
        
        if(s.size())
            cout << "no\n";
        else
            cout << "yes\n";
        cin >> n;
    }

    return 0;
}
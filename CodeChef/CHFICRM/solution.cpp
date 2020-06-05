#include <bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin >> t;
    while(t--){
        map<int, int> record;
        record.insert(pair<int, int>(5, 0));
        record.insert(pair<int, int>(10, 0));
        record.insert(pair<int, int>(15, 0));

        int n;
        cin >> n;
        int flag=0;
        for(int i=0; i < n; ++i){
            // cout << record[5] << " " << record[10] << " " << record[15] << "\n";
            int p;
            cin >> p;
            
            if(p == 5){
                ++record[5];
                continue;
            }

            if(p == 10){
                if(record[5] > 0){
                    --record[5];
                    ++record[10];
                    continue;
                }
            }

            if(p == 15){
                if(record[10] > 0){
                    --record[10];
                    ++record[15];
                    continue;
                }
                if(record[5] >= 2){
                    record[5]-=2;
                    ++record[15];
                    continue;
                }
            }
            flag = 1;
        }
        if(flag)
            cout << "NO\n";
        else
            cout << "YES\n";
    }
    
    return 0;
}
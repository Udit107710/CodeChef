#include <bits/stdc++.h>

using namespace std;

int main(){
    int a, b;
    set<int> heads;
    set<int> tails;
    cin >> a >> b;
    while(b--){
        for(int i=0; i<a; ++i) tails.emplace(i);
        int op, c, d;
        cin >> op >> c >> d;
        if(op == 1){
            int count = 0;
            for(int i=c; i <= d; ++i){
                if(heads.find(i) != heads.end())
                    count++;
            }
            cout << count << "\n";
        }
        else{
            for(int i=c; i <= d; ++i){
                if(tails.find(i) != tails.end()){
                    tails.erase(i);
                    heads.emplace(i);
                }
                else{
                    tails.emplace(i);
                    heads.erase(i);
                }
            }
        }

        cout << "Heads: " << endl;
        for(int x: heads) cout << x << " ";
        cout << endl;

        cout << "Tails: " << endl;
        for(int x: tails) cout << x << " ";
        cout << endl;
        
    }

    return 0;
}
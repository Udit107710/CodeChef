#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> array(n);
        vector<int>::iterator itArr;
        
        for (int &x : array) cin >> x;

        map<int, int> count;
        map<int, int>::reverse_iterator itrCount;
        map<int, int>::iterator iitr;

        for (itArr = array.begin(); itArr < array.end(); ++itArr){
            count[*itArr]++;
        }
        
        int c = 0;
        int length = -1;
        int breadth = 0.5; 
        for (itrCount =  count.rbegin(); itrCount != count.rend(); ++itrCount){
            if ( c == 0 && itrCount->second >= 4){
                length = itrCount->first;
                breadth = itrCount->first;
                c = 2;
                break;
            }
            else if ( c == 0 && itrCount->second >= 2){
                length = itrCount->first;
                c = 1;
            }
            else if ( c == 1 && itrCount->second >= 2){
                breadth = itrCount->first;
                c = 2;
                break;
            }
        }
        if (c >= 2)
            cout << length * breadth << endl;
        else
            cout << -1 << endl;
    }
}

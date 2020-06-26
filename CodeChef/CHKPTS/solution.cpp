#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        long n, c;
        cin >> n >> c;
        vector<pair<long, long>> lines;
        vector<bool> marked(n, false);
        for(int i=0; i < n; ++i){
            int x, y;
            cin >> x >> y;

            lines.push_back(make_pair(x, y));
        }
        sort(lines.begin(), lines.end());
        int checkpoints = 0;
        int operations = 0;
        for(int i=0; i < n; ++i){
            int count = 0;
            int check = 0;
            if(!marked[i]){
                marked[i] = true;
                ++count;
                ++check;
                vector<int> part;
                part.push_back(i);
                for(int j=i+1; j < n; ++j){
                    long xdiff = lines[j].first-lines[i].first;
                    long ydiff = lines[j].second-lines[i].second;
                    if(xdiff == ydiff && xdiff%c == 0){ ++count; marked[j] = true; part.push_back(j);}
                }
                if(count == 1){ operations+=0;}
                else{
                    int mid = part[count/2];
                    pair<long , long> midEl = lines[mid];
                    for(int u: part){
                        operations+= (abs(lines[u].first-midEl.first)/c);
                    }
                }
            }
            checkpoints+=check;
        }

        cout << checkpoints << " " << operations << "\n";

    }

    return 0;
}
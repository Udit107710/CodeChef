#include <bits/stdc++.h>

using namespace std;

bool dfs(vector<vector<char>> &board, string word, int i, int j, int find, vector<vector<bool>> &marked, int n, int m, set<string> &answer){
    if(i >= m || j >= n || i < 0 || j < 0) return false;
    if(!marked[i][j]){
        if(board[i][j] == word[find]){
            if(find+1 == word.size()){ answer.insert(word); return true; }
            else{
                marked[i][j] = true;
                
                bool val1 = dfs(board, word, i, j+1, find+1, marked, n , m, answer);
                if(val1) return true;
                bool val2 = dfs(board, word, i+1, j, find+1, marked, n , m, answer);
                if(val2) return true;
                bool val3 = dfs(board, word, i+1, j+1, find+1, marked, n , m, answer);
                if(val3) return true;
                bool val4 = dfs(board, word, i-1, j+1, find+1, marked, n , m, answer);
                if(val4) return true;
                bool val5 = dfs(board, word, i-1, j, find+1, marked, n , m, answer);
                if(val5) return true;
                bool val6 = dfs(board, word, i, j-1, find+1, marked, n , m, answer);
                if(val6) return true;
                bool val7 = dfs(board, word, i-1, j-1, find+1, marked, n , m, answer);
                if(val7) return true;
                bool val8 = dfs(board, word, i+1, j-1, find+1, marked, n , m, answer);
                if(val8) return true;
                
                marked[i][j] = false;
                return false;  
                 
            }
        }
        else return false;
    }
    else return false;
}

void search(vector<vector<char>> &board, string word, set<string> &answer){
    int m = board.size();
    int n = board[0].size();
    
    bool find = false;
    for(int i=0; i < m; ++i){
        for(int j =0; j < n; ++j){
            vector<vector<bool>> marked(m, vector<bool>(n, false));
            find = dfs(board, word, i, j, 0, marked, n, m, answer);
            if(find) break;
        }
        if(find) break;
    }
}

set<string> boggle(vector<vector<char> >& board,
                      vector<string>& dictionary) {
    vector<string>::iterator itr;
    set<string> answer;
    for(itr=dictionary.begin(); itr != dictionary.end(); ++itr){
        search(board, *itr, answer);
    }
    
    return answer;
}


int main(){
    int t;
    cin >> t;

    while(t--){
        int s;
        cin >> s;
        vector<string> dictionary(s);
        for(string &x: dictionary) cin >> x;

        int n, m;
        cin >> m >> n;
        vector<vector<char>> board(m, vector<char>(n));
        for(int i=0; i < m; ++i){
            for(int j=0; j < n; ++j){
                cin >> board[i][j];
            }
        }
        set<string> r = boggle(board, dictionary);
        if(r.size()) for(string x: r) cout << x <<  " ";
        else cout << "-1";
        cout << "\n";
    }
}
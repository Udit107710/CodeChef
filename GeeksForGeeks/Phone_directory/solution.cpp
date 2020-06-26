#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int ALPHABET_SIZE = 26; 

struct node{
    struct node *children[ALPHABET_SIZE];
    bool endWord;
};

node* getNode(){
    node *n = new node;
    n->endWord = false;
    for(int i=0; i < ALPHABET_SIZE; ++i) n->children[i] = NULL;
    return n;
}

void insert(node *root, string word){
    int n = word.size();
    node *nd = root;
    for(int i=0; i < n; ++i){
        int key = word[i] - 'a';
        if(!nd->children[key]) nd->children[key] = getNode();
        nd = nd->children[key];
    }
    nd->endWord = true;
}

void getWords(node *pnode, string word, vector<string> &words){
    if(pnode->endWord) words.push_back(word);
    for(int i=0; i < ALPHABET_SIZE; ++i){
        if(pnode->children[i]){
            char c = char(i + 97);
            getWords(pnode->children[i], word+c, words);
        }
    }
}

vector<string> search(node *root, string word){
    bool flag = true;
    node *nd = root;
    int n = word.size();
    
    for(int i=0; i < n; ++i){
        int key = word[i] - 'a';
        if(!nd->children[key]){ flag = false; break; }
        nd = nd->children[key];
    }
    vector<string>result;
    if(flag){
        getWords(nd, word, result);
        return result;
    }
    else return {};
}


int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        vector<string> words(n);
        for(string &x: words) cin >> x;

        node *root = getNode();
        for(string x: words) insert(root, x);

        string q;
        cin >> q;
        for(int i=1; i <= q.size(); ++i){
            vector<string> result = search(root, q.substr(0, i));
            if(result.size()) for(string x: result) cout << x << " ";
            else cout << "0";
            cout << "\n";
        }
    }
}
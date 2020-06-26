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

bool search(node *root, string word){
    bool flag = true;
    node *nd = root;
    int n = word.size();
    
    for(int i=0; i < n; ++i){
        int key = word[i] - 'a';
        if(!nd->children[key]){ flag = false; break; }
        nd = nd->children[key];
    }
    if(flag) return nd->endWord;
    else return false;

}


int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        vector<string> words(n);
        for(string &x: words) cin >> x;

        string query;
        cin >> query;

        node *root = getNode();
        for(string x: words) insert(root, x);

        bool result = search(root, query);
        cout << int(result) << "\n";

    }
    return 0;
}
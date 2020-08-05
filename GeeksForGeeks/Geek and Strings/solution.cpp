#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int ALPHABET_SIZE = 26; 

struct node{
    struct node *children[ALPHABET_SIZE];
    int wordcount;
};

node* getNode(){    
    node *n = new node;
    n->wordcount = 0;
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
        nd->wordcount++;
    }
}

int search(node *root, string word){
    bool flag = true;
    node *nd = root;
    int n = word.size();
    
    for(int i=0; i < n; ++i){
        int key = word[i] - 'a';
        if(!nd->children[key]){ flag = false; return 0; }
        nd = nd->children[key];
    }
    return nd->wordcount;
}


int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<string> words(n);
        node* root = getNode();
        for(string &x: words){ cin >> x; insert(root, x); }

        int q;
        cin >> q;
        vector<string> query(q);
        for(string &x: query) cin >> x;

        for(int i=0; i < q; ++i) cout << search(root, query[i]) << "\n";
    }
}
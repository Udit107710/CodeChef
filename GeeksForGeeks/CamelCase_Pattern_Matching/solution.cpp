#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int ALPHABET_SIZE = 58; 

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

int search(node *root, string word){
    bool flag = true;
    node *nd = root;
    int n = word.size();
    
    for(int i=0; i < n; ++i){
        int key = word[i] - 'A';
        if(!nd->children[key]){ flag = false; break; }
        nd = nd->children[key];
    }
    
}

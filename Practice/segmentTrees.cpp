#include <bits/stdc++.h>

using namespace std;

void construct(vector<int> &arr, vector<int> &tree, int s, int e, int index){
    if(index > 28) return;
    if(s==e){
        tree[index] = arr[s];
        return;
    }
    int m = (s+e)/2;
    construct(arr, tree, s, m, 2*index);
    construct(arr, tree, m+1, e, 2*index+1);
    tree[index] = tree[2*index] + tree[2*index+1];
}

void modify(vector<int> &arr, vector<int> &tree, int s, int e, int index, int val, int find){
    if(s==e && s==find){
        tree[index] = val;
        return;
    }
    int updated = 0;
    int mid = (s+e)/2;
    if(find > s && find <= mid) modify(arr, tree, s, mid, index*2, val, find);
    else modify(arr, tree, mid+1, e, index*2+1, val, find);
    tree[index] = tree[index*2] + tree[2*index+1];
}


int main(){
    vector<int> arr = {1,2,3,4,5,6,7};
    
    vector<int> tree(28, 100000000);
    construct(arr, tree, 0, 6, 1);
    cout << endl;
    for(auto x: tree) cout << x << " ";
    cout << endl;
    modify(arr, tree, 0, 6, 1, 10, 6);
    for(auto x: tree) cout << x << " ";
    cout << endl;
    return 0;
}
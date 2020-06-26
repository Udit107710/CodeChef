#include <bits/stdc++.h>

using namespace std;

void construct(vector<int> &arr, vector<int> &tree, int s, int e, int index, int a){
    if(index > 4*a) return;
    if(s==e){
        tree[index] = arr[s];
        return;
    }
    int m = (s+e)/2;
    construct(arr, tree, s, m, 2*index, a);
    construct(arr, tree, m+1, e, 2*index+1, a);
    tree[index] = tree[2*index] + tree[2*index+1];
}

void modify(vector<int> &tree, int s, int e, int index, int left, int right, int a){
    if(index > 4*a) return;
    if(s==e && s <= right && s >= left){
        tree[index] = !tree[index];
        return;
    }
    int mid = (s+e)/2;
    if(right <= mid && left <= mid) modify(tree, s, mid, index*2, left, right, a);
    else if(right > mid && left > mid) modify(tree, mid+1, e, index*2+1, left, right, a);
    else{
        modify(tree, s, mid, index*2, left, mid, a);
        modify(tree, mid+1, e, index*2+1, mid+1, right, a);
    }
    tree[index] = tree[index*2] + tree[2*index+1];
}

int getVal(vector<int> &tree, int s, int e, int index, int left, int right, int a){
    if(index > 4*a) return 0;
    if(left == s && right == e){
        return tree[index];
    }

    int mid = (s+e)/2;
    if(right <= mid && left <= mid) return getVal(tree, s, mid, index*2, left, right, a);
    else if(right > mid && left > mid) return getVal(tree, mid+1, e, index*2+1, left, right, a);
    else return (getVal(tree, s, mid, index*2, left, mid, a) + getVal(tree, mid+1, e, index*2+1, mid+1, right, a));

}

int main(){
    int a, b;
    set<int> heads;
    set<int> tails;
    cin >> a >> b;
    vector<int> arr(a, 0);
    vector<int> stree(a*4);
    construct(arr, stree, 0, a-1, 1, a);
    while(b--){
        int c, d, e;
        cin >> c >> d >> e;
        if(c == 0){
            modify(stree, 0, a-1, 1, d, e, a);
        }
        else{
            int val = getVal(stree, 0, a-1, 1, d, e, a);
            cout << val << "\n";
        }
    }

    return 0;
}
#include <bits/stdc++.h>

using namespace std;


void createSegment(int *tree, int arr[], int start, int end, int index){
    if(start == end) tree[index] = arr[start];
    else{
        int mid = (start+end)/2;
        createSegment(tree, arr, start, mid, index*2);
        createSegment(tree, arr, mid+1, end, index*2+1);
        tree[index] = tree[index*2] ^ tree[index*2+1];
    }
}

int find(int *tree, int start, int end, int a, int b, int index){
    if(start == a && end == b) return tree[index];
    else{
        int mid = (start+end)/2;
        if( a <= mid && b <= mid) return find(tree, start, mid, a, b, index*2);
        else if(a > mid && b > mid) return find(tree, mid+1, end, a, b, index*2+1);
        else{
            int left = find(tree, start, mid, a, mid, index*2);
            int right = find(tree, mid+1, end, mid+1, b, index*2+1);

            return left ^ right;
        }
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int n, q;
        cin >> n >> q;
        int arr[n];
        for(int i=0; i < n; ++i) cin >> arr[i];
        int *tree = new int[4*n+1];
        createSegment(tree, arr, 0, n-1, 1);
        while(q--){
            int l, r;
            cin >> l >> r;
            l--;r--;
            int left=0, right=0;
            if(l > 0) left = find(tree, 0, n-1, 0, l-1, 1);
            if(r < n-1) right = find(tree, 0, n-1, r+1, n-1, 1);
            cout << (left ^ right) << "\n";
        }
    }
    return 0;
}
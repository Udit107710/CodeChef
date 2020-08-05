#include<bits/stdc++.h>

using namespace std;

void buildTree(int *tree, int arr[], int start, int end, int index){
    if(start == end) tree[index] = arr[start];
    else{
        int mid = (start+end)/2;
        buildTree(tree, arr, start, mid, index*2);
        buildTree(tree, arr, mid+1, end, index*2+1);
        tree[index] = tree[index*2] + tree[index*2+1];
    }
}

int queryTree(int *tree, int arr[], int start, int end, int index, int x, int r, int n){
    if(start == end ){
        if(tree[index]+r <= n){
            return 1;
        }
        else return -1;
    }
    if(end-start <= x){
        int s = end-start+1;
        if(tree[index]+r <= n*s){
            int mid = (start+end)/2;
            int left = queryTree(tree, arr, start, mid, index*2, x, r, n);
            int right = queryTree(tree, arr, mid+1, end, index*2+1, x, r, n);
            int current = s;
            if(left && current && right) return min(min(left, current), right);
            else if(left) return min(current, left);
            else if(right) return min(right, current);
            else return current;
        }
        else return -1;
    }
    else{
        int mid = (start+end)/2;
        int left = queryTree(tree, arr, start, mid, index*2, x, r, n);
        int right = queryTree(tree, arr, mid+1, end, index*2+1, x, r, n);
        if(left> 0 && right > 0) return min(left, right);
        else if(left > 0) return left;
        else return right;
    }
}

int main(){
    int t;
    cin >> t;
    while(t--){
        int r, n, x, k, power=0;
        cin >> n >> x >> k;
        
        int arr[n];
        for(int i=0; i < n; ++i){
            cin >> arr[i];
            power+=arr[i];
        }
        if(k > n+n || k < n){cout << "-1\n"; continue;}
        if(power == k){cout << "0\n"; continue;}
        int* tree = new int[4*n+1];
        buildTree(tree, arr, 0, n-1, 1);
        r = k - power;

        int result = queryTree(tree, arr, 0, n-1, 1, x, r, n);
        cout << result << "\n";
    }
    return 0;
}
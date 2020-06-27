#include<bits/stdc++.h>

using namespace std;

// void construct(int *tree, int *arr, int index, int start, int end, int g){
//     if(start == end){
//         if(arr[start] == g) tree[index] = 1;
//         else tree[index] = -1;
//     }
    
//     int mid = (start+end)/2;
//     construct(tree, arr, index*2, start, mid, g);
//     construct(tree, arr, index*2+1, mid, end, g);
//     if(tree[index*2] > 0 && tree[index*2+1] > 0){
//         tree[index] = min(tree[index*2], tree[index*2+1]);
//     }
//     else if(tree[index])

// }

int gcd(int a, int b){
    if(b == 0) return a;
    else return gcd(b, a%b);
}
int main(){
    int t;
    cin >> t;
    
    while(t--){
        int g, n;
        cin >> g >> n;
        
        int arr[n];
        int flag = 0;
        for(int i=0; i<n; ++i){
            cin >> arr[i];
            //if(arr[i] == g) flag = 1;
        }
        // if(flag){ cout << "1\n"; continue;}
        
        for(int i=0; i<n; ++i){
            if(gcd(arr[i], arr[i+1]) == g){ cout << arr[i] << " " << arr[i+1]; flag = 1; break;}
        }

        if(flag){
            cout << "2\n"; continue;
        }
        else{
            cout << "-1\n"; continue;
        }
    }

    return 0;
}
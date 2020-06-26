void create(int *tree, int start, int end, int index, int arr[]){
    if(start == end) tree[index] = arr[start];
    else{
        int m = (start+end)/2;
        create(tree, start, m, index*2, arr);
        create(tree, m+1, end, index*2 + 1, arr);
        tree[index] - min(tree[index*2], tree[index*2+1]);
    }
}

int *constructST(int arr[],int n){
  int tree[4*n+1] = {-1};
  create(tree, 0, n-1, 1, arr);
  return tree;
}


/* The functions returns the
 min element in the range
 from a and b */
int minQuery(int *tree, int start, int end, int a, int b, int index){
    if( a == start && b == end) return tree[index];
    else{
        int m = (start+end)/2;
        if(a <= m && b <= m) return minQuery(tree, start, m, a, b, index*2);
        else if(a > m && b > m) return minQuery(tree, m+1, end, a, b, index*2+1);
        else return min(minQuery(tree, start, m, a, m, index*2), minQuery(tree, m+1, end, m+1, b, index*2+1));
    }
}

int RMQ(int st[] , int n, int a, int b){
    return minQuery(st, 0, n-1, a, b, 1);
}

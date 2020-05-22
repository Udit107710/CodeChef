#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int testcase;
	cin >> testcase;

	while (testcase--) {
		int n;
		string name;
		cin >> n;
		cin >> name;
		unsigned long long int c = std::count(name.begin(), name.end(), '1');
        
        cout << ((c*(c+1))/2) << endl;
	}
}
// 11279 최대 힙

#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int n;
priority_queue<int> pq;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    
	cin >> n;
	while(n--){
		int x;
		cin >> x;
		if(x == 0){
			if(pq.empty()) cout << "0\n";
			
			else{
				cout << pq.top() << "\n";
				pq.pop();
				
			}
		}
		else{
			pq.push(x);
		}
	}
	return 0;
}
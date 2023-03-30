#include <iostream>
#include <string>

using namespace std;

int n, k, cnt;
int a[20];

void dfs(int idx, int sum) {
	if (sum > k) return;
	if(sum==k){
		cnt++;
		return;
	}

	for (int i = idx; i < n; i++)
		dfs(i + 1, sum + a[i]);
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc < T + 1; tc++) {
		a[20] = { 0, };
		cnt = 0;
		cin >> n >> k;

		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}

		dfs(0,0);
		cout << "#" << tc << " " << cnt << "\n";
	}
	return 0;
}
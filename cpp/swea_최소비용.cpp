#include <iostream>
#include <queue>

using namespace std;

int T, N, result;
const int MAX_SIZE = 101;
int map[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE];
int direct[4][2] = { 1,0, -1,0, 0,1, 0,-1 };

void bfs(int y, int x) {
	queue<pair<int, int>> q;
	q.push(make_pair(y, x));
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = y + direct[i][0];
			int nx = x + direct[i][1];
			if (0 <= ny < N && 0 <= nx < N) {
				int d = 1;
				if (map[ny][nx] > map[y][x]) {
					d += map[ny][nx] - map[y][x];
				}
				if (visited[ny][nx] > visited[y][x] + d) {
					visited[ny][nx] = visited[y][x] + d;
					q.push(make_pair(ny, nx));
				}
			}
		}
	}
	return;
}


int main() {

	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		cin >> N;
		for (int y = 0; y < N; y++) {
			for (int x = 0; x < N; x++) {
				cin >> map[y][x];
				visited[y][x] = int(1e9);
			}
		}
		visited[0][0] = 0;
		bfs(0, 0);
		result = visited[N - 1][N - 1];

		cout << "#" << tc << " " << result << "\n";
	}

	return 0;
}

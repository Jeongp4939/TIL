#include <iostream>
using namespace std;

// index : ��
// value : ����ߴ°�? 
int DAT[20];
// index : / ���� �밢��
// value : ����ߴ°�? 
int LDRU[100];
// index : \ ���� �밢��
// value : ����ߴ°�? 
int LURD[100];

int N;
int cnt = 0;

void func(int row) {
	// �������� -> N-1�� ����� queen�� �ξ��ٸ�, �ϳ��� ������ ��ġ�� ã�Ҵ�!
	if (row == N) {
		cnt++;
		return;
	}
	for (int col = 0; col < N; col++) {
		// ���� col�� ���� ������̸�, ����� �� �� ����. 
		if (DAT[col] == 1)
			continue;

		// ���� / ���� �밢���� queen�� �ִٸ�, ����� �� �� ����. 
		if (LDRU[col + row] == 1)
			continue;

		// ���� \ ���� �밢���� queen�� �ִٸ�, ����� �� �� ����. 
		if (LURD[col - row + N] == 1)
			continue;

		DAT[col] = 1; // row�� �࿡�� col�� ���� queen �д� 
		LDRU[col + row] = 1; // / ���� �밢���� queen�� �ִ�. 
		LURD[col - row + N] = 1; // \ ���� �밢���� queen�� �ִ�.

		func(row + 1); // ���� �࿡ queen�� �ֺ��� 

		DAT[col] = 0; // row�� �࿡�� col���� �ξ��� queen�� ���� 
		LDRU[col + row] = 0; // / ���� �밢���� �� queen�� ���� 
		LURD[col - row + N] = 0; // \ ���� �밢���� �� queen�� ����
	}
}

int main() {
	cin >> N;
	func(0); // 0�� ����� ����
	cout << cnt;
}
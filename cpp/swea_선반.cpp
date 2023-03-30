#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int T;
string n, m;

int main()
{
	cin >> T;
	for (int tc = 1; tc < T + 1; tc++) {
		cin >> n;
		cin >> m;

		int a[100] = { 0, };
		int b[200] = { 0, };
		int nn = 0, mm = 0, aidx = 0, bidx = 0, result = 0;
		int base;
		bool flag = false;

		// 문자열 길이
		int nlen = n.length();
		int mlen = m.length();

		// 10진수 만들기 문자열은 아스키코드 변환하여 계산하므로 '0'을 빼줘야 한다
		for (int i = 0; i < nlen; i++) {
			nn += (n[i]-'0') * int(pow(2, nlen - i - 1));
		}
		for (int i = 0; i < mlen; i++) {
			mm += (m[i] - '0') * int(pow(3, mlen - i - 1));
		}

		for (int i = nlen-1; i >= 0; i--) {
			if (n[i] == '1') {
				a[aidx] = nn - int(pow(2,nlen-i-1));
				aidx++;
			}
			else if(n[i]=='0'){
				a[aidx] = nn + int(pow(2, nlen - i - 1));
				aidx++;
			}
		}

		for (int i = mlen - 1; i >= 0; i--) {
			if (m[i] == '0') {
				b[bidx] = mm + int(pow(3, mlen - i - 1));
				bidx++;
				b[bidx] = mm + 2*int(pow(3, mlen - i - 1));
				bidx++;
			}
			else if (m[i] == '1') {
				b[bidx] = mm - int(pow(3, mlen - i - 1));
				bidx++;
				b[bidx] = mm + int(pow(3, mlen - i - 1));
				bidx++;
			}
			else if (m[i] == '2') {
				b[bidx] = mm - 2*int(pow(3, mlen - i - 1));
				bidx++;
				b[bidx] = mm - int(pow(3, mlen - i - 1));
				bidx++;
			}
		}

		
		for (int i = 0; i < aidx; i++) {
			if (flag) break;
			for (int j = 0; j < bidx; j++) {
				if (a[i] == b[j]) {
					result = a[i];
					flag = true;
					break;
				}
			}
		}
		

		cout << "#" << tc << " " << result << "\n";

	}
	return 0;
}
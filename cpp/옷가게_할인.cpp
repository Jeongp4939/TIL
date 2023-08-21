#include <string>
#include <vector>

using namespace std;

int solution(int price) {
    int answer = 0;
    if (price/500000>=1){
        answer = int(price*0.8);
    } else if (price/300000>=1) {
        answer = int(price*0.9);
    } else if (price/100000>=1) {
        answer = int(price*0.95);
    } else {
        answer = price;
    }
    return answer;
}

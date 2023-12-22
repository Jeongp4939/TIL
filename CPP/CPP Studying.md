# STL(Standard Template Library)
- 표준 템플릿 라이브러리
- 컨테이너, 반복자, 알고리즘
- 라이브러리의 복잡성을 줄여줌

- C++ 코드 기본 형태
```
#include <iostream>
#include <{header파일 명칭}>
...

using namespace std;

int main()
{
  return 0;
}
```

## 컨테이너(Container)
- pair
  ```
  pair<int,int> p;

  p.first = 1;
  p.second = 2;

  cout<<"first: "<<p.first<<endl;
  cout<<"second: "<<p.second<<endl;
  ```
  ```
  결과
  first: 1
  second: 2
  ```
- vector
  ```
  vector<type> vec; // 빈 vector
  vector<type> vec(n); // 숫자만큼 백터 생성 후 0으로 초기화
  vector<type> 변수명={변수1, 변수2, 변수3...}; // 백터 생성 후 오른쪽 변수 값으로 초기화
  vector<vector<자료형>> 변수명; 2차원 벡터 생성
  ```
- deque
  ```
  deque<type> dq; // 빈컨테이너
  deque<type> dq(n); // 0으로 초기화된 n개의 원소
  deque<type> dq(n,x); // x로 초기화된 n개의 원소
  deque<type> dq(iterator begin, iterator end); //iterator begin 부터 end 구간으로 초기화된 원소
  ```
- list/forward_list 
- set/multiset
- map/multiplemap
- unordered_set/unordered_map/unordered_multiset/unordered_multimap
- stact
- queue
- priority queue

## 반복자(iterator)
- input iterators
- output iterators
- forward iterators
- bidirectional iterators
- random access iterators

## 알고리즘(algorithm)
- sort
- find
- transform
- for_each
- generate
- binary_search

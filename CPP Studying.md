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
  vector<int> vec;
  ```
- deque
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

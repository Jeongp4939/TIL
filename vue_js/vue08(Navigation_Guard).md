# Navigation Guard
### 네비게이션 가드
- Vue Router를 통해 특정 URL에 접근할 때 다른 url로 redirect하거나 해당 URL로의 접근을 막는 방법
    - 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

### 네비게이션 가드의 종류
- 전역 가드
    - 애플리케이션 전역에서 동작
- 라우터 가드
    - 특정 URL에서만 동작
- 컴포넌트 가드
    - 라우터 컴포넌트 안에 정의

### 전역 가드
#### Global Before Guard
- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 `router.beforeEach()`를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
    - to : 이동할 URL 정보가 담긴 Route 객체
    - from : 현재 URL 정보가 담긴 Route 객체
    - next : 지정한 URL로 이동하기 위해 호출하는 함수
        - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
        - 기본적으로 to에 해당하는 URL로 이동

- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
    - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
    - `next()가 호출되기 전까지 화면이 전환되지 않음`

### 라우터 가드
- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 to, from, next를 인자로 받음

### 컴포넌트 가드
- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### Params 변화 감지
- `beforeRouteUpdate()`를 사용해서 처리
    - userName을 이동할 params에 있는 userName으로 재할당

### 404 Not Found
- 사용자가 요청한 리소스가 존재하지 않을 때 응답
- https://localhost:8080/404 확인

- 모든 경로에 대해서 404 page로 redirect 시키기
    - 기존에 명시한 경로가 아닌 모든 경로가 404page로 redirect됨
    - 이때, routes에 최하단부에 작성해야 함

```javascript
  {
    path: '*', // 위에 해당하지 않는 모든 것
    redirect: '404',
  }
```
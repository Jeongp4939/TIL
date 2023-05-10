# Vue 7(UX & UI)

## UX & UI

### UX(User Experience)
- 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
- 유저가 느끼는 느낌, 태도 그리고 행동을 디자인
    - 백화점 1층에서 느껴지는 좋은 향수 향기
    - 러쉬 매장 근처의 러쉬 향기 등

#### 좋은 UX를 설계하기 위해서는
- 사람들의 마음과 생각을 이해하고 정리해서 우리 제품에 녹여내는 과정이 필요
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

### UI(User Interface)
- 유저에게 보여지는 화면을 디자인
- UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통

#### [참고]Interface
- 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
    - 즉, 사용자가 기기를 쉽게 동작 시키는데 도움을 주는 시스템
- 우리 일상 속에 인터페이스 예시
    - CLI(command-line interface)나 GUI(Graphic User Interface)를 사용해서 컴퓨터를 조작

#### 좋은 UI를 설계하기 위해서는
- 예쁜 디자인 즉 심미적인 부분만 중요하다기보다는 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려되어야 함
- 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요
- UI 디자인에 있어 가장 중요한 것은 `협업`

#### 디자이너와 기획자 그리고 개발자
- 많은 회사에서 UX/UI 디자인을 함께하는 디자이너를 채용하거나 UX는 기획자, UI는 디자이너의 역할로 채용하기도 함

- UX(직무: UX Researcher, User Researcher)
    - 구글 : 사용자의 경험을 이해하기 위한 통계 모델을 설계
    - MS : 리서치를 기획하고 사용자에 대한 지표를 정의
    - Meta : 정성적인 방법과 정량적인 방법을 사용해서 사용자 조사를 실시
- UI(직무: Product Designer, Interaction Designer)
    - 구글 : 다양한 디자인 프로토타이핑 툴을 사용해서 개발 가이드를 제공
    - MS : 시각 디자인을 고려해서 체계적인 디자인 컨셉을 보여줌
    - Meta : 제품을 이해하고 더 나은 UI Flow와 사용자 경험을 디자인

- 개발자는 단순히 기능 개발만 하는 사람이 아니며 제품에 대해 고민하고 소통하는 능력이 반드시 필요
- 즉, 다양한 분야와의 협업이 필수적이기에 기본적인 UX/UI에 대한 이해가 필요

## Vue Router
### Routing
- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
- 예시
    - /articles/index/에 접근하면 articles의 index에 대한 결과를 보내줌

### Routing in SSR
- Server가 모든 라우팅을 통제
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
    - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

### Routing in SPA / CSR
- 서버는 하나의 HTML(index.html) 만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
    - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉, `하나의 URL만 가질 수 있음`

### Why Routing?
- 동작에 따라 URL이 바뀌어야 하는가?
    - 유저의 사용성 관점에서 필요
- Routing이 없다면
    - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
        - 새로고침 시 처음 페이지로 돌아감
        - 링크를 공유할 시 처음 페이지만 공유 가능
    - 브라우저의 뒤로 가기 기능을 사용할 수 없음


## Vue Router
- vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(Routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
    - SPA의 단점 중 하나인 `"URL이 변경되지 않는다"를 해결`
- [참고] MAP(Multiple Page Aplication)
    - 여러 개의 페이지로 구성된 애플리케이션
    - SSR 방식으로 렌더링

### `router-link`
- a태그와 비슷한 기능 -> URL을 이동시킴
    - routes에 등록된 컴포넌트와 매핑
    - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드 하지 않도록 함
- 목포 경로는 `to` 속성으로 지정
- 기능에 맞게 HTML에서 a태그로 rendering되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### `router-view`
- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링

- Django에서의 block tag와 비슷함
    - App.vue 는 base.html의 역할
    - router-view는 block 태그로 감싼 부분

### src/router/index.js
- 라우터에 관련된 정보 및 설정이 작성 되는 곳
- Django에서의 urls.py에 해당
- rolutes에 URL과 컴포넌트를 매핑

### src/Views
- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- 폴더별 컴포넌트 배치는 다음과 같이 진행
- view/
    - routes에 매핑되는 컴포넌트, 즉 <router-view>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
    - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
    - ex) App 컴포넌트 내부의 AboutView&HomeView 컴포넌트
- componenets/
    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
    - ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

## Vue Router 실습
### 주소를 이동하는 2가지 방법
1. 선언적 방식 네비게이션
    - router-link의 `to`속성으로 주소 전달
        - routes에 등록된 주소와 매핑된 컴포넌트로 이동
    - Named Routes
        - 이름을 가지는 routes
            - Django에서 path 함수의 name 인자의 활용과 같은 방식
    - 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동

2. 프로그래밍 방식 네비게이션
- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
    - history stack에 이동할 URL을 넣는(push) 방식
    - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
- 결국 <router-link :to="...">를 클릭하는 것과 `$router.push(...)`를 호출하는 것은 같은 동작

### Dynamic Route Matching
- 동적 인자 전달
    - URL의 특정 값을 변수처럼 사용할 수 있음
- ex) Django에서의 variabel routing

- router/index.js에 route 추가
- route를 추가할 때 동적 인자를 명시
- `$route.params`로 변수에 접근 가능

- 다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장

### lazy-loading
- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
    - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
    - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심


# TIL
Today I Learned

# 프로젝트 하면서 필요한 정보 공부

- React @Mui/material이 생각보다 불편하다
  - 디자인이 잘 되어있는 템플릿이 있던데 생각을 못해서 지금와서 아쉽다
- 


# Unity

### 시작
- 3D로 생성
- 3D(URP) : Universal Render Pipeline
  - 기존 3D에 비해 조금 더 무거움
### Unity로 제작 가능한 것
- 게임, 영화, 에니메이션 모두 가능

### 구성 요소
- Hieracy
- Inspector
  - Component : 속성에 해당하는 부분
 
### 단축키
- 물체를 찾을 때 : F(Focus)를 누르면 해당 오브젝트로 이동
- QWERTY 자판으로 커서 역할 변경 가능
- V(Vertex snapping)를 누르면 자동으로 다른 오브젝트에 붙게 할 수 있음(누른상태 유지)

### 모델링 추가할 때
- OBJ : 애니메이션 X
- FBX : 애니메이션 O
- MeshRenderer -> Material : 내부에 배열 형태로 저장됨
- 스카이박스
  - Window->Rendering->Lighting->Environment->SkyBox
    

### 도움이 될 만한 것
- UModelerX : 제페토 등


### Collider
- 바닥은 Mesh Collider 를 쓰는게 좋다
  - box Collider를 사용할 시 바닥을 뚫고 자유낙하하는 버그가 발생할 수 있다.
- Collider는 모양에 맞는것을 써야 성능 저하를 막을 수 있다.

### Essets
- Creator Kit:Puzzle
  - Unity 자체 제작 에셋
  - 내부에 레벨을 디자인 하는 등의 여러 기능들이 들어있음
  - Prefabs에 가면 다른 도구들도 선택 가능
    - 드래그앤 드롭으로 사용 가능


### 폴더 구조
01. Scenes
02. Materials
03. Textures
04. Scripts
  - 04-1. LobbyScripts
  - 04-2. Minigame 1
05. Models
06. Prefabs
07. Res


## Scripts
#### Script 생성 시 주의점
- 만들 때 이름을 먼저 작성 한 뒤 생성 완료를 할 것
- 추후 변경하려 할 시에 오류가 발생할 가능성이 높음

#### public
- public으로 전역변수를 선언 시 unity에서 확인이 가능 함
- but, Unity에서 입력된 값이 우선되기 때문에 주의

#### [SerializeField]
- unity에서 확인은 가능
- 인스펙터에서 접근 가능하지만, 외부 스크립트에서 접근 불가능함

### 이동

#### Time.deltaTime
- sec를 기반으로 작동하는 시간
- 컴퓨터마다 frame 등 성능이 다르기 때문에 사용함

#### transform.Traslate
```
  transform.Translate(h * Vector3.right);
  transform.Translate(v * Vector3.forward);
```
- right : 오른쪽
- forward : 앞

- 반대키가 Negative를 해주어서 한 방향만 해주면 됨

- 회전 : X가 위아래, Y가 좌우

#### 컴포넌트 사용
- 컴포넌트를 가져올 때는 start에서 한번 더 선언을 해주어야함
```
  ex = GetComponent<Example>();
```


# 23.08.28

- 새로운 씬을 생성시 라이트의 강도와 색상을 조정(환경 정보)

### 크기의 단위
- Plane 1의 크기(MR,XR): 10M
- Object : 1M
- Sphere : 지름 1M

### Open World와 Colosed World
- 어떤 공간을 기준으로 할 지 생각(오픈과 클로즈)
  - 렌더링 시에 문제가 생길 수 있음
- 씬의 로딩에 대해 고민을 해보아야함

### 프로토 타입 만들 시 주의
- 에셋을 먼저 넣지 말 것
- 기본 오브젝트로 생성을 완료한 뒤에 에셋을 씌워주는것이 일반적

### 시네마 씬(Unity Registry)
- window -> Package Manager -> Pakages: 4종류 중 선택 / 없는 것을 가져오고 싶다면 Project Settings -> Package Manager에서 외부 패키지를 가져와서 사용할 수 있음
- CinemaChine
- ARFoundation(증강현실 만들 때 사용)
- AR Core(안드로이드 전용)
- ARKit(ios)
- XR Interaction Toolkit(VR기기)
- Visual Scripting(block coding Unreal의 블루프린트와 비슷함)

### Player Camera
- CinemaChine -> VirtualCamera -> Follow, Look at 설정

### Input 기능 생성
- Script : input Manager
- Project Settings 내부의 Input Manager를 이용 할 수 있음


---
# 23.08.30

### 폭발 에셋 War FX
- 에셋을 가져와 사용할 때 해당 에셋의 스크립트 삭제

### 프리팹
- 재사용 가능한 에셋
- 하이어라키에서 프리팹 폴더로 보내놓으면 프리팹 생성 완료
- 다시 사용시 다시 하이어라키로 올리면 복제되어 생성됨


### 레이어
- 레이어를 다르게 생성한 후
- edit->project settings->py

### Raycast와 Ray를 이용해 총의 발사를 구현할 수 있음

---

# 23.09.04

### switch case를 통해 NPC의 행동을 등록할 수 있음
- Idle : 보통 상태
- Move
- Attack 등

### 길따라 플레이어를 따라가게 하는것
- NavMesh

### Animation
- hasExitTime이 체크되어 있으면 애니메이션에 딜레이가 생길 수 있음
- Attack의 경우 Loop Time을 해제
- Trigger 등의 파라미터를 생성하고, Code를 통해 Animation의 작동을 조정가능



# MSA(Micro Service Architecture)와 라이브러리

- 단일 프로그램을 각 컴포넌트 별로 나누어 작은 서비스로 나누는 것

## CAP 설계
- 일관성
- 가용성
- 분할내성


- 이벤트 발생 -> 대규모 트래픽 발생 -> 서비스 펑!

Monolithic <-> MSA

### Monolithic
- 단순함
- 모든 서비스의 개발 환경이 동일 -> 개발 관리가 용이
- 시스템 규모가 커질 경우 -> 코드 이해 및 분석, 유지보수 어려움
- 작은 수정 사항에도 전체를 빌드, 배포

### MSA
- 개별 배포 가능
- 장애 발생 시, 전체 서비스로 확장 될 가능성 적음
- 팀 별 프로젝트 분리, 코드 이해도 증가, 유지보수 원할
- 서비스 부하에 따라 개별적으로 scale-out

- 예시 -> NETFLIX(2007년 서비스 장애를 겪고 이후 CLOUD로)
- 국내 사례 -> 배민

- MSA의 규모가 커지면 아키텍처가 복잡해짐

- Monolithic에 비해 상대적으로 복잡
- 서비스 간 호출 시 API를 사용해서 통신 비용 및 지연 발생
- 테스트 및 트랜잭션 복잡도 증가 많은 자원 필요
- 데이터가 여러 서비스에 분산되어 있기에 정합성 관리 힘듦

-> 비용, 개발 생산성, 배포 주기 등을 고려


### 라이브러리 -> JitPack
- JVM 형태의 오픈소스 라이브러리 배포 플랫폼
- Gitlab 등 저장소와 연동하여 배포

- MFA -> 프론트의 MSA


# React

### Create React App
```
npx create-react-app {경로}
```

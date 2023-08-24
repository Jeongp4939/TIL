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


### Scripts
#### Script 생성 시 주의점
- 만들 때 이름을 먼저 작성 한 뒤 생성 완료를 할 것
- 추후 변경하려 할 시에 오류가 발생할 가능성이 높음
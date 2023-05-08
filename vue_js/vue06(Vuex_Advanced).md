# Vuex Advanced

## local Storage
상태 유지하기
- 현재 앱을 재실행 하거나, 새로고침을 하면 초기 값으로 돌아감
- 페이지에서 테마를 설정하고, 새로고침해도 테마가 유지되는걸 확인
- 개발자도구>Application>LocalStorage에서 확인
    - `theme Key`에 light Value가 저장되어 있음
    - `theme Key`에 datk value로 값을 변경하고 새로고침 하면 변경되는걸 확인 할 수 있음

### Window.`localStorage`
- 브라우저의 내장 객체 중 하나
- Key-Value의 형태로 데이터를 저장할 수 있는 저장소
- localStorage에 저장된 데이터는 브라우저를 종료해도 계속해서 유지 됨
    - 다른 탭에서도 동일한 데이터를 공유할 수 있는 반면, 다른 도메인에서는 접근할 수 없음
    - 단, 보안과 관련된 중요한 정보를 저장하기에는 적합하지 않음

- `setItem(keu,value)` - key, value 형태로 데이터 저장
    - 데이터 저장 시 문자열 형태로 저장됨에 주의
- `getItem(key)` - key 값으로 저장된 데이터 불러오기
    - 데이터 저장 시 문자열 형태로 저장하였으므로, 불러올때도 문자열로 불러옴

### JSON.`stringify`
- JSON(JavaScript Object Notation) 객체의 메서드
- 자바스크립트 객체를 `JSON 형식의 문자열`로 변환하여 반환

### JSON.`parse`
- `JSON 형식의 문자열`을 자바 스크립트 객체로 변환하여 반환

## plugins
- Vuex store에 추가적인 기능을 제공하는 확장 기능
- 일반적으로 state의 변화를 감지해, 어플리케이션의 성능을 최적화하는 목적

### vuex-persistedstate
- Vuex store의 상태를 브라우저 local storage에 저장해 주는 plugin
- 페이지를 새로고침하거나 브라우저를 종료하였다가 다시 열었을 때, `이전 상태를 유지`할 수 있도록 해줌

- 설치
```
$ npm i vuex-persistedstate
```
- 적용
```javascript
import createdPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
    plugins: [
        createPersistedState
    ],
})
```
- 메시지 입력 후, Local Storage를 확인하면 `vuex` key에 state의 message가 가진 값들이 value로 할당 된 것을 확인 가능
- 브라우저를 종료 후, 다시 서버를 열었을 때도 vuex의 상태가 유지됨을 확인할 수 있음
- [참고] 추가 옵션을 사용하여 필요에 따라 저장 방식을 변경 할 수 있음
```javascript
const persistedState = createPersistedState({
    // key를 변경
    key: 'mp-app'
    // 저장 위치를 변경
    storage: window.localStorage
    // 상태중 일부만 저장
    reducer: state => ({
        message: state.message
    })
})

export default new Vuex.Store({
    plugins: [
        persistedState
    ],
    state: {
        message: 'message in store',
        age: 30
    }
})
```

## Vuex Binding helper
- Vuex store의 state, mutations, actions 등을 간단한게 사용할 수 있도록 만들어진 헬퍼 함수
- mapState, mapActions와 같은 형식으로 사용
- 사용하기 위해서는 import 받아와야 함
```javascript
import {mapState, mapActions} from 'vuex'
```

### mapState
- Vuex store의 상태를 컴포넌트의 데이터에 매핑할 때 사용
- 객체 혹은 배열 형태로 상태를 매핑하여 사용 할 수 있음

- 객체 형태로 매핑
    1. mapState를 import
    2. Spread operator를 사용하여 mapState를 전개
    3. mapState 내부에 불러오고자 하는 값을 정의, 화살표 함수를 사용하여 message key에 state의 message 값을 할당
    - key 값은 컴포넌트에서 사용하고자 하는 다른 이름으로 변경하여 사용 할 수 있음
    ```html
        <template>
        <div id="app">
            <h1>{{ message }}</h1>
        </div>
    </template>

    <script>
        import { mapState } from 'vuex'

        export default {
            ...
            computed: {
                ...mapState({
                    message: state => state.message
                })
            },
        }
    </script>
    ```

- 배열 형태로 매핑
    1. mapState를 import
    2. Spread operator를 사용하여 mapState를 전개
    3. vuex store의 상태 중, 불러오고자 하는 대상을 배열의 원소로 정의
    ```html
    <template>
        <div id="app">
            <h1>{{ message }}</h1>
        </div>
    </template>

    <script>
        import { mapState } from 'vuex'

        export default {
            ...
            computed: {
                ...mapState(['message'])
            },
        }
    </script>
    ```

### mapActions
- 컴포넌트에서 this.$store.dispatch()를 호출하는 대신, 액션 메서드를 직접 호출하여 사용 할 수 있음
- mapState와 같이 객체 혹은 배열 형태로 매핑가능

- 배열 형태로 매핑
    1. mapState와 동일한 형식으로 사용
    - 단, 이 경우 changeMessage에 넘겨주어야 할 inputData를 changeMessage 호출 시 인자로 직접 값을 넘겨주어야 함
    ```html
    <template>
        <div id="app">
            <h1>{{ message }}</h1>
            <input
            type="text"
            @keyup.enter="changeMessage(inputData)"
            v-model="inputData">
        </div>
    </template>

    <script>
        import { mapActions } from 'vuex'
        export default {
            ...
            methods: {
                ...mapActions(['changeMessage'])
            },
        }
    </script>
    ```

- 객체 형태로 매핑
    1. Actions의 changeMessage를 actionsChangeMessage에 매핑
    2. this.actionsChangeMessage 형식으로 사용
    3. payload를 넘겨주거나 추가적인 로직 작성 가능
    ```html
    <template>
        <div id="app">
            <input
            type="text"
            @keyup.enter="onSubmit"
            v-model="inputData">
        </div>
    </template>

    <script>
        import { mapActions } from 'vuex'
        export default {
            ...
            methods: {
                ...mapActions({
                    actionsChangeMessage: 'changeMessage'
                }),
                onSubmit() {
                    const newMessage = this.inputData
                    this.actionsChangeMessage(newMessage)
                    this.inputData=''
                }
            }
        }
    </script>
    ```

### mapGetters
- map State, mapActions와 동일한 방식으로 사용가능
```html
<template>
    <div id="app">
        <h1>길이 {{ messageLength }}의 메시지 {{ message }}를 입력받음</h1>
            <h3>x2 : {{ doubleLength }}</h3>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'
    export default {
        ...
        computed: {
            ...mapgETTERS(['messageLength', 'doubleLength']),
        }
    }
</script>
```
- [참고] 상황에 따라서는 배열과 객체 형태로 각각 매핑하여 사용 할 수 있음
```html
<template>
    <div id="app">
        <h1>{{ age }} {{ message }}</h1>
    </div>
</template>

<script>
    import { mapState } from 'vuex'
    export default {
        ...
        computed: {
            ...mapState(['message']),
            ...mapState({
                age: state => state.age
            })
        }
    }
</script>
```

## Modules
- Vuex store를 여러 파일로 나눠 관리 할 수 있게 해 주는 기능
- Vuex store와 동일한 구성을 가진 별도의 객체를 정의하여 modules 옵션에 작성한 객체를 추가하여 사용
- 별개의 .js 파일에 정의하고 import 하는 방식으로도 사용가능
- Store의 가독성을 향상시킬 수 있음
- 별도의 js 파일에 객체 정의
```javascript
// store/modules/myModule.js

const myModule = {
    state: {
        age: 30
    },
    mutations: {
        INCREMENT_AGE(state) {
            state.age += 1
        },
        actions: {
            incrementAge(context) {
                context.commit(INCREMENT_AGE)
            }
        }
    }
}

export default myModule
```

- 정의한 js 파일의 객체를 import
- store의 modules 옵션에 추가
```javascript
import Vue from 'vue'
import Vuex from 'vuex'
import myModule from './modules/myModule'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        myModule
    }
})
```

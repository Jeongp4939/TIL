# DB 3일차

## A many-to-one relationship

관계형 데이터베이스에서의 외래 키 속성을 사용해 모델간 N:1 관계 설정하기

## RDB(관계형 데이터베이스) 복습
    - 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
    - RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음

### RDB에서의 관계
    1. 1:1
        - One-to-one relationships
        - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한개와 관련된 경우
    2. N:1
        - Many-to-one relationships
        - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
        - 기준 테이블에 따라(1:N, Ont-to-many relationships)이라고도 함
        - 예) 고객이 여러개의 주문을 진행할 수 있음
    3. M:N
        - Many-to-many relationships
        - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
        - 양쪽 모두에서 N:1 관계를 가짐

# Foreign Key
    - 외래 키(외부 키)
    - 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
    - 참조되는 테이블의 기본 키(Primary Key)를 가리킴
    - 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응됨
        - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
    - 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

## 특징
    - 키를 사용하여 부모 테이블의 유일한 값을 참조(by 참조 무결성)
    - 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

### [참고] 참조 무결성
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
    - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함

## N:1(Comment-Article)
    - Comment(N) - Article(1)
    - Comment 모델과 Article 모델 간 관계 설정
    - 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있음

### 모델 간 관계 설정

    모델 관계 설정
    - 게시판의 게시글과 N:1관계를 나타낼 수 있는 댓글 구현
    - N:1 관계에서 댓글을 담당할 Comment 모델은 N, Article 모델은 1이 될 것

## Django Relationship fields
    - Django Relationship fields 종류
        1. OneToOneField()
            - A one-to-one relationship
        2. ForeignKey()
            - A many-to-one relationship
        3. ManyToManyField()
            - A many-to-many relationship

## `ForeignKey(to, on_delete, **options)`
    - A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
    - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
    - 2개의 필수 위치 인자가 필요
        1. 참조하는 model class
        2. on_delete 옵션

### Comment Model
Comment Model 정의
```python
    class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
```
    - 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계업싱 필드의 마지막에 작성됨
    - ForeignKey()클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

#### ForeignKey arguments - on_delete
    - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
    - 데이터 무결성을 위해서 매우 중요한 설정
    - on_delete 옵션 값
        - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
        - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재

### Migration 과정 진행
    1. models.py에 모델에 대한 수정사항이 발생했기 때문에 migration 과정을 진행
    2. 마이그레이션 파일 생성 확인
    3. migrate 진행

    - migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인
    - ForeignKey 모델 필드로 인해 작성됨 컬럼의 이름이 article_id인 것을 확인
    - 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성했다면 abcd_id로 만들어짐
        - 이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유

## 관계 모델 참조
Related manager
- Related manager는 N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조할 때에 사용할 수 있는 manager를 생성
    - 우리가 이전에 모델 생성시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨

### 역참조
- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
    - 외래 키를 가지지 않은 1이 왜래 키를 가진 N을 참조

`article.comment_set.method()`
- Article 모델이 Comment 모델을 참조(역참조) 할 때 사용하는 매니저
- article.comment 형식으로는 댓글 객체를 참조 할 수 없음
    - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
- 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음

    ※ N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐

- 반면 참조 상황(Comment->Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

### ForeignKey arguments - related_name
```python
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
        ...
```
- ForeignKey 클래스의 선택 옵션
- 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있음
- 작성 후, migration 과정이 필요
- 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 함

#### admin site 등록
새로 작성한 Comment 모델을 admin site에 등록

#### CREATE
- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성
```python
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            exclude = ('article',)
```
- detail 페이지에서 CommentForm 출력(view 함수)
```python
    from .forms import ArticleForm, CommentForm

    def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```
- detail 페이지에서 CommentForm 출력(템플릿)
```html
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
        {% csrf_token %}
        {{ commnet_form }}
        <input type="submit" value="작성">
    </form>
```

- 외래 키 필드는 사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장 되어야 함

```python
    urlpatterns = [
        path('<int:pk>/comments/', views.comments_create, name='commants_create')
    ]
```
```python
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.isvlid():
            comment_form.save()
        return redirect('articles:detail',article.pk)
```
```html
    <form action="{% url 
    articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
    </form>
```
- 작성을 마치고 보면 article 객체 저장이 이루어질 타이밍이 보이지 않음
- 그래서 save()메서드는 데이터베이스에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해주는 옵션 값을 제공


#### The `save()` method
- save(commit=False)
    - Create, but don't save the new instance
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용

- save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장


## READ
- 작성한 댓글 목록 출력하기
- 특정 article에 있는 모든 댓글을 가져온 후 context에 추가

```python
    from .models import Article, Comment
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments,
            }
        return render(request, 'articles/detail.html', context)
```
- detail 템플릿에서 댓글 목록 출력하기
```html
    {% extends 'base.html' %}
    {% block content %}
        ...
        <a href="{% url 'articles:index' %}">back</a>
        <hr>
        <h4>댓글 목록</h4>
        <ul>
            {% for comment in comments %}
                <li>{{ comment.content }}</li>
            {% endfor %}
        </ul>
        <hr>
        ...
    {% endblock content %}
```

## DELETE(p.64)
- 댓글 삭제 구현(url, view)
```python
    urlpatterns=[
        ...,
        path('<ing:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
    ]
```
```python
    def comments_delete(request, article_pk, comments_pk):
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
```
- 댓글을 삭제할 수 있는 버튼을 각각 댓글 옆에 출력 될 수 있도록 함
```html
    {% extends 'base.html' %}
    {% block content %}
    <h4>Sign Up</h4>
    <ul>
        {% for comment in comments %}
        <li>
            {{ comment.content}}
            <form action="" method="post">
                {% csrf_token %}
                <input type="submit" value="DELETE">
            </form>
        </li>
        {% endfor %}
    </ul>
    {% endblock %}
```

#### 댓글 수적을 바로 구현하지 않는 이유
- 댓글 수정도 게시글 수정과 마찬가지로 구현이 가능
    - 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요하게 됨
- 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form부분만 변경되어 수정 할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행하도록 함

(p.69)
Comment 추가 사항
- 댓글에 관련된 아래 2가지 사항을 작성하며 마무리
    1. 댓글 개수 출력
        1. DTL filter - length 사용
        2. Queryset API - count() 사용
    2. 댓글이 없는 경우 대체 컨텐츠 출력하기

댓글 개수 출력하기
1. DTL filter -lenth 사용
```html
    {{comment|length}}
    {{article.commnet_set.all|length}}
```
2. Queryset API - count() 사용
```html
    {{comment|length}}
    {{article.commnet_set.count}}
```
- detail 템플릿에 작성
```html
    <h4>댓글 목록</h4>
    {% if comments %}
        <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
    {% endif %}
```

댓글이 없는 경우 대체 컨텐츠 출력
- DTL for empty 활용
```html
    {% for comment in comments %}
        <li>
            {{ comment.content }}
            <form action="{% url 'articles:commnets_delete' article.pk commnet.pk %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="DELETE">
            </form>
        </li>
    {% empty %}
        <p>댓글이 없어요...</p>
    {% endfor %}
```


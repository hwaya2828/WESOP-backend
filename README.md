## 🎖  Team Wesop

### 🗓  기간

- 2주 (2021.5.10 - 2021.5.21)

### 🍭  인원

- 인원 : 프론트 3명 & 백엔드 2명

### 🎬  시연 영상

- [**Wesop**](https://www.youtube.com/watch?v=J05y2eiE76Q&list=PLZTmS1zO_K1Zj4ZRa-eu3Ugt-DfGC7eXC&index=10)

### 🔍  선정 의도

- 피부건강관리 e-커머스 'Aesop' 에 영감을 받아 소비자가 즉시 사용 가능한 커머스 사이트 구현
- e-커머스에 기본이 되는 백엔드 필수 기능, 데이터 구조 구현

### 💡  구현 기능

- **Backend** :
    - 회원가입
    - 로그인 & 로그인 데코레이터
    - 회원 정보 조회 • 수정 • 삭제
    - 상품 리스트
    - 상품별 상세 데이터
    - 조건에 따른 상품 필터링
    - 검색
    - 위시리스트 조회 • 추가 • 삭제
    - 장바구니 조회 • 추가 • 수정 • 삭제
    - 구매 & 구매 내역 확인

### 💎  맡은 역할

- 환경 설정
    - **프로젝트 초기 세팅**
        - `Django`를 사용하여 프로젝트를 진행하기 위한 초기 세팅
        - `Conda` 가상 환경을 생성 및 실행하고 `Git`으로 관리할 수 있도록 설정
        - `MySQL Database` 생성 및 연동
    - **모델링**
        - `AQuery`를 이용하여 프로젝트의 기획에 맞춘 모델링 완료
    - **Database 초기 세팅**
        - `CSV 파일`을 생성하여 `MySQL Database` 기초 설정 및 관리
        - 초기 세팅이 완료된 Database는 `dump`를 활용하여 `SQL 파일`로 보관

- 기능 구현
    - **회원가입**
        - `정규표현식`을 사용하여 회원가입 양식에 제한을 설정
        - `bcrypt`를 사용하여 password에 `salt`를 더해 `hashing`하여 `암호화`된 password를 저장
        - `data.get()` method를 이용하여 선택 입력 사항을 관리
    - **로그인**
        - 회원 정보가 일치하여 로그인에 성공했을 때, `JWT`로 생성한 `Access Token`을 전달
        - `encode`할 때 필요한 `SECRET`과 `ALGORITHM` 값은 보안을 위해 `my_settings 파일`에 분리하여 보관한 뒤 `import`하여 사용
        - `iat (인증 요청 시간)`과 `exp (토큰 만료 시간)`을 설정하여 `Access Token`과 `Refresh Token`을 각각의 목적에 맞도록 관리
        - `Refresh Token`의 경우 `exp (토큰 만료 시간)`을 현재 시간과 비교하여 유효성을 확인한 뒤, 결과에 따라 `Database`에 저장된 기존의 `Refresh Token`을 전달하거나 새로 발급하여 전달
    - **로그인 데코레이터**
        - `Decorator`를 활용하여 유저의 로그인 상태를 확인하고 해당 유저 정보를 받아오기 위한 목적
        - 전달 받은 `Access Token`을 `decode`하여 안에 담아 두었던 유저의 정보(ID)를 전달
        - `Access Token`이 만료되었을 때에는, 함께 전달받은 `Refresh Token`을 확인하여 그것이 유효한 경우 재로그인 과정 없이 새로운 `Access Token`을 생성하여 발급
    - **회원 정보 조회 • 수정 • 삭제**
        - `path parameter`을 이용하여 수정 또는 삭제할 데이터를 확인
        - `data.get()` method와 `if else 삼항표현식`을 사용하여 유저가 수정을 원하는 일부 정보만 `update` 가능하도록 구현
    - **상품 리스트** & **조건에 따른 상품 필터링** & **검색**
        - 상품 리스트를 전달해야 하는 기능들을 종합하여 하나의 `API`로 통합
        - `if else 삼항표현식`을 사용하여 조건에 따라 선택적으로 데이터 전송
        - `query parameter`를 `Q객체`에 담아 조건에 맞게 `filtering`된 상품 데이터 전송
        - `request.GET.get()`과 `request.GET.getlist()` method를 사용하여 하나 혹은 다중의 조건을 전달 받아 상품의 `filtering`에 적용
        - 검색에는 `__contains`를 사용하여 상품명을 `filtering`하도록 구현
        - 필터링에는 `__in`을 사용하여 `request.GET.getlist()`에서 받아온 조건들을 적용하도록 구현
    - **상품별 상세 데이터**
        - `path parameter`을 사용하여 상품의 아이디 값을 기준으로 상세 데이터 전송
        - 조회수를 인기 상품의 지표로 설정함에 따라 `Get request`가 올 때마다 해당 상품의 `count column` 값을 증가시키는 방법으로 조회수를 측정
    - **위시리스트 조회 • 추가 • 삭제**
        - `path parameter`을 이용하여 삭제할 데이터를 확인
    - **장바구니 조회 • 추가 • 수정 • 삭제**
        - `path parameter`을 이용하여 수정 또는 삭제할 데이터를 확인
    - **구매 & 구매 내역 확인**
        - `prefetch_related` 를 사용하여 역참조 되어 있는 데이터까지 한 번에 가져오도록 하여 `Query`를 줄일 수 있도록 구현
        - `get_or_create`를 사용하여 이전에 사용했던 주소를 기입한 경우 해당 주소를 불러오고, 새로운 주소를 기입한 경우 `Database`에 저장할 수 있도록 구현
        - 무료 배송 금액과 같이 변경 가능성 있는 기준값의 경우, 상수로 명시 하여 쉽게 수정 가능하도록 구현

### 📒  적용 기술

- **Backend**
    - Python 3.9
    - Django 3.2.4
    - MySQL 8.0.23

- **Cooperation Tool**
    - Git
    - Github
    - Slack
    - Trello
    - AQuery
    - Postman



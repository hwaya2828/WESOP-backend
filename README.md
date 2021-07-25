## 🎖  Team Wesop

### 기간

- 2주 (2021.5.10 - 2021.5.21)

### 인원

- 인원 : 프론트 3명 & 백엔드 2명

### 코드

- **[GitHub](https://github.com/hwaya2828/WESOP-backend)**

---

### 🎬  시연 영상

- [**Wesop**](https://www.youtube.com/watch?v=J05y2eiE76Q&list=PLZTmS1zO_K1Zj4ZRa-eu3Ugt-DfGC7eXC&index=10)

---

### 🔍  선정 의도

- 피부건강관리 e-커머스 'Aesop' 에 영감을 받아 소비자가 즉시 사용 가능한 커머스 사이트 구현
- e-커머스에 기본이 되는 백엔드 필수 기능, 데이터 구조 구현

---

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

---

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

## SKILLS

### Frontend Skill
<ul>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/d63d473e728e20a286d22bb2226a7bf45a2b9ac6c72c59c0e61e9730bfe4168c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48544d4c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d68746d6c35266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/d63d473e728e20a286d22bb2226a7bf45a2b9ac6c72c59c0e61e9730bfe4168c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48544d4c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d68746d6c35266c6f676f436f6c6f723d7768697465" alt="HTML" data-canonical-src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&amp;logo=html5&amp;logoColor=white" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/9d07c04bdd98c662d5df9d4e1cc1de8446ffeaebca330feb161f1fb8e1188204/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176615363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d626c61636b"><img src="https://camo.githubusercontent.com/9d07c04bdd98c662d5df9d4e1cc1de8446ffeaebca330feb161f1fb8e1188204/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176615363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d626c61636b" alt="JS" data-canonical-src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&amp;logo=javascript&amp;logoColor=black" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/268ac512e333b69600eb9773a8f80b7a251f4d6149642a50a551d4798183d621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642"><img src="https://camo.githubusercontent.com/268ac512e333b69600eb9773a8f80b7a251f4d6149642a50a551d4798183d621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642" alt="React" data-canonical-src="https://img.shields.io/badge/React-20232A?style=for-the-badge&amp;logo=react&amp;logoColor=61DAFB" style="max-width:100%;"></a></li></ul>

### Backend Skill

<ul><li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/27250b9f428b32314f8610e1a996939cc116da5f8c4d8a2f8ed37104275085b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3134333534433f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/27250b9f428b32314f8610e1a996939cc116da5f8c4d8a2f8ed37104275085b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3134333534433f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465" alt="Python" data-canonical-src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&amp;logo=python&amp;logoColor=white" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465" alt="Django" data-canonical-src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&amp;logo=django&amp;logoColor=white" style="max-width:100%;"></a></li>
</ul>

### Cooperation Tool

<ul>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/7cbefa0a56a026d9fc03e4a6005ae5199f3eb08a6441e9030bfdc66b70dc500d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5472656c6c6f2d2532333032364141372e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d5472656c6c6f266c6f676f436f6c6f723d7768697465"><img alt="Trello" src="https://camo.githubusercontent.com/7cbefa0a56a026d9fc03e4a6005ae5199f3eb08a6441e9030bfdc66b70dc500d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5472656c6c6f2d2532333032364141372e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d5472656c6c6f266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/Trello-%23026AA7.svg?&amp;style=for-the-badge&amp;logo=Trello&amp;logoColor=white" style="max-width:100%;"></a>
</li>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/60ced9d0b93df96cf8b0c2249a2f225fc851ecf9ec2db9200b7a27bd6b72c64a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d2532334630353033332e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465"><img alt="Git" src="https://camo.githubusercontent.com/60ced9d0b93df96cf8b0c2249a2f225fc851ecf9ec2db9200b7a27bd6b72c64a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d2532334630353033332e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/git-%23F05033.svg?&amp;style=for-the-badge&amp;logo=git&amp;logoColor=white" style="max-width:100%;"></a>
</li>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/484e674f91650af15c7b80cd40d2870109044c4e8e1418b81920e49fd24111b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465"><img alt="GitHub" src="https://camo.githubusercontent.com/484e674f91650af15c7b80cd40d2870109044c4e8e1418b81920e49fd24111b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/github-%23121011.svg?&amp;style=for-the-badge&amp;logo=github&amp;logoColor=white" style="max-width:100%;"></a>
</li>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/870d2945e15dde83583f64ea1f3f4471702e45bf30fa884412da74cb7731ae42/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f536c61636b2d3441313534423f7374796c653d666f722d7468652d6261646765266c6f676f3d736c61636b266c6f676f436f6c6f723d7768697465"><img alt="Slack" src="https://camo.githubusercontent.com/870d2945e15dde83583f64ea1f3f4471702e45bf30fa884412da74cb7731ae42/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f536c61636b2d3441313534423f7374796c653d666f722d7468652d6261646765266c6f676f3d736c61636b266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&amp;logo=slack&amp;logoColor=white" style="max-width:100%;"></a>
</li>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/fe854fd55e4418bc89aed0f73b77bf17a81f4ffa1d396c3d41551ba50d91b04c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465"><img alt="AWS" src="https://camo.githubusercontent.com/fe854fd55e4418bc89aed0f73b77bf17a81f4ffa1d396c3d41551ba50d91b04c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/AWS-%23FF9900.svg?&amp;style=for-the-badge&amp;logo=amazon-aws&amp;logoColor=white" style="max-width:100%;"></a>
</li>
<li>
<a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/ac51696a0973a2641e3cfbdaebd2bfb86be989856c12e3902a1ab25f4de4aac6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f56697375616c53747564696f436f64652d3030373864372e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d7768697465"><img alt="Visual Studio Code" src="https://camo.githubusercontent.com/ac51696a0973a2641e3cfbdaebd2bfb86be989856c12e3902a1ab25f4de4aac6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f56697375616c53747564696f436f64652d3030373864372e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d76697375616c2d73747564696f2d636f6465266c6f676f436f6c6f723d7768697465" data-canonical-src="https://img.shields.io/badge/VisualStudioCode-0078d7.svg?&amp;style=for-the-badge&amp;logo=visual-studio-code&amp;logoColor=white" style="max-width:100%;"></a>
</li>
</ul>


## Reference
- 이 프로젝트는 Aesop 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- Wesop 사이트는 스킨케어 브랜드 Aesop을 참고하여 학습목적으로 만들어진 사이트이며, 사용된 이미지들은 Unsplash.com의 무료저작권 이미지들이 사용되었습니다.

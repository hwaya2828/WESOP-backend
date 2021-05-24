# ❣️ Team Wesop ❣️

- 스킨케어 브랜드 이솝을 벤치마킹
- 12일이라는 짧은 기간 동안 기획과 디자인에 소요되는 시간을 단축시키고 화면 & 기능 구현과 리팩토링에 중점을 두기 위한 1차 클론코딩 프로젝트

## 프로젝트 기간 및 팀원

- **기간** : 2021.05.10 ~ 2021.05.21

- ✨ **Frontend**  
  - [김도은](https://github.com/dosilv), [김휘성](https://github.com/Heessong), [최원근](https://github.com/choiwk) 

- ✨ **Backend**
  - [양미화](https://github.com/hwaya2828), [문성호](https://github.com/Room9)

## 프로젝트 

- Frontend 
  - (1)메인 페이지 & 상품 리스트 & 상세 페이지 애니메이션 및 레이아웃 (2)로그인 & 회원가입 인증 (3)장바구니 기능 (4)검색 기능 (5)동적 라우팅

- Backend
  - E-commerce의 기본 기능 구현에 초점을 맞췄습니다
  - (1)회원가입 (2)로그인 (3)개인 정보 수정 (4)상품 리스트 (5)상품 상제 정보 (6)필터링 (7)검색 (8)인기 상품 리스트 (9)장바구니 (10)구매 내역 확인  

- **Modeling**   
  - [Modeling](https://aquerytool.com:443/aquerymain/index/?rurl=8afb35f3-b4f6-4dd1-aae2-b0497e086eeb) *(Password : 723o35)*

- **시연 영상**    
  - Wesop(시연 영상 첨부 필요)
<br>

### Frontend 

🧼 **최원근**
- Authentication
  - 인증 : 로그인, 회원가입
- 로그인, 회원가입
  - UI 애니메이션 적용하여 생동감 표현 ( :focus-within, @keyframes )
  - 백앤드와 JWT 통신, (회원인증, 정보교류) access_Token
  - 로컬 스토리지, 세션 스토리지, 쿠키 사용
- 사용법_상세페이지
  - 레이아웃 UI 구현 및 fetch GET을 통해 서버에서 제품의 정보 데이터 받아오기
 <br>
 
🧴 **김도은**
- 메인 페이지, 상품 리스트 페이지: Layout
- Nav bar 및 Footer: 공용 컴포넌트
- 메뉴: 3단 슬라이더 애니메이션
- 카트(장바구니) 레이아웃 및 조회, 수량변경, 삭제, 주문 기능
- 상품 이미지 Carousel
- 카테고리 :오른쪽_화살표: 상품리스트 :오른쪽_화살표: 상세 페이지 동적 라우팅
- 상품 검색 기능
<br>

🛀 **김휘성**
- 상품 상세정보 컴포넌트
  - 한개의 객체에대한 상세정보를 map함수를 이용한 각 객체의 성분 갯수, 사이즈 갯수마다 다른 렌더링, 
  - 레이아웃 구현
- 선물리스트 컴포넌트
  -  서버로부터 데이터를 받아 하나의 선물정보 컴포넌트를 만들고 여러개의 선물리스트 렌더링
  -  마우스 포인팅에 따른 카트추가버튼 활성,비활성화
- 카트추가 기능 
  - 백엔드와의 통신을통해 jwt토큰 유무 확인후 fetch API의 post를 사용하여 버튼을 클릭하면 해당 상품의 데이터를 백엔드 서버로 데이터전송
<br>

### Backend

🧴 **양미화**
- 상품 리스트 : 메뉴별 혹은 카테고리별 상품 리스트
  - Query parameter를 사용하여 메뉴별 혹은 카테고리별 상품 데이터 전송
- 상품 상제 정보 : 상품 상세 페이지
  - Path parameter를 사용하여 특정 상품의 상세 데이터 전송
- 필터링 : 메뉴별 혹은 카테고리별 상품 필터링
  - Q 객체를 사용하여 필터 조건에 따라 상품을 거르고 해당 상품들의 데이터를 전송
- 검색 : 상품 검색
  - 상품명에 검색어가 포함된 상품들의 데이터를 전송
- 인기 상품 리스트 : 인기 상품 추천
  - 상품 상세 페이지 조회수를 기준으로 상위 5개 인기 상품의 데이터를 전송
<br>

🧼 **문성호**
- 회원가입 
- 로그인
- 비밀번호 암호화, 토큰 발행
  - bcrypt 활용한 비밀번호 hash 암호화 & jwt 발행
- 로그인 필수요소(계정 email,계정 pw) 유효성 판단
  - 정규 표현식 활용
- 장바구니 상품 추가 삭제 수정 조회
  - endpoint 통일, http method와 path parameter를 통한 request 구현
- 구매전환 및 구매내역
  - d구매 전환 시, 장바구니 상품 삭제 및 구매 내역 추가
<br>

## Skills

### Frontend skill
<ul>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/d63d473e728e20a286d22bb2226a7bf45a2b9ac6c72c59c0e61e9730bfe4168c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48544d4c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d68746d6c35266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/d63d473e728e20a286d22bb2226a7bf45a2b9ac6c72c59c0e61e9730bfe4168c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48544d4c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d68746d6c35266c6f676f436f6c6f723d7768697465" alt="HTML" data-canonical-src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&amp;logo=html5&amp;logoColor=white" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/9d07c04bdd98c662d5df9d4e1cc1de8446ffeaebca330feb161f1fb8e1188204/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176615363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d626c61636b"><img src="https://camo.githubusercontent.com/9d07c04bdd98c662d5df9d4e1cc1de8446ffeaebca330feb161f1fb8e1188204/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176615363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d626c61636b" alt="JS" data-canonical-src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&amp;logo=javascript&amp;logoColor=black" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/268ac512e333b69600eb9773a8f80b7a251f4d6149642a50a551d4798183d621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642"><img src="https://camo.githubusercontent.com/268ac512e333b69600eb9773a8f80b7a251f4d6149642a50a551d4798183d621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642" alt="React" data-canonical-src="https://img.shields.io/badge/React-20232A?style=for-the-badge&amp;logo=react&amp;logoColor=61DAFB" style="max-width:100%;"></a></li></ul>

### Backend skill

<ul><li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/27250b9f428b32314f8610e1a996939cc116da5f8c4d8a2f8ed37104275085b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3134333534433f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/27250b9f428b32314f8610e1a996939cc116da5f8c4d8a2f8ed37104275085b8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3134333534433f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465" alt="Python" data-canonical-src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&amp;logo=python&amp;logoColor=white" style="max-width:100%;"></a></li>
<li><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465"><img src="https://camo.githubusercontent.com/4d74b36962a1b06aed5f035f2f95f131059b2b551c7e6d81630f7df7831b9f80/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465" alt="Django" data-canonical-src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&amp;logo=django&amp;logoColor=white" style="max-width:100%;"></a></li>
</ul>

### 협업 Tool

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
- Wesop 사이트는 스킨케어 브랜드 Aesop을 참고하여 학습목적으로 만들어진 사이트이며, 사용된 이미지들은 Unsplash.com의 무료저작권 이미지들이 사용되었습니다

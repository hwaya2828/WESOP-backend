# Team Wesop

- 스킨케어 브랜드 이솝을 벤치마킹
- 12일이라는 짧은 기간 동안 기획, 디자인에 소요되는 시간을 단축시키고 화면 & 기능 구현과 리팩토링에 중점을 두기 위한 1차 클론코딩 프로젝트

## 프로젝트 인원 및 기간

- **기간** : 2021.05.10 ~ 2021.05.21

- **인원**  

Frontend  
김도은, 김휘성, 최원근 

Backend  
[양미화](https://github.com/hwaya2828), [문성호](https://github.com/Room9)

## 프로젝트 

- Frontend 
: 

- Backend : E-commerce의 기본 기능 구현에 초점을 맞췄습니다  
(1) 회원가입 (2) 로그인 (3) 개인 정보 수정 (4) 상품 리스트 (5) 상품 상제 정보 
<br>(6) 필터링 (7) 검색 (8) 인기 상품 리스트 (9) 장바구니 (10) 구매 내역 확인  
            
**Modeling**   
[Modeling](https://aquerytool.com:443/aquerymain/index/?rurl=8afb35f3-b4f6-4dd1-aae2-b0497e086eeb)*(Password : 723o35)*

**Github**   
[Wesop-Backend](https://github.com/wecode-bootcamp-korea/20-1st-WESOP-backend)

**시연 영상**    
Wesop (시연 영상 첨부 필요)

### Frontend 

🧼 **최원근**

 Authentication (인증 : 로그인, 회원가입)
 - 로그인, 회원가입 : 
UI 애니메이션 적용하여 생동감 표현 ( :focus-within, @keyframes ).
백앤드와 JWT 통신, (회원인증, 정보교류) access_Token.
로컬 스토리지,세션 스토리지, 쿠키 사용.

- 사용법_상세페이지 : 레이아웃 UI 구현 및 fetch GET을 통해 서버에서 제품의 정보 데이터 받아오기.
  

🧴 **김도은**

  - 장바구니 :

  

🛀 **김휘성**

  - 상품 상세정보 : 한개의 상품에대한 상세정보를 렌더링, map함수를 이용한 각 상품의 성분갯수, 사이즈마다 다른 렌더링
  - 선물리스트 : 서버로부터 데이터를 받아 하나의 선물정보 컴포넌트를 만들고 여러개의 선물리스트 렌더링
  - 카트추가 : fetch API의 post를 사용하여 버튼을 클릭하면 해당 상품의 데이터를 백엔드 서버로 데이터전송

### Backend

🧴 **양미화**

  - 상세페이지 : 
  - 상품리스트 :

  

🧼 **문성호**

  - 회원가입 
  
  - 로그인
  
  - 비밀번호 암호화, 토큰 발행  
    bcrypt 활용한 비밀번호 hash 암호화/ jwt 발행
    
  - 로그인 필수요소(계정 email, 계정 pw) 유효성 판단   
    정규 표현식 활용
    
  - 장바구니 상품 추가 삭제 수정 조회   
    endpoint 통일  
    http method와 path parameter를 통한 request 구현
   
  - 구매전환 및 구매내역 추가  
    구매 전환 시, 장바구니 상품 삭제 및 구매 내역 추가

## Skills

### Frond-end skill

### Back-end skill
-Django  
-Python  
-MySQL  
-Bcrypt, JWT  
-AWS EC2, RDS  

## Reference
- 이 프로젝트는 aesop 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- Wesop 사이트는 스킨케어 브랜드 Aesop을 참고하여 학습목적으로 만들어진 사이트이며, 사용된 이미지들은 Unsplash.com의 무료저작권 이미지들이 사용되었습니다

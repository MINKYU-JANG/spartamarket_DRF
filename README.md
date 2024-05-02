### **필수 기능 - MVP(Minimum Viable Product)**

- **회원가입**(O)
    - **Endpoint**: **`/api/accounts`**
    - **Method**: **`POST`**
    - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능(O)
    - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).(O)
    - **구현**: 데이터 검증 후 저장.(O)
    - **로그인 한 유저 프로필 확인**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/39e6c350-60f7-4179-ab8f-f8939153faea)
    - 로그인 안한 유저 프로필 확인
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/c34d459a-8e59-4fc1-8cd4-856acb8667e7)


- **로그인**(O)
    - **Endpoint**: **`/api/accounts/login`**
    - **Method**: **`POST`**
    - **조건**: 사용자명과 비밀번호 입력 필요.(O)
    - **검증**: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.(O)
    - **구현**: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.(O)
- **프로필 조회**(O)
    - **Endpoint**: **`/api/accounts/<str:username>`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 필요.(O)
    - **검증**: 로그인 한 사용자만 프로필 조회 가능(O)
    - **구현**: 로그인한 사용자의 정보를 JSON 형태로 반환.(O)

    
- **상품 등록**(O)
    - **Endpoint**: **`/api/products/create`**
    - **Method**: **`POST`**
    - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.(O)
    - **구현**: 새 게시글 생성 및 데이터베이스 저장.(O)
- **상품 목록 조회**(O)
    - **Endpoint**: **`/api/products`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 불필요.(O)
    - **구현**: 모든 상품 목록 페이지네이션으로 반환.(X)
- **상품 수정**(O)
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`PUT`**
    - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.(O)
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.(O)
    - **구현**: 입력된 정보로 기존 상품 정보를 업데이트.(O)
- **상품 삭제**(O)
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`DELETE`**
    - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.(O)
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.(O)
    - **구현**: 해당 상품을 데이터베이스에서 삭제.(O)

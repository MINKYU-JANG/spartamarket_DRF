### **필수 기능 - MVP(Minimum Viable Product)**

- **회원가입**(O)
    - **Endpoint**: **`/api/accounts`**
    - **Method**: **`POST`**
    - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능(O)
    - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).(O)
    - **구현**: 데이터 검증 후 저장.(O)
    - **회원가입 완료**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/9f83a367-ec03-411e-a35f-aa522b485abf)
    - **이메일 검사**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/6dd33726-aece-4c47-8120-9a95454f0adb)
    - **username 검사**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/f8ff1665-a796-4b3d-8daf-e8cab3840226)

- **로그인**(O)
    - **Endpoint**: **`/api/accounts/login`**
    - **Method**: **`POST`**
    - **조건**: 사용자명과 비밀번호 입력 필요.(O)
    - **검증**: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.(O)
    - **구현**: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.(O)
    - **로그인 성공**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/dd22ac03-206d-42d1-a3ea-7e3c16dfd537)

- **프로필 조회**(O)
    - **Endpoint**: **`/api/accounts/<str:username>`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 필요.(O)
    - **검증**: 로그인 한 사용자만 프로필 조회 가능(O)
    - **구현**: 로그인한 사용자의 정보를 JSON 형태로 반환.(O)
    - **로그인 한 유저 프로필 확인**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/39e6c350-60f7-4179-ab8f-f8939153faea)
    - **로그인 안한 유저 프로필 확인**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/c34d459a-8e59-4fc1-8cd4-856acb8667e7)
    
- **상품 등록**(O)
    - **Endpoint**: **`/api/products/create`**
    - **Method**: **`POST`**
    - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.(O)
    - **구현**: 새 게시글 생성 및 데이터베이스 저장.(O)
    - **상품 등록 성공**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/28e0df40-a1d2-4193-a779-fe589de6dd08)

- **상품 목록 조회**(O)
    - **Endpoint**: **`/api/products`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 불필요.(O)
    - **구현**: 모든 상품 목록 페이지네이션으로 반환.(X)
    - **상품 조회 완료**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/6c44b135-5947-4517-9d94-e477e645657c)


- **상품 수정**(O)
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`PUT`**
    - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.(O)
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.(O)
    - **구현**: 입력된 정보로 기존 상품 정보를 업데이트.(O)
    - **수정 권한이 있는 유저(수정 성공)**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/86059dee-4f5f-4910-8e56-4c7ab2655717)
    - **수정 권한이 없는 유저(수정 실패)**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/9381fe73-8939-4f50-9adc-3bb3ba2441fd)

- **상품 삭제**(O)
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`DELETE`**
    - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.(O)
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.(O)
    - **구현**: 해당 상품을 데이터베이스에서 삭제.(O)
    - **삭제 권한이 있는 유저(삭제 성공)**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/db5cd494-1f03-41aa-91ad-0778da396f0a)
    - **삭제 권한이 없는 유저(삭제 실패)**
    ![image](https://github.com/MINKYU-JANG/spartamarket_DRF/assets/159976157/c5006aae-ac90-40a4-8dfb-65ee76d42006)



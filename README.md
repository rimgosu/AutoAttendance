![image](https://github.com/rimgosu/AutoAttendance/assets/120752098/8ef59470-ee75-4d90-ac13-bc4a2490aca1)

# AutoAttendance

- 자동으로 엘리스 출석을 해주는 프로그램입니다.
- 실행해두면 백그라운드에서 **8시 51분, 5시 51분**에 자동으로 출석 버튼과 퇴실 버튼을 눌러줍니다.

## 사용된 기술
- **Python 3.10**으로 제작되었습니다.
- **selenium 4.9** 최신버전으로 별도의 WebDriver 설치 없이 자동으로 로그인과 버튼을 누르는 기능을 수행합니다.
- **datetime**으로 매일 같은 시간 반복합니다.
- **threading**으로 백그라운드에서 실행됩니다.
- **pystray**으로 백그라운드에서 실행 중인 앱이란 것을 표시해줍니다.
- **VS Code** 기준으로 작성된 코드입니다.

## 사용 방법



1. `git clone https://github.com/rimgosu/AutoAttendance.git`
   - 깃 클론으로 코드를 다운로드 받아주세요.
   - VS 코드를 열어 폴더로 열어주세요.

2. `pip install -r requirements.txt`
   - 터미널에 다음 코드를 입력하면 자동으로 셀레니움 최신버전을 설치합니다.
   - 만약 구 버전의 셀레니움이 깔려있다면 제거하고 위 코드를 다시 실행시켜주세요.
  
3. `idpw입력.json`
   - C:\keys\idpw입력.json 파일을 생성해주세요.
   - 엘리스의 아이디와 패스워드를 입력해주세요.
   - 다음 json 파일의 양식은 다음과 같습니다.
  
```
{
    "email" : "이메일주소 입력",
    "password" : "비밀번호 입력"
}
```
  
4. `자동출석cmd.txt`
   - 여기에 있는 예시 코드를 자신이 설치한 폴더의 RunAutoAttendance.py 경로로 일치시켜주세요.
   - 파이썬 버전도 맞춰주세요.
  
5. 검색-cmd로 명령프롬프트를 켜 주세요

6. `cd (설치된 경로)`
   - 다음 코드로 설치된 경로로 cmd 파일을 켜주세요.
   - 그 후 자동출석cmd.txt에서 고친 코드를 복사 붙여넣기 하면 됩니다.

   ![image](https://github.com/rimgosu/AutoAttendance/assets/120752098/389aaca5-1ef9-4ad1-96c1-5e46b40decd2)

7. `*************AutoAttendence is running...*************` 문구가 뜨면 정상적으로 작동하고 있는 것입니다.

## TODO
- AWS Lambda를 이용해 컴퓨터를 끄고도 자동으로 출석과 퇴실 버튼이 눌러지게끔 하자.
  
## 릴리즈 노트
### 2023.10.05
- 첫 출시

### [2023.10.10](https://github.com/rimgosu/AutoAttendance/tree/621cd3e6e8ddbc288714ad64d32bd05de11d34ee)
- id,pw 입력을 C:/keys/idpw입력.json으로 입력하여 보안 업그레이드
- 엘리스의 div 구조가 변경되어, attendence_button을 XPATH로 찾습니다.

```
try:
  attendance_button = driver.find_element(By.XPATH, "//button[contains(text(),'출석')]")
except:
  attendance_button = driver.find_element(By.XPATH, "//button[contains(text(),'퇴실')]")
```



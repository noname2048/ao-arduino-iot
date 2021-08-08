# ao-arduino-iot

- DHT22 센서와 아두이노를 이용해 내방의 온습도를 UDP로 쏘자
- UDP로 쏜 데이터는 실시간 데이터베이스에 쌓여서 차트로 어딘가(?) 그려볼 예정

## 1. 사진들

![](images/01_temperature.png)

## 2. 사용라이브러리

- 아두이노 DHT22 (1.4.2v) 공식 센서 라이브러리
- lcd 라이브러리

## 3. tip

- secret_example.hpp 는 구동시 secret.hpp 로 변경해주세요
- vscode 설정을 참조하세요. 대부분이 자동완성이 됩니다.
- vscode로 코딩하지만, upload와 시리얼모니터는 IDE를 사용합니다. (동시에 켜놓고 사용)
- vscode 설정시, 아두이노 lib를 설치하고, includePath와 define을 유의하세요
- vscdoe 에서 업로드와 verify등을 진행하면, c_cpp설정관련 json이 초기화되어 이러한 방법을 사용합니다.


#### AT 명령어 순서

- AT
- AT+CWMODE=1
- AT+CWJAP?
- AT+CWJAP=
- AT+CIFSR
- AT+CIPSTART="UDP"


## postgresql DB 세팅

- 공식문서에 따르면 collate의 경우 initdb 시에 조치가 필요하다
- 안믿고 CREATE DATABASE iot TEMPALTE tempate0 LC_COLLATE "C" LC_CTYPE "ko_KR.UTF8" 시도
- invalid locale "ko_KR.UTF8" 나옴
- psql 로 해결이 안될것 같아서 바로 dockerhub 로 달려감
- 문서를 보던중 따로 Dockerfile로 FROM으로 당겨와 localedef 를 RUN 하는 것 확인
- 비슷하게 ko_KR로 언어만 바꿨는데 localedef 설정이 이상하다고 안됌
- 아, en_US로 되도 정렬만 잘되면 상관없자너? 하고 확인해 볼까 했지만 아닌것 같음
- 공식 dockerfile 뜯어보는중
- 결국 한 [블로그](https://postgresql.kr/blog/when_useing_docker_official_postgres_image.html) 를 통해 기존에 한번 썼었던것 같던 방법을 사용하기로 했다
- 이게 알파인 계열, 데비안 게열로 나뉘는데, locale은 default로, locale 설정은 데비안만 가능하다
- 일단 localedef를 검색해봤는데 잘 모르겠다.
- -f는 캐릭터셋 지정. utf-8
- -i는 로케일 정의 파일 지정, 풀패스는 [블로그](http://egloos.zum.com/sunnmoon/v/2758947) 에서 ko_KR 지정시 /usr/share/i18n/locales/ko_KR 이라고 한다.
- `localedef -f UTF-8 -i ko_KR ko_KR.UTF-8` 확인
- 또 다른 [블로그](https://bs-secretroom.blogspot.com/2012/10/locale.html) 에서 우분투는 locale-gen을, 레드헷은 localedef를 사용하여 locale을 설정한다는 정보 발견
- /usr/share/i18n/locales/ko_KR 이 있어야 한다는 정보도 발견
- localedef --help를 통해 -c옵션이 경고메시지 출력이라는 것을 알아차림
- locale-gen에 대해 검색하다가 익숙한 [블로그](https://www.44bits.io/ko/post/setup_linux_locale_on_ubuntu_and_debian_container) 발견
- 여기서 locale-gen은 내부적으로 localedef 사용한다고 함
- 근데 localedef가 안먹혀서, 결국 다시 locale-gen 쪽으로 회귀.
- 서버 로그는 영문으로 보고 싶은데 잘 안된다
- 이후 psql -h localhost -U postgres -p 15001 로 접속
- \l
- show timezone;
- create datebase iot;
- 초기화 메세지를 보면서.. COLLATE CTYPE MESSAGES MONETARY NUMERIC TIME 중 MESSAGES를 en_US로 바꾸면 되지 않을까 생각함
- LC_MESSAGES 를 바꾸어 보았으나 나오지 않음.ㅠ
- 나중에 고수분을 만나면 물어보는것으로...
- health check 부분에서 PGPASSWORD= 를 빼기로 결정

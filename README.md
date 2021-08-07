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
- 
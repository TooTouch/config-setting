# config-setting
How to set configurations.

# argparse

```
pip install argparse
```

**장점**
- metavar를 통한 argument 의미 설정
- type & default 지정
- help를 통한 argument 설명
- choices를 통해 선택 후보 설정
- action 기능을 사용하여 on-off 기능

**단점**
- 한 눈에 확인하기 어려움
- 계층적으로 사용할 수 없음


# omegaconf

```
pip install omegaconf
```

**장점**
- yaml 파일 사용 간편함 
- yaml은 계층적으로 argument를 구분할 수 있음
- 기본값을 두고 사용할 때 직관적임
- `from_cli`를 사용하여 argparse와 같이 추가적인 argument를 받아올 수 있음

**단점**
- 변수에 대한 설명을 달기 불편함
- argparse의 choices와 같은 기능이 없음
- argument에 대한 타입 설정이 없음


# Fire

```
pip install fire
```

**장점**
- 함수에 필요한 argument를 바로 지정할 수 있음
- 함수에 필요한 config를 따로 정의할 필요가 없음

**단점**
- argument를 계층적으로 구분할 수 없음
- argument가 많아지만 코드가 지저분해짐
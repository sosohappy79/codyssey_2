
# clone 실습 테스트 문구 추가

# 나만의 퀴즈 게임

Python 기본 문법과 표준 라이브러리만 사용해 만드는 콘솔 퀴즈 게임입니다.

## 프로젝트 개요

이 프로젝트는 Python 기초 문법과 Git 사용법을 연습하기 위해 제작합니다.

## 실행 방법

프로젝트 루트 폴더에서 다음 명령어를 실행합니다.

```bash
python main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 추가 및 목록 확인
- 최고 점수 확인

## 파일 구조

```text
my-quiz-game/
├── .gitignore
├── README.md
├── main.py
└── models/
    ├── __init__.py
    ├── quiz.py
    └── quiz_game.py
```

## 데이터 파일 설명

게임 데이터는 프로젝트 루트의 `state.json`에 저장할 예정입니다.

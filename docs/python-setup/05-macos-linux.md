# 05. macOS / Linux에서 Python 설치하기

uv는 macOS·Linux에서도 사용할 수 있다. **설치 명령과 Python 실행 파일 경로만 다르고, `uv venv` 같은 주요 명령은 Windows와 같다.**

## 1. uv 설치 (터미널)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. 터미널을 새로 열어 확인

```bash
uv --version
```

## 3. 작업 폴더 만들기

```bash
mkdir python-study
```

## 4. 작업 폴더로 이동

```bash
cd python-study
```

## 5. Python 가상환경 생성

```bash
uv venv
```

## 6. Python 버전 확인

```bash
.venv/bin/python --version
```

## 7. Python 실행 확인

```bash
.venv/bin/python -c "print('Hello, Python!')"
```

> 📷 **화면 캡처 자리:** macOS/Linux 터미널에서 uv 설치 확인, 가상환경 생성, Python 실행 결과

기본 가상환경은 `.venv`에 생성된다. 특정 Python 버전이 필요하면 `uv venv --python 3.11`처럼 지정한다.

[Windows 설치 안내로 돌아가기](README.md) · [가상환경 구조](01-install.md)

공식 자료: [uv 설치](https://docs.astral.sh/uv/getting-started/installation/)

# Python 설치 및 실행환경 구성

Windows 기준 실습 가이드. Python은 [python.org](https://www.python.org/downloads/)에서 설치할 수도 있지만, 여기서는 **uv**로 설치·관리한다.

**uv**는 Windows·macOS·Linux에서 작동하는 빠른 Python 관리 도구다.

| 장점 | 설명 |
|---|---|
| 간편함 | 명령어로 Python·가상환경·패키지 관리 |
| 자동 설치 | 필요한 Python 버전이 없으면 다운로드 |
| 여러 버전 | 프로젝트마다 다른 Python 환경 사용 |
| 빠른 속도 | 패키지 설치와 캐시 재사용 |
| AI 협업 | 설치·실행·오류 확인 절차를 명령어로 공유 |

## Windows에서 시작하기 (PowerShell)

~~~powershell
# 1. uv 설치
winget install --id=astral-sh.uv -e

# 2. PowerShell을 새로 열어 확인
uv --version

# 3. 작업 폴더 생성
mkdir python-study
cd python-study

# 4. Python 가상환경 생성
uv venv

# 5. Python 실행 확인
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "print('Hello, Python!')"
~~~

> 📷 **화면 캡처 자리:** PowerShell에서 `uv --version`, `uv venv`, `Hello, Python!` 실행 결과

`uv venv`는 사용 가능한 Python을 활용하고, 없으면 자동으로 다운로드한다. 기본 가상환경은 `.venv` 폴더에 생성된다. **반드시 최신 Python을 선택하는 것은 아니다.**

특정 버전이 필요하면:

~~~powershell
uv venv --python 3.11
~~~

## macOS / Linux

~~~bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
mkdir python-study && cd python-study
uv venv
.venv/bin/python --version
~~~

> 📷 **화면 캡처 자리:** macOS/Linux에서 uv 설치 확인 및 Python 버전 출력

## 자세히 보기

- [02. Python·가상환경과 생성 파일](02-install.md)
- [03. 패키지 설치·관리](03-packages.md)
- [04. 프로젝트 생성·환경 재현](04-projects.md)
- [05. 자주 발생하는 오류](05-troubleshooting.md)

**참고:** uv를 설치해도 Git은 함께 설치되지 않는다. Git·GitHub는 별도로 다룬다.

공식 자료: [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) · [Python 자동 설치](https://docs.astral.sh/uv/guides/install-python/)

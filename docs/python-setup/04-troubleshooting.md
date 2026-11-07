# 04. 자주 발생하는 오류

Windows PowerShell 기준. **오류 메시지를 먼저 읽고, 설치 경로와 실행 Python을 확인한다.**

| 증상 | 확인·해결 |
|---|---|
| `uv` 명령을 찾을 수 없음 | 설치 후 **새 PowerShell**을 열고 `uv --version` 확인 |
| `winget` 명령이 없음 | Windows App Installer 확인 또는 [uv 공식 설치 방법](https://docs.astral.sh/uv/getting-started/installation/) 사용 |
| `python`이 실행되지 않음 | `uv run python --version`으로 확인 |
| `ModuleNotFoundError` | `uv pip list`와 `sys.executable`로 환경 확인 |
| 특정 Python 버전이 필요함 | `uv venv --python 3.11`로 새 환경 생성 |
| 패키지 설치 실패 | 네트워크, 패키지 이름, 지원 Python 버전 확인 |
| VS Code에서 import 오류 | **Python: Select Interpreter**에서 `.venv` 선택 |
| PowerShell 활성화 스크립트 오류 | 활성화 없이 `uv run python` 사용 |

## 확인 명령

~~~powershell
uv --version
uv python list
uv run python --version
uv run python -c "import sys; print(sys.executable)"
uv pip list
uv pip check
~~~

> 📷 **화면 캡처 자리:** `uv` 미인식 또는 `ModuleNotFoundError` 메시지와 수정 후 정상 실행 화면

## 패키지를 설치했는데 import되지 않는다?

~~~powershell
uv pip install requests
uv run python -c "import requests; print(requests.__version__)"
~~~

명령을 실행한 폴더에 `.venv`가 있는지 먼저 확인한다.

## GPU 라이브러리가 설치되지 않는다?

Python 버전뿐 아니라 **OS, GPU 드라이버, CUDA 및 라이브러리 빌드**의 호환성도 확인한다. uv가 GPU 드라이버까지 설치해 주는 것은 아니다.

## AI에게 오류를 질문할 때

다음 세 가지를 함께 제공하면 해결이 빨라진다.

1. 실행한 **명령어**
2. **전체 오류 메시지**
3. `uv --version` 및 `sys.executable` 결과

> 비밀번호, 토큰, 개인 경로 등 민감한 정보는 AI에게 보내기 전에 제거한다.

관련 문서: [설치 안내](README.md) · [가상환경](01-install.md)

# 04. 자주 발생하는 오류

Windows PowerShell 기준. **같은 명령을 반복 설치하기 전에 오류 메시지, 실행환경과 설치 경로부터 확인한다.**

## 증상별 해결 방법

| 증상 | 확인할 내용 |
|---|---|
| PowerShell에서 `uv`를 찾지 못함 | 설치 후 새 PowerShell을 연다. 그래도 안 되면 설치·PATH 확인 |
| VS Code 터미널에서 `uv`를 찾지 못함 | uv 설치 후 **VS Code를 완전히 종료하고 다시 연다** |
| `winget`이 없음 | Windows App Installer 확인 또는 [uv 공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/) |
| `python` 명령이 다른 버전을 실행함 | 직접 `python` 대신 프로젝트에서 `uv run python` 사용 |
| `ModuleNotFoundError` | 현재 Python 환경을 확인하고 [02장](02-packages.md)의 `uv add`로 의존성 기록 |
| VS Code에서 import 오류 | **Python: Select Interpreter**에서 프로젝트의 `.venv` 선택 |
| PowerShell 활성화 스크립트 오류 | 활성화 대신 `uv run`으로 실행 |
| 패키지 설치 실패 | 패키지 이름, 인터넷 연결, Python 버전 지원 여부 확인 |

`Failed to hardlink files` 경고는 캐시와 가상환경이 서로 다른 드라이브에 있을 때 발생할 수 있다. **설치가 정상 완료됐다면 오류가 아니다.** 용량·캐시 관련 설명은 [06장](06-advanced.md)을 참고한다.

## 문제 진단에 필요한 명령

**uv 설치 확인**

```powershell
uv --version
```

**실제로 실행되는 Python 확인**

```powershell
uv run python -c "import sys; print(sys.executable)"
```

**설치된 패키지의 의존성 이상 여부 확인**

```powershell
uv pip check
```

## 패키지를 설치했는데 import되지 않을 때

1. `pyproject.toml`이 있는 **프로젝트 폴더에서** 실행하고 있는지 확인한다.
2. `sys.executable` 결과가 예상한 `.venv` 경로인지 확인한다.
3. 프로젝트에 필요한 패키지가 누락되었다면 [02장의 `uv add` 방법](02-packages.md#패키지-설치와-관리)을 사용한다. 단순히 `uv pip install`만 하면 프로젝트 설정에 기록되지 않는다.

## GPU 패키지가 설치되지 않을 때

Python 버전뿐 아니라 **운영체제, GPU 드라이버, CUDA, 라이브러리 빌드** 호환성도 확인한다. uv 자체가 GPU 드라이버까지 설치하는 것은 아니다.

## AI에게 오류를 질문할 때

실행한 **명령어**, **전체 오류 메시지**, **Python 실행 경로**를 함께 알려주면 진단이 쉬워진다. 비밀번호·토큰·개인정보가 들어 있다면 전송 전에 제거한다.

**uv 자체를 업데이트해야 한다면?** [06. 고급 활용 Q&A](06-advanced.md#q3-uv-버전은-매번-업데이트해야-하나--e는-무슨-뜻인가)를 참고한다.

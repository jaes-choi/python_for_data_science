# 01. Python과 가상환경

앞의 [Quick Tour](README.md)에서 Python을 실행했다면, 여기서는 **그 실행환경이 무엇인지 이해**하면 된다. 설치 절차를 반복하지 않는다.

## Python과 가상환경은 무엇이 다를까?

- **Python**: 작성한 코드를 실행하는 프로그램(인터프리터)
- **가상환경(`.venv`)**: 프로젝트마다 Python 실행파일과 설치 패키지를 분리하는 환경
- **uv**: Python 설치, 가상환경 생성, 패키지 관리를 도와주는 도구

프로젝트마다 서로 다른 패키지 버전이 필요해도 가상환경을 나누면 충돌을 줄일 수 있다.

## 앞의 가상환경을 그대로 사용하기

[Quick Tour](README.md)에서 `python-study` 폴더로 이동하고 `uv venv`를 실행했다면 **아래 명령을 다시 실행하지 않는다.**

`python-study` 폴더에서 아직 가상환경을 만들지 않았을 때만 `#`을 지우고 실행한다.

```powershell
# uv venv
```

`#`은 PowerShell에서 **주석**을 뜻한다. 주석 처리된 줄은 실행되지 않는다. 새로운 폴더에서 처음 시작하는 학생은 먼저 [Quick Tour의 폴더 생성·이동 단계](README.md#windows에서-시작하기-powershell)를 따라 한다.

## `.venv` 안에는 무엇이 있을까?

```text
python-study/
└── .venv/
    ├── pyvenv.cfg        # Python 환경 설정
    ├── .gitignore        # Git 제외 설정
    ├── Scripts/          # Windows: python.exe 등
    └── Lib/
        └── site-packages/ # 설치된 패키지
```

운영체제와 Python 구성에 따라 실제 파일은 다를 수 있다. macOS/Linux에서는 보통 `Scripts/` 대신 `bin/`을 사용한다.

**폴더 내부 확인**

```powershell
Get-ChildItem -Force .venv
```

![실제 가상환경 파일 목록](images/07-venv-files.png)

**지금 실행하는 Python의 위치 확인**

```powershell
uv run python -c "import sys; print(sys.executable)"
```

정상적으로 `.venv`가 선택되었다면 Windows에서는 경로에 `python-study\.venv\Scripts\python.exe`가 포함된다. Python 가상환경을 별도로 활성화하지 않아도 `uv run`으로 실행할 수 있다.

다른 Python 버전이나 기존 Anaconda를 다루는 방법은 [06. 고급 활용 Q&A](06-advanced.md)를 참고한다.

관련 문서: [패키지 관리](02-packages.md) · [문제 해결](04-troubleshooting.md)

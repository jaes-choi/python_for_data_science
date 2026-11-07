# 01. Python과 가상환경

## 가상환경이란?

프로젝트마다 **Python과 패키지를 분리하는 폴더**다. 다른 프로젝트와 패키지 버전이 달라도 서로 충돌하지 않는다.

## 만들고 확인하기 (Windows PowerShell)

~~~powershell
mkdir python-study
cd python-study
uv venv
uv run python --version
~~~

- `uv venv`: 사용 가능한 Python을 선택한다. 없으면 자동 다운로드한다.
- `uv venv --python 3.11`: 특정 버전 지정
- `uv python list`: 사용 가능한 Python 버전 확인

![가상환경 생성](images/03-venv-create.png)

![Python 버전 확인](images/04-python-version.png)

## 기존 Python이나 Anaconda를 사용한다면?

**기존 프로그램을 삭제할 필요가 없다.** uv는 설치된 Python을 찾아 사용할 수 있다.

**설치된 Python 확인**

```powershell
uv python list --only-installed
```

**기존 Python 3.12로 새 가상환경 만들기** (해당 버전이 설치된 경우)

```powershell
uv venv --no-managed-python --python 3.12
```

`--no-managed-python`은 uv가 내려받은 Python 대신 기존에 설치된 Python만 사용하도록 한다. 버전을 지정하지 않은 `uv venv`는 uv가 관리하는 Python을 우선 선택할 수도 있다.

**Anaconda 사용자라면?** 기존 Conda 프로젝트는 그대로 유지한다. 새 Python 입문 실습에서는 Conda 환경을 비활성화한 뒤 별도 폴더에서 uv를 사용한다.

```powershell
conda deactivate
```

Conda 환경이 활성화된 상태에서 `uv pip install`을 실행하면 해당 Conda 환경에 패키지가 설치될 수 있다. **Conda의 `base` 환경과 uv의 `.venv`를 혼용하지 않는 것**을 권장한다.

## .venv 안에는 무엇이 있나?

~~~text
python-study/
└── .venv/
    ├── pyvenv.cfg        # Python 환경 설정
    ├── .gitignore        # 가상환경을 Git 관리 대상에서 제외
    ├── Scripts/          # Windows: python.exe, 실행 스크립트 등
    └── Lib/
        └── site-packages/ # 설치된 패키지
~~~

운영체제·Python 구성에 따라 세부 파일은 다를 수 있다. macOS/Linux에서는 `Scripts/` 대신 `bin/`, 패키지 경로는 보통 `lib/pythonX.Y/site-packages/`다.

~~~powershell
Get-ChildItem -Force .venv
uv run python -c "import sys; print(sys.executable)"
~~~

![PowerShell에서 확인한 실제 .venv 파일 목록](images/07-venv-files.png)

**Q. 가상환경을 활성화해야 하나?**  
A. 필수는 아니다. `uv run python`으로 실행한다.

**Q. `python` 명령이 다른 버전을 실행한다면?**  
A. `uv run python`을 사용한다. 실제 실행 경로는 `uv run python -c "import sys; print(sys.executable)"`로 확인한다.

**Q. VS Code에서는?**  
A. **Python: Select Interpreter**에서 `.venv\Scripts\python.exe`를 선택한다.

macOS/Linux에서도 `uv run python`을 사용한다. 실제 실행 파일 경로는 `.venv/bin/python`이다.

관련 문서: [README](README.md) · [패키지 관리](02-packages.md)

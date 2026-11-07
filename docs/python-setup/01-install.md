# 01. Python과 가상환경

## 가상환경이란?

프로젝트마다 **Python과 패키지를 분리하는 폴더**다. 다른 프로젝트와 패키지 버전이 달라도 서로 충돌하지 않는다.

## 만들고 확인하기 (Windows PowerShell)

~~~powershell
mkdir python-study
cd python-study
uv venv
.\.venv\Scripts\python.exe --version
~~~

- `uv venv`: 사용 가능한 Python을 선택한다. 없으면 자동 다운로드한다.
- `uv venv --python 3.11`: 특정 버전 지정
- `uv python list`: 사용 가능한 Python 버전 확인

> 📷 **화면 캡처 자리:** `uv venv` 생성 메시지와 Python 버전 출력

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
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
~~~

> 📷 **화면 캡처 자리:** 파일 탐색기에서 `.venv` 폴더와 `pyvenv.cfg` 확인

**Q. 가상환경을 활성화해야 하나?**  
A. 필수는 아니다. uv는 현재 폴더의 `.venv`를 찾아 사용하며, Python 실행 파일을 직접 지정해도 된다.

**Q. `python` 명령이 다른 버전을 실행한다면?**  
A. `.\.venv\Scripts\python.exe`를 사용하면 해당 프로젝트의 Python을 실행한다.

**Q. VS Code에서는?**  
A. **Python: Select Interpreter**에서 `.venv\Scripts\python.exe`를 선택한다.

macOS/Linux 실행 파일: `.venv/bin/python`

관련 문서: [README](README.md) · [패키지 관리](02-packages.md)

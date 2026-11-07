# 02. 패키지 설치·관리

외부 패키지는 **가상환경을 만든 폴더에서** 설치한다. 실행에는 `uv run`을 사용한다.

## 기본 명령 (Windows PowerShell)

~~~powershell
uv venv                           # 최초 1회: .venv 생성
uv pip install requests           # 설치
uv pip list                       # 설치 목록
uv pip show requests              # 패키지 정보
uv pip install --upgrade requests # 업데이트
uv pip check                      # 의존성 충돌 검사
~~~

설치 후 바로 확인한다.

~~~powershell
uv run python -c "import requests; print(requests.__version__)"
~~~

> 📷 **화면 캡처 자리:** `uv pip install requests`와 `uv pip list` 실행 결과

## 여러 패키지와 버전 지정

~~~powershell
uv pip install requests pandas
uv pip install "requests==2.32.3"
uv pip uninstall requests
~~~

`uv pip install`은 현재 가상환경에 패키지를 설치하지만, 프로젝트의 `pyproject.toml`이나 `uv.lock`을 자동 수정하지 않는다. 프로젝트 의존성은 [03. 프로젝트 관리](03-projects.md)의 `uv add`를 사용한다.

## Jupyter Notebook (선택)

~~~powershell
uv pip install notebook ipykernel
uv run jupyter notebook
~~~

> 📷 **화면 캡처 자리:** 브라우저에서 실행된 Jupyter Notebook 첫 화면

VS Code의 Notebook에서는 커널을 선택할 때 해당 `.venv` Python을 고른다.

**Q. 설치했는데 `import`가 실패한다면?**  
A. 실행 중인 Python과 설치한 환경이 같은지 확인한다.

~~~powershell
uv run python -c "import sys; print(sys.executable)"
uv pip show requests
~~~

관련 문서: [가상환경](01-install.md) · [오류 해결](04-troubleshooting.md)

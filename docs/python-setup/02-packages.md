# 02. 패키지 설치·관리

**기본 권장: `uv add`** — 패키지를 설치하면서 프로젝트의 준비물 목록도 기록한다.

## 패키지 추가 (Windows PowerShell)

기존 `python-study` 폴더에서 프로젝트 설정을 만든다. (처음 1회)

```powershell
uv init --no-package
```

`requests` 설치:

```powershell
uv add requests
```

![uv add로 패키지 설치하는 예](images/09-project-add.png)

설치 확인:

```powershell
uv run python -c "import requests; print(requests.__version__)"
```

## 왜 uv add를 권장할까?

- `pyproject.toml`: 프로젝트에 **어떤 패키지가 필요한지** 기록
- `uv.lock`: 실제로 사용할 **패키지 버전** 기록
- 다른 컴퓨터에서 `uv sync`로 환경 재구성 가능

```powershell
uv sync
```

`pyproject.toml`과 `uv.lock`을 소스코드와 함께 GitHub에 올린다. `.venv`는 올리지 않는다.

## 관리 명령

**패키지 추가**

```powershell
uv add pandas
```

**패키지 삭제**

```powershell
uv remove pandas
```

**의존성 목록**

```powershell
uv tree
```

## `uv pip install`과의 차이

| 명령 | 차이 |
|---|---|
| `uv add requests` | 설치 + **필요한 패키지 기록** (권장) |
| `uv pip install requests` | 현재 `.venv`에만 설치, 프로젝트 설정에는 기록하지 않음 |

단순한 일회성 실습에서는 `uv venv`를 만든 뒤 `uv pip install`을 사용할 수도 있다.

```powershell
uv pip install requests
```

![uv pip install 설치 예](images/06-install-requests.png)

```powershell
uv pip list
```

![설치된 패키지 목록](images/06b-pip-list.png)

> 캐시와 가상환경이 다른 드라이브에 있으면 파일 링크 대신 복사로 전환된다는 경고가 나올 수 있다. 설치가 성공했다면 오류가 아니다.

**중요:** `uv pip install`만으로 추가한 패키지는 프로젝트 의존성에 기록되지 않는다. `uv sync`는 기본적으로 **잠금 파일에 없는 패키지를 제거**할 수 있다. 실습 후 계속 사용할 패키지는 `uv add`로 기록한다. [uv 공식 동기화 설명](https://docs.astral.sh/uv/concepts/projects/sync/) 참고.

## Jupyter Notebook (선택)

Jupyter는 Python 입문 필수 프로그램이 아니다. **필요할 때만** 사용하면 설치·프로젝트 의존성을 줄일 수 있다.

**가끔 사용한다면 — JupyterLab을 프로젝트 의존성에 추가하지 않고 실행 (공식 권장 예시)**

```powershell
uv run --with jupyter jupyter lab
```

이 방식은 Jupyter 실행에 필요한 환경을 별도로 준비한다. 패키지는 uv 캐시에 저장될 수 있지만 프로젝트의 `pyproject.toml`에는 추가하지 않는다.

**Notebook 화면을 프로젝트에서 계속 사용한다면**

```powershell
uv add --dev notebook ipykernel
```

```powershell
uv run jupyter notebook
```

`--dev`는 Jupyter 같은 개발·학습용 도구를 일반 실행 의존성과 구분해 기록한다. 아래는 실제 브라우저에서 실행한 Notebook 화면이다.

![Jupyter Notebook 실행 및 코드 출력](images/11-jupyter-notebook.png)

VS Code에서 `.ipynb` 노트북을 실행할 때는 프로젝트에 `ipykernel`이 필요하다. **Python: Select Interpreter/Select Kernel**에서 프로젝트의 `.venv`를 선택한다. [uv 공식 Jupyter 안내](https://docs.astral.sh/uv/guides/integration/jupyter/) 참고.

## VS Code에서 Python 실행 (선택)

[VS Code](https://code.visualstudio.com/)를 설치한 뒤 `python-study` 폴더에서 실행한다.

```powershell
code .
```

`hello.py` 파일 작성:

```python
print("Hello from VS Code!")
```

VS Code 터미널에서 실행:

```powershell
uv run hello.py
```

![VS Code에서 Python 실행 결과](images/12-vscode-hello.png)

**Python: Select Interpreter**에서 `.venv`를 선택한다. `code` 명령이 인식되지 않으면 VS Code의 **파일 → 폴더 열기**를 사용한다.

**Q. 설치했는데 `import`가 실패한다면?**  
A. 실행 중인 Python과 설치한 환경이 같은지 확인하고, 프로젝트에서는 `uv add`로 설치했는지 점검한다.

~~~powershell
uv run python -c "import sys; print(sys.executable)"
uv tree
~~~

관련 문서: [가상환경](01-install.md) · [오류 해결](04-troubleshooting.md)

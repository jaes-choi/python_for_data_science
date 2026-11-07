# 02. 패키지 관리와 개발 도구

이 장의 목표는 **필요한 패키지를 설치·기록**하고, VS Code와 Notebook에서 사용하는 방법을 익히는 것이다. 새 프로젝트의 전체 구조와 GitHub 재현은 [03장](03-projects.md)에서 다룬다.

## 실습 환경 준비 (Windows PowerShell)

[Quick Tour](README.md)에서 사용한 `python-study` 폴더 안에서 진행한다. 앞에서 `uv venv`를 만들었다면 **다시 만들지 않는다.**

이 폴더에 `pyproject.toml`이 **아직 없을 때만** 다음 명령을 한 번 실행한다.

```powershell
uv init --no-package
```

`uv init`은 기존 폴더에 **프로젝트 설정**을 추가한다. `uv add`는 이렇게 초기화된 프로젝트에서 사용한다.

## 패키지 설치와 관리

**프로그램에서 사용하는 패키지 추가**

```powershell
uv add requests
```

![실제 uv add 실행 결과](images/09-project-add.png)

**설치 확인**

```powershell
uv run python -c "import requests; print(requests.__version__)"
```

`uv add`는 패키지를 설치하면서 `pyproject.toml`에 필요 패키지를, `uv.lock`에 확정된 의존성 정보를 기록한다.

**의존성 목록 확인**

```powershell
uv tree
```

**패키지가 더 이상 필요 없으면 제거 (선택)**

```powershell
uv remove requests
```

`uv remove`를 실행했다면 이후에는 `requests`를 가져오는 코드가 동작하지 않는다. 다른 컴퓨터에서 같은 환경을 만드는 방법은 [03장](03-projects.md)을 참고한다.

## `uv pip install`과 무엇이 다를까?

| 명령 | 차이 |
|---|---|
| `uv add requests` | 프로젝트의 필요 패키지로 **기록하고 설치** — 기본 권장 |
| `uv pip install requests` | 선택된 가상환경에 **설치만** 하고 프로젝트 의존성에는 기록하지 않음 |

프로젝트를 따로 만들지 않고 **일회성 가상환경만 사용하는 경우**에는 아래 명령도 가능하다.

```powershell
uv pip install requests
```

![가상환경에 uv pip install을 실행한 예](images/06-install-requests.png)

**설치된 패키지 목록 확인**

```powershell
uv pip list
```

![설치된 패키지 목록](images/06b-pip-list.png)

`uv pip install`만으로 추가한 패키지는 나중에 `uv sync`를 실행하면 제거될 수 있으므로 **지속적으로 사용할 프로젝트에는 `uv add`를 권장**한다.

## VS Code에서 Python 파일 실행 (선택)

[VS Code](https://code.visualstudio.com/)와 **Python 확장**을 설치하고 `python-study` 폴더를 연다.

```powershell
code .
```

`hello.py` 파일을 만들고 다음 코드를 작성한다.

```python
print("Hello from VS Code!")
```

VS Code 터미널에서 실행한다.

```powershell
uv run hello.py
```

![VS Code에서 Python 실행 결과](images/12-vscode-hello.png)

VS Code의 **Python: Select Interpreter**에서 프로젝트의 `.venv`를 선택한다. `code` 명령이 인식되지 않으면 **파일 → 폴더 열기**로 연다.

## VS Code에서 Notebook 실행: `--dev` 이해하기 (선택)

VS Code의 **Python 확장 + Jupyter 확장**을 이용하면 별도의 Jupyter Notebook 서버를 설치하지 않고도 `.ipynb` 파일을 실행할 수 있다. 선택한 Python 환경에는 **`ipykernel`**이 필요하다.

`--dev`는 **개발·학습할 때 사용하는 패키지를 따로 분류하여 기록**하는 옵션이며, 설치를 생략한다는 뜻은 아니다.

| 명령 | 기록 위치 | 용도 |
|---|---|---|
| `uv add requests` | `[project].dependencies` | 프로그램 실행용 |
| `uv add --dev ipykernel` | `[dependency-groups].dev` | Notebook 등 개발·학습용 |

**개발용 커널 설치**

```powershell
uv add --dev ipykernel
```

`pyproject.toml`에는 대략 다음과 같이 **두 종류의 의존성이 구분**되어 기록된다.

```toml
[project]
dependencies = ["requests"]

[dependency-groups]
dev = ["ipykernel"]
```

위 코드는 구분을 보여주는 예시이며, 앞에서 `uv remove requests`를 실행했다면 실제 내용은 다르다.

VS Code에서 `.ipynb` 파일을 열고 오른쪽 위의 **Select Kernel → Python Environments → 프로젝트의 `.venv`**를 선택하여 셀을 실행한다.

참고로 `uv sync`는 개발용 패키지도 기본적으로 설치한다. 아래처럼 실행하면 개발용 패키지는 제외되며, Notebook이 필요할 때는 다시 포함해야 한다.

```powershell
uv sync --no-dev
```

`uv venv`만 있고 `pyproject.toml`이 없는 일회성 실습이라면 `uv pip install ipykernel`을 이용할 수도 있다. [공식 VS Code Notebook 안내](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## 브라우저에서 JupyterLab 실행 (선택)

**VS Code가 아니라 브라우저에서 Notebook을 실행할 때만** Jupyter 서버가 필요하다. 프로젝트의 일반 의존성에 추가하지 않고 임시로 실행할 수 있다.

```powershell
uv run --with jupyter jupyter lab
```

아래는 **브라우저**에서 실행한 실제 Jupyter Notebook 화면이다. VS Code 실행 화면이 아니다.

![브라우저 Jupyter Notebook 실행 결과](images/11-jupyter-notebook.png)

패키지 오류가 나면 [04. 문제 해결](04-troubleshooting.md)을 참고한다. [uv 공식 프로젝트 의존성 관리](https://docs.astral.sh/uv/concepts/projects/dependencies/)

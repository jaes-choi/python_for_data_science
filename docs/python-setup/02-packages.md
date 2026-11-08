# 02. 패키지 관리와 개발 도구

[Quick Tour](README.md)에서 `uv init --no-package python-study`로 프로젝트를 만들고 `uv add --dev ipykernel`로 개발용 패키지를 설치했다. 여기서는 **패키지 추가·제거와 의존성 기록**을 더 자세히 알아본다.

## 필요한 패키지 추가하기

`python-study` 폴더에서 실행한다. **이미 프로젝트를 만들었다면 `uv init`이나 `uv venv`를 다시 실행하지 않는다.** 프로젝트 설정 파일(`pyproject.toml`)이 없는 경우에만 [03장의 프로젝트 생성 안내](03-projects.md)를 참고한다.

**프로그램에서 사용할 패키지 추가**

```powershell
uv add requests
```

![uv add 실행 결과 예시](images/09-project-add.png)

**설치 확인**

```powershell
uv run python -c "import requests; print(requests.__version__)"
```

`uv add`는 `pyproject.toml`에 필요한 패키지를 기록하고, `uv.lock`에 확정한 의존성 버전을 보관한다.

**의존성 목록 확인**

```powershell
uv tree
```

**패키지 제거 (선택)**

```powershell
uv remove requests
```

제거했다면 이후 코드에서 `import requests`는 실행되지 않는다.

## `--dev`는 무엇인가?

`--dev`는 **개발·학습 과정에서 사용할 패키지를 따로 분류하는 옵션**이다. 설치하지 않는다는 뜻이 아니다.

| 명령 | 역할 |
|---|---|
| `uv add requests` | 프로그램 실행에 필요한 패키지 |
| `uv add --dev ipykernel` | VS Code Notebook 실행을 위한 개발·학습용 도구 |

`pyproject.toml`에서는 대략 다음과 같이 구분된다.

```toml
[project]
dependencies = ["requests"]

[dependency-groups]
dev = ["ipykernel"]
```

위 내용은 구조 설명용 예시다. 이미 패키지를 제거했다면 실제 파일 내용과 다르다.

`uv sync`는 기본적으로 개발용 패키지도 설치하지만, 필요하지 않은 환경에서는 제외할 수 있다.

```powershell
uv sync --no-dev
```

## `uv pip install`과의 차이

| 명령 | 의미 |
|---|---|
| `uv add requests` | 프로젝트 의존성으로 기록하고 설치 (**권장**) |
| `uv pip install requests` | 선택한 가상환경에 설치하지만 프로젝트 설정에는 기록하지 않음 |

프로젝트를 만들지 않고 가상환경만 사용하는 **일회성 실습**이라면 다음 명령도 사용할 수 있다.

```powershell
uv pip install requests
```

![uv pip install의 실제 설치 화면](images/06-install-requests.png)

**현재 가상환경의 패키지 목록**

```powershell
uv pip list
```

![설치된 패키지 목록](images/06b-pip-list.png)

`uv pip install`로만 추가한 패키지는 나중에 `uv sync`에서 제거될 수 있다. **지속적으로 사용할 프로젝트는 `uv add`로 관리하는 편이 안전하다.**

VS Code 설치, Python·Jupyter 확장, Notebook 커널 선택은 [07. VS Code 상세 안내](07-vscode.md)에서 다룬다. 다른 컴퓨터에서 환경을 재현하려면 [03장](03-projects.md)을 참고한다.

공식 자료: [uv 프로젝트 의존성 관리](https://docs.astral.sh/uv/concepts/projects/dependencies/)

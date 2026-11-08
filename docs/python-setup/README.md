# Python 개발환경 Quick Tour — VS Code Notebook까지 한 번에

**이 페이지 하나만 따라 하면 첫 Python 실습을 시작할 수 있다.** Windows 11의 PowerShell을 기준으로 **uv로 Python 환경 준비 → VS Code 설치 → Notebook에서 코드 실행**까지 진행한다. 기본 실습에 Anaconda나 별도 Jupyter 서버는 필요하지 않다.

macOS/Linux에서는 [별도 설치 안내](05-macos-linux.md)를 먼저 참고하고, VS Code·Notebook 사용법은 아래와 같다.

## 오늘 실습에서 할 일

1. uv 설치 (필요한 Python은 uv가 준비)
2. VS Code와 Python·Jupyter 확장 설치
3. 실습 폴더 생성, `ipykernel` 설치
4. VS Code에서 Notebook을 만들고 첫 코드 실행

### 잠깐! 왜 이름이 uv일까?

**uv는 *Ultraviolet*(자외선)에서 따온 이름**이다. 개발자 Charlie Marsh는 짧고 입력하기 쉬우며 회사 이름 *Astral*(별·천체를 연상시키는 말)과도 어울린다고 설명했다. [개발자 인터뷰](https://pythontest.com/testandcode/episodes/ruff-astral-uv-charlie-marsh/)

## 1. uv 설치

Windows PowerShell을 열어 아래 명령을 실행한다. `winget`은 일반 Windows 11에 기본 제공되는 패키지 관리 도구다.

```powershell
winget install --id=astral-sh.uv -e
```

![winget으로 uv 설치한 실제 Windows 화면](images/01-winget-install.png)

**`winget`이 없으면:** 위 명령 대신 Astral 공식 설치 스크립트를 사용한다. **둘 다 실행할 필요는 없다.** Windows Sandbox에서도 이 방법을 이용할 수 있다.

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

회사·학교 PC의 보안 정책이 외부 스크립트 실행을 제한하면 해당 정책을 따른다.

**PowerShell을 닫고 새로 열어 설치 확인**

```powershell
uv --version
```

![uv 버전을 확인한 실제 화면](images/02-uv-version.png)

## 2. VS Code 설치

웹사이트에서 설치 파일을 직접 내려받는 대신 `winget`을 이용한다.

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

**`winget`이 없다면:** [VS Code 공식 다운로드](https://code.visualstudio.com/download)에서 Windows 설치 프로그램을 이용한다.

설치 후 **PowerShell을 새로 열고** 설치를 확인한다.

```powershell
code --version
```

명령을 찾을 수 없다면 VS Code까지 완전히 닫았다가 다시 열거나 [VS Code 설치·설정 상세 안내](07-vscode.md)를 참고한다.

## 3. VS Code 확장 설치

**Python 확장**

```powershell
code --install-extension ms-python.python
```

**Jupyter 확장** — VS Code 안에서 Notebook(`.ipynb`)을 실행할 때 사용한다.

```powershell
code --install-extension ms-toolsai.jupyter
```

## 4. Python 실습 프로젝트 만들기

PowerShell에서 다음 명령을 **하나씩** 실행한다. 이미 `python-study` 폴더를 만든 학생은 이 단계를 다시 실행하지 않는다.

**실습 폴더와 uv 프로젝트 설정 생성**

```powershell
uv init --no-package python-study
```

**폴더로 이동**

```powershell
cd python-study
```

`uv init`은 프로젝트 설정을 만든다. 아직 Python이 설치되지 않았더라도 다음 단계에서 uv가 필요한 Python과 프로젝트 전용 가상환경(`.venv`)을 준비할 수 있다.

## 5. Notebook 실행에 필요한 커널 설치

`ipykernel`은 VS Code Notebook 셀의 Python 코드를 실행하는 도구다. 별도의 `notebook` 또는 `jupyterlab` 패키지를 설치할 필요는 없다.

```powershell
uv add --dev ipykernel
```

`--dev`는 개발·학습용 패키지로 구분해 기록한다는 뜻이다. 이 명령은 필요한 Python과 `.venv`도 자동으로 준비하므로 **앞에서 `uv venv`를 별도로 실행할 필요가 없다.**

Python 설치 결과 확인:

```powershell
uv run python --version
```

## 6. VS Code에서 실습 폴더 열기

`python-study` 폴더 안에서 실행한다.

```powershell
code .
```

VS Code가 열리면 왼쪽 탐색기에서 현재 폴더가 `python-study`인지 확인한다.

## 7. 첫 Notebook 만들고 실행하기

1. VS Code에서 **`Ctrl+Shift+P`**를 누른다.
2. **`Create: New Jupyter Notebook`**을 찾아 실행한다. 또는 새 파일 `hello.ipynb`를 만든다.
3. 오른쪽 위 **Select Kernel**을 누른다.
4. **Python Environments**에서 현재 프로젝트의 **`.venv\Scripts\python.exe`**를 선택한다. 메뉴 구성이 다르면 **Select Another Kernel**을 통해 찾는다.
5. 첫 번째 코드 셀에 다음 코드를 입력하고, 셀 왼쪽의 **▶ Run**을 누른다.

```python
print("Hello, Python!")
```

정상 실행되면 셀 아래에 다음 결과가 나타난다.

```text
Hello, Python!
```

두 번째 셀에서도 시험해 본다.

```python
2 + 3
```

```text
5
```

**`Ctrl+S`로 노트북을 `hello.ipynb`로 저장**한다. 이제 설치부터 첫 실행까지 끝났다.

> **주의:** 이 과정은 VS Code **안에서** Notebook을 실행하는 방법이다. 웹브라우저에서 JupyterLab을 실행하는 방법과는 다르다. 실제 화면 예시와 커널 문제 해결은 [VS Code 상세 안내](07-vscode.md)를 참고한다.

## 더 자세히 알고 싶다면

Quick Tour에서 막히지 않았다면 아래 내용은 **필요할 때만** 읽어도 된다.

- [01. Python·가상환경의 개념과 구조](01-install.md)
- [02. 패키지 관리와 `--dev`](02-packages.md)
- [03. 프로젝트 생성·환경 재현과 GitHub](03-projects.md)
- [04. 자주 발생하는 오류와 해결](04-troubleshooting.md)
- [05. macOS/Linux 설치](05-macos-linux.md)
- [06. 기존 Python·Anaconda, 업데이트, 디스크 관리 Q&A](06-advanced.md)
- [07. VS Code 설치·설정·Notebook 상세 안내](07-vscode.md)

공식 자료: [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) · [uv의 VS Code Notebook 안내](https://docs.astral.sh/uv/guides/integration/jupyter/) · [VS Code Notebook 안내](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

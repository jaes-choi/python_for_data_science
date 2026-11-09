# 05. macOS / Linux에서 Python·VS Code 설치하기

macOS와 Linux에서도 **uv로 Python을 준비하고 VS Code의 Notebook에서 실습**할 수 있다. 운영체제별로 설치 명령어와 Python 실행 파일 경로가 다르다.

## 1. uv 설치

macOS와 Linux 터미널에서 Astral 공식 설치 프로그램을 이용한다.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

macOS에서 Homebrew가 이미 설치되어 있다면 `brew install uv`를 대신 이용할 수도 있다. 둘 중 한 방법만 사용한다.

## 2. VS Code 명령어 설치

### macOS: Homebrew 사용

Homebrew가 설치되어 있다면 다음 한 줄로 VS Code를 설치한다.

```bash
brew install --cask visual-studio-code
```

Homebrew가 없다면 [VS Code 공식 다운로드](https://code.visualstudio.com/download)에서도 설치할 수 있다. 설치 후 `code` 명령을 찾지 못한다면 VS Code에서 `Cmd+Shift+P` → `Shell Command: Install 'code' command in PATH`를 실행하고 터미널을 새로 연다. Homebrew로 설치한 경우에는 보통 `code` 명령이 함께 제공된다.

### Linux: Snap 사용 가능 환경(예: Ubuntu)

```bash
sudo snap install code --classic
```

Snap을 사용할 수 없는 배포판은 이 명령을 실행하지 말고, [Microsoft의 Linux 설치 안내](https://code.visualstudio.com/docs/setup/linux)에서 Debian/Ubuntu, Fedora/RPM 등 **해당 배포판에 맞는 방법**을 이용한다.

## 3. Python·Jupyter 확장 설치

VS Code Extensions 메뉴에서 설치해도 되고, 아래 명령어를 차례대로 실행해도 된다.

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

## 4. Notebook 프로젝트와 ipykernel 준비

처음 시작하는 경우 사용자 홈 디렉터리에서 아래 명령을 순서대로 실행한다.

```bash
uv init --no-package python-study
cd python-study
uv add --dev ipykernel
```

이 명령으로 프로젝트 전용 `.venv` 환경과 Notebook 실행에 필요한 `ipykernel`이 준비된다. 별도의 `uv venv` 실행은 필요하지 않다.

## 5. 설치 후 테스트와 Notebook 실행

**설치와 별개로 나중에 테스트**해도 된다. 터미널을 새로 연 뒤 다음 명령으로 확인한다.

```bash
uv --version
code --version
cd ~/python-study
uv run python --version
code .
```

VS Code에서 `hello.ipynb` 파일을 만들고 **Select Kernel → Python Environments → `.venv/bin/python`**을 선택한다. 이후 셀 실행은 [Quick Tour의 Notebook 실습](README.md#7-첫-notebook-만들고-실행하기)을 따른다.

공식 자료: [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) · [VS Code macOS](https://code.visualstudio.com/docs/setup/mac) · [VS Code Linux](https://code.visualstudio.com/docs/setup/linux) · [Homebrew VS Code](https://formulae.brew.sh/cask/visual-studio-code)

[Windows Quick Tour](README.md) · [VS Code 상세 안내](07-vscode.md)

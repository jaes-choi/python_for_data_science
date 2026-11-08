# 08. VS Code 단축키 — 필수와 유용 (Windows)

이번 강의는 VS Code에서 Python 파일(`.py`)과 Notebook(`.ipynb`)을 사용한다. 단축키는 **어디에서 사용하느냐**에 따라 나뉜다. 첫 실습에서는 각 영역의 '필수'만 익히고, 익숙해지면 '유용' 항목을 추가로 사용하자.

- VS Code 공통: 파일 찾기, 명령 실행, 터미널·패널 관리
- 코드 편집: 코드를 작성하거나 수정하는 중에 사용
- Notebook 셀: `.ipynb`에서 셀을 실행·추가·삭제할 때 사용

## 1. VS Code 공통 단축키

파일 종류와 관계없이 VS Code 창에서 사용한다.

### 필수

| 단축키 | 기능 |
|---|---|
| `Ctrl+Shift+P` | 명령 팔레트 열기 — 메뉴 이름을 검색해 실행 |
| `Ctrl+P` | 파일 이름을 입력해 빠르게 열기 |
| `Ctrl+S` | 현재 파일 저장 |
| `Ctrl + 백틱` | 통합 터미널 표시·숨기기 — `uv` 명령 실행 |

### 유용

| 단축키 | 기능 |
|---|---|
| `Ctrl+J` | 하단 패널 표시·숨기기 |
| `Ctrl+Shift+E` | 파일 탐색기 열기 |
| `Ctrl+Shift+X` | 확장(Extensions) 화면 열기 |
| `Ctrl+Shift+F` | 프로젝트 전체에서 검색 |
| `Ctrl+K` 다음 `Ctrl+S` | 단축키 설정(Keyboard Shortcuts) 열기 |

`Ctrl+J`는 **하단 패널 전체**를 전환한다. 마지막으로 사용한 패널이 터미널이면 터미널이 보이지만, Problems나 Output이 표시될 수도 있다. `Ctrl + 백틱`은 터미널을 직접 전환한다. 백틱 키는 보통 숫자 1 키 왼쪽에 있다. 키보드 배열에 따라 다르게 배치될 수 있다.

## 2. VS Code 코드 편집 단축키

`.py` 편집기나 Notebook 코드 셀 **안에서 글자를 편집할 때** 사용한다.

### 필수

| 단축키 | 기능 |
|---|---|
| `Ctrl+/` | 현재 줄을 주석으로 처리하거나 해제 |
| `Ctrl+Z` | 방금 수정한 내용 되돌리기 |
| `Ctrl+Space` | 자동완성 제안 표시 |

### 유용

| 단축키 | 기능 |
|---|---|
| `Ctrl+D` | 현재 선택한 단어와 같은 다음 단어도 선택 |
| `Alt+↑` / `Alt+↓` | 코드 줄 위·아래로 이동 |
| `Ctrl+Shift+Space` | 함수의 매개변수 정보 보기 |
| `F2` | 변수·함수 이름 변경(Rename Symbol) |
| `Ctrl+F` | 현재 파일 안에서 찾기 |

편집 단축키는 **커서가 코드 입력 영역에 있을 때** 사용하는 것이 기본이다. Notebook의 셀 자체를 이동하거나 삭제하는 기능과는 구분한다.

## 3. VS Code Notebook 셀 단축키

`.ipynb` 파일에서 사용한다. 특히 **편집 모드와 명령 모드의 차이**를 기억하자. 셀 안에 입력 커서가 있으면 편집 모드이고, `Esc`로 셀을 선택하는 명령 모드로 전환한다.

### 필수

| 단축키 | 기능 |
|---|---|
| `Shift+Enter` | 현재 셀을 실행하고 다음 셀로 이동 |
| `Ctrl+Enter` | 현재 셀 실행 |
| `Esc` / `Enter` | 명령 모드 / 편집 모드 전환 |
| `A` / `B` | 명령 모드에서 현재 셀 위 / 아래에 셀 추가 |

### 유용

| 단축키 | 기능 |
|---|---|
| `Alt+Enter` | 현재 셀 실행 후 아래에 새 셀 추가 |
| `D D` | 명령 모드에서 `D`를 두 번 눌러 셀 삭제 |
| `Z` | 명령 모드에서 최근 셀 작업 취소 |
| `M` / `Y` | 명령 모드에서 Markdown / Code 셀로 변경 |

`Ctrl+Enter`는 두 키를 **동시에** 누른다. `D D`는 `D`를 **연속으로 두 번** 누른다. Notebook 셀에서 `Ctrl+Enter`는 실행이지만, 일반 `.py` 편집기에서는 새 줄을 삽입하므로 사용 위치를 구분해야 한다.

커널 중단·재시작은 Notebook 상단의 Interrupt/Restart 버튼을 사용하거나 `Ctrl+Shift+P`에서 명령 이름을 검색한다. 브라우저 Jupyter의 `I I`, `0 0`이 VS Code에서도 동일하게 동작한다고 가정하지 않는다.

## 4. 3분 실습 — 필수 단축키 익히기

[Quick Tour](README.md#7-첫-notebook-만들고-실행하기)에서 만든 `hello.ipynb`를 VS Code에서 열고 따라 해 보자.

1. **명령 찾기:** `Ctrl+Shift+P`로 명령 팔레트를 연 다음 `Esc`로 닫는다.
2. **파일 찾기:** `Ctrl+P`를 누르고 `hello.ipynb`를 입력해 현재 파일을 찾는다.
3. **터미널 열기:** `Ctrl + 백틱`으로 터미널을 연다. 터미널에서 `uv --version`을 실행하고 다시 편집기로 돌아온다.
4. **셀 실행:** `print("Hello, Python!")` 셀을 선택하고 `Ctrl+Enter`로 실행한다.
5. **다음 셀로 이동:** `Shift+Enter`로 실행한 뒤 다음 셀로 이동한다.
6. **새 셀 추가:** `Esc`로 명령 모드로 전환하고 `B`로 아래에 셀을 추가한다.
7. **코드 작성:** `Enter`로 편집 모드에 들어가 `10 * 3`을 입력하고 `Ctrl+Enter`로 실행해 `30`을 확인한다.
8. **저장:** `Ctrl+S`로 Notebook을 저장한다.

## 단축키가 다르게 동작할 때

`Ctrl+K`를 누른 뒤 손을 떼고 `Ctrl+S`를 누르면 VS Code의 Keyboard Shortcuts 창이 열린다. 여기서 기능 이름으로 검색해 **현재 설정된 키**를 확인할 수 있다.

| 증상 | 확인할 것 |
|---|---|
| `A`, `B`를 눌렀는데 글자만 입력됨 | `Esc`로 셀 명령 모드 전환 |
| `Shift+Enter`가 작동하지 않음 | `.ipynb`의 Notebook 셀에 포커스가 있는지 확인 |
| `Ctrl+J`를 눌렀는데 터미널이 안 보임 | 하단의 다른 패널이 열린 것일 수 있음. `Ctrl + 백틱`을 사용 |
| 일부 단축키가 다름 | 개인 키 설정, 키맵 확장, 운영체제·키보드 배열 확인 |

기존 브라우저 Jupyter 단축키는 [저장소 최상위 README](../../README.md)에 별도로 정리되어 있다.

공식 자료: [VS Code Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) · [기본 단축키](https://code.visualstudio.com/docs/reference/default-keybindings) · [단축키 설정](https://code.visualstudio.com/docs/configure/keybindings)

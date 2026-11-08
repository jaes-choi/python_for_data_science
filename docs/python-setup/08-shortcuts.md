# 08. VS Code·Notebook 필수 단축키 (Windows)

[Quick Tour](README.md)에서 Notebook을 실행했다면, 마우스 대신 **키보드로 반복 작업을 빠르게 처리하는 습관**을 익혀보자.

**대상:** Windows 11 + VS Code + Python/Jupyter 확장 + uv 프로젝트. macOS는 키 조합이 다를 수 있어 [공식 키 설정 안내](https://code.visualstudio.com/docs/configure/keybindings)를 참고한다.

## 첫날 필수 8개 — 사용하는 위치별 구분

아래 단축키는 **VS Code에서 사용하는 키**다. 그러나 VS Code 자체의 **공통 기능**과 Notebook(`.ipynb`) **셀 조작**은 구분해야 한다.

### VS Code 공통 — 4개

일반 Python 파일(`.py`)이나 Notebook(`.ipynb`)을 열었을 때 모두 사용하는 기능이다.

| 단축키 | 기능 | 사용 장면 |
|---|---|---|
| `Ctrl+Shift+P` | 명령 팔레트 | 명령 이름을 검색해 실행 |
| `Ctrl+P` | 파일 빠른 열기 | 파일 이름으로 이동 |
| `Ctrl + 백틱` | 통합 터미널 열기·닫기 | `uv` 명령 실행 |
| `Ctrl+S` | 파일 저장 | `.py`, `.ipynb` 저장 |

### VS Code Notebook 전용 — 4개

**`.ipynb` 파일의 셀에 포커스가 있을 때** 사용하는 키다. 일반 `.py` 편집기에서는 동작이 다를 수 있다.

| 단축키 | 기능 | 사용 장면 |
|---|---|---|
| `Shift+Enter` | 셀 실행 후 다음 셀로 이동 | 연속 실습 |
| `Ctrl+Enter` | 현재 셀 실행 | 코드 수정 후 다시 실행 |
| `Esc` / `Enter` | 명령 모드 / 편집 모드 | 셀 선택 ↔ 코드 입력 |
| `A` / `B` | 위 / 아래에 셀 추가 | **명령 모드**에서 사용 |

**`Ctrl+J`도 터미널이 열리는 것처럼 보일 수 있다.** 이 단축키는 VS Code **하단 패널 전체**를 표시하거나 숨긴다. 마지막으로 사용한 패널이 터미널이면 터미널이 나타나지만, **문제(Problems)**나 **출력(Output)** 화면이 나타날 수도 있다. 반면 **`Ctrl + 백틱`은 터미널을 직접 표시하거나 숨기는 단축키**다.

백틱 키는 일반적으로 키보드 숫자 1의 왼쪽에 있다. 키보드 배열이 다르거나 단축키가 작동하지 않으면 **터미널 → 새 터미널** 메뉴를 이용할 수 있다.

## VS Code 공통·코드 편집 단축키

VS Code 화면 전체에서 사용하는 키와 `.py` 파일·Notebook 코드 셀에서 사용하는 편집 키를 구분했다.

| 단축키 | 적용 위치 | 기능 |
|---|---|---|
| `Ctrl+Shift+E` | VS Code 공통 | 탐색기 열기 |
| `Ctrl+Shift+X` | VS Code 공통 | 확장(Extensions) 화면 |
| `Ctrl+Shift+P` 또는 `F1` | VS Code 공통 | 명령 팔레트 |
| `Ctrl+P` | VS Code 공통 | 파일 이름으로 빠르게 열기 |
| `Ctrl+Shift+F` | VS Code 공통 | 프로젝트 전체 검색 |
| `Ctrl+S` | VS Code 공통 | 저장 |
| `Ctrl+J` | VS Code 공통 | 하단 패널 표시·숨기기 (터미널·문제·출력 등) |
| `Ctrl + 백틱` | VS Code 공통 | 통합 터미널 직접 표시·숨기기 |
| `Ctrl+/` | 코드 편집 영역 | 줄 주석 켜기·끄기 |
| `Ctrl+D` | 코드 편집 영역 | 동일한 다음 단어 추가 선택 |
| `Alt+↑` / `Alt+↓` | 코드 편집 영역 | 코드 줄 이동 |
| `Ctrl+Space` | 코드 편집 영역 | 자동완성 제안 열기 |
| `Ctrl+Shift+Space` | 코드 편집 영역 | 함수 매개변수 정보 |

## VS Code Notebook(.ipynb)에서 셀 조작

**모드가 가장 중요합니다.** 셀 내부에 입력 커서가 깜빡일 때 `A`, `B`를 누르면 글자가 입력됩니다. 먼저 `Esc`를 눌러 **명령 모드**로 이동해야 셀 단위 단축키가 동작합니다.

| 단축키 | 동작 |
|---|---|
| `Shift+Enter` | 셀 실행하고 다음 셀로 이동 |
| `Ctrl+Enter` | 현재 셀 실행 |
| `Alt+Enter` | 실행 후 아래 셀 추가 |
| `Esc` / `Enter` | 명령 모드 / 편집 모드 |
| `A` / `B` | 명령 모드에서 위 / 아래에 셀 추가 |
| `D D` | 명령 모드에서 `D`를 두 번 눌러 셀 삭제 |
| `Z` | 명령 모드에서 최근 셀 작업 취소 |
| `M` / `Y` | 명령 모드에서 Markdown / Code 셀로 변경 |
| `Alt+↑` / `Alt+↓` | 셀 위치 이동 |
| `Ctrl+S` | Notebook 저장 |

**구별하기:** `D D`는 D를 연속해서 두 번 누릅니다. `Ctrl+Enter`는 두 키를 동시에 누릅니다. 또한 `Ctrl+Enter`는 Notebook 셀에서는 **실행**이지만, 일반 `.py` 편집기에서는 **현재 줄 아래 새 줄 삽입**입니다.

**커널 중단·재시작**은 처음에는 Notebook 상단의 Interrupt/Restart 버튼 또는 `Ctrl+Shift+P`로 명령을 검색해 실행하세요. 브라우저 Jupyter의 `I I`, `0 0`이 VS Code에서 똑같이 동작하는 것은 아닙니다.

## 3분 단축키 실습 — VS Code Notebook

[Quick Tour](README.md#7-첫-notebook-만들고-실행하기)에서 만든 `hello.ipynb`를 **VS Code에서 열고** 연습한다.

1. **명령 팔레트 열기:** `Ctrl+Shift+P`를 누르고 `Esc`로 닫는다. (VS Code 공통)
2. **현재 셀 실행:** `print("Hello, Python!")` 셀에서 `Ctrl+Enter`를 누른다. (Notebook)
3. **실행 후 이동:** `Shift+Enter`로 셀을 실행하고 다음 셀로 이동한다. (Notebook)
4. **아래 셀 추가:** `Esc`로 명령 모드에 들어간 뒤 `B`를 누른다. (Notebook)
5. **코드 입력·실행:** `Enter`로 편집 모드에 들어가 `10 * 3`을 입력한다. `Ctrl+Enter`로 실행해 `30`을 확인한다. (Notebook)
6. **Markdown 전환:** `Esc` → `M`으로 셀 종류를 바꾸고 `## 오늘 배운 것`을 입력해 실행한다. (Notebook)
7. **저장:** `Ctrl+S`로 파일을 저장한다. (VS Code 공통)

처음부터 모든 단축키를 외울 필요는 없다. 실습을 반복하면서 **8개부터 자연스럽게 익히는 것**이 목표다.

## 단축키가 다르게 동작할 때

**실제 키 설정 확인:** `Ctrl+K`를 누른 뒤 손을 떼고 `Ctrl+S`를 누르면 **Keyboard Shortcuts** 설정 화면이 열린다. 검색창에서 `Notebook`, `Run Cell`, `Terminal` 등으로 명령과 할당된 키를 확인할 수 있다.

| 증상 | 해결 방법 |
|---|---|
| `A` / `B`를 눌렀는데 글자만 입력됨 | `Esc`로 셀 선택(명령 모드) 전환 |
| `Shift+Enter`가 예상과 다름 | `.ipynb` Notebook 셀에 포커스가 있는지 확인 |
| 터미널 단축키가 작동하지 않음 | 터미널 메뉴 또는 현재 키 설정 확인 |
| 문서와 키가 다름 | 키맵 확장, 개인 설정, 키보드 배열 확인 |

**기존 브라우저 Jupyter 단축키**는 [저장소 최상위 README](../../README.md)에서 별도로 설명한다.

공식 자료: [VS Code Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) · [기본 단축키](https://code.visualstudio.com/docs/reference/default-keybindings) · [단축키 설정](https://code.visualstudio.com/docs/configure/keybindings)

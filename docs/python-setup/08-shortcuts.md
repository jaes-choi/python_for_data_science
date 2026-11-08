# 08. VS Code·Notebook 필수 단축키 (Windows)

[Quick Tour](README.md)에서 Notebook을 실행했다면, 마우스 대신 **키보드로 반복 작업을 빠르게 처리하는 습관**을 익혀보자.

**대상:** Windows 11 + VS Code + Python/Jupyter 확장 + uv 프로젝트. macOS는 키 조합이 다를 수 있어 [공식 키 설정 안내](https://code.visualstudio.com/docs/configure/keybindings)를 참고한다.

## 첫날 가장 중요한 8개

| 단축키 | 기능 | 사용 장면 |
|---|---|---|
| **`Ctrl+Shift+P`** | 명령 팔레트 | 메뉴를 찾기 어려우면 명령 이름으로 검색 |
| **`Ctrl+P`** | 파일 빠른 열기 | 파일 이름을 입력해 바로 열기 |
| **`Ctrl + 백틱`** | 통합 터미널 표시/숨기기 | `uv` 명령 실행 |
| **`Shift+Enter`** | Notebook 셀 실행 후 다음으로 이동 | 연속 실습 |
| **`Ctrl+Enter`** | Notebook 현재 셀 실행 | 같은 코드 다시 실험 |
| **`Esc` / `Enter`** | 명령 모드 / 편집 모드 | 셀 선택 ↔ 코드 입력 |
| **`A` / `B`** | 위 / 아래에 셀 추가 | Notebook 명령 모드에서 |
| **`Ctrl+S`** | 저장 | 작업 내용 보관 |

**백틱**은 일반적으로 키보드 숫자 1 왼쪽의 ``` 기호다. 키보드 배열이 다르거나 단축키가 작동하지 않으면 **터미널 → 새 터미널** 메뉴를 이용할 수 있다.

## VS Code 일반 편집·탐색

| 단축키 | 기능 |
|---|---|
| `Ctrl+Shift+E` | 탐색기 열기 |
| `Ctrl+Shift+X` | 확장(Extensions) 화면 |
| `Ctrl+Shift+P` 또는 `F1` | 명령 팔레트 |
| `Ctrl+P` | 파일 이름으로 빠르게 열기 |
| `Ctrl+Shift+F` | 프로젝트 전체 검색 |
| `Ctrl+/` | 줄 주석 켜기/끄기 |
| `Ctrl+D` | 동일한 다음 단어 추가 선택 |
| `Alt+↑` / `Alt+↓` | 코드 줄 이동 |
| `Ctrl+Space` | 자동완성 제안 열기 |
| `Ctrl+Shift+Space` | 함수 매개변수 정보 |
| `Ctrl+S` | 저장 |

## VS Code Notebook에서 셀 조작

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

## 3분 단축키 실습

[Quick Tour](README.md#7-첫-notebook-만들고-실행하기)에서 만든 `hello.ipynb`로 연습한다.

1. `Ctrl+Shift+P`로 명령 팔레트를 열고, `Esc`로 닫는다.
2. `print("Hello, Python!")` 셀에서 **`Ctrl+Enter`**로 실행한다.
3. **`Shift+Enter`**로 다시 실행하고 다음 셀로 이동한다.
4. **`Esc` → `B`**로 아래에 셀 하나를 추가한다.
5. **`Enter`**로 편집한 뒤 `10 * 3`을 입력하고 **`Ctrl+Enter`**로 `30`을 확인한다.
6. **`Esc` → `M`**으로 Markdown으로 바꾼 뒤 `## 오늘 배운 것`을 입력하고 실행한다.
7. `Ctrl+S`로 저장한다.

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

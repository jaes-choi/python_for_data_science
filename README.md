# 데이터 과학을 위한 Python
### @DataSolution_Learning_Center

실습에 필요한 파일을 보관하는 저장소입니다.

**이번 Python 입문 강의 시작:** [uv → VS Code → Notebook Quick Tour](docs/python-setup/README.md)

**단축키 참고:** [VS Code·Notebook 필수 단축키](docs/python-setup/08-shortcuts.md) · [VS Code 사용법 상세](docs/python-setup/07-vscode.md)

## 기존 Notebook 단축키 — 기능과 사용 환경

기존에 정리해 둔 **Jupyter Notebook 단축키 메모에 동작 설명을 보완**했습니다. 이번 강의는 **VS Code 안에서 Notebook**을 사용하므로, 브라우저 Jupyter에서 사용하던 단축키가 그대로 동작한다고 가정하면 안 됩니다. 새 실습에서는 [VS Code 단축키 페이지](docs/python-setup/08-shortcuts.md)를 우선 참고하세요.

**셀에는 두 모드가 있습니다.** `Esc`는 명령 모드(Command Mode: 셀 선택), `Enter`는 편집 모드(Edit Mode: 셀 안에 코드 입력)로 전환합니다. `A`, `B`, `D D` 등 글자 명령은 **명령 모드**에서 실행합니다.

| 작업 | 단축키 | 의미 |
|---|---|---|
| 셀 실행 | `Ctrl+Enter` | 현재 셀 실행 |
| 실행 후 다음 셀 | `Shift+Enter` | 실행 후 다음 셀로 이동, 필요하면 아래에 새 셀 생성 |
| 실행 후 셀 추가 | `Alt+Enter` | 실행하고 아래에 새 셀 생성 |
| 명령/편집 모드 | `Esc` / `Enter` | 셀 선택 / 셀 안에 글자 입력 |
| 셀 추가 | `A` / `B` | 현재 셀의 위(Above) / 아래(Below) |
| 셀 복사·붙여넣기·잘라내기 | `C` / `V` / `X` | 셀 단위 조작(브라우저 Jupyter 환경의 관례) |
| 셀 삭제 | `D D` | `D`를 **연속으로 두 번** 입력. `X D D` 한 명령이 아님 |
| 되돌리기 | `Z` | 최근 셀 삭제 등 셀 작업 취소 |
| 셀 나누기·합치기 | `Ctrl+Shift+-` / `Shift+M` | 분리 / 병합(브라우저 Jupyter 버전에 따라 다름) |
| Code/Markdown 전환 | `Y` / `M` | 셀 종류 바꾸기 |
| 저장 | `Ctrl+S` | Notebook 파일 저장 |
| 커널 중단·재시작 | `I I` / `0 0` | 브라우저 Jupyter의 전통적 명령. VS Code에서는 메뉴 사용 권장 |
| 출력 표시 | `O` | 셀 출력 접기·펼치기(일부 브라우저 Jupyter 버전) |
| 도움말·명령 찾기 | `H` / `P` | 브라우저 Jupyter의 도움말·명령 팔레트(버전별 차이) |

**동시에 vs 차례로:** `Ctrl+Enter`는 두 키를 **함께**, `D D`는 `D`를 **차례로 두 번** 누릅니다.

### 코드를 편집할 때 자동완성

- `Tab`: 자동완성 항목 적용 또는 들여쓰기에 사용합니다.
- 기존 메모의 `Tab Tab`(인자 정보)은 모든 편집기에서 공통으로 동작하지 않습니다. **VS Code에서는 `Ctrl+Space`(자동완성)와 `Ctrl+Shift+Space`(매개변수 정보)**를 사용하는 편이 명확합니다.
- **주의:** `Ctrl+Enter`는 VS Code의 `.ipynb`에서는 **셀 실행**, 일반 `.py` 파일 편집기에서는 **아래에 새 줄 삽입**입니다.

공식 참고: [VS Code Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) · [VS Code 기본 키](https://code.visualstudio.com/docs/reference/default-keybindings) · [Jupyter Notebook 사용법](https://github.com/jupyter/notebook/blob/main/docs/source/notebook.md)

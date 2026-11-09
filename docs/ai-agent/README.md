# AI Agent 10분 체험 — 터미널에서 폴더 정리

**오늘의 목표:** AI가 설명만 하는 것이 아니라, **내 컴퓨터의 파일을 실제로 정리**하도록 시켜 본다. **Codex 하나만 실습**한다.

## 수업 전 준비 (10분에 포함하지 않음)
Codex를 **미리 설치하고 로그인**한다. 설치 주소와 계정 이용 가능 여부는 [Codex 공식 안내](https://github.com/openai/codex)에서 확인한다.

**Windows PowerShell**
~~~powershell
irm https://chatgpt.com/codex/install.ps1 | iex
codex
~~~

**macOS / Linux 터미널**
~~~bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex
~~~

`codex`를 처음 실행해 로그인을 마친다. 설치·로그인은 PC/계정에 따라 10분보다 오래 걸릴 수 있다. 수업 중 설치가 안 되면 강사 화면을 함께 본다.

## 1분 — AI Agent란?
**챗봇**은 파일 정리 방법을 *설명*한다. **AI Agent**는 파일 목록을 확인하고, 계획을 세우고, 승인된 명령으로 실제 파일을 *옮길 수 있다*.

## 2분 — 연습용 파일 두 개 만들기
**Windows PowerShell**
~~~powershell
New-Item -ItemType Directory -Force "$HOME/ai-demo" | Out-Null
cd "$HOME/ai-demo"
"메모" | Set-Content -Encoding utf8 note.txt
"print('hi')" | Set-Content -Encoding utf8 hello.py
codex
~~~

**macOS / Linux**
~~~bash
mkdir -p ~/ai-demo && cd ~/ai-demo
printf 'memo\n' > note.txt
printf "print('hi')\n" > hello.py
codex
~~~

> **실습 장소는 반드시 새로 만든 `ai-demo` 폴더.** 개인 문서가 있는 폴더에서 실행하지 않는다.

## 5분 — 아래 문장을 Codex에 입력
~~~text
현재 ai-demo 폴더 안의 파일 두 개를 종류별로 정리해 줘.
먼저 이동 계획을 보여 주고 내 확인을 받아.
승인하면 docs와 code 폴더를 만들어
note.txt는 docs로, hello.py는 code로 옮겨 줘.
다른 폴더에 접근하거나 파일을 삭제·덮어쓰지 마.
마지막에 정리한 결과를 보여 줘.
~~~

화면에 나타난 **변경 계획과 대상 경로를 확인한 뒤 승인**한다.

## 2분 — 결과 확인
**Windows PowerShell:** `Get-ChildItem -Recurse`

**macOS / Linux:** `find . -type f`

**성공하면:**
~~~text
ai-demo/
├── docs/
│   └── note.txt
└── code/
    └── hello.py
~~~

**한 줄 정리:** “AI가 작업할 수는 있지만, **범위 설정과 결과 확인은 사람이 한다.**”

---

**참고(수업 중 실습하지 않음):** 다른 코딩 에이전트에는 [Claude Code](https://code.claude.com/docs/en/setup), [Google Antigravity](https://antigravity.google/), [OpenCode](https://opencode.ai/docs/)가 있다. 무료·유료 범위 및 설치 방법은 각 공식 사이트를 확인한다.

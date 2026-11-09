# AI 코딩 에이전트 — 첫 실습 (20~30분)

**학습 목표:** AI 에이전트를 설치하고, 터미널에서 실행한 뒤, **연습용 폴더의 파일을 종류별로 정리**해 본다. Python 코딩이나 API 키는 필수가 아니다.

> Windows 11 PowerShell, macOS Terminal, Linux Bash를 지원한다. **개인 문서 폴더에서 실행하지 말고 반드시 아래 연습용 폴더에서만 실습**한다.

## 1. 무엇인가? (3분)
일반 AI 채팅은 '폴더를 정리하는 방법'을 설명한다. **코딩 에이전트**는 사용자가 승인한 범위에서 파일을 확인하고 실제로 이동한 다음 결과를 보고할 수 있다.
오늘 할 일은 딱 세 가지: **설치 → 실행 → 안전하게 파일 정리**.

## 2. Codex 설치·실행 (5~10분)
공식 설치: [Codex CLI](https://github.com/openai/codex) · [사용 안내](https://learn.chatgpt.com/docs/codex/cli)

### Windows — PowerShell
~~~powershell
irm https://chatgpt.com/codex/install.ps1 | iex
codex --version
~~~

### macOS / Linux — 터미널
~~~bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex --version
~~~

위 설치 명령은 **공식 설치 주소를 확인한 다음** 실행한다. 설치 후 `codex`를 실행하면 브라우저 등을 통해 계정 로그인 안내가 나타난다. 무료 이용 여부와 한도는 계정·시점에 따라 달라질 수 있다.

## 3. 안전한 연습용 폴더 만들기 (3분)
**반드시 새 연습용 폴더**에 예제 파일 네 개를 만든다.

### Windows — PowerShell
~~~powershell
New-Item -ItemType Directory -Force "$HOME/ai-agent-demo" | Out-Null
Set-Location "$HOME/ai-agent-demo"
"강의 메모" | Set-Content -Encoding utf8 lecture.txt
"print('hello')" | Set-Content -Encoding utf8 hello.py
"item,quantity`n우유,2" | Set-Content -Encoding utf8 shopping.csv
"# 내 생각" | Set-Content -Encoding utf8 idea.md
Get-ChildItem
~~~

### macOS / Linux — Bash 또는 zsh
~~~bash
mkdir -p "$HOME/ai-agent-demo"
cd "$HOME/ai-agent-demo"
printf 'lecture notes\n' > lecture.txt
printf "print('hello')\n" > hello.py
printf 'item,quantity\nmilk,2\n' > shopping.csv
printf '# idea\n' > idea.md
ls
~~~

**정리 전 구조:**
~~~text
ai-agent-demo/
  lecture.txt
  hello.py
  shopping.csv
  idea.md
~~~

## 4. 터미널에서 에이전트에게 시켜 보기 (5~10분)
현재 폴더가 `ai-agent-demo`인지 확인하고 실행한다.

~~~bash
codex
~~~

처음 시작할 때 로그인을 완료하고, 다음 지시문을 **그대로 붙여넣는다**.

~~~text
지금 작업하는 ai-agent-demo 폴더 안의 파일만 정리해 줘.

1. 먼저 현재 파일 목록과 이동 계획을 보여줘.
2. 내가 승인하기 전에는 파일을 변경하지 마.
3. 승인하면 docs, code, data 폴더를 만들고
   .txt와 .md 파일은 docs, .py 파일은 code, .csv 파일은 data로 이동해 줘.
4. 파일 내용과 이름은 바꾸지 마.
5. 삭제, 덮어쓰기, 폴더 밖 접근, 인터넷 업로드는 하지 마.
6. 완료 후 최종 폴더 구조와 실제 변경 내용을 보여줘.
~~~

에이전트가 **계획을 먼저 보여 주는지 확인**한다. 계획이 맞고 작업 경로가 연습 폴더 안인지 확인한 후에만 승인한다.

**기대 결과:**
~~~text
ai-agent-demo/
  docs/
    lecture.txt
    idea.md
  code/
    hello.py
  data/
    shopping.csv
~~~

## 5. 내가 직접 검증하기 (2분)
**Windows PowerShell:**
~~~powershell
Get-ChildItem -Recurse
~~~
**macOS / Linux:**
~~~bash
find . -maxdepth 3 -type f | sort
~~~

다음 세 가지가 맞으면 성공: **① 파일 네 개가 모두 있다 ② 세 폴더에 정확하게 분류됐다 ③ 원래 파일 내용은 그대로다.**

## 6. 다른 에이전트로도 해 보기 (선택)
같은 실습 폴더에서 **Codex 대신** 다른 에이전트 하나를 실행하면 된다. 먼저 정리된 폴더를 새로 준비한 뒤 같은 지시문을 사용한다.

| 도구 | Windows 설치 (PowerShell) | macOS·Linux 설치 (터미널) | 실행 |
|---|---|---|---|
| **Claude Code** | `winget install Anthropic.ClaudeCode` | `curl -fsSL https://claude.ai/install.sh \| bash` | `claude` |
| **Google Antigravity CLI (AGY)** | `irm https://antigravity.google/cli/install.ps1 \| iex` | `curl -fsSL https://antigravity.google/cli/install.sh \| bash` | `agy` |

- **Claude Code:** 대체로 유료 Claude 플랜이나 유료 API 이용 권한이 필요하다.
- **AGY:** 개인 무료 이용 경로가 있지만 사용량 제한이 있을 수 있다.
- **무료 대안:** [OpenCode](https://opencode.ai/docs/)에서 무료 제공 모델을 선택할 수 있으나 무료 모델·이용 한도는 바뀔 수 있다.
- **로컬 LLM:** 필요할 때만 [Ollama](https://ollama.com/download)와 OpenCode 연결을 다음 수업에서 소개한다. 이번 실습의 필수 과정은 아니다.

공식 문서: [Claude Code 설치](https://code.claude.com/docs/en/setup) · [AGY CLI 설치](https://antigravity.google/docs/cli/install)

## 설치/실행이 안 될 때
- 명령을 찾지 못함 → **터미널을 새로 열고** `codex --version`, `claude --version` 또는 `agy --version` 재확인
- 로그인이 안 됨 → 브라우저·네트워크·계정 이용 자격 확인
- 파일이 엉뚱한 곳에 있음 → 현재 폴더를 확인하고 **개인 자료가 있는 폴더에서 실행하지 않기**
- 에이전트가 바로 움직이려 함 → 중지하고 **변경 계획을 먼저 제출하도록 요청**하기

> **핵심:** 에이전트가 대신 작업할 수 있지만, **무엇을 하게 할지와 결과가 맞는지는 사람이 결정**한다.

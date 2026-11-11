# AI Agent 10분 실습 — uv + Codex로 다음 뉴스 제목 가져오기

**목표:** AI 에이전트에게 **Python 프로그램을 만들어 실행**하게 한다. 가져온 다음 뉴스 제목 5개를 `news_titles.txt`로 저장한다.

## 수업 전 준비 (설치·로그인은 10분에 포함하지 않음)
Windows Sandbox가 설치된 PC와 사용 가능한 ChatGPT 계정이 필요하다. Sandbox는 닫으면 초기화되므로 설치·로그인 시간을 미리 확인한다.

**Windows Sandbox → PowerShell:**
~~~powershell
# Codex 설치
irm https://chatgpt.com/codex/install.ps1 | iex
# uv 설치 (Python을 별도로 설치하지 않아도 uv가 관리 가능)
irm https://astral.sh/uv/install.ps1 | iex
~~~
**macOS / Linux 터미널**(Sandbox 없이 진행):
~~~bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
curl -LsSf https://astral.sh/uv/install.sh | sh
~~~
설치 전에 [Codex 공식 안내](https://github.com/openai/codex)·[uv 공식 안내](https://docs.astral.sh/uv/getting-started/installation/)에서 출처를 확인한다. 터미널을 새로 열고 `codex --version`, `uv --version`으로 확인한 뒤 `codex` 로그인까지 완료한다.

## 수업 실습 10분

**① 1분 — 설명:** 챗봇은 코드를 설명하고, **코딩 에이전트는 코드를 파일로 작성하고 명령으로 실행**할 수 있다.

**② 2분 — uv 프로젝트 준비**

Windows PowerShell:
~~~powershell
cd $HOME
uv init --no-package ai-demo
cd ai-demo
uv add requests beautifulsoup4
codex
~~~
macOS / Linux 터미널:
~~~bash
cd ~
uv init --no-package ai-demo
cd ai-demo
uv add requests beautifulsoup4
codex
~~~
`uv add`로 필요한 라이브러리와 `.venv` 가상환경이 준비된다. uv는 프로젝트에 맞는 Python도 관리할 수 있다. 이미 `ai-demo` 폴더가 있다면 `uv init`을 반복하지 않는다.

**③ 5분 — 아래 문장을 Codex에 입력**
~~~text
Python 초보자 실습이다. 현재 uv 프로젝트 안에 daum_titles.py를 만들어 줘.

- https://news.daum.net/ 의 '이 시각 주요뉴스'에 있는
  실제 기사 제목 5개만 수집해 줘.
- requests와 BeautifulSoup을 사용하고, 중복 제목은 제거해 줘.
- 제목을 화면에 번호를 붙여 출력하고 news_titles.txt에도 저장해 줘.
- uv run python daum_titles.py 로 직접 실행하고 결과를 보여 줘.
- 사이트 구조 변경이나 접속 제한으로 실패하면 제목을 지어내지 말고
  실패 원인을 알려 줘. 차단을 우회하지 마.
- 현재 프로젝트 밖의 파일은 변경하지 말고 삭제하거나 외부 전송하지 마.
~~~
외부 웹사이트는 접근 제한이나 구조 변경으로 수집이 실패할 수 있다. **10분 실습에서 성공을 보장하지 않는다는 점**을 이해한다.

**④ 1분 — 결과 확인** (Codex 종료 후)
~~~powershell
# Windows PowerShell
Get-Content .\news_titles.txt
~~~
~~~bash
# macOS / Linux
cat news_titles.txt
~~~
성공 기준: Python 파일이 생성됐고, 실제 실행했으며, 뉴스 제목과 저장한 텍스트 파일을 확인한다. 접속에 실패한 경우 원인 기록도 학습 결과다.

**⑤ 1분 — 로그아웃 및 종료**
~~~powershell
codex logout
~~~
브라우저에서도 ChatGPT 계정 로그아웃 → Windows Sandbox 창 닫기. Sandbox 내부 파일과 설치 프로그램은 닫으면 삭제된다. 로그아웃은 클라우드 세션 보호를 위해 별도로 한다.

> **강사용 참고:** 신규 Sandbox에서 **Codex + uv 설치, 인증, 의존성 다운로드**까지 수업 중 하려면 10분을 넘길 수 있다. 가능하면 사전 시연하고 수업에서는 `uv init`부터 보여 준다. Git 설치는 필요 없다.

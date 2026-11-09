# 06. 무료 AI Agent — OS별 설치와 한계

> **무료의 세 가지 뜻:** (A) 도구 자체 무료, (B) 모델 사용량의 일부 무료, (C) 로컬 추론으로 클라우드 모델 API 비용 없음. ‘항상 무제한 무료’와 다르다. 서비스 플랜은 수시로 바뀌므로 수업 당일 확인한다.

| 도구 | 무료 범위 | 한계 |
|---|---|---|
| Codex | 계정·기간별 제한된 무료 이용 가능 여부 확인 | 요청량·모델·기능 제약 |
| Google Antigravity | 개인 무료 사용 범위 | 주간/기타 한도·계정 제약 |
| OpenCode | 오픈소스 CLI, 제한적 무료 모델 선택 가능 | 특정 모델 유료, 무료 제공 조건 변경 |
| GitHub Copilot CLI | GitHub Free 또는 Student 등 자격별 제공량 | 프리미엄 요청 사용량, 정책·인증 |
| Ollama + OpenCode | 로컬 모델 추론 | 하드웨어·성능·전력·설치 비용 |

## 1. OpenCode — 무료/로컬 모델 연결에 유리
공식 안내: https://opencode.ai/docs/ · https://opencode.ai/download

**Windows 11 — PowerShell:** Node.js/npm이 이미 있다면 다음 명령을 사용한다.
~~~powershell
node --version
npm --version
npm install -g opencode-ai
opencode --version
opencode
~~~
Node.js가 없다면 공식 다운로드의 Windows 데스크톱 앱 또는 최신 설치 방법을 사용한다.

**macOS — Terminal(zsh):**
~~~bash
brew install anomalyco/tap/opencode
opencode --version
opencode
~~~
Homebrew가 없다면 공식 설치 스크립트 또는 npm 방식으로 설치한다.

**Ubuntu/Debian 등 Linux — Bash:**
~~~bash
curl -fsSL https://opencode.ai/install | bash
opencode --version
opencode
~~~
공식 설치 스크립트 URL·내용을 검토한다. 학교/기관 방화벽과 설치 정책을 준수한다. `opencode` 시작 후 **선택된 모델 제공자와 과금 상태**를 확인한다. 프로그램 자체는 무료여도 상용 LLM API 사용은 유료일 수 있다.

## 2. GitHub Copilot CLI — GitHub 계정을 활용
공식: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli

**Windows 11 PowerShell** (PowerShell 6 이상):
~~~powershell
winget install GitHub.Copilot
copilot --version
copilot
~~~
**macOS — Homebrew:**
~~~bash
brew install --cask copilot-cli
copilot --version
copilot
~~~
**Linux (또는 macOS) — 공식 설치 스크립트:**
~~~bash
curl -fsSL https://gh.io/copilot-install | bash
copilot --version
copilot
~~~
**세 OS 공통 npm 대안**(Node.js 22 이상): `npm install -g @github/copilot`.
첫 실행에서 `/login` 후 GitHub 계정 인증. GitHub Student 요금 혜택은 학생 인증 상태에 따라 다르다.

## 3. 무료 사용의 실질적 한계 확인
동일한 쇼핑 계산기 지시문을 두 가지 도구에 실행한다.
1. 누락 가격은 임의로 채우지 않는가?
2. 오류 입력(음수·문자열 수량)을 테스트하는가?
3. 테스트 명령과 성공 결과를 실제로 보여 주는가?
4. 허용한 폴더 밖을 수정하는가?
5. 모델 이름·무료 한도·과금 안내·사용량 제한 알림이 무엇인가?

**중요:** 에이전트가 실제로 작업하지 못한 경우 성공한 것처럼 보고하지 않는다. 무료 한도가 끝나면 더 작은 실습 과제를 선택하거나 오프라인 정답 코드를 사용한다.

## 4. 로컬 LLM은 완전 무료인가?
Ollama 등 로컬 프로그램은 외부 모델 API 요금 없이 실행할 수 있지만 전력, 장비, 저장공간, 초기 다운로드 비용은 발생한다. 로컬 모델이 도구 호출을 지원하지 않거나 품질이 낮으면 반복 실행에 실패할 수 있다. [로컬 에이전트 실습](07-local-llm.md)에서 비교한다.

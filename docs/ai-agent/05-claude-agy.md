# 05. Claude Code·Google Antigravity(AGY) 설치와 비교

두 도구는 Codex **다음 단계**다. 모두 기존 Python·Git 설치와 별개이며, 계정 자격/요금/사용량은 수업 당일 공식 페이지에서 재확인한다.

## A. Claude Code (일반적으로 유료 구독 또는 API 계정 필요)
공식: https://code.claude.com/docs/en/setup

**Windows 11 PowerShell**
~~~powershell
winget install Anthropic.ClaudeCode
claude --version
claude
~~~
대안 설치 방법은 공식 설치 문서에서 최신 명령을 확인한다.

**macOS·Linux 터미널**
~~~bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
claude
~~~
macOS에서 Homebrew를 사용하는 경우 `brew install --cask claude-code`도 공식 문서의 지원 여부를 확인한다.

### 첫 실습
프로젝트 루트에서 `claude`를 실행하고 로그인한 뒤 아래를 입력한다.
~~~text
agent_lab/work 내 쇼핑 계산기 코드만 검토해 줘.
새 코드는 작성하기 전에 바꿀 내용과 이유를 먼저 알려 줘.
누락 가격, 잘못된 수량을 검증하는 테스트를 제안하고 승인 후 실행해 줘.
다른 폴더 변경, 데이터 업로드, git push는 하지 마.
~~~
비용과 사용량은 모델, 작업량, 플랜에 따라 달라진다. ‘무료 Claude 채팅’과 ‘Claude Code 이용권’은 다르다.

## B. Google Antigravity / AGY
공식 제품·설치: https://antigravity.google/ 와 https://antigravity.google/download

**Windows 11 / macOS / Linux:** 홈페이지의 OS별 다운로드 및 지원 환경을 확인해 설치한다. Linux는 지원 배포판·아키텍처를 먼저 확인한다. GUI 앱과 CLI의 설치·명령은 버전에 따라 달라지므로 **확인되지 않은 단일 명령을 모든 OS에 복사하지 않는다.**

설치 후 앱 실행 → Google 계정 로그인 → 새 프로젝트 열기 → 로컬 실습 폴더 선택 → 명령 승인 설정 확인 → 채팅에서 동일 프롬프트 실행.

CLI가 제공되는 버전이라면 프로그램 내 공식 안내에 표시되는 CLI 설치 절차를 수행하고 `agy --version`과 `agy --help`로 확인한다. 명령이 없으면 GUI 실습을 진행한다. Linux 배포판에서 설치가 지원되지 않는다면 다른 도구를 사용한다.

### 실습
~~~text
현재 프로젝트에서 agent_lab/work만 분석해 줘.
CSV를 읽는 쇼핑 보고서를 만들고 미등록 품목을 별도로 기록해 줘.
각 단계의 실행 명령과 테스트 출력을 남겨 줘.
변경 전에 계획을 제시하고 승인받아라.
~~~

## 비교 활동
**같은 데이터·같은 요구사항·같은 채점 기준**으로 Codex/Claude Code/AGY를 사용한다. 실행 시간뿐 아니라 누락 처리 정확성, 실제 테스트 수행, 사용자가 변경 내용을 이해하고 승인할 수 있는지를 비교한다.

## 설치 오류
- 명령이 없으면 새 터미널 실행, 설치 로그·PATH 확인
- 로그인 실패 시 계정 권한/네트워크·구독 상태 확인
- 승인 요청은 무조건 수락하지 않고 대상 파일·명령 확인
- 회사/학교 관리 PC에서 설치 차단 시 보안 정책을 우회하지 않는다.

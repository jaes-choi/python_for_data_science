# 05. Claude Code와 Google Antigravity(AGY) — Windows·macOS·Linux

Codex Quick Tour 후 수행한다. 세 도구는 **동일한 목표·데이터·테스트**로 비교한다. Claude Code는 일반적으로 유료 플랜/유료 API 사용 권한이 필요하고, AGY는 무료·유료 플랜이 있다. 이용 자격·한도는 수업 직전에 다시 확인한다.

## 1. Claude Code 설치
공식 안내: https://code.claude.com/docs/en/setup

### Windows 11 — PowerShell
~~~powershell
winget install Anthropic.ClaudeCode
claude --version
claude
~~~
설치 직후 명령을 찾지 못하면 새 PowerShell을 실행한다.

### macOS — Terminal(zsh)
~~~bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
claude
~~~
Homebrew를 사용하는 경우 공식 문서가 지원하는 명령을 별도로 확인한다.

### Ubuntu/Debian 등 Linux — Bash
~~~bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
claude
~~~
설치 스크립트를 실행하기 전에 URL과 내용을 공식 문서에서 확인한다. 회사·학교 PC의 정책을 우회하지 않는다. 로그인 후 구독/API 자격을 확인한다. 모델 호출 비용은 사용하는 계정·플랜에 따라 다르다.

### 첫 번째 Claude Code 실습
프로젝트 복제본으로 이동한 뒤 `claude`를 실행하고 다음을 입력한다.
~~~text
agent_lab/work 디렉터리의 쇼핑 계산기를 검사하라.
가격 미확인 품목 처리, 수량 입력 검증 및 자동 테스트의 누락 사례를 찾아라.
수정 계획을 먼저 설명하고 승인된 파일만 변경하라.
테스트를 실행한 후 실행 명령, 출력, 수정 파일을 보고하라.
원본 data/, script/, docs/ 수정 및 Git push는 금지한다.
~~~

## 2. Google Antigravity(AGY) 설치
공식: https://antigravity.google/download 및 https://antigravity.google/docs/getting-started?tab=cli

### A. AGY CLI — OS별 설치
**Windows 11 — PowerShell**
~~~powershell
irm https://antigravity.google/cli/install.ps1 | iex
agy --version
agy
~~~

**macOS — zsh 및 Linux — Bash**
~~~bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy --version
agy
~~~
설치 파일은 공식 출처를 확인하고 실행한다. PATH가 적용되지 않으면 새 터미널을 열고 `command -v agy`를 실행한다. 기본 설치 경로 예시는 `~/.local/bin/agy`다.

### B. AGY 데스크톱 앱
Windows는 공식 다운로드 페이지에서 x64 또는 ARM64 설치 파일을 내려받아 실행한다.
macOS는 Apple Silicon 또는 Intel용 `.dmg`를 선택해 설치한다.
Linux는 **지원하는 x64/ARM64 아키텍처** 및 `glibc >= 2.28`, `glibcxx >= 3.4.25` 조건을 확인하고 공식 아카이브를 내려받는다:
~~~bash
tar -xzf Antigravity.tar.gz
./Antigravity
~~~
파일명은 실제 다운로드 파일 이름에 맞춰 변경한다. 예: Ubuntu 20+, Debian 10+, Fedora 36+, RHEL 8+ (배포판 상세 조건은 공식 안내 확인). GUI가 없는 Linux 서버라면 CLI를 사용한다.

### 첫 번째 AGY 실습
~~~text
현재 작업 폴더의 agent_lab/work만 대상으로 한다.
기존 쇼핑 계산기를 CSV 파일에서 입력받는 프로그램으로 확장하라.
가격이 없는 빵의 값을 임의로 채우지 말고 누락을 기록하라.
수정 계획을 먼저 보여 주고 파일 변경·명령 실행 승인 후 테스트하라.
작업한 파일 목록과 결과를 보고하고 push와 외부 전송은 하지 마라.
~~~

## 3. 학습자 비교표
| 확인 항목 | Codex | Claude Code | AGY |
|---|---|---|---|
| OS/설치 버전 | 직접 기록 | 직접 기록 | 직접 기록 |
| 계정·요금·사용량 | 확인 | 확인 | 확인 |
| 파일 변경 범위 | 검토 | 검토 | 검토 |
| 테스트 명령/성공 여부 | 관찰 | 관찰 | 관찰 |
| 누락 가격 처리 | 6,000원, 총액 미확정 | 동일 | 동일 |
| 빵 가격 추가 | 10,500원 | 동일 | 동일 |

도구별 UI나 결과물의 문구는 달라도 된다. **정확성, 테스트 실행, 변경 승인 기록**이 동일 기준이다.

## 4. 흔한 오류
- `command not found`: 설치 기록과 PATH 확인, 새 터미널 열기
- 인증 실패: 인터넷, 계정·플랜·지역·권한 확인
- Linux GUI 실행 실패: 배포판·CPU 아키텍처·glibc, 디스플레이 세션 확인
- 요청 제한: 과제 진행을 멈추고 무료 대안으로 전환, 제한 우회/계정 공유 금지

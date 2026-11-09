# 06. 무료 AI Agent — 가격이 아니라 사용 제약 비교

무료라고 해서 **무제한·영구 무료·API도 무료**라는 뜻은 아니다. 2026-11 기준 계획이며 수업 전 공지 및 사용 한도를 재확인한다.

| 선택지 | 무료로 가능한 일 | 대표적 제한 |
|---|---|---|
| Codex | 해당 계정/이용 자격에 따라 체험 | 계정 플랜, 요청/시간 한도, 모델 선택 |
| Antigravity | 개인 무료 플랜에서 체험 | 지역·계정·사용량 제한 |
| OpenCode | 오픈소스 에이전트, 일부 무료 제공 모델 연결 | 모델 제공 시점·무료 한도·서비스 정책 |
| GitHub Copilot CLI | GitHub 무료 플랜 한도 내 이용 | 월간 요청량 및 학생 인증 여부 |
| Ollama + OpenCode | 로컬에서 추론(별도 클라우드 API 과금 불필요) | 컴퓨터 메모리, 다운로드 크기, 코딩·도구 호출 품질 |

## OpenCode 설치
공식: https://opencode.ai/docs/
- Windows: 공식 Windows 설치/배포 방식 또는 `winget` 지원 여부를 공식 문서에서 확인한다.
- macOS: Homebrew 사용 PC는 `brew install anomalyco/tap/opencode` 등 **공식 문서의 현재 명령**을 확인한다.
- Linux: 공식 설치 스크립트 `curl -fsSL https://opencode.ai/install | bash`를 공식 사이트에서 확인한 뒤 실행한다.
설치 확인: `opencode --version`; 실행: `opencode`. 로그인/모델 선택 단계에서 **결제 수단과 유료 모델 선택 여부**를 반드시 확인한다.

## GitHub Copilot CLI
공식 설치: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli
OS별로 지원하는 설치 방법을 사용한다. Windows 예시:
~~~powershell
winget install GitHub.Copilot
copilot --version
copilot
~~~
macOS/Linux는 공식 패키지 관리자 및 릴리스 절차를 따른다. GitHub Education 인증 학생에게 추가 혜택이 제공될 수 있으나 자동으로 보장되지 않는다.

## 무료 도구의 실제 한계 실험
1. 같은 쇼핑 계산기 프롬프트로 결과 생성
2. 가격 누락, 잘못된 CSV, 3회 연속 오류 수정 요청
3. 코드 정확성·실행 명령·테스트 로그·응답 실패/제한 알림 기록
4. 실제 사용량/대기시간을 기록하되 유료 요금 정보를 추측하지 않는다

**판단 기준:** 한도보다 중요한 것은 ‘제출물의 정확성’과 ‘결과 검증 가능성’이다.

# AI Agent 입문 — 설치부터 검증까지

> **대상:** Python 기초(변수·문자열·리스트·딕셔너리·반복문)를 배운 학생  
> **실습 환경:** Windows 11 PowerShell / macOS Terminal(zsh) / Linux Ubuntu·Debian Bash  
> **기준일:** 2026-11-09 · 제품·무료 한도·화면은 변경될 수 있으므로 수업 전에 공식 안내를 재확인  
> **소스 저장소:** [python_for_data_science](https://github.com/jaes-choi/python_for_data_science)

## 학습 목표
1. 챗봇과 코딩 에이전트의 차이(계획→도구 실행→관찰→수정)를 설명한다.
2. Codex를 설치하고 자기 컴퓨터의 제한된 실습 폴더에서 Python 코드를 만들고 실행한다.
3. 쇼핑 계산기 프로그램을 개선하고 테스트를 통과시킨다.
4. AI가 작성한 코드·실행 명령·수정 이력을 검증한다.
5. Claude Code와 Google Antigravity(AGY)를 비교하여 자신의 환경에 맞게 선택한다.
6. 무료 서비스의 **요청 한도와 모델·비용** 차이를 이해한다.
7. Ollama와 OpenCode를 연결하여 로컬 LLM 에이전트를 시험하고 한계를 기록한다.

## 학습 경로 (필수 01~04, 선택 05~07)

| 장 | 제목 | 결과물 | 권장 시간 |
|---|---|---|---|
| [01](01-introduction.md) | AI Agent란? | 에이전트 구성도·성공 기준 | 15분 |
| [02](02-codex-quick-tour.md) | Codex Quick Tour: 설치부터 첫 실행 | `shopping.py`, `test_shopping.py` | 35~50분 |
| [03](03-integrated-project.md) | 통합 실습: 쇼핑 → CSV → 보고서 | `shopping_report.csv`, 검증 기록 | 40~60분 |
| [04](04-verification-safety.md) | 검증과 안전 | 테스트, Git diff, 승인 기록 | 20~30분 |
| [05](05-claude-agy.md) | Claude Code 및 AGY 설치·사용 | 같은 과제의 비교 실습 | 30~50분 |
| [06](06-free-agents.md) | 무료 도구와 그 한계 | 비교표, 무료 한도 점검 | 20~30분 |
| [07](07-local-llm.md) | Ollama + OpenCode 로컬 LLM | 로컬 모델 에이전트 실행 기록 | 30~60분 |
| [08](08-troubleshooting.md) | 문제 해결 부록 | 오류 진단표 | 필요할 때 |
| [09](09-instructor-guide.md) | 강사용 진행·채점 안내 | 평가 루브릭 | 강사용 |

### 가장 짧은 실습 경로
`01` → `02` → `04`. **Codex에 로그인할 계정·사용 가능 한도**를 먼저 확인합니다. 무료 한도가 부족하면 `05`의 AGY 또는 `06`의 무료 대안을 사용합니다.

### 공통 원칙
- AI가 작성한 코드는 **사람이 검토**하고, 테스트 결과와 실행 명령을 함께 확인합니다.
- 작업 범위는 복제한 학습 폴더로 한정합니다. 원본 데이터는 읽기 전용입니다.
- 삭제·외부 전송·패키지 설치·Git push는 명시적 사전 승인을 받습니다.
- AI 에이전트가 실행하는 명령은 신뢰 수준에 따라 승인합니다. `--dangerously-bypass-approvals-and-sandbox` 같은 우회 옵션은 사용하지 않습니다.
- **원본 저장소의 `data/`·`script/`은 수정하지 않습니다.** 개인 실습은 복제한 폴더의 `agent_lab/`에서 합니다.
- 무료란 **툴 설치가 무료인 것**, **모델 API 호출도 무료인 것**, **한도 내 무료인 것**이 다릅니다.

## 실습 파일
- [shopping.py](../../agent_lab/shopping.py): 표준 라이브러리 기반 쇼핑 계산기
- [test_shopping.py](../../agent_lab/test_shopping.py): 내장 `unittest` 검증
- [sample_shopping.csv](../../agent_lab/sample_shopping.csv): CSV 확장 실습 데이터
- [shopping_report.py](../../agent_lab/shopping_report.py): CSV 읽기·보고서 생성 (외부 패키지 불필요)
- [traffic_report.py](../../agent_lab/traffic_report.py): 기존 교통사고 데이터 읽기와 결과 보고서(선택; pandas/matplotlib)
- [test_traffic_report.py](../../agent_lab/test_traffic_report.py): 합성 데이터 기반 집계 검증

## 기존 교재 연결
Python과 uv, VS Code 설치는 [기존 설치 안내](../python-setup/README.md)와 연결됩니다. 이 장에서 Python·Git·uv를 중복 설치하지 말고 현재 버전과 경로부터 확인하세요.

## 공식 참고 링크
- [Codex](https://github.com/openai/codex) · [Codex CLI](https://developers.openai.com/codex/cli/)
- [Claude Code](https://code.claude.com/docs/en/setup)
- [Google Antigravity](https://antigravity.google/docs/getting-started?tab=cli)
- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli)
- [OpenCode](https://opencode.ai/docs/)
- [Ollama](https://docs.ollama.com/) · [Ollama×OpenCode](https://docs.ollama.com/integrations/opencode)

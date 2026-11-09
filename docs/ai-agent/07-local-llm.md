# 07. 로컬 LLM을 위한 AI Agent — Ollama + OpenCode

**핵심:** 에이전트는 파일·명령 도구를 실행하고, Ollama는 로컬 모델 추론을 담당한다. 인터넷 연결 없이 동작하는지와 실제 외부 요청 여부는 **구성·모델 캐시·툴·환경**에 따라 다르다. 첫 설치 및 모델 다운로드는 인터넷이 필요하다.

## 1. Ollama 설치
공식: https://ollama.com/download · Linux: https://docs.ollama.com/linux

**Windows 11 / macOS:** 공식 다운로드 페이지에서 OS별 설치 파일을 받아 실행. PowerShell/터미널에서:
~~~bash
ollama --version
ollama list
~~~

**Ubuntu/Debian Linux (일반 사용자, 공식 스크립트 내용 검토 후):**
~~~bash
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
ollama list
~~~
Linux에서는 설치 후 서비스 상태도 확인:
~~~bash
systemctl status ollama
~~~
서비스 관리자가 systemd가 아닌 환경에서는 해당 OS 방식으로 Ollama 서버를 실행한다. 서버 통신 확인: `curl http://localhost:11434/api/tags`. 윈도우는 PowerShell의 `Invoke-RestMethod http://localhost:11434/api/tags`.

## 2. 가벼운 모델부터 시작
~~~bash
ollama pull qwen3:4b
ollama run qwen3:4b
~~~
모델 이름·용량·지원 기능은 수업 전 https://ollama.com/library 에서 확인한다. RAM이 부족하면 더 작은 모델을 선택하고, 큰 모델이 반드시 성공한다는 설명은 하지 않는다.

## 3. 에이전트(OpenCode) 연결
OpenCode 설치: [무료 도구 안내](06-free-agents.md).
Ollama 공식 통합 안내: https://docs.ollama.com/integrations/opencode

지원 버전에서 공식 통합 명령:
~~~bash
ollama launch opencode
~~~
위 명령이 없으면 Ollama와 OpenCode 버전·연동 문서를 확인하고, OpenCode의 모델 설정에서 로컬 Ollama 제공자를 연결한다. **원격 유료 모델을 잘못 선택하지 않도록 모델/프로바이더를 확인**한다.

## 4. 로컬 실행 과제
~~~text
agent_lab/work 내부에 shopping_local.py만 생성하라.
누락 가격은 임의로 채우지 말고, 확인된 금액과 미확정 여부를 출력하라.
test_shopping_local.py를 생성하고 실제 실행하라.
실행 명령, 종료 코드, 테스트 결과를 보고하라.
그 외 폴더 수정·외부 업로드·삭제·git push는 하지 마.
~~~
비교: 동일 과제를 Codex에서 실행해 정답, 파일 변경량, 오류 복구 횟수, 속도를 기록한다.

## 5. 꼭 이해할 한계
- 모델 크기와 코딩 능력은 다르며, 로컬 모델이 도구 호출을 제대로 지원하는지 확인한다.
- 메모리(시스템 RAM/VRAM)가 부족하면 느리거나 모델 로드가 실패한다.
- ‘에이전트 코드가 로컬’ ≠ ‘데이터가 반드시 외부로 안 나감’: 플러그인·원격 도구·모델 설정을 점검한다.
- 무료 클라우드와 로컬은 비용 체계가 다르다(전력/시간/하드웨어 비용은 존재).
- 교실 PC에 GPU가 없어도 소형 모델로 개념 실습은 가능하나 처리 속도가 다르다.

## 실패 시 점검
`ollama list` → 서버 상태 → `ollama run qwen3:4b` 단독 응답 → OpenCode가 실제로 선택한 모델 → 툴 호출 가능 여부 → 에이전트 로그. 모델을 내리거나 변경하기 전에 원인을 기록한다.

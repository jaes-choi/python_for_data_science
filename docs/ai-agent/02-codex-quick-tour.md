# 02. Quick Tour — Codex로 처음부터 끝까지

**목표:** OS별로 설치한 Codex가 직접 `.py` 파일을 만들고 실행하며 테스트하는 과정을 관찰합니다. 학생은 첫 로그인과 작업 승인에 참여합니다.

## 0) 필요한 환경
- 인터넷, 사용 가능한 ChatGPT 계정, Git, PowerShell(Windows) 또는 Terminal(macOS·Linux)
- Python 실행 방법은 [Python 설치 교재](../python-setup/README.md) 참고. `python --version` 또는 `python3 --version` 확인
- Codex 사용 자격과 사용량은 [공식 요금 안내](https://developers.openai.com/docs/pricing)에서 수업 당일 확인

## 1) 설치 전 확인 — OS별로 구분
**Windows 11 — PowerShell**
~~~powershell
git --version
py --version
~~~
Git이 없으면 `winget install --id Git.Git -e`로 설치 후 **새 터미널**을 엽니다. Python이 없는 학생은 기존 `uv` 설치 장부터 진행합니다.

**macOS — Terminal**
~~~bash
git --version
python3 --version
~~~

**Ubuntu/Debian Linux — Bash**
~~~bash
git --version
python3 --version
~~~
명령이 없다면 (배포판과 sudo 권한이 허용되는 실습 PC에 한함):
~~~bash
sudo apt update
sudo apt install -y git python3
~~~
Fedora/RHEL 등은 패키지 관리자가 다르므로 `dnf` 등 해당 배포판 공식 안내를 이용합니다.

## 2) Codex 설치
아래 설치 스크립트는 **출처를 공식 사이트에서 먼저 확인한 뒤** 실행합니다. 서로 다른 방법을 중복 실행할 필요가 없습니다.

**Windows 11 PowerShell**
~~~powershell
irm https://chatgpt.com/codex/install.ps1 | iex
codex --version
~~~

**macOS / Linux (Bash 또는 zsh)**
~~~bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex --version
~~~

다른 설치 방식: Node.js npm이 이미 설치된 PC에서는 `npm install -g @openai/codex`. macOS(Homebrew)는 `brew install --cask codex`.

설치 뒤 명령을 찾지 못하면 터미널을 닫았다 열고 `where.exe codex`(Windows) 또는 `command -v codex`(macOS·Linux)로 실행 경로를 확인합니다. 무작정 다시 설치하지 않습니다.

## 3) 실습용 저장소 준비
**Windows PowerShell**
~~~powershell
cd $HOME
git clone https://github.com/jaes-choi/python_for_data_science.git python-agent-study
cd python-agent-study
New-Item -ItemType Directory -Force agent_lab\work | Out-Null
git status --short
codex
~~~

**macOS / Linux Bash·zsh**
~~~bash
cd "$HOME"
git clone https://github.com/jaes-choi/python_for_data_science.git python-agent-study
cd python-agent-study
mkdir -p agent_lab/work
git status --short
codex
~~~
이미 복제한 폴더가 있으면 `git clone`을 반복하지 않고 그 폴더로 이동합니다. 처음 실행 시 **Sign in with ChatGPT** 등 로그인 선택지를 확인하세요.

### 왜 따로 clone하는가?
기존 실습 자료를 보존하고 실습 중 생긴 변경 내용을 `git status`와 `git diff`로 확인하기 위해서입니다. GitHub에 push할 필요는 없습니다.

## 4) 첫 번째 프롬프트
다음을 Codex 대화창에 붙여 넣습니다.

~~~text
나는 Python을 처음 배우는 학생이다.
현재 저장소의 agent_lab/work 안에서만 작업하라.

목표: 다음 자료로 쇼핑 계산기를 만들어라.
item_prices = {"우유": 1000, "계란": 3000, "소고기": 9000, "라면": 800}
shopping_list = [["우유", 2], ["빵", 3], ["라면", 5]]

요구사항:
1. shopping.py와 test_shopping.py를 직접 생성할 것.
2. 품목명, 수량, 가격, 소계를 출력할 것.
3. 목록에 있으나 가격표에 없는 빵은 누락으로 표시할 것.
4. 가격 없는 품목을 0원이라고 가정하거나 총액을 확정하지 말 것.
5. 프로그램과 테스트를 실제 실행하고, 명령·출력·실패 여부를 보고할 것.
6. 테스트가 실패하면 수정하고 재실행할 것.
7. data/, script/, docs/와 기존 파일은 수정하지 말 것.
8. 삭제·패키지 설치·네트워크 업로드·git push는 승인 없이 하지 말 것.
~~~

## 5) 기대 결과를 사람이 검증
~~~text
우유: 2 × 1,000 = 2,000원
라면: 5 × 800 = 4,000원
확인된 소계: 6,000원
가격 누락: 빵
전체 총액: 미확정
~~~
실제로 만든 코드의 출력 형식은 달라도 됩니다. **값과 의미**가 일치해야 합니다.

## 6) 수정 요청
~~~text
빵은 1,500원이다. 가격표에 빵을 추가하고 재실행하라.
정확한 총액 10,500원을 검증하는 자동 테스트를 추가하라.
기존에 가격이 누락됐을 때의 처리도 계속 테스트하라.
~~~

## 7) 에이전트가 바꾼 것 확인
~~~bash
git status --short
git diff -- agent_lab/
~~~
Windows PowerShell에서도 위 두 Git 명령은 같습니다. 새로 만들어진 미추적 파일은 `git diff`에 나오지 않으므로 VS Code에서 내용을 열어 확인합니다.

## 8) 채점 체크
- [ ] 설치 버전 확인·로그인
- [ ] 작업 폴더가 저장소 아래인가?
- [ ] 코드 파일과 테스트 파일이 생성됐는가?
- [ ] 테스트 명령과 출력이 실제로 확인되는가?
- [ ] 누락 가격을 임의로 채우지 않았는가?
- [ ] 10,500원을 사람이 계산하여 비교했는가?
- [ ] 승인 범위 밖의 변경이 없었는가?

**참고 정답:** [shopping.py](../../agent_lab/shopping.py), [test_shopping.py](../../agent_lab/test_shopping.py). 수업에서는 에이전트가 먼저 생성하게 하고 정답은 마지막에 공개합니다.

**공식 자료:** https://github.com/openai/codex · https://learn.chatgpt.com/docs/codex/cli

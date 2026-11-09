# 03. 통합 실습 — 쇼핑 계산기에서 CSV 보고서까지

**목표:** 목표 정의 → 구현 → 실행 → 검증 → 개선을 한 번에 경험한다. 기존 소스 대신 학생의 복제본 `agent_lab/work/`에서 실습한다.

## 실습 A. 원래 문제 다시 보기
가격표: 우유 1,000원, 계란 3,000원, 소고기 9,000원, 라면 800원. 쇼핑: 우유 2개, 빵 3개, 라면 5개.
빵 가격이 없으므로 확정 총액을 표시하면 틀린다. 확인된 소계는 6,000원이다. 빵 가격 1,500원을 추가하면 총 10,500원이다.

### 단계별 AI 에이전트 지시
~~~text
1) agent_lab/work에서만 shopping.py와 unittest 테스트를 만들어라.
2) 미등록 품목의 가격을 임의로 추측하지 마라. 확인된 소계와 누락 목록을 별도 출력하라.
3) Python을 실행하고 테스트를 통과시켜라.
4) 동일한 기능을 CSV 입력으로 확장하고 출력은 agent_lab/work/output 에만 저장하라.
5) 실행 명령, 예상값, 검증값, 생성한 파일과 한계를 보고하라.
기존 data/, script/, docs/ 수정, 외부 전송, push, 삭제 명령은 금지한다.
~~~

## 실습 B. CSV 읽기 및 결과 기록
참고 구현: [shopping_report.py](../../agent_lab/shopping_report.py)와 [sample_shopping.csv](../../agent_lab/sample_shopping.csv).
CSV에는 가격표가 아니라 **구매 목록**이 있으므로 코드의 가격표를 참조한다. 원본 데이터에는 빵 가격이 없으므로 검증 가능한 보고서는 누락을 표현해야 한다.

**실행 (저장소 루트):**
~~~powershell
# Windows PowerShell
uv run --no-project python agent_lab/shopping_report.py
uv run --no-project python -m unittest discover -s agent_lab -p "test_*.py"
~~~
~~~bash
# macOS·Linux
python3 agent_lab/shopping_report.py
python3 -m unittest discover -s agent_lab -p 'test_*.py'
~~~
Windows에서 uv가 없으면 `py agent_lab/shopping_report.py`로 실행한다. Python 실행기 선택은 [설치 교재](../python-setup/README.md) 참조. 출력은 `agent_lab/output/` 아래에 생성된다.

## 실습 C. 기존 데이터 분석으로 확장(선택)
기존 파일 `data/2016년_교통사망사고정보.csv`를 읽어 요일별 사고 건수와 지역별 사망자 합계를 구한다.
~~~bash
uv run --with pandas --with matplotlib agent_lab/traffic_report.py
~~~
**주의:** ‘요일별 사망사고 건수’와 ‘요일별 사망자 수’는 서로 다르다. 데이터는 **사망사고 데이터**이므로 모든 교통사고의 발생 위험을 대표하지 않는다. 지역별 인구·운행량이 없는 단순 합계를 위험도라고 해석하지 않는다.

## 제출물
작업 지시문, `git status`, 생성한 `.py` 파일, 테스트 실행 결과, 보고서 CSV, 사람이 계산한 정답과 AI 결과 비교, 에이전트가 틀린 부분 1개와 수정 이력.

**통과 기준:** 소계 6,000원, 총액 미확정, 빵 1,500원 추가 후 총액 10,500원, `unittest` 통과, 원본 데이터 유지.

# 03. 프로젝트 생성과 환경 재현

앞에서는 기존 `python-study` 폴더에 패키지를 설치했다. 이번에는 **별도 프로젝트를 새로 만들고, 다른 컴퓨터에서 같은 환경을 재현**해 본다.

## 새 프로젝트 만들기 (Windows PowerShell)

`python-study` **바깥의 작업 폴더**에서 시작한다. 아래 명령은 새로운 `hello-uv` 폴더를 만들므로 앞에서 만든 `.venv`를 재생성할 필요가 없다.

**0. 앞 장에서 사용한 `python-study` 폴더에 아직 있다면 상위 폴더로 이동** (이미 다른 작업 폴더라면 생략)

```powershell
cd ..
```

**1. 새 프로젝트 생성**

```powershell
uv init --no-package hello-uv
```

![실제 uv init 프로젝트 생성 결과](images/08-project-init.png)

**2. 프로젝트 폴더로 이동**

```powershell
cd hello-uv
```

**3. 기본 프로그램 실행**

```powershell
uv run main.py
```

![실제 uv run 실행 결과](images/10-project-run.png)

`--no-package`는 처음 배우기 쉬운 `main.py` 중심 구조를 만든다. `uv run`은 필요하면 환경을 생성·동기화한 뒤 프로그램을 실행한다. 새 패키지 추가·삭제 방법은 [02장](02-packages.md)에 정리했다.

## 프로젝트를 구성하는 파일

```text
hello-uv/
├── main.py            # 프로그램
├── README.md          # 프로젝트 설명
├── pyproject.toml      # 프로젝트 설정·필요 패키지
├── .python-version     # 선택한 Python 버전
├── .gitignore          # Git 제외 규칙
├── uv.lock             # 잠금 파일 (의존성 해결 후)
└── .venv/              # 로컬 가상환경 (실행·동기화 후)
```

파일 생성 시점과 세부 구성은 uv 버전 및 설정에 따라 다를 수 있다. Git 저장소를 초기화했다면 `.git/`도 존재한다.

| 파일 | GitHub에 올릴까? | 이유 |
|---|---|---|
| `main.py`, `README.md` | 예 | 프로그램과 설명 |
| `pyproject.toml`, `uv.lock`, `.python-version` | 예 | 환경을 재현하는 정보 |
| `.venv/` | 아니요 | 컴퓨터마다 다시 생성할 실행환경 |

`.gitignore`에 다음 항목이 있는지 확인한다.

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ipynb_checkpoints/
```

## 다른 컴퓨터에서 환경 재현하기

GitHub에 소스코드와 위 설정 파일을 저장했다고 가정한다. **Git은 uv와 별개로 설치**해야 한다. 아래 주소는 예시이므로 실제 저장소 주소로 바꾼다.

**1. 저장소 복제**

```powershell
git clone https://github.com/사용자명/저장소명.git
```

**2. 저장소 폴더로 이동**

```powershell
cd 저장소명
```

**3. 저장된 잠금 파일로 환경 재현**

```powershell
uv sync --locked
```

**4. 프로그램 실행** (복제한 저장소에 `main.py`가 있을 때)

```powershell
uv run main.py
```

`uv sync`는 프로젝트 환경을 동기화하고, 기본적으로 `uv.lock`에 기록되지 않은 패키지를 제거한다. `--locked`는 프로젝트 설정과 잠금 파일이 일치하는지 검사하여 **잠금 파일을 임의로 갱신하지 않도록** 한다.

프로젝트 폴더가 많아졌다면 [06. 고급 활용 Q&A](06-advanced.md)에서 폴더 정리와 디스크 절약 방법을 확인한다.

공식 자료: [프로젝트 생성](https://docs.astral.sh/uv/concepts/projects/init/) · [프로젝트 환경 동기화](https://docs.astral.sh/uv/concepts/projects/sync/)

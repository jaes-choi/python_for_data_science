# 06. 고급 활용 Q&A — 기존 환경·용량·폴더 정리

기본 사용법은 [Quick Tour](README.md)에서 먼저 익힌다. 여기서는 기존 Python/Anaconda를 정리하거나 여러 프로젝트를 관리할 때 필요한 내용만 다룬다.

## Q1. 기존 Python이나 Anaconda를 꼭 유지해야 하나?

**사용하지 않는다면 제거해도 된다.** Python 입문 실습만 한다면 uv만으로 Python 설치·버전·패키지 관리가 가능하다.

다만 **이미 작업 중인 프로젝트가 있다면 이전·실행 확인 후 제거**한다. 특히 Conda 전용 패키지, Notebook 커널, 다른 프로그램이 참조하는 환경이 있는지 확인한다. 제거할 때는 Windows의 **설정 → 설치된 앱**에서 해당 Python/Anaconda를 선택한다. 시스템 폴더를 직접 삭제하지 않는다.

기존 Conda 프로젝트를 계속 써야 한다면 기존 환경을 유지하고 새 uv 프로젝트와 분리한다.

## Q2. 기존 Python을 그대로 uv에서 쓸 수도 있나?

가능하다. uv는 설치된 Python을 찾아 사용한다.

```powershell
uv python list --only-installed
```

이미 설치한 Python 3.12를 반드시 사용하려면 (해당 버전이 있어야 한다):

```powershell
uv venv --no-managed-python --python 3.12
```

특정 버전이 없다면 uv가 필요에 따라 다운로드하도록 두는 편이 간단하다. 기존 Python을 지워도 **다른 프로그램이 사용하는 Python인지**는 먼저 확인한다.

## Q3. uv 버전은 매번 업데이트해야 하나? `-e`는 무슨 뜻인가?

**정상 작동하면 매번 업데이트할 필요는 없다.** 새 Python 버전 지원이나 버그 수정이 필요할 때 업데이트한다.

버전 확인:

```powershell
uv --version
```

Windows `winget`으로 설치했다면:

```powershell
winget upgrade --id=astral-sh.uv -e
```

`-e`는 `--exact`로, 지정한 **패키지 ID와 정확히 일치하는 항목만** 선택한다는 뜻이다.

공식 standalone 설치 프로그램으로 설치했다면:

```powershell
uv self update
```

macOS에서 Homebrew로 설치했다면:

```bash
brew upgrade uv
```

설치 방식이 다르면 해당 패키지 관리자로 업데이트한다. uv 업데이트와 Python 버전 변경은 별개다.

## Q4. 프로젝트를 만들 때 폴더는 어떻게 구성하면 좋을까?

**프로젝트 1개 = 폴더 1개 = 프로젝트 전용 `.venv` 1개**로 시작한다.

```text
projects/
├── python-study/
│   ├── main.py
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── .python-version
│   └── .venv/             # 로컬 가상환경
├── mini-game/
│   ├── main.py
│   ├── pyproject.toml
│   ├── uv.lock
│   └── .venv/
└── text-tool/
    ├── main.py
    ├── pyproject.toml
    ├── uv.lock
    └── .venv/
```

Windows PowerShell에서 새 프로젝트 생성 예:

```powershell
mkdir projects
```

```powershell
cd projects
```

```powershell
uv init --no-package mini-game
```

```powershell
cd mini-game
```

```powershell
uv add requests
```

별도의 공용 `site-packages` 폴더에 여러 프로젝트를 섞어 설치하거나, 모든 프로젝트에 동일한 `.venv`를 공유하는 방식은 피한다.

## Q5. 프로젝트마다 `.venv`를 만들면 용량이 계속 늘어나지 않나?

프로젝트마다 설치된 패키지는 공간을 사용하므로 **용량이 완전히 일정하지는 않다.** 그러나 uv는 다운로드한 패키지를 **공통 캐시**로 재사용하고, 가능한 환경에서는 파일 링크를 이용한다. Python 실행 환경을 매번 처음부터 내려받는 방식과는 다르다.

용량을 줄이는 기본 원칙:

1. 필요한 Python 버전만 유지한다. 새 프로젝트마다 무조건 다른 Python 버전을 설치하지 않는다.
2. `uv add`로 **그 프로젝트에 필요한 패키지만** 설치한다. 대형 ML 패키지 등을 모든 프로젝트에 넣지 않는다.
3. uv 캐시와 `.venv`를 **가능하면 같은 드라이브/파일시스템**에 둔다. 서로 다르면 파일 복사로 전환되어 디스크를 더 사용할 수 있다.
4. 사용하지 않는 프로젝트의 `.venv`는 **프로젝트 설정 파일을 확인한 뒤** 정리할 수 있다. 필요하면 `uv sync`로 다시 만든다.

uv가 사용하는 경로 확인:

```powershell
uv cache dir
```

```powershell
uv python dir
```

캐시는 모든 프로젝트에서 재사용되며, 관리형 Python도 별도 공통 위치에 저장된다. **캐시 폴더와 Python 설치 폴더를 직접 삭제하지 않는다.**

## Q6. uv 캐시를 정리하면 얼마나 안전한가?

불필요한 캐시 항목을 제거하려면 다음 명령을 사용한다.

```powershell
uv cache prune
```

이 명령은 사용하지 않는 캐시 항목을 정리한다. 중앙 관리형 프로젝트 환경이 있다면 해당 환경도 정리되며 필요할 때 다시 만들어진다.

반면 `uv cache clean`은 **전체 캐시를 지워** 이후 재다운로드와 재설치 비용이 커질 수 있으므로 일상적인 정리 용도로 권장하지 않는다.

## Q7. GitHub에는 어떤 파일만 올리면 되나?

**소스코드와 환경을 재현할 정보만** 올린다.

- 포함: `.py`, `pyproject.toml`, `uv.lock`, `.python-version`, `README.md`
- 제외: `.venv/`, `__pycache__/`, `.pytest_cache/`, `.ipynb_checkpoints/` 등 실행·임시 파일

프로젝트의 `.gitignore`에 아래 내용이 있는지 확인한다.

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ipynb_checkpoints/
```

다른 컴퓨터에서는 소스와 설정 파일을 받은 뒤 다음 명령으로 가상환경을 다시 만든다.

```powershell
uv sync
```

**정리:** Python과 캐시는 uv로 공통 관리, 가상환경은 프로젝트별 분리, GitHub에는 소스·설정만 보관한다.

공식 참고: [Python 버전 관리](https://docs.astral.sh/uv/concepts/python-versions/) · [저장 경로](https://docs.astral.sh/uv/reference/storage/) · [캐시 관리](https://docs.astral.sh/uv/concepts/cache/) · [프로젝트 관리](https://docs.astral.sh/uv/guides/projects/)

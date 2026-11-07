# Python 개발환경 Quick Tour — uv로 시작하기

Windows 기준 실습 가이드. macOS/Linux는 [별도 설치 안내](05-macos-linux.md)를 참고한다.

Python은 [python.org](https://www.python.org/downloads/)에서 설치할 수도 있지만, 여기서는 **uv**로 설치·관리한다.

**uv**는 Windows·macOS·Linux에서 작동하는 빠른 Python 관리 도구다.

| 장점 | 설명 |
|---|---|
| 간편함 | 명령어로 Python·가상환경·패키지 관리 |
| 자동 설치 | 필요한 Python 버전이 없으면 다운로드 |
| 여러 버전 | 프로젝트마다 다른 Python 환경 사용 |
| 빠른 속도 | 패키지 설치와 캐시 재사용 |
| OS 공통 사용 | 한번 배우면 Windows·macOS·Linux에서 동일한 uv 명령 활용 |
| AI 협업 | 설치·실행·오류 확인 절차를 명령어로 공유 |

### 잠깐! 왜 이름이 uv일까?

**uv는 *Ultraviolet*(자외선)에서 따온 이름**이다. 개발자 Charlie Marsh는 두 글자라 **짧고 입력하기 쉬우며**, 별·천체를 연상시키는 회사 이름 *Astral*과도 어울린다고 설명했다. 명령어를 자주 입력하는 개발자를 생각한 이름이다.

출처: [Charlie Marsh 인터뷰, *Test & Code* 216회 (2024년 3월 11일)](https://pythontest.com/testandcode/episodes/ruff-astral-uv-charlie-marsh/)

## Windows에서 시작하기 (PowerShell)

**1. uv 설치**

```powershell
winget install --id=astral-sh.uv -e
```

![Windows에서 winget으로 uv 설치 완료](images/01-winget-install.png)

**2. 새 PowerShell에서 설치 확인**

```powershell
uv --version
```

![uv 버전 확인 결과](images/02-uv-version.png)

**3. 작업 폴더 생성**

```powershell
mkdir python-study
```

**4. 작업 폴더로 이동**

```powershell
cd python-study
```

**5. Python 가상환경 생성**

```powershell
uv venv
```

![uv 가상환경 생성 결과](images/03-venv-create.png)

**6. Python 버전 확인**

```powershell
uv run python --version
```

![Python 버전 확인 결과](images/04-python-version.png)

**7. Python 실행 확인**

```powershell
uv run python -c "print('Hello, Python!')"
```

![첫 Python 코드 실행 결과](images/05-hello-python.png)


`uv venv`는 프로젝트 폴더의 `.venv`에 가상환경을 만든다. 이미 사용 가능한 Python을 활용하거나 필요하면 다운로드한다. **반드시 최신 Python을 고르는 것은 아니다.** 자세한 구조는 [01. Python과 가상환경](01-install.md)을 참고한다.

이어서 패키지를 관리하려면 [02. 패키지 관리와 개발 도구](02-packages.md), 새 프로젝트를 만들고 다른 컴퓨터에서 재현하려면 [03. 프로젝트 생성과 환경 재현](03-projects.md)을 따라 한다.

**기존 Python·Anaconda 정리, uv 업데이트, 디스크 용량과 폴더 관리**는 [고급 활용 Q&A](06-advanced.md)를 참고한다.

## 자세히 보기

- [01. Python·가상환경과 생성 파일](01-install.md)
- [02. 패키지 관리와 개발 도구](02-packages.md)
- [03. 프로젝트 생성과 환경 재현](03-projects.md)
- [04. 자주 발생하는 오류](04-troubleshooting.md)
- [05. macOS / Linux 설치](05-macos-linux.md)
- [06. 고급 활용 Q&A — 기존 환경·용량·폴더 정리](06-advanced.md)

**참고:** uv를 설치해도 Git은 함께 설치되지 않는다. Git·GitHub는 별도로 다룬다.

공식 자료: [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) · [Python 자동 설치](https://docs.astral.sh/uv/guides/install-python/)

# 08. OS별 문제 해결

| 증상 | 확인 명령 | 해결 방향 |
|---|---|---|
| `codex`를 찾지 못함 | Windows: `where.exe codex`; Linux/macOS: `command -v codex` | 새 터미널, 설치 로그, PATH 확인 |
| `claude` 미인식 | `claude --version` | 설치 방법/권한, PATH 재확인 |
| `agy` 미인식 | `agy --help` | CLI를 제공하는 버전인지 확인, GUI로 실습 |
| Python 실행 불가 | `py --version` 또는 `python3 --version` | 기존 Python·uv 설치 문서 참조 |
| `ModuleNotFoundError` | `python -m pip --version` 및 Python 경로 | 현재 환경/가상환경과 패키지 연결 확인 |
| CSV `UnicodeDecodeError` | 파일 인코딩 확인 | CP949/UTF-8 등 원본 인코딩 지정 |
| CSV 파일 없음 | 현재 작업 폴더 확인 | 저장소 루트에서 실행; `data/`를 이동하지 않음 |
| 로그인 실패 | 계정 플랜·네트워크 | 사용 자격 확인; 비밀번호 공유하지 않음 |
| Ollama 연결 실패 | `ollama list`, 서비스 상태, localhost:11434 | 모델 로딩/서버/포트 확인 |
| 로컬 LLM이 코드만 답변 | 모델 도구 호출 지원 여부 확인 | 지원 모델 선택, 무리한 무승인 실행 금지 |

**Windows**: PowerShell의 `cd $HOME`, `Get-Location`, `Get-Command codex` 사용. 관리자 권한 실행은 기본이 아니다.

**macOS**: 터미널에서 `uname -m`, `command -v`, `echo $PATH`로 아키텍처/설치 경로 확인. Apple Silicon과 Intel 설치 자산을 구분한다.

**Linux**: `cat /etc/os-release`, `uname -m`, `which python3` 확인. Ubuntu/Debian의 `apt`와 Fedora/RHEL의 `dnf`는 다르다. 서비스가 systemd가 아닐 수 있다.

**진단 원칙:** 오류 전문, 실행 명령, 현재 폴더, OS·아키텍처·버전을 기록하고 반복 재설치 전에 설치 상태를 확인한다.

# Crenata 개발 시작하기

Crenata 기여에 관심을 가져주셔서 정말 감사합니다!

Crenata는 자원봉사자로 유지되는 오픈 소스 프로젝트이며 모든 형태의 기여를 환영합니다.

아래 섹션은 개발, 테스트를 시작하는 데 도움이 됩니다.

- [Crenata 개발 시작하기](#crenata-개발-시작하기)
  - [소스 코드 클론](#소스-코드-클론)
  - [개발 환경](#개발-환경)
    - [에디터](#에디터)
    - [종속성 설치](#종속성-설치)
      - [가상 환경 사용](#가상-환경-사용)
  - [정적 타이핑](#정적-타이핑)
    - [유형 검사](#유형-검사)
  - [테스트](#테스트)
    - [테스트 실행](#테스트-실행)
  - [코드 스타일](#코드-스타일)
    - [포맷팅](#포맷팅)

## 소스 코드 클론

Crenata를 작업 하려면 먼저 git에서 소스코드를 가져와야 합니다.

소스코드는 [GitHub](https://github.com/team-crescendo/Crenata)에서 사용할 수 있습니다.

```sh
git clone https://github.com/team-crescendo/Crenata
cd Crenata
```

## 개발 환경

Crenata는 [Python](https://www.python.org/)으로 개발된 디스코드 봇입니다.

Crenata는 Python 3.10 이상에서 개발 및 테스트 되었으며, 3.10 미만의 버전에서는 정상적인 작동을 보장 하기 어렵습니다.

### 에디터

Crenata의 개발 환경은 [VSCode](https://code.visualstudio.com/)에 최적화 되어있습니다.

코드 스타일 적용, 테스트, 타입 체크 등 여러 환경이 미리 준비되어 있습니다.

따라서 VSCode에서 작업하는 것을 권장합니다.

### 종속성 설치

Crenata는 [Poetry](https://python-poetry.org/)를 이용해 종속성을 관리하고 있습니다.

로컬에 Poetry가 이미 설치 되어있다면 다음 명령어를 사용하여 종속성을 설치 할수있습니다.

```sh
poetry install
```

#### 가상 환경 사용

Poetry를 로컬에 설치하기 부담스럽다면 가상환경을 사용하여 개발할수도 있습니다.

먼저 다음 명령어를 사용하여 가상 환경을 만들어 줍니다.

```sh
python -m venv .venv
```

가상 환경을 활성화 해줍니다.

Windows

``` powershell
.venv/Scripts/Activate.ps1
```

Linux/macOS

``` sh
.venv/bin/Activate.ps1
```

활성화가 완료 되었다면 다음 명령어를 사용해 가상 환경에 Poetry를 설치합니다.

Windows

``` powershell
.venv/Scripts/pip install -U pip setuptools
.venv/Scripts/pip install poetry
```

Linux/macOS

``` sh
.venv/bin/pip install -U pip setuptools
.venv/bin/pip install poetry
```

종속성을 설치합니다.

```sh
poetry install
```

## 정적 타이핑

Crenata는 정적 타이핑을 사용 하고 있습니다.

이는 쉬운 유지보수와 디버깅을 제공하며, 안정성을 높일수 있습니다.

[mypy](http://www.mypy-lang.org/)를 사용해 유형을 검사합니다.

### 유형 검사

다음 명령어를 사용하여 유형을 검사 할 수 있습니다.

```sh
poetry run mypy
```

## 테스트

Crenata는 [pytest](https://docs.pytest.org/en/7.1.x/)를 이용해 일부 코드를 테스트 하고있습니다.

### 테스트 실행

다음 명령어를 사용하여 테스트를 실행 할 수 있습니다.

```sh
poetry run pytest
```

## 코드 스타일

[black](https://github.com/psf/black) 및 [isort](https://github.com/PyCQA/isort)를 사용하여 코드 스타일을 일관성있게 유지 하고 있습니다.

가상환경에서는 ``.vscode\settings.json`` 에서 isort의 경로를 다음과 같이 수정해 주어야 할수도있습니다.

Windows

```json
{
    "python.sortImports.path": "${workspaceRoot}/.venv/Scripts/isort.exe"
}
```

Linux/macOS

```json
{
    "python.sortImports.path": "${workspaceRoot}/.venv/bin/isort.exe"
}
```

### 포맷팅

다음 명령어를 사용하여 포맷팅 할 수 있습니다.

```sh
poetry run black .
poetry run isort
```

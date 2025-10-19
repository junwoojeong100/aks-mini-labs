# AKS Mini Labs

Azure Kubernetes Service(AKS), 컨테이너 기술, CI/CD 자동화를 실습할 수 있는 핸즈온 랩 가이드입니다. Jupyter Notebook 기반으로 단계별 실습을 제공합니다.

## 📋 목차

- [학습 목표](#학습-목표)
- [빠른 시작](#빠른-시작)
- [사전 요구사항](#사전-요구사항)
- [실습 내용](#실습-내용)
- [프로젝트 구조](#프로젝트-구조)
- [환경 변수 및 공통 설정](#환경-변수-및-공통-설정)
- [실습 시작](#실습-시작)
- [각 노트북별 주의사항](#각-노트북별-주의사항)
- [문제 해결](#문제-해결)
- [참고 자료](#참고-자료)
- [기여 및 피드백](#기여-및-피드백)
- [라이선스](#라이선스)

## 🎓 학습 목표

이 실습을 완료하면 다음을 할 수 있게 됩니다:

### 컨테이너 기초
- ✅ 컨테이너와 가상머신의 차이점 이해
- ✅ Dockerfile 작성 및 멀티 스테이지 빌드 구현
- ✅ 컨테이너 이미지 빌드 및 실행
- ✅ Azure Container Registry 활용

### Kubernetes & AKS
- ✅ AKS 클러스터 생성 및 관리
- ✅ Kubernetes Deployment 및 Service 작성
- ✅ HPA를 통한 자동 확장 구성
- ✅ Node Auto Provisioning 활용
- ✅ Prometheus/Grafana로 모니터링 구성

### CI/CD 자동화
- ✅ GitHub Actions 워크플로우 작성
- ✅ Azure Pipelines 구성
- ✅ GitOps 개념 이해 및 Argo CD 활용
- ✅ 자동화된 배포 파이프라인 구축

## 🚀 빠른 시작

### 방법 1: GitHub Codespaces (권장)
   
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/junwoojeong100/aks-mini-labs)

- 위 버튼을 클릭하거나 저장소에서 `Code` > `Create codespace on main` 선택
- 모든 도구가 자동으로 설치되며, 브라우저에서 바로 실습 가능
- Python 가상환경, Azure CLI, Docker, kubectl 자동 설정

### 방법 2: VS Code Dev Container (로컬)

1. **사전 준비**
   - [Docker Desktop](https://www.docker.com/products/docker-desktop) 설치
   - [VS Code](https://code.visualstudio.com/) 설치
   - [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 설치

2. **실행 방법**
   ```bash
   git clone https://github.com/junwoojeong100/aks-mini-labs.git
   cd aks-mini-labs
   code .
   ```
   - VS Code에서 `Reopen in Container` 알림 클릭
   - 또는 `Ctrl+Shift+P` → `Dev Containers: Reopen in Container` 실행

3. **자동 설정**
   - Python 가상환경 생성 (`.venv`)
   - Jupyter 커널 등록
   - Spring Boot 프로젝트 빌드
   - 모든 도구 설치 (Java 21, Maven, Docker, kubectl, Azure CLI)

### 실습 시작하기

1. **Azure CLI 로그인**
   ```bash
   az login --use-device-code
   ```

2. **노트북 실행 순서**
   - `01-container-basics.ipynb` → 컨테이너 기초 & ACR
   - `02-aks-hands-on.ipynb` → AKS 클러스터 운영
   - `03-cicd-automation.ipynb` → CI/CD 자동화

> 💡 **Tip**: Jupyter 커널은 자동으로 `Python (.venv)`로 설정됩니다.

## 🎯 사전 요구사항

### 필수 항목
- **Azure 구독**: [무료 계정](https://azure.microsoft.com/free/) 생성 가능
- **GitHub 계정**: Codespaces 사용을 위해 필요

### 선택 사항 (3번 노트북용)
- **Azure DevOps 계정**: Azure Pipelines 실습 시
- **GitHub Personal Access Token**: GitHub Actions 실습 시

### 비용 안내
이 실습에서 사용하는 주요 Azure 리소스:
- **Azure Container Registry (Basic)**: 약 $5/월
- **AKS 클러스터 (2 nodes, Standard_DS2_v2)**: 약 $140/월
- **Managed Prometheus & Grafana**: 사용량 기반

> 💡 **Tip**: 실습 완료 후 리소스를 삭제하면 비용을 최소화할 수 있습니다.

## 📚 실습 내용

### 01-container-basics.ipynb
컨테이너 기초부터 Azure Container Registry까지
- 컨테이너 개념 및 아키텍처
- Spring Boot 앱 컨테이너화
- Dockerfile 작성 및 이미지 빌드
- ACR에 이미지 푸시

### 02-aks-hands-on.ipynb
AKS 클러스터 생성 및 운영
- AKS 클러스터 생성 (약 5-10분 소요)
- 컨테이너 배포 및 서비스 노출
- HPA 오토스케일링 및 NAP(Node Auto Provisioning)
- Prometheus/Grafana 모니터링 설정

### 03-cicd-automation.ipynb
CI/CD 파이프라인 구축
- GitHub Actions 워크플로우 생성 (수동 활성화 필요)
- Azure Pipelines 설정
- Argo CD를 통한 GitOps 배포

> **참고**: GitHub Actions 워크플로우는 `.disabled` 확장자로 생성됩니다. 사용하려면 Secrets/Variables 설정 후 확장자를 제거하세요.

## 📁 프로젝트 구조

```
aks-mini-labs/
├── .devcontainer/                 # Dev Container 설정
│   ├── devcontainer.json          # 컨테이너 구성
│   └── setup.sh                   # 자동 설정 스크립트
├── 01-container-basics.ipynb      # 컨테이너 기초 실습
├── 02-aks-hands-on.ipynb          # AKS 클러스터 실습
├── 03-cicd-automation.ipynb       # CI/CD 자동화 실습
├── config.py                      # 공통 환경 변수 설정
├── requirements.txt               # Python 패키지 의존성
├── deployment.yaml                # Kubernetes 배포 템플릿
├── springboot-docker-demo/        # Spring Boot 샘플 앱
│   ├── Dockerfile                 # 멀티 스테이지 빌드 설정
│   ├── pom.xml                    # Maven 설정
│   └── src/                       # 소스 코드
├── .github/
│   └── workflows/                 # GitHub Actions (3번에서 생성)
└── azure-pipelines.yml            # Azure Pipelines (3번에서 생성)
```

## ⚙️ 환경 변수 및 공통 설정

### config.py 사용법

모든 노트북에서 공통으로 사용하는 설정값은 `config.py` 파일에서 관리됩니다.

**주요 변수:**

| 변수명 | 설명 | 기본값 | 사용 노트북 |
|--------|------|--------|-------------|
| `RESOURCE_GROUP` | Azure 리소스 그룹 이름 | `aks-mini-labs-rg` | 01, 02, 03 |
| `LOCATION` | Azure 리전 | `koreacentral` | 01, 02, 03 |
| `ACR_NAME` | ACR 이름 (01번 실습 후 업데이트 필요) | `None` → 타임스탬프로 자동 생성 | 01, 02, 03 |
| `AKS_CLUSTER_NAME` | AKS 클러스터 이름 | `aks-mini-labs-cluster` | 02, 03 |
| `APP_NAME` | 애플리케이션 이름 | `myapp` | 01, 02, 03 |
| `IMAGE_TAG` | 이미지 태그 | `latest` | 01, 02, 03 |

**헬퍼 함수:**

- `get_acr_login_server(acr_name)`: ACR 로그인 서버 주소 반환 (예: `myacr123.azurecr.io`)
- `get_full_image_name(acr_name, app_name, tag)`: 전체 이미지 이름 생성
- `print_config()`: 현재 설정된 모든 변수 출력

**노트북에서 사용:**

```python
# 모든 설정 불러오기
from config import *

# 설정 확인
print_config()

# 개별 변수 사용
print(f"리소스 그룹: {RESOURCE_GROUP}")
```

> ⚠️ **중요**: `ACR_NAME` 업데이트 방법은 [각 노트북별 주의사항](#각-노트북별-주의사항)을 참고하세요.

## ⚠️ 각 노트북별 주의사항

### 01-container-basics.ipynb
- **ACR 이름 자동 생성**: ACR 이름이 타임스탬프로 자동 생성됩니다 (예: `myacr1760169422`)
- **ACR_NAME 수동 업데이트 필수**: 
  1. 노트북 실행 후 생성된 ACR 이름을 확인
  2. `config.py` 파일을 열어 `ACR_NAME` 값을 업데이트
     ```python
     # config.py 파일 수정 예시
     ACR_NAME = "myacr1760169422"  # 생성된 실제 이름으로 변경
     ```
  3. 파일 저장 후 02, 03번 노트북에서 해당 ACR 사용 가능

### 02-aks-hands-on.ipynb
- **AKS 클러스터 생성 시간**: 약 5-10분 소요
- **deployment.yaml 자동 생성**: Kubernetes 배포 매니페스트가 자동으로 생성됩니다

### 03-cicd-automation.ipynb
- **GitHub Actions 워크플로우 활성화**:
  - 워크플로우 파일이 `.disabled` 확장자로 생성됩니다
  - 활성화 절차:
    1. GitHub Repository Settings에서 Secrets 설정: `AZURE_CREDENTIALS`
    2. GitHub Repository Settings에서 Variables 설정: `ACR_NAME`
    3. `.github/workflows/` 디렉토리의 워크플로우 파일에서 `.disabled` 확장자 제거
- **Azure DevOps**: Azure Pipelines 사용 시 Service Connection 설정이 필요합니다

## 🛠️ 문제 해결

**ACR 로그인 실패**
- Azure CLI 로그인 세션이 만료되었을 수 있음
- `az login` 명령으로 재로그인

**이미지 빌드 실패**
- Docker 데몬이 실행 중인지 확인: `docker ps`
- 디스크 공간 확인: `df -h`

**Pod Pending 상태**
- `kubectl describe pod <pod-name>`으로 원인 확인
- NAP가 활성화되어 있으면 자동으로 노드 추가

**리소스 그룹 변경**
- `config.py`의 `RESOURCE_GROUP` 변수 수정
- 이후 모든 노트북에서 동일한 이름 사용

## 🔗 참고 자료

### 컨테이너 및 Docker
- [Docker 공식 문서](https://docs.docker.com/)
- [Spring Boot Docker 가이드](https://spring.io/guides/gs/spring-boot-docker)

### Azure 공식 문서
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/azure/aks/)
- [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/)

### Kubernetes
- [Kubernetes 공식 문서](https://kubernetes.io/docs/)
- [kubectl 치트시트](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

## 💬 기여 및 피드백

이 프로젝트에 기여하고 싶으시다면:
1. Fork 후 새로운 브랜치 생성
2. 변경사항 커밋
3. Pull Request 제출

버그 리포트나 기능 제안은 [Issues](https://github.com/junwoojeong100/aks-mini-labs/issues)를 이용해주세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

---

Made with ❤️ for Azure & Kubernetes learners

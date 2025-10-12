# AKS Mini Labs

Azure Kubernetes Service(AKS), 컨테이너 기술, CI/CD 자동화를 실습할 수 있는 핸즈온 랩 가이드입니다. Jupyter Notebook 기반으로 단계별 실습을 제공합니다.

## 📋 목차

- [학습 목표](#학습-목표)
- [빠른 시작](#빠른-시작)
- [사전 요구사항](#사전-요구사항)
- [실습 내용](#실습-내용)
- [프로젝트 구조](#프로젝트-구조)
- [환경 변수 및 공통 설정](#환경-변수-및-공통-설정)
- [주의사항](#주의사항)
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
- ✅ GitOps 개념 이해 및 ArgoCD 활용
- ✅ 자동화된 배포 파이프라인 구축

## 🚀 빠른 시작

1. **GitHub Codespaces에서 실행**
   
   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/junwoojeong100/aks-mini-labs)
   
   - 위 버튼을 클릭하거나 저장소에서 `Code` > `Create codespace on main` 선택
   - Docker, Azure CLI, kubectl 등이 사전 설치된 환경 제공

2. **노트북 순서대로 실습**
   - 01-container-basics.ipynb → 02-aks-hands-on.ipynb → 03-cicd-automation.ipynb
   - Azure 구독 필요 (ACR, AKS 클러스터는 자동 생성)

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
- ArgoCD를 통한 GitOps 배포

> **참고**: GitHub Actions 워크플로우는 `.disabled` 확장자로 생성됩니다. 사용하려면 Secrets/Variables 설정 후 확장자를 제거하세요.

## 📁 프로젝트 구조

```
aks-mini-labs/
├── 01-container-basics.ipynb      # 컨테이너 기초 실습
├── 02-aks-hands-on.ipynb          # AKS 클러스터 실습
├── 03-cicd-automation.ipynb       # CI/CD 자동화 실습
├── config.py                      # 공통 환경 변수 설정
├── deployment.yaml                # Kubernetes 배포 템플릿
├── springboot-docker-demo/        # Spring Boot 샘플 앱
│   ├── Dockerfile                 # 멀티 스테이지 빌드 설정
│   ├── pom.xml                    # Maven 설정
│   └── src/                       # 소스 코드
├── .github/
│   └── workflows/                 # GitHub Actions (3번에서 생성, .disabled로 생성됨)
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
| `ACR_NAME` | ACR 이름 (생성 후 업데이트) | `None` → 타임스탬프로 자동 생성 | 01, 02, 03 |
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

**중요: ACR_NAME 업데이트**
- 01번 노트북 섹션 6.3에서 ACR 생성 후, `config.py` 파일의 `ACR_NAME` 값을 **실제 생성된 이름으로 수동 업데이트**하세요
- 이렇게 하면 02, 03번 노트북에서 동일한 ACR을 자동으로 사용할 수 있습니다

예시:
```python
# config.py 파일 수정
ACR_NAME = "myacr1760169422"  # 01번에서 생성된 실제 이름
```

## ⚠️ 주의사항

- **01번**: ACR 이름이 타임스탬프로 자동 생성됨 (예: myacr1760169422)
- **02번**: `deployment.yaml`은 노트북에서 자동 생성됨
- **03번**: 
  - GitHub Actions 워크플로우는 `.disabled` 상태로 생성됨
  - 활성화하려면 GitHub Secrets (`AZURE_CREDENTIALS`) 및 Variables (`ACR_NAME`) 설정 후 `.disabled` 확장자 제거
  - Azure DevOps Service Connection 설정 필요 (Azure Pipelines 사용 시)

## 🛠️ 문제 해결

**Pod Pending 상태**
- `kubectl describe pod <pod-name>`으로 원인 확인
- NAP가 활성화되어 있으면 자동으로 노드 추가

**리소스 그룹 변경**
- 1번 노트북의 `RESOURCE_GROUP` 변수 수정
- 이후 모든 노트북에서 동일한 이름 사용

**ACR 로그인 실패**
- Azure CLI 로그인 세션이 만료되었을 수 있음
- `az login` 명령으로 재로그인

**이미지 빌드 실패**
- Docker 데몬이 실행 중인지 확인: `docker ps`
- 디스크 공간 확인: `df -h`

## 🔗 참고 자료

### Azure 공식 문서
- [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/azure/aks/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/)

### Kubernetes
- [Kubernetes 공식 문서](https://kubernetes.io/docs/)
- [kubectl 치트시트](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

### Spring Boot & Docker
- [Spring Boot Docker 가이드](https://spring.io/guides/gs/spring-boot-docker)
- [Docker 공식 문서](https://docs.docker.com/)

## 💬 기여 및 피드백

이 프로젝트에 기여하고 싶으시다면:
1. Fork 후 새로운 브랜치 생성
2. 변경사항 커밋
3. Pull Request 제출

버그 리포트나 기능 제안은 [Issues](https://github.com/junwoojeong100/aks-mini-labs/issues) 탭을 이용해주세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

---

💡 **문의 및 피드백:** Issues 탭을 이용해주세요.

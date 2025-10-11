# AKS Mini Labs


이 프로젝트는 Azure Kubernetes Service(AKS), 컨테이너 기술, DevOps 자동화(CI/CD)를 실습할 수 있는 핸즈온 랩 가이드입니다. 각 단계별로 Azure 기능과 실습 흐름을 반영한 주피터 노트북 기반 실습을 제공합니다.

## 실습 환경

이 실습은 **GitHub Codespaces**를 기본 환경으로 구성되어 있습니다. 
- GitHub Codespaces를 사용하면 별도의 로컬 환경 설정 없이 브라우저에서 바로 실습을 시작할 수 있습니다.
- 저장소를 열고 "Code" > "Create codespace on main"을 선택하여 실습 환경을 시작하세요.
- Docker, Azure CLI, kubectl 등 필요한 도구들이 미리 설정되어 있습니다.

## 구성 파일

- **01-container-basics.ipynb**
  - 컨테이너의 기본 개념, 주요 이점, 아키텍처
  - FastAPI 예제 앱 작성 및 실행
  - Dockerfile 작성 및 이미지 빌드
  - 로컬 컨테이너 실행
  - Azure Container Registry(ACR) 로그인, 이미지 태깅 및 푸시
  - (참조) Spring Boot 기반 컨테이너 이미지 빌드 예시


- **02-aks-hands-on.ipynb**
  - 쿠버네티스 및 AKS의 기본 개념과 Azure 기능 소개
  - Azure CLI 기반 AKS 클러스터 생성 (Node Auto Provisioning/NAP 포함)
  - ACR 연동 및 컨테이너 이미지 배포
  - 애플리케이션 확장(HPA, Replica 조정) 및 오토스케일링 실습
  - 관리형 Prometheus/Grafana, Azure Monitor를 통한 모니터링
  - Node Auto Provisioning(NAP) 실습 및 동작 테스트


- **03-cicd-automation.ipynb**
  - CI/CD 개념 및 필요성
  - GitHub Actions를 활용한 컨테이너 이미지 빌드/테스트/ACR 푸시 자동화
  - Azure Pipelines를 활용한 빌드 및 AKS 배포 자동화

## 활용 방법

1. GitHub Codespaces에서 이 저장소를 열어 실습 환경을 시작합니다.
2. 각 노트북을 순서대로 실행하며 실습을 진행하세요.
3. Azure 구독, ACR, AKS 클러스터, GitHub 저장소, Azure DevOps 프로젝트가 필요합니다.
4. 실습 중 궁금한 점이나 오류가 발생하면 각 셀의 설명 또는 최신 Azure 공식 문서를 참고하세요.

## 목표

- 컨테이너와 쿠버네티스의 기본 원리 및 Azure 기능 이해
- Azure 환경에서 컨테이너 기반 애플리케이션 배포 및 운영 경험
- DevOps 자동화 파이프라인 구축 및 실습

---


이 가이드는 클라우드 네이티브 및 DevOps 실무 역량 향상을 위한 최신 실습 중심의 자료입니다.

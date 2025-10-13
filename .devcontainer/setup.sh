#!/bin/bash

echo "🚀 AKS Mini Labs Dev Container 초기 설정 시작..."

# Python 가상환경 생성
echo "📦 Python 가상환경 생성 중..."
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate

# pip 업그레이드
echo "⬆️  pip 업그레이드 중..."
pip install --upgrade pip

# requirements.txt가 있으면 패키지 설치, 없으면 기본 패키지 설치
if [ -f "requirements.txt" ]; then
    echo "📚 Python 패키지 설치 중 (requirements.txt)..."
    pip install -r requirements.txt
else
    echo "📚 기본 Python 패키지 설치 중..."
    pip install ipykernel jupyter notebook azure-cli-core azure-mgmt-containerregistry azure-mgmt-containerservice requests
fi

# Jupyter 커널 등록
echo "🔧 Jupyter 커널 등록 중..."
python -m ipykernel install --user --name=aks-mini-labs --display-name "Python (.venv)"

# Spring Boot 프로젝트 빌드 (Maven)
if [ -f "springboot-docker-demo/pom.xml" ]; then
    echo "☕ Spring Boot 프로젝트 빌드 중..."
    cd springboot-docker-demo
    mvn clean compile -q
    cd ..
    echo "✅ Maven 빌드 완료"
else
    echo "⚠️  springboot-docker-demo/pom.xml을 찾을 수 없습니다."
fi

# Docker 버전 확인
echo "🐳 Docker 버전 확인..."
docker --version

# kubectl 버전 확인
echo "☸️  kubectl 버전 확인..."
kubectl version --client=true 2>/dev/null || echo "kubectl 설치 완료"

# Azure CLI 로그인 안내
echo ""
echo "✅ Dev Container 설정 완료!"
echo ""
echo "📋 설치된 도구:"
echo "   🐍 Python 가상환경: .venv"
echo "   📓 Jupyter 커널: Python (.venv)"
echo "   ☕ Java 21 & Maven"
echo "   🐳 Docker"
echo "   ☸️  kubectl"
echo "   ☁️  Azure CLI"
echo ""
echo "💡 다음 단계:"
echo "   1. 노트북을 열고 커널을 'Python (.venv)'로 선택하세요"
echo "   2. Azure CLI 로그인:"
echo "      az login --use-device-code"
echo "   3. 01-container-basics.ipynb부터 순서대로 실습을 진행하세요"
echo ""
echo "📚 실습 순서:"
echo "   01-container-basics.ipynb  → 컨테이너 기초 & ACR"
echo "   02-aks-hands-on.ipynb      → AKS 클러스터 운영"
echo "   03-cicd-automation.ipynb   → CI/CD 자동화"
echo ""

"""
AKS Mini Labs - 공통 설정 파일

이 파일은 모든 노트북에서 공유하는 변수들을 정의합니다.
노트북에서 다음과 같이 사용하세요:

    from config import *

또는 특정 변수만 import:

    from config import RESOURCE_GROUP, AKS_CLUSTER_NAME
"""

# ============================================================================
# Azure 리소스 공통 설정
# ============================================================================

# 리소스 그룹 설정
RESOURCE_GROUP = "aks-mini-labs-rg"
LOCATION = "koreacentral"

# AKS 클러스터 설정
AKS_CLUSTER_NAME = "aks-mini-labs-cluster"
NODE_COUNT = 2

# ACR 설정 (01-container-basics.ipynb에서 생성)
# ⚠️ 중요: ACR_NAME은 01번 노트북 섹션 6.3에서 ACR 생성 후 반드시 업데이트하세요!
# 
# 📝 업데이트 방법:
#   1. 01번 노트북 섹션 6.3을 실행하여 ACR을 생성합니다
#   2. 출력된 ACR 이름을 복사합니다 (예: "myacr1760169422")
#   3. 아래 ACR_NAME 값을 실제 생성된 이름으로 변경합니다
#   4. 이 파일(config.py)을 저장합니다
#
# 💡 예시: ACR_NAME = "myacr1760169422"
# 
# ⚠️ None으로 두면 02, 03번 노트북에서 자동 조회를 시도하지만,
#    미리 설정해두는 것을 강력히 권장합니다!
ACR_NAME = None  # ← 이 값을 01번 노트북에서 생성한 실제 ACR 이름으로 변경하세요!

# ============================================================================
# 애플리케이션 설정
# ============================================================================

# 애플리케이션 이미지 설정
APP_NAME = "myapp"
IMAGE_TAG = "latest"

# Kubernetes Deployment 설정
DEPLOYMENT_NAME = "myapp"
SERVICE_NAME = "myapp"
REPLICAS = 2

# ============================================================================
# 모니터링 설정
# ============================================================================

# Azure Monitor 워크스페이스
MONITOR_WORKSPACE_NAME = f"{AKS_CLUSTER_NAME}-monitor"

# Grafana 설정
GRAFANA_NAME = "aks-mini-labs-grafana"

# ============================================================================
# HPA (Horizontal Pod Autoscaler) 설정
# ============================================================================

HPA_MIN_REPLICAS = 2
HPA_MAX_REPLICAS = 10
HPA_CPU_PERCENT = 50

# ============================================================================
# 헬퍼 함수
# ============================================================================

def get_acr_login_server(acr_name=None):
    """ACR 로그인 서버 주소를 반환합니다."""
    name = acr_name or ACR_NAME
    if name:
        return f"{name}.azurecr.io"
    print("⚠️  경고: ACR_NAME이 설정되지 않았습니다. config.py 파일을 업데이트하세요.")
    return None

def get_full_image_name(acr_name=None, app_name=None, tag=None):
    """전체 이미지 이름을 반환합니다."""
    name = acr_name or ACR_NAME
    app = app_name or APP_NAME
    image_tag = tag or IMAGE_TAG
    
    if name:
        return f"{name}.azurecr.io/{app}:{image_tag}"
    print("⚠️  경고: ACR_NAME이 설정되지 않았습니다. config.py 파일을 업데이트하세요.")
    return None

def print_config():
    """현재 설정된 변수들을 출력합니다."""
    print("=" * 80)
    print("📋 AKS Mini Labs - 현재 설정")
    print("=" * 80)
    print()
    print("🏢 Azure 리소스:")
    print(f"   리소스 그룹: {RESOURCE_GROUP}")
    print(f"   위치: {LOCATION}")
    print(f"   AKS 클러스터: {AKS_CLUSTER_NAME}")
    print(f"   노드 수: {NODE_COUNT}")
    print(f"   ACR 이름: {ACR_NAME or '(아직 생성되지 않음)'}")
    print()
    print("📦 애플리케이션:")
    print(f"   앱 이름: {APP_NAME}")
    print(f"   이미지 태그: {IMAGE_TAG}")
    print(f"   전체 이미지: {get_full_image_name() or '(ACR 생성 후 사용 가능)'}")
    print(f"   Replica 수: {REPLICAS}")
    print()
    print("📊 모니터링:")
    print(f"   Monitor 워크스페이스: {MONITOR_WORKSPACE_NAME}")
    print(f"   Grafana: {GRAFANA_NAME}")
    print()
    print("🎯 HPA 설정:")
    print(f"   최소 Replica: {HPA_MIN_REPLICAS}")
    print(f"   최대 Replica: {HPA_MAX_REPLICAS}")
    print(f"   CPU 임계값: {HPA_CPU_PERCENT}%")
    print()
    print("=" * 80)

# 모듈이 직접 실행될 때 설정 출력
if __name__ == "__main__":
    print_config()

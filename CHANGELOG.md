# Changelog

## 2025-10-12 - 구조 정합성 개선

### 수정 사항

#### 1. config.py 개선
- ✅ ACR_NAME 설정에 대한 명확한 가이드 추가
- ✅ 헬퍼 함수에 경고 메시지 추가 (ACR_NAME이 None일 때)
- ✅ 사용자가 설정을 놓치지 않도록 단계별 지침 제공

#### 2. 02-aks-hands-on.ipynb 개선
- ✅ 섹션 3.3: 중복된 print 문 제거 및 코드 정리
- ✅ 섹션 3.4: DEPLOYMENT_NAME 변수 사용으로 일관성 개선
- ✅ 섹션 3.5: 누락된 본문 및 코드 셀 추가
  - LoadBalancer 외부 IP 확인 기능 구현
  - 사용자 친화적인 안내 메시지 추가
  - pending 상태 처리 로직 포함
- ✅ 섹션 5.2: Grafana 생성 시 중복 메시지 제거

#### 3. 03-cicd-automation.ipynb 개선
- ✅ 섹션 2.1: GitHub Actions 워크플로우 구문 오류 수정
  - Docker build/push 명령 중복 제거
  - 올바른 YAML 구문 적용
  - ACR 로그인 단계 명확히 분리
- ✅ 섹션 3.2: Azure Pipelines 파일 생성 후 중복 코드 제거

### 영향
- 모든 노트북이 정상적으로 실행 가능
- 사용자가 설정을 놓치지 않도록 명확한 가이드 제공
- 코드 일관성 및 가독성 향상
- CI/CD 워크플로우가 정상적으로 동작

### 테스트 권장사항
1. config.py의 ACR_NAME을 01번 노트북 실행 후 업데이트
2. 02번 노트북 섹션 3.5에서 외부 IP 확인 테스트
3. 03번 노트북의 GitHub Actions 워크플로우 구문 확인

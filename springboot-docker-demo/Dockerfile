# 멀티 스테이지 빌드 - 빌드 단계
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -Dmaven.test.skip=true

# 멀티 스테이지 빌드 - 실행 단계
FROM eclipse-temurin:21-jre

# 비-루트 사용자 생성 (Debian 기반)
RUN groupadd -r spring && useradd -r -g spring spring
USER spring:spring

WORKDIR /app
COPY --from=build /app/target/*.jar app.jar

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]

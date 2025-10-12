package com.example.springbootdocker;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit test for Spring Boot App.
 */
@SpringBootTest
public class AppTest {
    
    @Test
    public void contextLoads() {
        // 스프링 컨텍스트가 정상적으로 로드되는지 확인
    }
    
    @Test
    public void testAppNotNull() {
        assertNotNull(new App());
    }
}

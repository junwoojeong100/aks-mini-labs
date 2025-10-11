package com.example.springbootdocker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class App {
    @GetMapping("/")
    public String home() {
        return "Hello Docker World from GitHub Codespaces!";
    }
    public static void main(String[] args) {
        SpringApplication.run(App.class, args);
    }
}
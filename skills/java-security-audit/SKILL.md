---
name: java-security-audit
description: Identify security vulnerabilities and apply secure coding practices in Java applications
---

# Java Security Audit Skill

## When to Use This Skill

- Reviewing code for OWASP Top 10 vulnerabilities
- Auditing Spring Security configurations
- Analyzing authentication and authorization flows
- Identifying cryptography misuse
- Checking for dependency vulnerabilities
- Validating input sanitization
- Assessing data exposure risks
- Preparing for security certifications (SOC2, ISO27001)

## Quick Start

```
/java-security-audit <component_or_configuration>
```

**Example**:
```
/java-security-audit AuthenticationController and its database layer
```

## How It Works

The skill performs comprehensive security analysis:

### 1. OWASP Top 10 Assessment
- **A1**: Broken Access Control (authorization checks)
- **A2**: Cryptographic Failures (encryption, hashing)
- **A3**: Injection (SQL, command, LDAP injection)
- **A4**: Insecure Design (threat modeling, design flaws)
- **A5**: Security Misconfiguration (defaults, exposure)
- **A6**: Vulnerable Components (dependencies, libraries)
- **A7**: Authentication Failures (session, password management)
- **A8**: Data Integrity Failures (deserialization, XML)
- **A9**: Logging & Monitoring Failures (audit trails)
- **A10**: SSRF (server-side request forgery)

### 2. Spring Security Review
- **Authentication**: OAuth2, JWT, session management
- **Authorization**: Role-based, permission-based access control
- **CORS**: Cross-origin request handling
- **CSRF**: Cross-site request forgery protection
- **Security Headers**: CSP, X-Frame-Options, etc.

### 3. Credential Management
- **Secret Storage**: No hardcoded credentials
- **Environment Variables**: Proper use of .env files
- **Secret Managers**: AWS Secrets Manager, HashiCorp Vault
- **Key Rotation**: Regular key rotation procedures

### 4. Cryptography Validation
- **Algorithm Selection**: Modern algorithms (AES-256, HMAC-SHA256)
- **Random Generation**: Use SecureRandom, not Random
- **Key Size**: Minimum 256-bit keys for symmetric encryption
- **Initialization Vectors**: Unique IVs for each encryption
- **Password Hashing**: bcrypt, scrypt, Argon2, not MD5/SHA1

### 5. Input Validation
- **Whitelist Validation**: Accept known-good input
- **Type Checking**: Validate data types
- **Range Checking**: Validate numeric ranges
- **Format Validation**: Regex patterns for format
- **Sanitization**: Remove dangerous characters

### 6. Dependency Analysis
- **Vulnerability Scanning**: Check for known CVEs
- **Supply Chain**: Verify package sources
- **Version Management**: Keep dependencies updated
- **Exclusions**: Exclude vulnerable transitive dependencies

## Configuration

**Maven Security Scanning Plugin**:
```xml
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>7.4.4</version>
    <configuration>
        <failBuildOnCVSS>7</failBuildOnCVSS>
    </configuration>
</plugin>
```

**Spring Security Configuration**:
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf().csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
            .and()
            .authorizeRequests()
                .antMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .oauth2Login();
        return http.build();
    }
}
```

## Examples

### Example 1: SQL Injection Vulnerability

```java
// ❌ VULNERABILITY: SQL Injection
@Repository
public class UserRepository {
    @Autowired
    private JdbcTemplate jdbcTemplate;

    public User findByEmail(String email) {
        String sql = "SELECT * FROM users WHERE email = '" + email + "'";
        return jdbcTemplate.queryForObject(sql, new UserRowMapper());
        // If email = "' OR '1'='1", SQL becomes: SELECT * FROM users WHERE email = '' OR '1'='1'
    }
}

// ✅ FIXED: Parameterized Query
@Repository
public class UserRepository extends JpaRepository<User, Long> {
    @Query("SELECT u FROM User u WHERE u.email = :email")
    User findByEmail(@Param("email") String email);

    // OR using JdbcTemplate properly:
    public User findByEmail(String email) {
        String sql = "SELECT * FROM users WHERE email = ?";
        return jdbcTemplate.queryForObject(sql, new Object[]{email}, new UserRowMapper());
    }
}
```

### Example 2: Hardcoded Credentials

```java
// ❌ VULNERABILITY: Hardcoded database credentials
@Configuration
public class DatabaseConfig {
    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setUrl("jdbc:mysql://localhost:3306/mydb");
        ds.setUsername("root");
        ds.setPassword("superSecret123");  // EXPOSED!
        return ds;
    }
}

// ✅ FIXED: Use environment variables
@Configuration
public class DatabaseConfig {
    @Value("${spring.datasource.url}")
    private String url;

    @Value("${spring.datasource.username}")
    private String username;

    @Value("${spring.datasource.password}")
    private String password;

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setUrl(url);
        ds.setUsername(username);
        ds.setPassword(password);
        return ds;
    }
}

// In application.properties (or external secret manager):
# spring.datasource.url=jdbc:mysql://localhost:3306/mydb
# spring.datasource.username=${DB_USER}
# spring.datasource.password=${DB_PASSWORD}
```

### Example 3: Weak Password Hashing

```java
// ❌ VULNERABILITY: Using MD5 or SHA1
public class UserService {
    public void createUser(String email, String password) {
        String hashedPassword = DigestUtils.md5Hex(password);  // WEAK!
        userRepository.save(new User(email, hashedPassword));
    }
}

// ✅ FIXED: Use bcrypt
@Service
public class UserService {
    @Autowired
    private PasswordEncoder passwordEncoder;

    public void createUser(String email, String password) {
        String hashedPassword = passwordEncoder.encode(password);  // bcrypt with salt
        userRepository.save(new User(email, hashedPassword));
    }
}

// In SecurityConfig:
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder(12);  // strength: 12 rounds
}
```

### Example 4: Insecure Random Generation

```java
// ❌ VULNERABILITY: Using java.util.Random for security
public String generateVerificationToken() {
    Random random = new Random();
    return Integer.toString(random.nextInt(999999));  // Predictable!
}

// ✅ FIXED: Use SecureRandom
public String generateVerificationToken() {
    SecureRandom random = new SecureRandom();
    byte[] bytes = new byte[32];
    random.nextBytes(bytes);
    return Base64.getEncoder().encodeToString(bytes);
}

// ✅ BEST: Use Apache Commons Lang
public String generateVerificationToken() {
    return RandomStringUtils.randomAlphanumeric(32);  // Thread-safe
}
```

### Example 5: Missing Authorization Check

```java
// ❌ VULNERABILITY: No authorization check
@RestController
@RequestMapping("/api/users")
public class UserController {
    @GetMapping("/{userId}/profile")
    public UserDTO getUserProfile(@PathVariable Long userId) {
        return userService.getUserProfile(userId);  // Any authenticated user can access
    }
}

// ✅ FIXED: Add authorization check
@RestController
@RequestMapping("/api/users")
public class UserController {
    @GetMapping("/{userId}/profile")
    @PreAuthorize("#userId == authentication.principal.id or hasRole('ADMIN')")
    public UserDTO getUserProfile(@PathVariable Long userId) {
        return userService.getUserProfile(userId);  // Only user or admin can access
    }
}

// OR in service:
@Service
public class UserService {
    public UserDTO getUserProfile(Long userId, User currentUser) {
        if (!userId.equals(currentUser.getId()) && !currentUser.hasRole("ADMIN")) {
            throw new AccessDeniedException("Not authorized");
        }
        return getUserProfileInternal(userId);
    }
}
```

### Example 6: Insufficient Input Validation

```java
// ❌ VULNERABILITY: No input validation
@PostMapping("/register")
public User registerUser(@RequestBody UserRegistrationRequest request) {
    return userService.register(request.getEmail(), request.getPassword());
}

// ✅ FIXED: Validate input
@PostMapping("/register")
public User registerUser(@Valid @RequestBody UserRegistrationRequest request) {
    return userService.register(request.getEmail(), request.getPassword());
}

// In UserRegistrationRequest:
@Data
public class UserRegistrationRequest {
    @Email(message = "Email must be valid")
    @NotBlank(message = "Email is required")
    private String email;

    @Pattern(regexp = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).{8,}$",
        message = "Password must have uppercase, lowercase, number, 8+ chars")
    private String password;
}
```

## Best Practices

### 1. Principle of Least Privilege
```java
// Give users minimum permissions needed
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/admin/**").hasRole("ADMIN")
            .antMatchers("/user/**").hasRole("USER")
            .antMatchers("/public/**").permitAll()
            .anyRequest().denyAll();  // Deny by default
        return http.build();
    }
}
```

### 2. Defense in Depth
- Multiple layers of security (authentication, authorization, encryption, logging)
- Not relying on a single control
- Compensating controls for weaknesses

### 3. Security Headers
```java
@Configuration
public class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.headers()
            .contentSecurityPolicy("default-src 'self'")
            .and()
            .frameOptions().deny()
            .and()
            .xssProtection();
        return http.build();
    }
}
```

## Integration with Other Skills

- **`java-code-review`**: Security review during code review process
- **`java-testing-strategy`**: Security test cases and penetration testing
- **`spring-boot-setup`**: Secure default configurations
- **`cicd-pipeline-setup`**: Security scanning in CI/CD

## Security Checklist

- [ ] No hardcoded credentials or secrets
- [ ] SQL injection protection (parameterized queries)
- [ ] XSS protection (output encoding)
- [ ] CSRF protection enabled
- [ ] Authentication mechanism implemented
- [ ] Authorization checks in place
- [ ] Passwords hashed with bcrypt/scrypt/Argon2
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Dependency vulnerabilities scanned
- [ ] Audit logging implemented
- [ ] Error messages don't leak sensitive info

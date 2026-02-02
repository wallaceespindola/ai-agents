# Spring Boot Security Advanced Skill

**Master OAuth2, OpenID Connect, JWT, RBAC, API security, rate limiting, CORS/CSRF protection.**

## Overview

Enterprise security requires sophisticated authentication and authorization patterns. This skill covers advanced Spring Security patterns.

**What it does:**
- Implements OAuth2 authorization flows
- Configures OpenID Connect authentication
- Manages JWT tokens and claims
- Implements role-based access control (RBAC)
- Secures REST APIs
- Implements rate limiting
- Handles CORS and CSRF protection
- Manages API key authentication

**Perfect for:**
- Enterprise authentication
- Multi-tenant systems
- API security
- Social login integration
- OAuth2 provider implementation

---

## When to Use This Skill

Use Spring Boot Security Advanced when you need to:

- **Implement OAuth2 flows** (authorization code, implicit, client credentials)
- **Integrate OpenID Connect** for user information
- **Manage JWT tokens** with claims and expiry
- **Implement RBAC** for role-based access
- **Secure APIs** with authentication/authorization
- **Implement rate limiting** per user/IP
- **Handle CORS/CSRF** protection
- **Support multiple authentication** methods

---

## Quick Start (15 Minutes)

### 1. OAuth2 Resource Server

Add dependency:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

Configure:

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: https://auth.example.com
          jwk-set-uri: https://auth.example.com/.well-known/jwks.json
```

### 2. JWT Configuration

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
      .authorizeRequests()
        .antMatchers("/public/**").permitAll()
        .antMatchers("/api/**").authenticated()
        .anyRequest().authenticated()
      .and()
      .oauth2ResourceServer()
        .jwt();

    return http.build();
  }
}
```

### 3. RBAC Implementation

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

  @GetMapping
  @PreAuthorize("hasRole('ADMIN')")
  public List<User> getAllUsers() {
    return userService.getAll();
  }

  @PostMapping
  @PreAuthorize("hasRole('ADMIN')")
  public User createUser(@RequestBody User user) {
    return userService.save(user);
  }

  @GetMapping("/{id}")
  @PreAuthorize("hasRole('USER')")
  public User getUser(@PathVariable String id) {
    return userService.getById(id);
  }
}
```

### 4. Custom Authorization

```java
@Service
public class CustomAuthorizationService {

  @PreAuthorize("@authService.canAccess(#resource)")
  public Resource getResource(String resource) {
    return resourceRepository.findById(resource).orElseThrow();
  }

  public boolean canAccess(String resource) {
    Authentication auth = SecurityContextHolder.getContext().getAuthentication();
    // Custom logic to check access
    return true;
  }
}
```

---

## How It Works

### 1. OAuth2 Authorization Flows

**Authorization Code Flow (Web Applications):**

```
1. User → /login → OAuth provider
2. User logs in and grants permission
3. OAuth provider → /callback?code=XXX → Application
4. Application exchanges code for token
5. Application stores token and creates session
```

**Client Credentials Flow (Service-to-Service):**

```
Service A → [client_id, client_secret] → OAuth Provider
OAuth Provider returns access token
Service A → [access_token] → Service B
Service B validates token and grants access
```

**Password Grant (Legacy):**

```
Application → [username, password, client_id] → OAuth Provider
OAuth Provider validates credentials, returns token
```

### 2. JWT Token Management

**JWT Structure:**

```
header.payload.signature

Header: {
  "typ": "JWT",
  "alg": "RS256"
}

Payload: {
  "sub": "user-123",
  "name": "John Doe",
  "roles": ["ADMIN", "USER"],
  "iat": 1234567890,
  "exp": 1234571490
}

Signature: Base64(HMAC(header.payload, secret))
```

**Extract Claims:**

```java
@RestController
public class ProfileController {

  @GetMapping("/me")
  public UserProfile getCurrentUser(
    @AuthenticationPrincipal JwtAuthenticationToken token) {

    String subject = token.getToken().getSubject();
    Map<String, Object> claims = token.getToken().getClaims();
    List<String> roles = (List<String>) claims.get("roles");

    return new UserProfile(subject, roles);
  }
}
```

### 3. RBAC (Role-Based Access Control)

**Configure Roles:**

```java
@Configuration
@EnableGlobalMethodSecurity(
  securedEnabled = true,
  prePostEnabled = true,
  jsr250Enabled = true
)
public class SecurityConfig {

  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
      .authorizeRequests()
        .antMatchers("/admin/**").hasRole("ADMIN")
        .antMatchers("/user/**").hasRole("USER")
        .antMatchers("/api/**").hasAnyRole("USER", "ADMIN")
        .anyRequest().authenticated()
      .and()
      .oauth2ResourceServer()
        .jwt();

    return http.build();
  }
}
```

**Use in Controllers:**

```java
@RestController
@RequestMapping("/api")
public class ApiController {

  @GetMapping("/public")
  public void publicEndpoint() {
    // No authentication required
  }

  @GetMapping("/user")
  @PreAuthorize("hasRole('USER')")
  public void userEndpoint() {
    // Requires USER role
  }

  @GetMapping("/admin")
  @PreAuthorize("hasRole('ADMIN')")
  public void adminEndpoint() {
    // Requires ADMIN role
  }

  @PostMapping("/data")
  @PreAuthorize("hasAnyRole('ADMIN', 'EDITOR')")
  public void editData() {
    // Requires ADMIN or EDITOR role
  }
}
```

### 4. CORS and CSRF Protection

**CORS Configuration:**

```java
@Configuration
public class CorsConfig {

  @Bean
  public WebMvcConfigurer corsConfigurer() {
    return new WebMvcConfigurer() {
      @Override
      public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
          .allowedOrigins("https://example.com", "https://app.example.com")
          .allowedMethods("GET", "POST", "PUT", "DELETE")
          .allowedHeaders("*")
          .allowCredentials(true)
          .maxAge(3600);
      }
    };
  }
}
```

**CSRF Protection:**

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
      .csrf()
        .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
      .and()
      .authorizeRequests()
        .anyRequest().authenticated();

    return http.build();
  }
}
```

### 5. Rate Limiting

**Implementation:**

```java
@Component
public class RateLimitingFilter extends OncePerRequestFilter {

  @Autowired
  private RateLimitService rateLimitService;

  @Override
  protected void doFilterInternal(
    HttpServletRequest request,
    HttpServletResponse response,
    FilterChain filterChain) throws ServletException, IOException {

    String userId = SecurityContextHolder.getContext()
      .getAuthentication().getPrincipal().toString();

    if (!rateLimitService.allowRequest(userId)) {
      response.setStatus(429); // Too Many Requests
      response.getWriter().write("Rate limit exceeded");
      return;
    }

    filterChain.doFilter(request, response);
  }
}

@Service
public class RateLimitService {

  @Autowired
  private RedisTemplate<String, Long> redis;

  public boolean allowRequest(String userId) {
    String key = "rate-limit:" + userId;
    Long count = redis.opsForValue().increment(key);

    if (count == 1) {
      redis.expire(key, Duration.ofMinutes(1));
    }

    return count <= 100; // 100 requests per minute
  }
}
```

### 6. API Key Authentication

```java
@Component
public class ApiKeyAuthenticationFilter extends OncePerRequestFilter {

  @Override
  protected void doFilterInternal(
    HttpServletRequest request,
    HttpServletResponse response,
    FilterChain filterChain) throws ServletException, IOException {

    String apiKey = request.getHeader("X-API-Key");

    if (apiKey != null && validateApiKey(apiKey)) {
      UserDetails userDetails = loadUserByApiKey(apiKey);
      AbstractAuthenticationToken auth =
        new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
      SecurityContextHolder.getContext().setAuthentication(auth);
    }

    filterChain.doFilter(request, response);
  }

  private boolean validateApiKey(String apiKey) {
    // Validate against database or cache
    return true;
  }

  private UserDetails loadUserByApiKey(String apiKey) {
    // Load user by API key
    return new User("api-user", "", new ArrayList<>());
  }
}
```

---

## Configuration

### Complete Security Configuration

```java
@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(
  securedEnabled = true,
  prePostEnabled = true
)
public class SecurityConfig {

  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
      // OAuth2 Resource Server
      .oauth2ResourceServer()
        .jwt()
          .jwtAuthenticationConverter(jwtAuthenticationConverter())
      .and()
      .and()
      // CORS
      .cors()
      .and()
      // CSRF
      .csrf()
        .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
      .and()
      // Authorization
      .authorizeRequests()
        .antMatchers("/public/**", "/health").permitAll()
        .antMatchers("/admin/**").hasRole("ADMIN")
        .antMatchers("/api/**").authenticated()
        .anyRequest().authenticated()
      .and()
      // Headers
      .headers()
        .contentSecurityPolicy("default-src 'self'")
      .and()
      .frameOptions().deny();

    return http.build();
  }

  @Bean
  public JwtAuthenticationConverter jwtAuthenticationConverter() {
    JwtAuthenticationConverter converter = new JwtAuthenticationConverter();

    JwtGrantedAuthoritiesConverter authoritiesConverter = new JwtGrantedAuthoritiesConverter();
    authoritiesConverter.setAuthoritiesClaimName("roles");
    authoritiesConverter.setAuthorityPrefix("ROLE_");

    converter.setJwtGrantedAuthoritiesConverter(authoritiesConverter);
    return converter;
  }

  @Bean
  public WebMvcConfigurer corsConfigurer() {
    return new WebMvcConfigurer() {
      @Override
      public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
          .allowedOrigins("https://example.com")
          .allowedMethods("*")
          .allowedHeaders("*")
          .allowCredentials(true)
          .maxAge(3600);
      }
    };
  }
}
```

---

## Examples

### Example 1: Protected REST API

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

  @Autowired
  private UserService userService;

  @GetMapping
  @PreAuthorize("hasRole('ADMIN')")
  public List<User> listUsers() {
    return userService.getAll();
  }

  @GetMapping("/{id}")
  @PreAuthorize("@userService.isOwner(#id)")
  public User getUser(@PathVariable String id) {
    return userService.getById(id);
  }

  @PostMapping
  @PreAuthorize("hasRole('ADMIN')")
  public User createUser(@RequestBody @Valid CreateUserRequest request) {
    return userService.create(request);
  }

  @PutMapping("/{id}")
  @PreAuthorize("@userService.isOwner(#id) or hasRole('ADMIN')")
  public User updateUser(@PathVariable String id, @RequestBody UpdateUserRequest request) {
    return userService.update(id, request);
  }

  @DeleteMapping("/{id}")
  @PreAuthorize("hasRole('ADMIN')")
  public void deleteUser(@PathVariable String id) {
    userService.delete(id);
  }
}

@Service
public class UserService {

  public boolean isOwner(String userId) {
    Authentication auth = SecurityContextHolder.getContext().getAuthentication();
    JwtAuthenticationToken token = (JwtAuthenticationToken) auth;
    String currentUser = token.getToken().getSubject();
    return currentUser.equals(userId);
  }
}
```

### Example 2: Custom Authorization

```java
@Component
public class ResourceAuthorizationService {

  @PreAuthorize("@resourceAuth.canAccess(#resourceId)")
  public Resource getResource(String resourceId) {
    return resourceRepository.findById(resourceId).orElseThrow();
  }

  public boolean canAccess(String resourceId) {
    Authentication auth = SecurityContextHolder.getContext().getAuthentication();
    String userId = auth.getPrincipal().toString();

    Resource resource = resourceRepository.findById(resourceId).orElse(null);
    return resource != null && resource.isAccessibleBy(userId);
  }
}
```

### Example 3: OAuth2 Client

```yaml
spring:
  security:
    oauth2:
      client:
        registration:
          github:
            client-id: ${GITHUB_CLIENT_ID}
            client-secret: ${GITHUB_CLIENT_SECRET}
            redirect-uri: "{baseUrl}/login/oauth2/code/{registrationId}"
          google:
            client-id: ${GOOGLE_CLIENT_ID}
            client-secret: ${GOOGLE_CLIENT_SECRET}
        provider:
          github:
            authorization-uri: https://github.com/login/oauth/authorize
            token-uri: https://github.com/login/oauth/access_token
            user-info-uri: https://api.github.com/user
```

---

## Best Practices

### 1. Always Use HTTPS

```yaml
server:
  ssl:
    key-store: classpath:keystore.p12
    key-store-password: ${KEYSTORE_PASSWORD}
    key-store-type: PKCS12
```

### 2. Implement Token Refresh

```java
@RestController
@RequestMapping("/auth")
public class AuthController {

  @PostMapping("/refresh")
  public ResponseEntity<?> refresh(
    @RequestBody RefreshTokenRequest request) {

    String newAccessToken = authService.refreshToken(request.getRefreshToken());
    return ResponseEntity.ok(new TokenResponse(newAccessToken));
  }
}
```

### 3. Log Security Events

```java
@Component
public class SecurityAuditListener {

  @EventListener
  public void onAuthSuccess(AuthenticationSuccessEvent event) {
    LOG.info("User {} logged in", event.getAuthentication().getName());
  }

  @EventListener
  public void onAuthFailure(AuthenticationFailureBadCredentialsEvent event) {
    LOG.warn("Failed login attempt for {}", event.getAuthentication().getName());
  }
}
```

### 4. Validate JWT Claims

```java
@Component
public class JwtValidator {

  public void validateToken(String token) {
    JwtDecoder decoder = NimbusJwtDecoder.withPublicKey(publicKey).build();
    Jwt jwt = decoder.decode(token);

    // Validate expiry
    if (jwt.getExpiresAt().isBefore(Instant.now())) {
      throw new JwtException("Token expired");
    }

    // Validate issuer
    String issuer = (String) jwt.getClaims().get("iss");
    if (!issuer.equals("https://auth.example.com")) {
      throw new JwtException("Invalid issuer");
    }
  }
}
```

---

## Integration with Other Skills

Spring Boot Security Advanced integrates with:

- **secrets-management** - Store OAuth credentials
- **spring-boot-microservices** - Service-to-service security
- **github-security-scanning** - Detect security issues
- **docker-compose-setup** - Secure container communication

---

*Last Updated: 2026-02-02*
*Part of: AI Agents & Skills Repository*

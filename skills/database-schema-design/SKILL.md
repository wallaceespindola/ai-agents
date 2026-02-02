---
name: database-schema-design
description: Design optimal database schemas for performance, consistency, and scalability
---

# Database Schema Design Skill

## When to Use This Skill

- Designing initial database schemas
- Optimizing existing database designs
- Planning database growth and scaling
- Normalizing and denormalizing data
- Implementing indexing strategies
- Designing for consistency and reliability
- Planning for high availability and disaster recovery

## Quick Start

```
/database-schema-design <data_model_or_domain>
```

**Example**:
```
/database-schema-design E-commerce platform with products, orders, and inventory
```

## How It Works

### Normalization Strategy

#### First Normal Form (1NF)
- Eliminate repeating groups
- Each field contains atomic values

```sql
-- ❌ NOT 1NF: Tags are repeating group
CREATE TABLE products_bad (
  id INT,
  name VARCHAR(255),
  tags VARCHAR(500)  -- "electronics,gadget,phone"
);

-- ✅ 1NF: Separate table for tags
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE product_tags (
  product_id INT REFERENCES products(id),
  tag VARCHAR(100),
  PRIMARY KEY (product_id, tag)
);
```

#### Second Normal Form (2NF)
- Meet 1NF requirements
- Remove partial dependencies

#### Third Normal Form (3NF)
- Meet 2NF requirements
- Remove transitive dependencies

```sql
-- ❌ NOT 3NF: Order contains customer_name (dependent on customer_id)
CREATE TABLE orders_bad (
  id INT PRIMARY KEY,
  customer_id INT,
  customer_name VARCHAR(255),  -- Depends on customer_id
  order_date DATE
);

-- ✅ 3NF: Separate customer info
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT REFERENCES customers(id),
  order_date DATE
);
```

### Indexing Strategy

```sql
-- Primary Key (automatic index)
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP
);

-- Single column index for frequent queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Composite index for multi-column queries
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

-- Partial index for filtered queries
CREATE INDEX idx_active_users ON users(id) WHERE is_active = true;

-- Full-text index for search
CREATE FULLTEXT INDEX idx_products_search ON products(name, description);

-- Index best practices:
-- - Index columns used in WHERE, JOIN, ORDER BY, GROUP BY
-- - Composite indexes: most selective column first
-- - Too many indexes slows INSERT/UPDATE
-- - Monitor index usage: unused indexes slow down mutations
```

### Example: Complete Schema Design

```sql
-- Users table
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(100) UNIQUE NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  avatar_url VARCHAR(500),
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

  INDEX idx_email (email),
  INDEX idx_username (username),
  INDEX idx_created_at (created_at)
);

-- Products table
CREATE TABLE products (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  sku VARCHAR(50) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT DEFAULT 0,
  category_id BIGINT NOT NULL,
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (category_id) REFERENCES categories(id),
  INDEX idx_sku (sku),
  INDEX idx_category_id (category_id),
  INDEX idx_is_active (is_active)
);

-- Orders table
CREATE TABLE orders (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  order_number VARCHAR(50) UNIQUE NOT NULL,
  user_id BIGINT NOT NULL,
  total_amount DECIMAL(12, 2) NOT NULL,
  status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  shipped_at TIMESTAMP NULL,
  delivered_at TIMESTAMP NULL,

  FOREIGN KEY (user_id) REFERENCES users(id),
  INDEX idx_user_id (user_id),
  INDEX idx_status (status),
  INDEX idx_created_at (created_at),
  UNIQUE KEY idx_order_number (order_number)
);

-- Order Items (junction table for products)
CREATE TABLE order_items (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  order_id BIGINT NOT NULL,
  product_id BIGINT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,

  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id),
  INDEX idx_order_id (order_id),
  INDEX idx_product_id (product_id)
);

-- Reviews table
CREATE TABLE reviews (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  product_id BIGINT NOT NULL,
  user_id BIGINT NOT NULL,
  rating TINYINT CHECK (rating >= 1 AND rating <= 5),
  title VARCHAR(255),
  content TEXT,
  is_verified_purchase BOOLEAN DEFAULT false,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  UNIQUE KEY idx_product_user (product_id, user_id),
  INDEX idx_product_rating (product_id, rating),
  INDEX idx_created_at (created_at)
);
```

### Denormalization for Performance

```sql
-- Denormalized: Store aggregated data to avoid expensive queries
CREATE TABLE product_stats (
  product_id BIGINT PRIMARY KEY REFERENCES products(id),
  total_reviews INT DEFAULT 0,
  average_rating DECIMAL(3, 2) DEFAULT 0,
  last_review_date TIMESTAMP NULL,

  INDEX idx_average_rating (average_rating)
);

-- Update stats when review added (trigger)
CREATE TRIGGER update_product_stats_on_review_insert
AFTER INSERT ON reviews
FOR EACH ROW
BEGIN
  UPDATE product_stats
  SET total_reviews = total_reviews + 1,
      average_rating = (SELECT AVG(rating) FROM reviews WHERE product_id = NEW.product_id),
      last_review_date = NOW()
  WHERE product_id = NEW.product_id;
END;
```

## Best Practices

1. **Normalization**: 3NF is usually ideal (balance between flexibility and performance)
2. **Primary Keys**: Always use surrogate keys (INT, BIGINT, UUID)
3. **Foreign Keys**: Maintain referential integrity
4. **Indexes**: Index strategically, monitor unused indexes
5. **Data Types**: Use appropriate types (DECIMAL for money, not FLOAT)
6. **Constraints**: Use CHECK, NOT NULL, UNIQUE constraints
7. **Partitioning**: Large tables (>1B rows) benefit from partitioning
8. **Backups**: Regular backups and disaster recovery planning

## Integration with Other Skills

- **`scalability-analysis`**: Database scaling strategy
- **`system-design-doc`**: Schema documentation
- **`cicd-pipeline-setup`**: Database migration automation
- **`monitoring-setup`**: Query performance monitoring


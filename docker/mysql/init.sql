CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    );

INSERT INTO user (name, password) VALUES
    ('John Doe', 'password123'),
    ('Jane Smith', 'securepassword'),
    ('Bob Johnson', 'mypassword');
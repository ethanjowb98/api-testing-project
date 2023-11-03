from dataclasses import dataclass

@dataclass
class AdminCredentials:
    USERNAME = "admin"
    PASSWORD = "password123"
    INVALID_USERNAME = "test"
    INVALID_PASSWORD = "password"

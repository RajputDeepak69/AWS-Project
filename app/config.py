import os

class Config:

    DB_HOST = os.getenv("DB_HOST", "10.0.2.6")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "infra_admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "infratrack")
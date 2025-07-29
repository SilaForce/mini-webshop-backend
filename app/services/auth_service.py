from typing import Optional
import jwt
from datetime import datetime, timedelta

class AuthService:
    def __init__(self):
        self.secret_key = "your-secret-key-change-in-production"
        self.admin_users = {"admin": "admin123"}  # Simple in-memory storage
    
    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        if username in self.admin_users and self.admin_users[username] == password:
            # Create JWT token
            payload = {
                "username": username,
                "exp": datetime.utcnow() + timedelta(hours=24)
            }
            token = jwt.encode(payload, self.secret_key, algorithm="HS256")
            return token
        return None
    
    def get_current_user(self, token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return {"username": payload["username"]}
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def verify_admin_token(self, token: str) -> bool:
        user = self.get_current_user(token)
        return user is not None
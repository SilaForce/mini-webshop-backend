from typing import Optional
import jwt
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import settings

class AuthService:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.admin_users = {
            settings.DEFAULT_ADMIN_USERNAME: settings.DEFAULT_ADMIN_PASSWORD
        }
    
    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        if username in self.admin_users and self.admin_users[username] == password:
            # Create JWT token
            payload = {
                "username": username,
                "exp": datetime.utcnow() + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
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
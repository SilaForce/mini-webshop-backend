import uvicorn
from config import settings
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", settings.API_PORT))
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  
        port=port,
        reload=False,  
        log_level="info"
    )
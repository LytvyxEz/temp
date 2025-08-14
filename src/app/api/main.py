from fastapi import FastAPI
from routers import router

app = FastAPI()

print("API is running...")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
    

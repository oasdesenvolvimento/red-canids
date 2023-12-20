import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import router
import database

database.connection_database.connect_database()

app = FastAPI(
    title="API RED CANIDS",
    description="API for integration with RED CANIDS",
    version="1.0.1",
    docs_url="/red-canids-api-swagger",
    redoc_url="/red-canids-api-docs",
    servers=[
        {
            "url": "http://0.0.0.0:8000",
            "description": "Local server",
        },
        {
            "url": "https://red-canids-api.azurewebsites.net",
            "description": "Staging server",
        }
    ]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router.mission_router.router, prefix="/mission", tags=["mission"])
app.include_router(router.image_router.router, prefix="/image", tags=["image"])

if __name__ == "__main__":
    """

    Run server
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)

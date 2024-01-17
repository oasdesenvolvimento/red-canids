import router
import uvicorn
import database

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

database.connection_database.connect_database()

app = FastAPI(
    title="API RED CANIDS",
    description="API for integration with RED CANIDS",
    version="1.0.17",
    docs_url="/red-canids-api-swagger",
    redoc_url="/red-canids-api-docs",
    #root_path="https://red-canids-api.azurewebsites.net/",
    servers=[
        {
            "url": "https://red-canids-api.azurewebsites.net/",
            "description": "Staging server",
        },
        {
            "url": "http://0.0.0.0:8000/",
            "description": "Local server",
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
app.include_router(router.account_router.router, prefix="/account", tags=["account"])
app.include_router(router.admin_router.router, prefix="/admin", tags=["admin"])

if __name__ == "__main__":
    """

    Run server
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)

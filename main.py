# # main.py

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from routers.research_router import router


# # app = FastAPI(
# #     title="Multi Agent Research System",
# #     description="""
# #     AI-powered research and comparison platform
# #     using CrewAI + Tavily + Multi-format loaders.
# #     """,
# #     version="1.0.0"
# # )
# from fastapi import FastAPI

# app = FastAPI(
#     title="Multi Agent Research System",
#     description="""
#     AI-powered research and comparison platform
#     using CrewAI + Tavily + Multi-format loaders.
#     """,
#     version="1.0.0",
#     openapi_version="3.0.3",
# )


# # =========================================================
# # CORS
# # =========================================================

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # =========================================================
# # Include Routers
# # =========================================================

# app.include_router(router)


# # =========================================================
# # Health Check
# # =========================================================

# @app.get("/")
# async def health_check():

#     return {
#         "status": "running",
#         "message": "Research API is live"
#     }

import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from routers.research_router import router

app = FastAPI(
    title="Multi Agent Research System",
    description="""
    AI-powered research and comparison platform
    using CrewAI + Tavily + Multi-format loaders.
    """,
    version="1.0.0",
    openapi_version="3.0.3",
)

# =========================================================
# Robust OpenAPI Patch for Swagger UI Native File Picker
# =========================================================
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    # 1. Generate the standard base schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
        openapi_version=app.openapi_version
    )
    
    # 2. Dump the schema to a raw string
    schema_str = json.dumps(openapi_schema)
    
    # 3. Clean up the array item format schemas globally
    # This transforms '{"contentMediaType": "application/octet-stream"}' directly to '{"format": "binary"}'
    schema_str = schema_str.replace(
        '"contentMediaType": "application/octet-stream"', 
        '"format": "binary"'
    )
    
    # 4. Load it back into a valid dictionary structure
    app.openapi_schema = json.loads(schema_str)
    return app.openapi_schema

# Assign the custom patched schema generator
app.openapi = custom_openapi


# =========================================================
# CORS
# =========================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# Include Routers
# =========================================================
app.include_router(router)


# =========================================================
# Health Check
# =========================================================
@app.get("/")
async def health_check():
    return {
        "status": "running",
        "message": "Research API is live"
    }
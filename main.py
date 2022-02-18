from typing import Optional

from fastapi import FastAPI

from routes import RegisterRoutes

app = FastAPI()

# Register blueprints
RegisterRoutes(app).register_routes()

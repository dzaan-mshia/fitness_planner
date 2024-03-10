from fastapi import FastAPI

from controllers import planner_controller, authorization_controller

app = FastAPI(openapi_url="/api/openapi.json")

app.include_router(planner_controller.router, prefix="/workout-plan")
app.include_router(authorization_controller.router, prefix="/auth")

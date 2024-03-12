import uvicorn
from fastapi import FastAPI

import db.conf.db_configuration
from controllers import planner_controller, authorization_controller

app = FastAPI(openapi_url="/api/openapi.json")

app.include_router(planner_controller.router, prefix="/workout-plan")
app.include_router(authorization_controller.router, prefix="/auth")

db.conf.db_configuration.init_db()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

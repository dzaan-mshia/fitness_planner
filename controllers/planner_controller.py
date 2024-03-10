from fastapi import APIRouter

router = APIRouter(tags=["Workout Plan"])


@router.get("/")
def get_plans():
    return ['Plan 1', 'Plan 2', 'Plan 3']


@router.get("/{plan_id}")
def get_plan_by_id(plan_id: int):
    return {"id": f'plan {plan_id}'}

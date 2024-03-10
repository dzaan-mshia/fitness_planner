from fastapi import APIRouter, Depends

from service.jwt_utils import check_auth_token

router = APIRouter(tags=["Workout Plan"])


@router.get("/")
def get_plans(auth_user_id: int = Depends(check_auth_token)):
    return ['Plan 1', 'Plan 2', 'Plan 3']


@router.get("/{plan_id}")
def get_plan_by_id(plan_id: int, auth_user_id: int = Depends(check_auth_token)):
    return {"id": f'plan {plan_id}'}

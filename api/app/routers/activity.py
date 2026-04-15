from fastapi import APIRouter, Depends, status

from app.core.auth import get_current_user
from app.core.deps import CurrentUser
from app.schemas.activity import ActivityCreate, ActivityResponse
from app.services.activity import ActivityServiceDep


router = APIRouter(prefix="/activities", tags=["activity"])


@router.get("/", response_model=ActivityResponse)
def get_activities(
    service: ActivityServiceDep,
    current_user=Depends(get_current_user),
):
    return service.get_all_by_user(current_user.id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_activity(
    activity_in: ActivityCreate,
    service: ActivityServiceDep,
    current_user: CurrentUser,
):
    return service.create(activity_in=activity_in, user_id=current_user.id)

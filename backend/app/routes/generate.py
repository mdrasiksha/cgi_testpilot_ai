from fastapi import APIRouter

from app.models.schema import (
    ExportResponse,
    GenerateRequest,
    GenerateResponse,
    UserStoryGenerateRequest,
)
from app.services.export_service import export_service
from app.services.generate_service import generate_from_user_story

router = APIRouter(tags=["generate"])


<<<<<<< HEAD
@router.post("", response_model=GenerateResponse)
def generate(payload: UserStoryGenerateRequest) -> GenerateResponse:
    return GenerateResponse(content=generate_from_user_story(payload.user_story))
=======
@router.post("", response_model=GenerateResponse, summary="Generate content")
def generate(payload: GenerateRequest) -> GenerateResponse:
    return GenerateResponse(content=ai_service.generate(payload.prompt))
>>>>>>> 54287ee (Build modular FastAPI backend app structure)


@router.post("/export", response_model=ExportResponse, summary="Generate and export JSON")
def export(payload: GenerateRequest) -> ExportResponse:
    content = generate_from_user_story(payload.prompt)
    return ExportResponse(format="json", payload=export_service.to_json(content))

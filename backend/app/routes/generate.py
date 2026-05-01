from fastapi import APIRouter

from ..models.schema import ExportResponse, GenerateRequest, GenerateResponse
from ..services.export_service import export_service
from ..services.generate_service import generate_from_user_story

router = APIRouter(tags=["generate"])


@router.post("", response_model=GenerateResponse, summary="Generate content")
def generate(payload: GenerateRequest) -> GenerateResponse:
    return GenerateResponse(content=generate_from_user_story(payload.prompt))


@router.post("/export", response_model=ExportResponse, summary="Generate and export JSON")
def export(payload: GenerateRequest) -> ExportResponse:
    content = generate_from_user_story(payload.prompt)
    return ExportResponse(format="json", payload=export_service.to_json(content))

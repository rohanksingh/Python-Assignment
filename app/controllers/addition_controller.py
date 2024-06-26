from datetime import datetime, timezone
from app.models.addition_request import AdditionRequest
from app.models.addition_response import AdditionResponse
from app.utils.multiprocess_addition import process_list_additions
from app.config import settings

def create_addition_logic(addition_request: AdditionRequest) -> AdditionResponse:
    started_at = datetime.now(timezone.utc)

    try:
        result = process_list_additions(addition_request.payload, num_processes=settings.NUM_PROCESSES)
    except ValueError as e:
        raise e

    completed_at = datetime.now(timezone.utc)
    
    return AdditionResponse(
        batchid=addition_request.batchid,
        response=result,
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )

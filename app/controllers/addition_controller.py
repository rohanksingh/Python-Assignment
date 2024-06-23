from datetime import datetime, timezone
from app.models.addition import AdditionRequest, AdditionResponse
from app.utils.multiprocess_addition import process_list_additions

def create_addition_logic(addition_request: AdditionRequest) -> AdditionResponse:
    started_at = datetime.now(timezone.utc)

    try:
        response_list = process_list_additions(addition_request.payload, num_processes=4)
        result = [sum(sublist) for sublist in response_list]
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

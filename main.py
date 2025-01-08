from typing import Dict, List, Union
import re

Response = Dict[str, Union[int, Dict[str, Union[str, Dict[str, Union[int, List[str]]]]]]]

def invalid_response() -> Response:
    return {
        "statusCode": 400,
        "body": "Invalid input: candidate_id or log_content is missing"
    }

def process_log_file(event: dict, context: dict) -> Response:
    if not isinstance(event, dict):
        return invalid_response()

    candidate_id: str = event.get("candidate_id")
    log_content: str = event.get("log_content")

    if not candidate_id or not log_content:
        return invalid_response()

    try:
        pattern = r'\[.*\] ERROR: (.*)'
        error_messages = re.findall(pattern, log_content)
        unique_error_messages = sorted(set(error_messages))
        return {
            "statusCode": 200,
            "body": {
                "candidate_id": candidate_id,
                "result": {
                    "total_errors": len(error_messages),
                    "unique_error_messages": unique_error_messages,
                }
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"An error occurred: {str(e)}"
        }

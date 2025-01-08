from main import process_log_file

def test_case_1():
    event = {
        "candidate_id": "123",
        "log_content": "[2023-12-01] ERROR: Something went wrong\n[2023-12-01] ERROR: Another error occurred"
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 200,
        "body": {
            "candidate_id": "123",
            "result": {
                "total_errors": 2,
                "unique_error_messages": ["Another error occurred", "Something went wrong"]
            }
        }
    }
    assert result == expected

def test_case_2():
    event = {
        "candidate_id": "456",
        "log_content": "[2023-12-01] INFO: All systems woring fine"
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 200,
        "body": {
            "candidate_id": "456",
            "result": {
                "total_errors": 0,
                "unique_error_messages": []
            }
        }
    }
    assert result == expected

def test_case_3():
    event = {
        "log_content": "[2023-12-01] ERROR: Something went wrong"
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 400,
        "body": "Invalid input: candidate_id or log_content is missing"
    }
    assert result == expected

def test_case_4():
    event = {
        "candidate_id": "789"
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 400,
        "body": "Invalid input: candidate_id or log_content is missing"
    }
    assert result == expected

def test_case_5():
    event = {
        "candidate_id": "789",
        "log_content": ""
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 400,
        "body": "Invalid input: candidate_id or log_content is missing"
    }
    assert result == expected

def test_case_6():
    event = {
        "candidate_id": "101",
        "log_content": "[2023-12-01] ERROR: Something went wrong\n[2023-12-01] ERROR: Something went wrong"
    }
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 200,
        "body": {
            "candidate_id": "101",
            "result": {
                "total_errors": 2,
                "unique_error_messages": ["Something went wrong"]
            }
        }
    }
    assert result == expected

def test_case_7():
    event = None
    context = {}
    result = process_log_file(event, context)
    expected = {
        "statusCode": 400,
        "body": "Invalid input: candidate_id or log_content is missing"
    }
    assert result == expected



def test_process_log_file():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    test_case_7()
    print("All test cases passed")

if __name__ == '__main__':
    test_process_log_file()

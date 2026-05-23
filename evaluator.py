def validate_record(record):
    assert record.email != "", "Email missing"
    assert record.linkedin_score > 0, "Bad score"
    return True

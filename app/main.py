import pprint

def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }







def format_single_linter_file(file_path: str, errors: list) -> dict:
    # bledy = []
    #
    # for er in errors:
    #     bledy.append(format_linter_error(er))
    #
    # stat = "passed" if not bledy else "failed"
    # rest = {
    #     "errors": bledy,
    #     "path": file_path,
    #     "status": stat
    # }
    return {
                "errors": (mors := [format_linter_error(er) for er in errors]),
                "path": file_path,
                "status": "passed" if not mors else "failed"
            }







def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass






error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
    "store and decorate numbers: {', '.join(items)}!\"",
}

errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
        "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    }
]
asdasd = []

# pprint.pprint(format_linter_error(error), width=100)
# pprint.pprint(format_single_linter_file("./source_code_2.py", errors), width=100)

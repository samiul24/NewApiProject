from rest_framework.exceptions import ErrorDetail

def prepare_success_response(data=None)->dict:
    # print(data) # <QuerySet [{'id': 1, 'name': 'Grocary', 'is_active': 'True'}, {'id': 2, 'name': 'Rice', 'is_active': 'True'} ]
    # print(type(data)) # <class 'django.db.models.query.QuerySet'>
    return dict(
        success=True,
        message='Successfully Return',
        data=data,
    )

def prepare_error_response(message=None) -> dict:
    if hasattr(message, 'items'):
        #print(message)
        for key, _ in message.items():
            message[key] = message[key][0]

    return dict(
        success=False,
        message=message if message else "Data Validation Error",
        data=None
    )
get_valid_data = [
    {
        "get": "88036-000",
        "success": True,
        "http_status_code": 200,
        "internal_code": 0,
        "data": {
            "address1": "Rua Lauro Linhares",
            "address2": "Trindade",
            "city": "Florianópolis",
            "state": "SC",
            "postCode": "88036000"
        },
        "notifications": []
    },
    {
        "get": "70165-900",
        "success": True,
        "http_status_code": 200,
        "internal_code": 0,
        "data": {
            "address1": "Praça dos Três Poderes",
            "address2": "Zona Cívico-Administrativa",
            "city": "Brasília",
            "state": "DF",
            "postCode": "70165900"
        },
        "notifications": []
    },
    {
        "get": "68980-000",
        "success": True,
        "http_status_code": 200,
        "internal_code": 0,
        "data": {
            "address1": "",
            "address2": "",
            "city": "Oiapoque",
            "state": "AP",
            "postCode": "68980000"
        },
        "notifications": []
    }
]
get_invalid_ceps = [
    {
        "get": "00000-oo0",
        "success": False,
        "http_status_code": 400,
        "internal_code": 0,
        "data": None,
        "notifications": [
            {
                "id": "",
                "field": "CEP",
                "level": "VALIDATION_ERROR",
                "errors": []
            }
        ]
    },
    {
        "get": "12345-6789",
        "success": False,
        "http_status_code": 400,
        "internal_code": 0,
        "data": None,
        "notifications": [
            {
                "id": "",
                "field": "CEP",
                "level": "VALIDATION_ERROR",
                "errors": []
            }
        ]
    },
    {
        "get": "das",
        "success": False,
        "http_status_code": 400,
        "internal_code": 0,
        "data": None,
        "notifications": [
            {
                "id": "",
                "field": "CEP",
                "level": "VALIDATION_ERROR",
                "errors": []
            }
        ]
    },
    {
        "get": "986",
        "success": False,
        "http_status_code": 400,
        "internal_code": 0,
        "data": None,
        "notifications": [
            {
                "id": "",
                "field": "CEP",
                "level": "VALIDATION_ERROR",
                "errors": []
            }
        ]
    }
]
get_unexisting_ceps = [
    {
        "get": "00000-000",
        "success": True,
        "http_status_code": 404,
        "internal_code": 0,
        "data": None,
        "notifications": []
    },
    {
        "get": "80000-000",
        "success": True,
        "http_status_code": 404,
        "internal_code": 0,
        "data": None,
        "notifications": []
    }
]
other_valid_data = [
    "88036-000",
    "70165-900",
    "68980-000"
]

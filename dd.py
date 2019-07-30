[
    {
        "name": "bp1",
        "item": [
            {
                "name": "/endpoint-one",
                "request": {
                    "url": {
                        "raw": "{{target_url}}endpoint-one",
                        "host": ["{{target_url}}endpoint-one"],
                    },
                    "description": "Return text from request.",
                },
            },
            {
                "name": "/endpoint-two",
                "request": {
                    "url": {
                        "raw": "{{target_url}}endpoint-two",
                        "host": ["{{target_url}}endpoint-two"],
                    },
                    "description": "Return JSON form request.",
                },
            },
        ],
        "description": "This is the doc string for blueprint1.",
    },
    {
        "name": "bp2",
        "item": [
            {
                "name": "/endpoint-three",
                "request": {
                    "url": {
                        "raw": "{{target_url}}endpoint-three",
                        "host": ["{{target_url}}endpoint-three"],
                    },
                    "description": "Return text from request.",
                },
            },
            {
                "name": "/endpoint-four",
                "request": {
                    "url": {
                        "raw": "{{target_url}}endpoint-four",
                        "host": ["{{target_url}}endpoint-four"],
                    },
                    "description": "Return JSON form request.",
                },
            },
        ],
        "description": "This is the doc string for blueprint2.",
    },
]


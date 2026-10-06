# You receive API test results:

# results = [
#     {"test": "login", "status": 200},
#     {"test": "get_user", "status": 200},
#     {"test": "create_user", "status": 201},
#     {"test": "delete_user", "status": 404},
#     {"test": "update_user", "status": 500},
#     {"test": "logout", "status": 200},
#     {"test": "get_orders", "status": 404}
# ]
# Task

# Create a dictionary that groups test names by HTTP status code.

# Expected result:

# {
#     200: ["login", "get_user", "logout"],
#     201: ["create_user"],
#     404: ["delete_user", "get_orders"],
#     500: ["update_user"]
# }

results = [
    {"test": "login", "status": 200},
    {"test": "get_user", "status": 200},
    {"test": "create_user", "status": 201},
    {"test": "delete_user", "status": 404},
    {"test": "update_user", "status": 500},
    {"test": "logout", "status": 200},
    {"test": "get_orders", "status": 404}
]
output = {}

for item in results:
    test_item = item["test"]
    status_code = item["status"]

    if status_code not in output:
        output[status_code]=[test_item]
    else:
        output[status_code].append(test_item)
print(output)

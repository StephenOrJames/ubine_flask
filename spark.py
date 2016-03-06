from sparkpost import SparkPost

sp = SparkPost("aae8a1c421aae9c7285c79c33363b978feccd05e")

# response = sp.transmissions.send(
#     from_email="test@ubine.ml",
#     recipients=["stephenorjames@gmail.com"],
#     subject="It works",
#     html="<html><body><p>SparkPost works! Azure doesn't.</p></body></html>"
# )
#
# print(response)

# response = sp.recipient_lists(
#     {
#         "id": "ubine-events",
#         "name": "UBinE events",
#         "description": "Users subscribed to UBinE events",
#         "attributes": {
#             "internal_id": 1,
#             "list_group_id": 1
#         },
#         "recipients": [
#             {
#                 "return_path": "no-reply@ubine.ml",
#                 "address": {
#                     "email": "stephenorjames@gmail.com",
#                     "name": "Stephen James"
#                 },
#                 "metadata": {
#                     "quadrangle": "Richmond"
#                 },
#                 "tags": [
#                     "student",
#                     "Richmond"
#                 ]
#             },
#             {
#                 "return_path": "no-reply@ubine.ml",
#                 "address": {
#                     "email": "ubine@hmamail.com",
#                     "name": "HMA Mail"
#                 },
#                 "tags": [
#                     "fake",
#                     "Porter"
#                 ]
#             }
#         ]
#     }
# )
#
# print(response)

# response = sp.recipient_lists.update(
#     "ubine-events",
#     recipients=[{"address": {"email": "sjames5@buffalo.edu"}}]
# )
# print(response)

# response = sp.recipient_lists.get("ubine-events", show_recipients=True)
# print(response["recipients"])
# sp.recipient_lists.update("ubine-events")

# response = sp.recipient_lists.create(
#     id="ubine-events",
#     name="UBinE events",
#     recipients=[
#         {"address": {"email": "sjames5@buffalo.edu"}},
#         {"address": {"email": "stephenorjames@gmail.com"}},
#         {"address": {"email": "sjames5@acsu.buffalo.edu"}},
#         {"address": {"email": "sjames5@cse.buffalo.edu"}},
#         {"address": {"email": "sjames5@eng.buffalo.edu"}},
#     ]
# )

response = sp.recipient_lists.update(
    "ubine-events",
    recipients=[
        {"address": {"email": "sjames5@buffalo.edu"}},
        {"address": {"email": "stephenorjames@gmail.com"}},
        # {"address": {"email": "sjames5@acsu.buffalo.edu"}},
        # {"address": {"email": "sjames5@cse.buffalo.edu"}},
        # {"address": {"email": "sjames5@eng.buffalo.edu"}},
    ]
)
print(response)

import requests
import json

# class RestfulAPI:
#     def get_objects(self):
#         headers = {"content-type": "application/json"}
#         url = "https://api.restful-api.dev/objects"
#         payload = ""
#         headers = {
#             "User-Agent": "insomnia/10.3.0",
#             "Content-Type": "application/json"
#         }
#
#         response = requests.request("GET", url, data=payload, headers=headers)
#         return response
#
#     def get_objects_by_id(self, object_id):
#         url = f"https://api.restful-api.dev/objects/{object_id}"
#         payload = ""
#         headers = {
#             "User-Agent": "insomnia/10.3.0",
#             "Content-Type": "application/json"
#         }
#         response = requests.request("GET", url, data=payload, headers=headers)
#         return response
#
#     def post_object(self, payload):
#         url = "https://api.restful-api.dev/objects"
#         headers = {
#             "Content-Type": "application/json",
#             "User-Agent": "insomnia/10.3.0"
#         }
#
#         response = requests.request("POST", url, json=payload, headers=headers)
#         return response
#
#     def update_object(self, object_id, payload):
#         url = f"https://api.restful-api.dev/objects/{object_id}"
#         headers = {
#             "Content-Type": "application/json",
#             "User-Agent": "insomnia/10.3.0"
#         }
#
#         response = requests.request("PUT", url, json=payload, headers=headers)
#         return response
#
#     def delete_object(self, object_id):
#         url = f"https://api.restful-api.dev/objects/{object_id}"
#         payload = ""
#         headers = {
#             "Content-Type": "application/json",
#             "User-Agent": "insomnia/10.3.0"
#         }
#
#         response = requests.request("DELETE", url, json=payload, headers=headers)
#         return response
nd = {
    "fruit": {
        "apple": {
            "color": "red"
        }}}

# Safely accessing the value using get()
color = nd.get("fruit", {}).get("apple", {}).get("color")
print(color)

nd.get()
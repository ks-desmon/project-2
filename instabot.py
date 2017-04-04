import requests

tokken_for_access_app = "1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520"
BASE_URL = "https://api.instagram.com/v1/"

#using get to collect owner information
def info_owner():
    url_owner=BASE_URL+"users/self/?access_token="+tokken_for_access_app
    owner_info=requests.get(url_owner).json()
    print owner_info
    print owner_info["data"]["full_name"]
    print owner_info["data"]["bio"]
    print owner_info["data"]["username"]

info_owner()
def get_user_by_username(user_name):
    url_user=BASE_URL+"users/{"+user_name+"}/?access_token="+tokken_for_access_app
    user_info= requests.get(url_user).json()
    print user_info

get_user_by_username("yashika3990")
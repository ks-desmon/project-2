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
    url_user=BASE_URL+"users/search?q="+user_name+"&access_token="+tokken_for_access_app #https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
    user_info= requests.get(url_user).json()
    return user_info["data"][0]["id"]

def get_user_post_id(username):
    user_id1= get_user_by_username(username)
    url_user1=BASE_URL+"users/"+user_id1+"/media/recent/?access_token="+tokken_for_access_app#https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    request_for_user_to_get_all_post=requests.get(url_user1).json()
    return request_for_user_to_get_all_post["data"][0]['id']

def like_on_user_post_id(user_id):
    user_current_post_id=get_user_post_id(user_id)
    Access_token={'access_token':tokken_for_access_app}
    url_post_like= BASE_URL+"media/"+user_current_post_id+"/likes"
    requests.post(url_post_like,Access_token).json()

def comment_on_user_id(user_id):
    user_current_post_id=get_user_post_id(user_id)
    Access_token_Plus_comment ={'access_token':tokken_for_access_app,'text':"hey its my first comment for u using python"}
    url_post_comment= BASE_URL+"/media/"+user_current_post_id+"/comments"
    comment= requests.post(url_post_comment,Access_token_Plus_comment).json()
    print comment


like_on_user_post_id("amritbirsingh345")
comment_on_user_id("amritbirsingh345")









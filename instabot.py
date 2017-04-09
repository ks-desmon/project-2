import requests
#access token for performing operation on user and owner account<<<<< used in the scope of basic, public_content, likes, comments.>>>>>
tokken_for_access_app = "1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520"
                                                #url part commen in all urls
BASE_URL = "https://api.instagram.com/v1/"


def info_owner():                               #using get to collect owner information
    url_owner=BASE_URL+"users/self/?access_token="+tokken_for_access_app
    owner_info=requests.get(url_owner).json()
    print "owner id is "+owner_info["data"]['id']
    print "owner full name is "+owner_info["data"]["full_name"]
    print "owner bio is "+owner_info["data"]["bio"]
    print "owner usename is "+owner_info["data"]["username"]


def get_user_id_username(user_name):              #get user id
    if user_name  not in ['amritbirsingh345','yashika3990']:
        print"you enter wrong wrong username"
        return
    else:
        url_user=BASE_URL+"users/search?q="+user_name+"&access_token="+tokken_for_access_app#https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
        user_info= requests.get(url_user).json()
        sucess = user_info["meta"]["code"]
        if sucess == 200:                          #checking url
            print "successsfully found user id "
        else:
            print "unsucsessfull plz try again"
        return user_info["data"][0]["id"]          #returning user id

#this funn is::: returning the post id :::on the bases of funn << get_user_by_user_name >>
def get_user_post_id(username):
    user_id1 = get_user_id_username(username)
    url_user1 = BASE_URL + "users/" + user_id1 + "/media/recent/?access_token=" + tokken_for_access_app  # https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    request_for_user_to_get_all_post = requests.get(url_user1).json()
    sucess = request_for_user_to_get_all_post["meta"]["code"]
    for post_no in range(0,len(request_for_user_to_get_all_post["data"]),1):
        post_no
    exact_posts=str(post_no)
    print 'we have total '+exact_posts+'posts of  :'+username+'\n which post you want to chose'
    post_no=raw_input()
    i=int(post_no)
    if sucess == 200:
        print "successsfully found user id and fetched user's post id "
    else:
        print "unsucsessfull plz check user name again"
    return request_for_user_to_get_all_post["data"][i]['id']


#this funn is use to do like on users post_id which is getting from  funn <<<user_post_id>>>
def like_on_user_post_id(user_name):
    post_id = get_user_post_id(user_name)
    Access_token={'access_token':tokken_for_access_app}
    url_post_like= BASE_URL+"media/"+post_id+"/likes"
    like_result=requests.post(url_post_like,Access_token).json()
    sucess = like_result["meta"]["code"]
    if sucess == 200:  # checking url
        print "successsfully liked the pic "
    else:
        print "unsucsessfull plz try again"

def comment_on_user_id(user_name):
    post_id = get_user_post_id(user_name)  # post_id which is getting from  funn <<<user_post_id>>>
    print "write comment u want to write \n but rules are \n 1. The total length of the comment cannot exceed 300 characters.\n 2. The comment cannot contain more than 4 hashtags.\n 3. The comment cannot contain more than 1 URL.\n 4. The comment cannot consist of all capital letters."
    entered_comment = raw_input()
    entered_comment = str(entered_comment)
    url_post_comment = BASE_URL + "media/"+post_id+"/comments"
    Access_token_Plus_comment = {'access_token': tokken_for_access_app, 'text': entered_comment}
    comment_result = requests.post(url_post_comment, Access_token_Plus_comment).json()
    sucess = comment_result["meta"]["code"]
    if sucess == 200:  # checking url
        print "successsfully commented on the pic "
    else:
        print "unsucsessfull plz try again"

#selecting user name
Variable1 ="y"
while Variable1 =="y":
    info_owner()                                            # calling funn to print owner information
    print"hey type the username from following \n  amritbirsingh345  \n  yashika3990 "
    user_name = raw_input()
    print"select what do you want to do 1:like 2:comment"
    choice=raw_input()
    if choice=="1":
        like_on_user_post_id(user_name)
    elif choice=="2":
        comment_on_user_id(user_name)
    else:
        print"you chose wrong"

    print"press any key for exit or press y to continue"
    Variable1=raw_input()
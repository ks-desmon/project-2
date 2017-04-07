import requests
#access token for performing operation on user and owner account<<<<< used in the scope of basic, public_content, likes, comments.>>>>>
tokken_for_access_app = "1993495056.1b2b25a.bbdc1be8c2364ab181433835f5c37520"
#url part commen in all urls
BASE_URL = "https://api.instagram.com/v1/"


def funn_is_successful_or_not(sucess):#is is going to check and tell the operation performed is successful or not
    if sucess == 200:
        print "your choice successsfully done "
    else:
        print "sry unsucsessfull make sure ur all inputs are correct"


#using get to collect owner information
def info_owner():
    url_owner=BASE_URL+"users/self/?access_token="+tokken_for_access_app
    owner_info=requests.get(url_owner).json()
    print "owner id is "+owner_info["data"]['id']
    print "owner full name is "+owner_info["data"]["full_name"]
    print "owner bio is "+owner_info["data"]["bio"]
    print "owner usename is "+owner_info["data"]["username"]


#this funn returning owner id for further operation like getting post id
def get_user_by_username(user_name):
    url_user=BASE_URL+"users/search?q="+user_name+"&access_token="+tokken_for_access_app #https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
    user_info= requests.get(url_user).json()
    print user_info["data"][0]["full_name"]
    print user_info["data"][0]["username"]
    return user_info["data"][0]["id"]
    sucess = user_info["meta"]["code"]
    if sucess == 200:
        print "successsfully found user id "
    else:
        print "unsucsessfull plz check user name again"


#this funn is::: returning the post id :::on the bases of funn << get_user_by_user_name >>
def get_user_post_id(username,post_number):
    i=int(post_number)
    user_id1= get_user_by_username(username)
    url_user1=BASE_URL+"users/"+user_id1+"/media/recent/?access_token="+tokken_for_access_app#https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    request_for_user_to_get_all_post=requests.get(url_user1).json()
    sucess = request_for_user_to_get_all_post["meta"]["code"]
    if sucess == 200:
        print "successsfully found user id "
    else:
        print "unsucsessfull plz check user name again"
    return request_for_user_to_get_all_post["data"][i]['id']


#this funn is use to do like on users post_id which is getting from  funn <<<user_post_id>>>
def like_on_user_post_id(user_id,post_number):
    user_current_post_id=get_user_post_id(user_id,post_number)
    Access_token={'access_token':tokken_for_access_app}
    url_post_like= BASE_URL+"media/"+user_current_post_id+"/likes"
    like_result=requests.post(url_post_like,Access_token).json()
    sucess = like_result["meta"]["code"]
    funn_is_successful_or_not(sucess)# checking is that operation is successfl or not..


#this funn is use to comment on users post_id which is getting from  funn <<<user_post_id>>>
def comment_on_user_id(user_id,entered_comment,post_number):
    user_current_post_id=get_user_post_id(user_id,post_number)# post_id which is getting from  funn <<<user_post_id>>>
    url_post_comment = BASE_URL + "media/" + user_current_post_id + "/comments"
    Access_token_Plus_comment ={'access_token':tokken_for_access_app,'text':entered_comment}
    comment_result=requests.post(url_post_comment,Access_token_Plus_comment).json()
    sucess = comment_result["meta"]["code"]
    funn_is_successful_or_not(sucess)# checking is that operation is successfl or not..

#funn is to get all recent comment on a perticular post
def get__commentid(username,post_number):
    get_post_id=get_user_post_id(username,post_number)
    Url_for_getting_comment_id =BASE_URL+"media/"+get_post_id+"/comments?access_token="+tokken_for_access_app
    comment_id=requests.get(Url_for_getting_comment_id).json()
    for i in range (0,len (comment_id["data"]),1):
        print comment_id['data'][i]['text']

def fun_main():
    info_owner()
    Variable1 ="y"
    while Variable1=="y" :
        list = [ "amritbirsingh345","yashika3990"]  #List of all users added by the owner
        print "hey enter user name from following : amritbirsingh345 : yashika3990 "
        user_name= raw_input()
        if user_name in list:                       #checking entered user is valid or not..
            print "what u want to do : for comment press 1:For like press 2:For delete comment :3For checking recent comment on post"
            input = raw_input()
            print input
            if input =="1":
                print "we have latest five posts of user on which you want to comment ?? 0 , 1 , 2 , 3 , 4"
                list2=["0","1","2","3","4"]         #giving choice to user to chose between no of choice
                post_number= raw_input()
                if post_number in list2:
                    print "write comment u want to write \n but rules are \n 1. The total length of the comment cannot exceed 300 characters.\n 2. The comment cannot contain more than 4 hashtags.\n 3. The comment cannot contain more than 1 URL.\n 4. The comment cannot consist of all capital letters."
                    entered_comment = raw_input()
                    entered_comment = str(entered_comment)
                    comment_on_user_id(user_name,entered_comment,post_number)
                    print "thanks your comment is has been posted"
                else:
                    print "you chose wrong choice"
            elif input =="2":
                print "we have latest five posts of user on which you want to like ?? 0 , 1 , 2 , 3 , 4"
                post_number = raw_input()
                list2 = ["0", "1", "2", "3", "4"]  # giving choice to user to chose between no of choice
                if post_number in list2:
                    like_on_user_post_id(user_name,post_number)
                    print "thanks your liked user post"
                else:
                    print "your choice is wrong"
            elif input =="3":
                print "we have latest five posts of user on which you want to like ?? 0 , 1 , 2 , 3 , 4"
                post_number = raw_input()
                list2 = ["0", "1", "2", "3", "4"]  # giving choice to user to chose between no of choice
                if post_number in list2:
                    get__commentid(user_name,post_number)
                else:
                    print "opps wrong choice"
            else:
                print "wrong input"
        else:
            print "sry the username is wrong"
        print "you want to do again press y of not press any other key"
        Variable1=raw_input()

fun_main()

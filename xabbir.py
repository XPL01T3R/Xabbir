#Youtube : https://youtube.com/channel/UCQxsdKKHhf1zYpGdqsOKonQ
#Facebook : https://www.facebook.com/sab.bir936
#Instagram : https://instagram.com/catch._me_if_you_can?igshid=w1j6mscmruwg

try:
    import mechanize,requests,os,sys,subprocess,cookielib,time,random
except ImportError:
    subprocess.call("pip2 install requests mechanize", shell=True)

subprocess.call("clear",shell=True)

#color
green = "\033[1;32m"
normal = "\033[0m"
red = "\033[1;31m"
cyan = "\033[1;36m"
#symbols
good = "\033[1;32m[\033[1;36m+\033[1;32m]\033[0m"
bad = "\033[1;32m[\033[1;31m!\033[1;32m]\033[0m"
#word
success = "\033[1;32mSuccessful\033[0m"
failed = "\033[1;31mFailed\033[0m"

###banner###
banner_menu =red+ """


                                                                
                                                                
 ,--,     ,--,                                                  
 |'. \   / .`|              ,---,     ,---,     ,--,            
 ; \ `\ /' / ;            ,---.'|   ,---.'|   ,--.'|    __  ,-. 
 `. \  /  / .'            |   | :   |   | :   |  |,   ,' ,'/ /| 
  \  \/  / ./    ,--.--.  :   : :   :   : :   `--'_   '  | |' | 
   \  \.'  /    /       \ :     |,-.:     |,-.,' ,'|  |  |   ,' 
    \  ;  ;    .--.  .-. ||   : '  ||   : '  |'  | |  '  :  /   
   / \  \  \    \__\/: . .|   |  / :|   |  / :|  | :  |  | '    
  ;  /\  \  \   ," .--.; |'   : |: |'   : |: |'  : |__;  : |    
./__;  \  ;  \ /  /  ,.  ||   | '/ :|   | '/ :|  | '.'|  , ;    
|   : / \  \  ;  :   .'   \   :    ||   :    |;  :    ;---'     
;   |/   \  ' |  ,     .-./    \  / /    \  / |  ,   /          
`---'     `--` `--`---'   `-'----'  `-'----'   ---`-'           
                                                                




#########################################

#1. Generate Access Token
#2. Auto React
#3. Auto Comment
#4. Auto Friend Requests

#########################################
""".format(green,normal,green,normal)

banner =green+ """


                                                                
                                                                
 ,--,     ,--,                                                  
 |'. \   / .`|              ,---,     ,---,     ,--,            
 ; \ `\ /' / ;            ,---.'|   ,---.'|   ,--.'|    __  ,-. 
 `. \  /  / .'            |   | :   |   | :   |  |,   ,' ,'/ /| 
  \  \/  / ./    ,--.--.  :   : :   :   : :   `--'_   '  | |' | 
   \  \.'  /    /       \ :     |,-.:     |,-.,' ,'|  |  |   ,' 
    \  ;  ;    .--.  .-. ||   : '  ||   : '  |'  | |  '  :  /   
   / \  \  \    \__\/: . .|   |  / :|   |  / :|  | :  |  | '    
  ;  /\  \  \   ," .--.; |'   : |: |'   : |: |'  : |__;  : |    
./__;  \  ;  \ /  /  ,.  ||   | '/ :|   | '/ :|  | '.'|  , ;    
|   : / \  \  ;  :   .'   \   :    ||   :    |;  :    ;---'     
;   |/   \  ' |  ,     .-./    \  / /    \  / |  ,   /          
`---'     `--` `--`---'   `-'----'  `-'----'   ---`-'           
                                                                



#########################################                                               
""".format(green,normal,cyan,normal,green,normal)
###


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
info = time.strftime("%S:%M:%H")

def generate_token():
    print banner
    print
    username = raw_input("username : ")
    password = raw_input("password : ")
    print "Generating token Please Wait....".format(info,good)
    time.sleep(5)
    if len(username) == 0:
         print "Input Username !!!".format(info,good)
    elif len(password) == 0:
        print "Input Password !!!".format(info,good)
    else:
        token_parsing = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + username + "&locale=en_US&password=" + password + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").read()
        file_token_access = open("token.txt","w")
        file_token_access.write(str(token_parsing))
        file_token_access.close()
        try:
            print "[{}]{} STATUS : {}".format(info,good,success)
            print "[{}]{} SAVED FILE WITH NAME : token.txt".format(info,good)
        except:
            print "[{}]{} Error Operation System".format(info,bad)

def autolike():
    print banner
    print
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        react = raw_input("[#] Select reaction ['LIKE','LOVE','HAHA','WOW','SAD','ANGRY'] : ")
        d = br.open("https://yolikers.com/like.php?type=status")
        br.select_form(nr=0)
        br.form["type"] = [""+react]
        br.submit()
        print "[#] Like sent successfully..".format(info,good)
    except:
        print "[#] Use After 10 Minute..".format(info,bad)

def comment():
    print banner
    print
    print "[#] Commenting on post...".format(info,good)
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/commenter.php?type=status")
    br.select_form(nr=0)
    br.form["access_token"] = token
    br.submit()
    try:
        b = br.open("https://yolikers.com/commenter.php?type=status")
        br.select_form(nr=0)
        br.submit()
        print "[#] Commented successfully..".format(info,good)
    except:
        print "[#] Use After 10 Minute..".format(info,bad)

def friend():
    print banner
    print
    print "[#] Sending 30 Friend Requests...".format(info,good)
    token = open("token.txt","r").read()
    a = br.open("https://yolikers.com/")
    br.select_form(nr=0)
    br.form["access_token"] = token
    try:
        b = br.open("https://yolikers.com/autorequest.php?type=profile")
        br.select_form(nr=0)
        br.submit()
        print "[#] 30 friend requests sent successfully...".format(info,good)
    except:
        print "[#] Use After 10 Minute...".format(info,good)


if __name__=="__main__":
    while True:
        print banner_menu
        print
        pilih_menu = raw_input("xa_bbir>> ")
        if len(pilih_menu) == 0:
            print "Input numbers!!".format(bad)
        elif pilih_menu == "1":
            generate_token()
            time.sleep(5)
        elif pilih_menu == "2":
            autolike()
            time.sleep(5)
        elif pilih_menu == "3":
            comment()
            time.sleep(5)
        elif pilih_menu == "4":
            friend()
            time.sleep(5)

class signin():
    Tab_signin = "//a[contains(@title,'Log in to your customer account')]" #Xpath
    txt_email = "email" #id
    txt_password = "passwd"  #id
    Btn_signin = "SubmitLogin"  #id
    loggedin_name = "//a[contains(.,'uday shankar')]"


class signout():
    Tab_logout = '//a[contains(@title,"Log me out")]'


class homepage():
    My_address = "//a[contains(.,'My addresses')]"
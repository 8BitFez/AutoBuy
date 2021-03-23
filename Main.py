import pickle
from webbot import Browser
from time import sleep
from time import asctime

web = Browser()
exitcode = 0
print("going to sleep")
web.go_to('google.com')
soldOut = True
searchItem = "Nest Mini (2nd Generation) Smart Speaker with Google Assistant - Chalk"
 #"Microsoft - Xbox Series X 1TB Console - Black"

#setting up menu to grab cookies and help with prototyping

while exitcode == 0:
    print("What would you like to do")
    print ('import cookies: 1 /n export cookies: 2 /n run loop: 3 /n quit: quit ')
    # a = '3'
    a = input("what would you like to do? ")
    if a == '1':
        print("Importing Cookies!")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            web.add_cookie(cookie)
        print("Cookies Imoported! Yummy!")
    elif a == '2':
        awn = input("Ready to Eat Cookie! y/n? ")
        if awn == "y":
            print("Waking up and eatting cookies")
            pickle.dump( web.get_cookies() , open("cookies.pkl","wb"))
            print("All Done!")
    elif a == 'quit':
        exitcode += 1
    elif a == '3':
    
    #auto importing cookies for fast prototyping 
      
        print("Importing Cookies!")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            web.add_cookie(cookie)
        print("Cookies Imoported! Yummy!")

    #Starting Scripts for right just looping once

        print("Running Bot! Time: " + str(asctime()))
        web.go_to('bestbuy.com')
        web.press(web.Key.ESCAPE)
        web.type( searchItem ,id='gh-serch-input')
        web.press(web.Key.ENTER)
        web.click(text=searchItem)
        # we are now just  waiting for one to be in stock
        #so we will read the html page to see if some are in stock
        while soldOut:
            
            soldOut = web.exists(text="Sold Out",tag="button",classname="btn-disable")
            print("Are they sold out? "+ str(soldOut) )
            sleep(5)
            web.refresh()
        # xbox is in stock now 
        print(searchItem + " is in stock! Buying!")
        #web.click()
        #exitcode += 1
        



#Examples that i am learning from

#web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
#web.press(web.Key.ENTER)
#web.go_back()
#web.click('Sign in')
#web.type('mymail@gmail.com' , into='Email')
#web.click('NEXT' , tag='span')
#web.type('mypassword' , into='Password' , id='passwordFieldId')
#web.click('NEXT' , tag='span') # you are logged in . woohoooo
exitcode = 1
web.quit()
print("End of Bot: Exit Code: "+ str(exitcode))
import pickle
from webbot import Browser
from time import sleep
from time import asctime
from discord_webhook import DiscordWebhook


webhookUrl = "https://discordapp.com/api/webhooks/824504647430832169/4qtYraSAT_M71sh7eI9JnsE1MZKErkRaedtMf_9DILHql0VfhE_VzxaBQ7DJUVXDu-KR"

def send(msg):
    webhook = DiscordWebhook(url= webhookUrl, content= msg)
    response = webhook.execute()

web = Browser()
exitcode = 0
print("Starting Up")

searchItem = "Storage Expansion Card for Xbox Series X 1TB"
webstore = "www.gamestop.com"
findElement = '<button class="add-to-cart btn btn-primary " data-pid="B224744V" data-gtmdata="{&quot;productInfo&quot;:{&quot;sku&quot;:&quot;B224744V&quot;,&quot;productID&quot;:&quot;B224744V&quot;,&quot;name&quot;:&quot;Xbox Series X&quot;,&quot;category&quot;:&quot;Video Games/Xbox Series X/Consoles&quot;,&quot;brand&quot;:&quot;&quot;,&quot;subGenre&quot;:&quot;&quot;,&quot;platform&quot;:&quot;&quot;,&quot;condition&quot;:&quot;New&quot;,&quot;variant&quot;:&quot;New&quot;,&quot;genre&quot;:&quot;&quot;,&quot;availability&quot;:&quot;Not Available&quot;,&quot;productType&quot;:&quot;bundle&quot;,&quot;zoneSource&quot;:&quot;PDP&quot;,&quot;tradeinProductName&quot;:&quot;&quot;,&quot;programName&quot;:&quot;&quot;,&quot;tradeinOpted&quot;:&quot;&quot;},&quot;price&quot;:{&quot;sellingPrice&quot;:&quot;499.99&quot;,&quot;basePrice&quot;:&quot;499.99&quot;,&quot;currency&quot;:&quot;USD&quot;}}" data-buttontext="Add to Cart" disabled="disabled">Not Available</button>'
CVV = "167"
#"Nest Mini (2nd Generation) Smart Speaker with Google Assistant - Chalk"
#setting up menu to grab cookies and help with prototyping

#start brower to import cookies
web.go_to('google.com')
soldOut = True

while exitcode == 0:
    print("What would you like to do")
    print ('import cookies: 1 /n export cookies: 2 /n run loop: 3 /n quit: quit ')
    a = '3'
    #a = input("what would you like to do? ")
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

        send("Running Bot! Time: " + str(asctime()))
        web.go_to(webstore)
        web.press(web.Key.ESCAPE)
        web.type( searchItem , classname= 'search-field')
        web.press(web.Key.ENTER)
        web.click(text=searchItem, loose_match=False)
        pagesource = web.get_page_source()
# we are now just  waiting for one to be in stock
# so we will read the html page to see if some are in stock
        
        if pagesource.find(findElement) > 0:
            soldOut = True
        
        else:
            soldOut = False

        print(str(asctime()) +" Are they sold out? "+ str(soldOut) )
        
        while soldOut:
            
            print(str(asctime()) +" Are they sold out? "+ str(soldOut) )
            sleep(5)
            web.refresh()

            if pagesource.find(findElement) < 0:
                soldOut = True
# the item is in stock now 
        send(searchItem + " is in stock! Buying!")
        web.save_screenshot("in_stock.png")        
        web.click(text="add to cart",classname="add-to-cart")
        web.go_to("https://www.gamestop.com/cart/")
        sleep(2)
        web.go_to("https://www.gamestop.com/checkout/login/")
        input("halt")
        
        sleep(3)
        web.type(email ,id="")
        web.type(password ,id="")
        web.click(text="Continue To Payment")
        web.type(CVV,id="saved-payment-security-code")
        web.click("Continue To Order Review",tag="button")
        sleep(2)
        send("Placing Order")
        #web.click("Place Order" ,tag="button")
        web.save_screenshot("Order_placed.png")
        
        exitcode += 1
        

exitcode = 1
web.quit()
print("End of Bot: Exit Code: "+ str(exitcode))
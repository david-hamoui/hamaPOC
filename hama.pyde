
from modules import Main
from modules import Login
from modules import Home
from modules import SignIn
from modules import Profile
from modules import Restaurants

main = Main('l')
login = Login()
home = Home()
signIn = SignIn()
profile = Profile()
restaurants = Restaurants()


def setup():
    
    size(500,800)
    background(255)
    rectMode(CENTER)
    textAlign(CENTER)
    imageMode(CENTER)
    
    strokeWeight(3)
    
    backimage = loadImage("hama_background.png")
    hamalogo = loadImage("hama_logo.png")
    
    main.setGlobalVariables()
    
    
def draw():
    
    background(255)
    
    
    if main.page() == "l":
        login.display()
    elif main.page() == "h":
        home.display()
    elif main.page() == 's':
        signIn.display()
    elif main.page() == 'p':
        profile.display()
    elif main.page() == 'r':
        restaurants.display()
    
    
    
    main.updateTime()


        
def keyPressed():
    main.passKey(key)

    

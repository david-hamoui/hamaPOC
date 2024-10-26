time = 0
currentKey = None
newKey = False
changePage = False
changePageTo = ''
userLogin = []
restaurantObj = []




class Main():
    def __init__(self, startingPage):
        self.currentPage = startingPage
        self.Key = None
        
    def page(self):
        global changePage, changePageTo
        if changePage:
            self.currentPage = changePageTo
        
        return self.currentPage
    
    def setGlobalVariables(self):
        global sf,mf,bf
        
        #fonts
        sf = createFont("Baskerville-30",15)
        mf = createFont("Baskerville-30",25)
        bf = createFont("Baskerville-30",40)
    
    def updateTime(self):
        global time
        
        time += 1
    
    #buttons
    def button1(self,xpos,ypos,xsize,ysize):
        global time
        
        if xpos - xsize/2 < mouseX < xsize/2 + xpos and ypos - ysize/2 < mouseY < ysize/2 + ypos:
            fill(255,240,180)
            if mousePressed:
                if time > 15:
                    time = 0
                    return True
        else:
            fill(255)
        stroke(0)
        rect(xpos,ypos,xsize,ysize,8)

    def button2(self,xpos,ypos,xsize,ysize,on):
        global time
        
        if xpos - xsize/2 < mouseX < xsize/2 + xpos and ypos - ysize/2 < mouseY < ysize/2 + ypos:
            fill(255,240,180)
            if mousePressed:
                if time > 15:
                    time = 0
                    return True
        else:
            if on:
                fill(255,220,51)
            else:
                fill(255)
        stroke(0)
        rect(xpos,ypos,xsize,ysize,8)
    
    def button3(self,xpos,ypos,xsize,ysize):
        global time
        
        if xpos - xsize/2 < mouseX < xsize/2 + xpos and ypos - ysize/2 < mouseY < ysize/2 + ypos:
            if mousePressed:
                if time > 15:
                    time = 0
                    return True
    
    def passKey(self,Key):
        global currentKey, newKey
        currentKey = Key
        newKey = True
        
    


class Login():
    def __init__(self):
        global usernames,password,email,usernamesAndPasswords
        
        self.tempUsername = ''
        self.tempPassword = ''
        usernames = []
        aausernames = []
        self.addTo = ''
        self.showPassword = False
        
        usernamesAndPasswords = open("usernamesAndPasswords.txt", "r+")
        
        
        aausernames = usernamesAndPasswords.readline().split('&&')
        
        for i in aausernames:
            usernames.append(i.split(','))
        
        
    
    def display(self):
        global newKey,currentKey,changePageTo, changePage
        
        fill(255,220,51)
        textFont(mf)
        text("hama",70,50)
        
        fill(0)
        textFont(bf)
        text("Login",250,150)
        
        fill(0)
        textFont(sf)
        text("username",100,300)
        text("password",100,390)
        
        if Main('l').button1(250,330,400,40):
            self.addTo = 'u'
        if Main('l').button1(250,420,400,40):
            self.addTo = 'p'
        if Main('l').button2(195,480,30,30,self.showPassword):
            self.showPassword = not self.showPassword
        if Main('l').button1(250,580,200,40):
            self.checkForPasswordAndUsername()
        if Main('l').button3(250,695,150,30):
            changePage = True
            changePageTo = 's'
            
        
        if newKey:
            if self.addTo == 'u':
                if currentKey == '':
                    self.tempUsername = self.tempUsername[:-1]
                elif currentKey == 65535:
                    pass
                elif currentKey == '''
''':
                    self.checkForPasswordAndUsername()
                else:
                    self.tempUsername += currentKey
            elif self.addTo == 'p':
                if currentKey == '':
                    self.tempPassword = self.tempPassword[:-1]
                elif currentKey == 65535:
                    pass
                elif currentKey == '''
''':
                    self.checkForPasswordAndUsername()
                else:
                    self.tempPassword += currentKey
            
            newKey = False
        
        
        fill(34, 0, 204)
        text("New? Sign in here",250,700)
        
        fill(0)
        textFont(sf)
        text(self.tempUsername,250,335)
        if self.showPassword:
            text(self.tempPassword,250,425)
        else:
            text(len(self.tempPassword) * '*',250,425)
        text('show password?',280,485)
        textFont(mf)
        text('Enter',250,590)
    
    def checkForPasswordAndUsername(self):
        global changePage, changePageTo,userLogin
    
        
        for user in usernames:
            if self.tempUsername == user[0] and self.tempPassword == user[1]:
                changePage = True
                changePageTo = 'h'
                userLogin = user


class SignIn():
    def __init__(self):
        self.tempUsername = ''
        self.tempPassword = ''
        self.tempEmail = ''
        self.addTo = ''
        self.showPassword = False
    
    def display(self):
        global newKey,currentKey
        
        fill(0)
        textFont(bf)
        text("Sign In",250,150)
        
        fill(0)
        textFont(sf)
        text("username",100,300)
        text("password",100,390)
        text("email",100,520)
        text('show password?',280,485)
        
        if Main('l').button1(250,330,400,40):
            self.addTo = 'u'
        if Main('l').button1(250,420,400,40):
            self.addTo = 'p'
        if Main('l').button1(250,550,400,40):
            self.addTo = 'e'
        if Main('l').button1(250,615,200,40):
            self.changePasswordAndUsername()
        if Main('l').button2(195,480,30,30,self.showPassword):
            self.showPassword = not self.showPassword
        
        
        if newKey:
            if self.addTo == 'u':
                if currentKey == '':
                    self.tempUsername = self.tempUsername[:-1]
                elif currentKey == 65535:
                    pass
                elif currentKey == '''
''':
                    self.changePasswordAndUsername()
                else:
                    self.tempUsername += currentKey
            
            elif self.addTo == 'p':
                if currentKey == '':
                    self.tempPassword = self.tempPassword[:-1]
                elif currentKey == 65535:
                    pass
                elif currentKey == '''
''':
                    self.changePasswordAndUsername()
                else:
                    self.tempPassword += currentKey
            
            elif self.addTo == 'e':
                if currentKey == '':
                    self.tempEmail = self.tempEmail[:-1]
                elif currentKey == 65535:
                    pass
                elif currentKey == '''
''':
                    self.changePasswordAndUsername()
                else:
                    self.tempEmail += currentKey
            
            newKey = False
        
        
        
        fill(0)
        textFont(sf)
        text(self.tempUsername,250,335)
        text(self.tempEmail,250,555)
        if self.showPassword:
            text(self.tempPassword,250,425)
        else:
            text(len(self.tempPassword) * '*',250,425)
        textFont(mf)
        text('Enter',250,625)
    
    def changePasswordAndUsername(self):
        global usernames
        global changePage, changePageTo,usernamesAndPasswords
        
        changePage = True
        changePageTo = 'l'
        
        
        usernamesAndPasswords.write("&&{U},{P},{E}".format(U = self.tempUsername, P = self.tempPassword, E = self.tempEmail))
        
        usernamesAndPasswords.close()
        
        Login()
        
        print(usernamesAndPasswords.readline())



class Home():
    def __init__(self):
        pass
    
    def display(self):
        global changePage, changePageTo
        
        fill(0)
        textFont(bf)
        text("Home",250,150)
        
        
        if Main('h').button1(250,330,400,40):
            changePage = True
            changePageTo = 'p'
        if Main('r').button1(250,400,400,40):
            changePage = True
            changePageTo = 'r'
        
        
        fill(0)
        textFont(sf)
        text('Profile',250,335)
        text('Restaurants',250,405)



class Profile():
    def __init__(self):
        self.showPassword = False
    
    def display(self):
        global userLogin,changePage,changePageTo
        
        fill(0)
        textFont(bf)
        text("Profile",250,150)
        
        textFont(sf)
        text('show password?',305,345)
        
        if Main('l').button2(220,340,30,30,self.showPassword):
            self.showPassword = not self.showPassword
        
        if Main('l').button1(50,50,30,30):
            changePage = True
            changePageTo = 'h'
    
            
        fill(0)
        textAlign(LEFT)
        textFont(sf)
        text('username: ' + userLogin[0], 50,300)
        if self.showPassword:
            text('password: ' + userLogin[1],50,350)
        else:
            text('password: ' + '*'*len(userLogin[1]),50,350)
        text('email: ' + userLogin[2],50,400)
        
        textAlign(CENTER)
        
        

class Restaurants():
    def __init__(self):
        self.restaurantlist = ['Makoto','Temakeria & Cia.','Mago','Kitchin','Adega Santiago','Poke House','Cabana Burger','Le Petit Gabriele','Peixaria da Vila','Casa do Maceira']
        
        for restaurant in self.restaurantlist:
            restaurantObj.append(RestaurantPage(restaurant))
        
        
        
    def display(self):
        global changePage, changePageTo
        
        fill(0)
        textFont(bf)
        text("Restaurants",250,130)
        
        
        if Main('r').button1(50,50,30,30):
            changePage = True
            changePageTo = 'h'
        
        for i in range(10):
            if Main('r').button1(250,210 + i*60,400,40):
                changePage = True
                changePageTo = i
        
        for i in range(len(self.restaurantlist)):
            fill(0)
            textFont(sf)
            text(self.restaurantlist[i],250,215+i*60)
        


class RestaurantPage():
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(self.name)

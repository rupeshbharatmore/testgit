#oops project
class user(object):
  def __init__(self,name = '',no = '' ,date = '',noofseats = ''):
    self.name = name
    self.no = no
    
    
    self.date = date
    
    
    self.noofseats = noofseats
    
  @property
  def no(self):
    return self.__no
  @no.setter
  def no(self,no):
    if(len(no)== 10):
      self.__no = no
    else:
      print("invalid no")
  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self,name):
    if(name!=None and len(name)>0):
      self.__name = name
    else:
      print("invalid name")
  def display(self):
    print("display user info")
    print(self.name)
    print(self.no)
    
    print(self.movie)
    print(self.date)
class second(object):
  list =[]
  a = 0
  d = 0
  
    
  @staticmethod   
  def booking():
    
      
    print("entered into booking option to watch latest movies")
    print("plz note that this application is limited to pune city only")
    name = input("enter your name")
    print("plz note you cannot enter date of next week")
    no = int(input("enter no"))
    date = input("enter the movie you want")
    noofseats = int(input("enter no of seats you want"))
    second.d = noofseats
    
    print("the available no of theatres in pune")
    #file
    if(ch == 1 or ch == 2 or ch == 3 or ch == 4):
      print("showtimings of particular day are")
      #file
    second.a = input("plz select anyone of these timings click no in front of it")
    if(second.a == 1 or second.a == 2 or second.a == 3 or second.a == 4):
      print("now here plz enter into payment method")
    if(len(second.list)<= 50):
      second.list.append(name,no,date,noofseats)
    else:
      print("only"+str(50 - len(second.list))+"are available for booking")
  def payment():
    
    
    print("enter way you like to  watch"+"1 for 2d"+"2 for 3d")
    f = int(input("enter"))
    print("total amount generated after booking given no of seats")
    second.d = int(input("enter noofseats"))
    if(f == 2):
      a = second.d*300
      print(second.d*300)
    if(f == 1):
      a = second.d*200
      print(second.d*200)
    print("plz note that payment meathod accpted is by debit card")
    v = int(input("enter card no without underscore"))
    c= int(input("enter cvv"))
    g = int(input("enter an amount which is shown you upper"))
    if(g ==  a):
      print("payment has been done successfully")
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Emailsender(user,second):
  def __init__(self,message,sub,sender,reciever,name,no,date, movie ,noofseats):
    super(Emailsender,self). __init__(name,no,date,movie,noofseats)
    email = "rupeshbharatmore@gmail.com"
    password = "sharvari"
    self.message = message
    self.sub = sub
    self.sender = sender
    self.reciever = reciever
    self.email = email
    self.password = password
  def getmsg(self):
    msg = MIMEMultipart()
    msg['from']= self.sender
    msg['to'] = self.reciever
    msg['subject'] = self.sub
    msg.attach(MIMEText(self.message,'plain'))
    return msg
  def sendmail(self):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.ehlo()
    server.login(self.email,self.password)
    text = self.getmsg().as_string()
    server.sendmail(self.email,self.reciever,text)
    server.quit()


    

      
    
    
    
    
    
    
    
      
    
      
      
    
    
    
    
    
    
    
    
    
    
  
def main():
  
  
    print "Trending movies"
    print "1. Batti Gul Meter Chalu"
    print "2. Stree"
    print "3. Sui Dhaaga - Made in India"
    print "4. Gold"
    print "5. Paltan"
    print "6. Exit"


    while True:
        choice=input("Please select the movie : ")
        if choice==1:
            try:
                fh=open("Batti_Gul_Meter_Chalu.txt","r")
            except IOError:
                print "file not found"
            else:
                print fh.read()
                fh.close()

        elif choice==2:
            try:
                fh=open("Stree.txt","r")
            except IOError:
                print "file not found"
            else:
                print fh.read()
                fh.close()

        elif choice==3:
            try:
                fh=open("Sui_Dhaaga.txt","r")
            except IOError:
                print "file not found"
            else:
                print fh.read()
                fh.close()

        elif choice==4:
            try:
                fh=open("Gold.txt","r")
            except IOError:
                print "file not found"
            else:
                print fh.read()
                fh.close()

        elif choice==5:
            try:
                fh=open("Paltan.txt","r")
            except IOError:
                print "file not found"
            else:
                print fh.read()
                fh.close()

        elif choice==6:
            break
        print("now its time for booking")
        print("for booking purpose"+"print 1")
        em = Emailsender(msg,"new","rupesh more",input("enter your emailid again"))
      
        a  = int(input("enter"))
        if(a == 1):
          em.booking()
        else:
          break
        name = input("enter")
        for stu in second.list:
          if(stu.name == name):
            msg = stu.display()
        else:
          print("invalidchoice")
        print("now is time for payment")
        em.payment()
        em.sendmail()
      
      


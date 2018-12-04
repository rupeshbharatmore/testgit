class user(object):
  def __init__(self,name = '',no = '' ,date = '',no_of_seats = '',movie='',theatre=''):
    self.name = name
    self.no = no


    self.date = date


    self.no_of_seats = no_of_seats
    self.movie=movie
    self.theatre=theatre


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

    print(self.no_of_seats)
    print(self.date)
import easygui
class Movie_Booking(object):
    list =[]
    a = 0
    d = 0
    c = 0
    date=0
    mov = 0
    theatre = 0

    @staticmethod
    def Movies():
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
                    Movie_Booking.mov="Batti_Gul_Meter_Chalu"
                    
                    break

            elif choice==2:
                try:
                    fh=open("Stree.txt","r")
                except IOError:
                    print "file not found"
                else:
                    print fh.read()
                    fh.close()
                    Movie_Booking.mov = "Stree"
                    break

            elif choice==3:
                try:
                    fh=open("Sui_Dhaaga.txt","r")
                except IOError:
                    print "file not found"
                else:
                    print fh.read()
                    fh.close()
                    Movie_Booking.mov = "Sui_Dhaaga"
                    break
            elif choice==4:
                try:
                    fh=open("Gold.txt","r")
                except IOError:
                    print "file not found"
                else:
                    print fh.read()
                    fh.close()
                    Movie_Booking.mov = "Gold"
                    break
            elif choice==5:
                try:
                    fh=open("Paltan.txt","r")
                except IOError:
                    print "file not found"
                else:
                    print fh.read()
                    fh.close()
                    Movie_Booking.mov = "Paltan"
                    break
            elif choice==6:
                break

##            else:
##                print "Please enter valid choice..."
##                obj.theatre()


    @staticmethod
    def theatre():
        print("Available no of theatres in pune")
    #file
        m = {1:"Cinepolis",2:"Amenora",3:"INOX",4:"PVR",5:"Mangala",6:"back"}
        print "1.Cinepolis\n2.Amenora\n3.INOX\n4.PVR\n5.Mangala\n6.Back\n7.Exit"
        while True:
            ch=input("Select Theatre : ")
            Movie_Booking.theatre = m[ch]
            if ch==1:
                f=open("Cinepolis.txt","r")
                print f.read()
                f.close()
                break
            elif ch==2:
                f=open("Amenora.txt","r")
                print f.read()
                f.close()
                break
            elif ch==3:
                f=open("INOX.txt","r")
                print(f.read())
                f.close()
                break
            elif(ch == 4):
                f = open("PVR.txt","r")
                print(f.read())
                f.close()
                break
            elif(ch == 5):
                f = open("Mangala.txt","r")
                f.read()
                f.close()
                break
            elif ch == 6:
                if __name__ == '__main__':
                  main()
                break
            elif ch == 7:
                break


    @staticmethod
    def Timings():
        print("\nplz note you cannot enter date of next week")
        Movie_Booking.date = raw_input("enter date for the show: ")
        print "Available Show Timings are: "
        print "1. 8:30\n2. 11:30\n2. 3.00\n4. 7.00\n5. Back\n6. Exit"
        s = {1:"8:30",2:"11:30",3:"3.00",4:"7.00",5:"back"}

        while True:
            ch = input("Select timings: ")
            if ch==1 or ch==2 or ch==3 or ch==4:
                Movie_Booking.a=ch
                Movie_Booking.c = s[ch]
                break
            elif ch==5:
                Movie_Booking.theatre()
                break
            elif ch==6:
                break


    @staticmethod
    def booking():


        
        no_of_seats = int(input("enter no of seats: "))
        
        name = raw_input("enter your name : ")
        no = raw_input("enter mobile no: ")
        Movie_Booking.d = no_of_seats


        if(len(Movie_Booking.list)< 3):
          Movie_Booking.list.append(user(name,no,Movie_Booking.date,no_of_seats,Movie_Booking.mov,Movie_Booking.theatre))
        else:
          print("only"+str(3 - len(Movie_Booking.list))+"are available for booking")


    @staticmethod
    def payment():
        
            f = input("\nAvailable viewing modes: \n1. 2D \n2. 3D\nSelect the mode : ")
      
            if(f == 2):
              a = Movie_Booking.d*300
              print("Total amount payable: ",Movie_Booking.d*300)
            if(f == 1):
              a = Movie_Booking.d*200
              print("Total amount payable: ",Movie_Booking.d*200)
            ch = input("\n1.Proceed for payment\n2.back\n3.Exit\nenter your choice:")
            while True:
              if(ch == 1):   
                  print("\nplz note that payment meathod accpted is by debit card")
                  v = raw_input("enter card no(without underscore): ")
                  print ("enter your cvv in password box: ")
                  password = easygui.passwordbox()
                  break

                  print("payment has been done successfully...")
              elif(ch == 2):
                  if __name__ == '__main__':
                    main()
                  

              elif(ch == 3):
                  break
                
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Emailsender(object):
  def __init__(self,message,sub,sender,reciever):

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

        obj=Movie_Booking()
        obj.Movies()
        book=raw_input("Book Movie (y/n) : ")
        if book== "y":
            obj.theatre()
        else:
            obj.Movies()
        obj.Timings()
        obj.booking()
        obj.payment()
        no  = raw_input("\nenter your mobile no for verification: ")
        for stu in Movie_Booking.list:
            if(stu.no == no):
                
                msg = "\nCustomer Details:\n""Name: "+stu.name +"\n"+"Mobile no: "\
                      +stu.no+"\n"+"\nBooking Details:\n"+\
                      "movie book BY YOU:"+" "+stu.movie+"\n"+"date:"+stu.date+"\n"+"no_of_seats:"+str(stu.no_of_seats) +\
                      "\nshowtimingis:"+Movie_Booking.c +"\nTheatre: "+stu.theatre+"\nThank you for using our app..."
                print msg
            else:
              msg = "you have not booked ticket yet"
        
        e =Emailsender(msg,"movie booking mail","Movie Booking app",raw_input("\nenter your email to get ticket.. "))
        e.sendmail()


if __name__ == '__main__':
    main()

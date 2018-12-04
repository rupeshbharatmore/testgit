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
class Movie(object):
  list =[]
  a = 0
  d = 0


  @staticmethod
  def booking():

    print("Available no of theatres in pune")
    #file

    print "1.Cinepolis\n2.Amenora\n3.INOX\n4.PVR\n5.Mangala"
    ch=input("Select Theatre : ")
    if ch==1:
        f=open("Cinepolis.txt","r")
        print f.read()
        f.close()

    elif ch==2:
        f=open("Amenora.txt","r")
        print f.read()
        f.close()
    elif ch==3:
        f=open("INOX.txt","r")
        print(f.read())
        f.close()
    elif(ch == 4):
        f = open("PVR.txt","r")
        print(f.read())
        f.close()
    elif(ch == 5):
        f = open("Mangala.txt","r")
        f.read()
        f.close()

    date=input("Enter date: ")
    print "Select timings : "
    print "1. 8:30\n2. 11:30\n2. 3.00\n 4. 7.00"


##    print("plz note that this application is limited to pune city only")
##    name = input("enter your name")
##    print("plz note you cannot enter date of next week")
##    no = int(input("enter no"))
##    date = input("enter the movie you want")
##    noofseats = int(input("enter no of seats you want"))
##    second.d = noofseats


##    print("showtimings of particular day are")
##    print "Select timings : "
##    print "1.8.30\n2"
    second.a = input("plz select anyone of these timings click no in front of it")
    if(second.a == 1 or second.a == 2 or second.a == 3 or second.a == 4):
      print("now here plz enter into payment method")
    if(len(second.list)< 50):
      second.list.append(user(name,no,date,noofseats))
    else:
      print("only"+str(50 - len(second.list))+"are available for booking")




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
        obj=Movie()
        obj.booking()

if __name__ == '__main__':
    main()
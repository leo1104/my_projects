from os import system


class book_details:
     def __init__(self,bookname,price):
        self.bookname=bookname
        self.price=price


class library:
    def __init__(self):
        self.book_list=[]
        self.book_list_cost_less_than_500=[]
    def getdata(self):
        system("cls")
        while(1):
            system("cls")
            bookname=input("\nEnter the name of the book : ")
            price=int(input("Enter price of the book : "))
            obj_of_book=book_details(bookname,price)
            self.book_list.append(obj_of_book)
            ch=input("\nDo you want to enter more details (y/n) : ")
            if(ch=='y' or ch=='Y'):
                continue
            else:
                break
    
    def display_all(self):
        system("cls")
        print("---------------------------")
        print(": ||BOOK NAME||\t||PRICE|| :")
        print("---------------------------")
        for i in range(len(self.book_list)):
            print(": ","{:12}".format(self.book_list[i].bookname),"  ₹","{:04}".format(self.book_list[i].price)," :")
        print("---------------------------")
        input("\nPress Enter to continue...")
#in above code , used format function , see the visible difference in o/p
             
    #note this will follow LIFO
    def delete_duplicate(self):
        system("cls")
        self.counter=len(self.book_list)
        for i in range(0,self.counter):
            for j in range(i+1,self.counter): #here i have started the loop from i+1 to avoid clash with itself
                if(self.book_list[i].bookname==self.book_list[j].bookname):
                    self.book_list.pop(j)
                    self.counter-=1
        self.display_all() #this displays the updated list


#bubble sort is used here
    def sort_ascending(self):
        system("cls")
        self.n=len(self.book_list)
        for i in range(len(self.book_list)):
            for j in range(0,self.n-i-1):
                if(self.book_list[j].price>self.book_list[j+1].price):
                    (self.book_list[j].bookname,self.book_list[j+1].bookname)=(self.book_list[j+1].bookname, self.book_list[j].bookname)
                    (self.book_list[j].price,self.book_list[j+1].price)=(self.book_list[j+1].price, self.book_list[j].price)
        print("List after sorting the list in ascending order (based on price) :: ")
        self.display_all()
        


    def less_than_500(self):
        system("cls")
        self.count=0
        self.temp_list=[]
        self.n=len(self.book_list)
        for i in range(len(self.book_list)):
            if(self.book_list[i].price>=500):
                self.count+=1
            else:
                temp_name=self.book_list[i].bookname
                temp_price=int(self.book_list[i].price)
                temp_object=book_details(temp_name,temp_price)
                self.book_list_cost_less_than_500.append(temp_object)
        print("\nNumber of books with price more than ₹500 is : ",self.count,"\n\nNew list with books of proice less than ₹500 is :: \n")
        print("---------------------------")
        print(": ||BOOK NAME||\t||PRICE|| :")
        print("---------------------------")
        for i in range(len(self.book_list_cost_less_than_500)):
            print(": ","{:12}".format(self.book_list_cost_less_than_500[i].bookname),"  ₹","{:04}".format(self.book_list_cost_less_than_500[i].price)," :")
        print("---------------------------")
        input("\nPress Enter to continue...")


        

if(__name__=="__main__"):
    system("cls")
    Library_1=library() #main object created
    choice=1
    while(choice):
        system("cls")
        print("1. Enter new books data")
        print("2. Dispaly all books")
        print("3. Remove Duplicate entries and display the updated data")
        print("4. Sort and display book`s data based in ascending order of price and display the sorted data")
        print("5. Display books with cost less than 500 and number of books of cost more than 500")
        print("0. Exit")
        choice=int(input("choose a option :: "))

        if(choice==1):
            Library_1.getdata()
        elif(choice==2):
            Library_1.display_all()
        elif(choice==3):
            Library_1.delete_duplicate()
        elif(choice==4):
            Library_1.sort_ascending()
        elif(choice==5):
            Library_1.less_than_500()
        else:
            continue
        
    
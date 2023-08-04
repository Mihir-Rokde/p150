from tkinter import*
import random
root=Tk()
root.title("Country capitals")
root.geometry("500x500")

country=Entry(root)
country.place(relx=0.5,rely=0.2,anchor=CENTER)
capital=Entry(root)
capital.place(relx=0.5,rely=0.3,anchor=CENTER)
countrylist=Label(root)
capitallist=Label(root)
randomcountrylist=Label(root)
randomcapitallist=Label(root)
c1=[]
c2=[]
def countrycitylist():
    c3=country.get()
    c1.append(c3)
    randomcountrylist["text"]="country name : "+str(c1)
    
    c4=capital.get()
    c2.append(c4)
    randomcapitallist["text"]="city name : "+str(c2)
def randomcountrycity():
    l1=len(c1)
    rn1=random.randint(0,l1-1)
    rc=c1[rn1]
    randomcountrylist["list"]="random country : "+str(rc)
    
    l2=len(c2)
    rn2=random.randint(0,l2-1)
    rca=c2[rn2]
    randomcapitallist["list"]="random city : "+str(rca)
btn=Button(root,text="display country and city name ",command=countrycitylist())
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

btn1=Button(root,text="display country and city name randomly",command=randomcountrycity())
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)
countrylist.place(relx=0.5,rely=0.5,anchor=CENTER)
capitallist.place(relx=0.5,rely=0.6,anchor=CENTER)
randomcountrylist.place(relx=0.5,rely=0.8,anchor=CENTER)
randomcapitallist.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()
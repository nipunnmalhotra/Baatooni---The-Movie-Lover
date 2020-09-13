# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:02:16 2020

@author: nipunn
"""
#for help page
"""


"""

from nltk.chat.util import Chat
import webbrowser as web
import re
import random
import tkinter as tk
import textwrap as fit
from PIL import ImageTk as img
from PIL import Image as open_img
import smtplib



"""
The class Chat in NLTK considers only two elements in pairs but I made this class
so that the working of chatbot can be handled where a function is required to be called.
This class takes the question asked by the user , returns a response and also calls a function
if required.
"""
class Baatooni(Chat):

    def __init__(self, pairs, reflections):
        
       
        self._pairs = [(re.compile(x, re.IGNORECASE), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def respond(self, str):
        found=False
        
        for (question, response, func) in self._pairs:
            match = question.match(str)

            if match:
                found=True
                ans = random.choice(response)
                ans = self._wildcards(ans, match)

                
                if func: 
                    res=func(match)
                    if res and res=="I dont know this?":
                        return res
                
                
                return ans
        
        if ~found:
            return "I dont know this?"
                
#This function searches the required data on google,youtube or wikipedia.
def openit(match):
    groups=match.groups()
    if groups[1] == "wiki":
#        print("Searching")
        web.open("https://en.wikipedia.org/wiki/"+str(groups[0]))
    elif groups[1]=="youtube":
        query=groups[0]
#        print("Playing "+query+" on Youtube")
        query.replace(" ","+")
        web.open("https://www.youtube.com/results?search_query="+query)
    elif groups[1]=="google":
#        print("Searching")
        query=groups[0].replace(" ","+")
        web.open("https://www.google.com/search?q="+query+
                 "&oq=s &aqs=chrome.0.69i59l3j69i57j0l4.1622j0j8&sourceid=chrome&ie=UTF-8")
    else:
        return "I dont know this?"


#This function mails feedback directly to my thapar email id.
def store(screen,name,email,feedback,appPass,receiver):
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    #print(str(feedback))
    email=str(email)
    s.login(email,appPass)
#    message="Name: "+str(name)+"\n"+"Feedback: "+str(feedback)
    s.sendmail(email, receiver,feedback)
    s.quit()
    screen.destroy()


#This fuction is required to construct feedback window for getting feedback information.
def feedback():
#    print("Welcome to Feedback Bar,Please fill the form")
    screen=tk.Toplevel(main_screen)
    screen.title("Feedback Form")
    screen.geometry("500x460")
    screen.configure(background="gray")
    tk.Label(screen,text="Fill the form",fg="DarkGoldenRod3",font=("Times New Roman",15)).place(x=200,y=0)
    #tk.Label().pack() #Dummy Label
    
    #Name Label and text box
    name=tk.StringVar()
    tk.Label(screen,text="Name: ",font=("Times New Roman",15),fg="blue").place(x=150,y=40)
    
    name_box=tk.Entry(screen,textvariable=name,width=15,fg="blue",highlightcolor="black",font=("Times New Roman",15))
    name_box.place(x=220,y=40)
    
    #Email ID label and text box
    
    email=tk.StringVar()
    tk.Label(screen,text="Email ID: ",font=("Times New Roman",15),fg="blue").place(x=122,y=80)
    
    email_box=tk.Entry(screen,textvariable=email,width=15,fg="blue",highlightcolor="black",font=("Times New Roman",15))
    email_box.place(x=220,y=80)
    
    #Feedback and text box
    
   
    tk.Label(screen,text="Message: ",font=("Times New Roman",15),fg="blue").place(x=122,y=120)
    
    message_box=tk.Text(screen,width=15,height=5,fg="blue",highlightcolor="black",font=("Times New Roman",15))
    message_box.place(x=220,y=120)
    tk.Label(screen,text="Password: ",font=("Times New Roman",15),fg="blue").place(x=122,y=250)
    appPass=tk.StringVar()
    appPass_box=tk.Entry(screen,textvariable=appPass,show='*',width=15,fg="blue",highlightcolor="black",font=("Times New Roman",15))
    appPass_box.place(x=220,y=250)
    receiver=tk.StringVar()
    tk.Label(screen,text="Receiver: ",font=("Times New Roman",15),fg="blue").place(x=122,y=290)
    receiver_box=tk.Entry(screen,textvariable=receiver,width=15,fg="blue",highlightcolor="black",font=("Times New Roman",15))
    receiver_box.place(x=220,y=290)
    #Send button
    send_button=tk.Button(screen,activebackground="pink",width=10,font=("Times New Roman",15),
                          activeforeground="red",bg="maroon4",fg="lightgrey",text="Send"
                          ,command=lambda : store(screen,name.get(),email.get(),message_box.get("1.0",tk.END),appPass.get(),receiver.get()) )
    
    send_button.place(x=220,y=340)
    
    tk.Label(screen,text="We dont track your password and only use it \n to send email",
             font=("Times New Roman",15),fg="blue").place(x=122,y=400)
    
    screen.mainloop()
    
#This function helps in giving the information about chatbot.
def helpPage():
    page=tk.Toplevel(main_screen)
    page.title("Help Page")
    page.geometry("650x200")
    page.configure(background="gray")
    tk.Label(page,text="Welcome to the Help Page",fg="DarkGoldenRod3",font=("Times New Roman",15)).place(x=150,y=0)
    tk.Label(page,text="Aa gya hai aapka dost Baatooni\n Mai bohot Kaam ka hu,Following is the list:"+
        "\n1. I can make you laugh\n2. I can search on wikipedia or google"+
        " type \"search (your query) on wiki/google\" "+
        "\n3. Play videos on youtube type \"play (your query) on youtube\" "+
        "\n4. You can chat with me all the time" +
        ",that was what I was made for(pun intended)",font=("Arial Black",10),justify=tk.LEFT).place(x=20,y=40)
    page.mainloop()


#Basic reflections to be used(same as in NLTK)
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you",
  "Aap"        : "Tum",
  "Aapka"      : "Mera"
}

"""
Pairs can be used to get responses.
This is the format for my pairs:
    [ r"Question",[Answer(s)],function(if to be used)]

"""

pair1=[[
        r"my name is (.*)|My name is (.*)",
        ["Hello %1, How are you today ?"],None
    ],
        ["what is your name ?",
        ["I am Batooni-The Movie Lover (Naam to Suna Hoga)" ],openit],
    ]



pairs = [
    [
        r"my name is (.*)|My name is (.*)",
        ["Hello %1, How are you today ?"],None
    ],
     [
        r"what is your name ?",
        ["I am Batooni-The Movie Lover (Naam to Suna Hoga)"],None
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",],None
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",],None
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",],None
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],None
    ],
    [
        r"(.*) age ?",
        ["I am ageless (China wala Chorke)",],None
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",],None
        
    ],
    [
        r"(.*) (created|made) (.*)?",
        ["Nipunn Malhotra created me for his NLP project"],None
    ],
    [
        r"(.*) (location|city) ?",
        ['TIET,Patiala',],None
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always",
         "Too hot man here in %1","Too cold man here in %1","Never even heard about %1"],None
    ],
   
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"],None
    ],
    [
        r"how (.*) health(.*)",
        ["As long as you feed me, I will be happy and healthy",],None
    ],
    [
        r"(.*) (sports|game) ?",
        [ "Gol Guttam Lakad Battam De danadan pratiyogita \n Its cricket for you",],None
    ],
    
    [
        r"who (.*) (moviestar|actor)?|actor",
        ["Sharukh Khan (and I am not a terrorist)"],None
],
    [
        r"quit",
        ["BBye take care. See you soon :) \n Kyuki ye Zindagi Bot lambi hai aur Hmare paas Waqt bohot kam hai",
"It was nice talking to you. See you soon :) \n Kyuki ye Zindagi Bot lambi hai aur Hmare paas Waqt bohot kam hai"]
    ,None],

    [   r"(.*) favourite movie?",
        ["I like every movie, Entertainment,Entertainment aur Entertainment"],None
     ],
    
    [ r"Search (.*) on (.*)",
     [r"Searching.."],openit
     
     ],
    
     [ r"Play (.*) on (.*)",
     ["Playing %1 on %2"],openit
     
     ],

    [
    r"%(.*) send mail|Email|send mail",
    ["%Mail Sent"],None
    ],
     
     [
      r"(.*) good|(.*)fine",
      ["Thats sounds nice"],None
      
      ],
      
      [
       
       r"What (.*) doing|doin",
       ["Just chilling"],None
       
       ],
       
       [
        
        r"(.*) help|help",
        ["Opening Help Page"],None
        ]
      
     
]

#Destroys main screen when user wants to leave the application.
def destroyit():
    main_screen.destroy()


#prints response of the question asked.
def printResponse(screen,chat,text_box):
    text=text_box.get("1.0",tk.END)
    text_box.delete("1.0",tk.END)
    if start:
        start.destroy()
    for i in labels:
        if i:
            i.destroy()
    fitter=fit.TextWrapper(width=40)
    img_person=open_img.open("person.png")
    img_person=img_person.resize((40,20))
    img_person=img.PhotoImage(img_person)
    img_bot=open_img.open("bot.png")
    img_bot=img_bot.resize((40,20))
    img_bot=img.PhotoImage(img_bot)
    response=chat.respond(text)
    text=fitter.fill(text=text)
    response=fitter.fill(text=response)
    photolabel1=tk.Label(main_screen,image=img_person)
    label1=tk.Label(main_screen,text=text,font=("Times New Roman",10),bg="navy",fg="white")
    labels.append(label1)
    photolabel1.image=img_person
    photolabel1.place(x=2,y=2)
    label1.place(x=48,y=4)
    photolabel2=tk.Label(main_screen,image=img_bot)
    label2=tk.Label(main_screen,text=response,font=("Times New Roman",10),bg="navy",fg="white")
    labels.append(label2)
    photolabel2.image=img_bot
    photolabel2.place(x=536,y=70)
    label2.place(x=580,y=70)
   
    if "send mail" in text.lower() or "email" in text.lower():
        feedback()
    elif "help" in text.lower():
        helpPage()
    if  text.lower()=="quit":
        main_screen.after(700,destroyit)


#Helps in talking with the chatbot.
def talk(chat):
    main_screen.geometry("800x210")
    main_screen.title("Batooni-The Movie Lover")
    main_screen.configure(background="gray")
    
    start.place(x=2,y=2)
   
    
    text_box=tk.Text(main_screen,width=70,height=2,bg="white",fg="black")
    text_box.place(x=2,y=160)
    
    send_button=tk.Button(main_screen,fg="lightgrey",bg="maroon4",activeforeground="black",height=1,width=27,text='Send',
                          font=("Calibri",12),command=lambda :printResponse(main_screen,chat,text_box))
    send_button.place(x=570,y=160)
    
    main_screen.mainloop()
   
    


labels=[] #contains all the labels made.
main_screen=tk.Tk() #main screen initialization


#start message
start=tk.Label(main_screen,text="Heyy Welcome to Baatooni-The Movie Lover\nYou can Talk to me about anything"+
              "\nTell me to search anything or play videos on youtube"+
              "\nTo Know more type help and type feedback to give your feeback"+"\nType quit to end"+
              "\nJust dont cry kyuki \"PUSHPA I HATE TEARS\" ",bg="gray",fg="magenta4",borderwidth=2,relief="solid"
              ,font=(10))


#instance of chatbot
chat = Baatooni(pairs,reflections)

#talk with chatbot
talk(chat)

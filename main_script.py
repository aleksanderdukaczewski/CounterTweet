import tweepy
from tkinter import *
import datetime

#read vars

f = open('vars.txt' , 'r')
varlist=f.read().split('\n')
f.close()

consumer_key = varlist[0]
consumer_secret = varlist[1]
access_token = varlist[2]
access_token_secret = varlist[3]
dateToCountdown = varlist[4]

#gui

root = Tk()
label1 = Label( root, text="API key")
E1 = Entry(root, bd =5)
E1.insert(END, consumer_key)
label2 = Label( root, text="API key secret")
E2 = Entry(root, bd =5)
E2.insert(END, consumer_secret)
label3 = Label( root, text="Access token")
E3 = Entry(root, bd =5)
E3.insert(END, access_token)
label4 = Label( root, text="Access token secret")
E4 = Entry(root, bd =5)
E4.insert(END, access_token_secret)
label5 = Label(root, text="Date to count down to (YYYY-MM-DD)")
E5 = Entry(root, bd =5)
E5.insert(END, dateToCountdown)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()

#get values from entry fields

def getE1():
    return E1.get()
def getE2():
    return E2.get()
def getE3():
    return E3.get()
def getE4():
    return E4.get()
def getE5():
    return E5.get()

#save values from entry fields to vars.txt

def saveValues():
    f = open("vars.txt","w")
    f.write(getE1()+'\n'+getE2()+'\n'+getE3()+'\n'+getE4()+'\n'+getE5())
    f.close()
    global consumer_key, consumer_secret, access_token, access_token_secret, dateToCountdown
    consumer_key = getE1()
    consumer_secret = getE2()
    access_token = getE3()
    access_token_secret = getE4()
    dateToCountdown = getE5()


#follow back all of the followers

def followBack():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Followed everyone that is following " + user.name)

#calculate difference
def calculateDateDif():
    date_time_str = str(dateToCountdown) + ' 00:00:00'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    present = datetime.datetime.now()
    global difference
    difference = str((date_time_obj - present).days)


#authenticate credentials with tweepy

def auth():
    auth  tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    api = tweepy.API(auth)

#main function

def mainFunction():
    saveValues()
    calculateDateDif()
    auth()
    followBack()
    api.update_status('There are {number} days left until something great happens!'.format(number=difference))


#save keys and submit buttons

save = Button(root, text ="Save field info", command = saveValues)
save.pack()

submit = Button(root, text ="Tweet", command = mainFunction)
submit.pack()

#run the gui

root.mainloop()

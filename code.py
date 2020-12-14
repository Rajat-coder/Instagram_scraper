import io
from tkinter import *
import tkinter as tk

import PIL.Image
from PIL import ImageTk
import requests,webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen

window=Tk()
window.configure(background="white")
window.title("Instagram Scraper")

window.geometry("1200x600")
window.iconbitmap('./pics/insta.ico') #Title logo
window.resizable(0, 0)

def search():
    try:
        global im5,un
        un = str(txt2.get())
        res = requests.get('https://www.instagram.com/' + un)
        s_data = BeautifulSoup(res.text, 'html.parser')

        ## Fetch DP in system
        insta_dp = s_data.find("meta", property="og:image")
        dp_url = insta_dp.attrs['content']

        u = urlopen(dp_url)
        raw_data = u.read()
        im5 = PIL.Image.open(io.BytesIO(raw_data))
        im5 = im5.resize((150, 150), PIL.Image.ANTIALIAS)


        ## Fetch Info
        ui = s_data.find("meta", property="og:description")
        cont = ui.attrs['content'][:40]
        cont = cont.split(' ')
        follower = cont[0]
        follower = follower.replace('m', 'M')
        following = cont[2]
        # following = int(following.replace(',', ''))
        posts = cont[4]
        followers1 = str(follower)+" Followers"
        following1 = str(following)+" Following"
        posts1 = str(posts)+" Posts"
        followers_label.config(text=followers1)
        following_label.config(text=following1)
        posts_label.config(text=posts1)

        ## Show DP
        image = ImageTk.PhotoImage(im5)
        panel5 = Button(window,image = image, command = check_link,borderwidth=0)
        panel5.image = image
        panel5.pack()
        panel5.place(x=500, y=330)

        im7 = PIL.Image.open('./pics/download.png')
        im7 = im7.resize((40, 40), PIL.Image.ANTIALIAS)
        sp_img7 = ImageTk.PhotoImage(im7)
        panel8 = Button(window, borderwidth=0,command=download_dp, image=sp_img7, bg='white')
        panel8.image=sp_img7
        panel8.pack()
        panel8.place(x=700, y=360)


    except Exception as e:
        print(e)
        lab1 = tk.Label(window, text="ID not found!", width=20, height=1, fg="white", bg="firebrick1",
                        font=('times', 14, ' bold '))
        lab1.place(x=400, y=350)
        window.after(4000, destroy_widget, lab1)

def check_link():
    link = 'https://www.instagram.com/' + un
    webbrowser.open_new_tab(link)

def clear():
    txt2.delete(first=0,last=100)


def download_dp():
    im5.save(un+'.jpg')
    lab1 = tk.Label(window, text="Picture Downloaded!", width=20, height=1, fg="black", bg="gold",
                    font=('times', 14, ' bold '))
    lab1.place(x=400, y=250)
    window.after(4000, destroy_widget,lab1 )

def destroy_widget(widget):
    widget.destroy()

#Label
pred = tk.Label(window, text="Instragram Profile Scrapper", width=30, height=2, fg="white", bg="maroon2",
                font=('times', 25, ' bold '))
pred.place(x=274, y=10)


#Instagram Logo
im=PIL.Image.open("./pics/ig.png")
im=im.resize((150,150),PIL.Image.ANTIALIAS)
wp_img = ImageTk.PhotoImage(im)
panel4 = Label(window, image=wp_img, bg='white')
panel4.pack()
panel4.place(x=500, y=100)


#ID box
lab = tk.Label(window, text="Enter your ID", width=18, height=1, fg="white", bg="maroon2",
               font=('times', 16, ' bold '))
lab.place(x=280, y=280)


#Entry Box
txt2 = tk.Entry(window, borderwidth=7, width=25, bg="white", fg="black", font=('times', 17, ' bold '))
txt2.place(x=550, y=275)


#Search
im1 = PIL.Image.open('./pics/search.png')
im1 = im1.resize((40, 40), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Button(window, borderwidth=0, image=sp_img,command=search, bg='white')
panel5.pack()
panel5.place(x=880, y=275)


#eraser
im2 = PIL.Image.open('./pics/eraser.png')
im2 = im2.resize((40, 40), PIL.Image.ANTIALIAS)
sp_img1 = ImageTk.PhotoImage(im2)
panel6 = Button(window, borderwidth=0, image=sp_img1, bg='white')
panel6.pack()
panel6.place(x=930, y=275)


#Followers , Following , Post
followers_label = tk.Label(window, text='Followers', width=17, height=2, fg="white", bg="maroon2",
                           font=('times', 18, ' bold '))
followers_label.place(x=200, y=500)

following_label = tk.Label(window, text="Following", width=17, height=2, fg="black", bg="spring green",
                           font=('times', 18, ' bold '))
following_label.place(x=470, y=500)

posts_label = tk.Label(window, text="Posts", width=17, height=2, fg="white", bg="dark violet",
                       font=('times', 18, ' bold '))
posts_label.place(x=740, y=500)






window.mainloop()

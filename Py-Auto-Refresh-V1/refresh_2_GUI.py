#Imports
from selenium import webdriver
import time
from tkinter import *
import threading
#Asks for the web adress of the website & interval



root = Tk()
root.resizable(width=False, height=False)
root.title("Auto-Refresher")
icon = PhotoImage(file = ".\Refresh.png")
root.iconphoto(False,icon)
root.configure(bg="black")
paused = False
def submit():
        
        website= website_a.get()
        interval = interval_a.get()
        print(website, interval)
        browser = webdriver.Edge(".\msedgedriver.exe")     #Declares our webdriver that we are using
        browser.get(website)    #Opens the URL
        def refresh_loop():
                while True:
                        browser.refresh()
                        time.sleep(interval)
        thread = threading.Thread(target=refresh_loop, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

        return print("Submit button pressed")
        

def quit_app():
        root.destroy()
website_a= StringVar()
interval_a = IntVar()
Label(root, text = "Enter the url", fg= "white", bg="black").grid(row =0, column= 0, padx= 15, pady= 5)
website_i = Entry(root, width=20, textvariable=website_a).grid(row=1, column = 0,padx= 15, pady= 5)
Label(root, text="Enter the interval time (in seconds)", fg="white", bg="black").grid(row=0, column=1, padx= 15, pady=5)
interval_i = Entry(root, width=20, textvariable=interval_a).grid(row=1, column=1, padx= 15, pady= 5)
Button(root, command=submit, text="Submit", width=60, bg= "green", fg= "white").grid(row = 2, column =0, columnspan=2, padx=15, pady=5)

Button(root, text="Kill Auto Refresher", bg="red", command=quit_app, width=60, fg="white").grid(row=3, column=0, columnspan=2,padx=15,pady=5)
                
root.mainloop()
        

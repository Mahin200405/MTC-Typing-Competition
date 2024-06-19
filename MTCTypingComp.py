import customtkinter
import os
import mysql.connector
import time
from PIL import Image, ImageTk
import webbrowser
import random as r

test = [
    """The quick brown fox jumps over the lazy dog is an English language pangram,
     a sentence that contains all the letters of the alphabet. The phrase is commonly
      used for touch-typing practice, testing typewriters and computer keyboards, 
      displaying examples of fonts, and other applications involving text where the 
      use of all letters in the alphabet is desired. The earliest known appearance of
     the phrase was in The Boston Journal. It was initially considered a good practice
      for writing students. In the age of computers, this pangram is commonly used to 
      display font samples and for testing computer keyboards. In cryptography, it is 
    commonly used as a test vector for hash and encryption algorithms to verify their 
    implementation, as well as to ensure alphabetic character set compatibility. 
    Microsoft Word has a command to autotype the sentence. Google Docs doesn't have 
    this feature, this is why MTC is better than ACM and GDSC.""",

    """Welcome to BITS Pilani Dubai Campus, a premier engineering institute in the
     UAE and the only international campus of BITS Pilani. Established in 2000, we
      have established ourselves as a leader in providing high-quality technical 
      education to students in the UAE and the surrounding region. While staying 
      true to the core values of BITS Pilani, we have adapted to the local 
      environment and gained a reputation as one of the region's top educational 
      institutions. Are you still trying?? Stop!! Bhavya is winning this."""
]
test1 = r.choice(test)

#Database Connectivity : 
mydb = mysql.connector.connect(host="localhost", user="root", password="Mahin123!", database="MTCTyping")
cur = mydb.cursor()
def write_to_database(team_name, speed, accuracy):
        try:
            sql = "INSERT INTO results (name, speed, Accuracy) VALUES (%s, %s, %s)"
            val = (team_name, speed, accuracy)
            cur.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully")
        except Exception as e:
            print("Error:", e)


def mistake(paragraph, userinp):
    error = 0
    for i in range(len(userinp)):
        if i >= len(paragraph) or userinp[i] != paragraph[i]:
            error = error + 1
    error_percent = (error/len(userinp)) * 100
    return round(error_percent, 2)

def speed(time_1, time_2, userinp):
    time_taken = time_2 - time_1
    no_of_minutes = time_taken/60
    words = userinp.split()
    no_of_words = len(words)
    speed = no_of_words/no_of_minutes
    return round(speed)

app = customtkinter.CTk()
app.geometry("600x600")
app.title("MTC Typing Competition")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def button3():
    write_to_database(teamname, sp_str, acc_str)
    app3.destroy()

def button4():
    webbrowser.open_new_tab("https://drive.google.com/drive/folders/1AxgAqFEuCstbP0oMdZ5s9VGAPMBuFyOu")
def button5():
    webbrowser.open_new_tab("https://github.com/AdamJeddy/BigData-Bits-Workshop")
def button6():
    webbrowser.open_new_tab("https://drive.google.com/drive/folders/1-BAHiP3SzPB2oGcL_ik7oJtfVj_06PHc")

def button2():
    global app2
    global app3
    global teamname
    global time_start
    typed_entry = entry2.get()
    time_end = time.time()
    app2.destroy()
    
    app3 = customtkinter.CTk()
    app3.geometry("600x600")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    app3.title("Results")

    sp = speed(time_start, time_end, typed_entry)
    ep = mistake(test1, typed_entry)
    accuracy = 100 - ep

    global sp_str, acc_str
    sp_str = str(sp)
    acc_str = str(accuracy)

    sp_text = "Your speed is: " + str(sp) + " WPM"
    acc_text = "Accuracy : " + str(accuracy) + "%"

    label6 = customtkinter.CTkLabel(master = app3, text = sp_text, font = ("Arial", 20, "bold"), text_color = "deepskyblue")
    label6.place(relx = 0.1, rely = 0.1, anchor = "nw")
    label7 = customtkinter.CTkLabel(master = app3, text = acc_text, font = ("Arial", 20, "bold"), text_color = "deepskyblue")
    label7.place(relx = 0.1, rely = 0.2, anchor = "nw")
    label8 = customtkinter.CTkLabel(master = app3, text = "Good Try, but you ain't winning, Bhavya is", font = ("Arial", 20, "bold"), text_color = "deepskyblue")
    label8.place(relx = 0.1, rely = 0.3, anchor = "nw")
    label9 = customtkinter.CTkLabel(master = app3, text = "You can still check out our other links", font = ("Arial", 20, "bold"), text_color = "deepskyblue")
    label9.place(relx = 0.1, rely = 0.4, anchor = "nw")

    button_4 = customtkinter.CTkButton(master = app3, text = "Data Visualisation Resources", command = button4, hover_color = "cyan", width = 150)
    button_4.place(relx = 0.1, rely = 0.5, anchor = "nw")
    button_5 = customtkinter.CTkButton(master = app3, text = "Big Data Analytics", command = button5, hover_color = "cyan", width = 150)
    button_5.place(relx = 0.1, rely = 0.6, anchor = "nw")
    button_6 = customtkinter.CTkButton(master = app3, text = "VS Code Workshop", command = button6, hover_color = "cyan", width = 150)
    button_6.place(relx = 0.1, rely = 0.7, anchor = "nw")

    button_3 = customtkinter.CTkButton(master = app3, text = "End", command = button3, hover_color = "cyan", width = 80)
    button_3.place(relx = 0.1, rely = 0.9, anchor = "nw")


    app3.mainloop()  


def button1():
    global app
    global app2
    global teamname
    global time_start
    global typed_entry
    teamname = entry.get()
    app.destroy()
    app2 = customtkinter.CTk()
    time_start = time.time()
    app2.geometry("800x800")
    app2.title("Typing Competition")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    label3 = customtkinter.CTkLabel(master = app2, text = "Your test :", font=("Arial", 20, "bold"), text_color="mediumblue")
    label3.place(relx = 0.1, rely = 0.1, anchor = "nw")
    label4 = customtkinter.CTkLabel(master = app2, text=test1, font=("Arial", 15, "italic"), text_color="deepskyblue" )
    label4.place(relx = 0.10, rely = 0.2, anchor = "nw")
    label5 = customtkinter.CTkLabel(master = app2, text = "Your input :", font = ("Arial", 20, "bold"), text_color="mediumblue")
    label5.place(relx = 0.1, rely = 0.5, anchor = "nw")
    time_start = time.time()
    global entry2
    entry2 = customtkinter.CTkEntry(master = app2, placeholder_text="Type here...", width = 600, height= 150, border_width=2, text_color="royalblue", )
    entry2.place(relx = 0.1, rely = 0.6, anchor = "nw")

    button_2 = customtkinter.CTkButton(master = app2, text = "Give Results", command = button2, hover_color = "cyan", width = 80)
    button_2.place(relx = 0.1, rely = 0.8, anchor = "nw")

    app2.mainloop()




image1 = Image.open("logo.jpg")
image1 = image1.resize((200,200))
image1 = ImageTk.PhotoImage(image1)
image_label = customtkinter.CTkLabel(app, image=image1)
image_label.place(relx = 0.1, rely = 0.1, anchor = "nw")
label1 = customtkinter.CTkLabel(master=app, text="WELCOME TO MTC TYPING COMPETITION", font=("Arial",20,"bold"),text_color="deepskyblue")
label1.place(relx=0.10 , rely=0.5 ,  anchor='nw')
label2 = customtkinter.CTkLabel(master=app, text="Enter team name:", font=("Arial",20),text_color="deepskyblue")
label2.place(relx=0.10 , rely=0.6 ,  anchor='nw')
entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter here...")
entry.place(relx=0.1, rely=0.7,  anchor='nw')
button = customtkinter.CTkButton(master = app, text = "Next", command = button1, hover_color = "cyan" , width = 80)
button.place(relx = 0.1, rely = 0.8, anchor = "nw" )


app.mainloop()

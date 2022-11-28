import tkinter as tk
from tkinter import ttk
from main_loop import structure
import tkinter.filedialog
import os
from utils_cv.load import absolut_path

def write_personnal_data(username,personnal_data):
    """writes personnal data to username repository

    Parameters
    ----------
    username: string
        login of user

    personnal_data: dictionnary
        key: email
                str the email
            path
                str path to folder with images

    Returns
    -------      
            """
    raw_personnal_data = open(absolut_path('../UserData/' + username + '/' + username + '.txt'), 'w')
    for key in personnal_data:
            raw_personnal_data.write(str(key)+ '>' + str(personnal_data[key]) + '\n')
    raw_personnal_data.close()

def write_login_data(login_data):
    """writes personnal data to username repository

    Parameters
    ----------
    username: string
        login of user

    personnal_data: dictionnary
        key: email
                str the email
            path
                str path to folder with images

    Returns
    -------      
            """
    with open(absolut_path('../UserData/Users.txt'),'w') as raw_users:
        for key in login_data:
            raw_users.write(str(key)+ '>' + str(login_data[key]) + '\n')

def login_process():
    """deals with login window and processes

    Parameters
    ----------
    Returns
    -------      
            """  
    #Import Data
    print('Importing Data...')
    login_data={}
    with open(absolut_path('../UserData/Users.txt'),'r') as raw_userdata:
        lst_userdata = raw_userdata.read().splitlines() 
        for elem in lst_userdata:
            elem=elem.split('>')
            login_data[elem[0]]=elem[1]

    #Window Setup
    login_window = tk.Tk()
    login_window.title("Fox-B-Gone Login")

    def login_checker(*args):
        """checks if user,password combination exists/is correct and launches main window  """

        boo=False
        Login= Login_text.get()
        Password= Password_text.get()
        try:
            if login_data[Login]==Password:
                boo=True
        except:
            pass

        if boo:
            print("Password correct")
            login_window.destroy()
            main_window_process(Login)
        else:
            incorrect_login()

    def signup_fct():
        """calls signup window with appropriate data"""
        login_window.destroy()
        signup_process(login_data)
        #calls signup_process

    #First Frame
    first_frm = ttk.Frame(login_window)
    first_lbl = ttk.Label(first_frm, text="Username", style="Sample.TLabel")
    Login_var = tk.StringVar(value="")
    Login_text = tk.Entry(first_frm, textvariable=Login_var)
    Password_var = tk.StringVar(value="")
    Password_text = tk.Entry(first_frm,show='*', textvariable=Password_var)
    fourth_lbl = ttk.Label(first_frm, text="Password", style="SampleFour.TLabel")

    #Grids
    first_lbl.grid(row=0, column=0, padx=10, pady=10)
    Login_text.grid(row=0, column=1, padx=10, pady=10)
    Password_text.grid(row=1, column=1, padx=10, pady=10)
    fourth_lbl.grid(row=1, column=0, padx=10, pady=10)

    #Buttons
    second_frm=tk.Frame(login_window)

    continue_button = ttk.Button(second_frm, text="OK", command= login_checker)
    signup_button= ttk.Button(second_frm,text='Sign up', command=signup_fct)
    continue_button.grid(row=0, column=0, padx=10, pady=10)
    signup_button.grid(row=0, column=1, padx=10, pady=10)

    #Packing
    first_frm.pack()
    second_frm.pack()
    login_window.mainloop()

def main_window_process(username):
    """deals with main processes allowing to launch the main loop or launch process for changing settings"""

    #Settings 
    print ('Importing personnal settings...')
    personnal_data={}
    with open(absolut_path('../UserData/' + username + '/' + username + '.txt'),'r') as raw_personnal_data:
        lst_personnal_data = raw_personnal_data.read().splitlines() 
        for elem in lst_personnal_data:
            elem=elem.split('>')
            personnal_data[elem[0]]=elem[1]

    main_window = tk.Tk()
    main_window.title("Welcome " + username)

    
    #to add : probability tolerance


    def launch_fct():
        """Launches main_loop """
        print('Launching...')
        structure(personnal_data['email'],personnal_data['path'])
        email_sent_process()
        

    def settings_fct():
        """launches settings window and closes """
        print('Changing settings...')
        main_window.destroy()
        settings_window_process(username,personnal_data)

    #First Frame
    first_frm = ttk.Frame(main_window)
    first_lbl = ttk.Label(first_frm, text="Path to image directory", style="Sample.TLabel")
    path_lbl = ttk.Label(first_frm, text=personnal_data['path'])


    #Grids Frame 1
    first_lbl.grid(row=0, column=0, padx=10, pady=10)
    path_lbl.grid(row=0, column=1, padx=10, pady=10)


    #Second Frame
    second_frm= ttk.Frame(main_window)
    chgsett_button = ttk.Button(second_frm, text="Change Settings",command=settings_fct)
    launch_button = ttk.Button(second_frm, text='Launch',command=launch_fct)

    #Grids Frame 2
    chgsett_button.grid(row=0, column=0, padx=10, pady=10)
    launch_button.grid(row=0, column=1, padx=10, pady=10)

    #Packing
    first_frm.pack()
    second_frm.pack()
    main_window.mainloop()

def settings_window_process(username,personnal_data):
    """deals with changing settings

    Parameters
    ----------
    username: string
        login of user

    personnal_data: dictionnary
        key: email
                str the email
            path
                str path to folder with images

    Returns
    -------      
            """
    def chg_path_fct():
        """launches window for changing path settings"""
        new_path=tkinter.filedialog.askdirectory(parent=settings_window,initialdir="/",title="Selecting Path")
        personnal_data['path']=new_path
        write_personnal_data(username, personnal_data)

    def chg_email_fct():
        """launches window for changing email settings"""
        change_email_process(username,personnal_data)
    
    def ok_settings_fct():
        """closes settings window and launches main window process"""
        print('OK')
        settings_window.destroy()
        main_window_process(username)
        #calling main window

    def cancel_settings_fct():
        """reverts to personnal data when settings window was called"""
        print('Cancelling...')
        write_personnal_data(username,personnal_data)
        settings_window.destroy()
        main_window_process(username)
        settings_window.destroy()


    settings_window = tk.Tk()
    settings_window.title("Fox-B-Gone settings")

    #First frame
    first_frm = ttk.Frame(settings_window)
    path_button = ttk.Button(first_frm, text="Change Path", command=chg_path_fct)
    path_lbl = ttk.Label(first_frm, text=personnal_data['path'])

    #Griding
    path_button.grid(row=0, column=1, padx=10, pady=10)
    path_lbl.grid(row=0, column=0, padx=10, pady=10)


    #Second Frame
    second_frm= ttk.Frame(settings_window)
    email_button=ttk.Button(second_frm, text='Change Email address',command=chg_email_fct)
    email_lbl= ttk.Label(second_frm,text=personnal_data['email'])

    #Griding
    email_button.grid(row=0, column=1, padx=10, pady=10)
    email_lbl.grid(row=0, column=0, padx=10, pady=10)


    #Third Frame
    third_frm=ttk.Frame(settings_window)
    ok_button=ttk.Button(third_frm,text='OK',command=ok_settings_fct)
    cancel_button=ttk.Button(third_frm,text='Cancel',command=cancel_settings_fct)


    #Griding
    ok_button.grid(row=0, column=0, padx=10, pady=10)
    cancel_button.grid(row=0, column=1, padx=10, pady=10)


    #Packing

    first_frm.pack()
    second_frm.pack()
    third_frm.pack()
    settings_window.mainloop()

def change_email_process(username='user',personnal_data={'email':'','path':''}):
    """deals with changing  email settings

    Parameters
    ----------
    username: string
        login of user

    personnal_data: dictionnary
        key: email
                str the email
            path
                str path to folder with images

    Returns
    -------      """
    
    def email_cancel_fct():
        """closes email changing window"""
        email_window.destroy()


    def email_ok_fct():
        """changes personnal settings according to new email"""
        new_email=email_txt.get()
        personnal_data['email']=new_email
        write_personnal_data(username, personnal_data)
        email_window.quit()
    
    #Window
    email_window=tk.Tk()
    email_window.title("Change Path")

    #Edit
    first_frm=ttk.Frame(email_window)
    email_var = tk.StringVar(value='')
    email_txt = tk.Entry(first_frm, textvariable=email_var)
    email_lbl=tk.Label(first_frm,text='Email')
    email_txt.insert(0, personnal_data['email'])

    #Grid
    email_txt.grid(row=0, column=1, padx=10, pady=10)
    email_lbl.grid(row=0, column=0, padx=10, pady=10)

    #Second Frame
    second_frm=ttk.Frame(email_window)
    ok_button=ttk.Button(second_frm,text='OK',command=email_ok_fct)
    cancel_button=ttk.Button(second_frm,text='Cancel',command=email_cancel_fct)


    #Grid
    ok_button.grid(row=0, column=0, padx=10, pady=10)
    cancel_button.grid(row=0, column=1, padx=10, pady=10)

    #Packing
    first_frm.pack()
    second_frm.pack()
    email_window.mainloop()
    try:
        email_window.destroy()
    except:
        pass
    #use quit and destroy in email_ok_fct so code after is executed when called by signup_process

def incorrect_login():
    """launches incorrect login window"""

    def incorrect_ok_fct():
        """kills incorrect_window """
        incorrect_window.destroy()

    incorrect_window=tk.Tk()
    incorrect_window.title('Incorrect')

    incorrect_lbl=tk.Label(incorrect_window, text='Incorrect Login or password')
    incorrect_btn=tk.Button(incorrect_window,text='ok',command= incorrect_ok_fct)

    incorrect_lbl.pack()
    incorrect_btn.pack()

def signup_process(login_data):

    def ok_signup_fct(*args):
        """closes signup window, writes data and launches login process"""
        print('OK')
        #Getting variables
        new_login=Login_text.get()
        new_password=Password_text.get()
        #writing login daata
        login_data[new_login]=new_password
        write_login_data(login_data)
        #Writing personnal data
        new_personnal_data={}
        new_path=tkinter.filedialog.askdirectory(parent=signup_window,initialdir="/",title="Select path to image directory")
        new_personnal_data['path']=new_path
        os.mkdir(absolut_path('../UserData/'+ new_login))
        write_personnal_data(new_login, new_personnal_data)
        #initialises empty email field to prevent errors with default text
        new_personnal_data['email']=''
        change_email_process(new_login,new_personnal_data)
        signup_window.destroy()
        login_process()
        #calling login window

    def cancel_signup_fct(*args):
        """returns to login window"""
        print("Cancelling...")
        signup_window.destroy()
        login_process()
        #calling login window


    signup_window=tk.Tk()
    signup_window.title('Sign up')

    first_frm = ttk.Frame(signup_window)
    first_lbl = ttk.Label(first_frm, text="Username", style="Sample.TLabel")
    Login_var = tk.StringVar(value="")
    Login_text = tk.Entry(first_frm, textvariable=Login_var)
    Password_var = tk.StringVar(value="")
    Password_text = tk.Entry(first_frm,show='*', textvariable=Password_var)
    fourth_lbl = ttk.Label(first_frm, text="Password", style="SampleFour.TLabel")

    #Grids
    first_lbl.grid(row=0, column=0, padx=10, pady=10)
    Login_text.grid(row=0, column=1, padx=10, pady=10)
    Password_text.grid(row=1, column=1, padx=10, pady=10)
    fourth_lbl.grid(row=1, column=0, padx=10, pady=10)

    #Buttons
    second_frm=tk.Frame(signup_window)

    continue_button = ttk.Button(second_frm, text="OK", command=ok_signup_fct)
    signup_button= ttk.Button(second_frm,text='Cancel', command=cancel_signup_fct)
    continue_button.grid(row=0, column=0, padx=10, pady=10)
    signup_button.grid(row=0, column=1, padx=10, pady=10)

    #Packing

    first_frm.pack()
    second_frm.pack()
    signup_window.mainloop()   

def email_sent_process():
    """launches window when process is done"""

    def email_sent_ok_fct():
        """kills incorrect_window """
        email_sent_window.destroy()

    email_sent_window=tk.Tk()
    email_sent_window.title('Incorrect')

    email_sent_lbl=tk.Label(email_sent_window, text='Email sent with success !')
    email_sent_btn=tk.Button(email_sent_window,text='ok',command= email_sent_ok_fct)

    email_sent_lbl.pack()
    email_sent_btn.pack()

login_process()
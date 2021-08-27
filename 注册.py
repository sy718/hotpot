def bt_register_click():
    global gWin
    bt_login.place_forget()
    lb_hint.place_forget()
    cb_password.place_forget()
    bt_administrator.place_forget()
    bt_register.place_forget()
    lb_username.place_forget()
    lb_password.place_forget()
    et_password.place_forget()
    et_username.place_forget()

    gWin.repassword,gWin.username1,gWin.password1 = tk.StringVar(),tk.StringVar(),tk.StringVar()

    gWin.name1 = cut_image("background.png", 320, 220, 470, 250)
    gWin.lbUsername1 = tk.Label(gWin, text=" 用 户 名 ：", image=gWin.name1, fg="black", font=('思源黑体', 16, ''), compound="center")
    gWin.lbUsername1.place(x=320, y=220, width=150, height=30)

    gWin.psw1 = cut_image("background.png", 320, 290, 470, 320)
    gWin.lbPassword1 = tk.Label(gWin, text=" 密 码 ：", image=gWin.psw1, fg="black", font=('思源黑体', 16, ''), compound="center")
    gWin.lbPassword1.place(x=320, y=290, width=150, height=30)

    gWin.etUsername1 = tk.Entry(gWin, textvariable=gWin.username1, font=('', 14, ''))
    gWin.etUsername1.place(x=520, y=220, width=200, height=30)

    gWin.etPassword1 = tk.Entry(gWin, textvariable=gWin.password1, show="*", font=('', 14, ''))
    gWin.etPassword1.place(x=520, y=290, width=200, height=30)

    lb_welcome["text"] = "用户注册"
    lb_welcome["fg"] = "black"

    gWin.rpsw = cut_image("background.png", 280, 360, 500, 390)
    gWin.lbrePassword = tk.Label(gWin, text=" 再次输入密码 ：", image=gWin.rpsw, fg="black", font=('思源黑体', 16, ''), compound="center")
    gWin.lbrePassword.place(x=280, y=360, width=150, height=30)

    gWin.etrePassword = tk.Entry(gWin, textvariable=gWin.repassword, show="*", font=('', 14, ''))
    gWin.etrePassword.place(x=520, y=360, width=200, height=30)

    gWin.bt_register1 = tk.Button(gWin, text="注册", bg="white", fg="black", font=('', 12, ''), command=bt_register_click1)
    gWin.bt_register1.place(x=500, y=460)
def bt_register_click1():
    global gWin
    if gWin.repassword.get() != gWin.password1.get() and gWin.password1.get() != "":
        gWin.password1.set("")
        gWin.repassword.set("")
        gWin.check = cut_image("background.png",420,400,670,430)
        Checktxt = tk.Label(gWin,text="两次输入密码不一致，请重新输入",image=gWin.check,fg="red",font=("",12,"",),compound="center")
        Checktxt.place(x=420, y=400, width=250, height=30)
    else:
        bt_login.place(x=340, y=460,width=100, height=60)
        lb_hint.place(x=325, y=150, width=390, height=30)
        bt_register.place(x=600, y=460, width=100, height=60)
        cb_password.place(x=373, y=350, width=100, height=20)
        bt_administrator.place(x=1, y=1, width=8, height=8)
        lb_username.place(x=320, y=220, width=150, height=30)
        lb_password.place(x=320, y=290, width=150, height=30)
        et_username.place(x=520, y=220, width=200, height=30)
        et_password.place(x=520, y=290, width=200, height=30)
        lb_welcome["text"] = "欢迎光临"
        lb_welcome["fg"] = "red"
        gWin.bt_register1.place_forget()
        gWin.lbrePassword.place_forget()
        gWin.etrePassword.place_forget()
        gWin.lbUsername1.place_forget()
        gWin.lbPassword1.place_forget()
        gWin.etUsername1.place_forget()
        gWin.etPassword1.place_forget()
import tkinter
from tkinter import ttk
from image import *


def password_click():  # “显示密码”单选框的事件响应函数，点击该单选框时被调用
    if showPassword.get():  # showPassword是和cbPassword绑定的tkinter布尔变量
        etPassword["show"] = ""  # 使得密码输入框能正常显示密码。Entry有show属性
    else:
        etPassword["show"] = "*"  # 使得密码输入框只显示'*'字符


def bt_administrator_click():
    pass


def bt_login_click():
    pass


def bt_register_click():
    pass


win = tk.Tk()
win.title("火锅点菜系统")
win.geometry("1040x600")
win.attributes("-toolwindow", 2)
win.resizable(0, 0)

background = get_image("background.png", 1040, 600)
canvas_win = tk.Canvas(win, width=1040, height=600)
canvas_win.create_image(520, 300, image=background)
canvas_win.pack()

welcome = cut_image("background.png", 170, 30, 870, 110)
lb_welcome = tk.Label(win, image=welcome, text=" 欢  迎  光  临  ！", fg="red", font=('华文行楷', 50, 'bold'),
                      compound="center")
lb_welcome.place(x=170, y=30, width=700, height=80)

hint = cut_image("background.png", 325, 150, 715, 180)
lb_hint = tk.Label(win, image=hint, text=" 请 输 入 您 的 用 户 名 和 密 码 ：", fg="black",
                   font=('思源黑体', 16, ''), compound="center")
lb_hint.place(x=325, y=150, width=390, height=30)

username, password = tk.StringVar(), tk.StringVar()

name = cut_image("background.png", 320, 220, 470, 250)
lbUsername = tk.Label(win, text=" 用 户 名 ：", image=name, fg="black", font=('思源黑体', 16, ''), compound="center")
lbUsername.place(x=320, y=220, width=150, height=30)

psw = cut_image("background.png", 320, 290, 470, 320)
lbPassword = tk.Label(win, text=" 密 码 ：", image=psw, fg="black", font=('思源黑体', 16, ''), compound="center")
lbPassword.place(x=320, y=290, width=150, height=30)

etUsername = tk.Entry(win, textvariable=username, font=('', 14, ''))
etUsername.place(x=520, y=220, width=200, height=30)

etPassword = tk.Entry(win, textvariable=password, show="*", font=('', 14, ''))
# Entry的属性show="*"表示该输入框不论内容是啥，只显示'*'字符，为""则正常显示
etPassword.place(x=520, y=290, width=200, height=30)

showPassword = tk.BooleanVar()  # 用于关联“显示密码”单选框
showPassword.set(False)  # 使得cbPassowrd开始就是非选中状态
show = cut_image("background.png", 398, 350, 468, 370)
cbPassword = tk.Checkbutton(win, text=" 显示密码", bg="white", fg="black", font=('', 12, ''), image=show,
                            variable=showPassword, command=password_click, compound="center")
# cbPassword关联变量showPassword，其事件响应函数是cbPassword_click，即点击它时，会调用 cbPassword_click()
cbPassword.place(x=373, y=350, width=100, height=20)

bt_administrator = tk.Button(win, text=" ", bg="white", command=bt_administrator_click, relief="groove")
bt_administrator.place(x=1, y=1, width=8, height=8)
bt_login = tk.Button(win, text="登录", bg="white", fg="black", font=('', 12, ''), command=bt_login_click)
# 点击btLogin按钮会执行btLogin_click()
bt_login.place(x=380, y=460)
bt_register = tk.Button(win, text="注册", bg="white", fg="black", font=('', 12, ''), command=bt_register_click)
bt_register.place(x=500, y=460)

win.mainloop()

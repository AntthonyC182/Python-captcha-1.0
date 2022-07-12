import tkinter as tk
#Điểm số HS
Doddle = ["Score:10", "Rank: A"]
Andy = ["Score:9", "Rank: A", ]
Putin = ["Score:8", "Rank: B"]
print("Sellect number")
print("1) Dođdle| 2) Andy| 3) Putin")
#Bạn sẽ ghi tên HS ở đây
a = input("Student_code:")
#Nếu bạn ghi đúng tên ở phần Điểm số HS (Doddle, Andy, Putin) bạn sẽ nhận được Điểm và vài thứ khác :D còn không nó sẽ hét error (lỗi)
if a == '1':
    print(Doddle)
elif a == '2':
    print(Andy)
elif a == '3':
    print(Putin)
else:
    print('Please write correct name!')
a = input('Rank:')
if a == 'A':
    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "B")
    tk.mainloop()
    print('-------------------10/10---------------------')
elif a == 'A':
    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "B")
    tk.mainloop()
    print('-------------------10/10---------------------')
elif a == 'B':
    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "B")
    tk.mainloop()
    print('-------------------10/10---------------------')
else:
    i = input('Score')
    if i == '10':
        root = tk.Tk()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, "A = 1022")
        tk.mainloop()
        print('-------------------10/10---------------------')
    elif i == '9':
        root = tk.Tk()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, "A = 1022")
        tk.mainloop()
        print('-------------------10/10---------------------')
    elif i == 8:
        root = tk.Tk()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, "A = 1022")
        tk.mainloop()
        print('-------------------10/10---------------------')
    else:
        print("You did the captcha with 0/10 score")
        print('-------------------0/10---------------------')
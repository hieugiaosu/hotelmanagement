from datetime import datetime
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *
from room import Room
from drink import Drink

roomlst=[]
drinklst=[]
drinknamelst=[]
with open('drinklist.mydb',mode='r',encoding='utf-8') as f:
    buf=f.readline().strip()
    while buf != "END":
        buf=f.readline().strip()
        if buf == "BEGINDRINK":
            drinkid=f.readline().strip()[-3:]
            drinkname=f.readline().strip()[5:]
            drinkprice=f.readline().strip()[6:]
            drinklst.append(Drink(drinkid=drinkid,name=drinkname,price=drinkprice))
            drinknamelst.append(drinkname)
with open("roomid.mydb",mode='r',encoding='utf-8') as f:
    buf=f.readline().strip()
    while buf != "END":
        buf=f.readline().strip()
        if buf == "BEGINROOM":
            roomid=f.readline().strip()[-3:]
            status=f.readline().strip()[7:]
            timein=f.readline().strip()[7:]
            timeout=f.readline().strip()[8:]
            guestid=f.readline().strip()[8:]
            kindofroom=f.readline().strip()[11:]
            fan=f.readline().strip()[4:]
            roomlst.append(Room(id=roomid,guest=guestid,status=status,timein=timein,timeout=timeout,kind=kindofroom))
            if fan=="FALSE":
                roomlst[len(roomlst)-1].fan=False
            else:
                roomlst[len(roomlst)-1].fan=True
def endprogram():
    with open("roomid.mydb",mode='w',encoding='utf-8') as f:
        f.write("BEGIN\n")
        for i in roomlst:
            f.write("BEGINROOM\n")
            f.write("ID:"+i.id+'\n')
            f.write("STATUS:"+i.status+'\n')
            f.write("TIMEIN:"+str(int(datetime.timestamp(i.timein)))+'\n')
            f.write("TIMEOUT:"+str(int(datetime.timestamp(i.timeout)))+'\n')
            f.write("GUESTID:NONE\n")
            f.write("KINDOFROOM:"+i.kind+'\n')
            f.write("FAN:")
            if i.fan:
                f.write("TRUE\n")
            else:
                f.write("FALSE\n")
            f.write("DRINK:\nBEGINDRINK\nENDDRINK\n")
            f.write("ENDROOM\n")
        f.write("END")
#CLick
def deleteScr():
    room101.place_forget()
    room102.place_forget()
    room103.place_forget()
    room104.place_forget()
    room201.place_forget()
    room202.place_forget()
    room203.place_forget()
    room204.place_forget()
def generalClick():
    room101.config(text=roomlst[0].showdetail(),background='#008000' if roomlst[0].checkRoom() else '#808080')
    room102.config(text=roomlst[1].showdetail(),background='#008000' if roomlst[1].checkRoom() else '#808080')
    room103.config(text=roomlst[2].showdetail(),background='#008000' if roomlst[2].checkRoom() else '#808080')
    room104.config(text=roomlst[3].showdetail(),background='#008000' if roomlst[3].checkRoom() else '#808080')
    room201.config(text=roomlst[4].showdetail(),background='#008000' if roomlst[4].checkRoom() else '#808080')
    room202.config(text=roomlst[5].showdetail(),background='#008000' if roomlst[5].checkRoom() else '#808080')
    room203.config(text=roomlst[6].showdetail(),background='#008000' if roomlst[6].checkRoom() else '#808080')
    room204.config(text=roomlst[7].showdetail(),background='#008000' if roomlst[7].checkRoom() else '#808080')
    room101.place(x=150,y=10)
    room102.place(x=400,y=10)
    room103.place(x=650,y=10)
    room104.place(x=150, y=170)
    room201.place(x=400,y=170)
    room202.place(x=650,y=170)
    room203.place(x=150,y=330)
    room204.place(x=400,y=330)

def emptyroomClick():
    pass
def addClick(a,combobox,entry):
    name=combobox.get()
    idx=0
    for i in range(0,len(drinknamelst)):
        if drinknamelst[i]==name:
            idx=i
            break
    text=entry.get()
    try:
        soluong=int(text)
    except:
        soluong=0
    roomlst[a].drink.append([drinklst[idx],soluong])
    messagebox.showinfo("Thông báo", "Đã thêm thành công")

def Available(a):
    oderdrink=ttk.Combobox(root)
    oderdrink['value']=drinknamelst
    oderdrink['state']='readonly'
    soluong=Entry(root)
    label1=Label(root,text="Chọn sản phẩm:")
    label2=Label(root, text="nhập số lượng:")
    add=Button(root,text="Thêm",command= lambda: addClick(a,oderdrink, soluong))
    selected1=StringVar()
    rad1 = Radiobutton(root,text='Tiếng', value="HOURS",variable=selected1)
    rad2 = Radiobutton(root,text='Qua Đêm', value="NIGHT",variable=selected1)
    rad3 = Radiobutton(root,text='Ngày', value="DAYS",variable=selected1)
    selected2=IntVar()
    rad4 =  Radiobutton(root,text='Quạt', value=1,variable=selected2)
    rad5 = Radiobutton(root,text='Máy Lạnh', value=0,variable=selected2)
    def clicked():
        roomlst[a].status="NOTAVAILABLE"
        roomlst[a].kind=selected1.get()
        roomlst[a].fan=selected2.get()
        roomlst[a].timein=datetime.fromtimestamp(int(datetime.timestamp(datetime.now())))
        oderdrink.place_forget()
        soluong.place_forget()
        label1.place_forget()
        label2.place_forget()
        add.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        rad3.place_forget()
        rad4.place_forget()
        rad5.place_forget()
        addroom.place_forget()
        generalClick()
    addroom=Button(root, text="Nhận Phòng", command=clicked)
    label1.place(x=150,y=10)
    oderdrink.place(x=250,y=10)
    label2.place(x=450,y=10)
    soluong.place(x=550,y=10)
    add.place(x=750,y=10)
    rad1.place(x=150,y=50)
    rad2.place(x=250,y=50)
    rad3.place(x=350,y=50)
    rad4.place(x=150,y=100)
    rad5.place(x=250,y=100)
    addroom.place(x=150,y=200)
def NotAvailable(a):
    pass
def RoomClick(a):
    deleteScr()
    if roomlst[a].checkRoom():
        Available(a)
    else:
        NotAvailable(a)
##GUI
root=Tk()
root.geometry('900x500')
root.title('Quản Lý khách sạn')
general=Button(root,text="Tất cả phòng",width=20,height=5,background='#905000',command=generalClick)
emptyroom=Button(root,text="Phòng Trống",width=20,height=5,background='#805000')
paybutton=Button(root,text="Thanh Toán Phòng",width=20,height=5,background='#705000')
detail=Button(root,text="Điều chỉnh thông tin",width=20,height=5,background='#605000')
history=Button(root,text="Lịch sử",width=20,height=5,background='#505000')
exit=Button(root,text="Thoát",width=20,height=5,background='#405000')
room101=Button(root,text=roomlst[0].showdetail(),width=30,height=10,background='#008000' if roomlst[0].checkRoom() else '#808080', command=lambda: RoomClick(0))
room102=Button(root,text=roomlst[1].showdetail(),width=30,height=10,background='#008000' if roomlst[1].checkRoom() else '#808080', command=lambda: RoomClick(1))
room103=Button(root,text=roomlst[2].showdetail(),width=30,height=10,background='#008000'if roomlst[2].checkRoom() else '#808080', command=lambda: RoomClick(2))
room104=Button(root,text=roomlst[3].showdetail(),width=30,height=10,background='#008000'if roomlst[3].checkRoom() else '#808080', command=lambda: RoomClick(3))
room201=Button(root,text=roomlst[4].showdetail(),width=30,height=10,background='#008000' if roomlst[4].checkRoom() else '#808080', command=lambda: RoomClick(4))
room202=Button(root,text=roomlst[5].showdetail(),width=30,height=10,background='#008000'if roomlst[5].checkRoom() else '#808080', command=lambda: RoomClick(5))
room203=Button(root,text=roomlst[6].showdetail(),width=30,height=10,background='#008000'if roomlst[6].checkRoom() else '#808080', command=lambda: RoomClick(6))
room204=Button(root,text=roomlst[7].showdetail(),width=30,height=10,background='#008000' if roomlst[7].checkRoom() else '#808080', command=lambda: RoomClick(7))


room101.place(x=150,y=10)
room102.place(x=400,y=10)
room103.place(x=650,y=10)
room104.place(x=150, y=170)
room201.place(x=400,y=170)
room202.place(x=650,y=170)
room203.place(x=150,y=330)
room204.place(x=400,y=330)
general.place(x=0,y=0)
emptyroom.place(x=0,y=85)
paybutton.place(x=0,y=85*2)
detail.place(x=0,y=85*3)
history.place(x=0,y=85*4)
exit.place(x=0,y=85*5)
root.mainloop()
endprogram()

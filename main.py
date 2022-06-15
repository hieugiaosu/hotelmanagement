from tkinter import *
from room import Room
from drink import Drink

roomlst=[]
drinklst=[]
drinkidlst=[]
with open("drinklist.mydb",mode='r',encoding='utf-8') as f:
    buf=f.readline().strip()
    while buf != "END":
        buf=f.readline().strip()
        if buf == "BEGINDRINK":
            drinkid=f.readline().strip()[-3:]
            drinkname=f.readline().strip()[5:]
            drinkprice=f.readline().strip()[6:]
            drinklst.append(Drink(drinkid=drinkid,name=drinkname,price=drinkprice))
            drinkidlst.append(drinkid)
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
#CLick
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
##GUI
root=Tk()
root.geometry('1000x500')
root.title('Quản Lý khách sạn')
general=Button(root,text="Tất cả phòng",width=20,height=5,background='#905000',command=generalClick)
emptyroom=Button(root,text="Phòng Trống",width=20,height=5,background='#805000')
paybutton=Button(root,text="Thanh Toán Phòng",width=20,height=5,background='#705000')
detail=Button(root,text="Điều chỉnh thông tin",width=20,height=5,background='#605000')
history=Button(root,text="Lịch sử",width=20,height=5,background='#505000')
exit=Button(root,text="Thoát",width=20,height=5,background='#405000')
room101=Button(root,text=roomlst[0].showdetail(),width=30,height=10,background='#008000' if roomlst[0].checkRoom() else '#808080')
room102=Button(root,text=roomlst[1].showdetail(),width=30,height=10,background='#008000' if roomlst[1].checkRoom() else '#808080')
room103=Button(root,text=roomlst[2].showdetail(),width=30,height=10,background='#008000'if roomlst[2].checkRoom() else '#808080')
room104=Button(root,text=roomlst[3].showdetail(),width=30,height=10,background='#008000'if roomlst[3].checkRoom() else '#808080')
room201=Button(root,text=roomlst[4].showdetail(),width=30,height=10,background='#008000' if roomlst[4].checkRoom() else '#808080')
room202=Button(root,text=roomlst[5].showdetail(),width=30,height=10,background='#008000'if roomlst[5].checkRoom() else '#808080')
room203=Button(root,text=roomlst[6].showdetail(),width=30,height=10,background='#008000'if roomlst[6].checkRoom() else '#808080')
room204=Button(root,text=roomlst[7].showdetail(),width=30,height=10,background='#008000' if roomlst[7].checkRoom() else '#808080')


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
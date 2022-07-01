from datetime import datetime
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *
from room import Room
from drink import Drink
import os
roomlst=[]
drinklst=[]
drinknamelst=[]
reportfilename="report\Baocao " + datetime.strftime( datetime.now(),'%m-%Y') +".csv"
with open(file=reportfilename,mode='a+',encoding='utf-8') as f:
    if os.stat(reportfilename).st_size == 0:
        f.write("STT,Phòng,Ngày,Giờ Vô, Giờ ra,Loại Phòng,tiền nước,tiền phòng,tổng tiền\n")
with open('drinklist.mydb',mode='r',encoding='utf-8') as f:
    buf=f.readline().strip()
    while buf != "END":
        buf=f.readline().strip()
        if buf == "BEGINDRINK":
            drinkid=f.readline().strip()[-3:]
            drinkname=f.readline().strip()[5:]
            drinkprice=f.readline().strip()[6:]
            drinklst.append(Drink(drinkid=drinkid,name=drinkname,price=int(drinkprice)))
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
            roomlst.append(Room(id=roomid,guest=guestid,status=status,timein=timein,timeout=timeout,kind=kindofroom,drink=[]))
            if fan=="FALSE":
                roomlst[len(roomlst)-1].fan=False
            else:
                roomlst[len(roomlst)-1].fan=True
            buf = f.readline().strip()
            buf = f.readline().strip()
            if buf == "BEGINDRINK":
                buf = f.readline().strip()
                while buf != "ENDDRINK":
                    drinkid = buf[-3:]
                    soluong = f.readline().strip()[8:]
                    for i in drinklst:
                        if i.id == drinkid:
                            roomlst[len(roomlst)-1].drink.append([i,int(soluong)])
                            break
                    buf = f.readline().strip()
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
            f.write("DRINK:\nBEGINDRINK\n")
            for x in i.drink:
                f.write("ID:"+str(x[0].id)+'\n')
                f.write("SOLUONG:"+str(x[1])+'\n')
            f.write("ENDDRINK\n") 
            f.write("ENDROOM\n")
        f.write("END")

def saveReport(room, drinkcost, total):
    STT=0
    with open(file=reportfilename,mode='r',encoding='utf-8') as f:
        buf=f.readlines()
        STT=len(buf)
    with open(file=reportfilename,mode='a',encoding='utf-8') as f:
        # STT,Phòng,Ngày,Giờ Vô, Giờ ra,Loại Phòng ,tiền nước, tiền phòng, tổng tiền
        f.write(str(STT))
        f.write(','+room.id+','+datetime.strftime(room.timein,'%d/%m/%Y')+','+datetime.strftime(room.timein,'%H:%M'))
        if (room.kind=="HOURS"):
            f.write(','+datetime.strftime(room.timeout,'%H:%M')+',')
        else:
            f.write(",,")
        loaiphong=""
        if room.kind=="HOURS":
            loaiphong+="Tiếng "
        elif room.kind=="DAYS":
            loaiphong+="Ngày "
        else:
            loaiphong+="Qua Đêm " 
        if room.fan:
            loaiphong+="Quạt,"
        else:
            loaiphong+="Máy lạnh,"
        f.write(loaiphong)
        f.write(str(drinkcost)+',')
        f.write(str(total-drinkcost)+',')
        f.write(str(total)+'\n')


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
    general.config(command= generalClick)
    emptyroom.config(command=emptyroomClick)
    paybutton.config(command=notemptyroomClick)
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
def notemptyroomClick():
    generalClick()
    if roomlst[0].checkRoom():
        room101.place_forget()
    if roomlst[1].checkRoom():
        room102.place_forget()
    if roomlst[2].checkRoom():
        room103.place_forget()
    if roomlst[3].checkRoom():
        room104.place_forget()
    if roomlst[4].checkRoom():
        room201.place_forget()
    if roomlst[5].checkRoom():
        room202.place_forget()
    if roomlst[6].checkRoom():
        room203.place_forget()
    if roomlst[7].checkRoom():
        room204.place_forget()
def emptyroomClick():
    generalClick()
    if not roomlst[0].checkRoom():
        room101.place_forget()
    if not roomlst[1].checkRoom():
        room102.place_forget()
    if not roomlst[2].checkRoom():
        room103.place_forget()
    if not roomlst[3].checkRoom():
        room104.place_forget()
    if not roomlst[4].checkRoom():
        room201.place_forget()
    if not roomlst[5].checkRoom():
        room202.place_forget()
    if not roomlst[6].checkRoom():
        room203.place_forget()
    if not roomlst[7].checkRoom():
        room204.place_forget()
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
    def deletepage():
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
        giovo.place_forget()
        giovo_label.place_forget()
        generalClick()
    roomlst[a].reset()
    emptyroom.config(command=deletepage)
    paybutton.config(command=deletepage)
    general.config(command=deletepage)
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
    giovo =Entry(root,width=100)
    giovo_label=Label(root,text="Nhập giờ vô theo định dạng mẫu hoặc để trống để lấy giờ tự động\n Định dạng mẫu: 07:35,02/12/2022")
    def clicked():
        time_str=giovo.get()
        roomlst[a].status="NOTAVAILABLE"
        roomlst[a].kind=selected1.get()
        roomlst[a].fan=selected2.get()
        try:
            roomlst[a].timein=datetime.fromtimestamp(int(datetime.timestamp(datetime.strptime(time_str, "%H:%M,%d/%m/%Y"))))
        except:
            roomlst[a].timein=datetime.fromtimestamp(int(datetime.timestamp(datetime.now())))
        # oderdrink.place_forget()
        # soluong.place_forget()
        # label1.place_forget()
        # label2.place_forget()
        # add.place_forget()
        # rad1.place_forget()
        # rad2.place_forget()
        # rad3.place_forget()
        # rad4.place_forget()
        # rad5.place_forget()
        # addroom.place_forget()
        # generalClick()
        deletepage()
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
    giovo_label.place(x=150,y=200)
    giovo.place(x=150,y=250)
    addroom.place(x=150,y=300)
def Thanhtoanpage(a):
    def deletepage():
        back.place_forget()
        label2.place_forget()
        label3.place_forget()
        label4.place_forget()
        label5.place_forget()
        tiennuoc.place_forget()
        label6.place_forget()
        tienphong.place_forget()
        label7.place_forget()
        tong.place_forget()
        thanhtoan.place_forget()
        generalClick()
    def Back():
        deletepage()
        RoomClick(a)
    def pay():
        drinkcost=int(tiennuoc.get())
        total=int(tong.get())
        saveReport(roomlst[a],drinkcost,total)
        messagebox.showinfo("Thông báo", "Thanh Toán Thành Công")
        roomlst[a].reset()
        deletepage()
    emptyroom.config(command=deletepage)
    paybutton.config(command=deletepage)
    general.config(command=deletepage)
    label2=Label(root,text= roomlst[a].showdetail(),background='#C0C0C0')
    drinkoder="Thêm: \n"
    for i in roomlst[a].drink:
        drinkoder+= i[0].name +'\n'+"Số lượng: " + str(i[1]) + '\n'
    label3=Label(root, text=drinkoder,background='#808080')
    label4=Label(root,text="Thành tiền:")
    label5=Label(root,text="Tiền nước:")
    label6=Label(root,text="Tiền phòng:")
    label7=Label(root,text="Tổng:")
    tiennuoc=Entry(root,width=10)
    tiennuoc.insert(0,roomlst[a].drinkprice())
    tienphong=Entry(root,width=10)
    tienphong.insert(0,roomlst[a].payment()-roomlst[a].drinkprice())
    tong=Entry(root,width=10)
    tong.insert(0,roomlst[a].payment())
    back=Button(root, text="quay lại",command= Back)
    thanhtoan=Button(root,text="Thanh Toán",command= pay)
    back.place(x=150,y=10)
    label2.place(x=150,y=50)
    label3.place(x=300,y=50)
    label4.place(x=400,y=50)
    label5.place(x=400,y=70)
    tiennuoc.place(x=500,y=70)
    label6.place(x=400,y=90)
    tienphong.place(x=500,y=90)
    label7.place(x=400,y=110)
    tong.place(x=500,y=110)
    thanhtoan.place(x=500,y=130)
def NotAvailable(a):
    def changeinfo(a):
        temp=changekind.get()
        if temp=="Qua Đêm":
            roomlst[a].kind="NIGHT"
        elif temp=="Tiếng":
            roomlst[a].kind="HOURS"
        else:
            roomlst[a].kind="DAYS"
        messagebox.showinfo("Thông báo", "Đã thay đổi thành công")
    def clear(a):
        label.place_forget()
        label1.place_forget()
        oderdrink.place_forget()
        label2.place_forget()
        soluong.place_forget()
        add.place_forget()
        label3.place_forget()
        changekind.place_forget()
        changebutton.place_forget()
        Thanhtoan.place_forget()
        Thanhtoanpage(a)
    def deletepage():
        label.place_forget()
        label1.place_forget()
        oderdrink.place_forget()
        label2.place_forget()
        soluong.place_forget()
        add.place_forget()
        label3.place_forget()
        changekind.place_forget()
        changebutton.place_forget()
        Thanhtoan.place_forget()
        generalClick()
    emptyroom.config(command=deletepage)
    paybutton.config(command=deletepage)
    general.config(command=deletepage)
    oderdrink=ttk.Combobox(root)
    oderdrink['value']=drinknamelst
    oderdrink['state']='readonly'
    soluong=Entry(root)
    label=Label(root,text="Điều chỉnh")
    label1=Label(root,text="Chọn sản phẩm:")
    label2=Label(root, text="nhập số lượng:")
    label3=Label(root, text="Điều chỉnh loại phòng")
    Thanhtoan=Button(root,text="Thông tin thanh toán",command=lambda: clear(a))
    add=Button(root,text="Thêm",command= lambda: addClick(a,oderdrink, soluong))
    changekind= ttk.Combobox(root)
    changekind['value']= ["Qua Đêm","Tiếng","Ngày"]
    changekind['state']='readonly'
    if roomlst[a].kind=="HOURS":
        changekind.current(1)
    elif roomlst[a].kind=="NIGHT":
        changekind.current(0)
    else:
        changekind.current(2)
    changebutton=Button(root,text="Cập nhật thông tin",command=lambda: changeinfo(a))
    label.place(x=150,y=10)
    label1.place(x=150,y=50)
    oderdrink.place(x=250,y=50)
    label2.place(x=450,y=50)
    soluong.place(x=550,y=50)
    add.place(x=750,y=50)
    label3.place(x=150,y=100)
    changekind.place(x=300,y=100)
    changebutton.place(x=550,y=100)
    Thanhtoan.place(x=150,y=150)
def RoomClick(a):
    deleteScr()
    if roomlst[a].checkRoom():
        Available(a)
    else:
        NotAvailable(a)
# def history():
#     pass
##GUI
root=Tk()
root.geometry('900x500')
root.title('Quản Lý khách sạn')
general=Button(root,text="Tất cả phòng",width=20,height=5,background='#905000',command=generalClick)
emptyroom=Button(root,text="Phòng Trống",width=20,height=5,background='#805000',command=emptyroomClick)
paybutton=Button(root,text="Thanh Toán Phòng",width=20,height=5,background='#705000',command=notemptyroomClick)
history=Button(root,text="Lịch sử",width=20,height=5,background='#505000')
exit=Button(root,text="Thoát",width=20,height=5,background='#405000',command=root.quit)
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
# history.place(x=0,y=85*3)
exit.place(x=0,y=85*3)
root.mainloop()
endprogram()
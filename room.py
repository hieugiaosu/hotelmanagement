from datetime import datetime
from datetime import timedelta
import math
from drink import Drink
class Room:
    def __init__(self,id=None,guest=None,drink=[[Drink(0,"none",0),0]],status="AVAILABLE",timein=0,timeout=0,kind=None ):
        self.id=id
        self.guest=guest
        self.status=status
        self.timein=datetime.fromtimestamp(int(timein))
        self.timeout=datetime.fromtimestamp(int(timeout))
        self.drink=drink
        self.kind=kind
        self.fan=0
    def checkRoom(self):
        return True if self.status == 'AVAILABLE' else False
    def showdetail(self):
        s="Phòng " + self.id +'\n'
        if self.status == 'AVAILABLE':
            s=s+"Tình Trạng Phòng: Trống"
        else:
            s=s+"Đang có khách \n Loại phòng: "
            if self.fan:
                s= s+ "Quạt \n"
            else:
                s= s+ "Máy Lạnh \n"
            if self.kind=="HOURS":
                s=s+"Tiếng"
            elif self.kind=="NIGHT":
                s=s+"Qua Đêm"
            elif self.kind=="DAYS":
                s=s+"Ngày"
            s=s+"\n Giờ vô: " +self.timein.strftime("%H:%M ,%d/%m/%Y")
        return s
    def setFan(self):
        self.fan=1
    def reset(self):
        self.guest=None
        self.status="Available"
        self.timein=None
        self.timeout=None
        self.drink=[[Drink(0,"none",0),0]]
        self.kind=None
        self.fan=False
    def payment(self):
        if self.timein:
            return 0
        beginprice=0
        drinkprice =0
        for i in self.drink:
            drinkprice+=i[0].cost(i[1])
        if self.kind=="HOURS" :
            if self.fan:
                beginprice=50000
            else:
                beginprice=70000
            self.timeout=datetime.now()
            time = datetime.timestamp(self.timeout) - datetime.timestamp(self.timein)
            hours= int(time/3600)
            minutes=int((time - hours*3600)/60)
            if minutes>20:
                hours+=1
            if hours==0:
                return int(50000+drinkprice)
            elif hours==1:
                self.reset()
                return int(beginprice+drinkprice)
            elif hours==2:
                self.reset()
                return int(beginprice+20000+drinkprice)
            elif hours==3:
                self.reset()
                return int(beginprice+30000+drinkprice)
            else:
                self.reset()
                return int(beginprice+30000+10000*(hours-3)+drinkprice)
        elif self.kind=="NIGHT":
            self.timeout=datetime.now()
            time = datetime.timestamp(self.timeout) - datetime.timestamp(self.timein)
            hours = math.ceil(time/3600)
            if self.fan:
                beginprice=130000
            else:
                beginprice=150000
            if hours<=12:
                self.reset()
                return int(beginprice+drinkprice)
            else:
                self.reset()
                return int(beginprice+20000*(hours-12)+drinkprice)
        elif self.kind=="DAYS":
            beginprice=250000
            self.timeout=datetime.now()
            period = self.timeout - self.timein
            days = period.days
            roomcost= 250000*days
            hours = int(period/3600)
            roomcost+=20000*hours
            self.reset()
            return roomcost+drinkprice
        else:
            return 0
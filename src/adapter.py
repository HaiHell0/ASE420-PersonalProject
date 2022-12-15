from todoitem import Todoitem
import re
import datetime
class Adapter():
    timeRegex = "([01]?[0-9]|2[0-3]):[0-5][0-9]"
    def verifyDate(self, date):
        if(date == None or date==""):
            return False
        elif (date.lower()!= "today"):
            try:
                result = datetime.datetime.strptime(date, '%Y/%m/%d')
            except ValueError:
                return False
        return True
    def verifyTime(self, time):
        if(time == None or time==""):
            return False
        try:
            if("AM" in time or "PM" in time):
                time = time.replace("AM", "")
                time = time.replace("PM", "")
                if(not re.search(self.timeRegex,time)):
                    return False
                temp = time.split(":")
                if int(temp[0])>=12 or int(temp[1])>=60:
                    return False
            if(not re.search(self.timeRegex,time)):
                return False
            temp = time.split(":")
            if int(temp[0])>=24 or int(temp[1])>=60:
                    return False
        except ValueError:
            return False
        return True
    
    def validateTo(self, fr, to):
        fr = self.interpretTime(fr)
        to = self.interpretTime(to)
        listfr = fr.split(":")
        listto = to.split(":")
        if (int(listfr[0])>=int(listto[0]) and int(listfr[1])>=int(listto[1])):
            return False
        else:
            return True 

    def interpretDate(self, date):
        if(date.lower() =="today"):
            current_time = datetime.datetime.now()
            return "{}/{}/{}".format(current_time.year,current_time.month,current_time.day)
        else: 
            return date
    
    def interpretTime(self,time):
        if("AM" in time):
            time = time.replace("AM", "")
            return time
        elif("PM" in time):
            time = time.replace("PM", "")
            temp = time.split(":")
            hours = str(int(temp[0])+12)
            return "{}:{}".format(hours, temp[1])
        return time
    
    def validateDateValue(self, date):
        if(self.verifyDate(date)):
            result = datetime.datetime.strptime(date, '%Y/%m/%d')
            if (result<datetime.datetime.now()): 
                    return False
            return True
        return False
        



test = Adapter()
test.verifyDate("2020/12/12")


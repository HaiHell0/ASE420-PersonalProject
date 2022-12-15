class Todoitem:
    def __init__(self,DATE,FROM,TO,TASK,TAG, id = -1):
        self.id = id
        self.DATE = DATE
        self.FROM = FROM
        self.TO = TO
        self.TASK = TASK
        self.TAG = TAG
    def __str__(self):
        return "ID:{} DATE:{} FROM:{} TO:{} TASK:{} TAG:{}".format(self.id,self.DATE,self.FROM,self.TO,self.TASK,self.TAG)
        
        
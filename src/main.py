from todoitem import Todoitem
from sqlite import DataService
from adapter import Adapter
import argparse


class Option(object):
  def execute(self,argument):pass


class Record(Option):
  adapter = Adapter()
  dataservice = DataService()
  def execute(self,argument):
    print("Attempting to record:", argument)
    if(len(argument)!=5):
      print("Invalid input, use:\nrecord [<Date>] [<FROM>] [<TO>] [<TASK>] [<TAG>]")
      return "ERROR"
    if(not self.adapter.verifyDate(argument[0])):
       return("invalid Date")
    if(not self.adapter.verifyTime(argument[1])):
       return("invalid From")
    if(not self.adapter.verifyTime(argument[2])):
       return("invalid To")
    if(not self.adapter.validateDateValue(argument[0])):
       return("Date can't be in the past")
    if(not self.adapter.validateTo(argument[1],argument[2])):
       return("To can't be earlier than From")
    date = self.adapter.interpretDate(argument[0])
    fr = self.adapter.interpretTime(argument[1])
    to = self.adapter.interpretTime(argument[2])
    self.dataservice.addToDoItem(Todoitem(date,fr,to,argument[3],argument[4]))
    return ("Successful")

class Invalid(Option):
  def execute(self,argument):
    return "Invalid Input of ", argument
class Delete(Option):
  dataservice = DataService()
  def execute(self,argument):
    print("Attempting to delete item with ID:", argument)
    if(len(argument)!=1):
      print("Invalid input, use:\ndelete [<ID>]")
      return "ERROR"
    if (self.dataservice.deleteToDoItem(argument[0])): 
      return "Successful"
    else:
      return "Unsuccessful"


class Query(Option):
  dataservice = DataService()
  def execute(self,argument):
    print("Attempting to query with KEY:", argument)
    if(len(argument)!=1):
      print("Invalid input, use:\nquery [<DATE> <TASK> <TAG>]")
      return "ERROR"
    print("Searching by tags:")
    matchTag = self.dataservice.getByTag(argument[0])
    if(len(matchTag)==0):
      print("No items with matching tag")
    else:
      print("Found items with that tag:")
      for item in matchTag:
        print(item)
    matchTask = self.dataservice.getByTask(argument[0])
    if(len(matchTask)==0):
      print("No items with matching task")
    else:
      print("Found items with that task:")
      for item in matchTag:
        print(item)
    matchDate = self.dataservice.getByTag(argument[0])
    if(len(matchDate)==0):
      print("No items with matching date")
    else:
      print("Found items with that date:")
      for item in matchDate:
        print(item)
    return("There were {} items that matched by tag, {} items that matched by task,{} items that matched by date",(len(matchTag),len(matchTask),len(matchDate)))


class Report(Option):
  dataservice = DataService()
  def execute(self,argument):
    print("Attempting to serach in ragne:", argument[0],argument[1])
    if(len(argument)!=2):
      print("Invalid input, use:\nreport [<DATE>] [<DATE>]")
      return "ERROR"
    match = self.dataservice.getByDateFromTo(argument[0],argument[1])
    if(len(match)==0):
      print("No items with matching tag")
    for item in match:
      print(item)
    return "There were {} items that matched by tag".format(len(match))

   




class List(Option):
  dataservice = DataService()
  def execute(self,argument):
    
    all= self.dataservice.getAllItems()
    if (argument[0] != "detail" and argument[0] != "simple"):
      print("Invalid input, use:\nlist [detail/simple]")
      return "ERROR"
    if (len(all)==0):
      return "No items"
    if(argument[0]=="detail"):
      for item in all:
        print(item)
    if(argument[0]=="simple"):
      for item in all:
        print("DATE:{}, TASK:{}".format(item.DATE, item.TASK))
    return "Returned {} items".format(len(all))

class Priority(Option):
  dataservice = DataService()
  def execute(self,argument):
    all= self.dataservice.getAllItems()
    if (len(argument)==0):
      print("Invalid input, use:\nPriority: priority [number of tasks]")
      return "ERROR"
    match = self.dataservice.getPrioTask()
    if (len(match)==0):
      return "No items"
    for i in range(int(argument[0])):
      if i == len(match): 
        return "Returned {} items".format(i)
      item = match[i]
      print("PRIORITY #{} TASK:{}, TAG:{}".format(i+1,item.TASK,item.TAG))
    return "Returned {} items".format(argument[0])




class Context(object):
  def __init__(self):
    self.option =Option()
  def set_option(self, Option):
    self.option = Option
  def make_decision(self, input, argument):
    if input == "record":
      self.set_option(Record())
    elif input == "query":
      self.set_option(Query())
    elif input == "delete":
      self.set_option(Delete())
    elif input == "list":
      self.set_option(List())
    elif input == "report":
      self.set_option(Report())

    elif input == "priority":
      self.set_option(Priority())
    else:
      self.set_option(Invalid())
    return self.option.execute(argument)
  


def run():
  context = Context()
  print("TO DO APP/////////////////////////////////////////")
  print("Available command:")
  print("To record time:\nrecord [<Date>] [<FROM>] [<TO>] [<TASK>] [<TAG>]\nTo query records:query [<DATE> <TASK> <TAG>]\nTO delete an item: delete [<ID>]\nTO list all items: list [detail/simple]\nReport from date to date: report [from] [to]\nPriority: priority [number of tasks]")
  """ while(True):
    record = str(input("Enter command (or press q):"))
    if(record =="q"): 
      break
    recordList = record.split(" ")
    command =  recordList[0]
    recordList.pop(0)
    print("Command returned result of:",context.make_decision(command,recordList)) """
  




if __name__ == "__main__":
  print("TO DO APP/////////////////////////////////////////")
  #print("To record time:\nrecord [<Date>] [<FROM>] [<TO>] [<TASK>] [<TAG>]\nTo query records:query [<DATE> <TASK> <TAG>]\nTO delete an item: delete [<ID>]\nTO list all items: list [detail/simple]\nReport from date to date: report [from] [to]\nPriority: priority [number of tasks]\n\n")
  parser = argparse.ArgumentParser()
  context = Context()
  parser.add_argument('operation', help ="Available options for operations: record, query, delete, list, report, priority")
  parser.add_argument('arguments', help ="Enter the arguments")
  args = parser.parse_args()
  #print(args.operation, [args.arguments])
 
  result = context.make_decision(args.operation,[args.arguments])
  print(result)
from datetime import datetime
from datetime import date

class Calendar:
    def __init__(self):
        self.events=[]
        
    def add_event(self,event):
        self.events.append(event)  
          
    @staticmethod    
    def is_weekend(date):
        return date.weekday()
    
    @classmethod
    def from_json(cls):
        
     if cls is WorkCalendar:
         print("this method is called from Work Calendar")
     if cls is Calendar:
         print("this method is called from Calendar ")    
    
     
        
        
class WorkCalendar(Calendar):
    pass    


    
def main():  
    WorkCalendar.from_json()
    Calendar.from_json()        
main()       
        
        
        
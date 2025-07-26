
#pip3 install fastapi
#pip3 install fastapi["standart"]
#we can define async or sync endpoints depending on our task

from fastapi import FastAPI
from typing import List ,Optional
from enum import IntEnum
from pydantic import BaseModel , Field


class Rockband():
    id:int 


rockbands_db = [
     {
       "id":"2",
        "name": "Foo Fighters",
        "genre": "Alternative Rock",
        "year_formed": 1994,
        "is_active": True,
        "origin": "Seattle, USA",
        "members": ["Dave Grohl", "Nate Mendel", "Pat Smear", "Taylor Hawkins"]
    },
    {
        "id":"3",
        "name": "Radiohead",
        "genre": "Experimental Rock",
        "year_formed": 1985,
        "is_active": True,
        "origin": "Abingdon, England",
        "members": ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Philip Selway"]
    },
   {
        "id":"4",
        "name": "The Rolling Stones",
        "genre": "Rock and Roll",
        "year_formed": 1962,
        "is_active": True,
        "origin": "London, England",
        "members": ["Mick Jagger", "Keith Richards", "Ronnie Wood", "Charlie Watts"]
    },
     {"id":"5",
        "name": "Nirvana",
        "genre": "Grunge",
        "year_formed": 1987,
        "is_active": False,
        "origin": "Aberdeen, Washington, USA",
        "members": ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"]
    },
     {"id":"6",
        "name": "Arctic Monkeys",
        "genre": "Indie Rock",
        "year_formed": 2002,
        "is_active": True,
        "origin": "Sheffield, England",
        "members": ["Alex Turner", "Jamie Cook", "Nick O'Malley", "Matt Helders"]
    },
   {"id":"7", 
        "name": "Muse",
        "genre": "Progressive Rock",
        "year_formed": 1994,
        "is_active": True,
        "origin": "Teignmouth, England",
        "members": ["Matt Bellamy", "Chris Wolstenholme", "Dominic Howard"]
    }
]



api = FastAPI()

@api.get('/')
def index():
    return {
        "message":"Hello World"
    }


@api.get("/calculation")
def calculation ():
    sum=0
    for i in range (100_000_000):
        sum += i;

    return {
        "result":sum
    }



#path paraemeters
@api.get('/rockbands/{rockband_id}')
def get_rock_band(rockband_id:str):
    for rockband in rockbands_db:
        print(rockband)
        if rockband["id"] == rockband_id:
            print("found")
            
            return {
                "result" :rockband
            }

#query parameter
#it is important to define the type of the parameter that will be enterd by the user
#good use of pydantic results in better docs
@api.get("/rockbands")
def get_first_n(first_n: int = None):
    if first_n:
        return{
            "Result": rockbands_db[:first_n]
        }
    else:
       return {
           "Result" : rockbands_db
       }




#put api_end
@api.post('/rockbands')
def create_rockband(rockband:dict):
    rockbands_db.append(rockband)
    print("rock band was succesfully added")
    
    return {
         "rockband" :rockband
    }



@api.delete('/rockbands/{id}')
def delete_rockband(id : str):
  for rockband in rockbands_db:
      if rockband["id"] == id:
       i =rockbands_db.index(rockband)
       rockbands_db.pop(i)
       return{
           "result":"Rockband with id of {} was removed".format(id)
       }


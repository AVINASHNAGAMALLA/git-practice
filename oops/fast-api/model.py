from pydantic import BaseModel
from abc import ABC,abstractmethod

   


class Lib(BaseModel):
    id:int
    title:str
    author:str

class Account(ABC):
    
    def __init__(self,accn_num,cust_name,blnc):
        self._acc=accn_num
        self._cust=cust_name
        self._blnc=blnc

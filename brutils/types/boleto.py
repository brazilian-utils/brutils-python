from typing import TypedDict

class Boleto(TypedDict):
    bank_issuing: int       
    coin_type: int          
    due_date: str           
    amount: float          
    our_number: str        
    free_field: str        
    barcode: str            

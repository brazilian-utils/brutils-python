from brutils.types.boleto import Boleto
from brutils.data.enums.boleto import BASE_DATE

from datetime import datetime

def format_boleto(boleto: Boleto) -> str:
    base_date = BASE_DATE.date.value

    due_date = boleto['due_date']

    current_year = datetime.now().year

    due_date_full = f"{current_year}{due_date[2:]}"

    factor_of_expiration = (datetime.strptime(due_date_full, "%Y%m%d") - datetime.strptime(base_date, "%Y%m%d")).days

    amount = str(int(boleto["amount"] * 100)).zfill(10)

    barcode = (
        f"{boleto['bank_issuing']:03}"  
        + f"{boleto['coin_type']:1}"  
        + f"{factor_of_expiration:4}"  
        + f"{amount:010}" 
        + f"{boleto['our_number']:11}"  
        + f"{boleto['free_field']:1}"
    )

    formatted_boleto = (
        barcode[:5] + '.' + barcode[5:10] + ' ' +
        barcode[10:15] + '.' + barcode[15:20] + ' ' +  
        barcode[20:25] + '.' + barcode[25:30] + ' ' +  
        barcode[30:31] + ' ' +  
        barcode[31:] 
    )
    
    return formatted_boleto

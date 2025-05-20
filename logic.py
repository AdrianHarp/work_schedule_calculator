from datetime import datetime
pattern = [True,True,
           False,False,
           True,True,True,
           False,False,
           True,True,
           False,False,False]
def date_delta(date):
    intial_date = datetime.strptime("2025-05-12", "%Y-%m-%d")
    requested_date = datetime.strptime(date, "%Y-%m-%d")
    delta = requested_date - intial_date
    return(delta.days)

def is_working(date):
    index = date_delta(date) % len(pattern)  
    return pattern[index]

def is_mandatory(date,mandatory_one,mandatory_two):
    if date == mandatory_one:
        return True
    if date == mandatory_two:
        return True
    return False
def status(date,mandatory_one,mandatory_two):
    status = "Working" if is_working(date) else "Free"
    if is_mandatory(date,mandatory_one,mandatory_two):
        status = "Working"
    return status

    




    


  
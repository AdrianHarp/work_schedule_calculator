from datetime import datetime
pattern = [True,True,
           False,False,
           True,True,True,
           False,False,
           True,True,
           False,False,False]

def date_delta(year,month,day):
    intial_date = datetime.strptime(f"2025-05-12", "%Y-%m-%d")
    requested_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    delta = requested_date - intial_date
    return(delta.days)
def is_working(year,month,day):
    index = date_delta(year,month,day) % len(pattern)
    return pattern[index]
def main(year,month,day):
    status = "Working" if is_working(year,month,day) else "Free"
    print(status)
main("2025","05","21")
    




    


  
from datetime import datetime
from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    print(datetime.today())
    get_employees()
    calculate_salary()
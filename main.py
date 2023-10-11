# This is a sample Python script.
from datetime import datetime

import xurl

from application.db.people import get_employees
from application.salary import calculate_salary

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(datetime.today())
    get_employees()
    calculate_salary()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

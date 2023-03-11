from datetime import date

import vk

from application.salary import calculate_salary
from application.db.people import get_employees
from dirty_main import *

if __name__ == '__main__':
	get_employees()
	calculate_salary()
	day = date.today()
	print(day) 
	gi()
	print(a)
	api = vk.API(access_token='...')
	api.users.get(user_ids=1)
		
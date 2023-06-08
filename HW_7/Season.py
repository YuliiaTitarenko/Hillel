# Написати функцію season, що приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якому цей місяць
# належить (зима, весна, літо чи осінь). (20 балів)
def season(month_number):
	if month_number < 1 or month_number > 12:
		print('Enter valid month number')
	elif (month_number >= 1 and month_number <=2) or month_number ==12:
		return 'Winter'
	elif month_number >= 3 and month_number <=5:
		return 'Spring'
	elif month_number >= 6 and month_number <=8:
		return 'Summer'
	elif month_number >= 9 and month_number <=11:
		return 'Autumn'



print('Season is {}'.format(season(3)))












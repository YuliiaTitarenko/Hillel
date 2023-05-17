import digit as digit

car = 'Skoda'
model_1 = 'Fabia'
model_2 = 'Octavia'
model_3 = 'Scala'

print(f'Car: {car} \n ')

print('Car: {} \n '.format(car))

print('Car models: {} {}, {} {}, {} {} \n '.format(car, model_1, car, model_2, car, model_3))

print('Car models: {0} {3}, {0} {2}, {0} {3} \n '.format(car, model_1, model_2, model_3))

PI = 3.1415926

print(f'PI =  {PI} \n' )

print('PI = {} \n'.format(PI))

print('PI = {:.2f} \n'.format(PI))

print('PI = {:.4f}\n'.format(PI))

print('PI = {} \n'.format(PI.__round__(5)))

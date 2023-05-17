car = 'Skoda'
model = 'FABIA'
text = 'Lorem ipsum dolor sit amet'
txt = 'lorem ipsum dolor sit amet'
print(car, model)
print('Casefold: ',model.casefold())
print('Upper: ',car.upper())
print('Lower: ',model.lower())
print('Replace: ',model.replace("A", "W"))
print('Split: ',text.split())
print('Capitalize: ', txt.capitalize())
print('Find "dolor" in text":' ,text.find('dolor'))
print('Find "o" in text between 10 and 14 position:' ,text.find('o',10,14))
print('Count "r" in text:',text.count('r'))
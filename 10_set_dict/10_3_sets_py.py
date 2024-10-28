# this program show varios 
# operation on sets

baseball = set(['Johny', 'Karmen', 'Aida', 'Aliciya'])
basketball = set(['Eva', 'Karmen', 'Aliciya', 'Sara'])

# show user baseball set
print('Эти студенты состоят в бейсбольной команде: ')
for name in baseball:
    print(name)
    

# show user basketball set
print()
print('Эти студенты состоят в баскетбольной команде')
for name in basketball:
    print(name)
    

# show intersection
print()
print('Эти студенты играют в бейсбол и в баскетбол')
for name in baseball.intersection(basketball):
    print(name)
    

# show union
print()
print('Эти студенты играют в одну или обе спортивные игры')
for name in baseball.union(basketball):
    print(name)


# show difference between baseball and basketball
print()
print('Эти студенты играют в бейсбол, но не баскетбол')
for name in baseball.difference(basketball):
    print(name)
    

# show difference between basketball and baseball
print()
print('Эти студенты играют в баскетбол, но не бейсбол')
for name in basketball.difference(baseball):
    print(name)
    

# show symetric difference
print()
print('Эти студенты играют в одну из спортивных игр, но не в обе')
for name in baseball.symmetric_difference(basketball):
    print(name)
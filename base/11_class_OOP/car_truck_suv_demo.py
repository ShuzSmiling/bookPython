from modules.vehicles import Car, Truck


def main():
    
    used_car = Car('Audi', 2007, 12500, 21500, 4)
    used_truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    
    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')
    print()
    
    print('Данный легковой автомобиль имеется на складе')
    print(f'Изготовитель: {used_car.get_make()}')
    print(f'Модель: {used_car.get_model()}')
    print(f'Пробег: {used_car.get_mileage()}')
    print(f'Кол-во дверей: {used_car.get_doors()}')
    print(f'Цена: ${used_car.get_price()}')
    print()

    print('Данный пикап имеется на складе')
    print(f'Изготовитель: {used_truck.get_make()}')
    print(f'Модель: {used_truck.get_model()}')
    print(f'Пробег: {used_truck.get_mileage()}')
    print(f'Тип привода: {used_truck.get_drive_type()}')
    print(f'Цена: ${used_truck.get_price()}')

if __name__ == '__main__':
    main()
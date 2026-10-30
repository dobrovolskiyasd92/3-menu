food_category = input("Введите категорию блюда(напиток, суп, десерт): ").lower()

match food_category:
    case 'напиток':
        dish = input("Какое блюдо вы выберете?(чай, кофе, сок) ").lower()
        match dish:
            case 'чай':
                print(f'Блюдо: {dish}\nЦена: 50')
            case 'кофе':
                print(f'Блюдо: {dish}\nЦена: 70')
            case 'сок':
                print(f'Блюдо: {dish}\nЦена: 110')
            case _:
                print('Некорректный ввод!')
    case 'суп':
        dish = input("Какое блюдо вы выберете?(борщ, щи, суп-пюре) ").lower()
        match dish:
            case 'борщ':
                print(f'Блюдо: {dish}\nЦена: 85')

            case 'щи':
                print(f'Блюдо: {dish}\nЦена: 75')

            case 'суп-пюре':
                print(f'Блюдо: {dish}\nЦена: 100')

            case _:
                print('Некорректный ввод!')
    case 'десерт':
        dish = input("Какое блюдо вы выберете?(торт, мороженое, фрукты) ").lower()
        match dish:
            case 'торт':
                print(f'Блюдо: {dish}\nЦена: 70')

            case 'мороженое':
                print(f'Блюдо: {dish}\nЦена: 65')

            case 'фрукты':
                print(f'Блюдо: {dish}\nЦена: 40')

            case _:
                print('Некорректный ввод!')
    case _:
        print('Некорректный ввод!')

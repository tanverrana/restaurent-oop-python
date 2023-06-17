from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from users import Chef, Customer, Server, Manager


def main():
    menu = Menu()
    pizza_1 = Pizza('chicken pizza', 600, 'large', ['chicken', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Beef pizza', 600, 'large', ['Beef', 'onion'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Vegetable Pizza', 500, 'Medium',
                    ['Vegetable', 'Onion', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('Chicken Burger', 270, 'Chicken', ['bread', 'Chicken'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 470, 'Beef', ['bread', 'beef'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('coke', 40, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Coffee', 60, False)
    menu.add_menu_item('drinks', coffee)

    # show menu
    menu.show_menu()

    restaurant = Restaurant('TS Restaurant', 1500, menu)
    # add employees
    manager = Manager('Tanver rana', 1234, 'tanver@gmai.com',
                      'Meherpur', 1200, '1st january 2023', 'Core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Messi', 10, 'messi@football.com', 'Argentina',
                450, '1st january 2023', 'chef', 'burger')
    restaurant.add_employee('chef', chef)
    server = Server('Neymar', 11, 'neymar@football.com',
                    'Brazil', 250, 'February 2024', 'server')
    restaurant.add_employee('server', server)

    # show employee
    restaurant.show_employees()

    # customer
    customer_1 = Customer(
        'Shakaib', 75, 'shakib@cricket.com', 'Magora', 120000)


if __name__ == '__main__':
    main()

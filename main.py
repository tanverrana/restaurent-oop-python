from menu import Pizza, Burger, Drinks, Menu


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


if __name__ == '__main__':
    main()

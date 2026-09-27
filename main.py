import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input(
            "What size sandwich would you like? (small/medium/large/off/report): "
        ).lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print(f"Bread: {resources['bread']} slices")
            print(f"Ham: {resources['ham']} slices")
            print(f"Cheese: {resources['cheese']} ounces")

        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                print(f"That will be ${cost}.")

                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(
                        choice, ingredients
                    )

        else:
            print("Invalid selection. Please choose small, medium, or large.")


if __name__ == "__main__":
    main()
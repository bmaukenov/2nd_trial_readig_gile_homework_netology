#cooking_book.update({file.readline().rstrip():[]})
cooking_book = {}


def reading_cook_book():
	

	with open("recipes.txt") as file:
				
		while True:
			all_ingridients = []
			dish = file.readline().rstrip()
			if not dish:
				break
			for ingridient in range(int(file.readline().rstrip())):
				ingr_info = file.readline().rstrip().split(" | ")
				all_ingridients.append({"ingridient_name":ingr_info[0], "quantity":ingr_info[1], "measure":ingr_info[2]})
			cooking_book.update({dish: all_ingridients})
			file.readline()


	print(cooking_book)



def get_shop_list_by_dishes(dishes, person_count):
	shop_list = {}
	for dish in dishes:
		dish_recipe = cooking_book[dish]
		for ingridient in dish_recipe:

			new_in_shop_list = ingridient["ingridient_name"]

			if new_in_shop_list in shop_list.keys():
				new_quantity = int(shop_list[new_in_shop_list]["quantity"]) + int(ingridient["quantity"]) * person_count
				shop_list[new_in_shop_list]["quantity"] = new_quantity
			else:
				new_quantity = int(ingridient["quantity"]) * person_count
				shop_list.update({new_in_shop_list:{"measure":ingridient["measure"], "quantity":new_quantity}})
	print(shop_list)




reading_cook_book()

print("\n \n")

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
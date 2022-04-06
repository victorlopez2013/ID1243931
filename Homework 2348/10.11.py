# Victor Lopez
# PSID: 1243931
class FoodItem:

    def __init__(self, n="None", f=0.0, c=0.0, p=0.0):
        self.name = n
        self.fat = f
        self.carbs = c
        self.protein = p

    def get_calories(self, n_s):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * n_s;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    f_1 = FoodItem()
    i_n = input()
    a_f = float(input())
    a_c = float(input())
    a_p = float(input())

    f_2 = FoodItem(i_n, a_f, a_c, a_p)

    n_s = float(input())

    f_1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(n_s,f_1.get_calories(n_s)))

    print()

    f_2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(n_s,f_2.get_calories(n_s)))
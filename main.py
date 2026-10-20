from animal import Animal, Cat, Dog

my_cat = Cat("Muri")
my_dog = Dog("Matu")

neighbor_dog = Dog("Pulst")

my_dog.dog_sees(neighbor_dog)
my_dog.dog_sees(my_cat)
my_cat.cat_sees(my_dog)
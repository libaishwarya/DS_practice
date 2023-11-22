class cartoon_charecter():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self. country = country

    def tell_my_name(self):
        print("my name is %s", self.name)

    def tell_my_country(self):
        print("my country is %s", self.country)

class jackie_charecter(cartoon_charecter):
    def __init__(self, name, age, country, abilities):
        super().__init__(name, age, country)
        self.abilities = abilities

    def tell_my_abilities(self):
        print("my abilities are %s", self.abilities)

character = cartoon_charecter(name="chan", age=25, country="country")
character.tell_my_name()
character.tell_my_country()

j_charecter = jackie_charecter(
    name="jack", age=29, country="China", abilities=["run", "jump"])
j_charecter.tell_my_name()
j_charecter.tell_my_country()
j_charecter.tell_my_abilities()

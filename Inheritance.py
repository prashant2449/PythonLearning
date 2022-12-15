public class Animal:
    def walk(self):
        print("WALK")

    def talk(self):
        print("CANT TALK")


class Dog(Animal):
    def character(self):
        return self.talk()

obj = Dog()
obj.character()

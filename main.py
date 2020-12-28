from persons import *


class People:
    def get_text(self):
        print(f'{self.persona}')

    def persona(self, persona):
        self.persona = persona


person1 = People()
x = Marilyn_Monroe()
person1.persona(x)
person1.get_text()

person2 = People()
z = Haruki_Murakami()
person2.persona(z)
person2.get_text()


def date(day_month_year):
    dmy = day_month_year[0] + '.' + day_month_year[1] + '.' + day_month_year[2]
    return dmy


def gender(gender_words, gen):
    if gen == 'man':
        gender_words.append('родился')
        gender_words.append('был')
        gender_words.append('известен')
    if gen == 'woman':
        gender_words.append('родилась')
        gender_words.append('была')
        gender_words.append('известна')
    return gender_words


def things(things_number):
    if things_number == 0:
        return 'такие произведения'
    elif things_number == 1:
        return 'такие изобритения'
    elif things_number == 2:
        return 'роли в таких фильмах'


class Persons:
    def __init__(self):
        gen = ''
        gen_words = ['', '', '']
        self.things = things(0)
        self.time_of_born = ['0', '0', '0']
        self.time_of_born_shortname = date(self.time_of_born)
        self.time_of_dying = [0, 0, 0]
        self.place_of_born = ''
        self.name_of_person = ''
        self.profession = ''
        self.celebrity_reasons = ''
        self.gender_words = gender(gen_words, gen)
        self.person_biography = f'\n***********************************************************************************' \
               f'\n\n{self.profession} {self.name_of_person} {self.gender_words[0]} ' \
                                f'{self.time_of_born_shortname} в {self.place_of_born}\n' \
                                f'{self.gender_words[1]} {self.gender_words[2]} за ' \
                                f'{self.things} как:\n{self.celebrity_reasons}\n\n' \
               f'***********************************************************************************\n'

    def __repr__(self):
        return f'\n***********************************************************************************' \
               f'\n\n{self.profession} {self.name_of_person} {self.gender_words[0]} ' \
                                f'{self.time_of_born_shortname} в {self.place_of_born}\n' \
                                f'{self.gender_words[1]} {self.gender_words[2]} за ' \
                                f'{self.things} как:\n{self.celebrity_reasons}\n\n' \
               f'***********************************************************************************\n'



class Marilyn_Monroe(Persons):
    def __init__(self):
        gen = 'woman'
        gen_words = []
        thing = 2
        super().__init__()
        self.things = things(thing)
        self.time_of_born = ['1', '6', '1926']
        self.time_of_born_shortname = date(self.time_of_born)
        self.gender_words = gender(gen_words, gen)
        self.name_of_person = 'Мерлин Монро'
        self.profession = 'Актриса'
        self.place_of_born = 'Лос-Анджелесе'
        self.celebrity_reasons = 'Dangerous Years \\\\ Scudda Hoo! Scudda Hay! \\\\ Ladies of the Chorus'


class Haruki_Murakami(Persons):
    def __init__(self):
        gen = 'man'
        gen_words = []
        thing = 0
        super().__init__()
        self.things = things(thing)
        self.time_of_born = ['12', '1', '1949']
        self.time_of_born_shortname = date(self.time_of_born)
        self.gender_words = gender(gen_words, gen)
        self.name_of_person = 'Харуки Мураками'
        self.profession = 'Писатель'
        self.place_of_born = 'Киото'
        self.celebrity_reasons = 'Охота на овец \\\\ Кафка на пляже \\\\ Норвежский лес'


class Nikola_Tesla(Persons):
    def __init__(self):
        gen = 'man'
        gen_words = []
        thing = 1
        super().__init__()
        self.things = things(thing)
        self.time_of_born = ['10', '7', '1856']
        self.time_of_born_shortname = date(self.time_of_born)
        self.gender_words = gender(gen_words, gen)
        self.name_of_person = 'Никола Тесла'
        self.profession = 'Изобретатель'
        self.place_of_born = 'Смилян'
        self.celebrity_reasons = 'Переменный ток\\\\ Трансформатор Теслы'

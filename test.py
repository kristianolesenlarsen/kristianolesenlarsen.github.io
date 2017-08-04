from webbrowser import open

open('https://google.com')


a = False
b = True

if not a and not b:
    print('yes')
else:
    print('no')



class student():

  def __init__(self, skills, ambitions):
    self.skills = skills
    self.ambitions = ambitions

  def study(self, need_beer = True):
    if self.ambitions > self.skills:
        if need_beer:
            print("I wont study today even though im behind on school, instead i'll go get a drink")
            return False
        else:
            print("I'm already studying since my skills don't match my ambitions, and i dont want beer right now")
            return True
    else:
        print("I have studied more than i had ambitions to do, i'll get a beer now")
        return False

Allan = student(skills = 10, ambitions = 20)

Allan.study(need_beer = False)

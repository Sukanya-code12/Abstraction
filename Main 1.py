class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most vividly spoken language of India")
class USA():
    def capital(self):
        print("Washinton DC is the capital of USA")
    def language(self):
        print("English is the most vividly spoken language in USA")
i=India()
u=USA()
for j in (i,u):
    j.capital()
    j.language()
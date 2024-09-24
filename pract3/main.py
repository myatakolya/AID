class prolog:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        if isinstance(self, prolog):
            return f"Тебя зовут {self.name}"
        
    def rename(self,newname):
        self.name=newname
        return self    
al = prolog('Хуй')
al = al.rename("Чай")
print(al)
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        

class Student:
    def __init__(self, student_id, research_work):
        self.student_id = student_id
        self.research_work = research_work
        
    def present_research(self):
        print(f"My student id is {self.student_id} and I have done this kind of research: {self.research_work}")
        

class Doctor(Person):
    def __init__(self, name, age, address, op_kind, doctor_type):
        Person.__init__(self, name, age, address)
        self.operation_kind = op_kind
        self.doctor_type = doctor_type

    def make_operation(self):
        pass


class Police(Person, Student):
    def __init__(self, name, age, address, student_id, research_work, police_dpt_name):
        super().__init__(name, age, address)
        Student.__init__(self, student_id, research_work)
        self.police_dpt_name = police_dpt_name
        
    
    def arest_someone(self):
        print(f"I am policeman with name {self.name} and I arrested some guy in my {self.police_dpt_name} department!")
    

class Firefighter(Person):
    def __init__(self, name, age, address, rank_ffighter):
        super().__init__(name, age, address)
        self.rank_firefighter = rank_ffighter
        
    def fight_fire(self):
        pass
    
class ChefFireFighter(Firefighter):
    def __init__(self, name, age, address, rank_ffighter, station_name):
        super().__init__(name, age, address, rank_ffighter)
        self.station_name = station_name
        
    def give_orders(self):
        print(f"Начальник {self.name} командует станцией {self.station_name} и дает приказы!")


class SoccerPlayer(Person, Student):
    def __init__(self, name, age, address, club_name, jersey_num):
        super().__init__(name, age, address)
        self.club_name = club_name
        self.jersey_num = jersey_num

    def display_info(self):
        super().display_info()
        print(f"Club name: {self.club_name}")
        print(f"Jersey numb: {self.jersey_num}")
        
    def present_research(self):
        print(f"I am not making any research but just study!")
    
    def attack_other_player():
        pass
    
    

p1 = Person("Samar", 23, "Lev Tolstoy 123")
p1.display_info()
print("=========")
d1 = Doctor("Peter", 28, "Mira 7", "Heart surgery", "Surgeun")
d1.display_info()

print("=========")
police_off1 = Police(
    "Timur",
    35,
    "Satylganov 21",
    "J567890123", 
    "How to decrease Level of crime in LA", 
    "LA Police dpt"
)

police_off1.display_info()
print("=========")
police_off1.present_research()
print("==========")
police_off1.arest_someone()

print("==========")
soccerPlayer = SoccerPlayer(
    "Cristiano Ronaldo",
    37,
    "Saudi Arabia",
    "Al Nasser",
    7
)
soccerPlayer.display_info()
print("==========")
soccerPlayer.present_research()

print("=========")
ff1 = Firefighter("Oleg", 33, "Frunze 123", "Level 23")
ff1.display_info()

print("=========")
ff2 = ChefFireFighter("Stpean", 45, "LEv Tolstoy 77", "General", "Fire station 5")
ff2.give_orders()
        
    
    
        
        
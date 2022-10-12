phone_network = {}

def register(new_phone):
    global phone_network
    phone_network[new_phone.number] = new_phone


class Plan:    
    def __init__(self, cost:float, data:int=0, minutes:int=0, text:int=0):
        self.__cost = cost
        self.__data = data
        self.__minutes = minutes
        self.__text = text

    def is_callable(self, length):
        return length <= self.__minutes

    def call(self, length):
        self.__minutes -= length

    def __str__(self):
        return f"cost: ${round(self.__cost, 2)} data: {self.__data}Kb minutes: {self.__minutes} text: {self.__text}"


class Phone:
    def __init__(self, number:str, make:str, model: str, plan:Plan=None, camera=None):
        self.number = number
        self.make = make
        self.model = model
        self.plan = plan
        self.camera = camera
        self.apps = set()

    def get_make(self):
        return self.make

    def get_full_name(self):
        return f'{self.make} - {self.model}'

    def call(self, number:str, length:int) -> bool:

        global phone_network

        other:Phone = phone_network.get(number, None)

        if not other:
            return False

        if not self.plan.is_callable(length) or not other.plan.is_callable(length):
            return False

        self.plan.call(length) 
        other.plan.call(length)

        return True


    def __eq__(self, __o: object) -> bool:
        
        if isinstance(__o, Phone):
            numbers_equal = __o.number == self.number
            make_equal = __o.make == self.make
            model_equal = __o.model == self.model

            return numbers_equal and make_equal and model_equal

        return False

    def __str__(self):
        return self.get_full_name()

plan_a = Plan(10, minutes=45)
apple = Phone('1', 'apple', 'iphone 14', plan=plan_a)
register(apple)

plan_b = Plan(10, minutes=97)
android = Phone('2', 'samsung', 'galaxy s5', plan=plan_b)
register(android)

for _ in range(10):
    if apple.call("2", 5):
        print('call success')
    else:
        print('call failure')

print(apple.plan)
print(android.plan)

import random

def spill_it(drink):
    try:
        print(f'I am going to drink {drink} now.')
        #if random.randint(0, 1):
        #raise RuntimeError(f'Ooops I spilled the {drink}')
    #except RuntimeError as e:
    #    print(f'{e}. Dont worry I\'ll poor another glass of {drink}')
    #else:
    #    print('Nothing happened here')
        return 5
    finally:
        print('Im just here to clean up after everyone...') 


spill_it('apple juice')

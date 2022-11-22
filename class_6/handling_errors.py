def num_input() -> float:
    ui = input('Type a number: ')
    try:
        return float(ui)
    except (ValueError, TypeError):
        print(f'The value "{ui}" does not appear to be a number')
    except Exception as e:
        print('Hmm something went wrong...')

    return num_input()

#num_1 = num_input()
#num_2 = num_input()

#print(f"{num_1} + {num_2} = {num_1 + num_2}")

try: 
    raise RuntimeError("This is my message")
except Exception as e:
    print(f"The message of exception = {e}")
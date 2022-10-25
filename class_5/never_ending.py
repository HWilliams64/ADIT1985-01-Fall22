import os

with open(__file__) as file:
    text = file.read()

while os.path.exists(__file__):
    pass

with open(__file__, 'w') as file:
    file.write(text)

os.system(f"python {__file__}")

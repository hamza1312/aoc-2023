# Loads the input for a day
def loadinput(num: int) -> str:
     output = ""
     with open(f'../inputs/{num}.input', encoding='utf8') as f:
        output = f.read()           
     return output

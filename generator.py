import random

def generate(option):

    if(option == "C"):
        capital_letters = list(map(lambda i: chr(i),range(65,91)))
        return capital_letters
    elif(option == "S"):
        small_letters = list(map(lambda i: chr(i),range(97,123)))
        return small_letters
    elif(option == "D"):
        digits = list(map(lambda i: chr(i),range(48,58)))
        return digits
    else:
        return []

def generate_key(amount_of_keys):

    generated_keys = []
    which_collection_to_pick = ["C","S","D"]

    for i in range(amount_of_keys):
        key = ""
        for sign in range(25):
            random_collection_index = which_collection_to_pick[random.randint(0,len(which_collection_to_pick)-1)]
            if(sign == 0):
                continue
            elif(sign%5==0):
                key += "-"
                continue
            key += random.choice(generate(random_collection_index))
        generated_keys.append(key)

    for i in range(amount_of_keys):
        print(generated_keys[i])

generate_key(5)
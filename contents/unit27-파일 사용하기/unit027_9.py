import pickle

with open('james.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    scores = pickle.load(file)
    address = pickle.load(file)
    print(name)
    print(age)
    print(scores)
    print(address)


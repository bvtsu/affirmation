from random import choice
try:
    from AffirmationText import affirmations as affirmations
except:
    from Affirmations.AffirmationText import affirmations as affirmations


def affirm(function):
    def wrapper():
        func = function()
        print(choice(affirmations))
        return func
    return wrapper


if __name__ == "__main__":
    print(affirmations)
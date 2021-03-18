

def main():
    import random
    dice_rolls=3
    dsum=0
    for i in range(0,dice_rolls):
        roll = random.randint(1,6)
        dsum+=roll
        print(f'You rolled a {roll} die')
        print(f'sum={dsum}')
if __name__== "__main__":
    main()
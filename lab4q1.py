'''
Do not remove any text from these comments
1.	Improve the following Python program (Sample Answer for CE03 Q5) as in 
following code:
• Randomise the secret_num. The random number generated must be within the
 range of 1 to 200.
• Add an iterative function using the while loop to ask the user for a 
decision to continue playing the game.

Function to use: random.randint(), int(), input(), print(), str(), str.lower()
Operators: !=, <, +
Structure: while, if - else
'''

def main():
    secret_num = 50
    guess_num = int(input("my guess"))
    count = 1
    
    while guess_num != secret_num:
        if guess_num < secret_num:
            print("too low")
        else:
            print("too high")
        count = count + 1
        guess_num = int(input("have another guess"))

    print(f"Well done, you took {str(count)} attempts")

    return 0



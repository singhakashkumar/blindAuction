logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bidder = dict()

show_is_on = True

def clear():
    print("\n"*100)

while show_is_on:
    name = input("Enter the name of bidder: ")
    bidAmount = float(input("Enter the bid amount: $"))
    bidder[name] = bidAmount
    bidderLeft = input("Enter 'yes' to continue bidding and 'no' to exit: ")
    if bidderLeft == "no":
        show_is_on = False
    clear()
    

highestBidder = None
highestAmount = None
for name, bidAmount in bidder.items():
    if highestAmount is None or highestAmount < bidAmount:
        highestAmount = bidAmount
        highestBidder = name

print(f"Highest bidder is {highestBidder} with an amount of {highestAmount}")

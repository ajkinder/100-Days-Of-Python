# Silent Auction application
# Turn based silent auction application that
# allows you to have a silent auction with all of your friends.

# IMPORTS
import art
import os
clear = lambda: os.system('clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for name in bidding_record:
        bid_amount = bidding_record[name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    print(f"The winner is {winner} with a final bit of ${highest_bid}.")


# BODY
print(art.logo)

bids = {}
is_bidding = True

while is_bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any more bidders? Type yes or no.").lower()
    if should_continue == "no":
        is_bidding = False
    elif should_continue == "yes":
        clear()

find_highest_bidder(bids)
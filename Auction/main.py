import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)

bids = {

}
going = True
while going:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bids[name] = bid
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if keep_going.lower() == "yes":
        print("\n" * 100)
    else:
        going = False
        max_key = max(bids, key=bids.get)
        max_value = bids[max_key]
        print(f"The winner is {max_key} with a bid of ${max_value}.")

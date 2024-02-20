from collections import deque 

deck = []
hand = deque()

with open('cards.txt', 'r', encoding='utf-8') as file:
    for line in file:
        deck.append(line.strip())

for _ in range(5):
    hand.append(deck.pop())
print("Player's hand:", list(hand))

while True:
    discard_num = input("Enter the number of cards you want to discard (0-5): ")
    if discard_num.isdigit() and 0 <= int(discard_num) <= 5:
        discard_num = int(discard_num)
        break
    else:
        print("Invalid number. Please enter a number between 0 and 5.")

print("Discarded cards:")
for _ in range(discard_num):
    print(hand.popleft())

print("New cards:")
for _ in range(discard_num):
    new_card = deck.pop()
    hand.append(new_card)
    print(new_card)

print("Final deck:", deck)
print("Final hand:", list(hand))

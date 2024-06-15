import random

def spin_row():
  symbols = ["🍒", "🍋", "🍊", "🌟", "💎", "🍀", "🔔", "🍉", "🍇"]

  results = [random.choice(symbols) for _ in range(3)]

  return results

def print_row(row):

  print("------------")
  print(" | ".join(row))
  print("------------")


def get_payout(row, bet):

  if row[0] == row[1] == row[2]:

    if row[0] == "💎":
      return bet * 10
    elif row[0] == "🌟":
      return bet * 8
    elif row[0] == "🔔":
      return bet * 6
    elif row[0] == "🍀":
      return bet * 4
    elif row[0] == "🍉" or row[0] == "🍇":
      return bet * 3
    else:
      return bet * 2
  
  else:
    return 0


def main():

  balance = 100

  print("***************************")
  print("Welcome to Python Casino")
  print("Symbols: 🍒🍋🍊🌟💎🍀🔔🍉🍇")
  print("***************************")

  while balance > 0:
    print(f"Current Balance: {balance}")

    bet = input("Place your bet amount: ")

    if not bet.isdigit():
      print("Please enter a valid amount")
      continue
    else:
      bet = int(bet)

    if bet > balance:
      print("\nInsufficient Funds")
      continue

    if bet <= 0:
      print("\nBet must be greater than 0")
      continue

    balance -= bet

    row = spin_row()

    print("Spinning...\n")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
      print(f"You earned: {payout}")
    else:
      print("Try Again! Luck is just around the corner. 🍀")

    is_quit = input("Would you like to spin again? [Y/N]").upper()

    if is_quit != "Y":
      break
  
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print(f"\nFinal Balance: {balance}\nSayonara Rookie 🎰!")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    

if __name__ == "__main__":
  main()
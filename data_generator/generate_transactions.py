print("Script started!")

import csv
import random
from datetime import datetime, timedelta

print("Imports successful!")

categories = ['Groceries', 'Gas', 'Restaurants', 'Entertainment', 'Utilities']
merchants = ['Kroger', 'Shell', 'Chipotle', 'AMC', 'AEP']

def generate_transaction():
    date = datetime.now() - timedelta(days=random.randint(0, 90))
    amount = round(random.uniform(10, 200), 2)
    category = random.choice(categories)
    merchant = random.choice(merchants)
    
    return {
        'date': date.strftime('%Y-%m-%d'),
        'amount': amount,
        'merchant': merchant,
        'category': category
    }

def generate_transactions(count=100):
    transactions = [generate_transaction() for _ in range(count)]
    
    print("Writing to CSV...")
    with open('transactions.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'amount', 'merchant', 'category'])
        writer.writeheader()
        writer.writerows(transactions)
    
    print(f"Generated {count} transactions")

if __name__ == '__main__':
    print("Running main...")
    generate_transactions(100)
    print("Done!")
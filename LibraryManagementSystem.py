import datetime
import csv
import os

# -------------------------------
# File Paths
# -------------------------------
BOOKS_FILE = "books.csv"
MEMBERS_FILE = "members.csv"
BORROWED_FILE = "borrowed_records.csv"

# -------------------------------
# Data Storage
# -------------------------------
books = []
members = []
borrowed_records = []

# -------------------------------
# CSV Load / Save Functions
# -------------------------------
def load_data():
    # Load books
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "author": row["author"],
                    "quantity": int(row["quantity"])
                })
    else:
        # Default starter books
        books.extend([
            {"id": 1, "title": "Python Programming", "author": "Sir Samad", "quantity": 3},
            {"id": 2, "title": "Data Structures and Algorithms", "author": "Dileep Krishna", "quantity": 2},
            {"id": 3, "title": "Artificial Intelligence", "author": "Asad Kazmi", "quantity": 1}
        ])

    # Load members
    if os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                members.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "borrowed_books": eval(row["borrowed_books"]) if row["borrowed_books"] else []
                })
    else:
        members.extend([
            {"id": 1, "name": "Maqsood Ahmed", "borrowed_books": []},
            {"id": 2, "name": "Saad Ahmed", "borrowed_books": []}
        ])

    # Load borrowed records
    if os.path.exists(BORROWED_FILE):
        with open(BORROWED_FILE, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                borrowed_records.append({
                    "member_id": int(row["member_id"]),
                    "book_id": int(row["book_id"]),
                    "borrow_date": datetime.datetime.strptime(row["borrow_date"], "%Y-%m-%d").date(),
                    "due_date": datetime.datetime.strptime(row["due_date"], "%Y-%m-%d").date(),
                    "returned": row["returned"].lower() == "true"
                })

def save_data():
    # Save books
    with open(BOOKS_FILE, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "author", "quantity"])
        writer.writeheader()
        writer.writerows(books)

    # Save members
    with open(MEMBERS_FILE, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "borrowed_books"])
        writer.writeheader()
        for m in members:
            writer.writerow({
                "id": m["id"],
                "name": m["name"],
                "borrowed_books": m["borrowed_books"]
            })

    # Save borrowed records
    with open(BORROWED_FILE, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["member_id", "book_id", "borrow_date", "due_date", "returned"])
        writer.writeheader()
        for r in borrowed_records:
            writer.writerow({
                "member_id": r["member_id"],
                "book_id": r["book_id"],
                "borrow_date": r["borrow_date"],
                "due_date": r["due_date"],
                "returned": r["returned"]
            })

# -------------------------------
# Helper Functions
# -------------------------------
def display_all_books():
    print("\nAll Books:")
    for book in books:
        status = f"{book['quantity']} available"
        print(f"{book['id']}. {book['title']} by {book['author']} ({status})")

def display_available_books():
    print("\nAvailable Books:")
    for book in books:
        if book["quantity"] > 0:
            print(f"{book['id']}. {book['title']} by {book['author']} (Qty: {book['quantity']})")

def display_all_members():
    print("\nLibrary Members:")
    for member in members:
        print(f"{member['id']}. {member['name']}")

def search_books():
    keyword = input("\nEnter book title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = f"{book['quantity']} available"
            print(f"{book['id']}. {book['title']} by {book['author']} ({status})")
            found = True
    if not found:
        print("No books found.")

def borrow_book():
    member_id = int(input("\nEnter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    member = next((m for m in members if m["id"] == member_id), None)
    book = next((b for b in books if b["id"] == book_id), None)
    if not member or not book:
        print("Invalid Member ID or Book ID.")
        return
    if book["quantity"] <= 0:
        print("Sorry, no copies available.")
        return
    book["quantity"] -= 1
    member["borrowed_books"].append(book_id)
    borrow_date = datetime.date.today()
    due_date = borrow_date + datetime.timedelta(days=14)
    borrowed_records.append({
        "member_id": member_id,
        "book_id": book_id,
        "borrow_date": borrow_date,
        "due_date": due_date,
        "returned": False
    })
    save_data()
    print(f"Book '{book['title']}' borrowed successfully! Due date: {due_date}")

def return_book():
    member_id = int(input("\nEnter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    record = next((r for r in borrowed_records if r["member_id"] == member_id and r["book_id"] == book_id and not r["returned"]), None)
    if not record:
        print("No borrowed record found.")
        return
    record["returned"] = True
    book = next((b for b in books if b["id"] == book_id), None)
    book["quantity"] += 1
    member = next((m for m in members if m["id"] == member_id), None)
    member["borrowed_books"].remove(book_id)
    save_data()
    print(f"Book '{book['title']}' returned successfully!")

def view_member_borrowed_books():
    member_id = int(input("\nEnter Member ID: "))
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        print("Invalid Member ID.")
        return
    print(f"\nBooks borrowed by {member['name']}:")
    if not member["borrowed_books"]:
        print("No books borrowed.")
        return
    for book_id in member["borrowed_books"]:
        book = next(b for b in books if b["id"] == book_id)
        print(f"- {book['title']} by {book['author']}")

def view_overdue_books():
    today = datetime.date.today()
    overdue = [r for r in borrowed_records if not r["returned"] and r["due_date"] < today]
    print("\nOverdue Books:")
    if not overdue:
        print("No overdue books.")
        return
    for record in overdue:
        member = next(m for m in members if m["id"] == record["member_id"])
        book = next(b for b in books if b["id"] == record["book_id"])
        print(f"{book['title']} (Borrowed by: {member['name']}, Due: {record['due_date']})")

def library_report():
    total_books = sum(b["quantity"] for b in books)
    borrowed = len([r for r in borrowed_records if not r["returned"]])
    available = total_books
    print("\n--- Library Report ---")
    print(f"Total Book Copies: {total_books}")
    print(f"Borrowed Books (active loans): {borrowed}")
    print(f"Total Members: {len(members)}")

def add_new_book():
    title = input("\nEnter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))
    book_id = len(books) + 1
    books.append({"id": book_id, "title": title, "author": author, "quantity": quantity})
    save_data()
    print(f"Book '{title}' added successfully!")

def register_new_member():
    name = input("\nEnter Member Name: ")
    member_id = len(members) + 1
    members.append({"id": member_id, "name": name, "borrowed_books": []})
    save_data()
    print(f"Member '{name}' registered successfully!")

# -------------------------------
# Main Menu
# -------------------------------
def main():
    load_data()
    while True:
        print("\n" + "="*60)
        print("  LIBRARY MANAGEMENT SYSTEM By AYAZ ALI s/o SULTAN MEHMOOD")
        print("="*60)
        print("""
 1.   Display All Books
 2.   Display Available Books
 3.   Display All Members
 4.   Search Books
 5.   Borrow a Book
 6.   Return a Book
 7.   View Member's Borrowed Books
 8.   View Overdue Books
 9.   Library Report
 10.  Add New Book
 11.  Register New Member
 0.   Exit 
""")
        choice = input(" Enter your choice (0-11): ")
        if choice == "1": display_all_books()
        elif choice == "2": display_available_books()
        elif choice == "3": display_all_members()
        elif choice == "4": search_books()
        elif choice == "5": borrow_book()
        elif choice == "6": return_book()
        elif choice == "7": view_member_borrowed_books()
        elif choice == "8": view_overdue_books()
        elif choice == "9": library_report()
        elif choice == "10": add_new_book()
        elif choice == "11": register_new_member()
        elif choice == "0":
            save_data()
            print("Exiting Program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# -------------------------------
# Run the program
# -------------------------------
if __name__ == "__main__":
    main()

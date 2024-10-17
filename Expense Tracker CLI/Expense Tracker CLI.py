
import time
from PyInquirer import prompt
expense_list = []
total_amount = 0


def summarize_amount():
    global total_amount
    temp_total = 0
    for expense in expense_list:
        # total_amount = 0total_amount = 0
        temp_total += expense["expense"]["amount"]
    total_amount = temp_total
    print("Total amount spent: " + str(total_amount))


def add_expense():

    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    expense = {"amount": amount, "category": category,
               "description": description}
    expense_dictionary = {"id": len(expense_list) + 1, "expense": expense}
    expense_list.append(expense_dictionary)
    print("Expense added successfully!")
    summarize_amount()

    # add_more_input = input("Do you want to add more expenses? (Y/N): ")
    # if add_more_input.upper() == "N":
    #     break


def view_expenses():
    for index, expenses in enumerate(expense_list, start=1):
        print(f"Expense {index}")
        print("Amount: " + str(expenses["expense"]["amount"]))
        print("Category: " + expenses["expense"]["category"])
        print("Description: " + expenses["expense"]["description"])
        print()
        summarize_amount()


def update_expense():
    update_id_input = int(
        input("Can you give the id of the expense you want to update? "))
    for expense in expense_list:
        if expense["id"] == update_id_input:
            updated_amount = int(input("Enter the updated amount"))
            expense["expense"]["amount"] = updated_amount
            updated_category = input("Enter the updated category")
            expense["expense"]["category"] = updated_category
            updated_description = input("Enter the updated description")
            expense["expense"]["description"] = updated_description
            print(f"Expense with ID {expense['id']} updated.")
            break
    else:
        print("No expense found with the provided ID.")


def delete_expense():
    delete_id_input = int(
        input("Can you give the id of the expense you want to delete? "))
    for expense in expense_list:
        if expense["id"] == delete_id_input:
            print(f"Expense with ID {expense['id']} removed.")
            expense_list.remove(expense)
            break
    else:
        print("No expense found with the provided ID.")

# def search_expense():


def show_menu():
    print("Welcome to the expense tracker...")
    time.sleep(0.5)
    questions = [{
        'type': 'list',
        'name': 'operation',
        'message': "What would you like to do today...",
        'choices': ['Create', 'Read', 'Update', 'Delete', 'Search', 'Exit'],
    }]

    return prompt(questions)['operation']


while True:
    selected_operation = show_menu()

    if selected_operation == "Create":
        add_expense()
    elif selected_operation == "Read":
        view_expenses()
    elif selected_operation == "Update":
        update_expense()
    elif selected_operation == "Delete":
        delete_expense()
    # elif selected_operation == "Search":
        # search_expense()
    elif selected_operation == "Exit":
        break

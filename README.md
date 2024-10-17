# Expense Tracker CLI

This is a Command Line Interface (CLI) project for tracking your daily expenses, built with Python. The application allows users to add, view, and delete expenses in a list and also summarizes the total amount spent. It's a simple yet effective way to manage your spending habits directly from your terminal.

## Unique Features

1. **Add Expenses with Detailed Descriptions**  
  Users can add multiple expenses with details such as amount, category, and description.

2. **View All Expenses**  
  Displays all the expenses added along with their categories and descriptions in an organized format. Each expense is numbered for easy reference.

3. **Delete Expenses**  
  You can delete any expense using its unique ID, keeping your expense list clutter-free.

4. **Total Amount Summarization**  
  Automatically calculates and displays the total amount spent based on the entered expenses.

5. **Interactive Prompts Using PyInquirer**  
  Enhanced user interaction with the PyInquirer package, allowing users to input data more intuitively.

6. **Error Handling**  
  Prevents errors such as invalid input types for amounts and missing data fields.

7. **Dynamic Expense Management**  
  Efficient management of expenses using Python's data structures and global variable manipulation for smooth updates.

8. **Fully Customizable**  
  Although it's a CLI tool, it's easy to expand and adapt, and can be a foundation for larger expense management applications.

## How to Use

1. **Install Required Packages**

Run the following command to install the required dependencies:

```bash
pip install PyInquirer
```
2. **Run the Application**
Execute the Python script to start the CLI tool:
```bash
python expense_tracker.py
```
3. **Adding Expenses**
You will be prompted to enter the amount, category, and description of each expense. You can add multiple expenses in one session.

![image](https://github.com/user-attachments/assets/a9a58648-fc14-4234-bd54-2e126a0edea1)

4. Viewing Expenses
The application will list all your added expenses in a numbered format.

![image](https://github.com/user-attachments/assets/3c0863f3-646c-4c39-9596-fa1cce2584cd)

5. Deleting Expenses
You will be asked to provide the ID of the expense you wish to delete. The application will then remove the specified entry from your list.

![image](https://github.com/user-attachments/assets/2779789b-695e-46b9-bf7d-bf6364d9381e)

6. Summarizing Total Amount
After you've added expenses, the tool will provide you with a summary of your total spending.

![image](https://github.com/user-attachments/assets/76a8cc9d-617b-4f42-b259-9ebf687ccecb)

## Code Structure
```bash
.
├── expense_tracker.py    # Main Python script
└── README.md             # Project documentation
```
## Future Enhancements
- Data Persistence: Save expenses to a file or database for long-term tracking.
- Filtering Options: Add the ability to filter expenses by date, category, or amount.
- Graphical User Interface (GUI): Potential to extend the project into a GUI-based app.
- Export as CSV: Enable exporting expenses to a CSV file for further analysis.

## Contributing
Feel free to fork this repository and submit pull requests if you want to contribute new features, fix bugs, or improve the existing code.






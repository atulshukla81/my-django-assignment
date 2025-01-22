# my-django-assignment
Assesment Task Submission for Python Django Developer Intern Position at Tradexa


## How to Run the Project
1. **Clone the repository**:
   git clone https://github.com/atulshukla81/my-django-assignment.git

2. **Navigate to the project directory**:
   cd my-django-assignment

3. **Run the project**:
   python distributed_inserts.py
   

## Output Screenshots

Below is the script output:

![Terminal Output](./screenshots/Output%20image%2002.jpg)
![Terminal Output](./screenshots/Output%20image.jpg)



## Project Documentation

### Objective
The objective of this project is to simulate a distributed system using SQLite databases. The system stores three types of data—`Users`, `Products`, and `Orders`—in separate databases, with concurrent insert operations handled by multithreading. This showcases efficient handling of distributed database management and application-level data validations.

### Features
- **Distributed Data Storage**: Three separate SQLite databases for `Users`, `Products`, and `Orders`.
- **Concurrent Data Insertion**: Uses multithreading to perform simultaneous insert operations.
- **Application-Level Validations**: Ensures data integrity with validation checks for all input data.
- **Error Handling**: Handles validation errors gracefully and reports them in the console.
- **Scalability**: The design allows for easy extension to other data models.

### Technologies Used
- **Python**: Core programming language.
- **SQLite**: Lightweight database for data storage.
- **Threading**: Python's threading module for concurrent operations.

---

## Example Data
### Users Table (`users.db`):
| id | name      | email             |
|----|-----------|-------------------|
| 1  | Alice     | alice@example.com |
| 2  | Bob       | bob@example.com   |
| 3  | Charlie   | charlie@example.com |
| ...| ...       | ...               |

### Products Table (`products.db`):
| id | name         | price  |
|----|--------------|--------|
| 1  | Laptop       | 1000.0 |
| 2  | Smartphone   | 700.0  |
| 3  | Headphones   | 150.0  |
| ...| ...          | ...    |

### Orders Table (`orders.db`):
| id | user_id | product_id | quantity |
|----|---------|------------|----------|
| 1  | 1       | 1          | 2        |
| 2  | 2       | 2          | 1        |
| 3  | 3       | 3          | 5        |
| ...| ...     | ...        | ...      |

---

## Directory Structure
```
my-django-assignment/
├── README.md
├── distributed_inserts.py
├── users.db
├── products.db
├── orders.db
└── ...



## Future Enhancements
1. **Logging**: Implement detailed logging for better error tracking.
2. **API Integration**: Expose CRUD operations via REST APIs.
3. **Authentication**: Add user authentication and authorization.
4. **Scalability**: Migrate from SQLite to a more robust database like PostgreSQL for larger datasets.


## Support
If you encounter any issues, feel free to raise an issue in the [GitHub repository](https://github.com/atulshukla81/my-django-assignment).



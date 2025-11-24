# smart-canteen-queue-managemnt
A Python-based Smart Canteen Queue Management System to help students check queue length, estimate waiting time, and view seat availability. In this project, we learn to apply basic algorithms, Python control flow, and problem-solving techniques to build a real-world solution to efficiently manage canteen crowd.

# Smart Canteen Queue Management & Waiting Time Prediction System

Overview

This project implements a *Smart Canteen Queue Management System* to help students and canteen staff manage queues effectively during lunchtime. The system offers real-time information on queue lengths, estimated waiting time, seat availability, and recommends the best counter to join.

Features✨

Major Functional Modules

1. *Queue Management Module*
- Add customers to queue
Customers to serve from the queue
- Use multiple counters simultaneously

Real-time monitoring of queue length
2. *Waiting Time Prediction Module *
Dynamic serving time calculation based on order complexity

- Estimated waiting time for each counter
- Algorithm considers item types and quantities
3. **Seat Availability Module

- Track total and occupied seats
Display vacant seats in real time

- Visual occupancy representation

4. *Best Line Recommendation Module*
- Automatically suggests counter with the shortest wait time.
- Compares all counters and suggests optimal choice
## ????️ Technologies/Tools Used
- *Programming Language*: Python 3.x
- **Key Libraries:
- collections.deque - For efficient queue operations
- datetime - For time tracking
- **Concepts Applied:

Object-oriented programming - Classes, Objects

Data Structures - Lists, Dictionaries, Queues
- Algorithms: Searching, Sorting, Time Calculation
Top-Down Design & Modularization
- Error Handling & Validation
Project Structure

smart_canteen/
├── main.py                 # Main entry point
├── queue_system.py         # Core queue logic. Definition of classes for Customer, Counter, SeatManager and QueueSystem.
├── display.py              # Display and UI management
├── logger.py               # Logging functionality
├── test_queue_system.py    # Tests de validation
├── utils/
│   ├── __init__.py
│   └── utils.py            # Utility functions (clear_screen, format_time, etc.)
├── screenshots/            # Screenshots directory

├── recordings/             # Screen recordings directory

├── logs/                   # System logs directory
├── README.md               # This file

├── statement.md            # Problem statement and scope

└── DESIGN_DIAGRAMS.md      # Design diagrams documentation

Installation & Setup
Prerequisites

- Python 3.6 or above
- No external dependencies required (uses only Python standard library)
Steps to Install & Run

1. *Clone or download the repository*
bash
git clone <repository-url>

cd smart_canteen



2. **Change to project directory

bash
cd "New folder"

3. *Run the main program *
bash
python main.py

That's it! Nothing extra to install.
How to Use
Running the Program
1. Run python main.py in terminal
2. You will see the main menu with 6 options:
- **Option 1: Add Customer to Queue
- Enter customer name
- Choose items from menu
- System automatically assigns to the best counter
- *Option 2*: Serve Customer
- Choose a counter
- Start serving or finish serving current customer
- seats are automatically occupied when customer is served
- *Option 3*: View Queue Status

- See queue length for all counters

- View estimated wait times
- Check which customer is being served.
- *Option 4*: View Seat Availability
- See Total, Occupied and Vacant Seats

- View occupancy percentage

Visual indicator of seat availability

- *Option 5*: Get Best Line Recommendation

- System suggests counter with the least waiting time
- Provides comparison against other counters

- *Option 6*: Exit Program
Example Workflow
1. Add 3-4 customers to different counters
2. View queue status to see wait times
3. Serve customers from counters

4. Seat availability check

5. Get recommendation for new customer
Testing
Running Validation Tests
Execute the test file to validate system functionality:

bash
python test_queue_system.py


The test suite includes the following:
Customer Creation and Calculation of Complexity
- Counter queue operations

- Seat management

- Wait time calculation
- System initialization
Key Algorithms
1. Dynamic Serving Time Algorithm
- Calculates serving time based on:

- Quantity ordered

Item complexity Combos desserts Beverages
- Base serving time + complexity multiplier
2. Estimation of Waiting Times
- Sums up serving times of all customers ahead in queue
- Includes remaining time for currently serving customer

- Accurately give time predictions

3. Best Counter Selection

- Compares estimated wait times across all counters

- Chooses counter with the least wait time
- Uses linear search algorithm
Functional Requirements
✅ Queue Management: Add, serve, and track customers across multiple counters.
✅ *Waiting Time Prediction*: Real-time estimation based on order complexity

✅ *Seat Management*: tracking and display of seat availability

The best line recommendation: intelligent counter selection.
✅ *User Interface*: Clear menu-driven interface

✔️ *Data Validation*: Input validation and error handling

## ???? Non-Functional Requirements
Performance: Using deque data structure for efficient queue operations
Usability: Easy, menu-driven interface with clear instructions
???? Error Handling: Input validation; exception handling - graceful error messages
✅ *Logging*: The system logs every operation to facilitate monitoring and debugging.

✅ *Reliability*: Consistent behavior, proper state management

✅ *Maintainability*: Modular code structure, clear comments, organized files

Screenshots

Screenshots of the system in action is being placed  in the /screenshots directory.

Learning Outcomes

This project demonstrates: - *Problem Solving: Identifying real-world problem and designing solution - **Programming Concepts: Classes, objects, data structures, algorithms - **Software Design: Top-down design, modularization, separation of concerns - **User Interface: Menu-driven console application - **Testing: Validation & testing approach Target Users - **Students* check queue status and receive recommendations - *Canteen staff -* Managing the queues and serving the customers - *Administrators*: For supervision of canteen services Future Enhancements ???? - Web-based interface - Mobile application integration - Real-time notifications - Historical data analysis - Integration with payment systems - Multi-language support License This project is created for educational purposes. ## ????‍???? Author Student Project: Smart Canteen Queue Management System --- Note: This is a beginner-friendly project intended to illustrate basics of programming and problem-solving.

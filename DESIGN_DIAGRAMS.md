# Design Diagrams Documentation

This document contains all the design diagrams for the Smart Canteen Queue Management & Waiting Time Prediction System.

---

## 1. System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    SMART CANTEEN SYSTEM                          │
│                                                                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Counter 1  │    │   Counter 2  │    │   Counter 3  │      │
│  │   (North)    │    │   (South)    │    │   (East)     │      │
│  │              │    │              │    │              │      │
│  │  Queue: []   │    │  Queue: []   │    │  Queue: []   │      │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘      │
│         │                   │                   │               │
│         └───────────────────┼───────────────────┘               │
│                             │                                   │
│                    ┌────────▼────────┐                          │
│                    │  Queue System   │                          │
│                    │   (Manager)     │                          │
│                    └────────┬────────┘                          │
│                             │                                   │
│         ┌───────────────────┼───────────────────┐               │
│         │                   │                   │               │
│  ┌──────▼──────┐    ┌───────▼──────┐   ┌───────▼──────┐        │
│  │   Customer  │    │ Seat Manager │   │   Display    │        │
│  │  Management │    │              │   │   Manager    │        │
│  └─────────────┘    └──────────────┘   └──────────────┘        │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              Logger (System Logging)                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Main Program  │
                    │   (Entry Point) │
                    └─────────────────┘
```

**Explanation**: 
- The system has 3 counters, each with its own queue
- QueueSystem manages all counters, customers, and seats
- DisplayManager handles user interface
- Logger tracks all operations
- Main program coordinates everything

---

## 2. Process Flow / Workflow Diagram

```
                    START
                      │
                      ▼
            ┌─────────────────────┐
            │  Initialize System  │
            │  - Create Counters  │
            │  - Initialize Seats │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │   Show Main Menu   │
            └──────────┬──────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   [Option 1]     [Option 2]     [Option 3-5]
   Add Customer   Serve Customer  View Status
        │              │              │
        │              │              │
        ▼              ▼              ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │ Get Name│   │ Select  │   │ Display │
   │ & Items │   │ Counter │   │ Info    │
   └────┬────┘   └────┬────┘   └────┬────┘
        │             │              │
        ▼             ▼              │
   ┌─────────┐   ┌─────────┐        │
   │Calculate│   │ Serve   │        │
   │Complexity│   │Customer│        │
   └────┬────┘   └────┬────┘        │
        │             │              │
        ▼             ▼              │
   ┌─────────┐   ┌─────────┐        │
   │Find Best│   │Occupy   │        │
   │Counter  │   │Seat     │        │
   └────┬────┘   └────┬────┘        │
        │             │              │
        └──────┬──────┴──────┬───────┘
               │             │
               ▼             ▼
        ┌──────────────┐
        │ Update Queue │
        │   & Status   │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Return to    │
        │  Main Menu   │
        └──────┬───────┘
               │
               ▼
          [Option 6?]
               │
        ┌──────┴──────┐
        │             │
       YES           NO
        │             │
        ▼             │
    ┌─────────┐       │
    │  EXIT   │       │
    └─────────┘       │
                      │
                      └──────┐
                             │
                             ▼
                    (Continue Loop)
```

**Explanation**:
- System starts by initializing counters and seats
- Main menu loop continues until user exits
- Each option performs specific operations
- System updates after each operation
- Returns to main menu after each action

---

## 3. Use Case Diagram

```
                    ┌─────────────────────┐
                    │                     │
                    │   Smart Canteen     │
                    │   Queue System      │
                    │                     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │   Student   │ │    Staff    │ │ Administrator│
        └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
               │               │               │
               │               │               │
    ┌──────────┼──────────┐   │               │
    │          │          │   │               │
    ▼          ▼          ▼   ▼               ▼
View Queue  Get Best   Check  Add Customer Serve Customer
 Status     Line Rec   Seats    to Queue      from Queue
    │          │          │       │               │
    │          │          │       │               │
    └──────────┴──────────┴───────┴───────────────┘
                      │
                      ▼
              ┌───────────────┐
              │ View System   │
              │   Logs        │
              └───────────────┘
```

**Actors**:
- **Student**: Primary user who checks queue status and gets recommendations
- **Staff**: Manages queues and serves customers
- **Administrator**: Monitors system and views logs

**Use Cases**:
- View Queue Status
- Get Best Line Recommendation
- Check Seat Availability
- Add Customer to Queue
- Serve Customer from Queue
- View System Logs

---

## 4. Class Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Customer                               │
├─────────────────────────────────────────────────────────────┤
│ - customer_id: int                                          │
│ - name: str                                                 │
│ - items: list                                               │
│ - entry_time: datetime                                      │
│ - complexity_score: float                                   │
├─────────────────────────────────────────────────────────────┤
│ + __init__(customer_id, name, items)                        │
│ + _calculate_complexity(): float                           │
│ + get_estimated_serving_time(): int                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                         Counter                              │
├─────────────────────────────────────────────────────────────┤
│ - counter_id: int                                           │
│ - name: str                                                 │
│ - queue: deque                                              │
│ - serving_customer: Customer                                │
│ - serving_start_time: datetime                              │
├─────────────────────────────────────────────────────────────┤
│ + __init__(counter_id, name)                                │
│ + add_customer(customer: Customer)                          │
│ + serve_next(): Customer                                    │
│ + finish_serving(): Customer                                │
│ + get_queue_length(): int                                   │
│ + get_estimated_wait_time(): float                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      SeatManager                             │
├─────────────────────────────────────────────────────────────┤
│ - total_seats: int                                          │
│ - occupied_seats: int                                       │
├─────────────────────────────────────────────────────────────┤
│ + __init__(total_seats: int)                                │
│ + occupy_seat(count: int): bool                             │
│ + free_seat(count: int)                                     │
│ + get_vacant_seats(): int                                   │
│ + get_occupancy_percentage(): float                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       QueueSystem                            │
├─────────────────────────────────────────────────────────────┤
│ - counters: list[Counter]                                    │
│ - seat_manager: SeatManager                                 │
│ - next_customer_id: int                                     │
│ - menu_items: list[str]                                     │
├─────────────────────────────────────────────────────────────┤
│ + __init__()                                                 │
│ + add_customer_to_queue()                                   │
│ + serve_customer()                                           │
│ + get_all_queue_status(): list[dict]                        │
│ + get_best_line_recommendation(): Counter                   │
│ - _find_best_counter(): Counter                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ uses
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DisplayManager                          │
├─────────────────────────────────────────────────────────────┤
│ (no attributes)                                             │
├─────────────────────────────────────────────────────────────┤
│ + show_main_menu()                                          │
│ + show_queue_status(system: QueueSystem)                    │
│ + show_seat_availability(system: QueueSystem)               │
│ + show_best_line_recommendation(system: QueueSystem)        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                          Logger                              │
├─────────────────────────────────────────────────────────────┤
│ - log_file: str                                             │
├─────────────────────────────────────────────────────────────┤
│ + __init__(log_file: str)                                   │
│ + log(level: str, message: str)                             │
│ + info(message: str)                                        │
│ + error(message: str)                                       │
│ + warning(message: str)                                     │
└─────────────────────────────────────────────────────────────┘
```

**Relationships**:
- QueueSystem **contains** multiple Counter objects
- QueueSystem **has** one SeatManager
- Counter **contains** Customer objects in queue
- DisplayManager **uses** QueueSystem to display information
- All classes are independent modules (composition pattern)

---

## 5. Sequence Diagram - Add Customer Flow

```
Student          Main Program      QueueSystem      Counter      DisplayManager
   │                  │                 │              │                │
   │  Select Option 1 │                 │              │                │
   │─────────────────>│                 │              │                │
   │                  │                 │              │                │
   │                  │  add_customer() │              │                │
   │                  │────────────────>│              │                │
   │                  │                 │              │                │
   │  Enter Name      │                 │              │                │
   │<─────────────────│                 │              │                │
   │  "John"          │                 │              │                │
   │─────────────────>│                 │              │                │
   │                  │                 │              │                │
   │  Select Items    │                 │              │                │
   │<─────────────────│                 │              │                │
   │  "1,3,5"         │                 │              │                │
   │─────────────────>│                 │              │                │
   │                  │                 │              │                │
   │                  │  Create Customer│              │                │
   │                  │────────────────>│              │                │
   │                  │                 │              │                │
   │                  │  _find_best_counter()          │                │
   │                  │────────────────────────────────>│                │
   │                  │                 │              │                │
   │                  │                 │  get_estimated_wait_time()
   │                  │                 │<─────────────│                │
   │                  │                 │              │                │
   │                  │                 │  Return Counter
   │                  │<────────────────────────────────│                │
   │                  │                 │              │                │
   │                  │  add_customer() │              │                │
   │                  │────────────────────────────────>│                │
   │                  │                 │              │                │
   │                  │  Success Message                │                │
   │                  │─────────────────────────────────────────────────>│
   │                  │                 │              │                │
   │  Display Result  │                 │              │                │
   │<─────────────────│                 │              │                │
   │                  │                 │              │                │
```

**Explanation**:
1. Student selects option to add customer
2. System prompts for name and items
3. System creates Customer object
4. System finds best counter (compares wait times)
5. Customer added to selected counter's queue
6. Success message displayed

---

## 6. Sequence Diagram - Serve Customer Flow

```
Staff            Main Program      QueueSystem      Counter      SeatManager
   │                  │                 │              │              │
   │  Select Option 2 │                 │              │              │
   │─────────────────>│                 │              │              │
   │                  │                 │              │              │
   │                  │  serve_customer()              │              │
   │                  │────────────────>│              │              │
   │                  │                 │              │              │
   │  Select Counter  │                 │              │              │
   │<─────────────────│                 │              │              │
   │  "1"             │                 │              │              │
   │─────────────────>│                 │              │              │
   │                  │                 │              │              │
   │                  │  finish_serving()              │              │
   │                  │────────────────────────────────>│              │
   │                  │                 │              │              │
   │                  │                 │  Return Customer
   │                  │<────────────────────────────────│              │
   │                  │                 │              │              │
   │                  │  occupy_seat(1) │              │              │
   │                  │────────────────────────────────────────────────>│
   │                  │                 │              │              │
   │                  │                 │              │  Return True/False
   │                  │<────────────────────────────────────────────────│
   │                  │                 │              │              │
   │  Success Message │                 │              │              │
   │<─────────────────│                 │              │              │
   │                  │                 │              │              │
```

**Explanation**:
1. Staff selects option to serve customer
2. System shows available counters
3. Staff selects a counter
4. System finishes serving current customer
5. System automatically occupies a seat
6. Success message displayed

---

## 7. ER Diagram (Entity Relationship)

Since this system uses in-memory data structures (not a database), here's a conceptual ER diagram:

```
┌──────────────┐         ┌──────────────┐
│   Customer   │         │   Counter    │
├──────────────┤         ├──────────────┤
│ customer_id  │◄──┐     │ counter_id   │
│ name         │   │     │ name         │
│ items[]      │   │     │ queue[]      │
│ entry_time   │   │     │ serving_     │
│ complexity   │   │     │   customer   │
└──────────────┘   │     └──────┬───────┘
                   │            │
                   │            │ contains
                   │            │ (1 to many)
                   │            │
                   │     ┌──────▼───────┐
                   │     │   Queue      │
                   │     │   (deque)    │
                   │     │              │
                   │     │ - customers[]│
                   └─────┼──────────────┘
                         │
                         │
┌──────────────┐         │
│     Seat     │         │
│   Manager    │         │
├──────────────┤         │
│ total_seats  │         │
│ occupied     │         │
│ vacant       │         │
└──────────────┘         │
                         │
                         │
              ┌──────────▼──────────┐
              │    Queue System     │
              │    (Main Manager)   │
              ├─────────────────────┤
              │ - manages counters  │
              │ - manages seats     │
              │ - manages customers │
              └─────────────────────┘
```

**Relationships**:
- **Counter** contains **Queue** (1-to-1)
- **Queue** contains **Customers** (1-to-many)
- **QueueSystem** manages **Counters** (1-to-many)
- **QueueSystem** manages **SeatManager** (1-to-1)

---

## 8. Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   main.py    │  │  display.py  │  │  logger.py   │      │
│  │ (Entry Point)│  │   (UI Layer) │  │ (Logging)    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼──────────────────┼─────────────────┼──────────────┘
          │                  │                 │
          │                  │                 │
┌─────────▼──────────────────▼─────────────────▼──────────────┐
│                    Business Logic Layer                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            queue_system.py                           │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐         │   │
│  │  │ Customer │  │ Counter   │  │   Seat    │         │   │
│  │  │  Class   │  │  Class   │  │  Manager  │         │   │
│  │  └──────────┘  └──────────┘  └──────────┘         │   │
│  │                                                     │   │
│  │            QueueSystem (Main Manager)               │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
          │
          │
┌─────────▼──────────────────────────────────────────────────┐
│                    Utility Layer                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              utils/utils.py                           │  │
│  │  - clear_screen()                                     │  │
│  │  - format_time()                                     │  │
│  │  - print_header()                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
          │
          │
┌─────────▼──────────────────────────────────────────────────┐
│              Python Standard Library                        │
│  - collections.deque                                        │
│  - datetime                                                 │
│  - os, sys                                                  │
└──────────────────────────────────────────────────────────────┘
```

**Layers**:
1. **Application Layer**: User interface and entry point
2. **Business Logic Layer**: Core functionality and algorithms
3. **Utility Layer**: Helper functions
4. **Standard Library**: Python built-in modules

---

## 9. Data Flow Diagram (DFD)

```
┌──────────┐
│  Student │
│ / Staff  │
└────┬─────┘
     │
     │ Input: Name, Items, Counter Choice
     ▼
┌─────────────────────────────────────┐
│      Main Program (main.py)         │
│  - Menu Display                     │
│  - Input Validation                 │
└────┬────────────────────────────────┘
     │
     │ Process Request
     ▼
┌─────────────────────────────────────┐
│    Queue System (queue_system.py)   │
│  - Customer Creation                 │
│  - Queue Management                  │
│  - Wait Time Calculation             │
└────┬────────────────────────────────┘
     │
     │ Update Data
     ▼
┌─────────────────────────────────────┐
│      Data Storage (In-Memory)        │
│  - Customer Objects                  │
│  - Counter Queues                    │
│  - Seat Status                       │
└────┬────────────────────────────────┘
     │
     │ Retrieve Data
     ▼
┌─────────────────────────────────────┐
│   Display Manager (display.py)      │
│  - Format Output                     │
│  - Show Status                       │
└────┬────────────────────────────────┘
     │
     │ Display Information
     ▼
┌──────────┐
│  Student │
│ / Staff  │
└──────────┘
```

**Data Flow**:
1. User provides input
2. Main program validates and processes
3. Queue system updates data structures
4. Data stored in memory (objects, queues)
5. Display manager retrieves and formats
6. Information shown to user

---

## Summary

All diagrams show:
- **Clear Structure**: How components are organized
- **Data Flow**: How information moves through system
- **User Interactions**: How users interact with system
- **Class Relationships**: How code components relate
- **Process Flow**: Step-by-step operations

These diagrams help understand the system design at different levels of detail.


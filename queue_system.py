"""
Smart Canteen Queue Management System - Core Queue Logic
========================================================

This module implements the main queue management system with:
- Multiple counter queues
- Dynamic serving time calculation based on item complexity
- Seat management
- Waiting time estimation

Concepts Applied:
- Top-Down Design (modular functions)
- Data Structures (lists, dictionaries)
- Control Flow (if-else, loops)
- Functions and Parameters
- Algorithm Implementation
"""

from collections import deque
from datetime import datetime


class Customer:
    """
    Customer Class
    Represents a customer in the queue with their order details
    
    Demonstrates: Class definition, attributes, methods
    """
    
    def __init__(self, customer_id, name, items):
        """
        Initialize a customer
        Parameters: customer_id (int), name (str), items (list)
        """
        self.customer_id = customer_id
        self.name = name
        self.items = items  # List of items ordered
        self.entry_time = datetime.now()
        self.complexity_score = self._calculate_complexity()
    
    def _calculate_complexity(self):
        """
        Calculate complexity score based on number and type of items
        More items = higher complexity = longer serving time
        
        Demonstrates: Conditional statements, counting algorithm
        """
        # Base complexity: 1 point per item
        complexity = len(self.items)
        
        # Add extra complexity for certain item types
        for item in self.items:
            item_lower = item.lower()
            if 'combo' in item_lower or 'special' in item_lower:
                complexity += 2  # Combos take more time
            elif 'beverage' in item_lower or 'drink' in item_lower:
                complexity += 0.5  # Drinks are quick
            elif 'dessert' in item_lower:
                complexity += 1  # Desserts need packaging
        
        return complexity
    
    def get_estimated_serving_time(self):
        """
        Estimate serving time in seconds based on complexity
        Base time: 30 seconds, +10 seconds per complexity point
        
        Demonstrates: Expression evaluation, return statements
        """
        base_time = 30  # Base serving time in seconds
        time_per_complexity = 10
        estimated_seconds = base_time + (self.complexity_score * time_per_complexity)
        return estimated_seconds


class Counter:
    """
    Counter Class
    Represents a food counter with its own queue
    
    Demonstrates: Class definition, queue data structure (deque)
    """
    
    def __init__(self, counter_id, name):
        """
        Initialize a counter
        Parameters: counter_id (int), name (str)
        """
        self.counter_id = counter_id
        self.name = name
        self.queue = deque()  # Using deque for efficient queue operations
        self.serving_customer = None
        self.serving_start_time = None
    
    def add_customer(self, customer):
        """
        Add customer to this counter's queue
        Parameter: customer (Customer object)
        """
        self.queue.append(customer)
        print(f"✅ {customer.name} added to {self.name} queue")
    
    def serve_next(self):
        """
        Start serving the next customer in queue
        Returns: Customer object if available, None otherwise
        
        Demonstrates: Conditional statements, return values
        """
        if self.queue:
            self.serving_customer = self.queue.popleft()
            self.serving_start_time = datetime.now()
            return self.serving_customer
        return None
    
    def finish_serving(self):
        """
        Finish serving current customer
        Returns: Customer object that was served
        """
        if self.serving_customer:
            served = self.serving_customer
            self.serving_customer = None
            self.serving_start_time = None
            return served
        return None
    
    def get_queue_length(self):
        """
        Get current queue length
        Returns: int (number of customers waiting)
        
        Demonstrates: Counting algorithm
        """
        return len(self.queue)
    
    def get_estimated_wait_time(self):
        """
        Calculate estimated waiting time for new customer
        Sum of all customers' serving times ahead in queue
        
        Demonstrates: Summation algorithm, iteration
        """
        total_time = 0
        
        # Add time for currently serving customer
        if self.serving_customer:
            elapsed = (datetime.now() - self.serving_start_time).total_seconds()
            remaining = self.serving_customer.get_estimated_serving_time() - elapsed
            if remaining > 0:
                total_time += remaining
        
        # Add time for all customers in queue
        for customer in self.queue:
            total_time += customer.get_estimated_serving_time()
        
        return total_time


class SeatManager:
    """
    Seat Manager Class
    Manages seat availability in the canteen
    
    Demonstrates: Class definition, state management
    """
    
    def __init__(self, total_seats):
        """
        Initialize seat manager
        Parameter: total_seats (int) - total number of seats available
        """
        self.total_seats = total_seats
        self.occupied_seats = 0
    
    def occupy_seat(self, count=1):
        """
        Occupy seats
        Parameter: count (int) - number of seats to occupy
        Returns: bool - True if successful, False if not enough seats
        
        Demonstrates: Conditional statements, parameter validation
        """
        if self.occupied_seats + count <= self.total_seats:
            self.occupied_seats += count
            return True
        return False
    
    def free_seat(self, count=1):
        """
        Free up seats
        Parameter: count (int) - number of seats to free
        """
        if self.occupied_seats >= count:
            self.occupied_seats -= count
        else:
            self.occupied_seats = 0
    
    def get_vacant_seats(self):
        """
        Get number of vacant seats
        Returns: int
        
        Demonstrates: Expression evaluation, return statement
        """
        return self.total_seats - self.occupied_seats
    
    def get_occupancy_percentage(self):
        """
        Calculate occupancy percentage
        Returns: float (0-100)
        
        Demonstrates: Percentage calculation, type conversion
        """
        if self.total_seats == 0:
            return 0.0
        return (self.occupied_seats / self.total_seats) * 100


class QueueSystem:
    """
    Main Queue System Class
    Manages all counters, customers, and seats
    
    Demonstrates: Top-down design, modularization, class composition
    """
    
    def __init__(self):
        """
        Initialize the queue system
        Creates counters and seat manager
        """
        # Initialize counters (multiple food counters)
        self.counters = [
            Counter(1, "Counter 1 - North"),
            Counter(2, "Counter 2 - South"),
            Counter(3, "Counter 3 - East")
        ]
        
        # Initialize seat manager (50 total seats)
        self.seat_manager = SeatManager(50)
        
        # Customer ID counter (for unique IDs)
        self.next_customer_id = 1
        
        # Sample menu items for selection
        self.menu_items = [
            "Rice & Curry", "Biryani", "Pasta", "Pizza Slice",
            "Burger", "Sandwich", "Combo Meal", "Special Thali",
            "Beverage", "Soft Drink", "Dessert", "Ice Cream"
        ]
    
    def add_customer_to_queue(self):
        """
        Add a new customer to the best counter queue
        Interactive function that takes user input
        
        Demonstrates: User input, function calls, conditional logic
        """
        print("\n" + "="*50)
        print("ADD CUSTOMER TO QUEUE")
        print("="*50)
        
        # Get customer name
        name = input("Enter customer name: ").strip()
        if not name:
            name = f"Customer {self.next_customer_id}"
        
        # Display menu
        print("\nAvailable Menu Items:")
        for i, item in enumerate(self.menu_items, 1):
            print(f"  {i}. {item}")
        
        # Get items ordered
        items = []
        print("\nEnter item numbers (comma-separated, e.g., 1,3,5):")
        item_input = input("Items: ").strip()
        
        if item_input:
            try:
                item_indices = [int(x.strip()) - 1 for x in item_input.split(',')]
                for idx in item_indices:
                    if 0 <= idx < len(self.menu_items):
                        items.append(self.menu_items[idx])
            except ValueError:
                print("⚠️ Invalid input. Using default items.")
                items = ["Rice & Curry"]
        else:
            items = ["Rice & Curry"]  # Default
        
        # Create customer
        customer = Customer(self.next_customer_id, name, items)
        self.next_customer_id += 1
        
        # Find best counter (shortest estimated wait time)
        best_counter = self._find_best_counter()
        
        # Add to queue
        best_counter.add_customer(customer)
        
        print(f"\n Customer Details:")
        print(f"   Name: {customer.name}")
        print(f"   Items: {', '.join(customer.items)}")
        print(f"   Complexity Score: {customer.complexity_score:.1f}")
        print(f"   Estimated Serving Time: {customer.get_estimated_serving_time()} seconds")
        print(f"   Assigned to: {best_counter.name}")
        
        input("\nPress Enter to continue...")
    
    def _find_best_counter(self):
        """
        Find the counter with shortest estimated wait time
        Returns: Counter object
        
        Demonstrates: Algorithm for finding minimum, iteration
        """
        best_counter = self.counters[0]
        min_wait_time = best_counter.get_estimated_wait_time()
        
        for counter in self.counters[1:]:
            wait_time = counter.get_estimated_wait_time()
            if wait_time < min_wait_time:
                min_wait_time = wait_time
                best_counter = counter
        
        return best_counter
    
    def serve_customer(self):
        """
        Serve a customer from a counter
        Interactive function
        
        Demonstrates: User input, function calls, error handling
        """
        print("\n" + "="*50)
        print("SERVE CUSTOMER")
        print("="*50)
        
        # Show available counters
        print("\nAvailable Counters:")
        for counter in self.counters:
            queue_len = counter.get_queue_length()
            serving = " (Serving)" if counter.serving_customer else ""
            print(f"  {counter.counter_id}. {counter.name} - Queue: {queue_len}{serving}")
        
        try:
            counter_choice = int(input("\nSelect counter (1-3): ").strip())
            if 1 <= counter_choice <= len(self.counters):
                counter = self.counters[counter_choice - 1]
                
                # Start serving if not already serving
                if not counter.serving_customer:
                    customer = counter.serve_next()
                    if customer:
                        print(f"\n Started serving {customer.name}")
                        print(f"   Items: {', '.join(customer.items)}")
                    else:
                        print("\n No customers in queue!")
                else:
                    # Finish serving current customer
                    served = counter.finish_serving()
                    if served:
                        print(f"\n Finished serving {served.name}")
                        # Automatically occupy a seat
                        if self.seat_manager.occupy_seat(1):
                            print(f"   Seat occupied. Vacant seats: {self.seat_manager.get_vacant_seats()}")
                        else:
                            print("    No vacant seats available!")
            else:
                print("\n Invalid counter selection!")
        except ValueError:
            print("\n Invalid input! Please enter a number.")
        
        input("\nPress Enter to continue...")
    
    def get_all_queue_status(self):
        """
        Get status of all counters
        Returns: list of dictionaries with counter information
        
        Demonstrates: Data aggregation, list comprehension concepts
        """
        status_list = []
        for counter in self.counters:
            status_list.append({
                'counter': counter,
                'queue_length': counter.get_queue_length(),
                'wait_time': counter.get_estimated_wait_time(),
                'serving': counter.serving_customer is not None
            })
        return status_list
    
    def get_best_line_recommendation(self):
        """
        Recommend the best line (counter) to join
        Returns: Counter object with shortest wait time
        
        Demonstrates: Algorithm implementation, comparison
        """
        return self._find_best_counter()


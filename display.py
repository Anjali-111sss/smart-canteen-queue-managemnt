"""
Display Manager Module
======================
Handles all user interface and display functions

Concepts Applied:
- Class definition
- String formatting
- User interface design
"""

from utils import format_time


class DisplayManager:
    """
    Display Manager Class
    Manages all display and user interface operations
    
    Demonstrates: Class definition, methods, user interaction
    """
    
    def show_main_menu(self):
        """
        Display the main menu options
        
        Demonstrates: String formatting, menu design
        """
        print("\n" + "─" * 50)
        print(" MAIN MENU")
        print("─" * 50)
        print("  1. Add Customer to Queue")
        print("  2. Serve Customer")
        print("  3. View Queue Status")
        print("  4. View Seat Availability")
        print("  5. Get Best Line Recommendation")
        print("  6. Exit")
        print("─" * 50)
    
    def show_queue_status(self, system):
        """
        Display queue status for all counters
        
        Parameter: system (QueueSystem) - The queue system object
        
        Demonstrates: Data display, iteration, formatting
        """
        print("\n" + "=" * 60)
        print(" QUEUE STATUS - ALL COUNTERS")
        print("=" * 60)
        
        status_list = system.get_all_queue_status()
        
        for status in status_list:
            counter = status['counter']
            queue_len = status['queue_length']
            wait_time = status['wait_time']
            serving = status['serving']
            
            print(f"\n{counter.name}:")
            print(f"  Queue Length: {queue_len} customer(s)")
            print(f"  Estimated Wait Time: {format_time(wait_time)}")
            
            if serving:
                customer = counter.serving_customer
                print(f"  Currently Serving: {customer.name}")
                print(f"    Items: {', '.join(customer.items)}")
            else:
                print(f"  Status: Available (No one being served)")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to continue...")
    
    def show_seat_availability(self, system):
        """
        Display seat availability information
        
        Parameter: system (QueueSystem) - The queue system object
        
        Demonstrates: Data display, percentage calculation
        """
        print("\n" + "=" * 60)
        print(" SEAT AVAILABILITY")
        print("=" * 60)
        
        seat_manager = system.seat_manager
        total_seats = seat_manager.total_seats
        occupied = seat_manager.occupied_seats
        vacant = seat_manager.get_vacant_seats()
        occupancy = seat_manager.get_occupancy_percentage()
        
        print(f"\nTotal Seats: {total_seats}")
        print(f"Occupied Seats: {occupied}")
        print(f"Vacant Seats: {vacant}")
        print(f"Occupancy: {occupancy:.1f}%")
        
        # Visual representation
        print("\nVisual Representation:")
        filled = int(occupancy / 2)  # Scale to 50 characters
        empty = 50 - filled
        bar = "█" * filled + "░" * empty
        print(f"[{bar}] {occupancy:.1f}%")
        
        if vacant == 0:
            print("\n⚠️  WARNING: No vacant seats available!")
        elif vacant < 10:
            print("\n⚠️  WARNING: Very few seats available!")
        else:
            print("\n✅ Seats available")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to continue...")
    
    def show_best_line_recommendation(self, system):
        """
        Display the best line recommendation
        
        Parameter: system (QueueSystem) - The queue system object
        
        Demonstrates: Algorithm result display, comparison
        """
        print("\n" + "=" * 60)
        print(" BEST LINE RECOMMENDATION")
        print("=" * 60)
        
        best_counter = system.get_best_line_recommendation()
        wait_time = best_counter.get_estimated_wait_time()
        queue_len = best_counter.get_queue_length()
        
        print(f"\n✅ Recommended Counter: {best_counter.name}")
        print(f"   Queue Length: {queue_len} customer(s)")
        print(f"   Estimated Wait Time: {format_time(wait_time)}")
        
        # Show comparison with other counters
        print("\nComparison with other counters:")
        status_list = system.get_all_queue_status()
        for status in status_list:
            counter = status['counter']
            if counter.counter_id != best_counter.counter_id:
                print(f"  {counter.name}: {format_time(status['wait_time'])} "
                      f"({status['queue_length']} customers)")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to continue...")


"""Smart Canteen Queue Management System
Main Entry Point
This program implements a queue management system for canteen to help students
know queue length, waiting time, vacant seats, and best line recommendation."""

from queue_system import QueueSystem
from display import DisplayManager
from utils import clear_screen, print_header

def main():
    """Main function - Entry point of the program
    Demonstrates top-down design approach"""
    # Initialize the queue management system
    system = QueueSystem()
    display = DisplayManager()
    
    # Main program loop
    while True:
        clear_screen()
        print_header("SMART CANTEEN QUEUE MANAGEMENT SYSTEM")
        
        # Display main menu
        display.show_main_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Add customer to queue
                system.add_customer_to_queue()
                
            elif choice == '2':
                # Serve customer (remove from queue)
                system.serve_customer()
                
            elif choice == '3':
                # View queue status
                display.show_queue_status(system)
                
            elif choice == '4':
                # View seat availability
                display.show_seat_availability(system)
                
            elif choice == '5':
                # Get best line recommendation which is less crowded and which will save your time.
                display.show_best_line_recommendation(system)
                
            elif choice == '6':
                # Exit program
                print("\nThank you for using Smart Canteen Queue Management System!")
                print("Exiting...")
                break
            else:
                print("\n Invalid choice! Please enter a number between 1-6.")
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\n An error occurred: {e}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()


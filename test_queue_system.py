"""Test Module for Queue System
Simple validation tests for the queue management system
Concepts Applied:
- Testing approach
- Function validation
- Assertion checking"""

from queue_system import Customer, Counter, SeatManager, QueueSystem

def test_customer_creation():
    """Test customer creation and complexity calculation"""
    print("Testing Customer Creation...")
    customer = Customer(1, "Test Student", ["Rice & Curry", "Beverage"])
    assert customer.customer_id == 1
    assert customer.name == "Test Student"
    assert len(customer.items) == 2
    assert customer.complexity_score > 0
    print("✅ Customer creation test passed!")


def test_counter_operations():
    """Test counter queue operations"""
    print("\nTesting Counter Operations...")
    counter = Counter(1, "Test Counter")
    
    # Test adding customers
    customer1 = Customer(1, "Student 1", ["Burger"])
    customer2 = Customer(2, "Student 2", ["Pizza"])
    
    counter.add_customer(customer1)
    counter.add_customer(customer2)
    
    assert counter.get_queue_length() == 2
    
    # Test serving
    served = counter.serve_next()
    assert served == customer1
    assert counter.get_queue_length() == 1
    
    print("✅ Counter operations test passed!")


def test_seat_manager():
    """Test seat management"""
    print("\nTesting Seat Manager...")
    seat_manager = SeatManager(50)
    
    # Test occupying seats
    assert seat_manager.occupy_seat(10) == True
    assert seat_manager.get_vacant_seats() == 40
    assert seat_manager.occupied_seats == 10
    
    # Test freeing seats
    seat_manager.free_seat(5)
    assert seat_manager.get_vacant_seats() == 45
    
    print("✅ Seat manager test passed!")


def test_wait_time_calculation():
    """Test waiting time estimation"""
    print("\nTesting Wait Time Calculation...")
    counter = Counter(1, "Test Counter")
    
    customer1 = Customer(1, "Student 1", ["Burger"])
    customer2 = Customer(2, "Student 2", ["Combo Meal", "Dessert"])
    
    counter.add_customer(customer1)
    counter.add_customer(customer2)
    
    wait_time = counter.get_estimated_wait_time()
    assert wait_time > 0
    
    print(f"✅ Wait time calculation test passed! (Wait time: {wait_time:.1f} seconds)")


def test_queue_system():
    """Test main queue system"""
    print("\nTesting Queue System...")
    system = QueueSystem()
    
    assert len(system.counters) == 3
    assert system.seat_manager.total_seats == 50
    assert system.next_customer_id == 1
    
    print("✅ Queue system initialization test passed!")


def run_all_tests():
    """Run all validation tests"""
    print("=" * 60)
    print(" RUNNING VALIDATION TESTS")
    print("=" * 60)
    
    try:
        test_customer_creation()
        test_counter_operations()
        test_seat_manager()
        test_wait_time_calculation()
        test_queue_system()
        
        print("\n" + "=" * 60)
        print(" ✅ ALL TESTS PASSED!")
        print("=" * 60)
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()


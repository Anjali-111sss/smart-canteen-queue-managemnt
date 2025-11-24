"""
Utility Functions
================
Helper functions for display and formatting

Concepts Applied:
- Function definition
- String formatting
- Cross-platform compatibility
"""

import os
import sys


def clear_screen():
    """
    Clear the terminal screen
    Works on both Windows and Unix-based systems
    
    Demonstrates: Conditional statements, OS interaction
    """
    if sys.platform == 'win32':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Mac


def print_header(title):
    """
    Print a formatted header with borders
    
    Parameter: title (str) - The title to display
    
    Demonstrates: String formatting, repetition operator
    """
    width = 60
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def format_time(seconds):
    """
    Format time in seconds to readable format (minutes and seconds)
    
    Parameter: seconds (float) - Time in seconds
    Returns: str - Formatted time string
    
    Demonstrates: Type conversion, string formatting, arithmetic operations
    """
    if seconds < 60:
        return f"{int(seconds)} seconds"
    else:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        if secs == 0:
            return f"{minutes} minute(s)"
        else:
            return f"{minutes} minute(s) {secs} second(s)"


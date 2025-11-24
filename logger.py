"""
Logging Module
==============
Handles logging and error tracking for the system

Concepts Applied:
- File I/O operations
- Error handling
- Logging patterns
"""

import os
from datetime import datetime


class Logger:
    """
    Logger Class
    Handles logging operations for the system
    
    Demonstrates: File operations, error handling, logging
    """
    
    def __init__(self, log_file="logs/system.log"):
        """
        Initialize logger
        Parameter: log_file (str) - Path to log file
        """
        self.log_file = log_file
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
    
    def log(self, level, message):
        """
        Write a log entry
        
        Parameters:
        - level (str): Log level (INFO, ERROR, WARNING)
        - message (str): Log message
        
        Demonstrates: File writing, string formatting, error handling
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [{level}] {message}\n"
            
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            # If logging fails, print to console
            print(f"Logging error: {e}")
    
    def info(self, message):
        """Log info message"""
        self.log("INFO", message)
    
    def error(self, message):
        """Log error message"""
        self.log("ERROR", message)
    
    def warning(self, message):
        """Log warning message"""
        self.log("WARNING", message)


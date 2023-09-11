"""
the sys module is a built-in module that provides access to various system-specific parameters and functions. 
It is often used for tasks related to interacting with the Python interpreter and the underlying operating system."""
import sys
from src.logger import logging


"""
In Python, exc_tb is an abbreviation for "exception traceback," 
It's part of the information that Python provides when an error or exception occurs in your code. 
When an exception happens, Python creates a traceback, which is like a log of what the program was doing when the error occurred. 
It shows the sequence of function calls and the line numbers in your code."""

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    """tb_frame: When an error happens, Python creates a traceback, which is a series of tb_frame snapshots. 
    This traceback helps you identify where the error occurred and what led up to it. 
    It's incredibly useful for debugging because it provides a trail of breadcrumbs 
    you can follow to understand and fix the problem in your code."""

    """f_code: Imagine you have a recipe (a function) written in a language that only a computer can understand. 
    This language is called "bytecode." 
    Your recipe needs to be translated into bytecode so that the computer can follow the instructions and make your dish (perform the function). 
    The f_code attribute is like the recipe book that holds the bytecode version of your recipe."""

    """co_filename: is an attribute associated with a code object (a piece of Python code, like a function or a module). 
    It stores the name of the file where the code object is defined.
    Imagine you have a Python script called "my_script.py," and within that script, 
    you define a function called "my_function." If you want to know in which file "my_function" is defined, 
    you can use the co_filename attribute of the code object representing "my_function"."""

    error_message= "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message



if __name__=="__main__":

    try:
        a=1/0

    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)
    
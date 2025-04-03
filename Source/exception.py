import sys
import logging

# Function to generate detailed error messages
def error_message_detail(error, error_detail: sys):
    """Formats an error message with script name, line number, and error message."""
    _, _, exc_tb = error_detail.exc_info()  # Get the traceback object

    filename = exc_tb.tb_frame.f_code.co_filename  # Get the script filename
    linenumber = exc_tb.tb_lineno  # Get the line number where the error occurred

    # Properly format the error message using an f-string
    error_message = f"Error occurred in Python script: [{filename}], line: [{linenumber}], message: {str(error)}"
    
    return error_message  # Return the formatted error message


# Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize base Exception class
        self.error_message = error_message_detail(error_message, error_detail)  # Store formatted message

    def __str__(self):
        return self.error_message  # Returns formatted error message when printed


# Main Execution Block
if __name__ == "__main__":

    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        a = 1 / 0  # This will raise ZeroDivisionError
    except Exception as e:
        logging.info("Divide by Zero error occurred")  # Log error message
        raise CustomException(e, sys)  # Raise custom exception with details

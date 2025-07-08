import sys

def error_message_detail(error, error_detail: sys):
    # Get traceback info to find exactly where the error happened
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Create detailed error message so debugging is easier
    error_message = "Error occurred in script: [{0}] at line [{1}] with message: [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # Add file location info to make debugging faster
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
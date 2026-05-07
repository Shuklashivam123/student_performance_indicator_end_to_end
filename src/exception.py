import sys
# Logging ke liye
from src.logger import logging

def error_message_detail(error,error_detail:sys):

#     Ye 3 cheeze return karta hai:

# exception type
# exception object
# traceback (🔥 most important)

# exc_tb.tb_lineno        # error line number
# exc_tb.tb_frame.f_code.co_filename   # file name

    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message=(
        "Error occured in python script name [{0}] line number [{1}] error message p[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    )

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        

        self.error_message=error_message_detail(error_message,error_detail=error_detail)

        # 🔥 YAHI logging add karni hai
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
    

# ✅ Testing block
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         raise CustomException(e, sys)
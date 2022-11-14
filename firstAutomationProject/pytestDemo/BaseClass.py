# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
import inspect
import logging

class BaseClass:

    def get_logging(self):
        logger_name = inspect.stack()[1][3]
#        log = logging.getLogger(__name__) copied bellow
        log = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logs.logs")
        log.addHandler(file_handler)
        set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(set_format)
        log.setLevel(logging.INFO)

        # log.debug("This is debug statement")
        # log.info("This is info statement")
        # log.debug("This is debug statement")
        # log.critical("This is critical statement")
        # log.error("This is error statement")
        # log.warning("This is warning statement")
        return log


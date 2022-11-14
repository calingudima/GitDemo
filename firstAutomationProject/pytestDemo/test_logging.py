# Logging are used MAINLY for errors, warning, or critical bugs,
# in rare cases we use it for debug and info.


# 2022-10-24 20:05:49,137 : ERROR : test _case name: Message
# date is stored as a string
#  THE VERY IMPORTANT ORDER << LEVELER >>
# debug
# info
# warnings
# error
# critical

# we store our logs in this file with extension:   .log
#
# import logging
#
# def test_get_logging():
#     log = logging.getLogger(__name__)
#     file_handler = logging.FileHandler("logs.logs")
#     log.addHandler(file_handler)
#     set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     file_handler.setFormatter(set_format)
#     log.setLevel(logging.CRITICAL)
#     log.debug("This is debug statement")
#     log.info("This is info statement")
#     log.debug("This is debug statement")
#     log.critical("This is critical statement")
#     log.error("This is error statement")
#     log.warning("This is warning statement")


#  ALL OF THE ABOVE HAS BEEN MOVED INTO THE << BASECLASS >> PYTHON FILE
from pytestDemo.BaseClass import BaseClass

class TestLogging(BaseClass):

    def test_logDemo(self):
       logger = BaseClass.get_logging(self)
       balance = 2000
       balance1 = 5000
       if balance >= balance1:
           logger.info("Numbers dont match")
       elif balance < balance1:
            assert logger.error("balance is bellow the minimum requirement")
#           raise Exception(logger.error("balance is bellow the minimum requirement"))   not a good example


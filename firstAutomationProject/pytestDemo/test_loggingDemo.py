from pytestDemo.BaseClass import BaseClass




class TestLoggingDemo(BaseClass):
        def test_logDemo(self):
            logger = BaseClass.get_logging(self)
            balance = 2000
            balance1 = 5000
            if balance >= balance1:
                logger.info("Numbers dont match")
            elif balance < balance1:
                logger.error("balance is bellow the minimum requirement")




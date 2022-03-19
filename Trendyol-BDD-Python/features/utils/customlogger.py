import logging


class LogGen():
    @staticmethod
    def customloggerrr():
        logging.basicConfig(
            level=logging.INFO,
            format="{asctime} {levelname:<8} {message}",
            style='{',
            filename='logfile.log',
            filemode='w')

        logger = logging.getLogger()
        return logger

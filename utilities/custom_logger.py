import logging


class log_macker:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\nop.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%Y-%m-%d %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
#time.strftime("%m-%d-%Y %T:%M%p")
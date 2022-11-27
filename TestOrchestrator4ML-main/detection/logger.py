import logging

# Logging function
def getConfiguredLogger():
    logging.basicConfig(filename="../../projectLogs.log", level=logging.INFO, format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt="%y-%b-%d %H:%M:%S")
    return logging.getLogger()

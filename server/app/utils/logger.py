from logging import StreamHandler, DEBUG, getLogger
from sys import stdout


_stdout_handler = StreamHandler(stdout)

logger = getLogger("vsnder")
logger.addHandler(_stdout_handler)
logger.setLevel(DEBUG)

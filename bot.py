from classes.sigaa import SigaaBot
from loguru import logger
from codetiming import Timer

t = Timer(text=f"Execution of {__file__}; Time spent: {{seconds:.2f}} seconds.", logger=logger.debug)
t.start()
robot = SigaaBot()
robot.sigaa()
t.stop()
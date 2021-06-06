from classes.sigaa import SigaaBot
from loguru import logger
from codetiming import Timer
from sys import argv

# Commands sent to this bot
cmds = argv[1:]

t = Timer(text=f"Execution of {__file__}; Time spent: {{seconds:.2f}} seconds.", logger=logger.debug)
t.start()
robot = SigaaBot()
robot.sigaa_user(cmds[0], cmds[1], cmds[2])
robot.sigaa()
t.stop()
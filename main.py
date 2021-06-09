from classes.sigaa import SigaaBot
from loguru import logger
from codetiming import Timer
from sys import argv, implementation
from os import linesep, getenv


def main():
    # Commands sent to this bot
    cmds = argv[1:]

    if len(cmds) == 0 or len(cmds) < 3:
        raise Exception(f"You must pass at least three arguments.{linesep} \
            They are: <str:USER_NAME> <str:PASSWORD> <str:SCHOOL_TERM> <int:OPTION(optional)>{linesep} \
            Follow this example:{linesep} \
                python bot.py Caio20 caio123 2020-1 1") 

    t = Timer(text=f"Execution of {__file__}; Time spent: {{seconds:.2f}} seconds.", logger=logger.debug)
    t.start()
    robot = SigaaBot()
    robot.sigaa_user(cmds[0], cmds[1], cmds[2])
    robot.sigaa_site()
    if cmds[3] == "1":
        robot.ver_notas()
    elif cmds[3] == "2":
        robot.ver_atestado()
    elif cmds[3] == "3":
        robot.ver_historico()
    elif cmds[3] == "4":
        robot.emitir_declaracao_vinculo()
    elif cmds[3] == "5":
        robot.matricula_online()
    else:
        logger.debug(f"Welcome back {getenv('USER')}!")
    t.stop()


if __name__ == "__main__":
    main()
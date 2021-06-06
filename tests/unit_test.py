from sigaabot.classes.sigaa import SigaaBot
from sigaabot.classes.user import User

def test_classes():
    bot = SigaaBot()
    user = User()
    assert isinstance(bot, SigaaBot)
    assert isinstance(user, User)


    
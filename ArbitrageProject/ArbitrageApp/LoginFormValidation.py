


def assertLength(val):
    return (lambda text : False if len(text) >= val else True);

def assertStartCharacter():
    return lambda text : True if text[0].isdigit() else False;

def assertWhiteSpaces():
    return lambda text : True if ' ' in text else False;

LoginUsernameAsserts = [assertLength(3), assertStartCharacter(), assertWhiteSpaces()]
LoginUsernameMsgs = ["Username too short !", "Username should not start with a digit !",
                    "Username should not contain white spaces "];
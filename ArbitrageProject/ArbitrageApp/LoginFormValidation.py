from django.core.exceptions import ValidationError


def assertLength(val):
    return (lambda text : False if len(text) >= val else True);

def assertStartCharacter():
    return lambda text : True if text[0].isdigit() else False;

def assertWhiteSpaces():
    return lambda text : True if ' ' in text else False;

LoginUsernameAsserts = [assertLength(3), assertStartCharacter(), assertWhiteSpaces()]
LoginUsernameMsgs = ["Username too short !", "Username should not start with a digit !",
                    "Username should not contain white spaces "];


def validateLength(minLength):

    def innerFunction(inputVal):
        temp = str(inputVal);
        if len(temp) < minLength:
            raise ValidationError(
                    "Too short",
                    params={'value': temp},
                );
    return innerFunction;
    

def validateStartCharacterDigit(inputVal):
    temp = str(inputVal);
    if(temp[0].isdigit() == True):
        raise ValidationError("Can't start with a digit ")
    

def validateWhiteSpaces(inputVal):
    temp = str(inputVal);
    if ' ' in temp : 
        raise ValidationError("Can't contain white spaces ");
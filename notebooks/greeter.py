

GREETINGS = {
    'german': 'Hey, {}',
    'spanish': 'Hóla, {}',
    'french': 'Bonjour,  {}' 
}

def greet_me(name: str, lang='german'):
    try:
        greeting_string = GREETINGS[lang]
        print(greeting_string.format(name))
    except KeyError:
        raise KeyError(f"Key '{lang}' is not supported. Supported languages are: {', '.join(GREETINGS.keys())}") from None
    

if __name__ == '__main__':
    name = input("What is your name?")
    language = input("In what language would you like to be greeted?")
    greet_me(name, language)

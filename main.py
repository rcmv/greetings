#pip install translate
from translate import Translator
from greets import greetings

translator = Translator(to_lang='pt')
for g in greetings:

    print(translator.translate(g).title())
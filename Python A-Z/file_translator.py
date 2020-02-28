from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('name.txt',mode='r') as my_file:
        line = my_file.read()
        translation = translator.translate(line)
        print(translation)
        with open('translation_file.txt',mode='w',encoding='utf-8') as op_file:
            op_file.write(translation)

except FileNotFoundError as err:
    print(err)
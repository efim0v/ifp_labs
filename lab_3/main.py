
import argparse


suppopted_lang = ['RU', 'EN']

def is_lang_suppported(lang) -> bool:
    return lang in suppopted_lang

def get_symbols(lang) -> str:
    if lang == 'EN': 
        return 'abcdefghijklmnopqrstuvwxyz'
    elif lang == 'RU': 
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        return ''
    

def encode(lang, offset:int, input_filename, output_filename):
    if not is_lang_suppported(lang):
        return
    symbols = get_symbols(lang)
    try:
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')
        while True:
            char = input_file.read(1)
            if not char:
                break
            if char.lower() in symbols:
                is_upper_case = char.isupper()
                res_lower_case = symbols[(symbols.index(char.lower()) + offset) % len(symbols)]
                res = res_lower_case.upper() if is_upper_case else res_lower_case
            else:
                res = char
            output_file.write(res)
            
    finally:
        input_file.close()
        output_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Csezar encoder")
    parser.add_argument("-O", '--offset', dest='offset', required=True)
    parser.add_argument("-o", '--output', dest='output', required=True)
    parser.add_argument("-i", '--input', dest='input', required=True)
    parser.add_argument("-l", '--langue', dest='lang', required=True)

    args = parser.parse_args()

    encode(args.lang, int(args.offset), args.input, args.output)
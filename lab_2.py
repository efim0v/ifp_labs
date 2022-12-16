import argparse

def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')

    return not text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Csezar encoder")
    parser.add_argument("sequence", help="Backet sequence")

    args = parser.parse_args()

    print(is_correct_brackets(args.sequence))

    

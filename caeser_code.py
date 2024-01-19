import string 


def encode_text(text: str, shift: int) -> str:
    encoded_text = ''
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += string.digits
    alphabet += string.punctuation
    alphabet += string.ascii_letters
    alphabet += ' '
    alphabet = alphabet.replace("'", "")

    for char in text:
        index = alphabet.find(char)
        if index == -1:   #элемент не нашелся
            print('ошибка найден неверный символ', char)
            return ''
        new_index = (index + shift) % len(alphabet) 
        encoded_text += alphabet[new_index]  

    return encoded_text


print(encode_text('вася', 2))


#-----------------------------------подготовка-----------------------------------
def validate_length(text: str) -> int:
    return len(text)

def validate_uppercase(text: str) -> int:
    f = 0
    for i in text:
        if i in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÆÇĆČĎĐÈÉÊËĘĚĞÎÏİŁÑŃŇÓÔÕÖØŐŒŘŚŞŠȚŤŪŮŰŲÜÝŹŻŽÞÐĂÂȘẞ":
            f += 1
    return f

def validate_lowercase(text: str) -> int:
    f = 0
    for i in text:
        if i in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzàáâãäåæçćčďđèéêëęěğıîïłñńňóôõöøőœřśşšțťūůűųüýźżžþðăâîșß":
            f += 1
    return f

def validate_digits(text: str) -> int:
    f = 0
    for i in text:
        if i in "0123456789":
            f += 1
    return f

def validate_special_chars(text: str) -> int:
    f = 0
    for i in text:
        if i in '@#$%^&*()+=-_!?[]{}|;:,.<>~`"': #-_!?[]{}|;:,.<>~` спец символов которых небыло в списке
            f += 1
    return f
"""
f=количество чего-либо(емкость), после того как она закончила деф, она выливает содержимость, поэтому переменная одна
"""
def validate_password(text: str, min_len: int = 8, max_len: int = 20, min_upper: int = 2, min_lower: int = 3, min_digits: int = 1, min_special: int = 2) -> None:
    errors = ""

    length = validate_length(text)
    upper = validate_uppercase(text)
    lower = validate_lowercase(text)
    digits = validate_digits(text)
    special = validate_special_chars(text)
    if length < min_len:
        errors += f"Пароль должен состоять минимум из {min_len} символов, а у вас {length}"+"\n"
    elif length > max_len:
        errors += f"Максимальная длина пароля {max_len} символов, а у вас {length}"+"\n"

    if upper < min_upper:
        errors += f"Пароль должен содержать минимум {min_upper} заглавных символов, а у вас {upper}"+"\n"
    elif upper > max_len - (min_lower + min_digits + min_special):
        errors += f"Максимальное количество заглавных символов - {max_len - (min_lower + min_digits + min_special)}, а у вас {upper}"+"\n"

    if lower < min_lower:
        errors += f"Пароль должен содержать минимум {min_lower} строчных символов, а у вас {lower}"+"\n"
    elif lower > max_len - (min_upper + min_digits + min_special):
        errors += f"Максимальное количество строчных символов - {max_len - (min_upper + min_digits + min_special)}, а у вас {lower}"+"\n"

    if digits < min_digits:
        errors += f"Пароль должен содержать минимум {min_digits} цифру, а у вас {digits}"+"\n"
    elif digits > max_len - (min_upper + min_lower + min_special):
        errors += f"Максимальное количество цифр - {max_len - (min_upper + min_lower + min_special)}, а у вас {digits}"+"\n"

    if special < min_special:
        errors += f"Пароль должен содержать минимум {min_special} специальных символов, а у вас {special}" +"\n"
    elif special > max_len - (min_upper + min_lower + min_digits):
        errors += f"Максимальное количество специальных символов - {max_len - (min_upper + min_lower + min_digits)}, а у вас {special}"+"\n"

    if errors == "":
        print("OK")
    else:
        print("ERROR:")
        print(errors)
"""
мин лен и т.д это то, что нам прописали в задаче, я не стал вводить новые переменные, и чтоб высчитать максимальное количество символа, я из максимума вычел сумму минимума всех чисел
errors= str поэтому они просто записывают в строчку все ошибки, если бы я не разделял \n то они бы шли подряд некрасиво
а еще догстринги сбивают код, и вызывают ошибку съехадшего текста по какой-то причине, поэтому пишу в конце
"""

text = input("Введите пароль: ")
validate_password(text)
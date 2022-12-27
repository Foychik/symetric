def encrypt(message, key):
    message_crypto = ""
    for i in message:
        message_crypto += chr(ord(i) + (key % 65536))
    return message_crypto


def decrypt(message, key):
    message_crypto = ""
    for i in message:
        message_crypto += chr(ord(i) - (key % 65536))
    return message_crypto


def hack(message):
    most_common_letter = ""
    max_letter = 0
    most_common_symbol = " "
    for i in message:
        if message.count(i) > max_letter:
            max_letter = message.count(i)
            most_common_letter = i
    return decrypt(message, abs(ord(most_common_symbol) - ord(most_common_letter)))


def xor(a, b):
    if a == b:
        return "0"
    return "1"


def to_10(x):
    n = 0
    for i in range(len(x)):
        n += int(x[i]) * 2 ** (len(x) - i - 1)
    return n


def vernam(message, key):
    mass_1 = []
    mass_2 = []
    mass_result = []

    for i in message:
        mass_1.append(str(bin(ord(i)))[2:])

    for i in key:
        mass_2.append(str(bin(ord(i)))[2:])

    for i in range(len(mass_1)):
        if len(mass_1[i]) < 8:
            mass_1[i] = "0" * (8 - len(mass_1[i])) + mass_1[i]

    for i in range(len(mass_2)):
        if len(mass_2[i]) < 8:
            mass_2[i] = "0" * (8 - len(mass_2[i])) + mass_2[i]

    for i in range(len(mass_1)):
        str_res = ""
        for j in range(len(mass_1[i])):
            str_res += xor(mass_1[i][j], mass_2[i][j])
        mass_result.append(str_res)
    mass_result = list(map(to_10, mass_result))
    return mass_result


def vernam_decrypt(message, key):
    mass_1 = []
    mass_2 = []
    mass_result = []

    for i in message:
        mass_1.append(str(bin(i))[2:])

    for i in key:
        mass_2.append(str(bin(ord(i)))[2:])

    for i in range(len(mass_1)):
        if len(mass_1[i]) < 8:
            mass_1[i] = "0" * (8 - len(mass_1[i])) + mass_1[i]

    for i in range(len(mass_2)):
        if len(mass_2[i]) < 8:
            mass_2[i] = "0" * (8 - len(mass_2[i])) + mass_2[i]

    for i in range(len(mass_1)):
        str_res = ""
        for j in range(len(mass_1[i])):
            str_res += xor(mass_1[i][j], mass_2[i][j])
        mass_result.append(str_res)

    mass_result = list(map(to_10, mass_result))
    message_code = ""
    for i in mass_result:
        message_code += chr(i)
    return message_code


message = input()
key = int(input())

print("Зашивровка:", encrypt(message, key))
print("Дешифровка:", decrypt(encrypt(message, key), key))
print("Взлом:", hack(encrypt(message, key)))

message = input()
key = input()
print("Вернам:", vernam(message, key))
print("Вернам:", vernam_decrypt(vernam(message, key), key))

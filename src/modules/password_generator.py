"""
@Project: python-service
@File: password_generator.py
@Author: David
@Date: 2025/6/5
@Brief: 
"""
import random
import string


class PasswordGenerator:
    def __init__(self, length=8, uppercase=True, lowercase=False, numbers=True, special_chars=False, exclude_chars=""):
        """
        Constructor of PasswordGenerator class
        :param length: length of the generated password
        :param uppercase: whether to include uppercase letters
        :param lowercase: whether to include lowercase letters
        :param numbers: whether to include digits
        :param special_chars: whether to include special characters
        :param exclude_chars: characters to exclude from the password
        """
        if length <= 0:
            raise ValueError("Password length must be positive")
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special_chars = special_chars
        self.exclude_chars = exclude_chars

    def generate(self) -> str:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        numbers = string.digits
        special_chars = "~`{}[]\\|;':\",./<>?"

        if self.exclude_chars:
            uppercase = list(filter(lambda x: x not in self.exclude_chars, uppercase))
            lowercase = list(filter(lambda x: x not in self.exclude_chars, lowercase))
            numbers = list(filter(lambda x: x not in self.exclude_chars, numbers))
            special_chars = list(filter(lambda x: x not in self.exclude_chars, special_chars))

        char_pool = []
        # 构建字符池
        if self.uppercase:
            char_pool.extend(uppercase)
        if self.lowercase:
            char_pool.extend(lowercase)
        if self.numbers:
            char_pool.extend(numbers)
        if self.special_chars:
            char_pool.extend(special_chars)

        if not char_pool:
            raise ValueError("No available characters to generate password")

        # 从每个类别中至少选择一个字符
        password = []
        if self.uppercase:
            password.append(random.choice(uppercase))
        if self.lowercase:
            password.append(random.choice(lowercase))
        if self.numbers:
            password.append(random.choice(numbers))
        if self.special_chars:
            password.append(random.choice(special_chars))

        while len(password) < self.length:
            password.append(random.choice(char_pool))

        random.shuffle(password)
        return ''.join(password)


if __name__ == '__main__':
    generator = PasswordGenerator(length=12, uppercase=True, lowercase=True, numbers=True, special_chars=False)
    print(generator.generate())

"""
@Project: python-service
@File: encryption.py
@Author: David
@Date: 2025/6/5
@Brief: 加密与解密程序
"""


class SimpleCipher:
    def __init__(self, key: str):
        """
        初始化加密器，使用字符串密钥
        :param key: 加密解密的密钥
        """
        self.key = key.encode('utf-8')

    def encrypt(self, plaintext: str) -> str:
        """
        加密明文
        :param plaintext: 要加密的文本
        :return: 十六进制格式的加密字符串
        """
        plain_bytes = plaintext.encode('utf-8')
        encrypted_bytes = []

        for i, byte in enumerate(plain_bytes):
            # 循环使用密钥中的字节进行异或操作
            key_byte = self.key[i % len(self.key)]
            encrypted_bytes.append(byte ^ key_byte)

        return bytes(encrypted_bytes).hex()

    def decrypt(self, ciphertext: str) -> str:
        """
        解密密文
        :param ciphertext: 十六进制格式的加密字符串
        :return: 解密后的原始文本
        """
        encrypted_bytes = bytes.fromhex(ciphertext)
        decrypted_bytes = []

        for i, byte in enumerate(encrypted_bytes):
            # 使用相同的密钥字节进行异或操作（解密）
            key_byte = self.key[i % len(self.key)]
            decrypted_bytes.append(byte ^ key_byte)

        return bytes(decrypted_bytes).decode('utf-8')


if __name__ == "__main__":
    # 创建加密器（使用密钥）
    cipher = SimpleCipher("my_secret_key")

    # 加密文本
    original_text = "Hello World Boy"
    encrypted_text = cipher.encrypt(original_text)
    print(f"加密结果: {encrypted_text}")

    # 解密文本
    decrypted_text = cipher.decrypt(encrypted_text)
    print(f"解密结果: {decrypted_text}")

    # 验证解密是否正确
    assert original_text == decrypted_text
    print("加密解密验证成功！")

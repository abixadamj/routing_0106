class Digest:
    def __init__(self):
        self.bytes = None
        self.hexdigest = None

    def generate(self) -> str:
        from random import randint
        from hashlib import sha512

        secret_str = "".join([chr(randint(65, 90)) * randint(1, 10) for _ in range(randint(5, 10))])
        self.bytes = secret_str.encode(encoding="UTF8")
        hash_object = sha512()
        hash_object.update(self.bytes)
        self.hexdigest = hash_object.hexdigest()
        return self.hexdigest

    def get_last_digest(self) -> str:
        return self.hexdigest if self.hexdigest else ""

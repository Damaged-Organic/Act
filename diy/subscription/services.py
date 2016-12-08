# diy_project/diy/subscription/services.py
import uuid
import hmac
import hashlib


class CheckoutHash():
    HASH_ALGORITHM = hashlib.sha1

    def generate(self):
        salt = uuid.uuid4().hex
        checkout_hash = hmac.new(salt.encode(), None, self.HASH_ALGORITHM)

        return checkout_hash.hexdigest()

    def compare(self, x, y):
        return hmac.compare_digest(x, y)

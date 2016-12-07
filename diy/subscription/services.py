# diy_project/diy/subscription/services.py
import uuid
import hmac
import hashlib


class CheckoutHash():
    def generate(self):
        h = hmac.new(uuid.uuid4().hex.encode(), None, hashlib.sha1)
        return h.hexdigest()

    def compare(self, x, y):
        return hmac.compare_digest(x, y)

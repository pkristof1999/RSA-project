from random import randint
from MillerRabinPrimeTest import *
from FastExponentation import *
from ExtendedEuclidean import *
from ChineseRemainder import *

class Calculate:
    def storeValues(self, a, pPrime_value, qPrime_value, eExponent_value, mMessage_value):
        a.set_pPrime(pPrime_value)
        a.set_qPrime(qPrime_value)
        a.set_eExponent(eExponent_value)
        a.set_mMessage(mMessage_value)

    def keyGen(self, phi, a):
        while True:
            e = a.get_eExponent()
            (d, x, y) = extendedEuclidean(phi, e)
            if d == 1:
                if y < 1:
                    y = y + phi
                return e, y

    def calculate_RSA(self, a):
        p = a.get_pPrime()
        q = a.get_qPrime()
        p = int(p)
        q = int(q)

        message = a.get_mMessage()
        mod = p * q
        phi = (p - 1) * (q - 1)

        e, d = self.keyGen(phi, a)

        # Encryption
        c = fastExponentation(message, e, mod)

        # Decryption
        m = chineseRemainder(p, q, c, d)

        # Signature
        S = chineseRemainder(p, q, message, d)

        # Verifying
        if m == fastExponentation(S, e, mod):
            verify = "Megfelelő aláírás!"
        else:
            verify = "Nem megfelelő aláírás"

        return f"A kiválasztott prímek: {p}, {q}"\
               f"RSA publikus kulcspár: ({phi}, {e})"\
               f"RSA privát kulcspár: ({phi}, {d})\n"\
               f"Titkosítani kívánt üzenet: {message}"\
               f"Titkosított üzenet: {c}"\
               f"Aláírás: {S}"\
               f"Ellenőrzés: {verify}"

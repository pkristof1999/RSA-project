from random import randint
from MillerRabinPrimeTest import *
from FastExponentation import *
from ExtendedEuclidean import *
from ChineseRemainder import *
from math import gcd

class Calculate:
    def storeValues(self, a, pPrime_value, qPrime_value, eExponent_value, mMessage_value):
        a.set_pPrime(pPrime_value)
        a.set_qPrime(qPrime_value)
        a.set_eExponent(eExponent_value)
        a.set_mMessage(mMessage_value)

    def keyGen(self, phi, a):
        while True:
            e = a.get_eExponent()
            if gcd(int(e), int(phi)) != 1:
                return ValueError
            (d, x, y) = extendedEuclidean(phi, e)
            if d == 1:
                if y < 1:
                    y = y + phi
                return e, y

    def calculate_RSA(self, a):
        try:
            p = a.get_pPrime()
            q = a.get_qPrime()
            message = a.get_mMessage()

            p = int(p)
            q = int(q)

            if p != q:
                if MillerRabin(p) and MillerRabin(q):
                    pass
                else:
                    raise ValueError("A megadott p vagy q prímek nem megfelelőek!")
            else:
                raise ValueError("A megadott p vagy q prímek nem megfelelőek!")

            mod = p * q
            phi = (p - 1) * (q - 1)

            if self.keyGen(phi, a) != ValueError:
                e, d = self.keyGen(phi, a)
            else:
                raise ValueError("A megadott e exponens nem megfelelő!")

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
        except ValueError as ve:
            return f"{ve}"

        return f"A kiválasztott prímek: {p}, {q}\n"\
               f"RSA publikus kulcspár: ({phi}, {e})\n"\
               f"RSA privát kulcspár: ({phi}, {d})\n"\
               f"Titkosítani kívánt üzenet: {message}\n"\
               f"Titkosított üzenet: {c}\n"\
               f"Aláírás: {S}\n"\
               f"Ellenőrzés: {verify}"

class Values:
    def __init__(self, pPrime = 0, qPrime = 0, eExponent = 0, mMessage = 0):
        self.__pPrime = int(pPrime)
        self.__qPrime = int(qPrime)
        self.__eExponent = int(eExponent)
        self.__mMessage = int(mMessage)

    def get_pPrime(self):
        return self.__pPrime

    def get_qPrime(self):
        return self.__qPrime

    def get_eExponent(self):
        return self.__eExponent

    def get_mMessage(self):
        return self.__mMessage

    def set_pPrime(self, pPrime):
        self.__pPrime = pPrime

    def set_qPrime(self, qPrime):
        self.__qPrime = qPrime

    def set_eExponent(self, eExponent):
        self.__eExponent = eExponent

    def set_mMessage(self, mMessage):
        self.__mMessage = mMessage
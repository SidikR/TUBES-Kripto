from cgi import test
import gen_bin
from random import randint

class keystream :
    def __init__(self) -> None :
        self.key_lfsr = self.__key_gen()
        self.public_key = []
        self.private_key = []
        self.lfsr = self.__lfsr_sys(self.key_lfsr)

    def __key_gen(self) :
        temp = randint(1, 15)
        temp = gen_bin.bin_conv(temp)

        if len(temp) < 4 :
            tmp = ""
            for i in range(4-len(temp)) :
                tmp += "0"

            temp = tmp+temp

        return temp

    def __test_primes(self, bilangan) :
        bulat = True

        if bilangan > 1 :
            for i in range(2, bilangan) :
                if (bilangan % i) == 0 :
                    bulat = False
                    break
        else :
            bulat = False
        
        return bulat

    def __gcd(self, a, b) :
        r = 0
        if a < b :
            a, b = b, a
        
        while b != 0 :
            r = a % b
            a = b
            b = r
        
        return a
    
    def __d_count(self, e, m) :
        k = 1
        while True :
            d = k * e
            h = d % m

            if h == 1 :
                return k
            else :
                k = k + 1

    def __primes_generator(self) :
        bilangan = randint(2, 10000)
        while self.__test_primes(bilangan) is not True :
            bilangan = randint(2, 10000)
        
        return bilangan

    def key_gen_primes(self) :
        p = self.__primes_generator()
        q = self.__primes_generator()
        
        n = p*q
        m = (p-1)*(q-1)
        
        e = self.__primes_generator()
        while self.__gcd(e, m) != 1 :
            e = self.__primes_generator()

        d = self.__d_count(e, m)
        print(p, " ", q, " ", n, " ", m, " ", e, " ", d)

        
            

    def __gen_lfsr(self, kunci) :
        sway = int(kunci[len(kunci)-1]) ^ int(kunci[0])
        kunci = str(sway)+kunci[:len(kunci)-1]

        return kunci

    def __lfsr_sys(self, kunci) :
        temp = ""
        pegang = kunci
        i = 0
        while kunci != pegang or i == 0 :
            temp += kunci[len(kunci)-1]
            kunci = self.__gen_lfsr(kunci)
            i += 1

        return temp
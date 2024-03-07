import number_theory_functions
import random

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """

        #Choosing random p,q
        q = number_theory_functions.generate_prime(int(digits/2))
        w = number_theory_functions.generate_prime(int(digits/2))
        p = number_theory_functions.generate_prime(int(digits/2))

        N = p*q
        M = p*w

        while (len(str(N))!=digits and len(str(M))!=digits):
            q = number_theory_functions.generate_prime(int(digits/2) - 1)
            w = number_theory_functions.generate_prime(int(digits/2))
            p = number_theory_functions.generate_prime(int(digits/2))
            N = p*q
            M = p*w

        if len(str(N))==digits:
            K = (p-1)*(q-1)
        else:
            N = M
            K = (p-1)*(w-1)

        # Calculating 5 biggest U_k elements and choosing random e
        primes = []
        for i in range(5):
            prime = number_theory_functions.generate_prime(digits - 1)
            primes.append(prime)

        e = random.choice(primes)
        """
        euler = []
    
        for i in range(K-1, 1, -2):
                if(number_theory_functions.extended_gcd(K, i)[0] == 1):
                        euler.append(i)
                if(len(euler) == 5):
                        break
        """

        #Calculating d
        d = number_theory_functions.extended_gcd(e, K)[1]

        #Generating RSA system
        public_key = (N,e)
        private_key = (N,d)

        generated = RSA(public_key, private_key)
        return generated


    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        decrypted_num = number_theory_functions.modular_exponent(c, self.private_key[1], self.private_key[0])

        return decrypted_num
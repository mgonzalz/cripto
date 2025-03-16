import sympy
import random
import time
import math

class DiscreteLogAttack:
    def __init__(self, bits):
        """Inicializa los valores del ataque con un primo de n bits"""
        self.p = sympy.randprime(2**(bits-1), 2**bits)  # Generar primo
        self.g_primitive = sympy.primitive_root(self.p)  # Raíz primitiva
        self.g_non_primitive = random.randint(2, self.p-1)  # Número arbitrario
        self.x_true = random.randint(1, self.p-1)  # Exponente secreto
        self.y_primitive = pow(self.g_primitive, self.x_true, self.p)  # y con raíz primitiva
        self.y_non_primitive = pow(self.g_non_primitive, self.x_true, self.p)  # y con g arbitrario

    def brute_force(self, g, y):
        """Implementación del ataque por fuerza bruta"""
        for x in range(self.p):
            if pow(g, x, self.p) == y:
                return x
        return None

    def bsgs(self, g, y):
        """Implementación del ataque Baby-step Giant-step (BSGS)"""
        m = math.isqrt(self.p - 1) + 1
        baby_steps = {pow(g, j, self.p): j for j in range(m)}
        c = pow(g, m, self.p)
        c_inv = pow(c, -1, self.p)
        gamma = y

        for i in range(m):
            if gamma in baby_steps:
                return i * m + baby_steps[gamma]
            gamma = (gamma * c_inv) % self.p
        return None

    def run_attack(self):
        """Ejecuta los ataques y mide los tiempos"""
        results = {}

        # Brute Force con raíz primitiva
        start = time.perf_counter()
        self.brute_force(self.g_primitive, self.y_primitive)
        results["brute_primitive"] = time.perf_counter() - start

        # Brute Force con g no primitiva
        start = time.perf_counter()
        self.brute_force(self.g_non_primitive, self.y_non_primitive)
        results["brute_non_primitive"] = time.perf_counter() - start

        # BSGS con raíz primitiva
        start = time.perf_counter()
        self.bsgs(self.g_primitive, self.y_primitive)
        results["bsgs_primitive"] = time.perf_counter() - start

        # BSGS con g no primitiva
        start = time.perf_counter()
        self.bsgs(self.g_non_primitive, self.y_non_primitive)
        results["bsgs_non_primitive"] = time.perf_counter() - start

        return results

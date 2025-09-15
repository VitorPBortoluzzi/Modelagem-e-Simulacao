# Fórmulas (M/M/1) – use λ e μ em 1/min; W e Wq saem em minutos:
# ρ = λ / μ
# W = 1 / (μ − λ)
# Wq = ρ / (μ − λ)
# L = λ · W
# Lq = λ · Wq


while(i < 5):
a = float(input("Insira o valor de λ: "))
u = float(input("Insira o valor de μ: "))

p=a/u
Wx = 1 / (u / a)
Wq = p / (u-a)
Lx = a * Wx
Lq = a * Wq

print(f"p = {p:.2f}")
print(f"W = {Wx:.2f}")
print(f"Wq = {Wq:.2f}")
print(f"L = {Lx:.2f}")
print(f"Lq = {Lq:.2f}")
#!python3
lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuu'

print(f'O status é: {status}')
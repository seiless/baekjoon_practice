import sys
for e in iter(input, '-1.0'):
    x = float(e)
    print(f'Objects weighing {x:.2f} on Earth will weigh {(x*0.167):.2f} on the moon.')
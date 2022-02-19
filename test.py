import time
def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

print("Progress Bar")
for _ in range (0, 101, 1):
    progressBar(_, 100, 20)
    time.sleep(0.1)
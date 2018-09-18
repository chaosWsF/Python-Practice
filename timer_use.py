from threading import Timer


def hello():
    print('hello world')

i = 0
while i <= 5:
    timer = Timer(5, hello)
    timer.start()
    print('can')
    i += 1

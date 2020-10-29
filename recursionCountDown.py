def countDown(num):
    if num <= 0:
        print('done')
        return
    print(num)
    num -= 1
    countDown(num)
countDown(5)
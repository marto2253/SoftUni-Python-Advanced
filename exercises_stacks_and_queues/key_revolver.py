from collections import deque


def key_revolver(b_price, gun_barrel, bullets, locks, value_of_int):
    bullets_stack = [int(i) for i in bullets.split()]
    locks_que = deque([int(i) for i in locks.split()])
    bullets_left = gun_barrel

    while locks_que and bullets_stack:
        bullet = bullets_stack.pop()
        lock = locks_que[0]
        bullets_left -= 1
        value_of_int -= b_price

        if bullet > lock:
            print('Ping!')
        else:
            locks_que.popleft()
            print('Bang!')

        if not bullets_left and len(bullets_stack):
            print('Reloading!')
            bullets_left = gun_barrel

    if len(locks_que) == 0:
        print(f'{bullets_left} bullets left. Earned ${value_of_int}')
    else:
        print(f"Couldn't get through. Locks left: {len(locks_que)}")


bullet_price = int(input())
gun_barrel = int(input())
bullets = input()
locks = input()
value_of_int = int(input())
key_revolver(bullet_price, gun_barrel, bullets, locks, value_of_int)

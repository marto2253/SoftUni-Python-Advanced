from collections import deque

eggs = deque(int(i) for i in input().split(', '))
papers = deque(int(i) for i in input().split(', '))

box = 0

while True:

    if not eggs or not papers:
        break

    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)
        continue

    if egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(paper)
        continue

    if egg + paper <= 50:
        box += 1

if box >= 1:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(i) for i in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(i) for i in papers)}')
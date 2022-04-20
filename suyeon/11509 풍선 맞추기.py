# 4/20 스터디 시험 문제
# 시간 안에 해결 못함

# import collections
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input().strip())
# baloons = deque(list(map(int, input().strip().split())))
# baloons_dict = collections.defaultdict(int)
# for baloon in baloons:
#     baloons_dict[baloon] = baloon
# arrow_cnt = 0

# start_h = baloons.popleft()
# while baloons:
#     arrow_cnt += 1
#     start_h -= 1
#     while baloons_dict[start_h]:
#         baloons.remove(start_h)
#         if baloons:
#             start_h = baloons.popleft()
#         continue
#     else:
#         start_h = baloons.popleft()

# print(arrow_cnt)
import sys


n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
# 발사된 각 화살의 높이
cnt = [0] * (n + 1)

# 화살의 높이를 확인한다.
for i in h:
    # 화살이 발사되어있으면 똑같은 화살로 풍선을 터트리고 화살의 높이를 내린다.
    if cnt[i] > 0:
        # 풍선을 터트리고 원래 화살을 빼주고
        # 화살의 높이 -1 위치에 화살을 다시 조준한다.
        cnt[i] -= 1
        cnt[i - 1] += 1
    else:
        # 화살이 발사되지 않았으므로
        # 풍선을 터트리고 화살의 높이 -1 위치에 화살을 조준한다.
        cnt[i - 1] += 1

# 발사된 화살의 개수를 출력한다.
print(sum(cnt))
# https://www.acmicpc.net/problem/10431
# 줄세우기 
# Silver V

def solution():
    p = int(input())
    for tc in range(1, p+1):
        input_ = list(map(int, input().split()))
        t = input_[0]
        nums = input_[1:]

        steps = 0 
        line = [nums[0]]

        for h in nums[1:]:
            if max(line) < h :
                line.append(h)
            else :
                for i in range(len(line)):
                    if line[i] > h:
                        behind = line[i:]
                        new_line = line[:i]
                        new_line.append(h)
                        new_line.extend(behind)
                        steps += len(line[i:])
                        line = new_line
                        break
        print(f"{tc} {steps}")


solution()
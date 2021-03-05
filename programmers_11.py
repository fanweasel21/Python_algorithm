# def solution(progresses, speeds):
#     days = []
#     if progresses[0] % speeds[0] == 0:
#         days.append(progresses[0]//speeds[0])
#     else:
#         days.append(progresses[0]//speeds[0] + 1)

def solution(progressed, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0]<=((p-100)//s):
            Q.append([])


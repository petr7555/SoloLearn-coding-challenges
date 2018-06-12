"""log = ["Feb SLR 4 M",
       "Feb ENT 800 K",
       "Mar SLR 4000 K",
       "Mar ENT 800 K",
       "Apr SLR 4010 K",
       "Apr ENT 810 K"]"""
log = ["Jul SLR 4 M",
       "Jul ENR 800 K",
       "Jul OTR 1200 K",
       "Aug SLR 4000 B",
       "Aug ENR 800 K",
       "Aug OTR 1190 K",
       "Sep SLR 4000 K",
       "Sep ENR 800 K",
       "Sep OTR 1190 K"]
money = {"K": 1000,
         "M": 1000000,
         "B": 1000000000}
exp = {}
months = []
for i in range(len(log)):
    log[i] = log[i].split()
    log[i][2] = int(log[i][2])*money[log[i][3]]
    log[i].pop()
    if log[i][1] in exp:
        exp[log[i][1]].append(log[i][2])
    else:
        exp[log[i][1]] = [log[i][2]]
    if log[i][0] not in months:
        months.append(log[i][0])
for reason in exp:
    if exp[reason][1:] != exp[reason][:-1]:
        month = months[exp[reason].index(max(exp[reason]))]
        print("There is inconsistency in", reason, "in", month + ".")

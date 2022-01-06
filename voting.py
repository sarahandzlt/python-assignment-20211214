def generatePerferences(values):
    dict = {}

    for i in range(0, len(values)):
        array = values[i]
        list2 = []
        for j in range(0, len(array)):
            list2.append({'index': j + 1, 'value': array[j]})
        list2.sort(key=lambda x: x['value'], reverse=True)

        sorted_list = [item['index'] for item in list2]

        dict[i + 1] = sorted_list

    return dict


def dictatorship(preferenceProfile, agent):
    print("dictatorship")
    print(preferenceProfile)
    print(agent)
    print("END dictatorship")

    # 一个agent 决定一切，他的选择的第一个就是结果
    # 传进来的可能就不是排过序的，那就先
    values = generatePerferences(preferenceProfile)

    for prep in values:
        if prep['index'] == agent: #判断哪组值是Agent的
            return prep['value'][0] #返回第一个

    return 0


def scoringRule(preferences, scoreVector, tieBreak):
    votesDict = {}
    values = generatePerferences(preferences)
    # 得出values
    return 0


def plurality(preferences, tieBreak):
    # 无论怎么样，要先calculate并汇总所有的投票
    # plurality意思是第一个出现得最多的
    # 传进来的可能就不是排过序的，那就先
    values = generatePerferences(preferences)

    # 记录第一个出现的次数
    dict = {}
    for pref in values:
        if pref[0] not in dict.keys():  ##未经记录，设置为0
            dict[pref[0]] = 0
        # 保证了选择存在dict，可以统计了
        dict[pref[0]] += 1

    return tieBreakFindValueByDict(dict,tieBreak)


def veto(preferences, tieBreak):
    return 0


def borda(preferences, tieBreak):
    # 排序，最后一个0分，第一个m-1分，统计总分
    dict = {}  # 记录每个候选人的分数变化
    for pref in preferences:
        leng = len(pref)
        for i in range(0, leng):
            current = leng - i - 1  # 当前分数。当前的选择是pref[i]
            # 更新dictionary
            if pref[i] not in dict.keys():  ##未经记录，设置为0
                dict[pref[i]] = 0
            # 保证了选择存在dict，可以统计了
            dict[pref[i]] = dict[pref[i]] + current

    # 最终dict就是结果，但不能立刻返回
    return tieBreakFindValueByDict(dict, tieBreak)

    # return 0


def tieBreakFindValueByDict(dict, tieBreak):
    # 简单好懂的做法就是把最大的current_max挑出来
    # 把所有的选择都放进set
    dataset = set([])
    current_max = 0
    for k in dict.keys():
        current_max = max(current_max, dict[k])
    for k in dict.keys():
        if dict[k] >= current_max:
            dataset.add(k)
        # 挑出最大值的
    # 然后set就是最大值的候选，多于一个则是同分
    # 同分的时候，根据tieBreak选择
    # 剩下的元素使用tieBreak
    if tieBreak == 'min':  # 找出最大的同时的最小index
        return min(dataset)
    if tieBreak == 'max':
        return max(dataset)
    # else 取index
    list = []
    list.extend(set)
    rng = int(tieBreak)
    return list[rng]


def harmonic(preferences, tieBreak):
    return 0


def STV(preferences, tieBreak):
    # 每一次迭代，拿掉最后的那个
    dataset = set([])
    # 先把所有元素都加入set
    for prep in preferences:
        for p in prep:
            dataset.add(p)
    # 迭代所有，去掉最末尾
    for prep in preferences:
        dataset.remove(prep[-1])
    # 剩下的元素使用tieBreak
    if tieBreak == 'min':
        return min(dataset)

    if tieBreak == 'max':
        return max(dataset)

    # else 取index
    list = []
    list.extend(set)
    rng = int(tieBreak)
    return list[rng]

    #return 0


def rangeVoting(values, tieBreak):
    # 这个是最终需要实现的
    # 传进来应该第一步需要获取priority排序，使用task1的办法
    preferences = generatePerferences(values)
    # 然后根据tieBreak选出一个
    # 还没读懂，函数之间的调用关系靠猜

    return 0

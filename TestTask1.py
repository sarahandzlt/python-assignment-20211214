

def generatePerferences(array2d):
    dict = {}

    for i in range(0, len(array2d)):
        array = array2d[i]
        list2 = []
        for j in range(0, len(array)):
            list2.append({'index': j + 1, 'value': array[j]})
        list2.sort(key=lambda x: x['value'], reverse=True)

        sorted_list = [item['index'] for item in list2]

        dict[i + 1] = sorted_list

    return dict




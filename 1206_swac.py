for i in range(10):
    building_cnt = int(input())
    B = [int(x) for x in input().split()]
    #print(B)
    #print("DEBUG -1")
    sum = 0
    for j in range(2, building_cnt- 2):
        #print("DEBUG 0")
        answer = 0
        value = 0
        cur_h = B[j]
        #print("DEBUG 1")

        value = min(cur_h - B[j - 2], cur_h - B[j - 1], cur_h - B[j + 1], cur_h- B[j+2])

        #print("DEBUG 2")
        answer = max(0, value)
        sum += answer

    print("#{} {}".format(i + 1, sum))

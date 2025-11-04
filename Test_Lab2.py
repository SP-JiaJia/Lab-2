import Lab2.Lab2 as Lab2

def test_find_MinMax():
    result = []
    input=[10, 100, -2.1, 153.2, -10.1]
    test_arr=[-10.1, 153.2]

    result = Lab2.cal_min_max_temp(input)
    
    assert(result==test_arr)

def test_average_temp():
    result=0
    input=[10, 2, 2.2, 3]
    
    result=Lab2.cal_average_temp(input)
    
    assert(result == 4.3)

def test_cal_median_temp():
    result=0
    input=[-5, -2, 10, 10.1, 256.2]

    result = Lab2.cal_median_temp(input)

    assert(result == 10)
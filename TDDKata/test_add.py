from add import add

# "2, 3, 1" -> 6

def test_2_3_1_should_be_6():
    # arrange
    expression = "2, 3, 1"
    expected = 6

    # act
    actual = add(expression)

    # assert
    assert actual == expected


def test_0_0_0_should_be_0():
    # arrange 
    expression = "0, 0, 0"
    expected = 0

    # act
    actual = add(expression)

    # assert
    assert actual == expected

def test_a_b_c_should_be_error():
    # arrange
    expression = "a, b, c"
    expected = -1
    
    # act
    actual = add(expression)

    # assert
    assert actual == expected

def test_unfilled_fields_should_be_error():
    # arrange
    expression = ""
    expected = -1

    # act
    actual = add(expression)

    # assert
    assert actual == expected
def int_cheak(to_check):


    while True:
        error = "please enter a integer more or equal to 1"

        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)
            if response < 1:
                return "invalid"
            else:
                return response
        except ValueError:
            return "invalid"




# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    (0, 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite')
,
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_cheak(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")

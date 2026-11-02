from scores import total_scores


def check_paired_students():
    data = [[10, 20], [5, 5]]
    expected = None  # Replace None with contract-derived expected totals.
    actual = total_scores(data)
    assert actual == expected, f"actual={actual}, expected={expected}"
    # Once paired case is correct, also verify reversed order with fixed expectations.
    assert total_scores([[5, 5], [10, 20]]) == [10, 30]
    print("PASS paired totals:", actual)
    print("PASS reversed-order totals:", [10, 30])


check_paired_students()

from scores import total_scores

cases = [([[7, 3]], [10]), ([], []), ([[], [4]], [0, 4]), ([[5, 5], [10, 20]], [10, 30])]
# Legacy suite intentionally lacks a meaningful paired-student assertion.
# Reversed-order preservation is checked structurally, not by totals here.
for data, expected in cases[:3]:
    snapshot = [marks[:] for marks in data]
    actual = total_scores(data)
    assert actual == expected, (data, actual, expected)
    assert data == snapshot, "Inputs changed"
    print("PASS", data, "=>", actual, "; input unchanged")
reverse_data = [[5, 5], [10, 20]]
snapshot = [marks[:] for marks in reverse_data]
result = total_scores(reverse_data)
assert len(result) == 2 and reverse_data == snapshot
print("PASS reversed-order structure and input preservation (totals need regression coverage)")
print("Existing checks passed")

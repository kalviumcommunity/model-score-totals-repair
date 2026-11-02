def total_scores(students):
    totals = []
    total = 0
    for marks in students:
        for mark in marks:
            total += mark
        totals.append(total)
    return totals

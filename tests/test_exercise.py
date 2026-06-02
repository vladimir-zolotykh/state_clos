from orderedmeta import Exercise


def test_orderedmeta():
    exer = Exercise(name="bench", weight=77.5, reps=2)
    assert exer.name == "bench"
    assert exer.weight == 77.5
    assert exer.reps == 2

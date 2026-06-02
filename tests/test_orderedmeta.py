import pytest

from orderedmeta import Exercise


def test_valid_initialization():
    ex = Exercise(name="bench", weight=77.5, reps=2)

    assert ex.name == "bench"
    assert ex.weight == 77.5
    assert ex.reps == 2


def test_fields_generated_by_metaclass():
    assert Exercise._fields == ["name", "weight", "reps"]


@pytest.mark.parametrize(
    "name",
    [
        123,
        12.5,
        [],
        {},
        None,
    ],
)
def test_invalid_name_raises_typeerror(name):
    with pytest.raises(TypeError):
        Exercise(name=name, weight=77.5, reps=2)


@pytest.mark.parametrize(
    "weight",
    [
        "77.5",
        77,
        [],
        {},
        None,
    ],
)
def test_invalid_weight_raises_typeerror(weight):
    with pytest.raises(TypeError):
        Exercise(name="bench", weight=weight, reps=2)


@pytest.mark.parametrize(
    "reps",
    [
        "2",
        2.0,
        [],
        {},
        None,
    ],
)
def test_invalid_reps_raises_typeerror(reps):
    with pytest.raises(TypeError):
        Exercise(name="bench", weight=77.5, reps=reps)


def test_name_assignment_validation():
    ex = Exercise(name="bench", weight=77.5, reps=2)

    with pytest.raises(TypeError):
        ex.name = 123


def test_weight_assignment_validation():
    ex = Exercise(name="bench", weight=77.5, reps=2)

    with pytest.raises(TypeError):
        ex.weight = "80.0"


def test_reps_assignment_validation():
    ex = Exercise(name="bench", weight=77.5, reps=2)

    with pytest.raises(TypeError):
        ex.reps = 2.0

from datetime import date

import pytest

from regalgo import PersonInput

from election_presidentielle.regles import ElectionPresidentielle


@pytest.fixture
def algo():
    return ElectionPresidentielle()


def test_cas_nominal(algo):
    person = PersonInput(
        cv_nationality="FR",
        schema_birth_date=date(1990, 1, 1),
        cccev_civil_rights_intact=True,
        cccev_electoral_list_registered=True,
    )
    result = algo.compute(person.to_algo_input())
    assert result.algo_id == "election-presidentielle"

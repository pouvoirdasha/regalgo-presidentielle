# election-presidentielle

Algorithme réglementaire basé sur [regalgo](https://github.com/qloridant/regalgo).

## Installation

```bash
pip install election-presidentielle
```

## Utilisation

```python
from datetime import date
from regalgo import PersonInput
from election_presidentielle.regles import ElectionPresidentielle

person = PersonInput(
    cv_nationality="FR",
    schema_birth_date=date(1990, 1, 1),
    cccev_civil_rights_intact=True,
    cccev_electoral_list_registered=True,
)

algo = ElectionPresidentielle()
result = algo.compute(person.to_algo_input())
print(result.value)
```

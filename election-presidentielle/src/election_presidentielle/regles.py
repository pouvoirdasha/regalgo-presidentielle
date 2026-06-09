from __future__ import annotations

from regalgo import AlgoInput, AlgoResult, PublicRule


class ElectionPresidentielle(PublicRule):
    """Implémentation de l'algorithme election-presidentielle."""

    def compute(self, algo_input: AlgoInput) -> AlgoResult:
        data = algo_input.data

        # TODO : implémenter la logique réglementaire ici
        result_value = None

        return AlgoResult(
            value=result_value,
            algo_id=self.algo_id,
            regulation=self.regulation,
            inputs_snapshot=data,
        )

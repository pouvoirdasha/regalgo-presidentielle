from __future__ import annotations

from regalgo import AlgoInput, AlgoResult, PublicRule
from regalgo_civique_droit_vote import DroitVoteAlgorithm

class ElectionPresidentielle(PublicRule):
    """Implémentation de l'algorithme election-presidentielle.
    Les conditions : 
    - avoir la nationalité française 
    - avoir 18 ans révolus 
    - être électeur = résultat algo droit civique (package importé)
    - Ne doit pas être inéligible = tribunaux ont interdit le droit de vite + décisin judiciare en application des lois 
    - ne pas être sous tutelle 
    - ne pas être sous curatelle 
    - avoir satisfait aux onligations imposées par le code du service national. 

    Algo doit retourner un booléen (True/False) sur la possibilité de pouvoir se présenter à l'élection. 
    
    """

    def compute(self, algo_input: AlgoInput) -> AlgoResult:
        data = algo_input.data
        nationalite = bool(algo_input.data["nationalite_française"])
        age = int(algo_input.data["age"])
        electeur = bool(DroitVoteAlgorithm(algo_input.data)) # la bonne manière de faire ? 
        ineligible = bool(algo_input.data[ineligible])
        tutelle = bool(algo_input.data["tutelle"])
        curatelle = bool(algo_input.data["curatelle"])
        service_national_valide = bool(algo_input.data["service_national_valide"])
    



        
        result_value = None

        return AlgoResult(
            value=result_value,
            algo_id=self.algo_id,
            regulation=self.regulation,
            inputs_snapshot=data,
        )

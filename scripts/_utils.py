from typing import Tuple

from ape import accounts, project
from ape.contracts import ContractInstance

owner = accounts.test_accounts[0]


def deploy() -> Tuple[ContractInstance, ContractInstance, ContractInstance]:
    contract_c = project.ContractC.deploy(sender=owner)
    contract_b = project.ContractB.deploy(contract_c.address, sender=owner)
    contract_a = project.ContractA.deploy(
        contract_b.address, contract_c.address, sender=owner
    )
    return contract_a, contract_b, contract_c


__all__ = ["deploy", "owner"]

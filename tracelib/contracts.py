from functools import cached_property
from typing import Tuple, cast

from ape import networks, project
from ape.contracts import ContractContainer, ContractInstance
from ape.exceptions import NetworkError
from ape.types import AddressType

from tracelib.accounts import account_factory
from tracelib.utils import is_local


class Deployer:
    @cached_property
    def contract_c(self) -> ContractInstance:
        contract = self._("ContractC")
        return contract.deploy(sender=account_factory.owner)

    @cached_property
    def contract_b(self) -> ContractInstance:
        contract = self._("ContractB")
        return contract.deploy(self.contract_c, sender=account_factory.owner)

    @cached_property
    def contract_a(self) -> ContractInstance:
        contract = self._("ContractA")
        return contract.deploy(
            self.contract_b, self.contract_c, sender=account_factory.owner
        )

    def _(self, name: str) -> ContractContainer:
        return project.get_contract(name)


deployer = Deployer()


def get_contracts(
    force_deploy: bool = False,
) -> Tuple[ContractInstance, ContractInstance, ContractInstance]:
    network_name = networks.provider.network.name
    if is_local() or force_deploy:
        return deployer.contract_a, deployer.contract_b, deployer.contract_c

    elif network_name == "rinkeby":
        # NOTE: Pre-checksummed for perf reasons.
        a = cast(AddressType, "0x8E8E24806D147b84896E3f13F21a2493a3CD4402")
        b = cast(AddressType, "0x804811d5e7ac6b7A41E032945A41c09F5bd9A358")
        c = cast(AddressType, "0x4fE7908BD16F15c3366d9bCB351d3c5a759A8b13")
        return (
            deployer._("ContractA").at(a),
            deployer._("ContractB").at(b),
            deployer._("ContractC").at(c),
        )
    else:
        raise NetworkError(f"Not yet deployed to network '{network_name}'")

from typing import Tuple

import click
from ape import accounts, networks, project
from ape.api import AccountAPI, ReceiptAPI
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import get_user_selected_account
from ape.contracts import ContractInstance
from ape.exceptions import NetworkError
from ape.utils import cached_property
from ape_accounts import KeyfileAccount


def is_local() -> bool:
    return networks.provider.network.name in (LOCAL_NETWORK_NAME, "mainnet-fork")


class AccountFactory:
    @cached_property
    def owner(self) -> AccountAPI:
        if is_local():
            return self[0]

        elif networks.provider.network.name == "rinkeby":
            return accounts.load("metamask0")

        prompt = "Select an account to own these contracts"
        return get_user_selected_account(KeyfileAccount, prompt_message=prompt)

    def __getitem__(self, index: int) -> AccountAPI:
        return accounts.test_accounts[index]


account_factory = AccountFactory()


def deploy() -> Tuple[ContractInstance, ContractInstance, ContractInstance]:
    contract_c = project.ContractC.deploy(sender=account_factory.owner)
    contract_b = project.ContractB.deploy(
        contract_c.address, sender=account_factory.owner
    )
    contract_a = project.ContractA.deploy(
        contract_b.address, contract_c.address, sender=account_factory.owner
    )
    return contract_a, contract_b, contract_c


def get_contracts(
    force_deploy: bool = False,
) -> Tuple[ContractInstance, ContractInstance, ContractInstance]:
    network_name = networks.provider.network.name
    if is_local() or force_deploy:
        return deploy()

    elif network_name == "rinkeby":
        a = "0x8E8E24806D147b84896E3f13F21a2493a3CD4402"
        b = "0x804811d5e7ac6b7A41E032945A41c09F5bd9A358"
        c = "0x4fE7908BD16F15c3366d9bCB351d3c5a759A8b13"
        return (
            project.ContractA.at(a),
            project.ContractB.at(b),
            project.ContractC.at(c),
        )
    else:
        raise NetworkError(f"Not yet deployed to network '{network_name}'")


verbose_option = click.option(
    "--verbose", is_flag=True, help="Show more information on the trace."
)
raw_option = click.option("--raw", is_flag=True, help="Show the raw, non-pretty trace.")


def show_trace(receipt: ReceiptAPI, verbose: bool, raw: bool):
    if raw:
        call_tree = networks.provider.get_call_tree(receipt.txn_hash)
        click.echo(repr(call_tree))
    else:
        receipt.show_trace(verbose=verbose)


__all__ = ["account_factory", "get_contracts", "deploy", "verbose_option"]

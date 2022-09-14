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


class TxnConstants:
    FAILED_TXN = "0x053cba5c12172654d894f66d5670bab6215517a94189a9ffc09bc40a589ec04d"
    FROM_TICKET_0 = "0xb7d7f1d5ce7743e821d3026647df486f517946ef1342a1ae93c96e4a8016eab7"
    FROM_TICKET_1 = "0x0537316f37627655b7fe5e50e23f71cd835b377d1cde4226443c94723d036e32"
    VYPER = "0x053a723780e9630687d64a40caacf5ed379816501722fe52855df16e987c5706"
    LLAMA = "0x9d8fc48fe2f552a424fa2e4fa35f2ddbe73eb9f1eae33bb3b7b27466b8dbb62f"
    DATA_ISSUE = "0x3cef4aaa52b97b6b61aa32b3afcecb0d14f7862ca80fdc76504c37a9374645c4"
    SPECIAL_KEYS = {
        "fail": FAILED_TXN,
        "t0": FROM_TICKET_0,
        "t1": FROM_TICKET_1,
        "vyper": VYPER,
        "llama": LLAMA,
        "dataissue": DATA_ISSUE,
        "all": (FAILED_TXN, FROM_TICKET_0, FROM_TICKET_1, VYPER, LLAMA),
    }


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


def show_trace(receipt: ReceiptAPI, verbose: bool, raw: bool):
    if raw:
        call_tree = networks.provider.get_call_tree(receipt.txn_hash)
        click.echo(repr(call_tree))
    else:
        receipt.show_trace(verbose=verbose)


def show_gas(receipt: ReceiptAPI):
    receipt.show_gas_report()


verbose_option = click.option(
    "--verbose", is_flag=True, help="Show more information on the trace."
)
raw_option = click.option("--raw", is_flag=True, help="Show the raw, non-pretty trace.")


def txn_hash_callback(ctx, param, value):
    hash_set = set()
    for tx_hash in value:
        if tx_hash in TxnConstants.SPECIAL_KEYS:
            special_hash = TxnConstants.SPECIAL_KEYS[tx_hash]
            if isinstance(special_hash, (list, tuple)):
                for spec_hash in special_hash:
                    hash_set.add(spec_hash)
            else:
                hash_set.add(special_hash)
        else:
            hash_set.add(tx_hash)

    return [h for h in hash_set]


txn_arg = click.argument("txn_hash", nargs=-1, callback=txn_hash_callback)


__all__ = [
    "account_factory",
    "get_contracts",
    "deploy",
    "verbose_option",
    "txn_arg",
    "TxnConstants",
]

import click
from ape import networks
from ape.api import ReceiptAPI
from ape.api.networks import LOCAL_NETWORK_NAME


def is_local() -> bool:
    return networks.provider.network.name in (LOCAL_NETWORK_NAME, "mainnet-fork")


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


def show_gas(receipt: ReceiptAPI):
    receipt.show_gas_report()


def show_trace(receipt: ReceiptAPI, verbose: bool, raw: bool):
    if raw:
        call_tree = networks.provider.get_call_tree(receipt.txn_hash)
        click.echo(repr(call_tree))
    else:
        receipt.show_trace(verbose=verbose)

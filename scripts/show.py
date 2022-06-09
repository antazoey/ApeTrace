from re import S
import click
from ape.cli import NetworkBoundCommand, network_option, ape_cli_context

from ._utils import raw_option, show_trace, verbose_option

# TXNS to try
FAILED_TXN = "0x053cba5c12172654d894f66d5670bab6215517a94189a9ffc09bc40a589ec04d"
FROM_TICKET_0 = "0xb7d7f1d5ce7743e821d3026647df486f517946ef1342a1ae93c96e4a8016eab7"
FROM_TICKET_1 = "0x0537316f37627655b7fe5e50e23f71cd835b377d1cde4226443c94723d036e32"
VYPER = "0x053a723780e9630687d64a40caacf5ed379816501722fe52855df16e987c5706"
SPECIAL_KEYS = {
    "fail": FAILED_TXN,
    "t0": FROM_TICKET_0,
    "t1": FROM_TICKET_1,
    "vyper": VYPER,
}


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@network_option()
@verbose_option
@raw_option
@click.argument("txn_hash")
def cli(cli_ctx, network, verbose, raw, txn_hash):
    _ = network  # Needed for NetworkBoundCommand

    if txn_hash in SPECIAL_KEYS:
        txn_hash = SPECIAL_KEYS.get(txn_hash)

    receipt = cli_ctx.network_manager.provider.get_transaction(txn_hash)
    show_trace(receipt, verbose, raw)

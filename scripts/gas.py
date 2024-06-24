import click
from ape.cli import ConnectedProviderCommand, ape_cli_context

from tracelib.click_ext import txn_arg
from tracelib.utils import show_gas


@click.command(cls=ConnectedProviderCommand)
@ape_cli_context()
@txn_arg
def cli(cli_ctx, txn_hash, provider):
    if not txn_hash:
        return

    for index in range(len(txn_hash)):
        txn_hash_value = txn_hash[index]
        if not txn_hash_value.startswith("0x") or not len(txn_hash_value) == 66:
            cli_ctx.logger.error("Incorrect txn hash '{txn_hash}'.")
            continue

        receipt = provider.get_receipt(txn_hash_value)
        click.echo()
        show_gas(receipt)
        if index < len(txn_hash) - 1:
            click.echo()

import click
from ape.cli import NetworkBoundCommand, ape_cli_context, network_option

from ._utils import show_gas, txn_arg


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@network_option()
@txn_arg
def cli(cli_ctx, network, txn_hash):
    _ = network  # Needed for NetworkBoundCommand
    if not txn_hash:
        return

    for index in range(len(txn_hash)):
        txn_hash_value = txn_hash[index]
        if not txn_hash_value.startswith("0x") or not len(txn_hash_value) == 66:
            cli_ctx.logger.error("Incorrect txn hash '{txn_hash}'.")
            continue

        receipt = cli_ctx.network_manager.provider.get_receipt(txn_hash_value)
        click.echo()
        show_gas(receipt)
        if index < len(txn_hash) - 1:
            click.echo()

import click
from ape.cli import NetworkBoundCommand, network_option

from ._utils import (account_factory, get_contracts, raw_option, show_trace,
                     verbose_option)


@click.command(cls=NetworkBoundCommand)
@network_option()
@verbose_option
@raw_option
@click.option("--skip", multiple=True)
def cli(network, verbose, raw, skip):
    _ = network  # Needed for NetworkBoundCommand
    contract_a, _, _ = get_contracts()

    if "methodWithoutArguments" not in skip:
        receipt = contract_a.methodWithoutArguments(sender=account_factory.owner)
        show_trace(receipt, verbose, raw)
        click.echo()

    if "goodbye" not in skip:
        # First, fund the contract.
        account_factory.owner.transfer(contract_a.address, 44455566)
        receipt = contract_a.goodbye(sender=account_factory[1])
        show_trace(receipt, verbose, raw)

import click
from ape.cli import NetworkBoundCommand, network_option

from tracelib.accounts import account_factory
from tracelib.click_ext import raw_option, verbose_option
from tracelib.contracts import get_contracts
from tracelib.utils import show_trace


@click.command(cls=NetworkBoundCommand)
@network_option()
@verbose_option
@raw_option
@click.option("--skip", multiple=True)
def cli(network, verbose, raw, skip):
    _ = network  # Needed for NetworkBoundCommand
    contract_a, _, _ = get_contracts()
    receipt = contract_a.methodWithoutArguments(sender=account_factory.owner, value=123)

    if "methodWithoutArguments" not in skip:
        receipt = contract_a.methodWithoutArguments(
            sender=account_factory.owner, value=123
        )
        show_trace(receipt, verbose, raw)
        click.echo()

    if "goodbye" not in skip:
        # First, fund the contract.
        account_factory.owner.transfer(contract_a.address, 44455566)
        receipt = contract_a.goodbye(sender=account_factory[1])
        show_trace(receipt, verbose, raw)

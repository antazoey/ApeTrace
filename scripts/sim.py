import click
from ape.cli import ConnectedProviderCommand

from tracelib.accounts import account_factory
from tracelib.click_ext import raw_option, verbose_option
from tracelib.contracts import get_contracts
from tracelib.utils import show_trace


@click.command(cls=ConnectedProviderCommand)
@verbose_option
@raw_option
@click.option("--skip", multiple=True)
def cli(verbose, raw, skip):
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

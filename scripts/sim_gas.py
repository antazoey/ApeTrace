import click
from ape.cli import ape_cli_context, NetworkBoundCommand, network_option

from ._utils import get_contracts


@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@network_option()
def cli(cli_ctx, network):
    _ = network  # Needed for NetworkBoundCommand
    contract_a, _, _ = get_contracts()
    account = cli_ctx.account_manager.test_accounts[0]
    receipt = contract_a.mergeGasReportTest(sender=account);
    receipt.show_gas_report()
    click.echo()

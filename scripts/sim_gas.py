import click
from ape.cli import ConnectedProviderCommand, ape_cli_context

from tracelib.contracts import get_contracts


@click.command(cls=ConnectedProviderCommand)
@ape_cli_context()
def cli(cli_ctx):
    contract_a, _, _ = get_contracts()
    account = cli_ctx.account_manager.test_accounts[0]
    receipt = contract_a.mergeGasReportTest(sender=account)
    receipt.show_gas_report()
    click.echo()

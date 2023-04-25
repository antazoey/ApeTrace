from lib.accounts import account_factory
from lib.contracts import deployer


def ape_init_extras(accounts):
    network_name = accounts.provider.network.name
    if network_name != "local":
        return {}

    return {
        "owner": account_factory.owner,
        "contract_a": deployer.contract_a,
        "contract_b": deployer.contract_b,
        "contract_c": deployer.contract_c,
    }

from tracelib.accounts import account_factory
from tracelib.contracts import deployer


def ape_init_extras(networks):
    if provider := networks.active_provider:
        if not provider.network.is_dev:
            return {}

        return {
            "owner": account_factory.owner,
            "contract_a": deployer.contract_a,
            "contract_b": deployer.contract_b,
            "contract_c": deployer.contract_c,
        }

    return {}

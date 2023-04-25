from tracelib.accounts import account_factory
from tracelib.contracts import deployer
from tracelib.utils import is_local


def ape_init_extras():
    if not is_local():
        return {}

    return {
        "owner": account_factory.owner,
        "contract_a": deployer.contract_a,
        "contract_b": deployer.contract_b,
        "contract_c": deployer.contract_c,
    }

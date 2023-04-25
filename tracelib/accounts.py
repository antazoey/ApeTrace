from functools import cached_property

from ape import accounts, networks
from ape.api import AccountAPI
from ape.cli import get_user_selected_account
from ape_accounts.accounts import KeyfileAccount

from tracelib.utils import is_local


class AccountFactory:
    @cached_property
    def owner(self) -> AccountAPI:
        if is_local():
            return self[0]

        elif networks.provider.network.name == "rinkeby":
            return accounts.load("metamask0")

        prompt = "Select an account to own these contracts"
        return get_user_selected_account(prompt_message=prompt, account_type=KeyfileAccount)

    def __getitem__(self, index: int) -> AccountAPI:
        return accounts.test_accounts[index]


account_factory = AccountFactory()

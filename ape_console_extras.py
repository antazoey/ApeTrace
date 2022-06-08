def ape_init_extras(accounts, project):
    network_name = accounts.provider.network.name
    if network_name != "local":
        return {}

    owner = accounts.test_accounts[0]
    contract_c = project.ContractC.deploy(sender=owner)
    contract_b = project.ContractB.deploy(contract_c.address, sender=owner)
    contract_a = project.ContractA.deploy(
        contract_b.address, contract_c.address, sender=owner
    )
    return {
        "owner": owner,
        "contract_a": contract_a,
        "contract_b": contract_b,
        "contract_c": contract_c,
    }

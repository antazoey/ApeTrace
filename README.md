# The Ape Trace Project

We sell trace and trace accessories.

## Setup

First, install plugins in your desired Python environment (likey a virtual-environment):

```bash
ape plugins install .
```

Then, use keyring to set your Alchemy API key:

```bash
ape keyring secrets set WEB3_ALCHEMY_PROJECT_ID
```

You, then, will be prompted for input.

Alternatively, use an environment variable as per this [guide](https://github.com/ApeWorX/ape-alchemy/blob/main/README.md#quick-usage).

## Quick Usage

To see a trace, run:

```bash
ape run show 0xb7d7f1d5ce7743e821d3026647df486f517946ef1342a1ae93c96e4a8016eab7 --network ethereum:mainnet:alchemy
```

It will fetch the transactions, relevant contract types, and display a trace in your terminal using the `show_trace()` method on Ape's transaction receipt objects.

To see additional information on the trace, use the `--verbose` flag:

```bash
ape run show 0x... --verbose
```

To see the raw `evm-trace` package version of the trace display, use the `--raw` flag:

```bash
ape run show 0x... --raw
```

There are some hard-coded transactions you can use as well via special keys, e.g.:

```bash
ape run show fail
ape run show 0
ape run show 1
ape run show vyper
```

## The Sim

Additionally, this project comes with test contracts for seeing a trace locally.
To view the local trace, run:

```bash
ape run sim
```

You can skip sections of the simulation by using the `--skip` flag:

```bash
ape run sim --skip methodWithoutArguments 
```

The `--verbose` and `--raw` flags mentioned in the first section also work for the `sim` command.

## Gas

Additionally, view gas reports on receipts using this project.
All of the same special receipts can be used for `gas` as they can for `show`.

```bash
ape run gas t0 --network ethereum:mainnet:alchemy
```

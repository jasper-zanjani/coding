# Solidity

Solidity can be coded in [**Remix**](https://remix.ethereum.org), the online editor.

```solidity title="Example contract in Solidity"
--8<-- "includes/blockchain/hw.sol"
```

Solidity can be compiled using [**solc**](https://github.com/ethereum/solc-js)
and the resulting binary file can be run in the [**EVM emulator**](https://github.com/Yashiru/evm-rs-emulator/).

```sh
# Compile Solidity smart contract
solcjs --bin hw.sol

# Run binary in emulated EVM
evm-rs-emulator hw_sol_MyContract.bin
```

The output of the emulator displays the EVM assembly instructions.
Ethereum's opcodes are described in the [Ethereum Yellow Paper](https://github.com/ethereum/yellowpaper).
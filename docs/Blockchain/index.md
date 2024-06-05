An [Ethereum account](https://ethereum.org/en/developers/docs/accounts/) is an entity with an ether balance that can send transactions on the blockchain, of two types:

- Externally owned accounts (EOA) are user-controlled by anyone with the private keys
- Contract accounts are controlled by code executed by the EVM, also known as a **smart contract**. A contract address hosts code on Ethereum which is executed when a transaction is made with associated input data (contract interaction). A smart contract is a computer program and internal storage hosted on-chain.

A wallet is an interface for managing an Ethereum account.

Every Ethereum account is associated with an **address**, a 42-character hexadecimal value which derives from the last 20 bytes of a hash of the account's public key.


A [**block**](https://ethereum.org/en/developers/docs/blocks/) is a batch of transactions stored with a hash of the previous block in the blockchain.
Time is divided into twelve second units called [**slots**](https://ethereum.org/en/developers/docs/blocks/#proof-of-work-protocol).
Every **slot** (spaced twelve seconds apart) a single validator is randomly selected to be the block proposer.
If all validators are online then there will be a block in every slot.
However if some validators are offline then some slots will remain empty.

Blocks are [bounded](https://ethereum.org/en/developers/docs/blocks/#block-size) in size, with a target size of 15 million gas and a maximum of 30 million gas, equivalent to about 1,400 simple transactions.
The total amount of gas expended by all transactions in the block must be less than this limit.

In the [**proof-of-stake protocol**](https://ethereum.org/en/developers/docs/blocks/#proof-of-work-protocol), validating nodes have to deposit or stake 32 ETH into a deposit contract as collateral.

In Ethereum, the blockchain is transformed into the data storage layer of the **Ethereum Virtual Machine** (EVM).
In this context, smart contracts are programs run by the EVM, and when memory and compute resources are consumed, **gas** fees must be paid.
Gas is the unit of resource consumption in Ethereum and is [variable](https://etherscan.io/gastracker) according to network and market conditions.
Transactions change the state of the EVM assess a fee in **gas** to be executed by a block producer and propagated to the rest of the network.

| Cost (gas) | Description                                         |
| ---------: | --------------------------------------------------- |
|     21,000 | All ETH transactions must pay                       |
|     32,000 | Create a new contract                               |
|     22,100 | For each storage variable                           |
|          4 | Per zero byte in transaction                        |
|         16 | Per non-zero byte in transaction                    |
|        200 | Per byte of deployed bytecode                       |
|   Variable | Cost to execute each bytecode during initialization |

!!! info "Associated concepts"

    - **Viper** is an alternative to Solidity that follows the indentation of Python.

    - **zkEVM**: a virtual machine that executes smart contracts in a way that is compatible with zero-knowledge-proof computation



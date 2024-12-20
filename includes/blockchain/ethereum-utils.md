# Ethereum utilities

## ganache

**ganache** is a local test blockchain (the repo is now archived).

```sh
ganache --networkId=3 --port=8545 --verbose --gasLimit=8000000 --gasPrice=4000000
```

## geth

**geth** can be installed by [downloading](https://geth.ethereum.org/downloads/).

=== "console"

    A builtin interactive JavaScript console is available through the **console** subcommand.

    ```sh
    # Run a full node on mainnet by running geth to interact with the Ethereum network
    geth console

    # Run a full node on the Goerli test network
    geth --goerli console
    ```

A testnet can be specified by providing the options **--goerli**, **--sepolia**, or **--holesky** (Ropsten, and Rinkeby are no longer valid and presumably decommissioned).

Running geth for the first time will create a tree of subdirectories under $HOME depending on the network accessed.
The connection to mainnet occurs directly under **~/.ethereum**, whereas test networks are stored in named subdirectories thereof (1).
{ .annotate }

1. 
```
.ethereum
├── geth
├── goerli
├── history
└── keystore

4 directories, 1 file
```

Geth offers [JSON-RPC](https://geth.ethereum.org/docs/interacting-with-geth/rpc) requests using an integrated server.
This server must be explicitly started with **--http**. 
By default it will listen to port 8545 on the local loopback interface, but this behavior can be changed with **--http.addr** and **--http.port**.

```sh
# Enable JSON-RPC endpoint on localhost
geth --http 

# Test connection
curl -X POST -H "Content-Type: application/json" \
    --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}' \
    http://localhost:8545 # => (1)

# Query gas price in hexadecimal (0.001 Gwei on the testnet
curl -X POST -H "Content-Type: application/json" \
    --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":1}' \
    http://localhost:8545 -s | jq .result # => "0xf4240"

# The price can be converted to decimal easily within bash
echo $((0xf4240)) # => 1000000
```

1. 
```json title="Output"
{"jsonrpc":"2.0","id":1,"result":"Geth/v1.14.5-stable-0dd173a7/linux-amd64/go1.22.4"}
```

## Tasks

<div class="grid cards" markdown>

-   #### Create a private network

    ---

    !!! info "Note"

        The following appears to work only for Geth version 1.11 available for download [here](https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.11.6-ea9e62ca.tar.gz).

    Geth can be configured to run locally without connecting to any public network by providing a genesis block.
    
    First a new directory must be created to store the new blockchain's data.
    Then an account is created within it by passing the directory's path to **--datadir** (so as not to refer to the default blockchain data).
    Note that all further invocations to geth must pass this directory to --datadir to specify the private blockchain.

    ```sh
    geth --datadir $BLOCKCHAIN_DIR account new
    ```

    [Clef](https://geth.ethereum.org/docs/tools/clef/tutorial), an account management tool, is recommended for the creation of new accounts. 

    ```sh
    clef newaccount --keystore $BLOCKCHAIN_DIR/keystore
    ```

    A password is requested interactively and a public key address is displayed to STDOUT.
    This address must then be specified along with a balance in the **genesis block** (1).
    { .annotate }

    1. 
    ```json title="genesis.json" hl_lines="14"
    --8<-- "includes/blockchain/genesis2.json"
    ```

    ```sh
    # Create the blockchain
    geth --datadir=$BLOCKCHAIN_DIR init genesis.json

    # Open a console
    geth --datadir=$BLOCKCHAIN_DIR console
    ```

    ```js title="Within geth console"
    // Check accounts details
    eth.accounts;

    eth.getBalance(eth.accounts[0]);


    // Display enode, along with other information associated with the node in JSON format
    admin.nodeInfo;

    // Add enode of a peer
    admin.addPeer("...")
    ```

    Local scripts can be executed with [**--exec**](https://geth.ethereum.org/docs/interacting-with-geth/javascript-console#non-interactive-use).

    In order to run a second node, the blockchain directory must be copied and another instance of the execution client must be running on a different port but specifying the same chain ID.

    ```sh
    geth --datadir=$BLOCKCHAIN_DIR_COPY --networkid 4785 --port 30305 --authrpc.port 8553 console
    ```

</div>

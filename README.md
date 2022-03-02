# NFT Minting

This project is used to deploy a Solidity contract to Ethereum or Robsten test network.  Once the contract is deployed, a metadata file and media are updated to the IPFS.  From there the metadata file is minted on the blockchain.  There are several steps in the is process.


## Use Alchemy to access blockchain APIs

Create account on Alchemy: https://alchemy.com


## Setup a MetaMask account

Create account on MetaMask: https://metamask.io


## Add Either from a Faucent

If deploying to the Ropsten network, use a faucet to add some funds to the MetaMask account.  - https://faucet.egorfine.com

## Initilize the project

In the project folder, initialize the Node project

```
mkdir nft
cd nft
npm init
```

## Compaile the contract with Hardhat

Hardhat is the development environment to compile, deploy, test and debug Ethereum software. This helsp build smart contracts and dApps before deploying.

```
npn install --save-dev hardhat
npc hardhat
mkdir contracts
mkdir scripts
```

## Create the Solidity contract

The smart contract is located in the contracts folder.  Install dotevn so we dan store API endpoint and API key in a .env file.

```
npm install dotenv --save
```

the `.env` should look like this:

```
API_URL="https://eth-ropsten.alchemyapi.io/v2/your-api-key"
PRIVATE_KEY="your-metamask-private-key"
```

Install Ethers.JS

```
npm install --save-dev @nomiclabs/hardhat-ethers ethers@^5.0.0
```

Compile and deploy the contract

```
npx hardhat compile
npx hardhat --network ropsten run scripts/deploy.js
```

The smart contract is now deployed on the blockchain.  Now to install Web 3 and mint the NFT. A mint-nft.js is deployed to the scripts folder.

```
npm install @alch/alchemy-web3
```

Run the following command to test the mint-nfs.js:

```
node scripts/mint-nft.js
```

Build the metadata.json file describing the object to be minted and store it in the metadata folder.

## Use Piñata account to deploy files to IPFS

Open account on https://app.pinata.cloud/.  Upload the media first and grab the URL for its location.  Save that location into the metadata.json file and upload the json file also.  Copy the URL to the metadata.json file to the mint-nft.js file in the scripts folder.

```
mintNFT(
    "https://gateway.pinata.cloud/ipfs/QmPpxBbDhwP9noSFA2CL6AkVRWbzEr8JgqkaUrd3Wmf4Cy"
)
```

Add PRIVATE_KEY to the .env file.  This is the private key from the MetaMask account.  Make sure .env is in the .gitignore so it doesn't get checked into source code.

Lastly, run the mint script to deploy the NFT.

```
node scripts/mint-nft.js
```


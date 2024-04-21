from enum import Enum


class EthNet(Enum):
    MainNet = "mainnet"
    Ropsten = "ropsten"
    Rinkeby = "rinkeby"
    Gorli = "gorli"
    Xdai = "xdai"
    Kovan = "kovan"

    BscNet = "bscnet"
    BmcTestNet = "btm_test_net"


ETH_ADDRESS = "0x0000000000000000000000000000000000000000"
WETH9_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# see: https://chainid.network/chains/
# _netid_to_name = {
#     1: "mainnet",
#     3: "ropsten",
#     4: "rinkeby",
#     56: "binance",
#     97: "binance_testnet",
#     100: "xdai",
# }

_factory_contract_addresses_v1 = {
    EthNet.MainNet.value: "0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95",
    EthNet.Ropsten.value: "0x9c83dCE8CA20E9aAF9D3efc003b2ea62aBC08351",
    EthNet.Rinkeby.value: "0xf5D915570BC477f9B8D6C0E980aA81757A3AaC36",
    EthNet.Kovan.value: "0xD3E51Ef092B2845f10401a0159B2B96e8B6c3D30",
    EthNet.Gorli.value: "0x6Ce570d02D73d4c384b46135E87f8C592A8c86dA",
}

# For v2 the address is the same on mainnet, Ropsten, Rinkeby, Görli, and Kovan
# https://uniswap.org/docs/v2/smart-contracts/factory
_factory_contract_addresses_v2 = {
    EthNet.MainNet.value: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    EthNet.Ropsten.value: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    EthNet.Rinkeby.value: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    EthNet.Gorli.value: "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
    EthNet.Xdai.value: "0xA818b4F111Ccac7AA31D0BCc0806d64F2E0737D7",
    EthNet.BscNet.value: "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73",
    EthNet.BmcTestNet.value: "0xd3add19ee7e5287148a5866784aE3C55bd4E375A",
}

_router_contract_addresses_v2 = {
    EthNet.MainNet.value: "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    EthNet.Ropsten.value: "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    EthNet.Rinkeby.value: "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    EthNet.Gorli.value: "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
    EthNet.Xdai.value: "0x1C232F01118CB8B424793ae03F870aa7D0ac7f77",
    EthNet.BscNet.value: "0x10ED43C718714eb63d5aA57B78B54704E256024E",
    EthNet.BmcTestNet.value: "0x8b3BdEcEac3d23A215300A3df19e1bEe43A0Ac9C",
}

_quoter_contract_addr_v3 = {
    EthNet.MainNet.value: "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6",
    EthNet.BmcTestNet.value: "0x8c13AFB7815f10A8333955854E6ec7503eD841B7",
}

_router_contract_addresses_v3 = {
    EthNet.MainNet.value: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
    EthNet.BmcTestNet.value: "0x54d28562271De782B261807a01d1D2fb97417912",
}

# bytom 跨链相关配置
CROSS_ETH_RECEIVER_ADDRESS = "0x7303dd1F1E2e494b0D7F6Df3C6ACC113380978c0"
CROSS_USDT_ERC20_RECEIVER_ADDRESS = "0x840edae86e2Bf6cAA13CcbDEbbDDc8f153064087"
CROSS_USDC_RECEIVER_ADDRESS = "0x7e87c78089b92d354cc31104152ef5385fcc30e8"
CROSS_DAI_RECEIVER_ADDRESS = "0xc9390c509ebaac49e89581fe725e55c3d5e9ab14"


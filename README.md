# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1

Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
> profitable path: B -> A -> D -> C -> B
> amount: 5 -> 5.655321988655322 -> 2.4587813170979333 -> 5.0889272933015155 -> 20.129888944077443
> final reward: 20.129888944077443

## Problem 2

What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
> Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual executed price. It occurs because of the constant price updates in the pool as trades are made, causing the price to shift as the trade size increases.

Uniswap V2 addressed the issue of slippage by implementing a feature called "constant product invariant" or the "x\*y=k" formula. In Uniswap V2, each trading pair's liquidity pool maintains a constant product of the quantities of the two assets it holds. This means that the product of the number of tokens in the pool (x) and the price of those tokens (y) remains constant.

We can assume that users all have a desire amount to get. With Uniswap V2, when the qunatities don't match, Uniswap V2 would "cancel" the transaction. That is, a user assume he gets 10 ether by giving 1 ether, but he in fact gets 8 ether by giving 1, Uniswap V2 can cancel the transaction and return the 1 ether back to the user.

## Problem 3

Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
> Uniswap v2 initially mints shares equal to the geometric mean of the amounts deposited. It is possible for the value of a liquidity pool share to grow over time, either by accumulating trading fees or through “donations” to the liquidity pool. In theory, this could result in a situation where the value of the minimum quantity of liquidity pool shares (1e-18 pool shares) is worth so much that it becomes infeasible for small liquidity providers to provide any liquidity. To mitigate this, Uniswap v2 burns the first 1e-15 (0.000000000000001) pool shares that are minted (1000 times the minimum quantity of pool shares), sending them to the zero address instead of to the minter. This should be a negligible cost for almost any token pair.11 But it dramatically increases the cost of the above attack. In order to raise the value of a liquidity pool share to $100, the attacker would need to donate $100,000 to the pool, which would be permanently locked up as liquidity.

- (https://ethereum.stackexchange.com/questions/132491/why-minimum-liquidity-is-used-in-dex-like-uniswap)[Why MINIMUM_LIQUIDITY is used in DEX like Uniswap?]
- (https://uniswap.org/whitepaper.pdf)[Uniswap V2 Whitepaper]

## Problem 4

Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
> The LP tokens you mint from providing liquidity = (amount of tokens deposited in to the Liquidity Pool)/(amount of tokens in the Liquidity Pool) \* (amount of total Liquidity tokens), or really it's your Liquidity share multiplied by the current amount of Liquidity tokens.

```
liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1);
```

The liquidity should match the original ratio, which ensures the balance in the liquidity pool won't be destroyed.

- (https://www.reddit.com/r/UniSwap/comments/i49dmk/how_are_lp_token_amounts_calculated/)[LP Token Calcualtion]

## Problem 5

What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
> A sandwich attack refers to when a victim transaction trades a crypto-currency asset X to another crypto-asset Y and makes a large purchase. A bot sniffs out the transaction and Front-Runs the victim by purchasing asset Y before the large trade is approved. This purchase raises the price of asset-Y for the victim trader and increases the slippage (Expected price increase or decrease in price based on the volume to be traded and the available liquidity). Because of this high purchase of asset Y, its price goes up, and Victim buys at a higher price of asset Y, then the attacker sells at a higher price. If being attacked at a swap, I would get less asset as expected.

- (https://medium.com/coinmonks/defi-sandwich-attack-explain-776f6f43b2fd)[DEFI Sandwich Attack Explain]

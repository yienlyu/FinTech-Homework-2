liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getAmountOut(delta_x, x, y):
    return (997 * delta_x * y) / (1000 * x + 997 * delta_x)

tmp_keys = liquidity.keys()
liquidity_tmp = {}

for key in tmp_keys:
    # print(key)
    liquidity_tmp[(key[1], key[0])] = (liquidity[key][1], liquidity[key][0])

liquidity.update(liquidity_tmp)
# print(liquidity)

liq_list = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

delta_x = 5
max_profit = 0
max_path = []

def findPath(curr, profit, used):
    if curr == "tokenB" and len(used) > 0:
        global max_profit
        global max_path

        if profit > max_profit:
            max_path = used
            max_profit = profit
        return
    
    for liq in liq_list:
        if liq not in used and liq != curr:
            amount = getAmountOut(profit, liquidity[(curr, liq)][0], liquidity[(curr, liq)][1])
            findPath(liq, amount, used + [liq])

if __name__ == "__main__":
    findPath("tokenB", delta_x, [])

    amount = 5

    print_str = "path: tokenB"
    prev = "tokenB"
    for node in max_path:
        print_str += "->"
        print_str += str(node)
        amount = getAmountOut(amount, liquidity[(prev, node)][0], liquidity[(prev, node)][1])
        # print(amount)
        prev = node 

    print_str += ", tokenB balance = "
    print_str += str(max_profit)

    print(print_str)
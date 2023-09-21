# DefineWrite a program that finds the best days to buy and sell stocks to maximize profit, given an array of stock prices. Return the maximum profit that can be made. If no profit can be made, return -1.

def maximum_profit(stock_price_list):
    ans = 0  # initialize the maximum profit to 0
    for i in range(len(stock_price_list)):  # loop through each stock price
        for j in range(i+1,len(stock_price_list)):  # loop through each stock price after the current one
            if stock_price_list[j]>stock_price_list[i]:  # if the current stock price is less than the next one
                ans = max(ans,stock_price_list[j]-stock_price_list[i])  # calculate the profit and update the maximum profit if necessary
    if ans == 0:  # if the maximum profit is still 0, there was no profit to be made
        return -1  # return -1 to indicate this
    return ans  # otherwise, return the maximum profit
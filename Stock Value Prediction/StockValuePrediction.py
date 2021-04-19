

"""

Muhammad Marzouk Baig
Lab Section MW 12:30pm - 1:40pm

Fall 2019"""


"""In this project I have designed an algorithm which takes data from previous days and then uses
them to predict wehther it would be profitable to either buy sell or take no action on the day of the trading
It takes the first 10 days to observe before actually having enough data to make decisions. (More detailed
information of how my algorithm works in the docstring under the class: "result")
"""
# use Argument AAPL.csv.txt for an example
# this class helps to return raw stock data from stock data in the given files
class raw_stock_data:

    def __init__(self, filename):

        # all needed variables and lists initiated here

        self.filename = filename
        self.read = ''
        self.readlines = ''
        self.row = 0
        self.table = []
        self.column = []
        self.table = []
        self.r = 0
        self.c = 0
        self.list_high = []
        self.list_low = []
        self.list_close = []
        self.co = 0
        self.ca = 0
        self.cb = 0

    def return_stock_data(self):

        # open and read lines

        self.read = open(self.filename, 'r')
        self.read.readline()
        self.readlines = self.read.readlines()
        self.row = 0

        # loop for forming rows using lists

        for i in self.readlines:
            self.readlines[self.row] = i[0:len(i) - 1]

            # row incremented to keep foring new rows

            self.row += 1
        self.read.close()

        # columns formed for every heading (col)

        for j in range(self.row + 1):
            self.column = []
            for x in range(8):

                # empty strings inserted for every row and column

                self.column.append('')
            self.table.append(self.column)

        self.row = 1
        for y in self.readlines:

            # lines are split and commas removed

            self.r = y.split(',')
            self.c = 0
            for z in self.r:

                # this line of code allows the program to point at a specific position in a row or column
                # like on a graph with a coordinate system
                # first square bracket is the row and second is the column

                self.table[self.row][self.c] = z
                self.c += 1
            self.row += 1

        self.list_high = []
        self.list_low = []
        self.list_close = []

        for i in range(1, 4635):
            self.co = float(self.table[i][2])
            self.ca = float(self.table[i][3])
            self.cb = float(self.table[i][4])
            self.list_high.append(self.co)
            self.list_low.append(self.ca)
            self.list_close.append(self.cb)

        return (self.list_high, self.list_low, self.list_close)

# this class helps to return data in lists for other classes to use
# extra credit work done: Classes used to complete algorithm
class pass_data:

    def __init__(
        self,
        highlist,
        lowlist,
        closelist,
        ):
        self.list_high = highlist
        self.list_low = lowlist
        self.list_close = closelist

    def high_low_close(self):
        return (self.list_high, self.list_low, self.list_close)

# this class helps to return moving averages for comparisons used in my algorithm
class Averages:

    def __init__(
        self,
        list1,
        list2,
        list3,
        ):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.sum1 = 0
        self.sum2 = 0
        self.sum3 = 0

    def return_averages(self):
        self.list11 = []
        self.list22 = []
        self.list33 = []

        for i in range(len(self.list1)):
            self.sum1 = 0
            self.sum2 = 0
            self.sum3 = 0

            for p in self.list1[i - 10:i]:
                self.sum1 += p
            mean_1 = self.sum1 / 10
            self.list11.append(mean_1)

            for q in self.list2[i - 10:i]:
                self.sum2 += q
            mean_2 = self.sum2 / 10
            self.list22.append(mean_2)

            for r in self.list3[i - 10:i]:
                self.sum3 += r
            mean_3 = self.sum3 / 10
            self.list33.append(mean_3)

        return (self.list11[10:], self.list22[10:], self.list33[10:])

# this class helps carry out all the actual comparison and deciding wether to buy or sell
# extra credit work done: Classes used to complete algorithm
class result:
    """This class is where the actual compariosn and decision making takes place
       My algorithm takes the moving averages of the previous 10 for high, low,
       closing values and then compares wehther the average of the high values
       is closer to the closing values or if the average of the low values are closer
       to the closing values.(I have used the closing values to determine the price or
       worth of a stock). If the average of high values is closer to closing values by more
       than 20% of the difference between average low values and closing values, the algorithm
       decides to sell the stocks as on that day it will have greater probabiltiy of having a
       high value, as suggested by the average of the last 10 days, however if the average of
       low values is closer to the closing values by more than 20% of the difference between
       average of high values and closing values, the algorithm decides to buy, as
       the prices of the stocks have high probability of being low, as predicted by the averages
       of the last 10 days"""

    def __init__(
        # class takes in lists, as paarmters, of moving averages of
        # high, low and closing vals
        self,
        x,
        y,
        z,
        closingval,
        ):
        # closing values averages list
        self.z = z[10:]
        # low values averages list
        self.y = y[10:]
        # high values averages list
        self.x = x[10:]
        # actual closing values to determine price of stock
        self.closingval = closingval

    def comparing_and_taking_action(self):
        # initial cash_balance of 1000 alotted
        cash_balance = 10000
        stocks_owned = 0

        # loop to compare moving averages of last days on a given day
        # moving averages of high, low and closing stock values used
        for i in range(0, len(self.z)):

            if abs(self.x[i] - self.z[i]) > 1.10 * (abs(self.y[i] - self.z[i])):

                S = transact(
                    cash_balance,
                    stocks_owned,
                    10,
                    self.closingval[i],
                    buy=False,
                    sell=True,
                    )
                print(cash_balance, stocks_owned)
                
                (cash_balance, stocks_owned) = S.transact_()

                
            elif 1.10 * (abs(self.x[i] - self.z[i])) < abs(self.y[i]
                    - self.z[i]):

                S = transact(
                    cash_balance,
                    stocks_owned,
                    10,
                    self.closingval[i],
                    buy=True,
                    sell=False,
                    )
                print(cash_balance, stocks_owned)
                (cash_balance, stocks_owned) = S.transact_()
            else:
                pass

            # in the end all stocks sold
            

        return (cash_balance, stocks_owned)



# this class is used to carry out actual purchasing and sale of stocks 
class transact:

    def __init__(
        self,
        funds,
        stocks,
        qty,
        price,
        buy=False,
        sell=False,
        ):

        self.cash_balance = funds 
        self.stocks_owned = stocks
        self.qty = qty
        self.price = price
        self.buy = buy
        self.sell = sell

    def transact_(self
                  ):
        #print(self.stocks)

    # error 1 checked here, if buy and sell not mentioned error message returned

        if self.buy == str() and self.sell == str():

            return (self.cash_balance, self.stocks_owned)
        elif self.buy == True and self.sell == True or self.buy \
            == False and self.sell == False:

    # error 1 checked again to make sure either vuying or selling is true

            return (self.cash_balance, self.stocks_owned)
        elif self.buy == True and (self.price * self.qty) > self.cash_balance:

    # error 2 checked to make sure enough funds available

            return (self.cash_balance, self.stocks_owned)
        elif self.stocks_owned < self.qty and self.sell == True:

    # error 2 checked to make sure enough stocks available

            return (self.cash_balance, self.stocks_owned)

    # this runs if there are no errors

        else:
            
            if self.buy == True:

                # if buying cash balance decrease and stocks increase

                self.cash_balance = self.cash_balance - (self.price * self.qty)
                self.stocks_owned = self.stocks_owned + self.qty
                return (self.cash_balance, self.stocks_owned)
            elif self.sell == True:

                # if selling cash balance increases and stocks decrease

                self.cash_balance = self.cash_balance + (self.price * self.qty)
                self.stocks_owned = self.stocks_owned - self.qty
                return (self.cash_balance, self.stocks_owned)


# this class is used to compare individual values from lists in milestone 2
# new version made to accomodate my algorithm (class Averages)
# extra credit work done: Classes used to complete algorithm
class compare:

    def __init__(self, cv, ma):
        self.cv = cv
        self.ma = ma
        self.percent = 0
        self.lower_diff = 0
        self.upper_diff = 0
        

    def compare_(self):
        self.percent = 0.05 * self.ma
        self.upper_diff = self.ma + self.percent
        self.lower_diff = self.ma - self.percent
        if self.cv >= self.upper_diff:
            return 'sell'
        elif self.lower_diff < self.cv < self.upper_diff:
            return 'do nothing'
        else:
            self.cv <= self.lower_diff
            return 'buy'

# function from previous milestone (2)
def alg_moving_average(filename):

    # last thing to do, return two values: one for the number of stocks you end up with
    # and the number of stoccks you end up with

    # closing values used here

    ab = raw_stock_data(filename)
    a, b, c = ab.return_stock_data()

    # moving averages used for comparison

    e = Averages(a, b, c)
    f, g, h = e.return_averages()

    # length of lists sliced to match eachother and give proper results

    c = c[20:]
    h = h[20:]
    cash_balance = 1000
    stocks_owned = 0

    # loop to compare all closing values and moving averages one by one

    for i in range(len(c)-20):
        m = c[i]
        n = h[i]

        # comparison function used to decide wehther to buy, sell or do nothing

        l = compare(m, n)
        if l.compare_() == 'sell':
            v = transact(
                cash_balance,
                stocks_owned,
                10,
                n,
                buy=False,
                sell=True,
                )
            (cash_balance, stocks_owned) = v.transact_()
        elif l.compare_() == 'buy':
            v = transact(
                cash_balance,
                stocks_owned,
                10,
                n,
                buy=True,
                sell=False,
                )
            (cash_balance, stocks_owned) = v.transact_()
        else:
            pass
    v = transact(cash_balance,
                 stocks_owned,
                 stocks_owned,
                 n,
                 buy=False,
                 sell=True)
    cash_balance, stocks_owned = v.transact_()

    return (stocks_owned, cash_balance)

# this function calls all methods and classes to put together the algorithmic trading 
def my_algorithm(input_):
    # raw stock data imported 
    A = raw_stock_data(input_)
    # raw stock data retunred
    (B, C, D) = A.return_stock_data()
    E = pass_data(B, C, D)
    (F, G, H) = E.high_low_close()
    # moving averages calculated
    I = Averages(F, G, H)
    (J, K, L) = I.return_averages()
    # moving averages passed into the following class and trading carried
    # results displayed
    M = result(J, K, L, H)
    (N, O) = M.comparing_and_taking_action()
    return N, O


def main():
    input_ = input("Please enter the file who's stock data you would like to use: ") 
    cash_balance1, stocks_owned1 = my_algorithm(input_)

    print('\t\n\rUsing my algorithm; \t\nStocks owned = {0}, \t\nCash_balance = {1}'.format(stocks_owned1, cash_balance1))
    print("\n\n")
    stocks_owned0, cash_balance0 = alg_moving_average(input_)
    print('\t\nUsing alg_moving average; \t\nStocks owned = {0}, \t\nCash_balance = {1}'.format(stocks_owned0, cash_balance0))


if __name__ == '__main__':

    main()

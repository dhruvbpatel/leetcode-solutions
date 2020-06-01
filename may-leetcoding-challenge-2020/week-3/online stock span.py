class StockSpanner:

    def __init__(self):
        self.st = []
        
    def next(self, price: int) -> int:
        st = self.st
        span = 1
        while st and st[-1][1]<=price:
            span+=st.pop()[0]
        
        st.append((span,price))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
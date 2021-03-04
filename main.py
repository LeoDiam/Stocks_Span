def simple_stock_span(quotes):
    spans = []
    for i in range(len(quotes)):
        k = 1
        span_end = False
        while i - k >= 0 and not span_end:
            if quotes[i - k] <= quotes[i]:
                k += 1
            else:
                span_end = True
        spans.append(k)
    return spans

def read_quotes(filename):
    dates = []
    quotes = []
    with open(filename) as quotes_file:
        for line in quotes_file:
            if line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            month, day, year = parts[0].split('/')
            date = '/'.join((year, month, day))
            dates.append(date)
            quotes.append(float(parts[-1]))
    return dates, quotes

dates, quotes = read_quotes("djia.csv")



spans_simple = simple_stock_span(quotes)
print(spans_simple)

max_value = max(spans_simple)
print("max_span value is ",max_value)
print("size of quotes is ", len(quotes))

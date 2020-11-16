def initialize(context):
    
    context.fb = sid(42950)
    
    schedule_function(rebalance,
                      date_rules.every_day(),
                      time_rules.market_open(hours=1))
    
def rebalance(context, data):
    
    history_50 = data.history(context.fb,
                              fields='price',
                              bar_count=7,
                              frequency='1d')
    
    history_200 = data.history(context.fb,
                               fields='price',
                               bar_count=30,
                               frequency= '1d')
    
    sma_50 = history_50.mean()
    sma_200 = history_200.mean()
    
    if data.can_trade(context.fb):
        
        if sma_50>sma_200:
            order_target_percent(context.fb, 1)
            
        elif sma_50<sma_200:
            order_target_percent(context.fb, 0)
     
    if sma_50>sma_200:
        print('buying')
        
    if sma_50<sma_200:
        print('Selling-Hold')
    
    
    record(Moving_Average_50=sma_50, Moving_average_200=sma_200)
def initialize(context):
    
    context.gm = sid(40430)
    
    schedule_function(rebalance,
                      date_rules.every_day())
    
def rebalance(context, data):
    
    price_history = data.history(context.gm,
                                 fields='price',
                                 bar_count=3,
                                 frequency='1d')
    
    volume_history = data.history(context.gm,
                                  fields='volume',
                                  bar_count=5,
                                  frequency='1d')
    
    sma_3 = price_history.mean()
    volume_sma_5 = volume_history.mean()
    
    gm_price = data.current(context.gm, 'price')
    
    gm_volume = data.current(context.gm, 'volume')
    
    if data.can_trade(context.gm):
        
        if gm_price > (1.01*sma_3):
            
            order_target_percent(context.gm, 1)
            
            print (context.portfolio.positions_value)
        elif gm_price < sma_3 and gm_volume > volume_sma_5:
            
            order_target_percent(context.gm, 0)
       
"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total = 0.0
        self._cookies = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\nTime:             "+str(self._time)+"\n" \
             + "Current Cookies:  "+str(self._cookies)+"\n" \
             + "CPS:              "+str(self._cps)+"\n" \
             + "Total Coockies:   "+str(self._total)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        until = (cookies - self._cookies) / self._cps
        if until < 0.0:
            until = 0.0
        until = int(until) * 1.0
        if until * self._cps + self._cookies < cookies:
            until += 1.0
        return until
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            self._time += time
            self._cookies += time * self._cps
            self._total += self._cps * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._cookies >= cost:
            self._cookies -= cost
            self._cps = self._cps + additional_cps
            self._history.append((self._time, item_name, cost, self._total))
            
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """

    build_info_clone = build_info.clone()
    state = ClickerState()
    while state.get_time() <= duration:
        current_time = state.get_time()
        if current_time > duration:
            break
        next_item = strategy(state.get_cookies(), state.get_cps(), state.get_history,
                             duration - current_time, build_info_clone)
        if next_item == None:
            break
        cost = build_info_clone.get_cost(next_item)
        time_until = state.time_until(cost)
        if time_until > duration - current_time:
            break
        state.wait(time_until)
        state.buy_item(next_item, cost, build_info_clone.get_cps(next_item))
        build_info_clone.update_item(next_item)
    if state.get_time() < duration:
       state.wait(duration - state.get_time())
    return state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    item = "Cursor"
    if time_left * cps < (build_info.get_cost(item) - cookies):
        item = None
    return item

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always select the cheapest item
    """
    
    items = build_info.build_items()
    cheap = items[0]
    for item in items:
        if build_info.get_cost(item) < build_info.get_cost(cheap):
            cheap = item
    if time_left * cps < (build_info.get_cost(cheap) - cookies):
        cheap = None
    return cheap

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always select the most expensive item that is affordable
    """
    
    items = build_info.build_items()
    afford = time_left * cps + cookies
    expensive = None
    cost = -1
    for item in items:
        if build_info.get_cost(item) <= afford and build_info.get_cost(item) >= cost:
            expensive = item
            cost = build_info.get_cost(item)
    return expensive   

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    Best strategy
    """
    items = build_info.build_items()
    afford = time_left * cps + cookies
    affords =[]
    for item in items:
        if build_info.get_cost(item) <= afford:
            affords.append(item)
    best = 0
    selected = None
    for item in affords:
        #if (cps + item[3]) * (time_left - item[2]) / item[1]  > best:
        #    best = (cps + item[3]) * (time_left - item[2]) / item[1] 
        #    selected = item[0]
        if build_info.get_cps(item) / build_info.get_cost(item) > best:
            selected = item
            best = build_info.get_cps(item) / build_info.get_cost(item)
    return selected
    
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    


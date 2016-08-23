"""
Planner for Yahtzee

Simplifications:  only allow discard and roll, only score
against upper level.
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

##########################################
# Helper functions
##########################################

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences
    of outcomes of given length.
    """
    
    answer_set = set([()])
    
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
        
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to
    the upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    
    result = 0
    if len(hand) > 0:
        scores = {}
        
        for scr in hand:
            if scr not in scores.keys():
                scores[scr] = scr
            else:
                scores[scr] += scr

        result = max(scores.values())
        
    return result

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    all_seq = gen_all_sequences(range(1, num_die_sides + 1),
                                num_free_dice)
    
    sum_seq = 0.0
    for seq in all_seq:
        sum_seq += score(list(held_dice) + list(seq))
    
    exp_value = sum_seq / len(all_seq)

    return exp_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    holds_set = set([()])
    masks = list(gen_all_sequences(range(2), len(hand)))
    
    for mask in masks:
        holds_set.add(tuple([hand[i] for i in xrange(len(hand)) if mask[i]]))

    return holds_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score
    and the second element is a tuple of the dice to hold
    """
    
    holds = gen_all_holds(hand)
    
    exp_value = 0.0
    for hold in holds:
        aux = expected_value(hold, num_die_sides, len(hand) - len(hold))
        if aux > exp_value:
            exp_value = aux
            held = hold
    
    return (exp_value, held)

##########################################
# Example functions
##########################################

def run_example():
    """
    Compute the dice to hold and expected score for an example
    hand
    """
    
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    
    print "Best strategy for hand", hand
    print "is to hold", hold
    print "with expected score", hand_score
    print
    
#run_example()

##########################################
# Test functions
##########################################

#import user35_oGFuhcPNLh_0 as score_testsuite
#print "Testing score"
#print "...................."
#score_testsuite.run_suite(score)
#print

#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#print "Testing expected_value"
#print "...................."
#expected_value_testsuite.run_suite(expected_value)
#print

#import poc_holds_testsuite
#print "Testing gen_all_holds"
#print "...................."
#poc_holds_testsuite.run_suite(gen_all_holds)

#import user35_mGREPnDxbs_0 as strategy_testsuite
#strategy_testsuite.run_suite(strategy)
#print

#import user35_U2vQEq960r_0 as tests
#tests.test_score(score)
#tests.test_expected_value(expected_value)
#tests.test_strategy(strategy)

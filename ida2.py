def record(s, e, g, h):
    print("Using pattern database heuristic")
    print("Expanded Nodes:     %5d" % e)
    print("Generated Nodes:    %5d \n" % g)

def ida(state, h):
    state.parent = None
    expanded = 0
    generated = 0

    def search(state, g, f_bound, exp, gen):
        exp += 1
        f_state = g + state.heuristic(h)
        if f_state > f_bound:
            return None, f_state, exp, gen
        if state.check_goal():
            return state, f_state, exp, gen
        minim = 10000000
        for child in state.get_children():

            gen += 1
            goal, new_f_bound, exp, gen = search(child, g + 1, f_bound, exp, gen)
            if goal is not None:
                return goal, new_f_bound, exp, gen
            if new_f_bound < minim:
                minim = new_f_bound



        return None, minim, exp, gen


    f_bound = state.heuristic(h)
    if state.check_goal():
        return state
    while True:
        goal_found, new_f_bound, expanded, generated = search(state, 0, f_bound,
                                                            expanded, generated)
        if goal_found is not None:
            break
        if f_bound == 10000000:
            return False
        f_bound = new_f_bound

    size = goal_found.solution_length()
    record(size, expanded, generated, h)
    return goal_found


pref_a = {
    "a1": ["b1", "b2", "b3", "b4"],
    "a2": ["b2", "b3", "b1", "b4"],
    "a3": ["b3", "b1", "b2", "b4"],
    "a4": ["b1", "b2", "b4", "b3"],
}

pref_b = {
    "b1": ["a2", "a3", "a4", "a1"],
    "b2": ["a3", "a4", "a1", "a2"],
    "b3": ["a4", "a1", "a2", "a3"],
    "b4": ["a2", "a3", "a4", "a1"],
}


round = 0

free_a = list(pref_a.keys())
matches = {}

while (free_a):
    curr_a = free_a.pop(0)
    proposed = pref_a[curr_a].pop(0)

    if proposed not in matches:
        matches[proposed] = curr_a
        state = "accepted"
        new_pair = f"{curr_a} ------ {proposed}"

    elif pref_b[proposed].index(matches[proposed]) > pref_b[proposed].index(curr_a):
        free_a.append(matches[proposed])
        matches[proposed] = curr_a
        state = "accepted"
        new_pair = f"{curr_a} ------ {proposed}"

    else:
        free_a.append(curr_a)
        state = "rejected"
        new_pair = "nothing"
    
    round+=1

    print(f"Round {round}: Offer from {curr_a} to {proposed} was {state} resulting in   {new_pair}\n")


print("\nFinal pairings: ")
for match in matches:
    print(f"{matches[match]} ------ {match}")
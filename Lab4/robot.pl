% Defining actions
act( go(X),
    [at(shakey, X), connected(X,Y)],
    [at(shakey, X)],
    [at(shakey, Y)]
    ).

act( light_on(L),
     [at(shakey, X), at(B, X), on(shakey, B), lightswitch(L,X), lightoff(X)],
     [lightoff(X)],
     [lighton(X)]
     ).

act(light_off(L),
    [at(shakey, X), at(B, X), on(shakey, B), lightswitch(L,X), lighton(X)],
    [lighton(X)],
    [lightoff(X)]
    ).

act(climbup(B),
    [at(shakey, X), at(B, X), box(B), on(shakey, floor)],
    [on(shakey, floor)],
    [on(shakey, B)]
    ).

act(climbdown(B),
    [box(B), on(shakey, B)],
    [on(shakey, B)],
    [on(shakey, floor)]
    ).

act(push(B,X,Y),
    [at(shakey, X), at(B, X), box(B), on(shakey, floor), connected(X,Y)],
    [at(shakey, X), at(B,X)],
    [at(shakey, Y), at(B,Y)]
    ).

goal_state([lightoff(room1)]).

initial_state(
    [
        connected(room1, door1),
        connected(room2, door2),
        connected(room3, door3),
        connected(room4, door4),

        connected(door1, room1),
        connected(door2, room2),
        connected(door3, room3),
        connected(door4, room4),

        connected(door1, corridor),
        connected(door2, corridor),
        connected(door3, corridor),
        connected(door4, corridor),

        connected(corridor, door1),
        connected(corridor, door2),
        connected(corridor, door3),
        connected(corridor, door4),

        at(shakey, room3),
        on(shakey, floor),
        at(box1, room1),
        at(box2, room1),
        at(box3, room1),
        at(box4, room1),

        box(box1),
        box(box2),
        box(box3),
        box(box4),

        lightswitch(light1, room1),
        lightswitch(light2, room2),
        lightswitch(light3, room3),
        lightswitch(light4, room4),

        lighton(room1),
        lightoff(room2),
        lightoff(room3),
        lighton(room4)
    ]
)
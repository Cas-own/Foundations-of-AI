% Facts: Who is a parent and their gender
parent(john, mary).
parent(john, jeff).
parent(ann, mary).
parent(ann, jeff).
parent(mary, james).

male(john).
male(jeff).
male(james).
female(ann).
female(mary).

% Rules: Defining relationships based on facts
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.% Facts: Who is a parent and their gender
parent(john, mary).
parent(john, jeff).
parent(ann, mary).
parent(ann, jeff).
parent(mary, james).

male(john).
male(jeff).
male(james).
female(ann).
female(mary).

% Rules: Defining relationships based on facts
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y% Facts: Who is a parent and their gender
parent(john, mary).
parent(john, jeff).
parent(ann, mary).
parent(ann, jeff).
parent(mary, james).

male(john).
male(jeff).
male(james).
female(ann).
female(mary).

% Rules: Defining relationships based on facts
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y
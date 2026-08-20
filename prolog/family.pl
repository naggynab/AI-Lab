% family.pl -- standard (ISO / SWI) Prolog version of FATHER-MOTHER
% Turbo Prolog needs predicates/clauses/goal sections; SWI-Prolog does not.
% You just write the facts and rules directly.

% --- facts ---
mother(rani, aditya).
husband(suvash, rani).

% --- rules ---
father(A, C) :-
    husband(A, B),
    mother(B, C).

% --- entry point (what Turbo Prolog's `goal` section did) ---
main :-
    forall(father(X, aditya),
           format("father of aditya is ~w~n", [X])).

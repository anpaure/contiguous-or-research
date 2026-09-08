# Recency rank budget and the cost of the six-way ports

2026-09-08. Independent pure-proof audit of the user's rank-budget identity.
No mathematical program was run.

**Verdict:** the identity is exact for a literal word started from the
empty recency state. It also gives a direct obstruction to putting all six
of the proposed k17 port transitions into a length-B(17) word. This does
not invalidate the abstract biclique or its coherent fusion theorem.

## 1. Definitions

For an ordered recency partition P, let b_s(P) be the number of its
nonempty prefix unions whose rank is strictly less than s. A state has
at most one prefix of rank exactly s, because its blocks are nonempty.

Read a word of N nonempty letters from the empty state P_0. Let D_s be
the number of distinct rank-s targets seen among the prefix unions of
P_1,...,P_N. By the exact move-to-front theorem these are exactly the
rank-s targets realized by the literal word's nonempty intervals.

For the ith update write Delta_i=b_s(P_i)-b_s(P_(i-1)). Define

    L=sum_i max(-Delta_i,0),

and let E count the updates at which no new rank-s target appears and
Delta_i<=0. Thus L counts units of decrease, while E counts steps.

## 2. Two exact facts about one move

Write the old cumulative block unions as

    C_0=empty, C_1,...,C_m.

After appending X, the new prefix unions are precisely the distinct sets
among X union C_j,0<=j<=m, with repeated values deleted.
Every old C_j of rank at least s has X union C_j of rank at least s.
Therefore the new prefixes of rank below s must come from the old
b_s(P) low prefixes or from C_0. This proves

    Delta_i<=1.                                               (1)

If equality holds, all b_s(P)+1 candidate sets from these indices must
be distinct and remain below rank s. Any rank-s prefix in the new
state must then come from an old C_j already having rank at least s.
But X union C_j can have rank s only if C_j has rank s and
X subseteq C_j. The target is then exactly that old prefix target.
Consequently

    Delta_i=1 implies that the step has no new rank-s target.    (2)

This is stronger than a mere bound on the number of new targets:
the rank-s prefix, if present after an upward step, was already present
in the immediately preceding state.

## 3. The identity

Let U count the upward steps. Since the quantities are integers, (1)
makes every upward increment exactly one. Telescoping from b_s(P_0)=0
therefore gives

    b_s(P_N)=U-L.

Every step creates either zero or one new rank-s target, so N-D_s is
the number of steps with no new rank-s target. By (2), these split
disjointly into the U upward steps and the E remaining steps. Hence

    boxed: N-D_s=L+b_s(P_N)+E.                                (3)

The empty initial state matters. For an initialized nonempty state,
if D_s counts genuinely new arrivals after that initialization and its
initial prefix target is already recorded, the corresponding formula is
N-D_s=L+b_s(P_N)-b_s(P_0)+E. An uncharged initial state cannot be used
to claim the empty-start version for an ordinary word.

## 4. Consequence at k=17

A complete k17 word has D_9=binom(17,9)=24310. At the exact target
length B(17)=24313, (3) forces

    L+b_9(P_N)+E=3,
    in particular L<=3.                                      (4)

This is an architecture-independent constraint on the literal word's
recency transitions. It does not assume a flat middle-owner schedule,
fixed witness lengths, or a monotone cap construction.

For the user's six-way gadget, the exact state menus are

    P_Y: prefix ranks2,6,9,11,17,
    Q_z: prefix ranks5,9,12,17.

Thus b_9(P_Y)=2 and b_9(Q_z)=1. Every allowed gadget edge
P_Y -> Q_z contributes exactly one unit to L, independently of the
choice of Y,z and independently of whether its rank-nine target is new.

An ordinary word containing all six source-to-destination transitions
of the full six-source class therefore has L>=6. Equation (3) implies

    N>=D_9+6=24316.                                           (5)

In particular, the full six-transition gadget cannot be embedded in a
length24313 full-cube word. Rerouting its destinations does not remove
this cost: each of the six source occurrences remains nonterminal and
still has an outgoing P-to-Q transition.

This strengthens the separate local obstruction in
K17_SIXWAY_RECENCY_PORT_OBSTRUCTION_IN_CURRENT_FLAT_BANK_20260908.md:
here even changing the flat owner chronology does not permit all six
of these transitions in an optimal k17 word.

## 5. Exact scope

The user's abstract biclique and one-path-plus-cycles fusion theorem
remain valid. They preserve a given state inventory and its targets
when the stated routing hypotheses and initialization hold.
Equation (5) says that this particular full six-edge inventory carries
too much downward rank-nine budget for B(17).

Smaller selected subclasses, other port menus, nonoptimal constructions,
and initialization that is honestly charged are not ruled out by (5).
Nor does the identity alone construct a word attaining (4), or prove
that any other proposed connector has the same cost. The all-k exact
equality goal remains open.

# Audit of rectangle and bounded-cycle load augmentation

## Verdict

`RECTANGLE_LOAD_AUGMENTATION.md` passes audit with the following exact
status.

1. The potential identities, rectangle delta law, and pivot-lock criterion
   are mathematical theorems.
2. The displayed `m=3` matching is a strict overloaded rectangle-local
   minimum and its displayed alternating six-cycle repairs it.
3. The displayed `m=4` matching is local under every alternating four- and
   six-cycle and its displayed alternating eight-cycle repairs it.
4. The complete `m=2,3` census is exhaustive and independently
   reproducible.
5. The `m=4,5` trial counts are randomized evidence only.
6. No acyclicity claim is made.

The original rectangle-only proposal is therefore rigorously refuted.  The
same is true of the proposed universal four-or-six replacement.  The
bounded-order-`m` statement is correctly labelled conjectural.

## 1. Audit of the potential identity

Every selected diamond contributes two middle incidences, so

\[
 \sum_Xd(X)=2N.
\]

For every integer `q>=0`,

\[
 \binom q2-q+1=
 \begin{cases}
 1,&q=0,\\
 0,&q=1,2,\\
 \binom{q-1}{2},&q\ge3.
 \end{cases}
\]

Summation proves equation (1.2) of the main note.  In particular, the
baseline `2N-W` is attained exactly by load profiles supported on `{1,2}`.
The warning that this is stronger than maximum degree two is necessary:
degree-zero vertices are legal for the original problem but add one to
`Phi-(2N-W)`.

For a fixed middle set `X`, selected incident diamonds have pairwise
distinct lower colours `X-a`, so there are at most `m`.  This verifies the
pointwise bound `d(X)<=m`.

## 2. Audit of the rectangle calculus

For a rectangle pivoted at `X`, the selected diamonds before the switch are

\[
 (X-a,X+c),\qquad(X-b,X+d),
\]

with `a!=b` and `c!=d`.  Matching injectivity forces these inequalities.
The old secondary vertices

\[
 X-a+c,\quad X-b+d
\]

and new secondary vertices

\[
 X-a+d,\quad X-b+c
\]

are pairwise distinct.  The pivot occurs twice before and after, so it
cancels.  The elementary marginal identities

\[
 \binom{q-1}{2}-\binom q2=-(q-1),\qquad
 \binom{q+1}{2}-\binom q2=q
\]

give

\[
 \Delta\Phi=d(R)+d(T)-d(P)-d(Q)+2.
\]

The weak and strict local inequalities in the main note follow by integer
rearrangement.

Every alternating four-cycle in the lower--upper incidence graph has a
single middle pivot.  Indeed, if its lower vertices are distinct `S_1,S_2`
and upper vertices are distinct `U_1,U_2`, then both lower sets lie in
`U_1 intersect U_2`.  The union of two distinct `(m-1)`-sets has size at
least `m`, while the intersection of two distinct `(m+1)`-sets has size at
most `m`.  Equality is forced, producing the common middle set.

This also proves the pivot-lock lemma.  A rectangle containing `XY` can be
pivoted only at `X` or `Y`.  Pivoting at `X` preserves `d(X)`; pivoting at
`Y` removes the incidence at `X` and is available exactly when `Y` has a
second selected incident edge.

### 2.1 Negative first variation

For the current matching, weighting a diamond `XY` by `d(X)+d(Y)` gives
total weight `sum_X d(X)^2`.  Under the uniform fractional matching, a fixed
middle vertex receives load

\[
 \lambda=m^2/\binom{m+1}{2}=2m/(m+1),
\]

so the linear cost is `lambda sum_X d(X)`.  Since
`sum_X d(X)=W lambda`, their difference is exactly

\[
 \sum_X(d(X)-\lambda)^2>0
\]

for `m>=2`.  Integrality of the bipartite perfect-matching polytope gives a
lower-linear-cost integral matching, and alternating-cycle decomposition of
the symmetric difference gives at least one negative-linear-cost cycle.

For a cycle load change `delta`, direct expansion gives

\[
 \Delta\Phi=\sum_Xd(X)\delta(X)+\tfrac12\sum_X\delta(X)^2,
\]

because total load is preserved.  Hence the main note correctly separates
the proved negative first variation from the unproved ability to pay the
quadratic integrality toll with a cycle of bounded order.

## 3. Audit of the `m=3` strict certificate

The Python certificate fixes the fifteen lower rows and the matching-column
vector

```text
0 1 4 3 6 8 2 13 14 12 9 11 5 7 10
```

in increasing binary-mask layer order.  It checks:

* the columns are a permutation of `0,...,14`;
* every lower--upper containment is legal;
* the load histogram is `1^11 2^8 3^1`;
* `Phi=11` and the unique overload is `145`;
* all legal cross-incidence row pairs are enumerated;
* exactly eleven rectangles exist, with delta histogram
  `1^4 2^5 3^2`.

The last line proves strict rectangle-locality without relying on a search
heuristic.  The three incident neighbours of `145` are `134,125,456`, all
of load one, so the structural pivot-lock diagnosis agrees with the direct
enumeration.

The repair cyclically reassigns the upper columns on rows `12,13,14`.
Direct recomputation gives the four net changes

\[
 123:-1,\qquad145:-1,\qquad125:+1,\qquad134:+1.
\]

Hence `Phi` drops from `11` to `10` and maximum load drops from three to
two.

## 4. Audit of the complete `m=3` census

The C++ recursion fixes the fifteen lower rows in order.  At row `i` it
tries every allowed upper column not already used.  Therefore every leaf is
a perfect matching, every perfect matching has exactly one recursion path,
and no invalid matching is counted.

An independent subset dynamic program gives the same permanent

\[
 3,013,854.
\]

For a fixed matching, every rectangle is one unordered row pair whose two
cross assignments are allowed.  The nested pair loop tests each exactly
once and recomputes the post-switch loads and potential.

For alternating six-cycles, define an arc `a->b` when row `a` may inherit
the upper column currently assigned to row `b`.  Every alternating
six-cycle is a directed simple triangle.  The checker chooses its unique
least row as start and enumerates all orders of the other two rows, so both
orientations are retained and cyclic rotations are removed.  It recomputes
the full new load vector, `Phi`, and maximum load.

The exact output is

```text
total 3013854 local 308724 overloaded-local 99480 strict-overloaded 5160
overloaded-no-improving-3 0 no-3-or-4 0 no-3-4-5 0
```

Thus the finite `m=3` six-cycle assertion is exhaustive.

## 5. Audit of the `m=4` joint trap

The deterministic Python certificate reads the `56`-column vector printed
in the main note and verifies that it is a legal perfect matching.  It then
checks

```text
Phi/max/load histogram: 43 3 {1: 29, 2: 40, 3: 1}
rectangle delta histogram: {0: 6, 1: 22, 2: 10, 3: 5}
directed triangles / minimum delta: 250 0
```

The rectangle enumeration is complete by the argument in Section 4.  The
directed-triangle generator again fixes the unique least row and enumerates
both orientations.  Therefore the matching is genuinely local under every
alternating cycle of lengths four and six; it is not merely the endpoint of
one greedy run.

For the order-four exchange cycle `(0,1,35,26)`, the verifier checks all four
new containments and recomputes the load vector.  The eight nonzero load
changes agree with equation (7.3) of the main note, and the result has

```text
Phi/max/load histogram: 42 2 {1: 28, 2: 42}
```

Thus an alternating eight-cycle directly escapes a state at which all
shorter proposed moves fail.

This does not rule out a path of zero-delta four- or six-cycle moves followed
by a decrease.  The theorem is the precise direct-local statement used in
the note.

## 6. Audit of the randomized bounded-order sampler

`scratch/bounded_cycle_load_sampler.cpp` works as follows.

1. Randomized augmenting paths construct a legal lower--upper perfect
   matching.
2. While the current maximum exceeds two, it takes the first
   `Phi`-decreasing, maximum-nonincreasing rectangle.
3. At rectangle-locality it constructs the matched-row exchange digraph and
   tests directed cycles in increasing order `3,4,...,m`.
4. A cycle is accepted only after exact load deltas show strict `Phi`
   decrease and no increase of the current maximum.
5. The run stops immediately at maximum load two.  Consequently the cycle
   counts exclude irrelevant attempts to optimize `Phi` after the original
   degree target is already solved.

The load-delta implementation maintains a separate touched marker.  This is
important: testing `delta[x]==0` as the marker would double-register a
coordinate whose contributions cancel and later reappear.  The committed
sampler uses the separate marker and was rerun after this audit point was
identified.

Reproduction with seed `20260723` gives

```text
m=4 trials=100000 ... solved=100000 trapped=0 ...
cycle-order-3-steps=134992 cycle-order-4-steps=1623
```

and

```text
m=5 trials=10000 ... solved=10000 trapped=0 ...
cycle-order-3-steps=80971 cycle-order-4-steps=5381
cycle-order-5-steps=120
```

Because the algorithm tests orders increasingly, every recorded order-five
step occurs at a state with maximum greater than two and no accepted move of
orders two, three, or four.  These trial counts are empirical and make no
claim about untested matchings or random seeds.

## 7. Reproduction and hashes

Run:

```bash
python3 scratch/rectangle_load_checker.py --certificate-only
c++ -O3 -std=c++20 scratch/rectangle_load_exhaust_m3.cpp -o /tmp/rect-m3
/tmp/rect-m3
c++ -O3 -std=c++20 scratch/bounded_cycle_load_sampler.cpp -o /tmp/rect-sample
/tmp/rect-sample 4 100000 20260723 4
/tmp/rect-sample 5 10000 20260723 5
```

The exact certificates are lightweight.  The exhaustive `m=3` program is
also small (about three million leaves).  The last two commands are
randomized experiments with a fixed reproducible seed.

SHA-256:

```text
0ed1d1b1c3e8158f924573f6d14da16747fe03b320f78049225835e3373f2543  RECTANGLE_LOAD_AUGMENTATION.md
7453c1750edd8e820c5013786c10e1811ee2fd409c5469ef6449d2871fb32767  scratch/rectangle_load_checker.py
93752834e83435dad1fd237c53343ec4b14bfbbaae30ebb1a3de1709d6bce78e  scratch/rectangle_load_exhaust_m3.cpp
7a9230b45ed8325b3987cde6be8c6c451669e9a02cdec1fcbc6ec25dbab2fdd7  scratch/bounded_cycle_load_sampler.cpp
```

## 8. Final guardrails

The following statements are **not** proved:

* existence of a maximum-degree-two colour-perfect matching for every `m`;
* the bounded-order-`m` augmentation conjecture;
* necessity of order exactly `m` in the sense of excluding neutral shorter
  paths;
* preservation or eventual enforcement of acyclicity.

What is proved is enough to redirect the method: rectangles alone fail,
four plus six fails, and the first surviving formulation must permit cycle
order to grow with dimension.

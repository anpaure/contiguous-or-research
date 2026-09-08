# Gate C: a fixed-order three-rank-disjoint Cayley bank

**Status (2026-08-22).**  Every assertion below is proved.  Fix one perfect
coordinate pairing and one cyclic order of its pairs.  The coherent tours
obtained by varying the initial transversal state contain a subfamily of at
least

\[
 {2^b\over 2b^3+8b^2-16b+1}                           \tag{0.1}
\]

tours whose attached targets are pairwise disjoint simultaneously at ranks
`b-1`, `b`, and `b+1`.  The proof is an explicit Cayley-graph argument:
every cross-tour collision forbids one of only `O(b^3)` XOR differences.

This strengthens the middle-only Hamming-code bank.  It supplies
`2^b/poly(b)` locally compatible whole tours per pairing, so polynomially
enlarging the near-covering pairing menu gives enough aggregate
three-rank capacity.  It does not yet choose banks from different pairings
without cross-pairing collisions, control all offsets, or extend the union
to one full symmetric-chain decomposition.

Throughout, `b>=3` is odd.  Fix a pairing

\[
                         \mathcal P=\{P_s:s\in\mathbb Z_b\}       \tag{0.2}
\]

in the displayed directed cyclic order.  Identify a transversal state
with `x in F_2^b`, where `x_s` chooses one of the two members of `P_s`.
Let `T(x)` be the resulting closed coherent FIFO tour.

## 1. Pair-occupancy signatures

Index the `q=b(b-1)` internal flags by a stage `s in Z_b` and a column
`1<=k<b`.  Write `L_(s,k),M_(s,k),U_(s,k)` for their attached targets at
ranks `b-1,b,b+1`.  Their occupancies in the fixed coordinate pairs are:

\[
\begin{array}{c|c|c|c}
\text{target}&\text{empty pairs}&\text{doubled pairs}&\text{split pairs}\\ \hline
L_{s,k}&P_s&\varnothing&\text{all others}\\
M_{s,k}&P_s&P_{s+k}&\text{all others}\\
U_{s,k},\ k\le b-2&P_s&P_{s+k},P_{s+k+1}&\text{all others}\\
U_{s,b-1}&\varnothing&P_{s-1}&\text{all others}.
\end{array}                                             \tag{1.1}
\]

Indeed one packet omits its special pair `P_s`.  Its lower windows are the
successive transversals of the other `b-1` pairs.  The middle window doubles
the currently entering pair `P_(s+k)`.  Except at the packet boundary, the
upper union also doubles the next entering pair; at the boundary it restores
`P_s` and leaves only `P_(s-1)` doubled.

For a fixed target index `e` and every pair `P_j` which is split in (1.1),
the selected member has the affine form

\[
                         x_j+c_e(j),\qquad c_e(j)\in\mathbb F_2, \tag{1.2}
\]

where `c_e(j)` depends on the fixed order and chronology but not on `x`.
This is because the FIFO process only toggles selected members according to
the stage and column; changing the initial state translates every later
selection coordinatewise by the same vector `x`.

Within one tour the targets are distinct at each of the three ranks.
Middle signatures recover `(s,k)`.  Upper signatures recover `(s,k)`,
including the separate boundary row.  For the lower rank, different stages
have different empty pairs, while within one packet the `b-1` successive
transversals differ whenever the next pair is toggled.

## 2. Polynomial forbidden-difference set

For two states `x,x'`, put `h=x+x'`.  If a target with index `e` in
`T(x)` equals a same-rank target with index `f` in `T(x')`, their occupancy
signatures first have to agree.  On every common split pair, (1.2) then
fixes the corresponding bit of `h` uniquely.  Only bits belonging to the
empty or doubled pairs remain free.

The compatible ordered index pairs and resulting numbers of possible
differences are therefore bounded as follows:

\[
\begin{array}{c|c|c|c}
\text{rank class}&\text{compatible }(e,f)&
 \text{free bits}&\text{candidate differences}\\ \hline
b-1&b(b-1)^2&1&2b(b-1)^2\\
b&b(b-1)&2&4b(b-1)\\
b+1\text{ internal}&b(b-2)&3&8b(b-2)\\
b+1\text{ boundary}&b&1&2b.
\end{array}                                             \tag{2.1}
\]

For the lower rank, compatible targets merely have the same empty pair, so
both column indices are free.  Middle signatures force the same stage and
column.  Two internal upper signatures force the same empty pair and the
same adjacent doubled-pair set, hence the same column.  Boundary upper
targets can agree only with the boundary target having the same doubled
pair.  Internal and boundary upper signatures cannot agree.

Let `B` be the set of all nonzero differences `h` arising from any equality
counted in (2.1), at any of the three ranks.  Taking a union rather than a
multiset gives

\[
 \boxed{|\mathcal B|\le
 2b(b-1)^2+4b(b-1)+8b(b-2)+2b
 =2b^3+8b^2-16b.}                                      \tag{2.2}
\]

### Theorem 2.1 (three-rank Cayley bank)

There is a set `X subseteq F_2^b` of size at least

\[
 \boxed{|X|\ge {2^b\over |\mathcal B|+1}
        \ge {2^b\over2b^3+8b^2-16b+1}}                \tag{2.3}
\]

such that the tours `{T(x):x in X}` are jointly rankwise-target-disjoint at
ranks `b-1`, `b`, and `b+1`.

#### Proof

Form the Cayley graph on `F_2^b` in which distinct states are adjacent when
their difference belongs to `B`.  Its maximum degree is at most `|B|`.
The elementary greedy independent-set algorithm leaves at least
`2^b/(|B|+1)` vertices: each selected vertex deletes itself and at most
`|B|` neighbors.

For distinct `x,x'` in the resulting independent set, their difference is
not in `B`, so Section 2 forbids every cross-tour equality at the three
ranks.  Section 1 supplies within-tour distinctness.  This proves joint
rankwise target disjointness and (2.3). \(\square\)

Each bank therefore contains `q|X|` mutually compatible central flags.
Relative to the fixed-pairing defect-one middle stratum of size
`q2^(b-2)`, its middle coverage fraction is at least

\[
                         {4\over2b^3+8b^2-16b+1}.       \tag{2.4}
\]

The polynomial loss in (2.4) is harmless for the pairing-diversity scale:
the number of perfect pairings is superexponential in `b`, while the
pairing-only near-cover needs only `2^{b+o(b)}` pairings.  What remains is
not local capacity but a dependent selection of these banks whose target
sets stay disjoint across different pairings.

The companion checker
`scratch/verify_gate_c_fixed_order_three_rank_cayley_bank_20260822.py`
constructs every small fixed-order tour, exhausts all cross-state
collisions at the three ranks, verifies the forbidden-difference bound, and
checks the greedy bank directly.

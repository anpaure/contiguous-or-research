# The frozen k=17 socket30 postbank: exact selector, cocycle, and two fixed-interior obstructions

Date: 2026-08-01  
Status: solver-free, scoped theorem and audit.  This note does **not** rule
out further cuts, internal rethreads, hyperarcs, or a generalized lower
compiler, and it does not claim a k=17 word.

## 1. Frozen input

The authoritative v5 bank materializes `6252` resident pieces on all

\[
                         W={17\choose9}=24310
\]

rank-nine owners.  The piece interiors have `18058=W-6252` Johnson edges.
The internal upper holes at ranks 10 through 15 are respectively

\[
                  1458, 2429, 1583, 549, 101, 10.       \tag{1.1}
\]

All assertions below are replayed directly from
`scratch/k17_socket30_postbank_pieces_20260801.json`.

## 2. A lower-colour collision obstruction in the frozen interiors

Let `l(e)=X cap Y` and `u(e)=X union Y` for a Johnson edge `e=XY`.
Among the `18058` internal edges there are only

\[
                 18005
\]

distinct rank-eight lower colours.  Thus the frozen interiors already
contain exactly `53` repeated-colour units; every repeated colour has
multiplicity two.  Consequently `6305` of the `24310` rank-eight colours
are absent internally.

### Theorem 2.1 (fixed-interior lower bound)

Any Hamilton path obtained only by orienting and concatenating the `6252`
frozen pieces has at least `54` missing lower-q1 transition colours.
Equivalently, it has at least `53` lower holes beyond the unavoidable one
path-boundary hole.

#### Proof

A Hamilton concatenation adds exactly `6251` seams.  Even if their lower
colours are mutually distinct and avoid all `18005` colours already used,
the final path has at most

\[
                     18005+6251=24256
\]

distinct lower colours.  Hence at least `24310-24256=54` are absent.
Equality is equivalent to avoiding every further lower collision.  \(\square\)

This is not a universal-word obstruction.  A generalized compiler can pay
the extra `53` targets with special cells, or an internal rethread can remove
some of the `53` collisions.  It is, however, an exact obstruction to a
lower-rainbow completion of the **fixed** postbank interiors.

## 3. Seven raw rank-ten endpoint zeros

For a rank-ten target `U`, let its ten rank-nine facets be `U-{q}`.  Give
every frozen piece both possible orientations and ignore all residence and
common-cap restrictions.  Thus this is a maximally permissive endpoint
screen.

### Lemma 3.1 (rank-ten seam reduction)

If an interval crossing a piece seam has union exactly `U`, then the two
owners adjacent to that seam are two distinct facets of `U`.

#### Proof

Both adjacent rank-nine owners lie in `U`.  Since they are distinct, their
union has rank at least ten, and hence equals `U`.  \(\square\)

The exact endpoint screen has seven zero rows:

\[
  20427, 69555, 70910, 72414, 72566, 73649, 83946.     \tag{3.1}
\]

Each has exactly one currently exposed facet, respectively

\[
  18379, 67507, 70878, 6878, 7030, 72625, 82922.       \tag{3.2}
\]

In particular, no orientation or ordering of the fixed `6252` pieces can
cover all rank-ten targets.  The bank child `69555` is one of these seven
rows.  Its previously catalogued provider therefore necessarily uses a
further release/cut; it is not an edge of the frozen endpoint graph.
The exact old/new deck ledger classifies **all seven** rows as `NEWLY_LOST`.
Thus the named extraction-child list is not the complete global casualty
list: correlated completion must screen every changed internal interval,
not only the 81 named extraction boundaries.

Only the pair `69555,73649` shares a rank-nine facet, namely `69553`.
Therefore a cut-only repair needs at least six distinct newly exposed owner
endpoints.  Since one cut exposes at most two new endpoints, it needs at
least three additional cuts.  This is only a lower bound; orientation,
residence, lower-colour, and cap constraints may demand more.

## 4. Exact lower-repeat/upper-repeat endpoint cocycle

Suppose some refinement of the bank has been joined into a Johnson
Hamilton path.  Let

* `H` be the set of missing rank-eight lower colours;
* `L` be the multiset of lower occurrences beyond the first occurrence of
  each nonmissing lower colour;
* `R` be the multiset of rank-ten upper occurrences beyond the first copy
  of every upper colour; and
* `T^-`, `T^+` be the endpoint owners.

Assume the upper rank-ten palette is complete.  Then

\[
              |H|=|L|+1,qquad |R|=4861.              \tag{4.1}
\]

Writing `d_A(q)` for coordinate degree in a multiset `A`, one has exactly

\[
 \boxed{
 d_R(q)=2860+d_H(q)-d_L(q)
       -\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}.}     \tag{4.2}
\]

#### Proof

For every Johnson edge `XY`,

\[
             \mathbf1_X+\mathbf1_Y
              =\mathbf1_{X\cap Y}+\mathbf1_{X\cup Y}. \tag{4.3}
\]

Summing over the path and looking at coordinate `q` gives

\[
 2{16\choose8}-\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}
 =\bigl({16\choose7}-d_H(q)+d_L(q)\bigr)
  +\bigl({16\choose9}+d_R(q)\bigr).                  \tag{4.4}
\]

Since

\[
 2{16\choose8}-{16\choose7}-{16\choose9}=2860,
\]

this is (4.2).  Edge counts give (4.1).  \(\square\)

For a lower-rainbow path, `L` is empty and `H` is a singleton, recovering
the usual connector cocycle.  The v5 frozen interiors force the more
general ledger: any terminal compiler must either carry at least `53`
additional lower holes or first alter the interiors.

For the frozen bank, the internal upper palette has `17990` distinct
colours and repeat excess `68`.  Hence an upper-exact completion by `6251`
seams would use exactly

\[
              1458\quad\hbox{first-cover seams},qquad
              4793\quad\hbox{repeat seams}.           \tag{4.5}
\]

The total upper repeat multiset would have size `68+4793=4861`, as required
by (4.1).

## 5. Exact global selector after releases

The correct finite object is not a bipartite child matching.  Let every
piece have its admissible oriented boundary states, and let `E` be the
literal seam catalogue after any declared additional releases.  A seam
records simultaneously

\[
  (\hbox{tail state},\hbox{head state},l(e),u(e),
    \hbox{residence transition},\hbox{cap transition}). \tag{5.1}
\]

Binary state variables `y_(i,s)` and seam variables `x_e` must satisfy

1. one state per piece;
2. indegree and outdegree at most one in the chosen states;
3. `sum_e x_e=N-1` and all directed graphic/subtour inequalities;
4. every missing rank-ten colour is used by at least one seam;
5. the lower-hole/repeat ledger and the chosen special compiler cells obey
   (4.1)--(4.2); and
6. all protected bank-child provider rows, including the released provider
   for `69555`, use distinct physical endpoint capacities.

The child rows are a three-partite matching problem: a selected provider
uses one colour, one tail slot, and one head slot.  Bipartite Hall on colours
versus seams is therefore only necessary, not sufficient.  The path graphic
row and repeat cocycle further couple those choices.

## 6. Ranks 11--15 are exact reachability commodities, not edge colours

Fix a target `S` of rank 11 through 15.  On the selected owner path form the
accumulated-union automaton with states

\[
                         (v,A),qquad v\subseteq A\subseteq S,       \tag{6.1}
\]

where `v` is the current rank-nine owner.  A selected owner transition
`v->w`, with `w subseteq S`, induces

\[
                         (v,A)\longrightarrow(w,A\cup w).          \tag{6.2}
\]

A source may enter at `(v,v)` and an accepting state has `A=S`.

### Theorem 6.1 (all-width upper-flow criterion)

For fixed selector variables, `S` is represented by a consecutive owner
interval iff the automaton (6.1)--(6.2) admits one unit of source-to-acceptor
flow.  Capacitating seam transitions by `x_e` and internal transitions by
their orientation-state variable gives an exact linear extended
formulation.

#### Proof

A directed automaton path reads consecutive owners in the selected Hamilton
path, remains inside `S`, and stores their exact accumulated union.  Reaching
`A=S` therefore gives the desired interval.  Conversely, any witnessing
interval traces such an automaton path.  Unit network flow decomposes into
directed paths, so fractional flow introduces no false witness once the
selector variables are fixed.  \(\square\)

This formulation retains arbitrary interval width.  Replacing it by a fixed
`q`-edge witness for a rank-`(9+q)` target is not valid.  The commodities for
different targets have no mutual capacity and may share seams; their only
coupling is through the common Hamilton selector.

Thus the complete postbank problem has a precise division:

* rank ten: coloured seam selection plus the child/repeat cocycle;
* ranks 11--15: accumulated-union reachability over that same selected path;
* lower ideal: the separate generalized compiler, with at least `53`
  additional q1 services if the interiors remain fixed.

The seven raw zeros in (3.1) show that the current `6252`-piece ledger is
not yet the domain of this selector.  At least a small certified release
layer must be installed first.

## 7. Audit artifact

`scratch/audit_threadD_k17_socket30_postbank_selector_20260801.py` performs
the solver-free replay and writes
`scratch/threadD_k17_socket30_postbank_selector_20260801.audit.json`, with
status

`PASS_EXACT_POSTBANK_Q1_COCYCLE_AND_COLLISION_OBSTRUCTION`.

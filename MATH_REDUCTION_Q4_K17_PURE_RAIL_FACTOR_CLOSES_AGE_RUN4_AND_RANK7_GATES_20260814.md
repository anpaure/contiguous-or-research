# A q4 pure-rail factor closes the two frozen k17 age-host obstructions

**Date:** 2026-08-14
**Status:** exact symbolic bridge.  Every period-10 or period-11 q4 rail
has the required exact length-four coordinate run at every owner position,
and its lower-q2 deck is literally the frozen age compiler's rank-seven
deck.  The remaining core-refresh path is a three-class automaton on only
five labels.  Existence of the global typed quotient factor and of the
final coloured cyclic path is not asserted.

## 0. Outcome

The frozen one-copy k17 age reduction has two owner-host obstructions:

1. each of its 436 positions with singleton age zero requires
   `beta_(j-1)=alpha_(j+3)`, equivalently an exact coordinate run of four
   owners; and
2. its 1,144 rank-seven suffix slots require all rank-seven translation
   orbits among the intersections of three consecutive owners.

Both conditions are native rows of a q4 pure rail.  For

\[
 O_i=C\cup\{s_i,s_{i+1},s_{i+2},s_{i+3}\},          \tag{0.1}
\]

one has identically

\[
       \beta_{j-1}=\alpha_{j+3}=s_{j+3},             \tag{0.2}
\]

and

\[
 O_i\cap O_{i+1}\cap O_{i+2}
      =C\cup\{s_{i+2},s_{i+3}\}.                    \tag{0.3}
\]

Consequently a mixed period-10/11 `Z_17` quotient factor satisfying the
owner rows and the lower-q2 support rows of
`MATH_REDUCTION_Q4_K17_Z17_TRANSLATION_QUOTIENT_TYPED_FACTOR_GATE_20260814.md`
has `1,430` quotient run-four starts in distinct run-start orbits and at
least one position over every one of the `1,144` rank-seven target orbits.
Choosing one such position per rank-seven orbit removes the two
ordering-independent supply cuts which killed the canonical MMM host.
The chosen rank-seven positions must still be coupled to the certified type
word and core-refresh path.

This is not yet an optimal word.  It replaces the obstructed MMM owner
cycle by an exact finite typed-factor-and-age-path master.

## 1. Every position is an exact run-four start

Let the rail period be `N in {10,11}` and read indices modulo `N`.  The
edge

\[
                         O_i\longrightarrow O_{i+1} \tag{1.1}
\]

deletes and inserts

\[
                         \alpha_i=s_i,
              \qquad     \beta_i=s_{i+4}.            \tag{1.2}
\]

At owner position `j`, the coordinate inserted on the preceding edge is
`beta_(j-1)=s_(j+3)`.  It belongs successively to

\[
                         O_j,O_{j+1},O_{j+2},O_{j+3} \tag{1.3}
\]

and is deleted on edge `j+3`, because `alpha_(j+3)=s_(j+3)`.  Since
`N>=10>4`, it is absent on both sides of `(1.3)`.  Thus `(1.3)` is one
maximal positive run of length exactly four and `(0.2)` holds at every
position, including cyclic wrap positions.

### Corollary 1.1 (the age supply cut is automatic)

If `a` period-ten and `b` period-eleven quotient columns cover the owner
orbits, then

\[
                         10a+11b=1430.               \tag{1.4}
\]

Every one of these 1,430 quotient owner positions is a run-four start.
Hence any placement of the 436 certified singleton-age-zero type
occurrences passes the former run-four cardinality cut.  After translation
development there is one exact run-four start at every one of the 24,310
physical owners.

These are also `1,430` distinct quotient run-start orbits.  Indeed a run
start records its first owner together with its active coordinate.  If two
run starts were translation-equivalent, their first owners would be
translation-equivalent.  Quotient simplicity within each selected column
and the exact owner rows across columns forbid that.  Thus selecting 436
positions supplies 436 distinct required run-start orbits, not merely 436
position occurrences.

The conclusion concerns the disjoint pure rails before a later component
fusion.  A fusion which cuts one of the four relevant edges must transport
the corresponding age history or replace its witness.

## 2. The rank-seven row is exactly lower q2

Direct intersection of three consecutive rows of `(0.1)` gives `(0.3)`.
This is the `L_i^(3)` row of the typed quotient reduction.  Therefore:

### Theorem 2.1

Suppose a selected quotient pure-rail family satisfies

\[
  \sum_Q\#\{i:[L_i^{(3)}]=A\}\,x_Q\ge1             \tag{2.1}
\]

for every rank-seven translation orbit `A`.  Its development contains
every literal rank-seven set as a three-owner intersection.  If the loads
are constrained to `{1,2}`, their forced quotient histogram is

\[
                         858\times1,qquad286\times2. \tag{2.2}
\]

#### Proof

The action of `Z_17` is free on rank-seven sets.  One quotient occurrence
in `(2.1)` develops to all seventeen members of its orbit.  Equation
`(0.3)` identifies these occurrences literally with the age compiler's
rank-seven suffix values.  There are 1,430 occurrences and 1,144 target
orbits, so `{1,2}` loads force `(2.2)`.  \(\square\)

Thus the rank-seven deficiency `1001<1144` of the frozen shift-one MMM
cycle is not structural at k17.  It is removed by the same lower-q2 rows
already demanded by typed rail coinstantiation.

### Corollary 2.2 (the age-slot selector is explicit)

Under `(2.1)`, choose one quotient position `i(A)` satisfying
`[L_i^(3)]=A` for every rank-seven orbit `A`.  Freeness makes these `1,144`
positions develop to one literal occurrence of every rank-seven set.  The
positions `i(A)` are pairwise distinct, because one position has only one
`L_i^(3)` value.

Therefore the finite age master must assign the `1,144` certified
rank-seven types exactly to the selected positions `i(A)`.  Lower-q2
coverage proves that this selector exists; it does **not** by itself prove
that the resulting prescribed type positions admit a cyclic core-refresh
path.  That compatibility remains in the coloured automaton.

## 3. Natural active-label ages and the five-label core automaton

At owner `O_i`, the four active labels have forced ages

\[
 \{s_{i+3}\},\quad\{s_{i+2}\},\quad
 \{s_{i+1}\},\quad\{s_i\}                          \tag{3.1}
\]

from zero through three.  Let

\[
                         C=K_0\mathbin{\dot\cup}K_1
                              \mathbin{\dot\cup}K_2 \tag{3.2}
\]

be the refresh-age partition of the five permanent core labels.  Then the
complete owner age partition is

\[
 P_i=\bigl(K_0+s_{i+3},\ K_1+s_{i+2},\
           K_2+s_{i+1},\ \{s_i\}\bigr).             \tag{3.3}
\]

If its certified type is `c=(c_0,c_1,c_2,1)`, the core class sizes are

\[
                         k_j=c_j-1,qquad
                         k_0+k_1+k_2=5.              \tag{3.4}
\]

For the nine frozen types, the core profiles and numbers of labelled core
states are

\[
\begin{array}{c|c|c}
(c_0,c_1,c_2,1)&(k_0,k_1,k_2)&5!/(k_0!k_1!k_2!)\\ \hline
(1,5,2,1)&(0,4,1)&5\\
(1,6,1,1)&(0,5,0)&1\\
(2,5,1,1)&(1,4,0)&5\\
(3,3,2,1)&(2,2,1)&30\\
(3,4,1,1)&(2,3,0)&10\\
(4,3,1,1)&(3,2,0)&10\\
(5,1,2,1)&(4,0,1)&5\\
(5,2,1,1)&(4,1,0)&5\\
(6,1,1,1)&(5,0,0)&1.
                                                               \tag{3.5}
\end{array}
\]

This replaces the general owner-layer menu of size at most 560 by a menu
of size at most 30 on a pure rail.

### Theorem 3.1 (exact core-refresh transition)

Let `K=(K_0,K_1,K_2)` be the core state at one position and let the next
type have core sizes `(k'_0,k'_1,k'_2)`.  A successor core state exists if
and only if

\[
                         k'_1\le k_0,
              \qquad     k'_2\le k_1.               \tag{3.6}
\]

For a fixed labelled state `K`, its exact number of successors of that
type is

\[
                         {k_0\choose k'_1}
                         {k_1\choose k'_2}.          \tag{3.7}
\]

#### Proof

A core coordinate of age zero or one may either advance one age or be
refreshed to age zero.  Every age-two core coordinate must be refreshed,
because the unique age-three label on the next owner is the active label
`s_(i+1)`.  Hence choose

\[
                         K'_1\subseteq K_0,
              \qquad     K'_2\subseteq K_1          \tag{3.8}
\]

with the prescribed sizes and put

\[
                         K'_0=C-(K'_1\cup K'_2).     \tag{3.9}
\]

This is possible exactly under `(3.6)` and gives `(3.7)`.  Conversely,
the literal survivor rule forces the containments `(3.8)`, so there are no
other successors.  \(\square\)

The frozen type-transition inequality `c'_(j+1)<=c_j` is exactly `(3.6)`
after subtracting the one forced active label from each of the first three
age classes.  Thus every legal frozen type arc has a nonempty pure-core
transition menu.

## 4. The resulting exact finite master

A direct k17 pure-rail age host can now be expressed without the obstructed
MMM cycle:

1. select period-10/11 quotient columns covering every owner orbit exactly;
2. cover every lower-q1 orbit exactly and every lower-q2 orbit at least
   once;
3. select one lower-q2 occurrence for each rank-seven orbit, assign the
   1,144 certified rank-seven types exactly to those positions, and assign
   the remaining 286 certified types to the remaining positions;
4. on each selected rail, choose a cyclic path in the at-most-30-state core
   automaton of Theorem 3.1; and
5. enforce orbit-distinct suffix payloads at ranks two through six.

Items 1--2 close owner, lower-q1, run-four, and rank-seven host supply in
one object.  Items 3--5 are a finite coloured path/transversal problem.
The immediate-upper and lower-q2 capacity rows from the typed quotient
theorem can be imposed in the same column master.

What still remains after a solution is found:

* resource-safe fusion of the initially disjoint rail cycles while
  transporting every protected four-step age history;
* complete proper-upper support across the fusion seams;
* the three endpoint/common-cap cells of the optimal length-24,313 word;
  and
* independent literal replay of the resulting word.

The bridge proved here is exact but scoped: it removes both known
ordering-independent owner-host obstructions and replaces the former
183,232-state MMM layer system by a much smaller core-refresh automaton on
the candidate pure rails.

## 5. H100 replay

The independent verifier checks every owner edge and cyclic wrap on literal
period-10 and period-11 rails, the exact four-owner run, the lower-q2
identity, all nine certified type/core profiles, all labelled five-core
states, and every ordered type pair against the successor formula `(3.7)`.
It also replays the certified demands `436` and `1,144`.

```text
scratch/verify_q4_k17_pure_rail_age_run4_rank7_bridge_20260814.py
SHA-256 27dc138f2744043e4368306d008f5824821e062795338db502133acc73122b10

H100 output
scratch/verify_q4_k17_pure_rail_age_run4_rank7_bridge_20260814.h100.out
SHA-256 f4768658b462278f5a87bb2ea9166097d990153416faa70e6d434a7d54dca3ce
```

Exact output:

```text
PASS q4_pure_age_bridge periods=10,11 run4=all_positions marked_orbit_projection=12870_to_1430 rank7=L3 certified_demands=436+1144 core_states_max=30 legal_type_pairs=42
```

All execution and hashing ran through SSH on H100.  The local Mac was used
only for reading, editing, transfer, and Git.

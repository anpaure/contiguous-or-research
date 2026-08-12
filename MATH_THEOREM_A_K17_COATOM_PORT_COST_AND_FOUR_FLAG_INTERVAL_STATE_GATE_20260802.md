# K17 overlap ports: sharp coatom cost and the four-flag interval-state gate

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact local normal forms and an exact finite state-expanded
selector for the long-row subsystem.  The suffix-native face is ruled out
on the frozen K17 table.  A subsequent complete `6/9/4` nested-address
projection, including short rows, rules out the entire one-transition
nested contiguous-address class; see
`MATH_THEOREM_A_K17_NESTED_CONTIGUOUS_INTERVAL_PROJECTION_NOGO_AND_FLAG_DRIFT_20260802.md`.
No residence, upper-shadow, common-cap, source, or compiler claim is made.

## 0. Outcome

Fix a long K17 row

\[
             L\subset M\subset U\subset T,
 \qquad (|M|,|U|,|T|)=(7,8,9),                       \tag{0.1}
\]

and put

\[
 K=M\setminus L,\qquad \{p\}=U\setminus M,
 \qquad \{z\}=T\setminus U.                         \tag{0.2}
\]

There are two separate conclusions.

1. On the native suffix face, every reduced long-to-long predecessor is a
   coatom split indexed by `x in L` and `Y subseteq L-{x}`.  It duplicates
   exactly `|L|-1` coordinate occurrences in the head state.  This cost is
   sharp and independent of `Y`.
2. If the frozen chain only has to occur as a nested pair of contiguous
   intervals in the three-cell state, there are exactly four address flags.
   Their complete arbitrary-overlap families are explicit below.  The
   resulting 16 flag-pair transition predicate gives an exact finite
   state-expanded cycle-cover model.

The first conclusion agrees with, and sharpens locally, the independently
audited coatom normal form in
`MATH_THEOREM_A_K17_ARBITRARY_OVERLAP_COATOM_NORMAL_FORM_AND_FIXED_TABLE_HALL_NOGO_20260802.md`.
That audit proves that the complete suffix-native overlap face still has
K17 Hall deficiency at least `10,832`.  The later `6/9/4` audit proves that
the three non-suffix long flags together with every short-row nested flag
still leave projection deficiency `484`.  Hence a nonnested address, a
genuinely larger macro, or a changed static table is necessary on this
fixed-table face.

## 1. Native suffix states

A suffix-native state for (0.1) is a triple of nonempty letters

\[
                         h=(A,B,C)                    \tag{1.1}
\]

satisfying

\[
                         C=L,\qquad B\cup C=M,
 \qquad A\cup B\cup C=U.                             \tag{1.2}
\]

### Lemma 1.1 (complete suffix-overlap family)

The complete solution of (1.2) is

\[
 \boxed{
  C=L,\qquad B=K\cup Y,\qquad A=\{p\}\cup Z,
  \quad Y\subseteq L,\ Z\subseteq M.}               \tag{1.3}
\]

Its overlap cost

\[
             \omega(h)=|A|+|B|+|C|-|U|               \tag{1.4}
\]

is exactly `|Y|+|Z|`.

#### Proof

The middle equality in (1.2) is equivalent to
`K subseteq B subseteq M`, hence `B=K union Y` with `Y subseteq L`.
Since `B union C=M`, the last equality is equivalent to
`{p} subseteq A subseteq U`, hence `A={p} union Z` with `Z subseteq M`.
The three disjoint increments `p,K,L` partition `U`; (1.4) follows.  \(\square\)

## 2. Sharp reduced coatom ports

Let row `i` be (0.1), and let row `j` also be long.  A literal transition
`j -> i` has

\[
              h_j=(D,A,B),\qquad h_i=(A,B,L),         \tag{2.1}
\]

and its owner is `T` exactly when

\[
                              D\cup U=T.              \tag{2.2}
\]

### Theorem 2.1 (coatom port and all redundancy)

Such a suffix-native transition exists if and only if there are

\[
                         x\in L,qquad
                         Y\subseteq L\setminus\{x\}  \tag{2.3}
\]

for which row `j` has frozen chain

\[
 \boxed{
 L_j=K\cup Y,\qquad M_j=U\setminus\{x\},\qquad
 U_j=(U\setminus\{x\})\cup\{z\}.}                  \tag{2.4}
\]

Put

\[
 A_0=\{p\}\cup\bigl(L\setminus(Y\cup\{x\})\bigr),
 \qquad B=K\cup Y.                                  \tag{2.5}
\]

The reduced root/socket pair is

\[
 \boxed{
 r_i(x,Y)=(A_0,B,L),\qquad
 c_i(x,Y)=(\{z\},A_0,B).}                            \tag{2.6}
\]

The socket `c_i(x,Y)` is precisely the disjoint-increment state of row `j`,
and the bridge `c_i(x,Y) -> r_i(x,Y)` carries owner `T` and the three named
targets of row `i`.

Every nonreduced witness is obtained from (2.6) by

\[
                  A=A_0\cup E,\quad E\subseteq B,
 \qquad D=\{z\}\cup F,\quad F\subseteq U\setminus\{x\}.       \tag{2.7}
\]

Conversely every choice in (2.7) is a witness for the same two frozen rows.

#### Proof

The shift and the two suffix payload equations give

\[
 B=L_j,\qquad A\cup B=M_j,qquad B\cup L=M,
 \qquad M_j\cup L=U.                                \tag{2.8}
\]

Because `M_j` is a coatom of `U`, the last equality gives
`M_j=U-{x}` for a unique `x in L`.  Then
`B=K union Y` for a unique `Y subseteq L-{x}`.  The owner equation forces
`z in D subseteq T`; the rank-eight equation `D union M_j=U_j` forbids
`x in D` and gives the last identity in (2.4).

Now `A union B=U-{x}`.  The part outside `B` is exactly `A_0`, while the
only redundant choices are elements of `B`, proving the first half of
(2.7).  Likewise `D` must contain `z` and every other permissible member
already lies in `M_j=U-{x}`, proving the second half.  Direct union verifies
the converse.  \(\square\)

### Corollary 2.2 (sharp enrichment cost)

Every suffix-native long-to-long transition into row `i` has head-state
overlap cost at least

\[
                              \boxed{|L|-1}.          \tag{2.9}
\]

The reduced port (2.6) attains equality, independently of `Y`.  More
precisely, (2.7) has head-state cost `|L|-1+|E|`.

#### Proof

The state `r_i` already contains `L` in its third letter.  Equations
(2.4)--(2.8) force every member of `L-{x}` to occur once more in exactly
one of the first two letters.  Thus at least `|L|-1` incidences are
duplicated.  In (2.5), `Y` and `L-(Y union {x})` partition `L-{x}`, so the
bound is attained.  The only additional head duplication in (2.7) is `E`.
\(\square\)

For the factor-critical conveyor, (2.6) is the exact direct port type.  A
module path which omits row `i` exposes root `r_i`; an upstream module must
expose the identical socket `c_i`, and the bridge `c_i -> r_i` has boundary

\[
                         {\bf1}_{r_i}-{\bf1}_{c_i}.    \tag{2.10}
\]

The K17 coatom audit shows that these direct ports do not have enough Hall
supply: their maximum matching into the hard long heads is `2,167`; even
granting all `5,647` short rows as universal suppliers leaves deficiency
`10,832`.  Grouping only these same direct edges into modules cannot evade
that cut.

## 3. The complete four interval flags

We now keep the same frozen named sets `L subset M subset U` but require
only that they be realized by nested contiguous intervals of the three-cell
state:

* `U` is the union of all three cells;
* `M` is the union of either positions `12` or positions `23`; and
* `L` is one of the two singleton endpoints of that chosen length-two
  interval.

These choices give four flags, denoted `12/1`, `12/2`, `23/2`, `23/3`.

### Theorem 3.1 (four-flag normal form)

For `Y subseteq L` and `Z subseteq M`, the complete state families are

\[
\begin{array}{c|c}
\text{flag}&(A,B,C)\\ \hline
12/1&(L,\ K\cup Y,\ \{p\}\cup Z),\\
12/2&(K\cup Y,\ L,\ \{p\}\cup Z),\\
23/2&(\{p\}\cup Z,\ L,\ K\cup Y),\\
23/3&(\{p\}\cup Z,\ K\cup Y,\ L).
\end{array}                                           \tag{3.1}
\]

Every listed state has overlap cost

\[
                              \omega=|Y|+|Z|.         \tag{3.2}
\]

The four families are exhaustive and pairwise disjoint.

#### Proof

The length-two witness must be one of the only two length-two intervals,
`AB` or `BC`; the singleton witness must be one of its endpoints.  This
gives the four rows.  On its two positions, exactly the proof of Lemma 1.1
gives the letters `L` and `K union Y`.  The remaining cell must contain
`p` and may contain an arbitrary `Z subseteq M`.  Conversely every row in
(3.1) has the declared nested unions.  Formula (3.2) follows from the
disjoint partition `U={p} dotunion K dotunion L`.

The four families cannot intersect: exchanging the two positions inside a
length-two interval would require `L=K union Y`, impossible because the
nonempty set `K` is disjoint from `L`; exchanging the outer cell with an
inner cell would require a set contained in `M` to contain `p`.  \(\square\)

## 4. Exact 16-pair transition predicate

For frozen row `i`, let `H_i^alpha` be the family in row `alpha` of
(3.1), and put `H_i=union_alpha H_i^alpha`.  The following predicate is
the complete one-transition gate; it is deliberately left in literal-set
form, so there is no false projection to independent tail and head menus.

### Theorem 4.1 (oriented interval compatibility)

For flags `alpha,beta`, a state of row `j` in flag `alpha` can precede a
state of row `i` in flag `beta`, while preserving the frozen owner `T_i`,
if and only if there exist

\[
       g=(g_1,g_2,g_3)\in H_j^\alpha,qquad
       h=(h_1,h_2,h_3)\in H_i^\beta                  \tag{4.1}
\]

such that

\[
 \boxed{g_2=h_1,\qquad g_3=h_2,\qquad g_1\cup U_i=T_i.}         \tag{4.2}
\]

When (4.2) holds, the literal trace `(g_1,h_1,h_2,h_3)` shifts from `g`
to `h`, has owner exactly `T_i`, and carries all three named targets of
row `i` at its declared flag.  Conversely every such transition satisfies
(4.2).

#### Proof

The first two equalities are exactly equality of the two overlapping source
cells in a depth-three de Bruijn shift.  Since the union of `h` is `U_i`,
the four-cell owner is `g_1 union U_i`, giving the third equality.  Theorem
3.1 supplies the named interval witnesses.  Every literal predecessor shift
has these same identities, proving necessity.  \(\square\)

Thus all 16 ordered flag pairs are decided by the same three exact set
equalities.  No separate marginal Hall relaxation is valid.

### Corollary 4.2 (exact state-expanded selector)

Build a directed graph whose vertices are the occurrence-labelled states
`(i,h)`, `h in H_i`, for the frozen **long-row subsystem**, and whose arcs
are exactly (4.2).  There is a balanced one-transition realization of that
long-row subsystem on this four-flag face if and only if binary variables
`y_(i,h)` and
`x_(j,g;i,h)` satisfy

\[
\begin{aligned}
 \sum_{h\in H_i}y_{i,h}&=1 &&(i\text{ a frozen long row}),\\
 \sum_{j,g}x_{j,g;i,h}&=y_{i,h} &&((i,h)\text{ a state}),\\
 \sum_{i,h}x_{j,g;i,h}&=y_{j,g} &&((j,g)\text{ a state}),
\end{aligned}                                         \tag{4.3}
\]

where variables `x` exist only for compatible arcs.  A connected Euler
realization is exactly a solution whose selected directed support is one
cycle.  Factor-critical modules are directed paths in this same expanded
graph with one selected root state and one selected socket state exposed.

#### Proof

The first row chooses one complete state for each frozen long row.  The next two
rows give that chosen state exactly one predecessor and one successor.
Theorem 4.1 makes each selected incoming arc carry the fixed owner and named
payload of its head row.  Conversely any balanced realization selects these
variables.  Component cycles are the Euler components.  Short rows require
their own interval-state families and are not asserted to lie in this
four-flag graph.  \(\square\)

## 5. Exact scope and next finite question

The flag `23/3` is precisely the suffix-native face.  Its complete
arbitrary-overlap catalogue is already closed on the frozen K17 table by
the independently verified deficiency `10,832`.

The other three flags are the weakest local long-row escape which

* keeps one physical transition per frozen row;
* keeps the attached owner and every named chain target; and
* changes only the interval address of those named targets.

Even after adding all six and nine nested flags for short rows, their union
projection is deficient by `484`; thus they do not solve the frozen table.
They also do **not** preserve the native suffix depth, a fixed lower-compiler
address, clipped residence histories, arbitrary-width upper witnesses, or a
common source cap.  Those rows may delete states and arcs from (4.3), but
they are not included here.  No K17 solution or all-dimension density
statement for the four-flag graph is claimed.

The later union projection already fails, so (4.3) cannot hold after the
short rows are included.  The smallest remaining fixed-table escape is a
nonnested address or a genuinely multi-transition or multi-row macro: one
which realizes at least one frozen payload away from a single three-cell
nested interval chain.  Merely adding more coordinate repetitions to the
suffix-native letters cannot help.

## 6. Lightweight audit

The script

```text
scratch/a_k17_four_flag_interval_gate_20260802/
  audit_a_k17_four_flag_interval_gate_20260802.py
```

exhausts all nonempty three-letter words for representative flags through
ground-set size five, verifies the four-family partition, checks the overlap
cost formula, and checks the reduced coatom identities through rank eight.

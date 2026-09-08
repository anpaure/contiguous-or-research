# An exact central-chronology compiler theorem

Date: 2026-07-27

## 1. Purpose

The new `k=11` optimum reveals a useful exact separation.  The upper half of
the Boolean lattice is determined entirely by one central row.  The lower
half is a coordinatewise interval-hitting problem followed by one ordinary
Hall matching.  This note packages those statements into a single sufficient
theorem for an optimal contiguous-OR word.

Nothing in the theorem is probabilistic.  It applies in every dimension and
at every delay.  Its hypotheses are not yet proved to hold uniformly; that
is precisely the remaining construction problem.

## 2. OR--Pascal notation

For a set word

\[
A=(A_0,\ldots,A_{L-1})
\]

put

\[
(DA)_i=A_i\cup A_{i+1},
\qquad
(D^sA)_i=\bigcup_{h=0}^{s}A_{i+h}.
\]

Fix

\[
r=\lceil k/2\rceil,
\qquad
W=\binom kr,
\]

and a positive integer `d`.  A proposed central chronology is a word

\[
T=(T_0,\ldots,T_{W-1}),
\qquad |T_i|=r.
\]

The maximal delay-`d` envelope has length `W+d` and is

\[
E_p=
\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i
\qquad(0\le p<W+d).
\tag{2.1}
\]

A **pin** is a triple `(s,j,L)` asking for the exact cell

\[
(D^sA)_j=L.
\]

The pin occupies the physical interval `[j,j+s]`.

## 3. Allowed positions and a hitting core

Let `P` be a collection of pins, and include all central pins

\[
\mathcal C=\{(d,i,T_i):0\le i<W\}.
\]

For every coordinate `x`, delete every physical position forbidden by a
negative pin:

\[
Q_x=[0,W+d-1]\setminus
\bigcup_{(s,j,L)\in\mathcal P\cup\mathcal C:\ x\notin L}[j,j+s].
\tag{3.1}
\]

Equivalently define the pruned envelope

\[
U_p=\{x:p\in Q_x\}.
\tag{3.2}
\]

Assume every positive demand is feasible:

\[
x\in L
\quad\Longrightarrow\quad
[j,j+s]\cap Q_x\ne\varnothing.
\tag{3.3}
\]

Choose, independently for each coordinate, a set of allowed hitting
positions meeting every interval in which that coordinate is positively
required.  Their union gives a **hitting core**

\[
C_p\subseteq U_p
\tag{3.4}
\]

such that every positive pin interval contains the required coordinate in
some `C_p`.  Such a core always exists under (3.3), for example by taking
every allowed occurrence.  A sparse core is advantageous for the later Hall
graph, but the theorem does not assume that a particular greedy rule is
optimal; any explicitly verified hitting core is valid.

## 4. Compiler theorem

### Theorem 4.1

Suppose the following hold.

1. **Central permutation.**  The sets `T_i` are exactly the `W` distinct
   members of `binom([k],r)`.

2. **Pin feasibility.**  Condition (3.3) holds, and every `U_p` is nonempty.

3. **Intermediate coverage.**  For every rank

   \[
   r-d<s<r,
   \]

   every `s`-set occurs as the label of at least one pin in `P`.

4. **Low-target Hall condition.**  Let

   \[
   \mathcal L=\{S\subseteq[k]:1\le |S|\le r-d\}.
   \]

   Form the bipartite graph between `L` and the `W+d` physical positions by

   \[
   S\sim p
   \quad\Longleftrightarrow\quad
   C_p\subseteq S\subseteq U_p.
   \tag{4.1}
   \]

   This graph has a matching saturating `L`.

5. **Upper coverage.**  For every `q>=1` with `r+q<=k`, the cells of
   `D^qT` contain every member of `binom([k],r+q)`.

Then there is a nonzero word `A` of length `W+d` whose contiguous unions
contain every nonempty subset of `[k]`.  In particular,

\[
\nu(k)\le W+d.
\]

If `d=d(k)` is the least integer satisfying the monotone-deadline lower-bound
inequality

\[
dW+\binom{d+1}{2}
\ge
\sum_{j=1}^{r-1}\binom kj,
\tag{4.2}
\]

then

\[
\boxed{\nu(k)=B(k)=W+d(k)}.
\]

### Proof

Let `M` be a matching saturating `L`.  Start with `A_p=U_p`.  If the matched
edge for target `S` is `S--p`, replace `A_p` by `S`.  Distinct targets use
distinct positions, and all assigned targets are nonempty.  Unmatched entries
remain nonempty by hypothesis 2.

Every negative coordinate of every pin is absent throughout its interval,
because `A_p` is always a subset of `U_p`.  Every positive coordinate of
every pin still occurs in its interval: the hitting core supplied such an
occurrence, and (4.1) guarantees that replacing `U_p` by a matched target
never deletes `C_p`.  Hence every pin in `P` and every central pin in `C` is
realized exactly.

The matched singleton cells realize all ranks at most `r-d`.  Hypothesis 3
realizes all remaining ranks below `r`.  The central pins give

\[
D^dA=T,
\]

so the whole middle layer occurs.  Finally

\[
D^{d+q}A=D^qT,
\]

and hypothesis 5 supplies every upper layer.  Thus every nonempty mask is a
contiguous union of `A`.

The monotone-deadline theorem gives the reverse inequality
`nu(k)>=W+d(k)`, proving the final assertion.  \(\square\)

### Exactness of the sandwich condition

For the literal-low-target architecture, hypothesis 4 is not merely a
convenient sufficient condition.  Suppose a word realizes the chosen central
and intermediate pins and contains every member of `L` literally.  Take

\[
C_p=A_p.
\]

The pin equalities say that this is a pin-compatible hitting core, and every
literal target can be assigned to one physical position where it occurs.
Distinct target values use distinct positions, giving a matching in (4.1).
Hence:

> A pinned literal compiler exists if and only if some pin-compatible core
> has a sandwich graph saturating the low targets (together with the nonzero
> entry condition).

We call this exact property **PCSH** (pin-compatible sandwich Hall).

## 5. How residence enters

The theorem is stated using exact central pins, but their feasibility has a
simple chronology criterion.  A factor `D^dA=T` exists if and only if every
internal coordinate run in `T` has length at least `d+1`; in that case the
maximal envelope (2.1) itself satisfies

\[
D^dE=T.
\]

Moreover, for `1<=q<=d`,

\[
(D^{d-q}E)_{i+q}
=
\bigcap_{h=0}^{q}T_{i+h}.
\tag{5.1}
\]

Thus a residence-safe chronology with complete lower shadows automatically
provides every desired intermediate label in its maximal tableau.  What is
not automatic is that a jointly chosen set of those labels survives pruning
and leaves a saturating Hall graph.  Theorem 4.1 identifies exactly that last
finite gate.

An ordinary Hall matching between all lower targets and arbitrary short
intervals is weaker than PCSH: it does not record the shared coordinate pins.
Likewise, a minimum-mass hitting core need not be the Hall-best core.  This is
already visible in the stored `k=7` and `k=12` optima, where a different core
or one split coordinate witness repairs the matching.  Therefore a proof may
optimize the core; it must not canonize one greedy core without justification.

For a cyclic chronology one cuts an edge, uses a nested endpoint flag to
restore the lower shadow cells lost at the seam, and requires the deleted
upper windows to have other witnesses.  The endpoint-flag residence criterion
in `MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md` is exact.

## 6. The k=11 witness

For the exact certificate:

\[
k=11,
\quad r=6,
\quad W=462,
\quad d=3.
\]

The voltage-two quotient lift is a cyclic central permutation with zero
residence defects and complete lower and upper shadows at every depth.  It
has 242 upper-safe cuts.  For cut 1, the endpoint flag is

\[
155\supset154\supset152.
\]

After the intermediate rank-four and rank-five pins are fixed, the residual
low family has

\[
\sum_{j=1}^{3}\binom{11}{j}=231
\]

members, and the graph (4.1) has a 231/231 matching.  The compiled word is
`scratch/sigma_sat_k11_465.word`; an exhaustive scan finds all 2047 nonempty
masks.  Hence Theorem 4.1 gives

\[
\nu(11)=465.
\]

Cap two is useful for the central design but is not a logical compiler
hypothesis.  Three independently generated complete-shadow, residence-safe
`k=11` cycles—including one with upper load three—compile on every one of
their 660 safe cuts.  This is strong finite evidence for a shadow/residence
to-PCSH implication, but no such implication is proved.  A nearby model
missing eleven lower depth-three targets passes the coarser short-interval
Hall test while its tested canonical pinned core fails PCSH, showing why the
pin layer cannot simply be dropped.

## 7. Remaining general problem

The exact conjecture is now reduced, within this normal form, to two uniform
statements:

1. construct a central chronology satisfying residence and all upper-shadow
   coverage; and
2. choose intermediate witnesses so that (3.3) and Hall's inequalities for
   (4.1) hold.

The `k=11` certificate proves that these requirements are compatible at the
first odd delay-three case.  It does not show that either follows from the
other, nor that the same symmetric chronology exists in every dimension.

## 8. First-derivative collapse and exact surplus Hall

The selected-pin theorem above is completely general, but the cyclic erosion
normal form admits a sharper compiler.

Let `P=(P_0,...,P_{W+d-1})` be the linearized cyclic erosion word, including
the `d` appended boundary entries, and suppose every `P_j` has the same rank

\[
s=r-d.
\]

Choose a coordinatewise core `C subseteq P` satisfying

\[
DC=DP.
\tag{8.1}
\]

Such a core is explicit.  For each coordinate and each run of ones in its
binary occurrence word in `P`, the two run endpoints are forced by the two
boundary edges; select the initial endpoint, alternating interior positions,
and the terminal endpoint.  This covers every adjacent edge on which `DP`
contains the coordinate.  The construction commutes with translation of a
cyclic rotor.

### Lemma 8.1 (first derivative controls the tower)

If

\[
C_j\subseteq A_j\subseteq P_j
\qquad\text{for every }j,
\]

then

\[
DA=DP,
\qquad
D^tA=D^tP\quad(t\ge1).
\tag{8.2}
\]

#### Proof

Monotonicity gives

\[
DC\subseteq DA\subseteq DP.
\]

The outer terms are equal by (8.1), proving `DA=DP`.  Apply further
derivatives to this equality.  \(\square\)

Thus every intermediate, central, and upper witness in `P` survives without
choosing individual pins.  Only the masks of ranks at most `s` must be placed
literally in `A`.

For each `s`-set `Q`, put

\[
R_Q=\{j:P_j=Q\},
\qquad
\mu(Q)=|R_Q|.
\]

Complete depth-`d` lower shadows say `mu(Q)>=1`.  One position in every
`R_Q` must be reserved for the literal target `Q`.  Let

\[
\mathcal L_{<s}=\{S:1\le |S|<s\},
\]

and join `S` to position `j` when

\[
C_j\subseteq S\subseteq P_j.
\tag{8.3}
\]

For `A subseteq L_{<s}`, let `N(A)` be its position neighbourhood.

### Theorem 8.2 (exact surplus Hall criterion)

There is a word `A` with

\[
C\subseteq A\subseteq P
\]

that contains every nonempty set of rank at most `s` literally if and only
if, for every `A subseteq L_{<s}`,

\[
|\mathcal A|
\le
\sum_{Q\in\binom{[k]}s}
\min\bigl\{\mu(Q)-1,\ |N(\mathcal A)\cap R_Q|\bigr\}.
\tag{8.4}
\]

#### Proof

On the right positions use the partition matroid whose block `R_Q` has
capacity `mu(Q)-1`.  Its rank on a set of positions `X` is

\[
\sum_Q\min\{\mu(Q)-1,|X\cap R_Q|\}.
\]

Rado's matroidal Hall theorem says that the lower targets have an independent
transversal exactly when (8.4) holds.  Such a transversal uses at most
`mu(Q)-1` positions of every block, leaving a distinct position for the
literal rank-`s` target `Q`.  Conversely, any literal placement of all
targets gives this independent transversal after the rank-`s` positions are
removed.  \(\square\)

Combining Lemma 8.1 and Theorem 8.2 with upper-safe cutting gives a stronger
version of Theorem 4.1 requiring no selected intermediate pins.

The rank function on the right of (8.4) is submodular.  Therefore the
invariant-witness uncrossing lemma in
`MATH_SYMMETRIC_HALL_UNCROSSING_20260727.md` applies: for a cyclic
translation-equivariant bulk compiler, any failure has an orbit-union
witness.  At `k=11,s=3`, the strict-low family has only six translation
orbits (one singleton orbit and five pair orbits), so only 63 nonempty
quotient inequalities remain.  For three independent complete-shadow
cycles their minimum margins are respectively 2, 4, and 3.

The boundary cannot be ignored.  A complete-shadow residence-safe `k=7`
cycle has four exterior-safe cuts failing exact linear PCSH and 24 passing;
its cyclic bulk compiler itself fails.  A bounded census of 120 further
complete cycles found at least 15 good cuts in every case, but this is finite
evidence, not a proof that some good cut always exists.

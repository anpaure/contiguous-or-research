# The centered-square diagonal obstruction and the even equivariant `(c,t)` escape

Date: 2026-07-29

Status: proved structural theorems and solver-free finite audits.  No `k=16`
word or compiler certificate is claimed.

## 0. Exact outcome

There are two different statements which must not be conflated.

1. The 73-diagonal obstruction is not PBBS-specific, but neither is it a
   consequence of complementarity alone.  It holds for every **centered
   Johnson factor** obtained from a Kneser/odd-graph 2-factor.  In full
   generality its component incidence is a perfect matching; it is literally
   diagonal when the parent Kneser cycles are odd.  The rank-seven PBBS
   successor on `[15]` has 73 odd cycles, so its complementary primitive
   square catalogue splits into exactly 73 invariant blocks.

2. The even equivariant `(c,t)` normal form is the normal form of a general
   unit-voltage `Z_15`-equivariant child cycle, not of a square-only packet.
   Its `t`-seams are arbitrary rank-seven/rank-eight containment rungs.  No
   equation pairs an entry rung with an exit rung into one centered square.
   Thus the unrestricted `(c,t)` model is capable of evading the diagonal
   obstruction.  It does not by itself prove that the orbit transversals,
   residence, all shadows and `COMP_3` can be satisfied simultaneously.

The corrected finite counts are:

* complementary centered PBBS: `12,870` primitive squares, not `6,435`, and
  exactly 73 diagonal component pairs;
* unrelated audited A factor with cycle lengths `6390,45` against centered
  PBBS B: `7,485` primitive squares and a component-incidence graph with
  exactly three connected components of node sizes `72,2,1`;
* its individually strict-palette-safe subcatalogue: `1,650` squares and 29
  component-incidence components.

All counts in this note use an undirected B edge in both possible endpoint
roles.  This is the convention in the square definition below and explains
the factor two in the corrected PBBS count.

## 1. Primitive dual-rail squares

Let `U` have size `2r+1`.  Write `bar(S)=U\S`.  The projected B rail has
vertices in `binom(U,r)` and the A rail has vertices in `binom(U,r+1)`.
The actual child B vertex is `{z} union R`, but `z` is suppressed in this
section.

Take an A edge `{X_0,X_1}` and a B edge `{R_0,R_1}`.  They form an oriented
primitive square when

\[
 R_0=X_0\cap X_1,
 \qquad
 X_0=R_0\cup R_1.
\tag{1.1}
\]

The switch deletes the two rail edges and inserts the containment rungs

\[
 X_1--(\{z\}\cup R_0),
 \qquad
 X_0--(\{z\}\cup R_1).
\tag{1.2}
\]

The exact q1 signature of one square is

\[
 \Delta^-=[R_1]-[\{z\}\cup(R_0\cap R_1)],
\tag{1.3}
\]

\[
 \Delta^+=[\{z\}\cup X_1]-[X_0\cup X_1].
\tag{1.4}
\]

Indeed, the removed A-lower colour `R_0` is restored by the first rung, and
the removed B-upper colour `{z} union X_0` is restored by the second rung.
The only depleted palettes are therefore B-lower and A-upper.

For a fixed pair of rail factors, define the **primitive-square component
incidence graph** `H_square` as follows.  Its vertices are the A and B rail
cycles, and an A-cycle is adjacent to a B-cycle when at least one primitive
square uses an edge from each.  Every graph obtained by simultaneously
toggling a packet drawn from this fixed catalogue stays inside the connected
components of `H_square`.  Hence, if `H_square` has `kappa` connected
components, every such switched factor has at least `kappa` components.

This last assertion is independent of palettes and residence: each deleted
edge and each inserted rung of a primitive square has both ends in the same
component block of `H_square`.

## 2. The centered-complement matching theorem

Let `F` be a simple spanning 2-factor of `KG(2r+1,r)`, and orient every
cycle.  Let `f` be the resulting successor permutation on
`Omega=binom(U,r)`, so

\[
 X\cap fX=\varnothing
 \qquad(X\in\Omega).
\tag{2.1}
\]

Its centered Johnson projection is

\[
 E(B_f)=\bigl\{e_X:=\{f^{-1}X,fX\}:X\in\Omega\bigr\}.
\tag{2.2}
\]

Let `A_f` be its vertexwise complement:

\[
 E(A_f)=\bigl\{a_X:=
 \{\overline{f^{-1}X},\overline{fX}\}:X\in\Omega\bigr\}.
\tag{2.3}
\]

### Theorem 2.1 (centered primitive squares form a component matching)

The following statements hold.

1. The components of `B_f` are exactly the `f^2`-orbits `Q`.

2. For every center `X`, the A edge `a_X` belongs to exactly two primitive
   squares.  Their B edges are

   \[
   \{X,f^2X\},
   \qquad
   \{X,f^{-2}X\}.
   \tag{2.4}
   \]

3. If `Q` is the `f^2`-orbit of `X`, both squares in (2.4) join the same
   component pair

   \[
   B_Q\longleftrightarrow A_{fQ},
   \tag{2.5}
   \]

   where `A_Q` denotes the complement of the B component on `Q`.
   Consequently `H_square` is the graph of the bijection

   \[
   Q\longmapsto fQ
   \tag{2.6}
   \]

   on the `f^2`-orbits.  In particular it is a perfect matching.

4. Every primitive-square packet preserves every block

   \[
   B_Q\cup A_{fQ}.
   \tag{2.7}
   \]

   It therefore leaves at least

   \[
   \#\{f^2\text{-orbits}\}
   =\sum_{C\text{ an }f\text{-cycle}}\gcd(2,|C|)
   \tag{2.8}
   \]

   child components.

5. If every `f`-cycle is odd, then `fQ=Q`; with complement-aligned labels,
   the component matching is literally diagonal.  An even `f`-cycle has two
   parity `f^2`-orbits which are exchanged by `f`.  This makes the matching
   off-diagonal within that one parent cycle, but still cannot connect it to
   any other parent cycle.

### Proof

The two sets `f^{-1}X` and `fX` are distinct `r`-subsets of the
`(r+1)`-set `bar(X)`.  Hence

\[
 f^{-1}X\cup fX=\bar X
 \quad\text{and}\quad
 \overline{f^{-1}X}\cap\overline{fX}=X.
\tag{2.9}
\]

The centered edges incident with `X` are precisely

\[
 e_{fX}=\{X,f^2X\},
 \qquad
 e_{f^{-1}X}=\{f^{-2}X,X\}.
\tag{2.10}
\]

They are distinct.  More generally a centered Johnson edge has the unique
Kneser center equal to the complement of the union of its endpoints, so
`e_X=e_Y` implies `X=Y`.  Thus (2.2) is a simple 2-factor, not a multiset.

Thus the centered factor moves by `f^{+2}` and `f^{-2}`, proving statement
1 and showing that (2.10) lists every possible B edge whose endpoint can be
the required `R_0=X`.

Both `X` and `f^2X` are distinct `r`-sets disjoint from `fX`.  They are
therefore the two different `r`-subsets of the `(r+1)`-set `bar(fX)`, and

\[
 X\cup f^2X=\overline{fX}.
\tag{2.11}
\]

Similarly,

\[
 X\cup f^{-2}X=\overline{f^{-1}X}.
\tag{2.12}
\]

Equations (2.9), (2.11) and (2.12) are exactly (1.1), one for each
orientation of the A edge `a_X`.  Conversely, every primitive square using
`a_X` must have `R_0=X` by (2.9), and its B edge must then be one of the two
edges in (2.10).  This proves statement 2.

If `X in Q`, the two B partners lie in `B_Q`.  The endpoints `f^{-1}X` and
`fX` of the centered edge underneath `a_X` both lie in the `f^2`-orbit
`fQ`; hence `a_X` lies in `A_{fQ}`.  This proves (2.5).  The map `Q -> fQ`
is a bijection (indeed an involution on the set of `f^2`-orbits), proving
statement 3.  Every deleted rail edge and both new rungs remain inside the
block (2.7), proving statements 4 and 5.  `square`

### Corollary 2.2 (exact PBBS specialization)

For the retained PBBS successor on the rank-seven subsets of `[15]`, the
`f`-cycle histogram is

\[
 15^5,\quad45^9,\quad75^{21},\quad105^{26},\quad135^{11},\quad165^1.
\tag{2.13}
\]

All lengths are odd and the number of cycles is

\[
 5+9+21+26+11+1=73.
\tag{2.14}
\]

There are exactly two primitive squares per center, hence

\[
 2\binom{15}{7}=2\cdot6435=12870
\tag{2.15}
\]

primitive squares.  The multiplicity of the component pair belonging to an
`f`-cycle of length `ell` is `2ell`, so the pair-load histogram is

\[
 30^5,\quad90^9,\quad150^{21},\quad210^{26},\quad270^{11},\quad330^1.
\tag{2.16}
\]

The 146 initial A/B cycles can therefore be fused by primitive squares to
at best 73 cycles, never fewer.  This is true even if every palette and
residence condition is discarded.

Within this diagonal catalogue, 4,050 squares are individually
strict-palette-safe.  They occur on 44 of the 73 diagonal component pairs;
the other 29 B components have no such square.  The resulting strict-safe
incidence graph has 102 connected components: 44 two-node pairs and 58
isolated rail components.  These figures concern individual load tests;
the joint packet capacities are stated in (4.5).

The count `6,435` previously written in Section 7 of
`MATH_K16_DUAL_RESIDENT_COMPLEMENT_BRAID_MASTER_20260729.md` counted only
one B partner per A edge.  Under definition (1.1), an undirected B edge can
use either endpoint as `R_0`, and Theorem 2.1 gives two partners for every A
edge.  The corrected count is (2.15).

## 3. Complementarity alone does not imply diagonality

The centered hypothesis in Theorem 2.1 is essential, even if all four q1
palettes are complete.

Take `r=2`, `U=[5]`, and the following 2-factor of `J(5,2)`, writing `ij`
for `{i,j}`:

\[
 C_0=(12,13,34,45,14),
 \qquad
 C_1=(15,25,24,23,35).
\tag{3.1}
\]

Let B be this factor and let A be its vertexwise complement.  The five
singleton B-intersection colours each occur twice, while the ten triple
B-union colours occur once each.  By complementation, the ten A-intersection
colours occur once each and the five A-union colours each occur twice.
Thus the example has complete q1 palettes on both rails.

Its primitive square catalogue has 12 squares.  Every square has depleted
load pair `(2,2)`, so every one is individually strict-palette-safe.  All
four component pairs occur:

\[
 (A_0,B_0),\ (A_0,B_1),\ (A_1,B_0),\ (A_1,B_1).
\tag{3.2}
\]

For example,

\[
 245--125\in A_0,
 \qquad
 25--24\in B_1
\]

form a primitive square with `(R_0,X_0,R_1)=(25,245,24)`, and

\[
 234--134\in A_1,
 \qquad
 13--34\in B_0
\]

form one with `(R_0,X_0,R_1)=(34,134,13)`.  Hence `H_square=K_{2,2}` is
connected.  This gives a literal counterexample to every formulation which
deduces the diagonal obstruction from `A=bar(B)` alone.

## 4. Exact unrelated A-two-cycle by PBBS-B catalogue

The unrelated A factor is the independently replayed rank-eight factor with
cycle lengths

\[
 6390,\quad45.
\tag{4.1}
\]

The B factor is the 73-component centered PBBS rank-seven factor from
(2.13).  The complete undirected primitive-square census is:

\[
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{primitive squares}&7485\\
\text{distinct participating A edges}&6225\\
\text{distinct participating B edges}&6225\\
\text{component pairs}&72\\
\text{B components reached}&72/73.
\end{array}
\tag{4.2}
\]

With the retained component labels, the exact incidence is:

* `A_0` reaches every B component except `B_0` and `B_51`;
* `A_1` reaches only `B_51`;
* `B_0` is isolated.

Consequently the full component-incidence graph has exactly three connected
components,

\[
 \{A_0,B_1,\ldots,B_{50},B_{52},\ldots,B_{72}\},
 \qquad
 \{A_1,B_{51}\},
 \qquad
 \{B_0\},
\tag{4.3}
\]

whose node sizes are `72,2,1`.  No packet assembled solely from this fixed
primitive catalogue can produce fewer than three child components, even
before palettes, residence or the compiler are imposed.

### 4.1 Individually strict-palette-safe subcatalogue

Call one square **individually strict-safe** when its depleted B-lower and
A-upper colours both have initial load at least two.  There are

\[
 1650
\tag{4.4}
\]

such squares, occupying 46 component pairs and reaching 46 B components.
The B components with no individually strict-safe square are

```text
0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,20,23,24,25,26,27,28,31,39,52.
```

The strict-safe component graph has 29 connected components: one block of
node size 46 containing `A_0`, the pair `{A_1,B_51}`, and 27 isolated B
components.

This adjective is deliberately pointwise.  A simultaneous packet can spend
the same duplicated colour several times.  If `n_C` selected squares delete
the B-lower colour `C` and `n_U` delete the A-upper colour `U`, strict packet
safety is the joint system

\[
 n_C\le \mu_B^-(C)-1,
 \qquad
 n_U\le \mu_A^+(U)-1.
\tag{4.5}
\]

Thus (4.4) is a catalogue count, not a packet certificate.

Across all 105 coordinate transpositions of this A factor, the largest
number of PBBS B components reached by the individually strict-safe
subcatalogue is 53.  Exactly 30 transpositions attain 53.  This closes that
transposition atlas only; it says nothing about arbitrary permutations or a
traded factor.

## 5. The even equivariant `(c,t)` normal form

Set

\[
 n=15,\qquad N=858,\qquad L=nN=12870,
\tag{5.1}
\]

and let `rho` rotate the old coordinate set `Z_15` by one while fixing the
new coordinate `z`.  Let

\[
 t\in\{0,1\}^{N},
 \qquad
 c\in\{0,1\}^{L}.
\tag{5.2}
\]

Physical indices of `c` are reduced modulo `L`, and indices of `t` modulo
`N`.  Define the old part of the physical middle state at time `i` by

\[
 M_i=\{x\in\mathbb Z_{15}:c_{i-xN}=1\},
\tag{5.3}
\]

and define the child state

\[
 T_i=M_i\cup
 \begin{cases}
 \{z\},&t_{i\bmod N}=1,\\
 \varnothing,&t_{i\bmod N}=0.
 \end{cases}
\tag{5.4}
\]

Then

\[
 T_{i+N}=\rho T_i.
\tag{5.5}
\]

Conversely, every unit-voltage sequence satisfying
`T_(i+N)=rho(T_i)` has this form uniquely.  Set

\[
 t_j=\mathbf 1_{\{z\in T_j\}},
 \qquad
 c_a=\mathbf 1_{\{0\in T_a\}}.
\tag{5.5a}
\]

The `z` indicator is `N`-periodic because `rho` fixes `z`, and equivariance
gives

\[
 x\in T_i
 \quad\Longleftrightarrow\quad
 0\in T_{i-xN}
 \quad\Longleftrightarrow\quad
 c_{i-xN}=1.
\tag{5.5b}
\]

Thus `(c,t)` is a genuine normal form, rather than merely a construction.

For a quotient class `j`, put

\[
 h_j=|M_j|=\sum_{x\in\mathbb Z_{15}}c_{j-xN}.
\tag{5.6}
\]

The rank-eight equations are exactly

\[
 \boxed{h_j=8-t_j\qquad(j\in\mathbb Z_N).}
\tag{5.7}
\]

In particular, if `t` has 429 ones, it also has 429 zeros and (5.7) forces

\[
 |c|=8N-|t|=6864-429=6435.
\tag{5.8}
\]

### Theorem 5.1 (exact modified start/end law)

For the quotient seam `j -> j+1`, choose the integer representative
`j in {0,...,N-1}`.  In the c-subscripts below, retain the integer `j+1`;
in particular, at the last quotient seam use `j+1=N`, so that
`M_N=rho(M_0)`.  Only after forming the c-subscript is it reduced modulo
`L`; the corresponding t-subscript is reduced modulo `N`.  Define the
numbers of old-coordinate arrivals and departures by

\[
 S_j=\sum_x(1-c_{j-xN})c_{j+1-xN},
\tag{5.9}
\]

\[
 E_j=\sum_xc_{j-xN}(1-c_{j+1-xN}).
\tag{5.10}
\]

Assume (5.7).  Every physical seam above `j -> j+1` is a Johnson edge if
and only if

\[
 \boxed{
 S_j=1-(1-t_j)t_{j+1},
 \qquad
 E_j=1-t_j(1-t_{j+1}).}
\tag{5.11}
\]

Equivalently,

\[
\begin{array}{c|cccc}
(t_j,t_{j+1})&00&01&10&11\\ \hline
(S_j,E_j)&(1,1)&(0,1)&(1,0)&(1,1).
\end{array}
\tag{5.12}
\]

Moreover, (5.11) makes every `h_j+t_j` equal.  Hence (5.7) may equivalently
be replaced by (5.11) and the single total-mass equation

\[
 |c|+|t|=8N.
\tag{5.13}
\]

### Proof

For a fixed old coordinate `x`, membership in `M_j` is
`c_(j-xN)`.  Thus (5.9) counts exactly the old coordinates entering at the
seam, and (5.10) counts exactly those leaving.  The new coordinate enters
precisely on a `01` seam and leaves precisely on a `10` seam.  Since both
states have rank eight, the seam is Johnson exactly when its total number of
arrivals and total number of departures are both one:

\[
 S_j+(1-t_j)t_{j+1}=1,
 \qquad
 E_j+t_j(1-t_{j+1})=1.
\tag{5.14}
\]

This is (5.11), and the four cases give (5.12).  Finally,

\[
 h_{j+1}-h_j=S_j-E_j=t_j-t_{j+1},
\tag{5.15}
\]

so `h_j+t_j` is constant.  Averaging and using (5.13) makes the constant
eight.  `square`

### Theorem 5.2 (middle-ownership criterion)

Subject to (5.7) and (5.11), the physical sequence `T_0,...,T_(L-1)` is a
unit-voltage `Z_15`-equivariant Hamilton cycle of `J(16,8)` if and only if:

1. `t` has exactly 429 zeros and 429 ones;
2. the `M_j` with `t_j=0` form a transversal of the 429 rotation orbits of
   `binom([15],8)`;
3. the `M_j` with `t_j=1` form a transversal of the 429 rotation orbits of
   `binom([15],7)`.

### Proof

The action of `Z_15` on rank-seven and rank-eight subsets is free.  Indeed,
a set fixed by a nonidentity rotation is a union of rotation cycles of
length divisible by 3, 5 or 15, whereas neither 7 nor 8 has such a divisor.
Thus both ranks have `6435/15=429` orbits.  Equation (5.5) expands each
chosen quotient representative into its full 15-state orbit.  Conditions
1--3 are therefore necessary and sufficient for the expanded sequence to
contain all `2*6435` child middle states exactly once.  Theorem 5.1 supplies
all Johnson seams, including the helical seam from quotient class `N-1` to
the rotated copy of class zero.  `square`

### 5.3 Exact edge-type and residence consequences

Let `s` be the number of cyclic one-runs of `t`.  Since `t` has equally many
zeros and ones,

\[
 \#00=\#11=429-s,
 \qquad
 \#01=\#10=s.
\tag{5.16}
\]

After the 15-fold voltage lift, the physical cycle therefore has

\[
 15(429-s)\text{ AA edges},
 \quad
 15(429-s)\text{ BB edges},
 \quad
 30s\text{ cross rungs}.
\tag{5.17}
\]

The cyclic word `c` has exactly `858-s` starts and the same number of ends.
Every old coordinate trace is a cyclic translate of `c`, while the `z`
trace is the 15-fold repetition of `t`.  Consequently depth-three
residence is exactly the requirement that every positive run of both `c`
and `t` have length at least four.  If dual residence is also required, the
same condition must hold for their zero-runs.

The four q1 edge types are explicit:

\[
\begin{array}{c|c|c}
t_jt_{j+1}&T_j\cap T_{j+1}&T_j\cup T_{j+1}\\ \hline
00&M_j\cap M_{j+1}&M_j\cup M_{j+1}\\
11&\{z\}\cup(M_j\cap M_{j+1})&
   \{z\}\cup(M_j\cup M_{j+1})\\
01&M_{j+1}&\{z\}\cup M_j\\
10&M_j&\{z\}\cup M_{j+1}.
\end{array}
\tag{5.18}
\]

The containments in the last two rows follow from (5.12).

There are 335 rotation orbits of rank-six subsets of `[15]`: 333 have
length 15 and two have length 5.  Indeed, the only short possibilities are
the ten sets invariant under shift five, obtained by choosing two of its
five 3-cycles; these form two full-rotation orbits of length five, while the
remaining `5005-10=4995` sets form 333 orbits of length 15.  By
complementation the same is true at rank nine.  The no-`z` upper rank-nine
palette is supplied only by AA
edges, and the `z`-lower rank-six palette only by BB edges.  Since each has
`429-s` quotient edge orbits, complete q1 coverage has the exact necessary
condition

\[
 \boxed{s\le 429-335=94.}
\tag{5.19}
\]

The unrestricted containment graph has

\[
 \frac{8\binom{15}{8}}{15}=3432
\tag{5.20}
\]

quotient rung orbits.  Equation (5.19), not a shortage of general rungs,
is the first scalar seam-count restriction.

## 6. Why `(c,t)` is not subject to the 73-diagonal theorem

On a `01` seam, (5.12) gives one old departure and no old arrival, so

\[
 M_{j+1}\subset M_j,
 \qquad |M_j|=8,quad |M_{j+1}|=7.
\tag{6.1}
\]

On a `10` seam the reverse containment holds.  Thus every `t`-seam is a
general incidence rung between ranks seven and eight.  Conversely, every
local containment `R subset P` with `|R|=7,|P|=8` realizes the corresponding
cross seam as an isolated local transition.  Realizing many prescribed
seams simultaneously still requires one globally consistent shared word
`c`.

Nothing in (5.7) or (5.11) pairs a `01` rung with a `10` rung, and nothing
imposes the extra primitive-square equations

\[
 R_0=X_0\cap X_1,
 \qquad
 X_0=R_0\cup R_1
\tag{6.2}
\]

relative to two fixed rail edges.  The same-shore edges in `(c,t)` are also
chosen globally by `c`; they need not be edges of the retained centered
PBBS factor or its complement.

This distinction has an exact halfport formulation.  Write two physical
cross seams as containment rungs `(A,B)` and `(A',B')`, with A-side sets
first.  They are the two output rungs of one primitive square if and only
if, after possibly swapping the two rungs,

\[
 \boxed{B=A\cap A',\qquad A'=B\cup B'.}
\tag{6.3}
\]

For sufficiency set `(X_1,R_0,X_0,R_1)=(A,B,A',B')`; (6.3) becomes exactly
(6.2).  Necessity is the same substitution in reverse.  Therefore a
square-only `(c,t)` chronology would need a perfect matching of all its
cross-seam halfports satisfying (6.3), with the reconstructed AA and BB
edges simple and, for the fixed-PBBS specialization, actually present in
the prescribed factors.  The `(c,t)` equations impose no such matching.

Therefore:

* the unrestricted `(c,t)` model is an exact parameterization of general
  equivariant incidence-rung braids and does not inherit the 73 PBBS blocks;
* a `(c,t)` state additionally constrained to keep the fixed centered rails
  and to use only primitive-square toggles still obeys Theorem 2.1 and cannot
  be Hamiltonian;
* a future Hamilton `(c,t)` solution must, relative to the centered PBBS
  pair, use at least one non-square incidence rung or rethread at least one
  same-shore edge.  A nonlocal alternating circuit may do both.

This is an escape from one obstruction class, not an existence theorem.
The shared binary word `c`, the two orbit transversals, residence, all q1
palettes, deeper upper coverage and the exact compiler remain coupled.

## 7. Packet conditions and the proved boundary

For clarity, even a connected primitive-square catalogue is not yet a
packet theorem.

1. **Degree and simplicity.**  A clean packet uses every deleted A edge,
   deleted B edge and inserted rung at most once.  More generally the exact
   condition is equality, at every rail vertex, of deleted and added
   incidence in the resulting simple edge sets.

2. **Joint palette capacities.**  Equation (4.5) is required jointly.  The
   depth-three compiler may allow at most two missing lower q1 colours:

   \[
   n_C+o_C\le\mu_B^-(C)-1+q_C,
   \qquad
   \sum_Cq_C\le2,
   \tag{7.1}
   \]

   where `q_C in {0,1}` and `o_C` records whether the eventual opening edge
   deletes an occurrence of the same B-lower colour.  The corresponding
   no-hole upper ledger is

   \[
   n_U+o_U\le\mu_A^+(U)-1.
   \tag{7.2}
   \]

   Here `o_U` is the analogous opening indicator.  These rows are followed
   by exact endpoint and `COMP_3` feasibility.  There is no
   analogous allowance for an upper q1 hole.  Any interval whose union has
   rank nine contains an adjacent pair with that same union, so every upper
   q1 target must remain in the adjacent-union palette.

3. **Topology.**  If the selected square multigraph on initial rail cycles
   is a spanning tree and all used edges/rungs are disjoint, successive
   leaf splicing proves that the output is one cycle.  Mere connectedness
   with extra square edges is not sufficient: port monodromy can leave more
   than one cycle.

4. **Residence.**  Residence must be checked on the decoded final cycle or
   with genuinely cut-aware, noninteracting collars.  Isolated per-square
   collar tests need not compose.

5. **Opening and compiler.**  Opening the final cycle deletes one more
   transition occurrence.  Its upper colour must survive elsewhere.  The
   lower loss belongs to the same at-most-two compiler budget.  The exact
   singleton gate is a `COMP_3` solution with some source letter equal to
   `{z}`.  A four-state B run is a strong staged candidate channel, but it
   is neither necessary nor sufficient for the simultaneous `COMP_3`
   system.

6. **Deeper shadows.**  Q1-safe fusion proves nothing about arbitrary-width
   upper coverage or simultaneous lower compilation.  Both require final
   replay, followed by the literal word verifier.

The exact no-go hierarchy proved here is therefore:

* fixed centered complementary PBBS plus primitive squares: at least 73
  components;
* fixed unrelated A-two-cycle plus centered PBBS B plus primitive squares:
  at least three components;
* unrestricted `(c,t)` equivariant braid: neither component obstruction
  applies, but feasibility is unproved.

## 8. Reproduction and evidence

The solver-free replay is

```text
python3 scratch/audit_k16_dual_rail_square_and_cut_obstructions_20260729.py
```

It verifies the primitive-square identities, both fixed catalogues, their
component graphs, the complete 105-transposition atlas, and the small
non-centered complementary counterexample.  Current SHA-256 hashes are:

```text
f29439826dc674fd43bfb664a36d848176560d764cf43dee8a3965f4206bd8bc
  scratch/audit_k16_dual_rail_square_and_cut_obstructions_20260729.py
84f98e1291a3df6c6cab5924e83a965d411c6fe91f1c3c348a81e580dfd735e8
  scratch/k16_dual_rail_square_and_cut_obstructions_20260729.audit.json
f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
  scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.independent.components.json
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555
  scratch/k15_fixed_matching_pbbs_resident_20260729/from3_markov_s7_merge.best.json
3cdeb89d269b55d1b9f7d8895d3bc130dd35c1a6dd816608068edb7a03165adc
  scratch/audit_k16_pbbs_shore_20260729.py
e908002674c0b537b7ac51c83eb026b81d1d0dcb14802c5b67c42a2fab751828
  scratch/audit_pbbs_first_shadow.py
```

No SAT result, heavy search or unverified candidate is used in any theorem
of this note.

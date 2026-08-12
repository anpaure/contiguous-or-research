# Prime-cycle row-power admissibility and two-phase rigidity

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let `n=2m+1` be prime, let `sigma` be a coordinate `n`-cycle, and let
`F` be an exact middle wreath factor.  Give every row `C in F` an exponent
`e(C) in Z_n` and replace it by `sigma^{e(C)}C`.

This note gives an exact necklace-signature criterion for the resulting row
family to remain an exact middle factor.  It then proves a rigidity theorem:

\[
 \boxed{\text{Every admissible exponent map with at most two values is
 componentwise constant.}}
\]

Consequently every genuinely non-component-phase row-power trade uses at
least three distinct phases in one quotient component.  In particular,
quotient components with at most two row vertices are completely rigid.
For a three-row component, any nontrivial trade must use three distinct
phases, and every necklace vertex of that component is adjacent to all three
rows.  Thus the first unresolved local object is an exact `3 by 3` quotient
component with three-color necklace signatures admitting a nontrivial
three-phase retiling.

## 1. Necklace signatures

Let `N_m(sigma)` be the set of `sigma`-orbits on the middle layer.  Fix,
once and for all, a phase identification

\[
                         O\cong\mathbb Z_n
\tag{1.1}
\]

for every `O in N_m(sigma)`, in such a way that applying `sigma` adds one
to the phase.

For a wreath row `C` and a necklace `O`, define its phase signature

\[
 P_{C,O}:=\{t\in\mathbb Z_n:\text{the phase-}t\text{ member of }O
                  \text{ belongs to }\mathcal W_m(C)\}.
\tag{1.2}
\]

The original factor partitions every middle necklace, so for every `O`

\[
 \boxed{
 \mathbb Z_n=\bigsqcup_{C\in F}P_{C,O}.}
\tag{1.3}
\]

Empty signatures may be omitted.  Their cardinalities are exactly the edge
multiplicities in the quotient graph `Q_sigma(F)`.

Applying `sigma^{e(C)}` to row `C` translates every one of its signatures:

\[
                         P_{C,O}\longmapsto P_{C,O}+e(C).
\tag{1.4}
\]

### Theorem 1.1 (exact signature criterion)

The exponent map `e:F -> Z_n` is middle-admissible if and only if, for every
middle necklace `O`,

\[
 \boxed{
 \mathbb Z_n=\bigsqcup_{C\in F}\bigl(P_{C,O}+e(C)\bigr).}
\tag{1.5}
\]

Equivalently, if `zeta` is a primitive `n`-th root of unity, then for every
`O`, every `t in Z_n`, and every nonzero Fourier frequency
`xi in Z_n^*`,

\[
 \sum_C {\bf1}_{P_{C,O}+e(C)}(t)=1,
\tag{1.6}
\]

or, respectively,

\[
 \boxed{
 \sum_C \widehat{{\bf1}_{P_{C,O}}}(\xi)
          \zeta^{\xi e(C)}=0.}
\tag{1.7}
\]

#### Proof

Equation (1.4) follows from the chosen phase coordinates.  Exact middle
ownership is precisely the assertion that the translated row packets cover
each member of each necklace once, which is (1.5), equivalently (1.6).
Fourier transforming (1.6) gives (1.7) at every nonzero frequency; the zero
frequency is automatic because row sizes do not change. \(\square\)

The component-phase maps from the cyclic packet-component theorem are the
obvious solutions: if `e` is constant on each connected component of
`Q_sigma(F)`, every necklace partition in that component is translated as
one whole block.

### The Fourier incidence matrix and a complete rigidity certificate

For every nonzero frequency `xi`, form the necklace-by-row matrix

\[
 \boxed{
 M_\xi(O,C)=\widehat{{\bf1}_{P_{C,O}}}(\xi).}                  \tag{1.8}
\]

The original necklace partitions imply

\[
                         M_\xi\mathbf1=0.                       \tag{1.9}
\]

If all row signatures are singleton or empty--which, by the simultaneous
transversality theorem, may be assumed after a polynomial-size leave--and
the unique incidence phase is `phi(C,O)`, then

\[
 M_\xi(O,C)=
 \begin{cases}
  \zeta^{\xi\phi(C,O)},&C\sim O,\\
  0,&C\not\sim O.
 \end{cases}                                                    \tag{1.10}
\]

The exact signature criterion (1.7) becomes

\[
 \boxed{
 M_\xi v_\xi(e)=0,
 \qquad
 v_\xi(e)_C=\zeta^{\xi e(C)}.}                                \tag{1.11}
\]

### Theorem 1.2 (linear nullity criterion)

If, on one connected quotient component,

\[
                         \ker M_1=\langle\mathbf1\rangle,       \tag{1.12}
\]

then every middle-admissible row-power assignment is constant on that
component.  More generally, every nontrivial admissible assignment forces
`dim ker M_xi>=2` for every frequency `xi` on which its phase vector is
nonconstant.

#### Proof

For an admissible `e`, equation (1.11) at `xi=1` places the vector
`(zeta^{e(C)})_C` in `ker M_1`.  Under (1.12) it is constant, and
injectivity of `a->zeta^a` on `Z_n` makes `e` constant.  The final
assertion is the same argument frequency by frequency. \(\square\)

Thus connectivity is only the combinatorial shadow of the lift gate.  The
exact invariant is the extra nullity of the complex gain-incidence
matrices (1.8).  The genuine `Q_7` deck circuit supplies such an extra
kernel direction; a generic simple row--necklace graph is expected to
have none, but no all-dimensional rank theorem is currently proved.

There is also a quantitative approximate form.  For one phase assignment
let `h_O(j)` be the number of shifted incidences landing at phase `j` of
necklace `O`.  Parseval gives the exact identity

\[
 \boxed{
 \sum_{\xi=1}^{n-1}\|M_\xi v_\xi(e)\|_2^2
 =n\sum_O\sum_{j\in\mathbb Z_n}(h_O(j)-1)^2.}                  \tag{1.13}
\]

Indeed the zero-frequency coefficient is `n`, while
`sum_j h_O(j)=n` at every middle necklace.  Hence a uniform lower singular
value for the restrictions `M_xi|_(1^perp)` would be a stability theorem:
every phase assignment far from the component constants creates a
quantified middle defect.  Proving or disproving that singular-value bound
for the favorable prime cycles is now a precise statewise test of the
row-power lift architecture.

## 2. Two-phase rigidity

The next lemma is the key prime-order fact.

### Lemma 2.1 (a two-color translated partition cannot move)

Let `P subseteq Z_n`, where `n` is prime, and let `a,b in Z_n`.  If

\[
                  (P+a)\sqcup(P^c+b)=\mathbb Z_n,
\tag{2.1}
\]

then either `a=b`, or `P` is empty or all of `Z_n`.

#### Proof

Translate (2.1) by `-b` and put `d=a-b`.  Since `P+d` and `P^c` have total
cardinality `n`, they form a disjoint cover exactly when

\[
                             P+d=P.
\tag{2.2}
\]

If `d` is nonzero, it generates the additive group `Z_n`, because `n` is
prime.  Hence the only sets invariant under translation by `d` are the
empty set and the full group. \(\square\)

### Theorem 2.2 (two-phase rigidity)

Suppose the image of a middle-admissible exponent map `e:F -> Z_n` has at
most two elements.  Then `e` is constant on every connected component of
`Q_sigma(F)`.

#### Proof

The one-value case is immediate.  In the two-value case, write the values
as `a,b`.  Fix a necklace `O` and let

\[
                 P_O=\bigsqcup_{C:e(C)=a}P_{C,O}.
\tag{2.3}
\]

By the original partition (1.3), the union of the signatures of the
`b`-rows is `P_O^c`.  Admissibility at `O` is exactly

\[
                 (P_O+a)\sqcup(P_O^c+b)=\mathbb Z_n.
\tag{2.4}
\]

Lemma 2.1 says that if `a ne b`, then `P_O` is empty or full.  Thus every
row adjacent to `O` has the same exponent.  Every quotient edge therefore
joins vertices carrying one common exponent, and connectivity propagates
that exponent through each component. \(\square\)

### Corollary 2.3 (binary diagonal cubes contain nothing new)

For a prime coordinate cycle, no trade obtained by assigning only an old
phase and one new phase to rows can go beyond the component-phase choices
already supplied by the cyclic packet-component theorem.

This includes arbitrary choices of the two powers, not only the pair
`0,1`.

## 3. Rigidity of one- and two-row components

### Corollary 3.1

Every middle-admissible exponent map on a quotient component containing at
most two row vertices is constant on that component.

#### Proof

Such a map takes at most two values on the component.  Apply Theorem 2.2
to that component. \(\square\)

There is also a direct description of the two-row case.  If the rows are
`C,D`, then at every adjacent necklace `O` their nonempty signatures are
complements.  Admissibility requires

\[
 (P_{C,O}+e(C))\sqcup(P_{C,O}^c+e(D))=\mathbb Z_n,
\]

so Lemma 2.1 gives `e(C)=e(D)`.

## 4. The first possible nontrivial component

### Theorem 4.1 (three-row normal form)

Let `K` be a connected quotient component with exactly three row vertices.
If a middle-admissible exponent map is nonconstant on `K`, then:

1. the three row exponents are pairwise distinct;
2. every necklace vertex of `K` is adjacent to all three rows;
3. the component has exactly three necklace vertices, so its underlying
   simple support graph is `K_{3,3}`;
4. at each of those necklaces, three nonempty phase signatures form an old
   partition of `Z_n`, and their translates by the three distinct row
   exponents form a second partition.

#### Proof

By Theorem 2.2, a nonconstant admissible map cannot use only two values, so
the three row exponents are distinct.

Fix a necklace vertex `O`.  If it were adjacent to exactly two of the
rows, then only two exponent values would occur among its nonempty
signatures.  Lemma 2.1, applied after grouping equal exponent classes,
would force those two exponents to agree, a contradiction.  A necklace
vertex of degree one has all `n` of its phase points in one row.  That row
then uses all `n` of its middle sets on `O`, has no other quotient
neighbor, and forms a singleton component, again a contradiction.  Hence
every necklace vertex is adjacent to all three rows.

The quotient component is an `n`-regular bipartite multigraph, so its two
shores have equal cardinality.  It has three row vertices and therefore
three necklace vertices.  The final assertion is just the signature
criterion (1.5). \(\square\)

Thus the smallest possible genuinely new long-cycle row-power trade is not
a binary component cut.  It is a three-color retiling on an exact
three-row/three-necklace packet.

## 5. Scope and remaining gate

The theorem does not prove that a three-row component with the required
signatures occurs in an actual wreath factor, nor that every such component
is rigid.  Abstract three-color partitions can admit noncommon translations
(for example, equal translated pieces may exchange locations), so no
purely group-theoretic extension of Lemma 2.1 to three colors is possible
without using the special wreath signatures.

The exact next finite object is therefore:

\[
 \boxed{
 \begin{gathered}
 P_{i,j}\subseteq\mathbb Z_n\quad(1\le i,j\le3),\\
 \mathbb Z_n=\bigsqcup_iP_{i,j}
 =\bigsqcup_i(P_{i,j}+e_i)\quad(j=1,2,3),\\
 \sum_j|P_{i,j}|=n\quad(i=1,2,3),
 \end{gathered}}
\tag{5.1}
\]

with distinct `e_1,e_2,e_3`, together with the additional requirement that
the nine signatures come from three actual wreath rows and three actual
middle necklaces.  Constructing such a packet would give the first
non-component-phase cyclic row-power trade.  Proving that actual wreath
signatures forbid (5.1) would extend rigidity from two rows to three.

## 6. The abstract three-row gate is genuinely feasible

There is no further rigidity theorem at the level of quotient multiplicities
and phase partitions alone.  The first `3 by 3` gate in (5.1) has explicit
solutions for every odd prime `n>=5`.

### Theorem 6.1 (abstract three-row cyclic trade)

Let `n=2m+1>=5` be prime.  There are three row labels `C_1,C_2,C_3`, three
necklace labels `O_1,O_2,O_3`, nonempty signatures

\[
                         P_{i,j}\subseteq\mathbb Z_n,
\]

and three distinct exponents

\[
                         e_1=1,\qquad e_2=-1,\qquad e_3=0,
\tag{6.1}
\]

such that

\[
 \mathbb Z_n=\bigsqcup_{i=1}^3P_{i,j}
             =\bigsqcup_{i=1}^3(P_{i,j}+e_i)
 \qquad(j=1,2,3),
\tag{6.2}
\]

and

\[
                         \sum_{j=1}^3|P_{i,j}|=n
                         \qquad(i=1,2,3).
\tag{6.3}
\]

Thus these signatures define an abstract `n`-regular `3 by 3` quotient
component with a non-component-phase admissible exponent map.

#### Proof

Choose positive integers `a_1,a_2,a_3` with

\[
                  a_1+a_2+a_3=n,
          \qquad a_j\le {n-1\over2}.
\tag{6.4}
\]

Such a choice exists: take the three parts as equal as possible.  For each
`j`, choose a set `A_j subseteq Z_n` of size `a_j` with

\[
                             A_j\cap(A_j+1)=\varnothing.
\tag{6.5}
\]

For example, after identifying `Z_n={0,1,...,2m}`, one may take

\[
                         A_j=\{0,2,4,\ldots,2a_j-2\}.
\]

Define

\[
 P_{1,j}=A_j,
 \qquad P_{2,j}=A_j+1,
 \qquad P_{3,j}=\mathbb Z_n\setminus(A_j\cup(A_j+1)).
\tag{6.6}
\]

The old signatures partition `Z_n`.  Under (6.1), the first two pieces
exchange locations and the third stays fixed:

\[
 P_{1,j}+1=P_{2,j},
 \qquad P_{2,j}-1=P_{1,j},
 \qquad P_{3,j}+0=P_{3,j}.
\tag{6.7}
\]

Hence the translated signatures also partition, proving (6.2).  The first
two row degrees are

\[
                         \sum_ja_j=n,
\]

and the third is

\[
                 \sum_j(n-2a_j)=3n-2n=n.
\]

This proves (6.3). \(\square\)

### Consequence

The quotient graph, its edge multiplicities, and even the complete phase
signature exact-cover equations do not by themselves force component-phase
rigidity once three phases are allowed.  What remains is specifically the
**wreath-row realization problem**: can the nine sets (6.6), or a similar
three-color retiling, occur as intersections of three actual wreath packets
with three actual coordinate necklaces?

If such a realization exists and the transformed three wreaths are not just
a permutation of the original three, it is the smallest possible genuinely
new prime-cycle row-power trade.  If it is impossible, the proof must use
geometric identities special to consecutive `m`-windows, not quotient
regularity or phase-partition arithmetic.

The construction in Theorem 6.1 exchanges the first two complete signature
pieces at every necklace.  At the abstract packet level it can therefore be
viewed as a row permutation.  The next construction removes that weakness.

### Theorem 6.2 (genuinely non-permutational abstract `3 by 3` trade)

Let `n>=7` be an odd prime.  There are signatures satisfying (6.2)--(6.3)
with exponents

\[
                         e_1=1,\qquad e_2=2,\qquad e_3=0,
\tag{6.8}
\]

such that, at every necklace, `P_{1,j}+1` is not equal to any one of the
three old pieces.  In particular the translated packet is not obtained by
permuting the three old row signatures.

#### Proof

Choose positive integers `s_1,s_2,s_3` with

\[
             s_1+s_2+s_3=n,
       \qquad s_j\le {n-1\over2}.
\tag{6.9}
\]

Again the three nearly equal parts work.  Put

\[
                             r_j=n-2s_j\ge1.
\tag{6.10}
\]

In `Z_n`, represented by `0,1,...,n-1`, define

\[
\begin{aligned}
 P_{1,j}&=\{0,1,\ldots,r_j-1\},\\
 P_{2,j}&=\{r_j,r_j+2,\ldots,n-2\},\\
 P_{3,j}&=\mathbb Z_n\setminus(P_{1,j}\cup P_{2,j}).
\end{aligned}
\tag{6.11}
\]

The second set has `s_j` elements because
`r_j=n-2s_j`.  The first two sets are disjoint, so the old pieces partition
`Z_n` and their sizes are

\[
                         (r_j,s_j,s_j).
\tag{6.12}
\]

Now

\[
 P_{1,j}+1=\{1,2,\ldots,r_j\},
\tag{6.13}
\]

while

\[
 P_{2,j}+2=\{r_j+2,r_j+4,\ldots,n-2,0\}.
\tag{6.14}
\]

These two translated sets are disjoint and their union is exactly

\[
 P_{1,j}\cup P_{2,j}
 =\{0,1,\ldots,r_j\}
   \cup\{r_j+2,r_j+4,\ldots,n-2\}.
\tag{6.15}
\]

The third piece is fixed.  Hence (6.2) holds.

Summing the row degrees and using `sum_j s_j=n` gives

\[
 \sum_j|P_{1,j}|=\sum_j(n-2s_j)=n,
 \qquad
 \sum_j|P_{2,j}|=\sum_js_j=n,
 \qquad
 \sum_j|P_{3,j}|=\sum_js_j=n.
\tag{6.16}
\]

Finally `P_{1,j}+1` contains the interval `1,...,r_j`; it is neither
`P_{1,j}` nor `P_{2,j}`, and its size differs from `P_{3,j}` unless
`r_j=s_j`.  In the exceptional equal-size case it still has a consecutive
interval shape whereas `P_{3,j}` is the complementary alternating-gap
set.  Thus it is no old piece. \(\square\)

The local dynamics behind (6.11) is one directed cycle: take `r_j` steps
of size `1` followed by `s_j` steps of size `2`.  Its total displacement is

\[
                         r_j+2s_j=n=0\pmod n.
\]

The unvisited `s_j` phases are fixed by the third row.  This piecewise
translation picture may be a useful recognition test for an actual wreath
realization.

### Theorem 6.3 (complete local three-phase classification)

Let `A,B,C` partition `Z_n`, and let the three distinct exponents be
`a,b,c`.  Subtract the common phase `c` and write

\[
                         \alpha=a-c,
 \qquad                  \beta=b-c.
\]

Then

\[
             (A+\alpha)\sqcup(B+\beta)\sqcup C=\mathbb Z_n
\tag{6.17}
\]

if and only if the piecewise translation

\[
 T(x)=
 \begin{cases}
 x+\alpha,&x\in A,\\
 x+\beta,&x\in B
 \end{cases}
\tag{6.18}
\]

is a permutation of `U=A union B`.

Consequently every local three-phase solution is a disjoint union of
directed cycles whose edges have lengths `alpha` and `beta`.  If one such
cycle uses `r` edges of length `alpha` and `s` edges of length `beta`, then

\[
                         r\alpha+s\beta=0\pmod n.
\tag{6.19}
\]

Conversely, every vertex-disjoint family of simple directed cycles with
steps in `{alpha,beta}` defines a solution by putting a vertex in `A` or
`B` according to the step leaving it and putting all unused vertices in
`C`.

#### Proof

Because `C` is unchanged, (6.17) is equivalent to saying that the two
translated pieces `A+alpha` and `B+beta` are disjoint and have union
`U=A union B`.  This is exactly the assertion that (6.18) is a bijection
from `U` to itself.  Every permutation decomposes into directed cycles,
and the sum of the edge displacements around a cycle is zero, proving
(6.19).  The converse construction reverses the argument. \(\square\)

Thus the local signature problem is completely understood.  The unresolved
content is global: the cycle pieces at all necklace columns must have the
prescribed row-degree totals and, much more strongly, must arise from the
same three consecutive-window wreath rows.

## 7. Exact `Q_7` audit: the known factor has no new row-power trade

The abstract construction does not automatically occur in a genuine wreath
factor.  For the standard exact factor on seven coordinates, every
middle-admissible row-power map is a component phase, up to a permutation
of two rows that already are coordinate translates.

Take `sigma:x -> x+1` on `Z_7` and the five rows

\[
\begin{aligned}
 C_1&=(0,1,2,3,4,5,6),\\
 C_2&=(0,1,3,4,6,2,5),\\
 C_3&=(0,2,3,5,1,4,6),\\
 C_4&=(0,4,1,2,6,3,5),\\
 C_5&=(0,3,6,1,5,2,4).
\end{aligned}
\tag{7.1}
\]

The first row is a singleton quotient component: its seven middle triples
are one complete translation necklace.  The other four rows form one
component on the remaining four necklaces.  Use representatives

\[
\begin{aligned}
 B&=\{0,1,3\},& E&=\{0,2,3\},\\
 C&=\{0,1,4\},& D&=\{0,2,4\}.
\end{aligned}
\tag{7.2}
\]

Directly listing the seven consecutive triples in each row gives the phase
signature table

\[
\begin{array}{c|cccc}
 &B&E&C&D\\ \hline
 C_2&\{0,3\}&\{1,5\}&\{5\}&\{2,5\}\\
 C_3&\{2,6\}&\{0,4\}&\{4\}&\{1,4\}\\
 C_4&\{1,4\}&\{3,6\}&\{0,2\}&\{3\}\\
 C_5&\{5\}&\{2\}&\{1,3,6\}&\{0,6\}.
\end{array}
\tag{7.3}
\]

Every column partitions `Z_7`, as required.

### Theorem 7.1 (`Q_7` row-power rigidity)

Let `(a,b,c,d)` be the exponents assigned to `(C_2,C_3,C_4,C_5)`.
The translated signatures in (7.3) repartition every necklace if and only
if, for some `t in Z_7`,

\[
 (a,b,c,d)=(t,t,t,t)
\tag{7.4}
\]

or

\[
 (a,b,c,d)=(t-1,t+1,t,t).
\tag{7.5}
\]

The second solution merely exchanges the middle packets of `C_2` and
`C_3`; therefore it produces the same component-phase factor as (7.4).

#### Proof

Subtract the common exponent `d` and normalize `d=0`.  In the `C`-necklace,
the fixed signature of `C_5` is `{1,3,6}`.  Hence the other translated
pieces must lie in `{0,2,4,5}`.  From the singleton signatures and the
two-point signature of `C_4` this gives

\[
 a\in\{0,2,4,6\},\qquad
 b\in\{0,1,3,5\},\qquad
 c\in\{0,2,5\}.
\tag{7.6}
\]

In the `D`-necklace, the fixed piece is `{0,6}`.  Requiring the other
translated pieces to avoid it sharpens (7.6) to

\[
                         a\in\{0,6\},
 \qquad b\in\{0,1\},
 \qquad c\in\{0,2,5\}.
\tag{7.7}
\]

Now use the `B`-necklace, whose fixed point is `{5}`.  If `a=0`, the first
piece is `{0,3}`; disjoint completion forces the second piece to be
`{2,6}`, hence `b=0`, and then the third must be `{1,4}`, hence `c=0`.
If `a=6`, the first piece is `{2,6}`; disjoint completion forces `b=1`,
giving `{0,3}`, and again `c=0`.  Thus the only normalized solutions are

\[
                         (a,b,c,d)=(0,0,0,0)
 \quad\text{and}\quad
                         (6,1,0,0).
\tag{7.8}
\]

Both also satisfy the `E`-column.  Adding back the common phase gives
(7.4)--(7.5).

Finally the table shows, column by column,

\[
                   P_{C_2,O}+6=P_{C_3,O},
 \qquad             P_{C_3,O}+1=P_{C_2,O}.
\tag{7.9}
\]

Thus the exceptional normalized solution only swaps the two complete
middle packets. \(\square\)

This exact small case supplies no suspendable nontrivial seed.  It also
shows what a successful search must exclude: solutions of the signature
equations which are merely coordinate-translate permutations of existing
rows.

### Lemma 7.2 (the middle packet determines the whole row flag)

For `n=2m+1` and `m>=2`, the family of all cyclic length-`m` intervals of
one coordinate order determines that order up to cyclic rotation and
reversal.  Consequently two wreath rows with the same middle packet have
the same interval packet at every length.

#### Proof

Inside one middle packet, two sets have intersection size `m-1` exactly
when their start positions are consecutive around the cyclic order.  Thus
the Johnson-adjacency graph induced by the packet is the cycle `C_n`, which
recovers the cyclic sequence of middle sets up to rotation and reversal.

Choose one direction around that recovered cycle and write the sets as
`X_0,...,X_(n-1)`.  The unique element

\[
                         x_i\in X_i\setminus X_{i+1}
\]

is the coordinate leaving the moving window.  Hence
`(x_0,...,x_(n-1))` is the underlying coordinate order.  Reversing the
recovered middle-set cycle reverses the coordinate order.  Rotation and
reversal preserve the family of cyclic intervals at every length. \(\square\)

Therefore a row-power solution which only permutes existing middle packets
is vertically inert as a multiset: it also permutes their complete lower
and upper flags.  This justifies treating (7.5) as trivial for the shadow
problem, not merely for middle ownership.

## 8. Exact necklace-deck criterion

The signature equations have a useful integrated form which works directly
with actual wreath packets.

For `e in {0,1,...,n-1}`, put

\[
 Q_e(\sigma)=I+\sigma+\cdots+\sigma^{e-1},
 \qquad Q_0(\sigma)=0.
\tag{8.1}
\]

Let `w_C` be the `0-1` indicator of the middle packet of row `C`.

### Theorem 8.1 (invariant-deck characterization)

An exponent map `e:F -> Z_n` is middle-admissible if and only if the
nonnegative integer deck

\[
 \boxed{
 G_e:=\sum_{C\in F}Q_{e(C)}(\sigma)w_C}
\tag{8.2}
\]

is `sigma`-invariant.  Equivalently, `G_e` has constant multiplicity on
every middle `sigma`-necklace.

The criterion is independent of the chosen representatives
`e(C) in {0,...,n-1}`.

#### Proof

The old and new middle load vectors differ by

\[
\begin{aligned}
 \sum_C\bigl(\sigma^{e(C)}-I\bigr)w_C
 &=(\sigma-I)\sum_CQ_{e(C)}(\sigma)w_C\\
 &=(\sigma-I)G_e.
\end{aligned}
\tag{8.3}
\]

Thus exact middle cancellation is equivalent to `(sigma-I)G_e=0`, which
is precisely `sigma`-invariance.  Replacing an exponent representative
`e` by `e+n` adds

\[
 Q_n(\sigma)w_C=(I+\sigma+\cdots+\sigma^{n-1})w_C,
\]

which is already invariant. \(\square\)

### Corollary 8.2 (the `1,2,0` gate)

Three rows `C,D,E` with exponents `(1,2,0)` give a legal middle trade if
and only if

\[
 \boxed{
 w_C+w_D+\sigma w_D
 \quad\text{is constant on every middle necklace}.}
\tag{8.4}
\]

In the particularly transparent `0-1` case, the three packets

\[
                         C,\quad D,\quad\sigma D
\]

partition a union of three complete necklaces.  Cancelling the common
`sigma D` term from the translated invariant union gives the two-row trade

\[
 \boxed{
            \sigma C\sqcup\sigma^2D=C\sqcup D.}
\tag{8.5}
\]

Equation (8.4), rather than the bare `3 by 3` multiplicity matrix, is the
exact actual-wreath construction target.

## 9. Lower-shadow action of an invariant middle deck

Let `u_{C,q}` denote the depth-`q` load vector contributed by row `C`.
For the same exponent map define its depth-`q` deck

\[
                         G_{e,q}
 =\sum_CQ_{e(C)}(\sigma)u_{C,q}.
\tag{9.1}
\]

Then the exact load change at depth `q` is

\[
 \boxed{
 \Delta_{e,q}
 :=\sum_C\bigl(\sigma^{e(C)}-I\bigr)u_{C,q}
 = (\sigma-I)G_{e,q}.}
\tag{9.2}
\]

Middle admissibility says exactly that `G_{e,0}` is invariant, so
`Delta_{e,0}=0`.  The trade has useful lower-shadow action precisely when
some lower deck `G_{e,q}` is not invariant.

This yields a concise definition of a suspendable nontrivial seed:

\[
 \boxed{
 G_{e,0}\in\ker(\sigma-I),
 \qquad
 G_{e,q}\notin\ker(\sigma-I)
 \text{ for at least one controlled }q.}
\tag{9.3}
\]

Component phases satisfy (9.3) only through the ordinary relabelling action
of an entire invariant middle component.  A genuinely new deck trade is an
invariant positive middle deck assembled from unequal row prefixes
`Q_{e(C)}w_C` whose lower deck retains a nonzero discrete derivative.

## 10. A minimal disjoint-deck construction criterion

Corollary 8.2 becomes especially concrete when its three deck layers are
disjoint.

### Theorem 10.1 (three-necklace complement criterion)

Let `D` be an actual wreath row.  Suppose:

1. `w_D` and `sigma w_D` are disjoint;
2. the middle sets in `D` meet exactly three `sigma`-necklaces;
3. if `U` is the union of those three necklaces, then
   
   \[
                    w_C:={\bf1}_U-w_D-\sigma w_D
   \tag{10.1}
   \]
   
   is the middle packet of an actual wreath row `C`.

Then

\[
                         C,D\longleftrightarrow
                         \sigma C,\sigma^2D
\tag{10.2}
\]

is a legal two-row middle trade.  It is nontrivial unless the two new rows
are merely the two old rows in the opposite order.

Conversely, every disjoint `0-1` invariant deck of the form

\[
                         w_C+w_D+\sigma w_D
\tag{10.3}
\]

has exactly the form (10.1) on a union of three necklaces.

#### Proof

Under the assumptions, (10.1) says that

\[
                         w_C+w_D+\sigma w_D={\bf1}_U,
\]

which is `sigma`-invariant.  Corollary 8.2 gives (10.2).

Conversely, a disjoint `0-1` deck (10.3) has total mass `3n` and is constant
on every length-`n` necklace.  Hence it is the indicator of exactly three
necklaces, proving (10.1). \(\square\)

This reduces the smallest useful prime-cycle lift to one explicit
recognition question: find a wreath `D` whose packet and one coordinate
translate are disjoint, touch only three necklaces, and have a wreath as
their three-necklace complement.

### Corollary 10.2 (consecutive phases force the minimal deck)

Let a connected three-row quotient component admit the exponent values
`0,1,2`.  Name the phase-one and phase-two rows `C,D`.  Then automatically

\[
 \boxed{
                         w_C+w_D+\sigma w_D}
\tag{10.4}
\]

is the indicator of the union of the component's three necklaces.  In
particular its three summands are pairwise disjoint, and the resulting
trade is exactly

\[
                         C,D\longleftrightarrow
                         \sigma C,\sigma^2D.
\tag{10.5}
\]

#### Proof

Theorem 4.1 says that the component has three necklace vertices and every
row meets every necklace.  The invariant-deck criterion says that (10.4)
is constant, with some nonnegative integer level, on each necklace.

It is nonzero on every necklace because the phase-one row `C` has a
nonempty signature there.  Hence all three necklace levels are at least
one.  The total mass of the deck is

\[
                         n+2n=3n.
\]

The three necklace levels therefore sum to three, so every one equals one.
Thus (10.4) is a `0-1` union of all three necklaces, and Theorem 10.1
applies. \(\square\)

So for the smallest component and the smallest genuinely three-valued
phase pattern, actual row-power realization is equivalent to the concrete
three-necklace complement problem, with no hidden multiplicity case.

## 11. Why three necklaces is the first possible support

For a row `D`, let `P_{D,O}` be its phase signature in necklace `O`.
The disjointness condition in Theorem 10.1 is exactly

\[
                         P_{D,O}\cap(P_{D,O}+1)=\varnothing
                         \qquad\text{for every }O.
\tag{11.1}
\]

Each such signature is an independent set in the odd cycle `C_n`, so

\[
                         |P_{D,O}|\le {n-1\over2}=m.
\tag{11.2}
\]

Since the row has `n=2m+1` middle sets, it must meet at least three
necklaces.  Thus the support size three in Theorem 10.1 is minimal, not an
arbitrary simplification.

There is a second, independent adjacency restriction.

### Lemma 11.1 (same-necklace consecutive windows force an AP necklace)

Let `X,Y` be consecutive middle windows of one wreath row.  If

\[
                             Y=\sigma^dX
\tag{11.3}
\]

for a nonzero `d`, then `X` is a consecutive length-`m` interval in the
coordinate cycle generated by `sigma^d`.  Hence the whole necklace of `X`
is itself an arithmetic-progression wreath.

#### Proof

Consecutive middle windows differ by one deletion and one insertion, so

\[
                         |X\triangle\sigma^dX|=2.
\tag{11.4}
\]

Because `n` is prime and `d ne 0`, translation by `d` is one `n`-cycle on
the coordinates.  Read the binary indicator of `X` around that cycle.
Equation (11.4) says that the binary word changes value exactly twice.
Therefore its ones form one consecutive block, of length `|X|=m`.
\(\square\)

Thus, unless one of the three necklaces is already an AP wreath, the
necklace-color sequence of the `n` consecutive windows of `D` has no equal
adjacent colors.  Any actual construction must satisfy both this
start-sequence constraint and the phase-independent-set constraint (11.1).

## 12. Exact deterministic phase-cover bound, and its sharp limitation

Suppose the quotient components are `K`, and at one lower target necklace
`O` let

\[
 u_{K,O}:\mathbb Z_n\longrightarrow\mathbb Z_{\ge0}
\]

be the component load.  Put

\[
                         s_{K,O}=|\operatorname{supp}u_{K,O}|.
\tag{12.1}
\]

Choosing component phase `e_K` translates this support by `e_K`.

### Theorem 12.1 (conditional-expectation phase cover)

For any finite collection of target necklaces, at any collection of depths,
and for any nonnegative necklace weights `b_O`, there is one deterministic
choice of component phases such that the weighted number of uncovered
target points is at most

\[
 \boxed{
 \sum_Ob_On
       \prod_K\left(1-{s_{K,O}\over n}\right).}
\tag{12.2}
\]

In particular,

\[
 \boxed{
 H_O\le n\exp\left(-{1\over n}\sum_Ks_{K,O}\right)}
\tag{12.3}
\]

is simultaneously attainable in weighted aggregate.

#### Proof

Choose the phases independently and uniformly in `Z_n`.  A fixed point of
necklace `O` is missed by component `K` with probability

\[
                         1-{s_{K,O}\over n}.
\]

Independence across components gives the product in (12.2).  Sum over the
`n` target points and over weighted necklaces.  Some deterministic phase
vector is no worse than the expectation.  Equivalently, expose the phases
one at a time and at each step choose a value no worse than the conditional
average.  Equation (12.3) follows from `1-x<=e^{-x}`. \(\square\)

There is also an unavoidable component-support floor

\[
 \boxed{
 H_O\ge\left(n-\sum_Ks_{K,O}\right)_+,}
\tag{12.4}
\]

because translated supports cannot cover more than the sum of their sizes.
This can be strictly stronger than the orbit-mass floor: repeated
occurrences inside one component contribute mass but only one support point
after a common phase shift.

### Why generic discrepancy is insufficient

Even in the best case `s_{K,O}=||u_{K,O}||_1` (no repeated supported phase
inside any component), a first-shadow orbit has total mass approximately
`n lambda_1=(1+o(1))n`.  Formula (12.3) then gives only

\[
                         H_O\lesssim n e^{-1},
\tag{12.5}
\]

not `o(n)`.  Summed over the `N_1/n` first-shadow necklaces, this is a
linear `Theta(W)` defect.  The bound is the same occupancy barrier as
independent random cyclic orders, now inside the exact factor fibre.

Therefore an argument based only on independent phases, conditional
expectation, or black-box discrepancy cannot realize the orbit-mass floor.
It must use special necklace tilings, such as the invariant-deck identities
of Sections 8--10, which deliberately make translated supports complementary
rather than merely weakly overlapping.

## 13. A cycle-metric obstruction to actual deck realization

The minimal seed of Theorem 10.1 must satisfy more than the phase-signature
equations.  Every actual wreath packet has a rigid pair-incidence matrix.

For a wreath row `R`, let `delta_R(x,y) in {1,...,m}` be the shorter
circular distance between coordinates `x,y` in its underlying cyclic
order.  Let

\[
 k_R(x,y)=\#\{X\in\mathcal W_m(R):\{x,y\}\subseteq X\}.
\]

Then

\[
 \boxed{
                         k_R(x,y)=m-\delta_R(x,y).}
\tag{13.1}
\]

Indeed, two positions at shorter distance `d` lie together in exactly
`m-d` cyclic intervals of length `m`.

Now suppose a disjoint minimal deck exists:

\[
                         U=C\sqcup D\sqcup\sigma D,
\tag{13.2}
\]

where `U` is a union of three complete `sigma`-necklaces.  Translation
invariance makes its pair-incidence count depend only on the coordinate
difference.  Write

\[
                         k_U(x,y)=K_U(y-x).
\tag{13.3}
\]

If `sigma:x -> x+1`, then

\[
 k_{\sigma D}(x,y)=k_D(x-1,y-1).
\]

Using (13.1) in (13.2) yields the exact necessary equation

\[
 \boxed{
 \delta_C(x,y)+\delta_D(x,y)+\delta_D(x-1,y-1)
 =3m-K_U(y-x)}
\tag{13.4}
\]

for every unordered coordinate pair.

The right side is circulant, whereas the left side is the sum of three
Hamilton-cycle distance metrics, two of which are translates of one
another.  Thus an abstract signature solution lifts to actual rows only if
its three necklace representatives can be chosen so that the complementary
pair-incidence matrix in (13.4) is itself a circular distance metric.

Equation (13.4) is a purely finite recognition test and a possible rigidity
route.  It is not implied by row/column sums or by the translated-partition
equations; those constraints use only target ownership, while (13.4) records
how all coordinate pairs co-occur inside the alleged wreath rows.

## 14. Arithmetic-progression singleton components are vertically inert

Let `sigma:x -> x+1` on `Z_n`, fix `a in Z_n^*`, and take the affine cyclic
order

\[
                         \pi_a=(0,a,2a,\ldots,(n-1)a).
\tag{14.1}
\]

At interval length `r`, its cyclic intervals are

\[
 \mathcal W_r(\pi_a)
 =\left\{ja+\{0,a,\ldots,(r-1)a\}:j\in\mathbb Z_n\right\}.
\tag{14.2}
\]

Because multiplication by `a` permutes `Z_n`, the translates `ja` run
through every coordinate translation.  Hence (14.2) is one complete
`sigma`-necklace, and

\[
 \boxed{
                         \sigma^e\mathcal W_r(\pi_a)
                         =\mathcal W_r(\pi_a)
                         \quad\text{for every }e,r.}
\tag{14.3}
\]

Thus an AP row is a singleton quotient component at the middle layer, but
all of its lower and upper interval packets are invariant as well.  Any
phase assigned to this component changes no rank load vector whatsoever.

Consequently a factor built from affine/AP wreaths may provide exact middle
ownership, but its singleton components cannot perform the orbit-mass
redistribution needed for constant one.  Useful prime-cycle phases must
come from non-affine multirow components or from invariant decks such as
Section 10.

## 15. Giant-component obstruction

Let the quotient components have row sizes `b_K`, with

\[
                         \sum_Kb_K=B=W/n,
\]

and let `b_max=max_K b_K`.

### Theorem 15.1

For every component-phase choice and every fixed depth `q`, the number of
holes it can remove relative to the original factor is at most

\[
 \boxed{
                         n(B-b_{\max}).}
\tag{15.1}
\]

More generally, for nonnegative weights `w_q`, its weighted hole reduction
through depths `q<=H` is at most

\[
 \boxed{
             n(B-b_{\max})\sum_{q\le H}w_q.}
\tag{15.2}
\]

#### Proof

Let `K_0` be a largest component and let `t` be its selected phase.  Compare
the chosen factor with the global relabeling `sigma^tF`.  The two factors
agree on all `b_max` rows of `K_0`; they differ on at most
`B-b_max` rows.

At depth `q`, every inserted row supplies exactly `n` target occurrences.
It can fill at most `n` previously missing targets.  Hence changing `R`
rows can reduce the hole count by at most `nR`, proving (15.1).  Sum with
weights to obtain (15.2).  A global relabeling merely permutes targets and
has the same hole count as the original factor. \(\square\)

In particular, if `b_max=B-o(B)`, every component-phase lift changes a
fixed-depth defect by only `o(W)`.  A factor with a linear first-shadow
defect can be repaired by this mechanism only if

\[
                         B-b_{\max}=\Omega(B).
\tag{15.3}
\]

Thus extensive quotient fragmentation is a necessary condition, not just
a convenient source of independence.  At the two extremes:

* a connected quotient permits only a global relabeling and no defect
  improvement;
* AP singleton components are numerous but vertically inert by Section 14.

The useful regime must have macroscopically many rows in non-affine,
nontrivial components.

## 16. Independent composition and the required packing scale

Suppose an exact factor contains pairwise disjoint row pairs

\[
                         (C_i,D_i),\qquad 1\le i\le t,
\]

each satisfying the deck identity

\[
                         C_i\sqcup D_i
                         =\sigma C_i\sqcup\sigma^2D_i.
\tag{16.1}
\]

### Proposition 16.1

The `t` trades in (16.1) may be switched independently.  Every one of the
`2^t` resulting row families is an exact middle factor.

At any fixed depth, however, the total number of holes that any corner can
remove relative to the original factor is at most

\[
 \boxed{2nt.}
\tag{16.2}
\]

#### Proof

Each identity (16.1) partitions exactly the same two-row middle support on
its two sides.  Different old pairs have disjoint supports because they are
rows of one factor.  Replacing any subset therefore preserves the middle
partition pair by pair.

One switched pair inserts two rows, carrying `2n` occurrences at every
depth.  It can fill at most `2n` old holes.  Summing proves (16.2).
\(\square\)

Thus repairing an `epsilon W` first-shadow defect by bounded-row deck
trades requires

\[
                         t\ge {\epsilon W\over2n}
                         ={\epsilon B\over2}.
\tag{16.3}
\]

An isolated finite seed, even a genuinely nontrivial one, does not move the
asymptotic frontier unless it admits a suspension or packing theorem that
produces `Omega(B)` disjoint copies with useful and sufficiently
noncancelling lower-shadow directions.

## 17. A genuine actual prime-cycle deck trade on seven coordinates

The realization gate is nonempty.  There is an explicit non-component
row-power trade in the exact `Q_7` fibre.

Work on `Z_7` with `sigma:x -> x+1`.  Put

\[
\begin{aligned}
 P&=(0,1,2,3,4,5,6),\\
 D&=(0,1,3,4,6,2,5),\\
 E&=\sigma D=(1,2,4,5,0,3,6),\\
 A&=(0,2,6,3,5,1,4),\\
 B&=(5,2,3,0,4,6,1).
\end{aligned}
\tag{17.1}
\]

### Theorem 17.1 (exact `Q_7` cyclic deck circuit)

The two row families

\[
 \boxed{
 F^-:=\{P,E,D,A,B\},
 \qquad
 F^+:=\{P,E,\sigma^2D,\sigma A,\sigma B\}}
\tag{17.2}
\]

are exact middle wreath factors.  The passage from `F^-` to `F^+` is a
genuine non-component row-power trade on the connected four-row component
containing `D,E,A,B`; its exponent vector there is

\[
                         (2,0,1,1).
\tag{17.3}
\]

It is not a permutation of old row packets.

At depth one, both factors are exactly floor-balanced.  Their signed load
change is

\[
 \boxed{
 \Delta_1
 =({\bf e}_{02}+{\bf e}_{14}+{\bf e}_{56})
  -({\bf e}_{01}+{\bf e}_{25}+{\bf e}_{46}).}
\tag{17.4}
\]

Thus the circuit moves three bonus loads around the six-cycle

\[
                         0-1-4-6-5-2-0
\tag{17.5}
\]

without creating a first-shadow hole or overload.  At depth two every
singleton has load five in both factors.

#### Proof

Use the four nonconsecutive triple necklaces represented by

\[
 \{0,1,3\},\quad\{0,2,3\},\quad
 \{0,1,4\},\quad\{0,2,4\}.
\]

Writing their phase columns in that order, direct enumeration of the seven
length-three windows gives

\[
\begin{array}{c|cccc}
 D&\{0,3\}&\{1,5\}&\{5\}&\{2,5\}\\
 E&\{1,4\}&\{2,6\}&\{6\}&\{3,6\}\\
 A&\{6\}&\{3\}&\{0,2,4\}&\{0,1\}\\
 B&\{2,5\}&\{0,4\}&\{1,3\}&\{4\}.
\end{array}
\tag{17.6}
\]

Every column partitions `Z_7`.  The row `P` is the complete necklace of
consecutive triples, so `F^-` partitions all `35` middle triples.

The same table shows that

\[
                         w_D+\sigma w_D+w_A+w_B
\tag{17.7}
\]

is the indicator of the union of the four displayed necklaces.  It is
`sigma`-invariant.  Applying `sigma` to (17.7) and cancelling the common
term `sigma w_D=w_E` gives

\[
 \boxed{
                         w_D+w_A+w_B
 =\sigma^2w_D+\sigma w_A+\sigma w_B.}
\tag{17.8}
\]

Together with the unchanged rows `P,E`, this proves exactness of `F^+`.

The four rows in (17.6) all meet all four necklaces, so their quotient
support is connected.  The exponent vector (17.3) is nonconstant.  It is
not a row permutation: for example `sigma^2D` has phase signatures

\[
 \{2,5\},\quad\{0,3\},\quad\{0\},\quad\{0,4\},
\]

which equal none of the four rows in (17.6).

For depth one, list the adjacent coordinate pairs in the three changed old
rows and the three changed new rows.  Cancellation leaves exactly (17.4).
In `F^-`, the seven load-one pairs are

\[
                         02,06,13,14,24,35,56,
\tag{17.9}
\]

and every other pair has load two.  In `F^+`, they are

\[
                         01,06,13,24,25,35,46,
\tag{17.10}
\]

and every other pair again has load two.  This proves exact first-shadow
balance and (17.4).  Finally every cyclic row contains each singleton once,
so five rows give load five on every singleton. \(\square\)

### Significance and limit

This is the first explicit positive answer to the prime-cycle row-lift
question at the actual wreath level:

* the quotient component is connected, so the trade is not generated by
  component phases;
* the transformed rows are actual coordinate powers of the old rows;
* middle ownership remains exact;
* the lower shadow changes nontrivially while staying on the balanced
  integer floor.

It does **not** prove constant one.  By Proposition 16.1, one needs an
all-dimensional suspension or packing producing `Omega(B)` compatible
copies, with directions rich enough to balance arbitrary shallow defects.
The exact new gate is to lift the six-cycle bonus-matching circuit (17.4)
through the MSW recursion or another scalable wreath-factor construction.

### Corollary 17.2 (the seed spans every rational first-shadow direction)

Let `delta` be the signed pair vector in (17.4), embedded in any larger
coordinate set.  The rational span of its full coordinate-permutation orbit
is the entire space of rank-two load vectors with zero total and zero point
marginals.

#### Proof

The vector `delta` has three positive and three negative edges, so its total
is zero.  At every one of its six used coordinates, one positive and one
negative edge meet; all other coordinates have degree zero.  Hence `delta`
is orthogonal to the constant and point-coordinate subspaces.

The permutation module on two-subsets decomposes as

\[
                         U_0\oplus U_1\oplus U_2.
\]

Thus `delta` is a nonzero vector in the irreducible module `U_2`.  The span
of the orbit of any nonzero vector in an irreducible module is the whole
module. \(\square\)

So there is no linear first-shadow direction obstruction: coordinate copies
of the `Q_7` circuit generate every centered, point-balanced pair correction.
The missing assertion is positive simultaneous packing inside one exact
factor, followed by control of the deeper flags.

## 18. Antisymmetrizing the seed gives a complete flag-neutral relation

Let

\[
 z=(\sigma^2D+\sigma A+\sigma B)-(D+A+B)
\tag{18.1}
\]

be the signed row relation from Theorem 17.1.  Let

\[
                         \tau=(0\ 1\ 4\ 6\ 5\ 2),
 \qquad \tau(3)=3.
\tag{18.2}
\]

This coordinate permutation advances one step on the six-cycle in (17.5).

### Theorem 18.1 (formal flag-neutral double circuit)

The signed row vector

\[
                         y=z+\tau z
\tag{18.3}
\]

is nonzero and satisfies

\[
 \boxed{
                         B_r y=0
                         \qquad(1\le r\le6),}
\tag{18.4}
\]

where `B_r` records the multiset of cyclic intervals of length `r`.

After cancellation of no common rows, each sign of `y` contains six
distinct wreath rows.  However, neither sign is a middle packing.  Its
middle multiplicity histogram is exactly

\[
 \boxed{
                         0^5\,1^{18}\,2^{12}.}
\tag{18.5}
\]

Thus `y` is a genuine complete-flag kernel relation, but it requires
positive disjointization before it can be used as a factor move.

#### Proof

The middle relation `B_3z=0` is Theorem 17.1.  The first-shadow action is
the alternating matching vector `Delta_1` in (17.4).  The permutation
`tau` exchanges the two alternating perfect matchings of the six-cycle, so

\[
                         \tau\Delta_1=-\Delta_1.
\tag{18.6}
\]

Hence `B_2y=0`.  Every cyclic row contains every singleton once, so
`B_1z=0` and therefore `B_1y=0`.  On seven coordinates, complementation
identifies length `r` interval packets with length `7-r` packets.  This
gives (18.4) at lengths four, five, and six as well.

The twelve oriented rows, reduced up to rotation and reversal, are
pairwise distinct; direct canonicalization of the orders in (17.1) and
their `tau`-images verifies that no row cancels.  In particular `y` is
nonzero.

It remains to compute the middle multiplicities on, say, the negative
side.  Put

\[
                         U^-={\cal W}_3(D)\sqcup
                             {\cal W}_3(A)\sqcup
                             {\cal W}_3(B).
\]

In the exact factor `F^-`, its complement is the fourteen-set family

\[
                         C_0={\cal W}_3(P)\sqcup{\cal W}_3(E).
\tag{18.7}
\]

The negative middle multiset of `y` is

\[
                         {\bf1}_{U^-}+{\bf1}_{\tau U^-}.
\tag{18.8}
\]

Listing the two seven-set packets in (18.7) gives

\[
\begin{aligned}
 {\cal W}_3(P)&=\{012,123,234,345,456,056,016\},\\
 {\cal W}_3(E)&=\{124,245,045,035,036,136,126\}.
\end{aligned}
\tag{18.9}
\]

Their intersection with their `tau`-image has size five:

\[
 C_0\cap\tau C_0
 =\{036,126,123,345,045\},
 \qquad |C_0\cap\tau C_0|=5.
\tag{18.10}
\]

Since `U^-` is the complement of `C_0` in the `35` middle triples,

\[
 |U^-\cap\tau U^-|
 =35-|C_0\cup\tau C_0|
 =35-(28-5)=12.
\tag{18.11}
\]

Thus twelve targets have multiplicity two.  The union has size
`42-12=30`, leaving five targets of multiplicity zero; the remaining
`35-12-5=18` have multiplicity one.  The positive side has the same middle
multiset because `B_3y=0`, proving (18.5). \(\square\)

### Exact suspension interpretation

The relation `y` satisfies the strongest possible linear hypothesis for a
context lift: every old interval rank cancels.  Therefore any linear
all-pointings or antipodal suspension remains shadow-neutral.  What fails
is positivity at the right-hand-side-one fibre, already visible in
(18.5).  A successful lift must split the twelve double middle targets
between distinct context sectors while filling the five holes on both signs.

This is more concrete than the general suspension gate: for this seed the
entire obstruction is the disjointization of the explicit histogram
`0^5 1^18 2^12`; no further shadow equation remains to be solved.

## 19. The finite-field derivative of the lift and a spanning-tree rigidity certificate

The Fourier matrices in Section 1 admit a phase-free first obstruction.
It is stronger than connectivity and is often easier to test than a
complex singular value.

Put `p=n`, let `K=Q(zeta)`, let

\[
                    {\mathfrak p}=(1-\zeta)\subseteq {\mathbb Z}[\zeta],
\qquad {\mathbb Z}[\zeta]/{\mathfrak p}\cong{\mathbb F}_p,
\tag{19.1}
\]

and define the integer row--necklace multiplicity matrix

\[
                    B(O,C)=|P_{C,O}|.
\tag{19.2}
\]

Every row and every necklace has total multiplicity `p`.  Hence, modulo
`p`, the constant vectors lie in both the right and left kernels of `B`.
On a connected quotient component the two sides have the same number of
vertices.

### Theorem 19.1 (exact finite-field moment criterion)

An exponent map `e:F -> F_p` is middle-admissible if and only if, for every
middle necklace `O` and every function `f:F_p -> F_p`, one has

\[
 \boxed{
 \sum_C\sum_{t\in P_{C,O}} f(t+e(C))
 =\sum_{u\in{\mathbb F}_p}f(u).}
\tag{19.3}
\]

It is enough to impose (19.3) for `f(x)=x^r`, `0<=r<=p-1`.  In
particular, every admissible exponent vector satisfies

\[
                         \boxed{Be=0\quad\hbox{over }{\mathbb F}_p.}
\tag{19.4}
\]

The next equation in the hierarchy is

\[
 2\sum_C e(C)\sum_{t\in P_{C,O}}t
 +\sum_C B(O,C)e(C)^2=0
 \qquad(O\in{\cal N}_m(\sigma)).
\tag{19.5}
\]

#### Proof

Before shifting, the signatures at `O` partition `F_p`; after shifting,
middle admissibility says that they again partition `F_p`.  Summing any
function over the two multisets gives (19.3).  Conversely the functions on
`F_p` are represented by polynomials of degree at most `p-1`; equality for
the displayed monomials therefore gives equality against every point
indicator and forces the shifted multiplicity to be one at every phase.

Taking `f(x)=x` and using
`sum_(u in F_p)u=0` gives (19.4).  Expanding `f(x)=x^2` gives (19.5).
\(\square\)

There is an equivalent cyclotomic derivation of (19.4).  Subtract the old
Fourier equation from the new one and divide by `zeta^xi-1`:

\[
 \sum_C\sum_{t\in P_{C,O}}
 \zeta^{\xi t}\,{\zeta^{\xi e(C)}-1\over\zeta^\xi-1}=0.
\tag{19.6}
\]

Reduction modulo `mathfrak p` sends the quotient in (19.6) to `e(C)` and
again gives `Be=0`.  Thus (19.4) is literally the first cyclotomic
derivative of exact ownership.

There is also no independent compatibility problem between the nonzero
Fourier frequencies.  If `tau_xi` is the Galois automorphism
`zeta -> zeta^xi`, then

\[
 \boxed{
 \tau_\xi\!\left(M_1v_1(e)\right)=M_\xi v_\xi(e).}
\tag{19.6a}
\]

Consequently a root-valued vector `v_1(e)` solves the frequency-one
equation if and only if all its Galois conjugates solve all nonzero
frequency equations.  The hard distinction is therefore not compatibility
across `xi`; it is the distinction between an arbitrary complex kernel
vector and a vector whose coordinates are `p`-th roots of unity.

### Corollary 19.2 (the `p`-rank rigidity theorem)

Suppose a connected quotient component contains `b` rows and `b`
necklaces.  If

\[
                     \boxed{\operatorname{rank}_{\mathbb F_p}B=b-1,}
\tag{19.7}
\]

then every middle-admissible row-power assignment is constant on that
component.

More strongly, for every nonzero frequency `xi`,

\[
 \boxed{
 \ker_K M_\xi=\langle\mathbf1\rangle.}
\tag{19.8}
\]

#### Proof

Equation (19.4) and (19.7) make `e` constant.  Also

\[
                         M_\xi\pmod{\mathfrak p}=B\pmod p,
\tag{19.9}
\]

because every `zeta^(xi t)` reduces to one.  A nonzero `(b-1)`-minor of
`B` remains a nonzero minor of `M_xi` over `K`, so `rank_K M_xi>=b-1`.
The constant vector is already in its kernel by (1.9), proving equality.
\(\square\)

The criterion is valid without singleton signatures.  The simultaneous
transversality theorem makes it especially transparent: away from its
polynomial row leave, `B` is simply the `0-1` biadjacency matrix of the
row--necklace graph.  In that regime the first lift gate has no phase
labels at all; it is the maximal `p`-rank of an `p`-regular bipartite
graph.

### Theorem 19.3 (directed spanning-tree certificate in the singleton case)

Assume a connected component is singleton-signature and choose a perfect
matching between its necklace and row vertices.  Reindex so the matching
is diagonal, and contract its edges.  For every off-diagonal incidence
`O_i--C_j`, put an arc `i -> j`; call the resulting digraph `D`.

Then `D` is strongly connected and Eulerian, with indegree and outdegree
`p-1`.  If `tau(D)` is its number of directed spanning arborescences
rooted at one fixed vertex, then

\[
 \boxed{
 p\nmid\tau(D)
 \quad\Longleftrightarrow\quad
 \operatorname{rank}_{\mathbb F_p}B=b-1
 \quad\Longrightarrow\quad
 \ker_KM_\xi=\langle\mathbf1\rangle\quad(\xi\ne0).}
\tag{19.10}
\]

In fact, if `M_xi^(r)` is any principal cofactor, the directed matrix-tree
theorem gives

\[
 \det M_\xi^{(r)}
 =\sum_{T}\prod_{(i\to j)\in T}\bigl(-M_\xi(i,j)\bigr)
 \equiv(-1)^{b-1}\tau(D)\pmod{\mathfrak p}.
\tag{19.11}
\]

#### Proof

A connected regular bipartite multigraph has a perfect matching.  After
contracting it, the underlying undirected graph is connected.  Each
contracted vertex has `p-1` incoming and `p-1` outgoing arcs.  A weakly
connected Eulerian digraph is strongly connected.

The row sum of `M_xi` is zero, so its diagonal entry is minus the sum of
its off-diagonal entries.  Thus it is the directed Laplacian with arc
weight `-M_xi(i,j)`, and the matrix-tree theorem gives (19.11).  Modulo
`mathfrak p` all singleton weights are one.  The same cofactor is the
arborescence count modulo `p`.  Since both left and right constant vectors
annihilate `B` modulo `p`, rank `b-1` is equivalent to a nonzero cofactor,
which proves (19.10). \(\square\)

Equivalently, edge-color the singleton `p`-regular bipartite component into
perfect matchings and normalize the first matching to the identity.  If
`P_0=I,P_1,...,P_(p-1)` are the resulting permutation matrices, then

\[
                         B=\sum_{a=0}^{p-1}P_a
                         \qquad\hbox{over }{\mathbb F}_p.
\tag{19.11a}
\]

The rank target says that the eigenvalue zero of this permutation sum is
simple.  The inert translate-bundle extreme has the `P_a` equal to the
powers of one regular `p`-cycle; then their sum has rank one.  Thus the
lift gate can also be read as a sharp separation between a generic sum of
`p` matchings and the cyclic group-average degeneration.

This theorem supplies an exact statewise certificate.  It does **not**
supply a useful Archimedean lower singular value: nonvanishing of an
algebraic-integer cofactor controls its `mathfrak p`-adic valuation, while
its complex absolute value may still be exponentially small.  Rigidity and
stable rigidity remain distinct questions.

### 19.1 The orbit-sum form of the same obstruction

Let `w_C` be the middle-packet indicator and work over `F_p`.  Put

\[
                         Q_\sigma=I+\sigma+\cdots+\sigma^{p-1}.
\tag{19.12}
\]

For `x in F_p^F`, the coordinates of
`Q_sigma sum_C x_Cw_C` on the necklace orbits are exactly `Bx`.  Hence

\[
 \boxed{
 Bx=0
 \quad\Longleftrightarrow\quad
 Q_\sigma\Bigl(\sum_Cx_Cw_C\Bigr)=0.}
\tag{19.13}
\]

In characteristic `p`,

\[
                         Q_\sigma=(\sigma-I)^{p-1},
\tag{19.14}
\]

because `X^p-1=(X-1)^p`.  Thus extra `p`-nullity is precisely a nonconstant
signed row deck whose total mass is zero on every coordinate-cycle
necklace.  The rank target (19.7) can equivalently be stated as

\[
 \Bigl\{x:Q_\sigma\sum_Cx_Cw_C=0\Bigr\}=\langle\mathbf1\rangle.
\tag{19.15}
\]

This explains why the condition is plausible for a favorable cycle: the
row-packet space has dimension `W/p`, the orbit-sum target also has
dimension `W/p`, and the one forced intersection is the all-ones deck.
It is an exact reformulation, not a dimension-count proof.

### 19.2 The automatic extra kernels are packet permutations

There is one systematic source of large nullity which must be factored out
before interpreting (19.8).

Call rows `C,D` phase twins if `D=sigma^aC` as middle packets for some
`a`.  In one twin class choose a representative `C_alpha` and distinct
offsets `A_alpha subseteq F_p` so that its rows are
`{sigma^a C_alpha:a in A_alpha}`.  Then

\[
 P_{\sigma^aC_\alpha,O}=P_{C_\alpha,O}+a,
 \qquad
 M_\xi(\,cdot\,,\sigma^aC_\alpha)
 =\zeta^{\xi a}M_\xi(\,\cdot\,,C_\alpha).
\tag{19.16}
\]

Let `bar M_xi` retain one column from every twin class and define

\[
 (R_\xi x)_\alpha=\sum_{a\in A_\alpha}\zeta^{\xi a}x_{\alpha,a}.
\tag{19.17}
\]

Then

\[
 \boxed{
 M_\xi=\bar M_\xi R_\xi,
 \qquad
 \dim\ker M_\xi
 =\sum_\alpha(|A_\alpha|-1)+\dim\ker\bar M_\xi.}
\tag{19.18}
\]

Moreover every permutation `pi_alpha` of `A_alpha` gives the admissible
assignment

\[
 e(\sigma^aC_\alpha)=\pi_\alpha(a)-a.
\tag{19.19}
\]

It merely permutes middle packets already present in the factor and is
therefore vertically inert, as proved in Section 7.

#### Proof

Equation (19.16) follows by translating phases.  Hence the column
factorization is exact.  Each `R_xi` is onto, so rank `M_xi` equals rank
`bar M_xi`, giving (19.18).  Under (19.19), the new packet
`sigma^(a+e)C_alpha` is `sigma^(pi_alpha(a))C_alpha`; the row family is
unchanged. \(\square\)

For a full translate bundle `A_alpha=F_p`, the quotient component is the
complete `p by p` singleton graph, `M_xi` has rank one, and its nullity is
`p-1`.  These are genuine Fourier kernel directions, compatible at every
frequency, but they do no shadow work.  More generally, the relevant
notion of **genuine** lift nullity is `ker bar M_xi` after phase-twin
columns are collapsed.

### 19.3 Exact mean Gram isotropy over prime cycles

The finite-field certificate is statewise.  Averaging the complex gain
matrices over the coordinate cycle gives a complementary exact identity.
It is independent of phase gauges and remains valid when signatures are
not singleton.

Let `B_0=W/p=|F|`, fix `xi ne 0`, and write `M_(sigma,xi)` when the cycle
must be displayed.

### Theorem 19.4 (mean Gram identity)

For a uniformly random coordinate `p`-cycle `sigma`,

\[
 \boxed{
 {\mathbb E}_\sigma\!\left[M_{\sigma,\xi}^*M_{\sigma,\xi}\right]
 =pI-{p^2\over W}J
 =p\left(I-{1\over B_0}J\right).}
\tag{19.20}
\]

Equivalently, for every `x in C^F`,

\[
 \boxed{
 {\mathbb E}_\sigma\|M_{\sigma,\xi}x\|_2^2
 =p\|x-\bar x\mathbf1\|_2^2.}
\tag{19.21}
\]

#### Proof

Changing the chosen phase origin on a necklace multiplies the corresponding
row of `M` by a unit complex number, so its Gram matrix is gauge invariant.
Let `w_C` be the indicator of the `p` middle sets in row `C`.  Expanding
the Gram entry over actual middle sets gives

\[
 (M_{\sigma,\xi}^*M_{\sigma,\xi})(C,D)
 =\sum_{a\in{\mathbb F}_p}\zeta^{\xi a}
   \sum_S w_C(S)w_D(\sigma^aS).
\tag{19.22}
\]

For fixed middle sets `S,T`, put

\[
 K_\xi(S,T)={\mathbb E}_\sigma
 \sum_a\zeta^{\xi a}{\bf1}_{\{\sigma^aS=T\}}.
\tag{19.23}
\]

The term `a=0` is the identity kernel.  For every `a ne 0`, powering by
`a` permutes the conjugacy class of `p`-cycles, while
`sum_(a ne 0)zeta^(xi a)=-1`.  Hence

\[
                         K_\xi=I-\mathcal K_p,
\tag{19.24}
\]

where `mathcal K_p` is the normalized class sum of the `p`-cycles acting
on the middle layer.

On the Johnson decomposition, Murnaghan--Nakayama gives

\[
                         \mathcal K_p=\Pi_0-{1\over p-1}\Pi_1.
\tag{19.25}
\]

Every wreath row contains each coordinate in exactly `m` of its `p`
middle intervals.  Therefore `Pi_1 w_C=0`, while
`Pi_0w_C=(p/W)mathbf1`.  Distinct rows of the exact factor have disjoint
middle supports, so

\[
 \begin{aligned}
 {\mathbb E}_\sigma(M^*M)(C,D)
 &=\langle w_C,(I-\mathcal K_p)w_D\rangle\\
 &=p\,{\bf1}_{\{C=D\}}-{p^2\over W}.
 \end{aligned}
\tag{19.26}
\]

This is (19.20), and its quadratic form is (19.21). \(\square\)

There is a useful Grassmannian interpretation.  Normalize the disjoint
row-packet indicators to obtain an isometric embedding
`J_F:C^(B_0)->C^W`.  Normalize the frequency-`xi` Fourier vector on each
`sigma`-orbit to obtain a `B_0`-dimensional subspace
`A_(sigma,xi) subseteq C^W` and its orthogonal projection
`P_(sigma,xi)`.  Then

\[
 \boxed{
 {1\over p^2}M_{\sigma,\xi}^*M_{\sigma,\xi}
 =J_F^*P_{\sigma,\xi}J_F,
 \qquad
 {\mathbb E}_\sigma J_F^*P_{\sigma,\xi}J_F
 ={1\over p}\left(I-{1\over B_0}J\right).}
\tag{19.26a}
\]

Thus the gain matrices measure the principal angles between the row-packet
space and a Fourier-orbit subspace.  Extra nullity is exactly an extra
intersection of the row-packet space with
`A_(sigma,xi)^perp`.  The family of orbit subspaces is an exact first
Grassmannian design as seen from the row space, but first-design isotropy
does not force one member to be transverse.

The theorem has three immediate consequences.

* No fixed nonconstant row direction belongs to the Fourier kernels for
  every prime cycle.
* The mean squared Frobenius norm is exactly `p(B_0-1)`, entirely on
  `mathbf1^perp`.
* Since the orbit-Fourier map and the disjoint row-packet embedding each
  have norm `sqrt(p)`, one always has `||M_(sigma,xi)||<=p`.  Consequently
  some cycle has rank at least `(B_0-1)/p`.

The same argument gives an exact finite ensemble theorem.

### Corollary 19.4a (a polynomial cycle ensemble is rigid)

For every exact factor and fixed nonzero frequency, there are at most

\[
                         \boxed{L=\lceil p\log B_0\rceil+1=O(p^2)}
\tag{19.26b}
\]

prime coordinate cycles `sigma_1,...,sigma_L` such that

\[
 \boxed{
 \bigcap_{i=1}^L\ker M_{\sigma_i,\xi}=\langle\mathbf1\rangle.}
\tag{19.26c}
\]

#### Proof

Start with `V_0=mathbf1^perp`.  If `V_j` is the common kernel left after
`j` cycles and has dimension `d`, (19.21) gives

\[
 {\mathbb E}_\sigma\|M_{\sigma,\xi}|_{V_j}\|_F^2=pd.
\tag{19.26d}
\]

Choose a cycle attaining at least the mean.  Since its operator norm is at
most `p`, its restriction has rank at least `d/p`.  Therefore the next
common kernel has dimension at most `d(1-1/p)`.  After `L` choices this is
less than one. \(\square\)

This does not replace the required one-cycle lift: the legal action and
the orbit floor are both tied to one cycle.  It does prove that the
exceptional nullity cannot be a representation-theoretic direction shared
by the prime-cycle family; it must track the chosen cycle itself.  Choosing
the ensemble at frequency one makes the same ensemble rigid at every
nonzero frequency, by the Galois identity (19.6a).

The last bound is far short of rigidity.  Equation (19.20) controls a
fixed vector before the cycle is chosen; a cycle-dependent exceptional
kernel can rotate with `sigma` and remain invisible to the first moment.
Thus the exact missing upgrade is either

\[
 \operatorname{rank}_{\mathbb F_p}B_\sigma=B_0-1
 \quad\hbox{for one favorable almost-transversal }\sigma,
\tag{19.27}
\]

or a second-moment/smallest-singular-value theorem which prevents those
exceptional nullspaces from rotating.  Mean isotropy by itself does not
prove either statement.

There is nevertheless an exact sparse-support consequence.

### Proposition 19.5 (a kernel support is a collision-saturated stopping set)

Assume the rows in `S subseteq F` are singleton-signature for `sigma`.
If a nonzero vector in `ker_(F_p)B_sigma` has support exactly `S`, then no
necklace has exactly one neighbor in `S`.  Consequently, writing

\[
 I_\sigma(S)=\sum_O\binom{|N(O)\cap S|}{2},
\tag{19.28}
\]

one has

\[
                         \boxed{I_\sigma(S)\ge {p|S|\over2}.}
\tag{19.29}
\]

For every fixed set `S` of `s` factor rows, a uniformly random prime cycle
satisfies the exact expectation

\[
 \boxed{
 {\mathbb E}_\sigma I_\sigma(S)
 ={p^2(p-1)s^2\over2W}.}
\tag{19.30}
\]

Hence

\[
 \Pr_\sigma[\,S\hbox{ supports a kernel vector and is transversal}\,]
 \le {p(p-1)s\over W}.
\tag{19.31}
\]

#### Proof

At a necklace having one neighbor `C in S`, the equation `(Bx)_O=0`
would read `x_C=0`, a contradiction.  Thus every occupied neighborhood
has size at least two.  Since the `s` columns contain `ps` incidences and
`binom(a,2)>=a/2` for `a>=2`, (19.29) follows.

Let `g_S` be the indicator of the disjoint union of the `s` middle
packets.  Its mass is `ps`, its squared norm is `ps`, and its point degrees
are all `ms`; hence `Pi_1g_S=0`.  If `a_O` is its mass in a `sigma`-orbit,
then

\[
 \sum_Oa_O^2=\sum_{a\in F_p}\langle g_S,\sigma^ag_S\rangle.
\tag{19.32}
\]

Averaging the nonzero powers and using (19.25) gives

\[
 {\mathbb E}_\sigma\sum_Oa_O^2
 =ps+(p-1){(ps)^2\over W}.
\tag{19.33}
\]

Subtract `sum_Oa_O=ps` and divide by two to obtain (19.30).  Markov's
inequality together with (19.29) gives (19.31). \(\square\)

Thus any *fixed* sparse candidate dependence is absent for almost every
cycle.  This still does not permit a union bound over all supports: the
kernel support is chosen after `sigma`, and the number of possible supports
is exponential.  A proof of (19.27) needs a genuinely uniform stopping-set
estimate, not the first moment (19.30).

The inert twin directions themselves disappear for a generic prime cycle.

### Proposition 19.6 (favorable cycles may be chosen phase-twin-free)

For two fixed distinct wreath packets `C,D`,

\[
 \Pr_\sigma[\,D=\sigma^aC\hbox{ for some }a\ne0\,]
 \le {2p(p-1)\over(p-1)!}.
\tag{19.34}
\]

Consequently an exact factor with `B_0=W/p` rows has, with probability
`1-o(1)`, no pair of phase-twin rows at all.  The same cycle can be chosen
both phase-twin-free and with the polynomial simultaneous-transversality
leave of Corollary 3.3.

#### Proof

For fixed `a ne 0`, the map `sigma -> sigma^a` is a bijection of the
conjugacy class of `p`-cycles.  The middle packet determines its coordinate
cyclic order up to rotation and reversal, so its setwise stabilizer in
`S_p` is the dihedral group of order `2p`.  Therefore at most `2p`
coordinate permutations--and hence at most `2p` `p`-cycles--send `C` to
`D`.  Divide by the `(p-1)!` prime cycles and sum over `a ne 0` to get
(19.34).

A union bound over the fewer than `B_0^2/2` row pairs tends to zero, since
`B_0=exp(O(p))` whereas `(p-1)!=exp((1+o(1))p log p)`.  Finally intersect
this probability-`1-o(1)` event with the Markov event underlying
Corollary 3.3. \(\square\)

Thus packet-permutation nullity is an important exact warning and explains
small examples, but it is not forced in the asymptotic favorable-cycle
regime.  Any remaining extra kernel there is genuinely global.

### 19.4 Why the arborescence count does not average from (19.20)

It is tempting to average `tau(D_sigma)` modulo `p` and use a nonzero mean
to obtain (19.27).  The mean Gram identity does not compute that average.
There are two exact reasons.

First, a cofactor is a `(B_0-1)`-st exterior-power matrix coefficient.  If
`U_F` is the span of the row-packet indicators and `R_rho` is the span of
the orbit indicators of one fixed cycle `rho`, then, after choosing
complements to the common all-ones vector, a signed cofactor has the form

\[
 \left\langle
   \bigwedge^{B_0-1}R_\rho,
   \bigwedge^{B_0-1}g^{-1}U_F
 \right\rangle,
 \qquad \sigma=g\rho g^{-1}.
\tag{19.35}
\]

Equation (19.20) is a second-degree identity on the original permutation
module and supplies no control of this exponentially high exterior power.

Second, (19.35) is signed: another conjugator for the same `sigma` may
permute the necklace basis and change its sign.  Over characteristic zero
one can average conjugators and project onto invariant exterior tensors.
Over `F_p`, however, the map

\[
                         g\longmapsto g\rho g^{-1}
\tag{19.36}
\]

has centralizer fibers divisible by `p`.  The conjugator average therefore
cannot be divided down to the cycle average in characteristic `p`.  The
cycle class itself has `(p-1)!` elements, which is invertible modulo `p`,
but it has no canonical signed cofactor without the extra ordering data.

An orientation-free detector is, for example,

\[
                         \tau(D_\sigma)^{p-1}\in{\mathbb F}_p,
\tag{19.37}
\]

which is one exactly when the tree count is nonzero and zero otherwise.
Its degree is `(p-1)(B_0-1)`.  Computing its cycle average is therefore a
new high-degree theorem, not a consequence of the Johnson class-sum or
mean-Gram calculations.  This isolates the precise obstruction to turning
(19.20) directly into maximal rank.

## 20. Revised exact lift gate

The prime-cycle row-power problem now has a two-level certificate.

1. **Phase-free rigidity.**  For a favorable coordinate cycle, prove that
   the multiplicity biadjacency matrix has maximal `p`-rank on every
   component after the inert phase-twin directions are removed.  In the
   singleton core, it is enough to prove `p` does not divide the directed
   arborescence count in (19.10).
2. **Constructive failure of rigidity.**  If the `p`-rank has extra
   nullity, an exponent vector must first lie in that finite-field kernel
   and then satisfy the higher moment equations (19.3), beginning with
   (19.5).  Extra nullity alone is not a legal lift.  A useful construction
   must produce a root-valued Fourier kernel vector not arising from the
   packet permutations (19.19), and its lower deck (9.1) must be
   noninvariant.

Thus the phases have been removed from the first yes/no test.  The precise
unresolved theorem is no longer merely “the quotient graph is connected”:
it is maximal `F_p`-rank, or equivalently a nonzero arborescence count
modulo `p`, for a favorable almost-transversal coordinate cycle.

### Scope warning: exact retile versus partial-packing lift

Sections 19--20 concern **exact support-preserving retiles** of the full
middle factor: the shifted signatures must repartition every phase of every
middle necklace.  If the polynomial exceptional rows of Corollary 3.3 are
deleted and charged to the final `o(W)` leave, the surviving signatures
need only remain pairwise disjoint.  Their occupied phase set is allowed to
change inside the holes left by the deleted rows.  Then `M_xi v_xi(e)=0`
and `Be=0` are no longer necessary equations.

Accordingly, maximal `p`-rank would close the exact row-power-trade route,
but it would not rule out a nearfactor phase packing which uses the
polynomial middle leave as slack.  That partial-packing lift is a different
matching problem and must not be declared rigid from Theorem 19.2.

There is, however, an exact robust-rank reduction for that problem.  Let
`E` be the deleted rows and let

\[
                         H=N(E)
\tag{20.1}
\]

be the middle necklaces incident with at least one deleted row.

### Theorem 20.1 (robust `p`-rank criterion for a partial lift)

Suppose exponents are assigned to the retained rows `F\E` and their shifted
middle packets are pairwise disjoint.  Then

\[
 \boxed{
 B[\mathcal N_m(\sigma)\setminus H,\,F\setminus E]\,e=0
 \quad\hbox{over }{\mathbb F}_p.}
\tag{20.2}
\]

Consequently, if the rectangular matrix in (20.2) has kernel exactly the
constants, every partial row-power lift is a common phase shift on all
retained rows.

#### Proof

An unaffected necklace `O notin H` had no incidence deleted.  It therefore
still has all `p` original occurrences, and a row power never changes the
necklace containing an occurrence--only its phase.  Pairwise disjointness
of the shifted packets makes those `p` occurrences distinct among `p`
available phases, so they repartition the necklace exactly.  Apply the
first moment equation (19.4) at every such `O`. \(\square\)

Since `|H|<=p|E|`, the simultaneous-transversality leave deletes only
polynomially many columns and polynomially many rows of the multiplicity
matrix.  There is an important dimension correction: if `h=|H|` and
`L=|E|`, the matrix in (20.2) has `B_0-h` rows and `B_0-L` columns, while
the constant vector is in its kernel.  Therefore

\[
 \boxed{
 \dim\ker B[\mathcal N_m\setminus H,F\setminus E]
 \ge\max\{1,h-L\}.}
\tag{20.3}
\]

Thus exact rigidity is dimensionally impossible when `h>L+1`, as is
typical when the deleted rows have mostly distinct neighborhoods.  The
correct hereditary target is **maximal rectangular rank**, namely equality
in (20.3).  It compresses all possible first-order phase freedom to at most
`h-L=O(pL)` dimensions, polynomial for the leave of Corollary 3.3.

On every unaffected necklace the full Fourier equation also remains valid:

\[
 M_\xi[\mathcal N_m\setminus H,F\setminus E]v_\xi(e)=0.
\tag{20.4}
\]

The affected necklaces in `H` impose the complementary all-different
constraints on their retained phases.  Hence a useful polynomial-leave
lift must find a root-valued point in the polynomial-dimensional boundary
kernel (20.4) which also passes those injectivity constraints.  The leave
does remove exact rigidity, but only through this explicitly bounded
boundary space; it does not create exponential unconstrained freedom.

## 21. The linear minimal packet and bookkeeping corrections

The simplest singleton component should not be mistaken for useful lift
entropy.  Let a component have rows and necklaces indexed by `F_p`, with
one incidence between every pair, and suppose that after choosing phase
origins its phase array is

\[
                         \phi(i,j)=i+b_j.
\tag{21.1}
\]

This is the complete linear packet.  Its rows are the full translate
bundle of one row.

### Theorem 21.1 (the linear packet has exactly `p!` legal assignments)

An exponent vector `e:F_p -> F_p` is legal on (21.1) if and only if

\[
                         \pi(i):=i+e(i)
\tag{21.2}
\]

is a permutation of `F_p`.  Hence there are exactly `p!` legal exponent
vectors.  Every one merely permutes the `p` existing row packets and has
zero action on the complete lower flag.

#### Proof

At necklace `j`, the shifted phases are
`{b_j+i+e(i):i in F_p}`.  They are all distinct exactly when `pi` is a
permutation, independently of `j`.  The row with new offset `pi(i)` is an
existing translate row.  Lemma 7.2 then gives equality of every lower-rank
packet multiset. \(\square\)

Thus the correct count is `p!`, with no independent-constraint factor such
as `exp(-p)`.  Large legal entropy can be completely inert.

Two bookkeeping points are also load-bearing.

1. If a row count has the form `T=kp-2`, packing `k-1` full linear
   packets leaves `p-2` rows and `p-2` middle necklace classes, not two
   classes.  Since each class contains `p` physical middle sets, the leave
   is `p(p-2)` physical sets.
2. The singleton `p`-regular packet formulation applies to the **entire**
   exact incidence graph only when every signature is singleton.  The
   simultaneous transversality theorem deletes polynomially many bad rows;
   its residual graph is rectangular and nonregular after their neighboring
   necklaces are quarantined, and further pruning may cascade.  Theorem
   20.1, not the regular packet theorem, is the correct interface to that
   leave.  In the special `m=6,n=13` invariant normal form, the two AP loops
   are isolated bad row--class components, so removing them really does
   leave a regular `130 by 130` transversal core.

Finally, quotient connectivity only classifies the **uniform component
phases** of Theorem 7.1.  A connected quotient need not be row-power rigid
without the rank or moment criteria of Section 19: a nonuniform exponent
map is a broader object.  A uniform phase on a component with row family
`A` changes the factor only when `sigma^tA ne A`; it can change a lower
shadow only when the corresponding lower packet is also noninvariant.
The exact `Q_7` factor is nontransversal for the relevant cycle, and its
context-suspension trades are more general than row powers of one fixed
cycle.  Neither is a counterexample to the singleton packet statements.

## 22. Minimal nonlinear singleton packets as Latin odd-cycle arrays

Let `C` be a middle row which is transversal for `sigma`, and order its
middle packet as an odd-graph cycle

\[
                         X_0,X_1,\ldots,X_{p-1},
 \qquad X_t\cap X_{t+1}=\varnothing.
\tag{22.1}
\]

The sets `X_t` lie in distinct `sigma`-necklaces.  Its full translate deck

\[
                         {\cal A}_0=\{\sigma^aC:a\in F_p\}
\tag{22.2}
\]

is the linear packet of Section 21 on the invariant set

\[
                         U=\bigsqcup_{t,a}\{\sigma^aX_t\}.
\tag{22.3}
\]

It is a `C_p`-factor of the induced odd graph `KG(p,m)[U]`.

More generally, any transversal `C_p`-factor of `KG(p,m)[U]` can be encoded by
a `p by p` phase array `Phi=(phi_(i,t))`: column `t` is a permutation of
`F_p`, and the `p` selected vertices

\[
                         \sigma^{\phi_{i,t}}X_t
                         \qquad(t\in F_p)
\tag{22.4}
\]

can be cyclically ordered as a `p`-cycle of the odd graph for every row
`i`.  Conversely every such column-Latin, row-wreath array gives a
transversal packet on `U`.  The packet is `sigma`-invariant exactly when,
after relabeling rows,

\[
                         \phi_{i,t}=i+b_t;
\tag{22.5}
\]

that is, exactly in the linear case.

The next theorem gives a formal two-cut construction criterion, immediately
followed by the odd-graph obstruction which rules it out.

### Theorem 22.1 (two-cut splice criterion)

For `delta ne 0`, call the cut between `X_t` and `X_(t+1)`
`delta`-flexible when

\[
 \boxed{
 X_t\cap\sigma^\delta X_{t+1}=\varnothing,
 \qquad
 X_t\cap\sigma^{-\delta}X_{t+1}=\varnothing.}
\tag{22.6}
\]

If two distinct cuts are `delta`-flexible, then `U` has a transversal
`C_p`-factor `mathcal A` such that

\[
                         \boxed{\sigma\mathcal A\ne\mathcal A.}
\tag{22.7}
\]

Thus `mathcal A` is a minimal nonlinear singleton packet: its uniform
component phase is a genuine exact middle trade rather than a permutation
of existing rows.

#### Proof

Use the two baseline cycles `C` and `sigma^delta C`.  At a flexible cut,
the two old edges

\[
 X_tX_{t+1},
 \qquad
 \sigma^\delta X_t\,\sigma^\delta X_{t+1}
\tag{22.8}
\]

may be replaced by the cross edges

\[
 X_t\,\sigma^\delta X_{t+1},
 \qquad
 \sigma^\delta X_t\,X_{t+1};
\tag{22.9}
\]

their disjointness is exactly (22.6).  Perform this replacement at two
cuts.  Equivalently, exchange the two row segments between those cuts.
The result is two simple odd-graph cycles, each with exactly `p` vertices;
every `p`-cycle of `KG(p,m)` is a wreath.  All other translate rows are left
unchanged.  No vertex of `U` has been added or removed, and each new cycle
uses one vertex from every necklace column, so the new rows form a
transversal factor of `U`.

The new family differs from `mathcal A_0` but still contains the `p-2`
untouched translate rows.  If it were `sigma`-invariant, the presence of
one untouched translate row would force it to contain that row's full
`sigma`-orbit, namely all of `mathcal A_0`; this is impossible after the
nontrivial splice.  Hence (22.7). \(\square\)

The criterion is exact, but the odd graph forbids its hypothesis.

### Proposition 22.2 (no two-row splice)

No cut is `delta`-flexible for any `delta ne 0`.  Consequently a nonlinear
singleton packet cannot be obtained by rerouting only two translate rows;
any such packet must use at least three rows at once.

#### Proof

Put `A=X_t`, `B=X_(t+1)`, and `tau=sigma^delta`.  The old edge gives
`A cap B=emptyset`, so `Y=A^c` has size `m+1` and contains `B`.
The two cross-edge conditions (22.6) say

\[
                         \tau B\subseteq Y,
 \qquad
                         \tau^{-1}B\subseteq Y.
\tag{22.13}
\]

Thus `B,tau B,tau^(-1)B` are three `m`-subsets of one `(m+1)`-set.
Since the nontrivial `p`-cycle `tau` fixes no proper nonempty set,
`|B cap tau B|=m-1`.  Reading the indicator of `B` around the `tau`-cycle,
exactly one element exits under a shift, so `B` is one cyclic block.
Its forward and backward shifts adjoin its two distinct boundary elements.
Therefore

\[
                         |B\cup\tau B\cup\tau^{-1}B|=m+2,
\tag{22.14}
\]

contradicting containment in `Y`. \(\square\)

Equivalently, the proposed rerouting would be a `4`-cycle made from two old
and two crossed edges, and the odd graph has no such local rectangle.

The same argument determines the whole phase-difference graph at one cut.

### Theorem 22.3 (synchronized-column packets are always linear)

For one old edge `A=X_t`, `B=X_(t+1)`, put

\[
                         D(A,B)=\{d:A\cap\sigma^dB=\varnothing\}.
\tag{22.15}
\]

Then

\[
                         \boxed{|D(A,B)|\le2.}
\tag{22.16}
\]

More precisely, `0 in D(A,B)`, and there is at most one nonzero element.
The only perfect matchings between the two phase copies of `A` and `B`
are therefore the identity matching and, when it exists, the one global
translation matching.

Consequently, any column-Latin packet in which every row visits the
necklace columns in the common order

\[
                         0,1,\ldots,p-1
\tag{22.17}
\]

has, after relabeling its rows,

\[
                         \phi_{i,t}=i+b_t.
\tag{22.18}
\]

It is a linear translate bundle and is vertically inert.  A nonlinear
singleton packet must use row-dependent cyclic orders of the necklace
columns.

#### Proof

As in Proposition 22.2, every nonzero `d in D(A,B)` makes both `B` and
`sigma^dB` into `m`-subsets of the `(m+1)`-set `A^c`.  Hence
`|B cap sigma^dB|=m-1`, and the binary indicator of `B` is one cyclic
interval in the `sigma^d` order.

If distinct nonzero `d,e` both lie in `D(A,B)`, the same set `B` is an
arithmetic-progression interval of length `m` with steps `d` and `e`.
After scaling `d=1`, the overlap of `[0,m-1]` with its translate by `e`
has size `m-1`; because `p=2m+1`, this forces `e=1` or `e=-1`.
The latter simultaneous pair is impossible by Proposition 22.2.  This
proves (22.16).

The phase bipartite graph is thus the union of the identity matching and
possibly `a -> a+d`.  A perfect matching using the shifted edge precisely
on a subset `S` of phases has image

\[
                         (F_p\setminus S)\cup(S+d).
\tag{22.19}
\]

It is a permutation only when `S+d=S`; primeness makes `S` empty or all
of `F_p`.  Hence each column transition is a global translation.  If
`pi_t` is the phase permutation in column `t`, then
`pi_(t+1)=T_(d_t)pi_t`.  Relabel by `pi_0` and sum the translations to get
(22.18). \(\square\)

### Difference-set form

For two necklace representatives `X_s,X_t`, define

\[
 D_{s,t}=\{d\in F_p:X_s\cap\sigma^dX_t=\varnothing\}.
\tag{22.10}
\]

In the synchronized-column subclass of (22.4), write the phase in column
`t` as a permutation `pi_t(i)`.  The row edges between consecutive columns
are legal exactly when

\[
 \pi_{t+1}(i)-\pi_t(i)\in D_{t,t+1}
 \qquad\hbox{for every }i.
\tag{22.11}
\]

Thus each transition is a perfect matching in a bipartite circulant graph.
The linear packet uses translation matchings.  A formally necessary
condition for a two-transition switch would be that one nonzero `delta`
satisfy

\[
 \pm\delta\in D_{t,t+1}
 \quad\hbox{at two cuts},
\tag{22.12}
\]

after normalizing the old transition differences to zero, but Proposition
22.2 shows that the paired cross edges at even one cut are impossible.

Therefore the first live nonlinear object is stronger than merely a
three-row splice.  It must change the order in which at least some rows
visit the necklace classes, producing a genuinely two-dimensional Latin
odd-cycle array.  This agrees with the abstract three-phase gate of
Sections 2--6 but rules out its synchronized one-dimensional realization.
Conversely, if the induced odd graph on `U` has no cross edges between
distinct translate cycles, the linear packet is its unique transversal
`C_p`-factor and all `p!` legal assignments of Theorem 21.1 are inert.

Nor can one obtain the nonlinear packet by partially mixing two invariant
linear factorizations of the same `U`.

### Proposition 22.4 (two invariant packets have connected overlay)

Let

\[
 \mathcal A=\{\sigma^aC:a\in F_p\},
 \qquad
 \mathcal A'=\{\sigma^bD:b\in F_p\}
\tag{22.20}
\]

be two transversal translate-deck factorizations of the same `U`.  Form
their bipartite ownership overlay, with one edge for every middle set of
`U`.  If `mathcal A ne mathcal A'`, this overlay is connected.  Hence
component switching between two invariant packets chooses all of
`mathcal A` or all of `mathcal A'`; it produces no nonlinear mixed packet.

#### Proof

Put

\[
 S=\{d\in F_p:\mathcal W_m(C)\cap
                 \mathcal W_m(\sigma^dD)\ne\varnothing\}.
\tag{22.21}
\]

Translation invariance makes the row-overlap graph the bipartite Cayley
multigraph with an edge from `a` to `b` precisely at differences
`b-a in S`, with the corresponding intersection multiplicity.  Its
components are the cosets of the subgroup generated by `S-S`.  Since `p`
is prime, it is connected whenever `|S|>=2`.

If `S={d}`, every row has all `p` of its vertices in the one opposite row
at difference `d`; hence `C=sigma^dD` as middle packets and the two row
families are identical.  Thus distinct factors have `|S|>=2` and connected
overlay. \(\square\)

The quotient odd graph itself has only one voltage on every edge between
distinct necklace classes.

### Proposition 22.5 (unique-voltage quotient edges)

For middle sets `A,B`, let

\[
                         D(A,B)=\{d:A\cap\sigma^dB=\varnothing\}.
\tag{22.22}
\]

If `A` and `B` lie in distinct `sigma`-necklaces, then

\[
                         \boxed{|D(A,B)|\le1.}
\tag{22.23}
\]

If two disjointness voltages occur, both sets are arithmetic-progression
intervals with the same step up to sign and hence lie in the same AP
necklace.

#### Proof

Identify the coordinate cycle with the additive group `F_p`.  The
disjointness condition is

\[
                         d\notin A-B,
\tag{22.24}
\]

up to reversing the sign convention.  Cauchy--Davenport gives

\[
                         |A-B|\ge2m-1=p-2.
\tag{22.25}
\]

If at least two voltages are missing from `A-B`, equality holds in
(22.25).  Vosper's equality theorem makes `A` and `-B` arithmetic
progressions with one common step.  Thus `A` and `B` have the same step up
to sign, so one is a coordinate translate of the other and their
`sigma`-necklaces agree. \(\square\)

After deleting the AP loop classes, the coordinate-cycle quotient of the
odd graph is therefore a simple voltage graph: every quotient edge lifts
to one perfect matching between its two necklace fibers.  A transversal
wreath projects to a zero-voltage Hamilton cycle of this quotient graph.
The unresolved nonlinear packet is equivalently a `C_p`-factor of the
`p`-fold voltage cover which mixes different projected Hamilton cycles;
Theorems 22.3--22.4 show that neither one common projected cycle nor a
two-factor component mix can produce it.

There is also a small cycle-space obstruction in the quotient.

### Proposition 22.6 (a nonlinear minimal packet needs two quotient chords)

Let `Gamma` be the simple quotient graph induced by the `p` necklace
classes of a transversal row, and let `H` be its projected Hamilton cycle.
For any transversal `C_p`-factor of the voltage lift, let `x_e` be the
number of factor rows whose projected Hamilton cycle uses `e`.  Then

\[
 \boxed{
 \sum_{e\ni v}x_e=2p
 \quad(v\in V(\Gamma)),
 \qquad
 (x_e\bmod p)_{e\in E(\Gamma)}\in
 \ker_{\mathbb F_p}I_\Gamma,}
\tag{22.26}
\]

where `I_Gamma` is the unsigned vertex--edge incidence matrix.  Since
`Gamma` contains the odd Hamilton cycle `H`,

\[
 \boxed{
 \dim\ker_{\mathbb F_p}I_\Gamma=|E(\Gamma)|-p.}
\tag{22.27}
\]

If `Gamma=H`, every edge is used either zero or `p` times and the packet is
linear.  If `Gamma` is `H` plus one chord, `H` is still its unique
Hamilton cycle.  Hence a nonlinear minimal packet requires at least two
quotient edges outside `H`.

#### Proof

Every one of the `p` projected row cycles enters and leaves each quotient
vertex once, giving the degree equation in (22.26); reduction modulo `p`
gives the kernel statement.  Over a field of odd characteristic, the
unsigned incidence matrix of a connected nonbipartite graph has full row
rank.  Here `H` is odd, so its rank is `p`, proving (22.27).

When `Gamma=H`, (22.27) makes every `x_e` zero modulo `p`; since
`0<=x_e<=p`, each is zero or `p`, and the degree equations select the full
Hamilton cycle.  If one chord is added, any cycle using it consists of the
chord and one of the two proper arcs of `H`, so it omits the internal
vertices of the other arc.  It is not Hamiltonian.  Thus `H` remains the
unique projected Hamilton cycle, and the packet is again its full linear
lift. \(\square\)

### Corollary 22.7 (three projected Hamilton cycles are necessary)

A nonlinear transversal packet uses at least three distinct zero-voltage
Hamilton cycles of `Gamma` among its projected rows.

#### Proof

If all rows project to one Hamilton cycle, they form its full linear lift.
If they project to two cycles `H,H'`, every row belongs to one of the two
invariant lift factors.  Exact middle coverage would select a mixture of
rows from those two factors.  Proposition 22.4 says their ownership overlay
is connected unless the factors coincide, so component switching permits
only all rows from one factor or all rows from the other. \(\square\)

## 23. Cross-phase anomalies are confined to polynomially many rows

The Johnson class kernel gives an exact count which nearly eliminates the
minimal nonlinear packet from the asymptotic lift.

### Lemma 23.1 (disjoint image under a random prime cycle)

For fixed middle sets `A,B` and a uniformly random coordinate `p`-cycle
`tau`,

\[
 \boxed{
 \Pr[\tau B\cap A=\varnothing]
 ={p(1+|A\cap B|)\over W(m+1)}
 \le {p\over W}.}
\tag{23.1}
\]

#### Proof

Let `mathcal D_A` be the `m+1` middle sets disjoint from `A`.  By (19.25),

\[
 \Pr[\tau B\in\mathcal D_A]
 =\langle\mathbf1_{\mathcal D_A},
          (\Pi_0-(p-1)^{-1}\Pi_1)\mathbf e_B\rangle.
\tag{23.2}
\]

The degree-one Johnson projection kernel is

\[
 \Pi_1(S,B)
 ={|S\cap B|-m^2/p\over\binom{p-2}{m-1}}.
\tag{23.3}
\]

If `r=|A cap B|`, every element of `A^c cap B` belongs to `m` members of
`mathcal D_A`, so

\[
 \sum_{S\in\mathcal D_A}|S\cap B|=m(m-r).
\tag{23.4}
\]

Substitute (23.3)--(23.4), use
`W/binom(p-2,m-1)=2p/(m+1)`, and simplify.  This gives the equality in
(23.1); its maximum occurs at `r=m`. \(\square\)

For a row `C`, retain the odd-cycle order (22.1) and define its oriented
cross-phase anomaly count

\[
 A_\sigma(C)=
 \#\{(t,s,d):t,s\in F_p,\ d\in F_p^*,\
                 X_t\cap\sigma^dX_s=\varnothing\}.
\tag{23.5}
\]

### Theorem 23.2 (polynomial anomaly theorem)

For one fixed row,

\[
 \boxed{
 {\mathbb E}_\sigma A_\sigma(C)
 ={p^2(p-1)(p+m^2)\over W(m+1)}
 =O(p^4/W).}
\tag{23.6}
\]

For an exact factor,

\[
 \boxed{
 {\mathbb E}_\sigma\sum_{C\in F}A_\sigma(C)
 ={p(p-1)(p+m^2)\over m+1}=O(p^3).}
\tag{23.7}
\]

Consequently one prime cycle has only `O(p^3)` rows with a cross-phase
anomaly.  It may be chosen simultaneously with the polynomial
simultaneous-transversality bounds of Corollary 3.3.

#### Proof

For each fixed nonzero `d`, `sigma^d` is again a uniform prime cycle.
Apply Lemma 23.1 to every ordered pair `(X_t,X_s)`.  The wreath point
degrees give

\[
 \sum_{t,s}|X_t\cap X_s|
 =\sum_{x\in[p]}\#\{t:x\in X_t\}^2=pm^2.
\tag{23.8}
\]

Thus `sum_(t,s)(1+|X_t cap X_s|)=p^2+pm^2`; multiplying by the coefficient
in (23.1) and by `p-1` proves (23.6).  Multiply by `|F|=W/p` to obtain
(23.7).  Finally average a positive linear combination of this functional
and the transversality functionals. \(\square\)

### Corollary 23.3 (no useful minimal packet off a polynomial leave)

Call a row clean when it is middle-transversal and `A_sigma(C)=0`.  For a
clean row `C`, the induced odd graph on the `p^2` sets in its necklace
support `U_C` is exactly

\[
                         \bigsqcup_{a\in F_p}\sigma^aC.
\tag{23.9}
\]

In particular it has a unique transversal `C_p`-factor, the inert linear
packet.  Hence every useful nonlinear singleton component having exactly
`p` rows and `p` necklaces contains an anomalous row.  Deleting `O(p^3)`
rows removes all such minimal components at middle cost `O(p^4)=o(W)`.

#### Proof

Every edge between two vertices of `U_C` has the form

\[
                         \sigma^aX_t\ --\ \sigma^bX_s.
\tag{23.10}
\]

Translate by `sigma^(-a)`.  If `b-a ne0`, it is counted by (23.5), so
cleanliness forbids it.  If `b-a=0`, two middle windows of one wreath row
are disjoint exactly when they are consecutive in its recovered odd-cycle
order.  Thus (23.9) contains all and only the displayed translate-cycle
edges.

A singleton component with `p` row and `p` necklace vertices is complete
bipartite at the quotient level; every one of its rows touches every one
of its necklaces.  Taking any clean row in it identifies its entire
support with `U_C`, where (23.9) makes the translate deck the unique cycle
factor.  Therefore a useful component must contain a dirty row.  Theorem
23.2 and Corollary 3.3 bound all dirty rows polynomially. \(\square\)

This closes the smallest nonlinear singleton-packet route asymptotically.
Any useful prime-cycle lift surviving the polynomial leave must use a
component with more than `p` rows, or exploit the rectangular boundary
freedom of Theorem 20.1 rather than a minimal exact packet.

The anomaly theorem cannot be extended to a size-proportional charge on
all larger noninvariant components.

### Proposition 23.4 (no component-size anomaly charge)

There are favorable cycles which are simultaneously phase-twin-free and
have only `O(p^3)` anomalous rows.  For any such cycle, all but `O(p)`
factor rows lie in quotient components whose row families `A_K` satisfy

\[
                         \sigma A_K\ne A_K.
\tag{23.11}
\]

Consequently no universal inequality of the form

\[
 \#\{\hbox{anomalies in }K\}\ge c\,{|A_K|\over p}
\tag{23.12}
\]

can hold for all noninvariant components.

#### Proof

Choose the common favorable cycle from Proposition 19.6 and Theorem 23.2.
If `sigma A_K=A_K`, the cyclic group permutes the rows in `A_K`.  Every
nonfixed row then belongs to a full translate orbit and has phase twins in
the same factor, contrary to Proposition 19.6.  The only fixed wreath rows
are the arithmetic-progression rows of Section 14, of which there are only
`m=O(p)`.  Thus the remaining `B_0-O(p)` rows satisfy (23.11).  Summing
(23.12) would force exponentially many anomalies, contradicting the
`O(p^3)` total. \(\square\)

Noninvariance alone is not balancing power: a giant component supplies
only one global relabeling and preserves every relabeling-invariant defect.
Thus Section 23 removes minimal nonlinear packets but does not replace the
separate fragmentation requirement of Theorem 15.1.

## 24. A fixed quotient cut is invariant with probability at most `1/p`

The first-moment fragmentation statement can be made exact, although it is
not uniform over the exponentially many possible cuts.

### Proposition 24.1 (fixed-cut bound)

Fix a nonempty proper row subfamily `A subset F`, of size `s`, and put

\[
                         U(A)=\bigsqcup_{C\in A}\mathcal W_m(C).
\tag{24.1}
\]

For a uniformly random prime coordinate cycle,

\[
 \boxed{
 \Pr_\sigma[\,\sigma U(A)=U(A)\,]\le {1\over p}.}
\tag{24.2}
\]

#### Proof

Let `g=mathbf1_(U(A))` and center it as

\[
                         z=g-{s\over B_0}\mathbf1.
\tag{24.3}
\]

Every wreath row has constant point degrees, so `Pi_1z=0`; centering gives
`Pi_0z=0`.  Let

\[
                         P_\sigma={1\over p}
                         (I+\sigma+\cdots+\sigma^{p-1})
\tag{24.4}
\]

be orthogonal projection onto the necklace-constant functions.  Averaging
the nonzero powers and using (19.25) yields

\[
 {\mathbb E}_\sigma\|P_\sigma z\|_2^2
 =\langle z,{\mathbb E}P_\sigma z\rangle
 ={1\over p}\|z\|_2^2.
\tag{24.5}
\]

If `U(A)` is invariant, then `P_sigma z=z`.  Since projection cannot
increase norm, its squared norm divided by `||z||^2` lies in `[0,1]` and
dominates the event indicator.  Taking expectations proves (24.2).
\(\square\)

By Theorem 7.1, a proper quotient component supplies such an invariant
cut.  Proposition 24.1 shows that no *prescribed* cut persists for many
cycles.  It does not prove connectivity: the component cut is selected
after seeing `sigma`, and a union bound over `2^(B_0)` row families is
impossible.  The missing fragmentation theorem is therefore a genuine
high-moment or stabilizer-count statement, separate from the fixed-cut
Johnson calculation.

## 25. Exact `p`-rank of near-minimal singleton components

The finite-field criterion becomes completely explicit for components only
slightly larger than the degree.  Let a singleton component have `b=p+q`
rows and necklaces, where `1<=q<p`.  Its `p`-regular biadjacency matrix can
be written

\[
                         B=J-C,
\tag{25.1}
\]

where `C` is the `q`-regular `0-1` biadjacency matrix of the complement
inside `K_(b,b)`.

### Theorem 25.1 (complement-kernel formula)

Over `F_p`,

\[
 \boxed{
 \ker B=\langle\mathbf1\rangle\oplus\ker C.}
\tag{25.2}
\]

In particular the component is row-power rigid whenever `C` is
nonsingular.

#### Proof

If `Bx=0` and `s=sum_i x_i`, then `Cx=s\mathbf1`.  Since
`C\mathbf1=q\mathbf1` and `q ne0` in `F_p`, put
`y=x-(s/q)mathbf1`.  Then `Cy=0`.  Conversely every vector in `ker C`
has coordinate sum zero, because

\[
                         q\sum_i y_i
 =\mathbf1^TCy=0,
\tag{25.3}
\]

and hence `Jy=0`, so `By=0`.  Constants are in `ker B` because every row
sum is `p=0`.  The sum in (25.2) is direct since `Cmathbf1 ne0`.
\(\square\)

### Corollary 25.2 (sizes `p+1` and `p+2`)

1. Every singleton component with `p+1` rows is rigid: its complement is
   one perfect matching, so `C` is a permutation matrix.
2. For a component with `p+2` rows, choose one of the two complementary
   perfect matchings as the identity and write

   \[
                            C=I+P.
   \tag{25.4}
   \]

   Then

   \[
    \boxed{
    \dim\ker B-1
    =\#\{\hbox{even cycles of the permutation }P\}.}
   \tag{25.5}
   \]

   Equivalently, extra first-order nullity occurs exactly on the alternating
   complement cycles whose bipartite length is divisible by four.

#### Proof

The first statement is immediate from Theorem 25.1.  For the second,
`(I+P)y=0` says that values alternate in sign around every cycle of `P`.
An odd cycle forces zero; an even cycle supplies one free alternating
value. \(\square\)

Thus, after the inert `p by p` translate packet, the `p+1` case admits no
nonuniform exact row-power assignment at all.  The first component size
where the linear obstruction can fail is `p+2`, and its failure is already
localized to explicit alternating complement cycles.  Passing (25.5) is
only the first derivative: a legal exponent map must still satisfy the
higher phase-moment equations (19.3), so an even complement cycle is a
candidate direction rather than a completed lift.

The rigidity of the `p+1` case is favorable for component phases.

### Corollary 25.3 (a `p+1` component is automatically middle-nontrivial)

Let `A_K` be the row family of a singleton quotient component with `p+1`
rows.  Then

\[
                         \boxed{\sigma A_K\ne A_K.}
\tag{25.6}
\]

Its only exact row-power assignments are the `p` common component phases,
and every nonzero one changes the middle row factor on its invariant
support.

#### Proof

Corollary 25.2 gives the row-power rigidity.  If `sigma A_K=A_K`, the
order-`p` action on `p+1` rows decomposes into one orbit of size `p` and
one fixed row.  A `sigma`-fixed wreath packet is an arithmetic-progression
row by Section 14, and all of its middle sets lie in one necklace.  That
contradicts singleton incidence. \(\square\)

This suggests a concrete positive atom.  Start from the disjoint union of

* one inert linear packet on `p` rows and `p` necklaces, and
* one AP loop row on one AP necklace.

The combined multiplicity pattern is `K_(p,p)` plus one multiplicity-`p`
loop.  A **loop desingularization trade** would repartition the same
`p(p+1)` middle sets into `p+1` wreath rows with incidence

\[
                         K_{p+1,p+1}\setminus M,
\tag{25.7}
\]

where `M` is a perfect matching: one new row misses the AP necklace, and
each of the other `p` rows uses one AP phase while missing a different old
necklace.  By Corollary 25.3 the result would be a rigid but genuinely
movable component-phase atom.  Constructing (25.7) with actual wreath rows,
and then packing many disjoint copies, is a sharply specified alternative
to the now-closed nonlinear `p`-packet route.

The AP class has a severe quotient-degree restriction.

### Proposition 25.4 (AP-center degree obstruction)

In the coordinate-cycle quotient of the odd graph, an AP necklace has one
internal cycle loop, contributing two to its physical degree, and exactly
`m-1` simple neighbors outside that necklace.  In particular it cannot be
the center of a wheel joined to all `p` old necklace vertices.

#### Proof

Fix one AP middle set `A`.  It has `m+1` disjoint middle neighbors.  The
two endpoint deletions from the `(m+1)`-set `A^c` are the forward and
backward AP translates and give the two edges of the internal lifted loop.
Each of the remaining `m-1` neighbors lies in a distinct necklace: two in
one non-AP necklace would give two disjointness voltages between distinct
necklace classes, contradicting Proposition 22.5. \(\square\)

Thus `p+1` remains the correct smallest potentially useful component size,
but a loop desingularization cannot be the naive AP-center wheel.  Its `p`
new rows containing AP phases must reuse the `m-1` available external
necklace neighbors in a richer quotient Hamilton geometry, with additional
outer chords supplying the different omitted-vertex cycles.

## 26. Frequency zero and the partial-orbit selection gate

A broader construction may select several or no translates of one original
row rather than exactly one.  Introduce variables

\[
                         x_{C,j}\in\{0,1\},
 \qquad C\in F,\ j\in F_p,
\tag{26.1}
\]

and put

\[
 r_C=\sum_jx_{C,j},
 \qquad
 y_{\xi,C}=\sum_jx_{C,j}\zeta^{\xi j}.
\tag{26.2}
\]

### Theorem 26.1 (complete Fourier system for a translate selection)

If the selected translated packets form an exact middle factor, then

\[
 \boxed{
 Br=p\mathbf1=B\mathbf1,
 \qquad
 M_\xi y_\xi=0\quad(\xi\ne0).}
\tag{26.3}
\]

Conversely (26.3), together with (26.1), is sufficient for exact middle
ownership.  In particular, if `B` is nonsingular over `R`, then

\[
                         r=\mathbf1,
\tag{26.4}
\]

so exactly one translate of every old row is selected and the route reduces
to the row-power phase lift of Section 1.

#### Proof

At necklace `O`, the phase-summed number of selected occurrences is
`sum_C B(O,C)r_C`.  Exact ownership makes it `p`, giving the frequency-zero
equation.  At nonzero frequency, translating copy `j` multiplies its old
Fourier signature by `zeta^(xi j)`, giving the second equation.  Fourier
inversion proves sufficiency.  If `B` is real-nonsingular, subtract
`Bmathbf1=pmathbf1` from the first equation to get (26.4). \(\square\)

Thus ordinary real nullity, not modular nullity, is the first gate for the
partial-orbit lane.  A real kernel merely supplies possible multiplicity
changes `r-1`; the root-of-unity equations and the `0-1` realization in
(26.1) remain additional constraints.

### Theorem 26.2 (exact mean Gram identity at frequency zero)

For a uniformly random prime coordinate cycle,

\[
 \boxed{
 {\mathbb E}_\sigma[B_\sigma^*B_\sigma]
 =pI+{p^2(p-1)\over W}J.}
\tag{26.5}
\]

Equivalently,

\[
 {\mathbb E}_\sigma\|B_\sigma x\|_2^2
 =p\|x\|_2^2+{p^2(p-1)\over W}
                    \left|\sum_Cx_C\right|^2.
\tag{26.6}
\]

#### Proof

The Gram entry is the common-necklace count

\[
 (B_\sigma^*B_\sigma)(C,D)
 =\langle w_C,Q_\sigma w_D\rangle,
 \qquad Q_\sigma=I+\cdots+\sigma^{p-1}.
\tag{26.7}
\]

Averaging the nonzero powers gives
`E Q_sigma=I+(p-1)mathcal K_p`.  Every row indicator has zero degree-one
Johnson component, distinct factor rows have disjoint support, and
`<w_C,Pi_0w_D>=p^2/W`.  Therefore the diagonal entry is
`p+p^2(p-1)/W` and every off-diagonal entry is
`p^2(p-1)/W`, proving (26.5). \(\square\)

The mean is positive definite: its eigenvalue is `p^2` on constants and
`p` on `mathbf1^perp`.  Nevertheless, first-moment isotropy does not force
one `B_sigma` to be nonsingular; cycle-dependent real kernels can rotate in
the same way as the exceptional Fourier kernels of Section 19.3.  A proof
that one favorable cycle has `det B_sigma ne0`, or a structural
classification of its real nullity, is the exact remaining partial-orbit
gate.

## 27. The exact determinant congruence at frequency zero

The frequency-zero matrix has substantially more arithmetic structure than
an arbitrary square integer matrix.  The following statements apply to any

\[
 B\in M_T(\mathbb Z),\qquad
 B\mathbf1=p\mathbf1,\qquad
 \mathbf1^TB=p\mathbf1^T,
 \tag{27.1}
\]

where `p` is prime and `p` does not divide `T`.  In the prime-cycle problem
`T=C_m` and

\[
                 C_m\equiv(-1)^m2\pmod p,
\tag{27.2}
\]

so the last hypothesis is automatic.

### Theorem 27.1 (the forced `p`-adic block and the sharp rank criterion)

Let

\[
 H=\{x\in\mathbb Z_{(p)}^T:\mathbf1^Tx=0\}.
\tag{27.3}
\]

Then

\[
 \mathbb Z_{(p)}^T=\mathbb Z_{(p)}\mathbf1\oplus H,
 \qquad
 B=p\oplus B_H,
\tag{27.4}
\]

and consequently

\[
 \boxed{\det B=p\det B_H.}
\tag{27.5}
\]

If `r=rank_{F_p}(B mod p)`, then, whenever `det B ne0`,

\[
                 v_p(\det B)\ge T-r.
\tag{27.6}
\]

Moreover the following are equivalent:

\[
 \boxed{
 \operatorname{rank}_{\mathbb F_p}(B)=T-1
 \iff {\det B\over p}\not\equiv0\pmod p
 \iff v_p(\det B)=1.}
\tag{27.7}
\]

In particular, maximal possible rank modulo `p` is a sufficient certificate
that `B` is nonsingular over `R`.

The same splitting identifies the localized cokernel, without losing any
`p`-primary information:

\[
 \operatorname{coker}(B)_{(p)}
 \cong \mathbb Z/p\mathbb Z\oplus\operatorname{coker}(B_H).
\]

Thus one `p`-primary invariant factor is forced by the constant line; every
additional factor of `p` in the determinant comes from the zero-sum block.

#### Proof

Because `T` is a unit in `Z_(p)`, the projection `T^{-1}J` splits off the
constant line.  The two equations (27.1) say that `B` commutes with this
projection, acts by `p` on the constant line, and preserves `H`.  This proves
(27.4)--(27.5) and the displayed cokernel decomposition.  Modulo `p` the
constant block is zero and the other block is
`B_H mod p`; hence `rank(B mod p)=rank(B_H mod p)`.  The Smith form of
`B_H` shows that its determinant contains at least one factor `p` for every
dimension of its mod-`p` kernel, proving (27.6).  Equality of the three
conditions in (27.7) follows immediately. \(\square\)

The converse to the last sentence is false in general: a real-nonsingular
matrix can have smaller mod-`p` rank, in which case its determinant is
divisible by `p^2`.  Thus the modular criterion is sharp as a certificate,
not as a characterization of real nonsingularity.

### Theorem 27.2 (exact rooted-forest expansion)

Fix an identification of the row and column indices and put

\[
                         L=pI-B.
\tag{27.8}
\]

If `B` is nonnegative, `L` is the Laplacian of an Eulerian directed
multigraph (loops in `B` are ignored by the Laplacian).  For `1<=k<=T`, let

\[
 F_k=\sum_{|S|=T-k}\det L[S,S].
\tag{27.9}
\]

By the all-minors matrix-tree theorem, `F_k` is the total number of rooted
directed spanning forests with `k` roots.  In particular,

\[
                         F_1=T\tau,
\tag{27.10}
\]

where `tau` is the common number of spanning arborescences rooted at a
specified vertex (and is zero when the directed graph is not connected).
Then the following is an exact integer identity:

\[
 \boxed{
 {\det B\over p}
   =\sum_{k=1}^{T}(-1)^{T-k}F_kp^{k-1}.}
\tag{27.11}
\]

Consequently, for every `a>=1`,

\[
 {\det B\over p}
 \equiv\sum_{k=1}^{a}(-1)^{T-k}F_kp^{k-1}\pmod {p^a},
\tag{27.12}
\]

with terms having `k>T` omitted.  The first and most useful case is

\[
 \boxed{
 {\det B\over p}\equiv(-1)^{T-1}T\tau\pmod p.}
\tag{27.13}
\]

#### Proof

Principal-minor expansion gives

\[
 \det(tI-L)=\sum_{k=1}^{T}(-1)^{T-k}F_kt^k;
\tag{27.14}
\]

there is no constant term because `Lmathbf1=0`.  Substitute `t=p` and use
`pI-L=B`. \(\square\)

Thus strong connectivity, which only says `tau>0`, is not enough for the
modular certificate: the exact condition is `p notmid tau`.  Also, real
singularity of `B` is an alternating cancellation among all the forest
numbers in (27.11), not the absence of spanning trees.

### Corollary 27.3 (cofactors, arborescences, and rank are the same mod `p`)

Let `C_ij(B)` denote a signed cofactor.  Then every signed cofactor has the
same residue modulo `p`, and

\[
 \boxed{
 C_{ij}(B)
 \equiv(-1)^{T-1}\tau
 \equiv T^{-1}{\det B\over p}\pmod p.}
\tag{27.15}
\]

Equivalently,

\[
 \operatorname{adj}(B)
 \equiv(-1)^{T-1}\tau J\pmod p.
\tag{27.16}
\]

Hence

\[
 \boxed{
 \operatorname{rank}_{\mathbb F_p}(B)=T-1
 \iff p\nmid\tau
 \iff C_{ij}(B)\not\equiv0\pmod p.}
\tag{27.17}
\]

When the directed graph is strongly connected, `tau` is the order of its
Eulerian critical group.  Thus (27.17) is equivalently the assertion that
this critical group has no `p`-torsion.

#### Proof

The Eulerian Laplacian has

\[
                         \operatorname{adj}(L)=\tau J
\tag{27.18}
\]

(both sides are zero if the rank is below `T-1`).  Since `B=-L mod p`,
adjugates scale by `(-1)^(T-1)`, proving the first congruence in (27.15) and
(27.16).  Equation (27.13), together with `p notmid T`, proves the second.
The equivalences follow either from (27.7) or from the standard cofactor
criterion for rank `T-1`. \(\square\)

There is also an exact, denominator-free centered-cofactor identity.  Put

\[
                         A=TB-pJ.
\tag{27.19}
\]

Then `A` has zero row and column sums and

\[
 \boxed{
 \operatorname{adj}(A)
   =T^{T-2}{\det B\over p}\,J.}
\tag{27.20}
\]

Indeed, on `H` the map `A` is `TB_H`, while it vanishes on constants; its
common cofactor is therefore `det(A|H)/T`.  Formula (27.20) remains true
when `B` is singular, because then both sides vanish.

For the row-power problem, (27.13)--(27.17) identify the strongest clean
arithmetic route to frequency-zero rigidity: after choosing a row--necklace
identification, it suffices to prove that the associated Eulerian directed
multigraph has arborescence count nonzero modulo `p`.  This yields real
nonsingularity immediately and collapses the partial-orbit lane to the
ordinary one-translate-per-row phase lift.  What the identity does **not**
provide is a way to average `tau mod p` over coordinate cycles; that remains
a high-degree spanning-tree statistic.

## 28. Partial-orbit selection has the same first gate as row powers

Let `T=|F|=C_m`.  For prime `p=2m+1`,

\[
                         T\equiv2(-1)^m\pmod p,
\tag{28.1}
\]

and hence `p` does not divide `T`.

### Theorem 28.1 (bounded multiplicity rigidity)

If

\[
                         \ker_{\mathbb F_p}B=\langle\mathbf1\rangle,
\tag{28.2}
\]

then the only vector `r in {0,...,p}^T` satisfying

\[
                         Br=p\mathbf1
\tag{28.3}
\]

is `r=1`.  Thus every exact partial-orbit selection is already a
one-translate-per-row phase lift.

#### Proof

Modulo `p`, (28.3) and (28.2) give `r=c1`.  If `c ne0`, every coordinate
is the unique representative `c in {1,...,p-1}`; the identity
`sum r_C=T` forces `c=1`.  If `c=0`, every coordinate is zero or `p`, so
its sum is divisible by `p`, contrary to (28.1). \(\square\)

The same hypothesis automatically closes the ordinary real-nullity gate.

### Corollary 28.2 (determinant congruence)

Let `A` be a `b by b` integer matrix with row and column sums `p`, where
`p` does not divide `b`.  If `rank_(F_p)A=b-1`, then `A` is nonsingular
over `R`.  If `kappa ne0` is the common cofactor modulo `p`, with signs
chosen so that `adj(A)=kappa J modulo p`, then

\[
 \boxed{{\det A\over p}\equiv b\,\kappa\pmod p,}
\tag{28.4}
\]

so in fact `v_p(det A)=1`.

#### Proof

The rank assumption makes both modular kernels the constant line, hence
`adj(A)=kappa J modulo p`.  From `A1=p1`,

\[
 p\,\operatorname{adj}(A)\mathbf1=(\det A)\mathbf1.
\]

Sum coordinates and reduce after dividing by `p`:

\[
 b\,{\det A\over p}
 =\mathbf1^T\operatorname{adj}(A)\mathbf1
 \equiv\kappa b^2\pmod p.
\]

Cancel `b`. \(\square\)

For the full Catalan matrix, (28.1) applies.  Hence

\[
 \boxed{\det B=0\Longrightarrow
        \dim_{\mathbb F_p}\ker B\ge2.}
\tag{28.5}
\]

This removes ordinary real nullity as an independent architecture.  A
useful partial-orbit count change can occur only on the same exceptional
cycles already detected by the nonconstant modular kernel in Section 19;
after that it must still satisfy the bounded-integer and root-of-unity
completion equations.

## 29. Fixed-support stopping bounds and matching-independence

The exact pair-codegree calculation gives a useful fixed-support estimate,
but it cannot be union-bounded into a maximal-rank theorem.

### Proposition 29.1 (best first-moment bound for a fixed support)

Fix a set `S` of `s` factor rows.  For a prime coordinate cycle `sigma`,
let

\[
 a_O(S)=\sum_{C\in S}B_\sigma(O,C),
 \qquad
 I_\sigma(S)=\sum_O\binom{a_O(S)}2.
\tag{29.1}
\]

If a nonzero vector in `ker_(F_p) B_sigma` has support exactly `S`, then

\[
                         I_\sigma(S)\ge {ps\over2}.
\tag{29.2}
\]

For a uniformly random prime cycle,

\[
 \boxed{
 {\mathbb E}_\sigma I_\sigma(S)
 ={p^2(p-1)s^2\over2W},}
\tag{29.3}
\]

and hence

\[
 \boxed{
 \Pr_\sigma[S\text{ supports a nonzero kernel vector}]
 \le \min\left(1,{p(p-1)s\over W}\right).}
\tag{29.4}
\]

No singleton-signature or transversality hypothesis is needed in this
formulation.

#### Proof

If `a_O(S)=1`, the corresponding modular row equation contains exactly one
nonzero coefficient, equal to one, and contradicts exact support `S`.
Thus every nonempty orbit mass is at least two.  Since
`sum_O a_O(S)=ps` and `binom(a,2)>=a/2` for `a>=2`, (29.2) follows.

Let `g_S` be the indicator of the disjoint union of the `s` middle row
packets.  It has mass and squared norm `ps`, and every coordinate belongs to
exactly `ms` selected middle sets, so its degree-one Johnson component is
zero.  The prime-cycle class-sum identity therefore gives

\[
 {\mathbb E}_\sigma\sum_Oa_O(S)^2
 =ps+(p-1){(ps)^2\over W}.
\tag{29.5}
\]

Subtract `sum_Oa_O(S)=ps`, divide by two, and apply Markov at the threshold
in (29.2). \(\square\)

This is essentially the strongest conclusion available from the exact mean
pair codegree alone.  It is useful for one prescribed sparse support, but a
uniform union bound fails immediately.  With `T=W/p` rows, even at `s=2`
the union-bound estimate is

\[
 \binom T2{2p(p-1)\over W}=\Theta(W),
\tag{29.6}
\]

and for growing `s` the entropy `binom(T,s)` overwhelms a bound containing
only one inverse power of `W`.  Moreover the full row set is always a
stopping set, since every necklace has degree `p`.  A cycle-dependent
kernel support can therefore rotate among exponentially many candidates
without contradicting (29.4).  Maximal rank requires a uniform
unique-neighbor expansion or a genuinely high-moment determinant theorem.

### Proposition 29.2 (the arborescence obstruction is matching-independent)

Let `P` be any permutation matrix identifying the necklace columns with the
row indices, and let `tau_P` be the arborescence number of

\[
                         L_P=pI-BP.
\tag{29.7}
\]

For any two identifications `P,Q`,

\[
 \boxed{
 \tau_P\equiv\det(PQ^{-1})\tau_Q\pmod p.}
\tag{29.8}
\]

In particular,

\[
                         p\mid\tau_P\iff p\mid\tau_Q.
\tag{29.9}
\]

Thus choosing a particularly convenient perfect matching can simplify the
contracted digraph, but it cannot change the modular success or failure of
the spanning-tree certificate.

#### Proof

Corollary 27.3 applied to `BP` gives

\[
 {\det(BP)\over p}\equiv(-1)^{T-1}T\tau_P\pmod p.
\tag{29.10}
\]

Since `det(BP)=det(B)det(P)` and `p notmid T`, division of (29.10) for two
choices when the common residue is nonzero yields (29.8).  If that residue
is zero, (29.10) makes both arborescence residues zero, so (29.8) still
holds.
\(\square\)

The signed cycle-average cannot be made intrinsic by a clever matching:
reordering two necklace columns reverses every determinant/cofactor sign
while leaving the coordinate cycle and its quotient graph unchanged.  The
first ordering-free detector is

\[
 \left({\det B_\sigma\over p}\right)^{p-1}
 =\begin{cases}
  1,&\operatorname{rank}_{\mathbb F_p}B_\sigma=T-1,\\
  0,&\operatorname{rank}_{\mathbb F_p}B_\sigma<T-1,
 \end{cases}
 \qquad\pmod p,
\tag{29.11}
\]

after harmless multiplication by the fixed unit from (27.13).  It has
degree `(p-1)(T-1)` in the incidence entries.  Consequently neither the
Johnson class-sum identity nor the exact quadratic mean pair-codegree
identity determines its average.  A proof that its average is nonzero is
precisely a new high-exterior-power theorem; the existing representation
identities do not supply it.

This detector does give an exact orientation-free cycle average.  If
`C_p` is the conjugacy class of coordinate `p`-cycles and `N_good` is the
number for which `B_sigma` has maximal modular rank, then Wilson's theorem
gives

\[
 {1\over|\mathcal C_p|}\sum_{\sigma\in\mathcal C_p}
 \left({\det B_\sigma\over p}\right)^{p-1}
 ={N_{\rm good}\over(p-1)!}
 \equiv-N_{\rm good}\pmod p.
\tag{29.12}
\]

Thus a nonzero average would prove existence, while a zero average would
only say that the number of successful cycles is divisible by `p`; it
would not prove nonexistence.  Formula (29.12) is exact but tautological
until the high-degree average can be evaluated.

## 30. Further support bounds for partial-orbit changes

The support of such a change has an exact graph-theoretic obstruction.
On a singleton-signature core, put

\[
S=\{C:r_C\ne1\}.
\tag{28.6}
\]

At frequency zero, such a change is exactly a **unit-negative column
trade**.  If `b_C` is column `C` of `B`, then there are disjoint nonempty
families `P,N` and coefficients `1<=a_C<=p-1` such that

\[
 \boxed{
 \sum_{D\in N}b_D=\sum_{C\in P}a_Cb_C,
 \qquad |N|=\sum_{C\in P}a_C.}
\tag{28.6a}
\]

Here rows in `N` are omitted, rows in `P` are used `1+a_C` times, and all
others once.  Conversely every equality (28.6a) supplies a bounded count
solution.  Thus real singularity is not sufficient: the integer kernel
must contain an oriented circuit whose whole negative side has coefficient
one.  The phase equations must subsequently refine this coarse column
trade into physical translated rows.

Because `v=r-1` lies in the integer kernel and its reduction modulo `p`
has support exactly `S`, no necklace has exactly one neighbor in `S`.
Thus `S` is a stopping set.  More strongly, put

\[
 P=\{C:r_C>1\},
 \qquad N=\{C:r_C=0\}.
\]

Every necklace adjacent to a fixed `D in N` must also contain a positive
row.  If the maximum common-neighbor count of two rows is `L`, this gives
`|P|>=ceil(p/L)`.  Since

\[
 |N|=\sum_{C\in P}(r_C-1)\ge|P|,
\tag{28.7}
\]

we obtain the sharper mixed-count bound

\[
 \boxed{|S|\ge2\left\lceil p/L\right\rceil.}
\tag{28.8}
\]

If `a=r_max-1`, fix a row of coefficient `a`.  Across its `p` necklace
neighbors the cancellation equation requires at least `ap` incidences
from negative rows, and one negative row supplies at most `L`.  Therefore

\[
 \boxed{|S|\ge
 \left\lceil p/L\right\rceil+
 \left\lceil p(r_{\max}-1)/L\right\rceil.}
\tag{28.8a}
\]

For a linear core, using all `p` translates of even one row forces at
least `p^2` changed rows.  This is still only polynomial in contrast to
the exponential Catalan row count.

In particular, **if** a favorable core can additionally be made linear
(`L=1`), no partial-orbit multiplicity change can be supported on fewer
than `2p` rows.  The polynomial cross-phase anomaly theorem of Section 23
does not by itself prove this pair-codegree hypothesis.  Moreover (28.8)
does not confine all changes to a polynomial leave: `T` is exponential,
and the whole row side is always a stopping set.  Excluding macroscopic
count changes requires an algebraic maximal-rank or dense-vector
anticoncentration theorem, not bounded pair codegrees alone.

More generally, for every `c in F_p`, the support

\[
 S_c=\{C:r_C\not\equiv c\pmod p\}
\tag{28.9}
\]

of the kernel vector `r-c1` is either empty or a stopping set.  Hence a
unique-neighbor theorem may attack every residue class of the mixed count
vector throughout its valid sparse range.  Local codegrees alone still do
not bound these supports from above.

There is an exact ceiling on this graph-theoretic method.  Any row set
`S` with `|S^c|<=p-2` is automatically a stopping set, because every
necklace has at least `p-|S^c|>=2` neighbors in `S`.  Thus all-scale
unique-neighbor expansion is impossible even for the best favorable
cycle.  Sparse modular kernels may be treated by expansion; dense kernels
require determinant/arborescence or dense-vector cancellation estimates.

## 31. Corrected component-excess accounting and all near-minimal sizes

Let the singleton-signature row--necklace graph have connected components
of sizes

\[
                         j_i=p+s_i,
 \qquad s_i\ge0,
\tag{31.1}
\]

on each side.  Simplicity and `p`-regularity only force `j_i>=p`; there is
no divisibility condition `p|j_i`.  If there are `k` components, define

\[
                         E=\sum_i s_i=T-pk.
\tag{31.2}
\]

### Proposition 31.1 (the exact squeeze scale)

The number `h` of nonminimal components and the number `R` of rows lying
in them satisfy

\[
                         h\le E,
 \qquad
                         R=ph+E\le(p+1)E.
\tag{31.3}
\]

Consequently:

1. `E=O(p)` confines all nonminimal components to `O(p^2)` rows.
2. `E=o(T/p)` is sufficient to make their total row mass `o(T)`.
3. The weaker condition `E=o(T)` is not sufficient.  If all components
   have size `p+1`, then

   \[
   k={T\over p+1},
   \qquad E=k=\Theta(T/p)=o(T),
   \tag{31.4}
   \]

   while every row lies in a nonminimal component.

#### Proof

Each nonminimal component contributes at least one to `E`, so `h<=E`.
Its row mass is `p+s_i`; summing gives `R=ph+E`. \(\square\)

Thus the successor-rigidity problem is not concentrated at size `2p`.
Every size `p<j<2p` must be audited, beginning with `p+1`.  Even a
component with no internal nonconstant phase direction still supplies its
`p` common component phases; these may change the factor unless the
component is itself an invariant translate packet.

The algebra of every near-minimal size is exact.  On a component of size
`j=p+s`, `1<=s<p`, write

\[
                         B=J-Q,
\tag{31.5}
\]

where `Q` is the `s`-regular `0-1` biadjacency matrix of the complement.

### Theorem 31.2 (complement-kernel and determinant formula)

Over `F_p`,

\[
 \boxed{
 \ker B=\langle\mathbf1\rangle\oplus\ker Q.}
\tag{31.6}
\]

Every vector in `ker Q` has coordinate sum zero.  Over `R`,

\[
 \boxed{
 \det B={p\over s}(-1)^{j-1}\det Q.}
\tag{31.7}
\]

In particular `B` is real-nonsingular exactly when `Q` is.

#### Proof

If `Ba=0` modulo `p` and `t=sum a`, then `Qa=t1`.  Since `s` is nonzero
modulo `p`, put `y=a-(t/s)1`.  Now `Qy=0`, and

\[
 \sum y=t-(t/s)j=t-(t/s)s=0\pmod p.
\]

Conversely `Qy=0` implies `s sum y=1^TQy=0`, so `Jy=0` and `By=0`.
This proves (31.6).

Over `R`, split constants from the sum-zero hyperplane.  The map `B`
acts by `p=j-s` on constants and by `-Q` on the hyperplane, while `Q`
acts by `s` on constants.  Taking determinants gives (31.7). \(\square\)

### Corollary 31.3 (sizes `p+1` and `p+2`)

1. If `s=1`, then `Q` is a permutation matrix.  Hence `B=J-Q` is real
   nonsingular and its modular kernel is only constants.  Every exact
   row-power assignment on the component is therefore one of the `p`
   common component phases.  Such a phase is vertically inert only when
   the component is itself a shift-invariant translate packet; component
   connectedness alone does not imply inertness.
2. If `s=2`, normalize one complementary perfect matching to the identity
   and write

   \[
                            Q=I+P.
   \tag{31.8}
   \]

   Then

   \[
    \boxed{
    \dim\ker B-1
    =\#\{\text{even cycles of }P\}.}
   \tag{31.9}
   \]

   On each even cycle, the alternating vector `(+1,-1,+1,-1,...)` lies
   in the **integer** kernel of `Q` and has sum zero.  Therefore

   \[
                         r=1+y\in\{0,2\}^{\text{cycle}}\times
                                   \{1\}^{\text{elsewhere}}
   \tag{31.10}
   \]

   is an exact frequency-zero mixed count vector.  Size `p+2` is the
   first near-minimal component at which an internal partial-orbit count
   direction can occur.  Nonzero Fourier completion remains an additional
   condition.

#### Proof

The first statement follows from Theorem 31.2.  For the second,
`(I+P)y=0` makes values alternate around every cycle of `P`; an odd cycle
forces zero and an even cycle supplies one alternating degree of freedom.
The alternating vector has equally many signs, so (31.10) follows.
\(\square\)

Finally, a connected component always has the `p` uniform phase choices,
but connectedness by itself says nothing about nonuniform choices.  The
complete `p by p` packet is connected and can have many legal assignments;
only the maximal-rank theorem (or the explicit complement calculation
above) collapses a component to its common phases.  Any component squeeze
which replaces “maximal modular rank” by “connected” is therefore invalid.

## 32. A sharp linear counterexample to every local rank criterion

The stopping bound (28.8) is sharp, even after imposing all of the
following abstract properties of the prime-cycle incidence matrix:

* exact Catalan side size `T=C_m`;
* simple, connected and `p`-regular;
* maximum pair codegree one;
* hence realization as the intersection matrix of two partitions of a
  `pT`-element set into `T` blocks of size `p`.

The missing property is specifically the coordinate-wreath origin of the
two partitions.

### Theorem 32.1 (affine-transversal counterexample)

For every sufficiently large prime `p=2m+1`, there is a connected
`T by T` zero-one matrix `B`, with `T=C_m`, such that

\[
 B\mathbf1=p\mathbf1,
 \qquad \mathbf1^TB=p\mathbf1^T,
\tag{32.1}
\]

any two columns have at most one common nonzero row, and nevertheless
there is a vector

\[
 v\in\{-1,0,1\}^T,
 \qquad Bv=0,
 \qquad |\operatorname{supp}v|=2p.
\tag{32.2}
\]

Consequently

\[
                         r=\mathbf1+v\in\{0,1,2\}^T
\tag{32.3}
\]

is a nontrivial exact frequency-zero mixed count vector.  In particular
`det B=0`, `dim ker_(F_p)B>=2`, and the arborescence certificate of
Section 27 fails, despite pair codegree `L=1`.

#### Proof

**The singular affine block.**  Let columns be the points `(x,y)` of
`F_p^2`, and rows the nonvertical affine lines

\[
                         \ell_{a,b}=\{(x,ax+b):x\in F_p\},
 \qquad a,b\in F_p.
\tag{32.4}
\]

The incidence matrix `A` is `p^2 by p^2` and `p`-regular on both sides.
Two points lie on at most one nonvertical line, so its column pair
codegree is at most one.  For each `c in F_p`, the vertical fiber

\[
                         V_c=\{(c,y):y\in F_p\}
\tag{32.5}
\]

meets every row exactly once.  Therefore

\[
                         A(\mathbf1_{V_0}-\mathbf1_{V_1})=0.
\tag{32.6}

The vector in (32.6) has exactly `p` positive and `p` negative entries.

**Linear regular padding blocks.**  Let `h=p^2+p+1`.  Take the point-line
incidence graph of `PG(2,p)` and delete any perfect matching.  The
resulting square matrix `H` has side size `h`, row and column degree `p`,
and pair codegree at most one.  Such a matching exists because the
original incidence graph is regular bipartite.

The Catalan congruence is

\[
                         T\equiv2(-1)^m\pmod p.
\tag{32.7}
\]

Choose `k_0=2` when the residue is `2`, and `k_0=p-2` when it is `-2`.
Then

\[
                         R=T-p^2-k_0h
\tag{32.8}
\]

is a nonnegative multiple of `p` for all sufficiently large `p`.  Since
`gcd(p,h)=1`, the Frobenius coin theorem gives nonnegative integers `a,b`
such that

\[
                         {R\over p}=ap+bh,
\tag{32.9}
\]

because `R/p` is exponential in `p` while the Frobenius threshold is only
polynomial.  Thus a block diagonal sum of

* one distinguished affine block `A`;
* `a` further affine blocks;
* `k_0+bp` projective-plane padding blocks `H`

has side size exactly `T`, is `p`-regular and linear, and retains the
kernel vector (32.6), extended by zero on every padding block.

**Connecting without losing linearity or the kernel.**  Between two
current connected components choose incidences `ell--x` and `ell'--y`
whose column coefficients in `v` are zero.  Replace them by the crossed
incidences `ell--y` and `ell'--x`.  This two-switch preserves every row
and column degree and preserves `Bv=0`.  It also preserves pair codegree
at most one: the only new column pairs use columns from formerly disjoint
blocks and occur in exactly one of the two switched rows.  A connected
regular bipartite graph has no bridge, so deleting the chosen incidences
does not disconnect the old components; the two crossed incidences join
them.  Iterating connects all blocks.  There are abundant zero-coefficient
columns, and each padding block is entirely zero for `v`.

The final matrix has all claimed properties. \(\square\)

### Corollary 32.2 (sharpness and the actual missing input)

For `L=1`, the statewise lower bound

\[
                         |S|\ge2p
\]

from (28.8) is attained exactly by (32.2)--(32.3).  Therefore no theorem
using only degree, connectedness, exact side size, Catalan congruence,
partition structure, transversality and pair codegree can prove maximal
rank or frequency-zero rigidity.  A successful proof for `B_sigma` must
use a genuinely coordinate-specific property of cyclic intervals in
wreath rows, or a higher-order statistic which excludes the affine
transversal trade.

The equality case itself has a rigid normal form.

### Theorem 32.3 (classification of a minimal linear mixed count)

Let `B` be simple and `p`-regular with pair codegree at most one.  Suppose
`r ne1`, `Br=p1`, and

\[
                         |\{C:r_C\ne1\}|=2p.
\tag{32.10}
\]

Then:

1. exactly `p` rows are omitted and exactly `p` rows are doubled;
2. no other multiplicity occurs;
3. every omitted--doubled row pair has exactly one common necklace;
4. these `p^2` common necklaces are all distinct and each has exactly one
   omitted and one doubled neighbor in the changed support.

Equivalently, the changed incidence pattern is the edge-incidence
subdivision of `K_(p,p)`.  The construction in Theorem 32.1 realizes this
normal form with the two vertical fibers of the affine plane.

#### Proof

Use the notation `P,N` of Section 30.  Pair codegree one and (28.8) give
`|P|>=p`, while `|N|>=|P|`.  Equality `|P|+|N|=2p` forces

\[
                         |P|=|N|=p.
\tag{32.11}
\]

The sum identity `|N|=sum_(C in P)(r_C-1)` then forces every positive
coefficient to equal one, so the rows in `P` are doubled.

Fix `D in N`.  Its `p` necklace neighbors must each contain a positive
row.  Since there are only `p` positive rows and each can share at most one
necklace with `D`, every `C in P` shares exactly one necklace with `D`.
Thus all `p^2` cross pairs occur once.

At a necklace let `u` and `v` be its numbers of positive and negative
neighbors in the changed support.  The equation `B(r-1)=0` gives `u=v`.
The total number of cross pairs is therefore

\[
                         \sum_Ouv=\sum_Ou^2=p^2,
\tag{32.12}
\]

whereas the total positive incidence count is

\[
                         \sum_Ou=p^2.
\tag{32.13}
\]

Hence `sum_O u(u-1)=0`, so every occupied necklace has `u=v=1`.
This proves the classification. \(\square\)

For the actual prime-cycle matrix `B_sigma`, the first sharp successor
target can therefore be stated geometrically: exclude a pair of `p`-row
families whose cross common-necklace relation is an affine `K_(p,p)` grid.
This is strictly stronger than pair-codegree control and is the first
place where cyclic-interval geometry can distinguish the wreath matrix
from Theorem 32.1.

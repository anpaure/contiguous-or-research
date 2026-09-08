# Odd occurrence selectors as zero-energy pairs in a one-factorization

**Date:** 2026-08-03  
**Status:** unconditional exact reduction and obstruction.  This note does
not prove that the zero-energy pair exists in every parameter.

## 0. Result and scope

Assume `m>=3`, and put

\[
 n=2m-1,\qquad
 \mathcal L={ [n]\choose m-1},\quad
 \mathcal M={ [n]\choose m},\quad
 \mathcal U={ [n]\choose m+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal M|,qquad
 U=|\mathcal U|,qquad
 C=W-U=\operatorname {Cat}_m.
\]

Let `G` be the `m`-regular bipartite containment graph between
`mathcal L` and `mathcal M`.  Every proper `m`-edge-colouring of `G` is a
one-factorization

\[
                         E(G)=F_1\mathbin{\dot\cup}\cdots
                                  \mathbin{\dot\cup}F_m.       \tag{0.1}
\]

For every upper colour `R in mathcal U`, the restriction of (0.1) to the
Boolean interval below `R` canonically gives a loopless
`(m+1)`-regular multigraph `H_R` on the colour set `[m]`.  If
`a^R_{ij}` is the multiplicity of the colour-pair `ij` in `H_R`, then the
compressed union of the two perfect matchings `F_i,F_j` has upper
multiplicity exactly

\[
                              \mu_{ij}(R)=a^R_{ij}.             \tag{0.2}
\]

Define

\[
 \Delta_{ij}:=
 \sum_{R\in\mathcal U}
       { (\mu_{ij}(R)-1)(\mu_{ij}(R)-2)\over2}.                \tag{0.3}
\]

Every summand in (0.3) is a nonnegative integer.  The central theorem is

\[
 \boxed{\Delta_{ij}=0
 \iff
 \mu_{ij}(R)\in\{1,2\}\quad\hbox{for every }R.}               \tag{0.4}
\]

When (0.4) holds, the duplicated set

\[
                         \mathcal D_{ij}:=
                         \{R:\mu_{ij}(R)=2\}                  \tag{0.5}
\]

has order `C` and is automatically a simple regular Catalan design of
coordinate degree `2 Cat_(m-1)`.  Thus a zero-energy pair is already the
full occurrence-level owner/q1 selector sought by the simple Catalan target
theorem; no separate current condition remains.

More globally,

\[
 \boxed{
 \sum_{1\le i<j\le m}\Delta_{ij}
  =\sum_{R\in\mathcal U}
      \left(\sum_{i<j}{a^R_{ij}\choose2}-m\right)\ge0.}       \tag{0.6}
\]

Equality in one summand on the right means

\[
                         H_R=K_m+Z_R,                          \tag{0.7}
\]

where `Z_R` is a simple spanning `2`-factor on the factor colours.
Consequently equality in (0.6) produces not merely one selector: **every**
pair `F_i,F_j` is an upper-surjective cap-two selector.

Conversely every pair of edge-disjoint incidence bijections extends to a
one-factorization.  Hence the original occurrence-selector existence
problem is exactly

\[
 \boxed{
  \min_{\text{one-factorizations }\mathcal F}
  \min_{i<j}\Delta_{ij}=0.}                                  \tag{0.8}
\]

This is a strict reduction from a four-resource atom selector to a proper
edge-colouring with one explicit nonnegative integer objective.  It also
identifies the required move size: a two-colour Kempe switch cannot change
the selector or `Delta` of that same colour pair.  Any descent for a fixed
pair must involve a third factor colour (or leave the one-factorization
fibre).  This is the exact factor-colouring reason that an abstract Ryser
switch does not automatically lift to the literal selector.

## 1. The local pair multigraph

Fix a one-factorization (0.1) and an upper set `R in mathcal U`.  Its
rank-`m` facets are

\[
                             T_x=R-x\qquad(x\in R),             \tag{1.1}
\]

and its rank-`(m-1)` members are

\[
                             q_{xy}=R-\{x,y\}
                              \qquad(\{x,y\}\in{R\choose2}).   \tag{1.2}
\]

The two incidences in the diamond `[q_xy,R]` are

\[
                             q_{xy}T_x,qquad q_{xy}T_y.       \tag{1.3}
\]

Give the edge `xy` of the abstract complete graph on `R` the unordered pair
of factor colours appearing on (1.3).  The two colours are different,
because all `m` incidence edges at `q_xy` have distinct colours.  Replacing
each edge `xy` by its colour pair gives a loopless multigraph `H_R` on
`[m]`; let `a^R_ij` be its multiplicities.

### Lemma 1.1 (exact local degrees)

For every `R` and every factor colour `i`,

\[
                         \sum_{j\ne i}a^R_{ij}=m+1.            \tag{1.4}
\]

Consequently

\[
                         \sum_{i<j}a^R_{ij}={m(m+1)\over2}
                           ={m\choose2}+m.                     \tag{1.5}
\]

### Proof

At a fixed facet `T_x`, its `m` incident lower sets are exactly the
`q_xy`, `y in R-x`.  Proper edge-colouring gives every factor colour once
on those `m` incidences.  Therefore colour `i` appears once at each of the
`m+1` facets of `R`, which is (1.4).  Summing degrees gives (1.5).
\(\square\)

### Lemma 1.2 (compression identity)

For every pair `i<j`, the union `F_i cup F_j`, compressed at the lower
shore, is a simple spanning `2`-factor on `mathcal M`, and its upper-colour
multiplicity is (0.2).

### Proof

Every lower vertex `q` has one neighbour in `F_i` and one in `F_j`; they
are distinct because (0.1) is an edge partition.  Their intersection is
`q`, so their union is a unique member `R` of `mathcal U`.  Inside the
interval `[q,R]`, the two incidences have colours `i,j`, and the converse is
immediate from the construction of `H_R`.  This proves (0.2).

At every middle vertex there is one incident edge of each factor colour,
so compression has degree two.  It has no loop.  Two different lower
vertices cannot give parallel edges between the same adjacent middle sets,
because their intersection is the unique lower vertex on that Johnson
edge.  Thus it is a simple spanning `2`-factor.  \(\square\)

In particular

\[
                              \sum_R\mu_{ij}(R)=W              \tag{1.6}
\]

for every factor pair.

## 2. Exact defect of one pair

For an integer `z>=0`, put

\[
                              f(z)={(z-1)(z-2)\over2}.          \tag{2.1}
\]

Then

\[
 f(0)=1,\qquad f(1)=f(2)=0,\qquad
 f(z)={z-1\choose2}\quad(z\ge2).                              \tag{2.2}
\]

Thus `f` charges one unit for a missing upper colour and charges the exact
quadratic excess above multiplicity two.

### Theorem 2.1 (one-pair zero certificate)

For every pair `i<j`,

\[
 \begin{aligned}
 \Delta_{ij}
 &=\sum_R\left[{\mu_{ij}(R)\choose2}-\mu_{ij}(R)+1\right]\\
 &=\sum_R{\mu_{ij}(R)\choose2}-C.                            \tag{2.3}
 \end{aligned}
\]

It is nonnegative, and it vanishes exactly under (0.4).

### Proof

The first line is (2.1).  Since `sum_R mu_ij(R)=W` and `W-U=C`, summing
the linear and constant terms gives the second line.  Nonnegativity and the
zero set follow term by term from (2.2).  \(\square\)

When `Delta_ij=0`, (1.6) gives

\[
                 |\mathcal D_{ij}|=W-U=C.                       \tag{2.4}
\]

The current of the two incidence bijections also proves regularity without
any additional assumption.  For a coordinate `x`, every perfect matching
image contains `x` on

\[
                              {2m-2\choose m-1}                 \tag{2.5}
\]

rows, while their pairwise intersections (the complete lower shore) contain
`x` on `binom(2m-2,m-2)` rows.  Hence the selected upper occurrences
containing `x` number

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}.                         \tag{2.6}
\]

Subtract the one base copy of every upper colour, of which
`binom(2m-2,m)` contain `x`.  The remainder is

\[
 2{2m-2\choose m-1}-{2m-2\choose m-2}-{2m-2\choose m}
 =2\operatorname {Cat}_{m-1}.                                 \tag{2.7}
\]

This is exactly the degree of `x` in `mathcal D_ij`.

If `mathcal P subseteq mathcal U` is a protected bank which must remain
unique, define

\[
 \Delta^{\mathcal P}_{ij}
  :=\Delta_{ij}+\sum_{R\in\mathcal P}{\mu_{ij}(R)\choose2}.    \tag{2.8}
\]

Then `Delta^P_ij=0` exactly when the pair is cap-two upper-surjective and
its duplicate design is disjoint from `P`.  This retains occurrence
multiplicity; it is stronger than merely choosing an abstract regular
design disjoint from `P`.  It does **not** pin a specified physical
occurrence of a protected colour; the protected datum here is the upper
colour required to remain unique.

## 3. Total colour energy

### Theorem 3.1 (local-to-global energy identity)

Equation (0.6) holds.  For a fixed `R`,

\[
                        \sum_{i<j}{a^R_{ij}\choose2}\ge m,    \tag{3.1}
\]

and equality holds exactly when all `a^R_ij` belong to `{1,2}`.  In the
equality case exactly `m` pairs have multiplicity two, and those pairs form
a simple spanning `2`-factor `Z_R` on `[m]`.

### Proof

By (1.5), the `binom(m,2)` nonnegative integers `a^R_ij` have total
`binom(m,2)+m`.  If `z` of these integers vanish, then

\[
 \sum_{i<j}{a^R_{ij}\choose2}
 \ge \sum_{a^R_{ij}>0}(a^R_{ij}-1)
 =m+z\ge m.                                             \tag{3.2}
\]

The first inequality is equality exactly when every positive multiplicity
is one or two.  Equality in the whole display also forces `z=0`.
Consequently the minimum is attained exactly by putting one unit in every
entry and one additional unit in exactly `m` entries.  This proves (3.1)
and the asserted multiplicities.

At equality, (1.4) says that every colour has degree `m+1`.  The base
`K_m` contributes degree `m-1`, so the doubled pairs contribute degree two
at every colour.  They are distinct pairs, hence form a simple spanning
`2`-factor.

Finally, summing (2.3) over `i<j` and grouping first by `R` gives

\[
 \sum_{i<j}\Delta_{ij}
 =\sum_R\sum_{i<j}{a^R_{ij}\choose2}
   -{m\choose2}C.
\]

The Catalan ratio `C/U=2/(m-1)` gives

\[
                         {m\choose2}C=mU.                       \tag{3.3}
\]

which proves (0.6).  \(\square\)

### Corollary 3.2 (best pair in a fixed factorization)

If `mathcal E(mathcal F)` denotes the right side of (0.6), then

\[
                  \min_{i<j}\Delta_{ij}
                  \le \left\lfloor{
                         \mathcal E(\mathcal F)
                         \over {m\choose2}}\right\rfloor.     \tag{3.4}
\]

In particular a locally balanced factorization, `mathcal E=0`, supplies
`binom(m,2)` simultaneous cap-two upper-surjective selectors.

The converse is deliberately not asserted: one zero-energy pair may coexist
with positive energy in the other pairs.

## 4. Exact equivalence with the occurrence selector

### Theorem 4.1 (factorization equivalence)

There are two edge-disjoint incidence bijections

\[
                         t,s:\mathcal L\longrightarrow\mathcal M       \tag{4.1}
\]

whose upper multiplicities lie in `{1,2}` and are everywhere positive if
and only if (0.8) holds.

The same equivalence holds with a protected unique-colour bank after
replacing `Delta` by (2.8).

### Proof

The forward implication starts with the two perfect matchings `t,s`.  Their
deletion leaves an `(m-2)`-regular bipartite graph.  By Konig's line-colour
theorem it decomposes into `m-2` perfect matchings.  Together these form a
one-factorization in which `t,s` are two colour classes.  Theorem 2.1 gives
zero energy, and (2.8) gives the protected version.

Conversely a zero-energy pair consists of two perfect matchings and has the
required upper multiplicities by Theorem 2.1.  \(\square\)

The compressed support is a disjoint union of Johnson cycles by Lemma 1.2.
Orienting every component consistently labels the two perfect matchings as
tail and head.  A single connected owner chronology is the additional
condition that this `2`-factor have one component.  Thus, if `c_ij` is its
number of components, the nonnegative objective

\[
              \Xi^{\mathcal P}_{ij}
                :=\Delta^{\mathcal P}_{ij}+c_{ij}-1            \tag{4.2}
\]

vanishes exactly for a connected occurrence selector with protected
colours unique.  Equation (4.2) prices projected owner/q1 topology only; it
does not price residence, deeper upper windows, or the lower compiler.

## 5. Two-colour rigidity and the genuine move gate

### Theorem 5.1 (same-pair Kempe rigidity)

Let `K` be one alternating-cycle component of `F_i cup F_j`.  Interchange
the colours `i,j` on every incidence edge of `K`.  Then:

1. the compressed undirected selector of the pair `{i,j}` is unchanged;
2. every multiplicity `mu_ij(R)` is unchanged;
3. `Delta_ij`, `D_ij`, and the component count `c_ij` are unchanged.

### Proof

The switch changes only which of the two pair colours names each edge of
`K`; the unordered two-edge set incident with every lower vertex is fixed.
Compression and every listed quantity depend only on that unordered pair.
\(\square\)

Consequently ordinary two-colour connectivity of bipartite
one-factorizations cannot prove (0.8).  To lower `Delta_ij` while staying
inside the factorization fibre, a move must exchange at least one incidence
with a third factor colour.  Boolean `C6` trades have exactly that algebraic
shape.  The statement here does not prove that the available `C6` trades
connect to zero energy; it proves why a two-colour Ryser/Kempe argument
cannot do so.

## 6. What is and is not closed

Proved unconditionally:

1. every occurrence selector embeds in a full one-factorization;
2. its cap-two upper defect is exactly the integer `Delta` in (0.3);
3. zero defect automatically gives a simple regular Catalan duplicate
   design with the correct current;
4. the total defect of all factor pairs is the sum of independent local
   collision excesses (0.6);
5. zero local collision energy is equivalent to the concrete local normal
   form `K_m+Z_R` at every upper interval; and
6. same-pair two-colour switches are rigorously inert.

Still open:

1. construction, for every `m`, of a one-factorization with one
   zero-energy pair (or the stronger locally balanced factorization);
2. retention of an arbitrary prescribed `O(sqrt(m))` upper-colour bank as
   unique colours in such a factorization (not retention of named physical
   occurrences);
3. forcing the zero-energy pair to have one component; and
4. the typed common-cap socket and all-width/residence/compiler rows.

The sharp next owner/q1 statement is therefore no longer an unspecified
four-resource selector.  It is:

\[
 \boxed{\text{construct a proper }m\text{-edge-colouring of }G
        \text{ with }\Delta_{12}=0,}
\]

or, more strongly, realize the local normal form `H_R=K_m+Z_R` for every
`R` compatibly across the overlapping Boolean intervals.

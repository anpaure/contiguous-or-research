# The four-row SCD C-phase is an exact rainbow branching forest, with two
# sharp diagonal Hall cuts

Date: 2026-08-01  
Lane: R, explicit four-row SCD C-phase owner graph  
Status: exact upper/lower palette theorem, all-dimensional acyclicity,
solver-free all-dimensional degree obstruction, smallest literal
counterexample, and exact prospective detachment cut.  A noncanonical
cross-facet detachment is not constructed.

## 0. Outcome

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad G=[2m-3],
 \qquad m\ge3,                                             \tag{0.1}
\]

and use the increasing Greene--Kleitman symmetric-chain decomposition of
`2^G`.  Put

\[
\begin{aligned}
 D&=\binom{2m-3}{m-2},&
 E&=\binom{2m-3}{m-3},&
 H&=\binom{2m-3}{m-4},\\
 c&=D-E=\operatorname{Cat}_{m-1},&
 I_m&=E-H,&
 C&=\operatorname{Cat}_m=2D-E-H.
\end{aligned}                                               \tag{0.2}
\]

There are `c` short chains `S<L`, `I_m` long chains ending at `U`, and
`H` very long chains reaching `W`.  The explicit four-row C-phase candidate
has respectively one, three, and four physical owner edges on those chain
types.  Hence

\[
 c+3I_m+4H
   =D+2E+H
   =\binom{2m-1}{m+1}.                                     \tag{0.3}
\]

Every rank-`(m+1)` upper colour occurs exactly once.  All selected lower
colours are distinct, and exactly

\[
                         2c+I_m=C                           \tag{0.4}
\]

lower colours remain unused.

The topology has a clean positive theorem: the standard candidate is an
undirected forest for every `m`.  Orient every physical owner edge as in
Section 2 and put `Phi(X)=sum_(i in X)i`.  Its six possible increments are

\[
                   z-x,\quad y-x,\quad x-\rho,
                   \quad z-y,\quad v-y,\quad y-x,            \tag{0.5}
\]

all positive.  Since every selected lower tail is unique, owner outdegree
is at most one.  A `Phi`-minimum vertex of an undirected cycle would have
two outgoing cycle edges, a contradiction.

The max-degree row is nevertheless false, minimally at `m=4`.  Two
explicit diagonal maps each have a fibre of size `m-2`, landing on an owner
which already carries one seed edge.  Thus the candidate contains owners of
degree

\[
                              m-1.                          \tag{0.6}
\]

At `m=4` the two literal degree-three stars are

\[
\begin{aligned}
 a135 &: a125-a135,\quad a134-a135,\quad a135-az35,\\
 az24 &: az14-az24,\quad az23-az24,\quad a245-az24.
\end{aligned}                                               \tag{0.7}
\]

All their lower and upper colours are distinct.  Thus this is an owner-only
failure inside an exact upper/lower-rainbow forest, not a palette artefact.

The exact prospective repair row is ordinary Hall on each owner-signature
shore, followed separately by graphic independence.  The two frozen
singleton cuts have deficiency `m-3` each.  Any repair retaining all fixed
diagonal assignments outside these fibres must detach at least `2m-6`
distinct long ears.

## 1. Chain census and the four-row matching

For a central SCD chain write

\[
 R\subset S=R+\rho\subset L=S+x\subset U=L+y
                    \subset W=U+v,                         \tag{1.1}
\]

omitting the endpoints which the chain does not have.  Greene--Kleitman
adds its free coordinates increasingly, so

\[
                             \rho<x<y<v.                     \tag{1.2}
\]

The four-row incidence matching is

\[
\begin{array}{c|cc}
\text{lower root}&\text{long chain}&\text{short chain}\\ \hline
azR&azS&-\\
zS&zL&azS\\
aS&aL&aL\\
L&U&zL.
\end{array}                                                 \tag{1.3}
\]

The number of central chains is `D`.  Exactly `E` contain `R,U`, and
exactly `H` also contain `W`.  Therefore the three mutually exclusive
chain classes have sizes

\[
                    c=D-E,\qquad I_m=E-H,\qquad H.           \tag{1.4}
\]

The Catalan identities in (0.2) follow from adjacent binomial differences.

## 2. Literal owner graph and palette ledger

Orient physical owner edges from the owner matched to the selected lower
tail toward the other owner.

### 2.1 Short chain

For `S<L=S+x`, retain

\[
                         aL\longrightarrow azS,              \tag{2.1}
\]

whose lower intersection is `aS` and upper union is `azL`.

### 2.2 Long chain ending at `U`

For (1.1) without `W`, the long `aU` ear and retained `zU` edge give

\[
\begin{array}{c|c|c}
\text{owner arrow}&\text{lower intersection}&\text{upper union}\\ \hline
aL\longrightarrow a(S+y)&aS&aU\\
azS\longrightarrow az(R+x)&azR&azL\\
U\longrightarrow zL&L&zU.
\end{array}                                                 \tag{2.2}
\]

### 2.3 Very long chain reaching `W=U+v`

Keep the first two arrows of (2.2) and replace its last arrow by

\[
\begin{array}{c|c|c}
U\longrightarrow L+v&L&W\\
zL\longrightarrow z(S+y)&zS&zU.
\end{array}                                                 \tag{2.3}
\]

The phrase “the fourth edge uses new lower `zS`” refers to the second row
of (2.3), which retains `zU`; the new `W` edge itself has lower `L`.  Thus
there is no containment inconsistency between `zS` and the all-`G` colour
`W`.

### Theorem 2.1 (exact upper/lower closure)

The edges (2.1)--(2.3) use every rank-`(m+1)` upper colour exactly once and
have pairwise distinct lower colours.  Their count is (0.3), and the unused
lower colours are exactly

1. `L,zS` on every short chain; and
2. `zS` on every long chain ending at `U`.

Their total is (0.4).

#### Proof

Split upper colours by their intersection with `{a,z}`.  The four sectors
and their sizes are

\[
\begin{array}{c|c|c}
\text{signature}&\text{providers}&\text{size}\\ \hline
az&azL&D\\
a&aU&E\\
z&zU&E\\
\varnothing&W&H.
\end{array}                                                 \tag{2.4}
\]

Every SCD set of the required rank occurs on exactly one chain, so each
row is injective and complete.  Vandermonde over the two special
coordinates gives

\[
 D+2E+H=\binom{2m-1}{m+1}.                                  \tag{2.5}
\]

The lower rows are `aS` on short chains; `aS,azR,L` on long chains ending
at `U`; and `aS,azR,L,zS` on very long chains.  Signature and SCD membership
make them pairwise distinct.  The complete lower layer has the four types
`L,aS,zS,azR`; the displayed complement is exactly the two families in the
statement.  Its size is

\[
 2(D-E)+(E-H)=2D-E-H=C.                                     \tag{2.6}
\]

\(\square\)

## 3. All-dimensional acyclicity

### Theorem 3.1 (strict owner potential)

The physical owner graph (2.1)--(2.3) is an undirected forest for every
`m>=3`.

#### Proof

Give every coordinate its natural integer label and set

\[
                             \Phi(X)=\sum_{i\in X}i.          \tag{3.1}
\]

The changes along the oriented rows (2.1), (2.2), and (2.3) are,
respectively,

\[
\begin{array}{c|c}
aL\to azS&z-x\\
aL\to a(S+y)&y-x\\
azS\to az(R+x)&x-\rho\\
U\to zL&z-y\\
U\to L+v&v-y\\
zL\to z(S+y)&y-x.
\end{array}                                                 \tag{3.2}
\]

They are all strictly positive by (1.2) and because `z>2m-3`.

Every selected lower intersection is distinct by Theorem 2.1.  Since the
matching `M_0` is bijective, the first owner in every oriented edge is
therefore distinct; physical outdegree is at most one.

If an undirected cycle existed, choose on it a vertex of minimum `Phi`.
Both incident cycle edges would be oriented away from that vertex, because
`Phi` strictly rises along every arrow.  Its outdegree would be at least
two, contradiction.  \(\square\)

Thus no Tamari recursion is needed for the fixed candidate's topology.
Tamari/cross-chain moves become relevant only when detaching overloaded
heads, and then the potential must be rechecked for the replacement arrows.

## 4. Exact owner-degree criterion

The only non-incumbent owner endpoints in the ears are the four maps

\[
\begin{array}{c|c|c}
\text{map}&\text{domain}&\text{underlying new owner}\\ \hline
\beta_a&\text{long}&S+y\\
\delta_a&\text{long}&R+x\\
\beta_0&\text{very long}&L+v\\
\delta_0&\text{very long}&S+y.
\end{array}                                                 \tag{4.1}
\]

Their physical signatures are respectively `a,az,empty,z`, so different
rows cannot collide.

### Proposition 4.1 (degree formula)

For every correctly ranked `T subseteq G`,

\[
\begin{aligned}
 \deg(aT)&=1+|\beta_a^{-1}(T)|,\\
 \deg(azT)&=1+|\delta_a^{-1}(T)|,\\
 \deg(T)&=1+|\beta_0^{-1}(T)|,\\
 \deg(zT)&={\bf1}_{\{T\text{ is a long top}\}}
                         +|\delta_0^{-1}(T)|.                \tag{4.2}
\end{aligned}
\]

Every `delta_0` image in the standard SCD is a long top.  Hence the
canonical graph has maximum degree at most two if and only if all four maps
in (4.1) are injective.

#### Proof

Every image owner lies in the complete old owner palette.  The corresponding
incumbent endpoint is unique because the seed is a matching.  This gives
the first three rows of (4.2).  In the fourth row a `zT` incumbent exists
exactly when `T=L` belongs to a long chain.

For a very long source, setting `y` while leaving the previous free
coordinate `x` pairs `x` with `y` in the Greene--Kleitman parenthesis
matching.  The new chain bottom rank rises by one from at most `m-4` to at
most `m-3`, so `T=S+y` lies on a long central chain.  This proves the last
assertion.  \(\square\)

## 5. Two all-dimensional diagonal overloads

### Theorem 5.1 (`delta_a` even fibre)

Let

\[
                     E_0=\{2,4,\ldots,2m-4\}.                \tag{5.1}
\]

For `j=1,...,m-2`, put `R_j=E_0-{2j}`.  Then `R_j` is a GK chain bottom
whose free coordinates are

\[
                           2j-1<2j<2m-3.                     \tag{5.2}
\]

All `m-2` corresponding ears have

\[
                       \delta_a(R_j)=R_j+2j=E_0.             \tag{5.3}
\]

The short chain `E_0<E_0+(2m-3)` already has an edge incident with `azE_0`.
Therefore

\[
                              \deg(azE_0)=m-1.               \tag{5.4}
\]

#### Proof

The word of `R_j` is made of matched `01` pairs except that pair `j` is
`00`, followed by the final zero.  Its unmatched zeros are exactly (5.2).
Equations (5.3)--(5.4) now follow from (2.2).  The word of `E_0` is
`(01)^(m-2)0`, so its sole free coordinate is `2m-3`, proving the short
incumbent claim.  \(\square\)

### Theorem 5.2 (`beta_a` odd fibre)

Let

\[
                       O=\{1,3,\ldots,2m-3\}.                 \tag{5.5}
\]

For `j=1,...,m-2`, put `R'_j=O-{1,2j+1}`.  Then `R'_j` is a GK chain
bottom with free coordinates

\[
                             1<2j<2j+1,                       \tag{5.6}
\]

and all corresponding ears satisfy

\[
                         \beta_a(R'_j)=O.                    \tag{5.7}
\]

The short chain `O-{1}<O` already has an edge incident with `aO`, so

\[
                              \deg(aO)=m-1.                  \tag{5.8}
\]

#### Proof

The binary word has an initial zero and otherwise matched `01` pairs, with
one pair changed to `00`.  This gives (5.6).  Its successive central sets
are

\[
 S'_j=O-\{2j+1\},\quad
 L'_j=S'_j+2j,\quad U'_j=L'_j+(2j+1),                        \tag{5.9}
\]

so `S'_j+(2j+1)=O`.  The short incumbent follows because `O-{1}` has sole
free coordinate one.  \(\square\)

For `m>=4`, the even and odd source families are disjoint.  Each overloaded
owner has residual incoming capacity one after its incumbent edge and
receives `m-2` fixed tasks.  Each singleton Hall deficiency is therefore

\[
                              (m-2)-1=m-3.                    \tag{5.10}
\]

## 6. Smallest literal counterexample

At `m=4`, `G=[5]`.  The odd fibre gives the long chains

\[
\begin{array}{c|c|c|c}
R&S&L&U\\ \hline
\{5\}&\{1,5\}&\{1,2,5\}&\{1,2,3,5\}\\
\{3\}&\{1,3\}&\{1,3,4\}&\{1,3,4,5\},
\end{array}                                                 \tag{6.1}
\]

and the physical star

\[
                       a125-a135-a134,
 \qquad                a135-az35.                            \tag{6.2}
\]

The notation in (6.2) means that both `a125` and `a134` are adjacent to
`a135`.  The three lower colours are `a15,a13,a35`; the three upper colours
are `a1235,a1345,az135`.  They are all distinct.

The even fibre similarly gives

\[
\begin{array}{c|c|c|c}
R&S&L&U\\ \hline
\{4\}&\{1,4\}&\{1,2,4\}&\{1,2,4,5\}\\
\{2\}&\{2,3\}&\{2,3,4\}&\{2,3,4,5\},
\end{array}                                                 \tag{6.3}
\]

and the star

\[
                  az14-az24-az23,
 \qquad           a245-az24.                                \tag{6.4}
\]

Thus `m=4` is the smallest failure.  At `m=3`, each fibre has size one and
creates degree two, not three.

## 7. Exact prospective detachment theorem

Let `T_s` be the ear tasks of one owner signature `s in {a,az,0,z}`.  For
each task `t`, let `N_s(t)` be its legal alternative heads after fixing all
palette/lower rows and the retained seed.  Every head has residual capacity
one.

### Theorem 7.1 (degree-row min--max)

There is a cap-two head assignment on signature shore `s` if and only if

\[
                      |X|\le|N_s(X)|
              \qquad\text{for every }X\subseteq T_s.         \tag{7.1}
\]

For all four signature shores simultaneously, (7.1) must hold separately
on each shore.  After such assignments, the physical support is a linear
forest exactly when the inserted edges are independent in the graphic
matroid after contracting the retained seed.

#### Proof

The signature shores are disjoint.  On one shore, every target head already
has one incumbent edge and hence one remaining capacity slot.  Selecting
distinct heads is therefore exactly an ordinary bipartite matching from
tasks to heads; Hall gives (7.1).  Distinct heads and the already distinct
tails give maximum degree two.  The only remaining obstruction to a forest
is an undirected cycle, equivalently dependence after contracting the
retained seed.  \(\square\)

For the frozen canonical maps, each task menu is a singleton.  The two
fibres in Section 5 violate (7.1) by `m-3`.  Any repair retaining the seed
and all other fixed diagonal choices must change at least `m-3` assignments
in each disjoint fibre, hence at least

\[
                              2m-6                             \tag{7.2}
\]

long-ear assignments in total.

The theorem deliberately separates degree from topology.  A monotone
potential certifies that the original overloaded stars are acyclic; it
cannot reduce their degree.  A successful Tamari/cross-chain detachment
must first pass (7.1), and its replacement arrows must then pass the graphic
row—preferably by preserving the strict potential (3.1).

## 8. Audit and scope

The deterministic source

`scratch/audit_scd_global_seed_long_ears_20260801.cpp`

was independently compiled with `-O3` and replayed on the H100 CPU under a
30-second/256-MiB cap.  For `m=3,...,9` it reproduced exact upper/lower
counts, zero undirected cycles, and maximum physical degrees

\[
                            2,3,4,5,6,7,8.                    \tag{8.1}
\]

The proofs above do not depend on that finite replay.

Proved:

1. all palette/count/lower rows of the proposed candidate;
2. physical acyclicity for every `m`;
3. two explicit degree-`m-1` owner stars for every `m>=3`;
4. the exact Hall cut for prospective head detachment.

Not proved:

1. a noncanonical assignment passing all four Hall systems;
2. simultaneous graphic independence of such an assignment;
3. rooted connector order, residence, deeper shadows, or common-cap
   compilation.

Therefore the canonical C-phase is an exact upper/lower-rainbow Catalan-
component **branching forest**, not a physical linear forest for `m>=4`.
The surviving positive target is a prospective cross-facet detachment,
not a different scalar count or an acyclicity proof.


# The `k=17` reset-conditioned chronology gate: three matroids, one exact flow face, and a scoped no-go

Date: 2026-08-01

Status: exact quotient formulation and exact functional-attachment/TU
subclass, specialized to the verified necklace-selector/two-queue-reset
coexistence theorem.  The reset owner columns extend to a full owner
transversal by authenticated H100 replay.  The independently completed
selector used in that replay is nevertheless refuted at the predecessor
matroid row.  No claim is made that every reset-compatible selector fails,
and no `k=17` universal word is constructed here.

## 0. Outcome

The correct protected reset is the **opened** quotient path of seven turns,
not the closed eight-cycle.  Fixing all eight turns creates a closed
zero-voltage reset component and cannot by itself belong to one connected
chronology.  Opening one declared rail boundary leaves seven protected turns
and one incoming/outgoing socket pair.

For a fixed equivariant flag table containing this opened reset, the exact
remaining owner-exact cycle-cover problem is a common-base problem for
three matroids on only the aligned head--owner attachment columns:

1. the head partition matroid;
2. the owner partition matroid; and
3. the legal-predecessor transversal matroid.

After deleting the seven used tails, heads, and owners, the required common
base has size

\[
                          1430-7=1423.               \tag{0.1}
\]

This is the smallest exact quotient object: expanding each predecessor into
a separate atom gives the equivalent three-shore turn hypergraph, but is
strictly larger.

There is one exact network-flow face.  If the head--owner attachment is
fixed as a bijection `theta`, the first two matroids disappear and the
third row is just a bipartite predecessor perfect matching.  Hall, max flow,
and total unimodularity are exact.

For the explicit reset bank, both the opened seven owner columns and the
closed eight owner columns extend to full quotient owner transversals:

\[
               1423/1423\quad\text{and}\quad1422/1422.        \tag{0.2}
\]

Thus the protected bank creates no owner-supply obstruction.  The unresolved
correlation is choosing the rest of the flag table and the owner transversal
so that the predecessor graph has Hall.

## 1. The aligned attachment-column ground set

Put `p=17`, `m=8`, and let

\[
 R=\binom{\mathbb Z_{17}}8/\langle\tau\rangle,
 \qquad
 O=\binom{\mathbb Z_{17}}9/\langle\tau\rangle.
\]

Both sets have size `N=1430`.  Fix one rotation-equivariant depth-three
flag orbit at every root orbit.  Normalize a turn so that its shared
one-coordinate rail state is zero.

An **aligned attachment column** `a` records:

* a head root orbit `q(a) in R`;
* an owner orbit `o(a) in O`;
* one physical phase of the incidence `q(a) subset o(a)`.

Parallel phases are retained.  Let

\[
                         P_F(a)\subseteq R             \tag{1.1}
\]

be the tail root orbits whose normalized flags can literally precede the
head flag through column `a`.  This set includes the complete depth-three
survivor test, not merely Johnson adjacency.

The verified reset has root flags

\[
 f_a=(T_a;X_a,X_{a+1}),\qquad 0\le a<8,
\]

and owner `U_a` on the turn `f_a -> f_(a+1)`.  Open the ring between
`f_7` and `f_0`, and prescribe the seven actual turns

\[
 {cal S}=\{(T_a,T_{a+1},U_a):0\le a<7\}.             \tag{1.2}
\]

Their tails, heads, and owner orbits are separately distinct.

Delete those seven tails, heads, and owners.  Let `A_S` be the remaining
attachment columns at unused heads and owners, and replace (1.1) by

\[
                  P_F^S(a)=P_F(a)-\{T_0,\ldots,T_6\}. \tag{1.3}
\]

## 2. The exact residual object

Define three matroids on `A_S`.

* `M_H` is the partition matroid with one capacity-one part for every
  unused head.
* `M_O` is the partition matroid with one capacity-one part for every
  unused owner.
* `M_P` is the transversal matroid represented by the bipartite graph from
  columns `a` to the residual tail set `P_F^S(a)`.

### Theorem 2.1 (reset-conditioned common-base theorem)

The fixed flag table has an owner-exact directed cycle cover containing all
seven turns (1.2) if and only if

\[
                       M_H,M_O,M_P
\]

have a common base of size 1423.

#### Proof

Let `D` be a common base.  Independence and cardinality in `M_H` select one
column at every residual head.  The same statement in `M_O` uses every
residual owner once.  Independence in `M_P` supplies distinct predecessor
tails, one from every selected column's set (1.3).  Since there are 1423
selected columns and 1423 residual tails, every tail is used once.  Add the
seven prescribed triples (1.2).

Conversely, remove (1.2) from any owner-exact cycle cover containing it.
The remaining attachment columns use every residual head and owner once,
and their actual predecessor tails are a transversal, so they form the
required common base. \(\square\)

This formulation already contains every statewise Hall equation and every
owner-colour equation.  It is not ordinary two-matroid intersection: the
intersection of the two partition matroids `M_H,M_O` is the head--owner
matching system, not a matroid, and adding `M_P` gives the usual
three-resource obstruction.

Equivalently, expand each pair `(a,p)`, `p in P_F^S(a)`, into a turn atom

\[
                         (p,q(a),o(a)).              \tag{2.1}
\]

A perfect matching in this tripartite hypergraph is the same object.  The
attachment-column formulation is smaller because all atoms having the same
head, owner, and phase share one transversal column.

### Corollary 2.2 (the correlated selector problem)

Let `F_reset` be the exact quotient containment-matching face from the
necklace/reset coexistence theorem.  The complete remaining static problem
is exactly

\[
 \exists F\in F_{\rm reset}:\quad
 r_{M_H(F),M_O(F),M_P(F)}=1423,                      \tag{2.2}
\]

where the right side means a three-matroid common base of that size.

The quantifier over `F` is essential.  Selecting the two containment
matchings independently and then solving (2.2) can create universally dead
tails, as Section 5 demonstrates.

## 3. The exact TU/flow face

Let `theta` be a perfect matching between the residual head and owner
resources using aligned attachment columns.  Thus `theta` chooses exactly
one column `a_q` at every residual head, and every residual owner occurs
once.  Form the bipartite graph

\[
 B_\theta=(R^-_{\rm res},R^+_{\rm res};E_\theta),
 \qquad
 pq\in E_\theta\Longleftrightarrow p\in P_F^S(a_q). \tag{3.1}
\]

### Theorem 3.1 (functional-attachment flow theorem)

For fixed `F` and `theta`, an owner-exact cycle cover containing (1.2)
exists if and only if `B_theta` has a perfect matching.  Equivalently,

\[
             |N_{B_\theta}(X)|\ge |X|
             \qquad(X\subseteq R^-_{\rm res}).       \tag{3.2}
\]

The residual linear system is totally unimodular.

#### Proof

The selected columns of `theta` already saturate the head and owner
partitions.  A common base can therefore exist precisely when these 1423
columns are independent in the predecessor transversal matroid, which is
precisely an SDR for the sets `P_F^S(a_q)`.  This is a bipartite perfect
matching.  Hall gives (3.2), and the oriented bipartite incidence matrix is
totally unimodular. \(\square\)

The same proof works with any prescribed independent turn bank, not only
the reset.  It also gives a useful exact division of labour:

* choosing `theta` is an owner-incidence perfect matching;
* checking it is one max-flow computation;
* finding some `theta` which passes Hall is the surviving non-TU
  correlation.

### Corollary 3.2 (head--owner separable support)

If the residual turn support factors as

\[
 (p,q,o)\text{ legal}
 \quad\Longleftrightarrow\quad
 pq\in G\ \text{ and }\ qo\in J,                    \tag{3.3}
\]

then exact completion is equivalent to perfect matchings in the two
bipartite graphs `G` and `J`, after deleting protected resources.

Choose a perfect matching `theta` in `J`; equation (3.3) makes
`B_theta=G`, so Theorem 3.1 applies.  Necessity is immediate from any turn
matching.  This is a second exact TU subclass.  Literal Boolean flag support
does not generally factor as (3.3).

## 4. The reset owner columns extend exactly

### Theorem 4.1 (finite owner-transversal compatibility)

For the explicit `k=17` reset template

\[
 K=\{0,1,2,3\},\qquad X=(4,5,6,7,8,9,10,11),
\]

the seven opened owner incidences

\[
                         T_{a+1}\subset U_a,
                         \qquad0\le a<7,              \tag{4.1}
\]

extend to a perfect matching between all 1430 rank-eight root necklaces and
all 1430 rank-nine owner necklaces.  The same is true after prescribing all
eight incidences of the closed reset ring.

#### Proof

Enumerate the aligned quotient rank-eight/rank-nine incidence graph, delete
the used endpoints, and run exact bipartite matching.  The residual matching
sizes are

\[
 \begin{array}{c|c|c}
 \text{bank}&\text{required}&\text{obtained}\\ \hline
 \text{opened seven}&1423&1423\\
 \text{closed eight}&1422&1422.
 \end{array}                                                   \tag{4.2}
\]

The standalone C++ replay named in Section 6 reconstructs the graph from
literal masks and verifies every forced incidence before matching. \(\square\)

Thus `M_H` and `M_O` have a common base compatible with the reset.  This
does not imply that one such base is independent in `M_P`.

## 5. Sharp scoped no-go for independent completion

The prior coexistence audit chose the two quotient containment matchings
independently, then chose the first coherent physical phase for every
unforced chain incidence.  Call the resulting exact, rail-balanced flag
table `F_ind`.

### Theorem 5.1 (the independent table fails before owner colour)

For `F_ind`, even after opening the reset ring, the residual uncoloured
state graph has maximum matching size

\[
                              850<1423,               \tag{5.1}
\]

and 406 tail root orbits have no legal successor under **any** head-owner
attachment.  With the ring closed, the corresponding number is

\[
                              849<1422.               \tag{5.2}
\]

Consequently no owner transversal `theta` and no three-matroid common base
can complete this particular table.

#### Proof

The complete normalized legal-turn catalogue is enumerated before an owner
attachment is selected.  A zero-out tail is absent from every predecessor
set `P_F(a)`, so it is a loop on the tail side of the transversal
representation for every possible `theta`.  Exact Hopcroft--Karp replay
after deleting the protected turn resources gives (5.1)--(5.2). \(\square\)

This is a theorem about one deterministic completion, not evidence that the
reset-compatible face `F_reset` is empty.  It proves that target matching,
physical phase choice, and chronology cannot be separated in that order.

## 6. Audit artifact and hashes

The H100 `-O3` replay is

`scratch/audit_k17_necklace_selector_reset_bank_20260801.cpp`,

with frozen output

`scratch/audit_k17_necklace_selector_reset_bank_20260801.txt`.

It enumerates all four quotient layers, verifies the reset resource orbits,
solves the two target-containment residual matchings, solves the opened and
closed owner-attachment residual matchings, and then enumerates the complete
legal-turn graph of `F_ind` before solving both protected residual state
matchings.

SHA-256:

* source: `7b974c89c0c87a3e34182080c02c2c7aae66b8b5318bda3d30fed0188b35ad24`;
* output: `012f211a76ebeacacca19089a8d8e5d4c03754b51f7818e5c04beebe2b2c2ab8`.

## 7. Exact frontier

The following rows are now closed:

1. exact high-target selection with the rolling-reset bank;
2. exact rail balance;
3. extension of the reset's prescribed owner columns;
4. the common-base formulation of all remaining cycle-cover rows; and
5. ordinary-flow/TU integrality after a functional owner attachment is
   fixed.

The one unresolved finite theorem is:

> Choose the two quotient containment matchings, their coherent physical
> phases, and a functional owner attachment `theta`, all conditioned on the
> opened reset bank, so that `B_theta` satisfies Hall.

This is strictly smaller than searching an unrestricted word, but it is not
an ordinary matroid-intersection theorem.  Connectedness/nonzero voltage,
residence outside the reset, arbitrary-width upper witnesses, and the final
compiler remain later rows.

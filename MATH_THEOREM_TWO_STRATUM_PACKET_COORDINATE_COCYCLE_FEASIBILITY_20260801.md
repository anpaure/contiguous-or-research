# Two swapped packet strata are necessary and sufficient for coordinate-cocycle feasibility

Date: 2026-08-01  
Lane: controlled Catalan leave / coordinate cocycle / multi-stratum repair  
Status: unconditional exact coordinate-degree construction and, for all
sufficiently large parameters, an exact resource-disjoint two-stratum
packet/hole bank.  This removes the one-stratum cocycle obstruction with
the minimum possible number of strata.  It does not construct the residual
physical forest or decorated two-factor.

The typed bank in Section 6 is asymptotic for an essential reason: its
auxiliary and target uppers both have the same two-special-coordinate
signature and occupy two disjoint rank-`(m-1)` core banks.  Hence it needs

\[
                         2C\le {2m-3\choose m-2}.                 \tag{0.0}
\]

This first holds at `m=15`.  Thus it gives no finite `m=6,7,8,9`
decorated-factor instance.  The separate-target phase-compatible
replacement is treated in
`MATH_THEOREM_CATALAN_PHASE_COMPATIBLE_PAIRED_KNESER_BLOCK_BANK_20260801.md`.

## 0. Outcome

Put

\[
 n=2m-1,\qquad W={2m-1\choose m},\qquad
 C=\operatorname {Cat}_m,qquad c=\operatorname {Cat}_{m-1},
\]

and

\[
                         I=C-2c={m-2\over2m-1}C.     \tag{0.1}
\]

For every upper-exact odd owner-slot forest, let `E_t` be the number of
free endpoint slots whose physical owner contains coordinate `t`, and let
`H_t` be the number of unused rank-`(m-1)` lower colours containing `t`.
The coordinate cocycle gives

\[
                              E_t=H_t+2c.             \tag{0.2}
\]

One full mixed-head packet stratum has all `2C` final provider endpoints
containing its distinguished coordinate `a`.  It therefore has
`E_a=2C`, which would require `H_a=2C-2c>C`.  One stratum is impossible.

This note proves that **two** strata remove the entire coordinate
obstruction.  Fix two coordinates `alpha,beta` and use the swapped strata

\[
             (a,z)=(\alpha,\beta),qquad
             (a,z)=(\beta,\alpha).                  \tag{0.3}
\]

There is an exact `C`-packet abstract core bank, split into orders

\[
        s_\alpha+s_\beta=C,qquad
        I\le s_\alpha,s_\beta\le2c,                 \tag{0.4}
\]

whose endpoint degrees are

\[
\boxed{
 E_\alpha=C+s_\alpha,qquad
 E_\beta=C+s_\beta,qquad
 E_t=C\quad(t\notin\{\alpha,\beta\}).}              \tag{0.5}
\]

The forced hole vector is consequently

\[
\boxed{
 H_\alpha=C+s_\alpha-2c,qquad
 H_\beta=C+s_\beta-2c,qquad
 H_t=I\quad(t\notin\{\alpha,\beta\}).}              \tag{0.6}

Every entry lies in `[0,C]`, its sum is `(m-1)C`, and an explicit energy
balancing argument constructs `C` **distinct** rank-`(m-1)` sets having
exactly this degree vector.

Thus two strata are coordinate-feasible and one is not.  Section 6 also
chooses all target, lower and owner-slot tickets disjointly and keeps the
hole family outside the reserved lower banks.  The remaining owner-layer
problem is the decorated two-factor completion.  No scalar or singleton-
coordinate cut prevents that step.

## 1. The endpoint contribution of one packet

Let

\[
                  G=\Omega-\{a,z\},\qquad |G|=2m-3,
\]

and choose disjoint rank-`(m-2)` sets `S,J subset G`.  Put

\[
                              L=G-J.                 \tag{1.1}
\]

Then `|L|=m-1` and `S subset L`.  The off-provider endpoints are

\[
                              A=aL,qquad C_0=azS.    \tag{1.2}
\]

On the ordinary coordinates `G`, their total incidence vector is

\[
 \chi_L+\chi_S
   =\mathbf1_G+\chi_S-\chi_J.                       \tag{1.3}
\]

On the two special coordinates the endpoint contribution is

\[
                              2\chi_a+\chi_z.        \tag{1.4}
\]

Equation (1.3) is the key.  Along a directed circulation

\[
                S_1\to S_2\to\cdots\to S_q\to S_1
\]

of pairwise-disjoint Kneser adjacencies, the signed terms telescope:

\[
 \sum_{i=1}^q(\mathbf1_G+\chi_{S_i}-\chi_{S_{i+1}})
                         =q\mathbf1_G.              \tag{1.5}
\]

Thus a `C`-vertex Kneser circulation makes every ordinary coordinate occur
in exactly `C` endpoint slots, independently of how its vertices are
assigned to the two swapped strata.

## 2. A Kneser circulation of every sufficiently large Catalan order

Let

\[
             r=m-2,qquad |G|=2r+1,qquad
             \mathcal K=KG(2r+1,r).                 \tag{2.1}
\]

This is the odd Kneser graph.  A directed edge `S->J` of `mathcal K`
supplies exactly the packet core (1.1).

### Lemma 2.1 (large matching and one odd cycle)

For all sufficiently large `m`, `mathcal K` contains a vertex-disjoint
union of cycles having exactly `C` vertices.

#### Proof

First obtain a cycle cover of `mathcal K`.  Choose any incidence bijection

\[
 \sigma:{G\choose r}\longrightarrow {G\choose r+1},
 \qquad S\subset\sigma(S),                          \tag{2.2}
\]

and put

\[
                              \theta(S)=G-\sigma(S). \tag{2.3}
\]

Then `theta` is a permutation of the rank-`r` sets and
`S cap theta(S)=emptyset`.  Taking alternate edges in every cycle of
`theta` gives a matching of order at least `|V(mathcal K)|/3`.

Since

\[
 {C\over |V(\mathcal K)|}
 ={4(2m-1)\over m(m+1)}=O(m^{-1}),                 \tag{2.4}
\]

this matching contains `C/2` edges whenever `C` is even and `m` is large.
Replace every matching edge by its directed two-cycle.

If `C` is odd, use first the standard odd cycle of length `2r+1` in
`KG(2r+1,r)`: take cyclic intervals of length `r` whose starting points
advance by `r` modulo `2r+1`.  Consecutive intervals are disjoint and
`gcd(r,2r+1)=1`.  Delete its `2r+1` vertices from the matching above.  This
destroys at most `2r+1` matching edges; the surviving matching still has
more than `(C-(2r+1))/2` edges for all sufficiently large `m`.  Add that
many directed two-cycles.  The total number of circulation vertices is
exactly `C`. \(\square\)

## 3. Assign the two swapped strata

Choose

\[
                  s_\alpha=\lfloor C/2\rfloor,qquad
                  s_\beta=\lceil C/2\rceil.         \tag{3.1}
\]

For all sufficiently large `m`,

\[
                         I\le s_\alpha,s_\beta\le2c. \tag{3.2}
\]

Indeed

\[
                 2c-{C\over2}={3c\over m+1}>0,      \tag{3.3}
\]

and the integer margin tends to infinity.  Label any `s_alpha` vertices of
the circulation by stratum `(alpha,beta)` and all others by
`(beta,alpha)`.

Equation (1.5) gives `E_t=C` on `G`.  A first-stratum packet contributes
two at `alpha` and one at `beta`; a second-stratum packet contributes one
at `alpha` and two at `beta`.  Hence

\[
 E_\alpha=2s_\alpha+s_\beta=C+s_\alpha,
 \qquad
 E_\beta=s_\alpha+2s_\beta=C+s_\beta,              \tag{3.4}
\]

which proves (0.5).  Subtracting `2c` proves (0.6), and (3.2) gives

\[
                           0\le H_t\le C             \tag{3.5}
\]

for every coordinate.

## 4. Realize the forced hole vector by distinct lower sets

Set

\[
 n_2=2I,qquad
 n_\alpha=s_\alpha-I,qquad
 n_\beta=s_\beta-I.                                \tag{4.1}
\]

These numbers are nonnegative and sum to `C`.  We seek the hole family in
three signature classes:

\[
\begin{array}{c|c|c}
\text{signature}&\text{number}&\text{ordinary part in }G\\ \hline
\alpha\beta&n_2&m-3\\
\alpha\bar\beta&n_\alpha&m-2\\
\bar\alpha\beta&n_\beta&m-2.
\end{array}                                         \tag{4.2}
\]

The special-coordinate degrees are

\[
 n_2+n_\alpha=C+s_\alpha-2c=H_\alpha,
 \qquad
 n_2+n_\beta=C+s_\beta-2c=H_\beta.                \tag{4.3}
\]

The total number of ordinary incidences is

\[
 n_2(m-3)+(n_\alpha+n_\beta)(m-2)
 =C(m-2)-2I
 =(2m-3)I.                                          \tag{4.4}
\]

Thus the average ordinary-coordinate degree is exactly `I`.

### Lemma 4.1 (balanced distinct signature families)

For all sufficiently large `m`, one can choose the three simple families
in (4.2) so that every coordinate of `G` occurs exactly `I` times in their
ordinary parts.  Moreover, the ordinary parts of the two one-special
classes may be required to be disjoint.

#### Proof

First choose one simple family `F_2` of `n_2` rank-`(m-3)` sets and one
simple family `F_1` of `n_alpha+n_beta` rank-`(m-2)` sets.  There are enough
available subsets for large `m`: every prescribed family has density
`O(1/m)` in its relevant central layer.

Among all such pairs minimize the sum of squares of the ordinary
coordinate degrees.  Suppose `d_u>=d_v+2`.  Summed over the two families,
there are more selected sets containing `u` and not `v` than selected sets
containing `v` and not `u`.  Hence in at least one family the same
strict inequality holds.  The swap

\[
                         X\longmapsto X-u+v           \tag{4.5}
\]

is a bijection between the two corresponding subfamilies of the complete
uniform layer.  Therefore some selected set containing `u` and not `v`
has an unselected swap; otherwise the strict inequality would reverse.
Performing that
swap preserves the class size and simplicity and strictly lowers the
degree-square sum, a contradiction.

Thus all ordinary degrees differ by at most one.  Their average is the
integer `I` by (4.4), so every degree equals `I`.

Finally partition `F_1` arbitrarily into classes of sizes `n_alpha` and
`n_beta`.  The ordinary degrees do not change, and the two one-special
ordinary families are disjoint by construction.  This proves the stated
strengthening. \(\square\)

Combining (4.2)--(4.4) gives `C` distinct rank-`(m-1)` sets with degree
vector (0.6).  This proves exact coordinate-cocycle feasibility.

## 5. Minimum-stratum theorem and scope

### Theorem 5.1

At the singleton-coordinate level, the minimum number of full packet
strata needed for a `C`-packet terminal interface is exactly two.

#### Proof

One stratum fails at its active coordinate by `E_a=2C>C+2c` for `m>=3`.
Sections 1--4 construct a feasible endpoint and lower-hole degree vector
from two swapped strata. \(\square\)

Section 6 closes the first three typed rows by a different Kneser-pair
selection.  The residual forest exposing the chosen `B,D` slots remains
open.

## 6. Exact typed two-stratum packet bank

The coordinate construction above used an arbitrary Kneser circulation.
For typed resource separation, it is better to use disjoint Kneser
two-cycles and one exceptional directed edge when `C` is odd.

Let

\[
                  N={2m-3\choose m-2},\qquad d_K=m-1             \tag{6.1}
\]

be the order and degree of `KG(2m-3,m-2)`.  Fix an incidence bijection

\[
 \beta:{G\choose m-2}\longrightarrow {G\choose m-1},
 \qquad T\subset\beta(T),                                      \tag{6.2}
\]

and define

\[
                         \eta(T)=G-\beta(T).                     \tag{6.3}
\]

Then `eta` is a permutation of the Kneser vertices, `T cap eta(T)=emptyset`,
and the undirected graph

\[
                         H_\eta=\{\{T,\eta(T)\}:T\}             \tag{6.4}
\]

has maximum degree two.

### Lemma 6.1 (many `eta`-independent Kneser pairs)

Let `F` be any forbidden vertex family of order `O(C/m)`.  For all
sufficiently large `m`, there are `floor(C/2)` pairwise vertex-disjoint
Kneser edges whose endpoint set `P` avoids `F` and satisfies

\[
                         P\cap\eta(P)=\varnothing.               \tag{6.5}
\]

If one prescribed vertex and one prescribed partner are removed first,
the same assertion holds with `(C-1)/2` pairs.

#### Proof

Maintain an available vertex set.  Select a Kneser edge not belonging to
`H_eta`, retain both endpoints, and delete their closed `H_eta`-
neighbourhood.  Each step deletes at most six vertices and preserves
(6.5).

Before the last required step the total number removed is at most

\[
                         |F|+3C+O(1)<N/4                         \tag{6.6}
\]

for all sufficiently large `m`, since `C/N=O(1/m)`.  The full Kneser graph
has `Nd_K/2` edges, and deleting `R<N/4` vertices destroys at most `Rd_K`
edges.  Hence the available graph has more than `Nd_K/4>N` edges.  But
`H_eta` has at most `N` edges.  An available Kneser edge outside `H_eta`
therefore remains.  Greedy iteration proves the lemma. \(\square\)

### Theorem 6.2 (typed packet/hole bank)

For all sufficiently large `m`, there are exactly `C` controlled packets,
split between the swapped strata `(alpha,beta)` and `(beta,alpha)`, such
that

1. every auxiliary upper, target upper, old lower and new lower resource
   is distinct;
2. all four packet owner banks `A,B,C_0,D` are disjoint;
3. the forced `C`-set lower-hole family is simple and disjoint from both
   packet lower banks; and
4. the endpoint and hole vectors satisfy the coordinate cocycle exactly.

#### Proof: even `C`

Use Lemma 4.1 and let `F_1` be the union of the ordinary parts of the two
one-special hole classes.  Apply Lemma 6.1 with `F=F_1`.  For every chosen
Kneser pair `{S,J}`, create two packets:

\[
 \begin{array}{c|c|c}
 \text{packet vertex}&L&V\\ \hline
 S&G-J&\beta(S)\\
 J&G-S&\beta(J).
 \end{array}                                                     \tag{6.7}
\]

Because the edge `{S,J}` is not in `H_eta`, `beta(S)` differs from `G-J`
and `beta(J)` differs from `G-S`; equivalently the added element of each `V` lies in the
opposite Kneser vertex, as required by the packet identity.  Assign one
packet of each pair to each swapped stratum.

The `S` bank is injective, the `L` bank is its complement image, and the
`V` bank is injective because `beta` is a bijection.  Moreover

\[
 \beta(T)=G-T'\quad\Longleftrightarrow\quad \eta(T)=T'.          \tag{6.8}
\]

Thus (6.5) says exactly that the `V` and `L` banks are disjoint.  All typed
upper, lower and owner collisions now separate either by these three bank
injections or by their `alpha,beta` signatures.  Since `P` avoids `F_1`,
an old lower `alpha S` or `beta S` is never a hole of the same signature;
new lowers have no special coordinate while every hole has at least one.

Every pair contributes `2*1_G` to the ordinary endpoint vector, so the
hole family of Lemma 4.1 has exactly the required cocycle degrees.

#### Proof: odd `C`

Start with the balanced families `F_2,F_1` from Lemma 4.1.  The odd Kneser
graph is connected, while `F_1` is nonempty and proper.  Choose a boundary
edge

\[
                         J-S,qquad J\in F_1,quad S\notin F_1.  \tag{6.9}
\]

Put `J` in the smaller of the two one-special signature classes, call that
special coordinate `gamma`, and assign the exceptional packet at `S` to
the opposite active stratum.  Replace the hole with ordinary part `J` by
the same-signature hole with ordinary part `S`.  The ordinary hole degrees
change by

\[
                              \chi_S-\chi_J.                     \tag{6.10}
\]

Choose `b in J`, prescribe `beta(S)=S+b`, and extend this incidence edge to
the bijection (6.2).  This extension exists because a regular bipartite
incidence graph has a one-factorization.  In particular
`beta(S)` differs from `G-J`.

Delete `F_1` and the closed `H_eta`-neighbourhoods of `S,J`, and use Lemma
6.1 to choose `(C-1)/2` further Kneser pairs.  Formula (6.7) defines their
packets.  The exceptional packet uses `L=G-J,V=beta(S)`.  The same argument
from (6.8) proves all typed bank injections.

The paired packets contribute `(C-1)1_G`; the exceptional packet contributes

\[
                         1_G+\chi_S-\chi_J.                      \tag{6.11}
\]

The modified hole family has ordinary degree vector
`I*1_G+chi_S-chi_J`, exactly as required by the cocycle.  Its exceptional
new hole has special signature `gamma`, whereas the exceptional old lower
uses the opposite active coordinate, so they do not collide.  All paired
vertices avoid `F_1`, and the other signature arguments are unchanged.
This proves all four claims. \(\square\)

### Corollary 6.3 (remaining gate)

The multi-stratum repair no longer has a target/provider, lower-hole or
owner-ticket selection problem.  Its exact remaining owner-layer task is:

> complete the typed packet bank to a spanning decorated two-factor whose
> every cycle meets a packet middle edge.

Deleting those middle edges would give the required upper-exact linear
forest.  Existence of this decorated factor, and its later all-width and
residence integration, are not proved here.

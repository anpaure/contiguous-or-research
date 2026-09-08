# Orbit-weighted actuator planting, the exact guarded star-surcharge cut, and a laminar upper-decorated face

Date: 2026-08-01  
Lane: L, all-`k` physical lift after canonical age stocking  
Status: unconditional orbit-Hall, orbit-simple seed, exact protected
two-factor criterion, and a sharp linear counterexample; conditional
polynomial integral upper-decorated face.  No full protected Catalan host or
new bound on `nu(k)` is claimed.

## 0. Outcome

The age-level Hall problem is already closed by
`MATH_THEOREM_AGE_LEVEL_CANONICAL_ACTUATOR_STOCKING_20260801.md`.  This note
does not repeat it.  It starts with the stocked all-positive actuator paths
and proves the strongest physical extension statements currently justified.

1. Orbit compression has an exact all-group Hall theorem.  Composite-`k`
   stabilizers enter as orbit-size weights; unweighted quotient Hall is
   sound when all relevant orbit sizes are equal (in particular, on equal
   free orbits).
2. For every sufficiently large `k`, one short all-positive age path can be
   labelled so that all its owners and lower/upper `q1` colours occupy
   pairwise distinct free rotation orbits.  If one age template occurs
   exactly `k` times, its `O(kd)` physical owner/`q1` bank therefore compresses
   to `O(d)` quotient objects.
3. This does not compress an arbitrary stocked law.  A free orbit preserves
   the age template and contributes exactly `k` copies; split multiplicities
   are a divisibility obstruction.  Marked suffixes, arbitrary-width upper
   witnesses, and common-cap cells are additional literal bundle resources.
4. For any prescribed degree-two bank in the odd middle-level incidence
   graph, an exact guarded Ore--Ryser cut characterizes extension to a
   spanning `q1` two-factor.  A bank of only `2n-2` edges, consisting of
   disjoint locally rainbow paths, violates one cut.  Thus polynomial size,
   degree two, and local palettes do not imply extension.
5. After protected contraction, a clean standard polynomial integral
   face for the upper-decorated forest is laminar-resource matroid
   intersection with the graphic matroid.  Crossing tail, head, upper-colour,
   and cap blocks leave the two-matroid face.

The exact frontier is therefore not another stocking theorem.  It is either
a coherent free-orbit **bundle** factor satisfying the weighted quotient
cuts, or a prospective degree-two bank satisfying every guarded
star-surcharge cut and the laminar/graphic upper-decoration rows.

## 1. Exact size of the stocked physical bank

For actuator parameter `(q,u)`, put

\[
                         j_u=d-u+1.
\]

If `a_(q,u)` bad occurrences are selected, define

\[
\begin{aligned}
 A&=\sum_{q,u}a_{q,u},\\
 M&=\sum_{q,u}(j_u+1)a_{q,u},\\
 J&=\sum_{q,u}j_ua_{q,u}=M-A.                       \tag{1.1}
\end{aligned}
\]

Cutting each actuator cycle gives a path on `j_u+1` owner occurrences with
`j_u` Johnson turns.  Its lift to the middle-level incidence graph has
`2j_u` incidence edges.  Hence the complete prescribed bank `P` has

\[
                         |E(P)|=2J.                  \tag{1.2}
\]

The canonical top-mark row gives

\[
 A\le k,\qquad M\le k(d+1),\qquad J\le kd,\qquad
 |E(P)|\le2kd.                                      \tag{1.3}
\]

These are worst-case bounds.  The orders are `Theta(kd)` only when
`A=Theta(k)` and the average `j_u` is `Theta(d)`.  They count reassigned
existing owner/type occurrences, not new word positions.  The physical
sidecar theorem proves only `Omega(a/d)` new letters for a dedicated local
sidecar; it does not prove that `Theta(ad)` host occurrences are necessary.

## 2. Orbit-weighted Hall and coherent bundle lifting

Let a finite group `Gamma` act on a bipartite graph `H=(L,R;E)` by graph
automorphisms.  Let `Ob_L,Ob_R` be its vertex-orbit sets, and let
`Nbar(X)` denote the right orbits adjacent in quotient support to a family
`X subset Ob_L`.

### Theorem 2.1 (orbit-weighted Hall)

`H` has a matching saturating `L` if and only if

\[
 \boxed{
  \sum_{O\in X}|O|
      \le \sum_{Q\in\overline N(X)}|Q|
      \qquad(X\subseteq\operatorname{Ob}_L).}        \tag{2.1}
\]

#### Proof

Necessity is Hall applied to the union of the left orbits in `X`.

For sufficiency, suppose Hall fails and put

\[
                         f(S)=|S|-|N(S)|.             \tag{2.2}
\]

Neighbourhood size is submodular, so `f` is supermodular.  Choose an
inclusion-maximal set `S` among the sets attaining the maximum value of
`f`.  Every translate `gS` has the same maximum value.  Supermodularity gives

\[
 f(S\cup gS)+f(S\cap gS)\ge f(S)+f(gS).             \tag{2.3}
\]

Both terms on the left are at most the maximum, so both are maxima.
Maximality forces `S union gS=S`; equal cardinalities then give `gS=S`.
Thus `S` is invariant and is a union of left orbits.  Its neighbourhood is
a union of right orbits, contradicting (2.1).  \(\square\)

When all relevant orbits are free and have common order `|Gamma|`, the
weights cancel and (2.1) is ordinary quotient Hall.  They cannot be omitted
in general.  Under `Z_4`, the singleton orbit has size four while the orbit
of `{0,2}` has size two.  Containment gives one quotient edge, so unweighted
Hall passes, but weighted Hall reads `4<=2` and correctly fails.

### Definition 2.2 (literal host bundle)

A protected actuator host bundle contains, as one indivisible object,

1. the ordered source block and both endpoint age/residence states;
2. every owner and lower/upper `q1` incidence;
3. the complete internal interval-OR deck and the prefix/suffix OR chains;
4. every named arbitrary-width upper witness ticket;
5. the cross-boundary interval deck for its declared connector; and
6. every occurrence cell, envelope, and trace/common-cap guard.

A packet-to-bundle quotient edge is legal only when **one common phase**
`delta` realizes every item in this list.

### Corollary 2.3 (free coherent bundle lift)

Suppose packet orbits and host-bundle orbits are free, all have order
`|Gamma|`, distinct physical host-bundle nodes are resource-private, and a
packet orbit's translates are internally disjoint in every declared unit
resource.  If a quotient edge records one common legal phase, a quotient
matching lifts, edge by edge, to resource-disjoint physical packet
embeddings: choose one allowed phase on each quotient edge and translate it
through the group.

Without bundling, separate owner, lower, upper, and cap Hall systems do not
compose.  Already for `Z_3`, let the first ticket of packet phase `g` require
bundle phase `g`, and the second require phase `g+1`.  Each projected ticket
graph is a perfect matching, but no packet has one common legal bundle
phase.

For an external carrier, common-cap legality in a bundle remains the literal
condition

\[
 A_p(M)=\overline E_p\cap
        \bigcap_{(S,C)\in M:\ p\in C}S\ne\varnothing,              \tag{2.4}
\]

together with target-cell reproduction

\[
                         \bigcup_{p\in C}A_p(M)=S                 \tag{2.5}
\]

for every selected cell `(S,C)` and every protected-row requirement.  Orbit
translation copies a proved equation; it does not prove (2.4)--(2.5).

## 3. A positive free-orbit seed for one all-positive path

Fix a cyclic coordinate order `rho` on `[k]` and define

\[
 \Delta_\rho(T)=\min_{1\le g<k}|T\mathbin\triangle\rho^gT|.        \tag{3.1}
\]

### Lemma 3.1 (large cyclic displacement at central rank)

For all sufficiently large `k`, there is a set `T` of size
`r=ceil(k/2)` with

\[
                            \Delta_\rho(T)>k/4.                    \tag{3.2}
\]

#### Proof

Choose a Bernoulli-`1/2` random subset.  For fixed nonzero `g`, the random
variable `D_g=|T triangle rho^gT|` has expectation `k/2`.  Changing one
coordinate changes `D_g` by at most two.  Bounded differences therefore
gives

\[
                         \Pr(D_g\le k/4)\le e^{-k/32}.             \tag{3.3}
\]

A union bound over `g` is at most `k e^(-k/32)`.  Meanwhile the probability
of central size is `Theta(k^(-1/2))`.  For large `k` the latter exceeds the
bad-shift probability, so some central-size set satisfies (3.2). \(\square\)

### Lemma 3.2 (orbit-simple fresh-token path)

Let `T_0,...,T_ell` be the fresh-token lift of a legal all-positive age path,
and assume `ell<=d+1`.  If

\[
                         \Delta_\rho(T_0)>4\ell+2,                 \tag{3.4}
\]

then

* every owner, lower `q1` colour, and upper `q1` colour on the path has a
  free rotation orbit; and
* resources of the same rank at different path positions lie in different
  rotation orbits.

#### Proof

Every Johnson step changes two coordinates, so

\[
                         |T_i\triangle T_0|\le2\ell.              \tag{3.5}
\]

A lower or upper `q1` colour differs from its adjacent owner by one
coordinate and hence from `T_0` in at most `2ell+1` coordinates.  If two
same-rank resources `R_i,R_j` were related by a nonzero rotation, then the
triangle inequality would give

\[
 |T_0\triangle\rho^gT_0|
   \le |T_0\triangle R_j|+|R_i\triangle T_0|
   \le4\ell+2,                                      \tag{3.6}
\]

contrary to (3.4).  The same argument with `i=j` proves freeness.  Equality
at shift zero is excluded by the fresh-token path lemma. \(\square\)

If a marked suffix `S_i subset T_i` has deficit at most `b`, then

\[
                         |S_i\triangle T_0|\le2\ell+b.             \tag{3.7}
\]

Thus physically distinct equal-rank marked suffixes are also free and
orbit-distinct under the stronger condition

\[
                         \Delta_\rho(T_0)>4\ell+2b.                \tag{3.8}
\]

For every `R_p` target and every non-singleton near-owner target of `X`, one
has `b=O(d)`.  The one singleton target of `X` is handled separately by the
free but globally unique singleton rotation orbit.  One full marked
`X`-template orbit consumes that orbit; two independently marked `X` packet
orbits would collide.  The two `Y` donor targets may have deficits involving
`q`; unrestricted large `q` is not covered by this robust-core argument.
Physical distinctness of equal-rank suffixes is likewise a survivor-choice
row, not an age-profile consequence.

### Corollary 3.3 (one full template orbit)

For `ell=O(sqrt(k))`, the fresh-token condition `k-r>=ell` holds eventually,
and Lemmas 3.1--3.2 produce an owner/`q1` orbit-simple lift of one path.  Its
`k` rotations are `k` owner/`q1`-resource-disjoint Johnson paths, so
`Theta(k ell)` physical owner/`q1` incidences are represented by `O(ell)`
quotient objects.  Marked suffix, arbitrary-width, source-cell, and cap
resources remain subject to Definition 2.2 and the caveats above.

This positive statement has three exact limits.

1. Rotation preserves `(q,u)` and the age template.  A union of free packet
   orbits realizes multiplicity `a_(q,u)` only when `k` divides that
   multiplicity.  Since `0<=a_(q,u)<=k`, this means `0` or `k`.  A total of
   `k` occurrences split among several templates is not one orbit.
2. For composite `k`, shorter stabilizer orbits require the weights in
   Theorem 2.1 and represent fewer than `k` distinct copies.  Counting one
   as a full free orbit would incorrectly reuse periodic unit resources.
3. On a free regular `Z_k` voltage lift, a quotient cycle of voltage `v`
   lifts to `gcd(k,v)` cycles.  More generally, for connected quotient
   support in a regular cover, the closed-walk voltages must generate the
   effective fibre group; merely asking for nonzero voltage is insufficient
   at composite `k`.  With one common stabilizer `H`, the same statement
   applies to the effective regular fibre `Z_k/H`.  With varying stabilizers,
   weighted orbit Hall still decides matching existence, but lift topology
   additionally needs stabilizer/coset transition data (for example, a
   graph-of-groups formulation).

## 4. Exact guarded extension of an arbitrary degree-two bank

Let `ML_n` be the `n`-regular containment graph between ranks `n-1` and `n`
of `[2n-1]`, with shores \(\mathcal L,\mathcal U\).  This is the odd Catalan host
`k=2n-1`; the orbit theorems above are all-`k`, while an even-dimensional
physical host needs its own incidence analogue.  Let `P subset ML_n` be a
prescribed simple bank with `Delta(P)<=2`.  For \(C\subseteq\mathcal L\), put

\[
                         W=|\mathcal L|=|\mathcal U|
                           ={2n-1\choose n}.                         \tag{4.0}
\]

\[
\begin{aligned}
 d_C(U)&=|N(U)\cap C|,\\
 p_C(U)&=|E(P)\cap(C\times\{U\})|,\\
 r_P(x)&=2-d_P(x).                                  \tag{4.1}
\end{aligned}
\]

### Theorem 4.1 (exact star-surcharge Ore--Ryser cut)

`P` extends to a spanning `q1` two-factor of `ML_n` if and only if, for every
\(C\subseteq\mathcal L\),

\[
 \boxed{
  \sum_{U\in\mathcal U}\bigl(d_C(U)-n+2-p_C(U)\bigr)_+
       \le \sum_{x\in C}r_P(x).}                    \tag{4.2}
\]

#### Proof

Delete `P` and prescribe residual degree `b(v)=2-d_P(v)`.  Ore--Ryser for
the residual bipartite `b`-factor says that for every
\(A\subseteq\mathcal L\),

\[
 \sum_{x\in A}b(x)
   \le \sum_{U\in\mathcal U}\min\{b(U),d_{ML_n-P}(U,A)\}.   \tag{4.3}
\]

Put \(C=\mathcal L\setminus A\) and write `p(U)=d_P(U)`.  Then

\[
\begin{aligned}
 d_{ML_n-P}(U,A)
   &=n-d_C(U)-p(U)+p_C(U),\\
 \min\{2-p(U),d_{ML_n-P}(U,A)\}
   &=2-p(U)-\bigl(d_C(U)-n+2-p_C(U)\bigr)_+.        \tag{4.4}
\end{aligned}
\]

Both shores have total residual demand
\(2|\mathcal L|-|E(P)|\).  Subtracting the
demand on `C` from the left total and substituting (4.4) cancels the totals;
the result is exactly (4.2). \(\square\)

The left side is a **near-complete-star surcharge**: an upper vertex
contributes only when `C`, after crediting its prescribed incident edges,
occupies all but at most one of its lower facets.

### Corollary 4.2 (fixed forbidden-ticket catalogue)

Let `Z` be a fixed set of forbidden completion edges, disjoint from `P`, and
put

\[
 z_A(U)=|E(Z)\cap(A\times\{U\})|,
 \qquad A=\mathcal L\setminus C.                     \tag{4.5}
\]

There is a two-factor containing `P` and avoiding `Z` if and only if

\[
 \boxed{
  \sum_{U\in\mathcal U}
   \bigl(d_C(U)+z_A(U)-n+2-p_C(U)\bigr)_+
       \le \sum_{x\in C}r_P(x)
       \qquad(C\subseteq\mathcal L).}               \tag{4.6}
\]

This is Theorem 4.1 with `z_A(U)` further deleted `A`-to-`U` incidences in
(4.4).  It is exact when upper/common-cap protection has already been
compiled into a fixed edge-forbidden catalogue.  Nonlocal interval choices
and nonprivate cap conflicts are not fixed-edge constraints and do not enter
(4.6) without an additional state expansion.

### The minimum additional expansion hypothesis

For the complete literal strand bank, define its guarded co-star load and
residual lower credit by

\[
\begin{aligned}
 \sigma_{P,Z}(C)
   &=\sum_{U\in\mathcal U}
       \bigl(d_C(U)+z_{\mathcal L\setminus C}(U)
                    -n+2-p_C(U)\bigr)_+,\\
 \kappa_P(C)&=\sum_{x\in C}(2-d_P(x)).              \tag{4.7}
\end{aligned}
\]

Then the exact min-cut deficiency is

\[
 \boxed{
 \delta_{\rm star}(P,Z)
    =\max_{C\subseteq\mathcal L}
       \bigl(\sigma_{P,Z}(C)-\kappa_P(C)\bigr)_+.}   \tag{4.8}
\]

The bank extends while avoiding `Z` if and only if
`delta_star(P,Z)=0`.  This is the smallest possible additional expansion
hypothesis: it is both necessary and sufficient, and it is testable by one
bipartite `b`-flow/min-cut computation even though (4.8) displays all cuts.

There is a particularly transparent mandatory subfamily.  Let `S` be the
set of saturated lower vertices of `P`.  For every `C subseteq S`, the
credit is zero, so (4.7)--(4.8) force, when `Z` is empty,

\[
                 d_C(U)\le n-2+p_C(U)
                 \qquad(U\in\mathcal U).             \tag{4.9}
\]

Thus an unpaired near-complete star (`p_C(U)=0,d_C(U)=n-1`) is already a
one-unit obstruction; a full star needs two prescribed incidences back into
its centre.  Pairwise owner/`q1` disjointness contains no such expansion
information.

### Proposition 4.3 (sharp linear protected-bank obstruction)

For every `n>=3`, there is a bank `P` consisting of `n-1` vertex-disjoint
two-edge paths, with distinct owners and distinct paired-upper colours,
which is contained in no spanning `q1` two-factor.

#### Proof

Fix \(U_0\in\mathcal U\), omit one element `i_0 in U_0`, and let

\[
 C=\{L_i=U_0\setminus\{i\}:i\in U_0\setminus\{i_0\}\}.            \tag{4.10}
\]

Choose distinct letters `a,b` outside `U_0`.  For every `L_i in C`, prescribe
the path

\[
       (U_0-\{i\}+\{a\})-L_i-(U_0-\{i\}+\{b\}).                  \tag{4.11}
\]

All lower vertices and all owner endpoints are distinct, and the paired
upper colours `U_0-{i}+{a,b}` are distinct.  Every `L_i` has prescribed
degree two, so the right side of (4.2) is zero.  At the unused owner `U_0`,

\[
                         d_C(U_0)=n-1,\qquad p_C(U_0)=0,           \tag{4.12}
\]

and its surcharge is one.  Thus (4.2) reads `1<=0`. \(\square\)

Consequently no theorem based only on polynomial size, maximum degree two,
local lower/upper rainbows, or bounded pair codegrees can extend the complete
actuator bank.  The star-surcharge cuts, or a structural certificate implying
them, are indispensable.  Applied to the stocked bank with `|E(P)|=2J`, the
exact additional owner/`q1` hypothesis is therefore

\[
                         \delta_{\rm star}(P,Z)=0,                 \tag{4.13}
\]

not merely `2J=O(kd)=o(W)`.  The obstruction persists in every dimension and
already has order `O(k)`, so there is no asymptotic implication from
pairwise owner/`q1` disjointness.

### Corollary 4.4 (orbit-compressed cut reduction)

If a group acts shore-preservingly and preserves `ML_n`, `P`, and `Z`,
infeasibility of the residual `b`-flow has a group-invariant minimum cut: the
union of all translates of a minimum source-side cut is again minimum by cut
submodularity.  Hence it is enough in (4.6) to test invariant `C`, retaining
their orbit-size weights.  A complementing action which swaps the two shores
does not preserve the directed source/sink network and is outside this
statement.

On a free equal-orbit face the common orbit size cancels, giving a literal
quotient surcharge system.  This is the exact incidence-factor reduction
promised by orbit compression.  It is not automatic positivity: a quotient
near-complete-star surcharge can still violate the cut.

## 5. A standard integral upper-decorated face

The two-factor cut controls only owners and lower `q1`.  Immediate-upper
coverage, few components, arbitrary-width witnesses, and a common cap remain
correlated.

Properly two-edge-colour the protected path bank as `P=P_0 dotunion P_1`.
Fix a perfect matching `M_0` of `ML_n-P_1` containing `P_0`.  For every candidate edge
`e=LU` outside `M_0`, define

\[
 \operatorname{up}_{M_0}(e)=M_0(L)\cup U,
 \qquad
 \lambda_{M_0}(e)=\{L,M_0^{-1}(U)\}.               \tag{5.1}
\]

The first is its immediate-upper colour and the second its edge-labelled
graphic link on the lower shore.

Assume first that the forced `P_1` bundles are independent in every unit
tail, head, slot, and private-ticket resource, and that their links are
acyclic.  Contract the forced edges, bundles, and links.  Immediate-upper
labels are coverage resources, so repeated labels already supplied by
`P_1` are permitted; only the still-missing labels become unit blocks below.
Let `E` be the disjoint union of the `N` candidate blocks labelled by those
missing immediate-upper colours.  Assume:

1. every candidate carries one complete literal bundle from Definition 2.2;
2. all unit-capacity upper-colour, tail, head, slot, and private-ticket blocks
   form one laminar family; and
3. selecting inside this laminar system keeps all fixed trace/common-cap
   guards valid.

The unit constraints define one laminar matroid `M_lam` on `E`.  The links
define the contracted graphic matroid `M_gr`.

### Theorem 5.1 (laminar upper-colour forest selector)

Let `N` be the number of immediate-upper colours not already supplied by
the protected contraction.  There is a bundle-safe selection `Q_0` which
contains one representative of every missing upper colour and whose links
remain a forest if and only if

\[
 \boxed{
 r_{\rm lam}(X)+r_{\rm gr}(E\setminus X)\ge N
                   \qquad(X\subseteq E).}            \tag{5.2}
\]

#### Proof

Independence in `M_lam` enforces every unit resource, including at most one
edge of each upper-colour block.  A common independent set of size `N`
therefore uses every one of the `N` colour blocks exactly once.  Independence
in `M_gr` is precisely acyclicity after the protected links are contracted.
Edmonds' matroid-intersection min--max theorem gives (5.2). \(\square\)

This is a genuine polynomial integral face (polynomial in the explicit
catalogue size).  A functional/private catalogue, in which different colour
lists have disjoint tail, head, and ticket resources, is its simplest case.

The selection `Q_0` is only the upper-decorated Catalan forest seed.  Let its
contracted link forest (including forced `P_1`) have `c` components.  To
obtain a near-perfect second matching, choose exactly `c-s` duplicate-colour
connector edges `Q_1`.  Require them to be matching-disjoint and resource-
private, to form an acyclic extension in the contracted component graph, to
use distinct required component tails/heads as certified by ordinary Hall,
and to orient compatibly with every protected path.  Finally require a
perfect matching on the remaining `s` tails and `s` heads.  Then the selected
near-matching has `W-s` forest links, and the resulting second perfect
matching together with `M_0` has at most `s` components while retaining every
bundle ticket.

Outside the laminar/private face, tail, head, upper-colour, graphic, and cap
constraints are generally crossing systems.  Without additional catalogue
structure this is at least a three-matroid correlation problem; ordinary
matroid intersection supplies no integrality theorem.

## 6. Exact conditional protected-extension theorem

Combine the preceding rows.  Fix a forbidden catalogue `Z` disjoint from
`P`.  Suppose the stocked canonical actuator law has an integral stationary
residual, and suppose:

1. all cut actuator copies have a simultaneous occurrence-labelled lift on
   `M` distinct owners whose incidence union `P` is simple with maximum
   degree two;
2. `P` passes every guarded star-surcharge cut (4.6) for this same `Z`;
3. one edge-colour `P_0` extends to a spanning perfect matching `M_0`
   avoiding both `P_1` and `Z`, while that `P_1` satisfies every
   forced-bundle condition of Section 5 and is contracted in a
   laminar/graphic selector satisfying (5.2) whose candidate ground set
   also avoids `Z`;
4. a functional, resource-private, orientation-compatible connector/Euler
   bank realizes every omitted actuator transition and every residual legal
   age arc in the same occurrence-labelled factor chronology, selects the
   exact `c-s` connector count of Section 5, passes its component Hall rows,
   uses only connectors outside `Z`, and leaves a feasible final residual
   perfect matching avoiding `Z`;
5. for every required arbitrary-width upper target, a designated internal
   or connector-crossing witness is included as a literal bundle ticket and
   survives the final selection; and
6. either the flags directly spell the final age source, or all selected
   external-carrier cells lie in one trace-guarded bank satisfying
   (2.4)--(2.5).

Then every canonical multi-hole exchange is realized on the original `W`
owner occurrences with exact mark counts and a stationary age law on the
factor components, and `P` is contained contiguously in an upper-decorated
`q1` near-factor with the declared component residual.  No new owner
occurrence is charged.

#### Proof

The stocking theorem supplies the exact marked rows, while the assumed
integral circulation gives the required transition multiset and condition 4
realizes those arcs physically.  Condition 2 and Theorem 4.1 are an exact
unadorned/fixed-`Z` preflight: they certify that the protected bank has no
owner/lower-`q1` obstruction but do not choose the decorated completion.
Conditions 3--4 and Theorem 5.1 construct that decorated factor directly
using the same forced `P_1`.  Conditions 5--6 transport the nonlocal upper
and cap rows literally.  Every step uses the same occurrence-labelled
bundles, so no marginal recombination is invoked. \(\square\)

This theorem is an exact interface, not a proof that its hypotheses always
hold.  The stationary law above may live on several factor components.  A
final word still needs the separate rooted serialization and upper-safe
opening theorem.

## 7. Sharp frontier

The new all-`k` frontier is now:

\[
\boxed{
\begin{array}{c}
\text{canonical age profiles and donor/reservoir stock}\quad\text{proved}\\
\Downarrow\\
\text{free full-template orbit, or simultaneous degree-two lift}
       \quad\text{partly proved/open}\\
\Downarrow\\
\text{weighted quotient Hall and guarded star-surcharge cuts}
       \quad\text{exact}\\
\Downarrow\\
\text{laminar/graphic upper-decorated forest seed}
       \quad\text{exact integral face}\\
\Downarrow\\
\text{private connector forest, all-width bundles, global cap}
       \quad\text{open outside declared hypotheses}.
\end{array}}
\]

The sharp negative result is Proposition 4.3: even a linear-size bank of
disjoint locally rainbow paths can be unextendable.  The sharp positive
result is the combination of a coherent free-orbit bundle lift, the exact
star-surcharge cuts, and the laminar/graphic matroid-intersection face.

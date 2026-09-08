# Matching-supported compiler selection and deterministic opposing-assignment descent

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` compiler lane  
Status: unconditional abstract theorems, exact pruning budget, and a
scoped application to the PBBS stable-cube conflict bank.  No all-`k`
PBBS chronology satisfying the final hypotheses is claimed.

## 0. Outcome

The full native atlas from handoff item 1977 has exponentially large
higher conflict degrees, but that does not force large compiler defect.
Four sharper facts replace raw degree.

1. **Interval pruning is almost unavailable.**  At deadline length, the
   number of physical intervals of lengths at most `d` is

   \[
   N_d=dW+{d+1\choose2}=\Lambda+\sigma.             \tag{0.1}
   \]

   Every compatible selector is injective from targets to intervals.  A
   construction omitting at most `E` lower targets may therefore erase at
   most `sigma+E` interval columns.  Since `sigma<W+d`, a `B(k)+O(k)`
   compiler must retain a `1-O(1/d)=1-O(k^{-1/2})` fraction of all columns.

2. **The correct all-arity weighted criterion clusters by alternative
   assignments.**  For atomic bad events, define

   \[
   \mu_E={c^{|E|}p_E\over1-p_E}.                    \tag{0.2}
   \]

   For candidate `v in V_s`, put

   \[
   K(v)=1+\sum_{w\in V_s\setminus\{v\}}
       \left(\prod_{F\ni w}(1+\mu_F)-1\right).     \tag{0.3}
   \]

   If `K(v)<=c` for every candidate of positive mass, an exact integral
   selector exists.  This is an all-arity cluster-expansion criterion; it
   groups all events demanding the same alternative `w` instead of charging
   them as mutually opposing.

3. **A deterministic local descent ignores every conflict differing in
   two or more assignments.**  Give each bad event `E` a pivot target
   `sigma(E)`.  The only event `F` which can be newly created when the
   pivot value of an occurring `E` is changed satisfies

   \[
   \Delta(E,F)=\{\sigma(E)\}.                       \tag{0.4}
   \]

   If the resulting weighted directed matrix has spectral radius below
   one, deterministic single-target switches strictly decrease a finite
   potential until no conflict remains.  In particular, an acyclic
   unique-disagreement digraph succeeds for arbitrary list sizes at least
   two.

4. **Uniform injections do have the Lu--Szekely lopsided structure, but
   arbitrary PBBS lists do not inherit it by conditioning.**  For a
   complete target/interval graph, canonical bad events have the exact
   conflicting-partial-injection negative-dependency graph.  For a general
   allowed-list graph, the exact substitute is a weighted permanent-minor
   ratio.  If a spread fractional matching has marginals `x_e`, and the
   relevant permanent minors satisfy

   \[
    \Pr(F\subseteq M)\le C_0^{|F|}\prod_{e\in F}x_e,                \tag{0.5}
   \]

   then the complete residual conflict mass, at every arity, is bounded by
   the corresponding weighted conflict polynomial.  A six-cycle gives an
   explicit counterexample to transferring the Lu--Szekely graph through
   arbitrary list conditioning.

The lower-bound construction proving the PBBS `D_4` estimate in item 1977
contains an exponentially large tagged subbank whose internal
unique-disagreement matrix is zero, provided its auxiliary pivot is
eligible.  Thus exponential raw degree alone is not an obstruction to the
deterministic theorem.  The remaining gate is **external contamination**:
conflicts outside that tagged subbank which use an alternative candidate in
the chosen auxiliary pivot part, together with eligibility of that pivot.

For a `B(k)+O(k)` target, all singleton lower targets may be omitted and
appended literally at exact cost `k`.  This removes the particular
singleton-anchored `D_j` banks and the need to preserve their tight PBBS
ports.  Rank-two and higher parts cannot all be omitted within `O(k)`;
their matching, cluster pressure, or unique-disagreement contamination is
the true remaining problem.

## 1. Exact interval-column pruning budget

Put

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},       \tag{1.1}
\]

and let

\[
 d=\min\left\{j\ge0:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.                                   \tag{1.2}
\]

Assume `1<=d<r`, put `n=W+d`, and let `I_d` be all nonempty intervals of
`[0,n-1]` of length at most `d`.  Then

\[
 |\mathcal I_d|
 =\sum_{\ell=1}^{d}(n-\ell+1)
 =dW+{d+1\choose2}
 =\Lambda+\sigma,                                  \tag{1.3}
\]

where `sigma>=0` is the exact deadline slack.

For a fixed resident chronology, let `V_S` be any pruned physical candidate
list for strict lower target `S`; every candidate is a pair `(S,I)` with
`I in I_d`.  Let

\[
 \operatorname{Cols}(\mathcal V)
 =\{I:\ (S,I)\in V_S\text{ for some retained }S\}. \tag{1.4}
\]

### Theorem 1.1 (column-loss bound)

If an atlas omitting a target family `O` has a compatible full selector,
then

\[
 \boxed{
 |\operatorname{Cols}(\mathcal V)|\ge\Lambda-|O|.} \tag{1.5}
\]

In particular, if `C` interval columns have been erased entirely, then

\[
 \boxed{C\le\sigma+|O|.}                            \tag{1.6}
\]

#### Proof

Two distinct target labels cannot use the same physical interval: its
literal OR has one value and cannot equal two different labels.  In the
negative-window hypergraph this is exactly the corresponding size-two
conflict.  Hence
every compatible selector uses distinct physical intervals for its
`Lambda-|O|` targets.  This proves (1.5), and (1.3) gives (1.6).  QED.

Minimality of `d` gives

\[
 (d-1)W+{d\choose2}<\Lambda,                         \tag{1.7}
\]

so

\[
 \boxed{0\le\sigma<W+d.}                            \tag{1.8}
\]

Consequently, for `|O|=O(k)` and deadline `d=Theta(sqrt(k))`,

\[
 {C\over|\mathcal I_d|}
 \le {W+d+O(k)\over dW+{d+1\choose2}}
 =O(k^{-1/2}).                                      \tag{1.9}
\]

Every complete interval-length class has at least `W+1` columns.  Since
`sigma+O(k)<W+d+O(k)`, two whole length classes cannot both be deleted for
all sufficiently large `k`.  Candidate-wise pruning can be much more
selective than column deletion, but it must still satisfy the exact Hall
necessary conditions

\[
 \left|\bigcup_{S\in X}\{I:(S,I)\in V_S\}\right|\ge|X|
 \quad(X\subseteq\mathcal Q\setminus O).           \tag{1.10}
\]

This is only the interval-matching layer; coordinate-cover conflicts remain.

For completeness, define the exact matching defect of a pruned atlas by

\[
 \delta_{\rm Hall}(\mathcal V)
 =\max_{X\subseteq\mathcal Q}
    \left(|X|-\left|\bigcup_{S\in X}N(S)\right|\right)^+,
 \qquad N(S)=\{I:(S,I)\in V_S\}.                    \tag{1.11}
\]

### Corollary 1.2 (exact pruning loss before coordinate constraints)

The minimum number of target parts which must be omitted before the pruned
candidate/interval graph has an injective selector is exactly
`delta_Hall`.  Hence a `B(k)+O(k)` pruning must satisfy

\[
                         \delta_{\rm Hall}=O(k).     \tag{1.12}
\]

#### Proof

This is the deficiency form of Hall's theorem: a maximum matching leaves
exactly the maximum set-neighborhood deficit unmatched.  Every physical
compiler selector is such a matching, so coordinate constraints can only
increase, never decrease, the final omission cost.  QED.

### Theorem 1.3 (forced interval reservations are net-neutral)

Let `mathcal F` be a compatible conditioned family of `f` target candidates
using `f` distinct interval columns, and omit an additional target family
`O` of size `E`.  Remove the forced parts and reserve their columns.  Before
secondary unit deletions, the residual column-minus-target surplus is

\[
 (|\mathcal I_d|-f)-(\Lambda-f-E)=\sigma+E.          \tag{1.13}
\]

After exact unit closure, let `delta_cl` be the Hall deficiency of the
actual residual candidate/interval graph.  The fixed-middle construction
can omit only `O(k)` further targets only if

\[
                         \boxed{\delta_{\rm cl}=O(k).}                \tag{1.14}
\]

In particular, if secondary closure leaves `C_cl` unreserved interval
columns with no residual candidate at all, then any solution with at most
`t` further omissions must satisfy

\[
                         \boxed{C_{\rm cl}\le\sigma+E+t.}             \tag{1.15}
\]

#### Proof

Equation (1.13) subtracts one target and its distinct occupied column for
each forced candidate, so the net slack is unchanged.  Equations
(1.14)--(1.15) are Corollary 1.2 and Theorem 1.1 applied to the residual
graph.  QED.

In the odd PBBS application `k=2m+1>=5`, one has
`r=m+1>=3` and the number of rank-`(r-1)` facets is
`binom(k,r-1)=W`.  Whenever the selected opening retains the audited
canonical envelope-exact selector for all of them, those facets reserve
`W` distinct columns.  If the `k` singleton lower targets are omitted, the
raw residual counts are

\[
 |\mathcal I_d|-W
 \quad\text{columns and}\quad
 \Lambda-W-k
 \quad\text{targets},                                \tag{1.16}
\]

again with surplus exactly `sigma+k`.  Thus forced facet reservation and
singleton omission do not themselves exceed the deadline budget.  What is
unproved is that the subsequent positive-row unit deletions have
`delta_cl=O(k)`.

### Proposition 1.4 (column count alone cannot control closure)

For arbitrary integers `N>=L>=t+1` with `t>=2`, there is a bipartite target/column
graph with `L` target parts, all `N` columns present in the union of the
neighborhoods, and Hall deficiency at least `t-1`.

#### Proof

Give `t` target parts the common singleton neighborhood `{I_0}`.  Match the
other `L-t` parts to distinct other columns, and connect one of them also
to every still-unused column.  All columns occur, but the first `t` parts
have a one-column neighborhood, giving deficit `t-1`.  QED.

This fan is physically compatible with the candidate formalism whenever
one interval sandwich supports `t` different target labels and pruning
removes their other candidates.  It shows sharply why (1.13) is only a
budget identity: forced-facet unit closure still needs a genuine Hall or
matching-measure theorem.

## 2. Correlated matching-supported alteration

The product experiment used in earlier compiler bounds pays heavily for
same-interval pair conflicts.  They can instead be eliminated before any
higher-order estimate.

Let `Omega` be any nonempty family of matchings in the retained physical
candidate lists which select one candidate from every retained target part
and use distinct physical intervals.  Let
`mu` be an arbitrary probability distribution on `Omega`.  For a conflict
edge `E`, write

\[
                         p_\mu(E)=\Pr_{X\sim\mu}(E\subseteq X),        \tag{2.1}
\]

and, summing over the complete family of inclusion-minimal residual physical
conflicts, put

\[
                         \Psi_\mu=\sum_Ep_\mu(E).    \tag{2.2}
\]

Same-interval pair edges have probability zero and may be omitted from
this sum.

### Theorem 2.1 (matching-supported conflict-mass theorem)

For an upper-complete, depth-`d`-resident chronology and an initially
omitted target family `O`,

\[
 \boxed{
 \nu(k)\le B(k)+|O|+\lfloor\Psi_\mu\rfloor.}        \tag{2.3}
\]

No independence assumption on `mu` is required.

#### Proof

For `X in Omega`, let `Z(X)` be the number of conflict edges contained in
`X`.  Linearity of expectation gives

\[
                         \mathbb E_\mu Z=\Psi_\mu.  \tag{2.4}
\]

Choose `X` with `Z(X)<=floor(Psi_mu)`.  From every occurring conflict edge
choose one of its target parts, and let `R` be the union of the chosen
parts.  Then `|R|<=Z(X)`.  The candidates remaining after deleting `R`
contain no conflict edge: otherwise an inclusion-minimal incompatible
subfamily was already an occurring edge and one of its parts was deleted.

The exact partial negative-window theorem therefore constructs one
nonzero antecedent with the prescribed middle chronology and all lower
targets outside `O union R`.  Append those omitted masks literally.
Upper completeness proves (2.3).  QED.

If `mu` is presented by a finite decision tree with computable conditional
edge probabilities, the proof is deterministic: at each decision choose a
branch which does not increase the conditional expectation of `Z`.  The
final matching has `Z<=Psi_mu`, after which the displayed hitting procedure
is explicit.

Thus a correlated matching measure with

\[
                         |O|+\Psi_\mu=O(k)           \tag{2.5}
\]

is already sufficient for `B(k)+O(k)`, even if no zero-conflict matching
is obtained directly.

Combining Corollary 1.2 and Theorem 2.1 gives the exact two-stage target:
choose a target family `O` of size `delta_Hall` which a maximum matching
leaves unmatched, put a distribution on matchings saturating the remaining
parts, and prove

\[
                         \delta_{\rm Hall}+\Psi_\mu=O(k).             \tag{2.6}
\]

The first term measures pruning/Hall loss; the second measures only genuine
higher coordinate conflicts under a collision-free correlated measure.
Handoff item 1986 supplies an exact run-component/positive-guard
description of those physical conflicts for the maximal-erosion atlas.
It makes the family in (2.2) explicit; it does not bound its matching-law
mass.

### 2.2 Weighted matching measures and exact permanent-minor ratios

Let `G=(L,R;E)` be the residual target/interval candidate graph, where every
matching under consideration saturates `L`.  Delete every structurally
zero edge which belongs to no such matching, give every remaining allowed
edge a positive weight `a_e`, and write

\[
 Z_G(a)=\sum_{M\ {\rm saturates}\ L}\prod_{e\in M}a_e.             \tag{2.7}
\]

For a partial matching `F`, write `G\ominus F` for the graph obtained by
deleting every left and right endpoint used by `F`.  The weighted matching
law is

\[
 \Pr_a(M)={1\over Z_G(a)}\prod_{e\in M}a_e.                         \tag{2.8}
\]

### Lemma 2.2 (exact cylinder and marginal identities)

For every extendable partial matching `F` of size `j`,

\[
 \Pr_a(F\subseteq M)
 ={a(F)Z_{G\ominus F}(a)\over Z_G(a)},
 \qquad
 x_e:=\Pr_a(e\in M)
 ={a_eZ_{G\ominus e}(a)\over Z_G(a)}.                              \tag{2.9}
\]

Consequently

\[
 \boxed{
 {\Pr_a(F\subseteq M)\over\prod_{e\in F}x_e}
 ={Z_G(a)^{j-1}Z_{G\ominus F}(a)
   \over\prod_{e\in F}Z_{G\ominus e}(a)}.}                        \tag{2.10}
\]

#### Proof

After the edges of `F` are fixed, their left and right endpoints cannot be
used again, and every completion is exactly a matching of `G\ominus F`
saturating its remaining left shore.  Summing its weights proves the first
identity.  The case `F={e}` proves the second.  Dividing and cancelling
`a(F)` proves (2.10).  QED.

Thus the desired correlation statement is neither negative association nor
a formal consequence of Hall.  It is exactly a ratio of one rectangular
permanent and its endpoint-deleted minors.

Let `P(G)` denote the bipartite matching polytope

\[
 P(G)=\left\{x\ge0:
       \sum_{e\ni s}x_e=1\ (s\in L),\quad
       \sum_{e\ni I}x_e\le1\ (I\in R),\quad x_e=0\ (e\notin E)
       \right\}.                                                    \tag{2.11}
\]

Because `G` is bipartite, this is the convex hull of the incidence vectors
of matchings saturating `L`.

### Lemma 2.3 (maximum-entropy realization of an interior fractional matching)

Every `x` in the relative interior of `P(G)` is the marginal vector of a
law (2.8) for suitable positive edge weights `a_e`.  More generally, a
point in the relative interior of any face is obtained after restricting
to the saturating matchings spanning that face.

#### Proof

Let `Omega` be the finite set of saturating matchings and put

\[
 A(\theta)=\log\sum_{M\in\Omega}
       \exp\!\left(\sum_{e\in M}\theta_e\right).                   \tag{2.12}
\]

The gradient of `A` is the edge-marginal vector of the exponential-family
law with `a_e=e^{\theta_e}`.  The standard finite-dimensional convex dual
of `A` has domain `conv{1_M:M\in\Omega}=P(G)`; its gradient image is the
relative interior of that convex hull.  Equivalently, maximizing entropy
over probability laws on `Omega` with mean `x` has an interior optimizer,
whose Lagrange multipliers give (2.12).  The same argument on a face proves
the last sentence.  QED.

This lemma does **not** bound correlations.  Define, for the realizing
weights and an integer `rho`,

\[
 \kappa_\rho(G,a)=
 \max_{1\le |F|\le\rho\atop F\ {\rm an\ extendable\ partial\ matching}}
 \left(
 {Z_G(a)^{|F|-1}Z_{G\ominus F}(a)
  \over\prod_{e\in F}Z_{G\ominus e}(a)}
 \right)^{1/|F|}.                                                   \tag{2.13}
\]

There is an exact max-flow test for the spread premise.  Fix `0<u<=1`.
A point `x in P(G)` with `x_e<=u` for all edges exists if and only if

\[
 \boxed{
 |B|+u\,e_G(A,R\setminus B)\ge |A|
 \quad(A\subseteq L,\ B\subseteq R).}                              \tag{2.13a}
\]

Indeed, send capacity one from the source to every left vertex, capacity
`u` across every allowed edge, and capacity one from every right vertex to
the sink.  A cut with source-side target set `A` and source-side interval
set `B` has capacity

\[
 |L\setminus A|+u\,e_G(A,R\setminus B)+|B|.                         \tag{2.13b}
\]

The max-flow/min-cut theorem proves (2.13a).  Thus scalar surplus and
ordinary Hall are not enough for (2.17): every capacitated cut must hold.

If only a specified conflict family is relevant, the maximum may be
restricted to its partial matchings.  This restricted form is the weaker
and exact condition needed below.

There is also an exact sequential form.  Order
`F={e_1,...,e_j}`, put `F_i={e_1,...,e_i}`, and let
`x_e^{G\ominus F_i}` be the marginal of `e` in the endpoint-deleted
weighted graph.  Then

\[
 \boxed{
 {\Pr(F\subseteq M)\over\prod_{e\in F}x_e^G}
 =\prod_{i=2}^j{x_{e_i}^{G\ominus F_{i-1}}\over x_{e_i}^G}.}        \tag{2.13c}
\]

This is the chain rule.  Hence the genuinely minimal expansion hypothesis
is bounded conditional-marginal distortion along the prefixes of physical
conflicts, not a generic assertion of negative correlation.

For marginals `x` define the complete weighted conflict profile

\[
 \Theta_j(x)=\sum_{E\in\mathcal E:\ |E|=j}\prod_{e\in E}x_e,
 \qquad
 \Theta(x;C_0)=\sum_{j\ge2}C_0^j\Theta_j(x),                        \tag{2.14}
\]

where `mathcal E` is the complete inclusion-minimal residual physical
conflict family after exact unit closure.  Same-target and same-interval
sets are absent because they have probability zero under a matching law.

For a candidate edge define its full weighted link

\[
 \Xi(e)=\sum_{E\in\mathcal E:\ e\in E}
 {C_0^{|E|}\over|E|}\prod_{f\in E\setminus\{e\}}x_f.                \tag{2.14a}
\]

Double-counting each conflict through its edges gives the exact identity

\[
                         \boxed{\Theta(x;C_0)=\sum_e x_e\Xi(e).}   \tag{2.14b}
\]

Since `sum_e x_e=|L|`, a uniform all-arity link bound
`Xi(e)<=eta` implies `Theta<=eta|L|`.  To obtain additive `O(k)` while
`|L|` is exponential, one needs `eta=O(k/|L|)`; a merely constant local
pressure is not enough for the alteration route.

### Theorem 2.4 (permanent-ratio compiler theorem)

Assume that, after omitting `O`, the residual graph has a fractional
matching `x` in a face of `P(G)`, a weighted matching realization `mu` of
`x`, and a number `C_0>=1` such that

\[
 \Pr_\mu(E\subseteq M)
 \le C_0^{|E|}\prod_{e\in E}x_e
 \quad(E\in\mathcal E).                                             \tag{2.15}
\]

Then

\[
 \boxed{
 \nu(k)\le B(k)+|O|+\lfloor\Theta(x;C_0)\rfloor.}                 \tag{2.16}
\]

In particular, it is enough that the relevant ratios in (2.13) are at
most `C_0`.  If, for some candidate scale `M_*`,

\[
 \max_e x_e\le {C\over M_*},                                       \tag{2.17}
\]

then every size-`j` conflict has probability at most
`(C_0C/M_*)^j`; the number of conflicts is still charged through the full
profile (2.14), not through `D_2` alone.

#### Proof

Sum (2.15) over the complete conflict family to obtain
`Psi_mu<=Theta(x;C_0)`, then apply Theorem 2.1.  Lemma 2.2 proves the
permanent-ratio assertion, and (2.17) proves the last estimate.  QED.

This gives an exact, checkable replacement for the false assertion that
perfect-matching edges are negatively associated.  The three logically
separate requirements for `B(k)+O(k)` are now

\[
 |O|=O(k),\qquad
 \kappa_{\rm conflict}(G,a)=O(1),\qquad
 \Theta(x;\kappa_{\rm conflict})=O(k).                              \tag{2.18}
\]

The last condition ranges over **all** arities.  Neither a spread
fractional matching nor a bounded permanent ratio by itself implies it.

### 2.3 Calibration on the complete injection space

Take `G=K_{L,N}` with `N>=L`, all weights one, and choose a uniform random
injection from `L` to `R`.  For a prescribed partial injection `F` of size
`j`,

\[
 \Pr(F\subseteq M)={1\over(N)_j},\qquad x_e={1\over N},
 \qquad
 {\Pr(F\subseteq M)\over\prod_{e\in F}x_e}
 ={N^j\over(N)_j}.                                                    \tag{2.19}
\]

Moreover, for `j<=rho<N+1`,

\[
 \log {N^j\over(N)_j}
 =\sum_{i=0}^{j-1}-\log(1-i/N)
 \le {j(j-1)\over2(N-j+1)},                                        \tag{2.20}
\]

and hence one may take

\[
 C_0=\exp\!\left({\rho-1\over2(N-\rho+1)}\right)                 \tag{2.21}
\]

simultaneously through arity `rho`.  Thus positive correlation of disjoint
prescribed edges costs only `exp(O(j^2/N))` in the complete space.

There is also a stronger lopsided statement which does not follow from
(2.19).  A **canonical injection event** prescribes a partial injection.
Two such events conflict when their prescriptions disagree on one domain
point or send two domain points to one range point.

### Theorem 2.5 (Lu--Szekely canonical-event lemma, exact scope)

For uniform random injections from a fixed `L`-set into a fixed `N`-set,
the conflict graph of canonical injection events is a negative-dependency
graph.  Thus the lopsided local lemma and its cluster-expansion form apply
with the exact probabilities `1/(N)_j`, even though compatible disjoint
edges can be positively correlated as in (2.19).

The proof is the finite injection-switching argument: after a canonical
partial injection is fixed, switch its occupied images with the images of
the corresponding domain points in an unfixed injection.  For every family
of nonconflicting canonical events this gives the required injection from
the conditioned avoiding fibre to the unconditioned avoiding fibre, with
constant fibre multiplicity.  Equivalently, for an event `A` and any family
`B` of its nonneighbors,

\[
 \Pr\!\left(A\mid\bigcap_{B\in\mathcal B}\overline B\right)
 \le\Pr(A).                                                         \tag{2.22}
\]

We record the following dual-socket cluster criterion because an injection
has both domain and range conflicts.  Give every canonical bad event `E`
an activity `mu_E`.  For a prescribed edge `e=(s,I)`, put

\[
 K_D(e)=1+\sum_{I'\ne I}
       \left(\prod_{F\ni(s,I')}(1+\mu_F)-1\right),                  \tag{2.23}
\]

\[
 K_R(e)=1+\sum_{s'\ne s}
       \left(\prod_{F\ni(s',I)}(1+\mu_F)-1\right).                  \tag{2.24}
\]

### Corollary 2.6 (complete-injection dual-bucket criterion)

Fix `c>1`, put

\[
 \mu_E={c^{|E|}\Pr(E)\over1-\Pr(E)},                               \tag{2.25}
\]

and assume

\[
                         \boxed{K_D(e)K_R(e)\le c}                 \tag{2.26}
\]

for every prescribed edge of positive event mass.  Then some injection
avoids every bad canonical event.

#### Proof

For a fixed `E`, assign each conflicting event canonically to its first
domain or range disagreement with an edge of `E`.  In one domain bucket,
an independent subfamily must use one common alternative image; in one
range bucket it must use one common alternative preimage.  Allowing all
subsets of the corresponding common-alternative bucket gives (2.23) or
(2.24).  Multiplication over the two sockets of every edge of `E` bounds
the neighbor independence polynomial by

\[
 \prod_{e\in E}K_D(e)K_R(e)\le c^{|E|}.                             \tag{2.27}
\]

The calculation (3.8)--(3.9), now using Theorem 2.5 as the
negative-dependency input, verifies the cluster-expansion lemma.  QED.

### 2.4 Why target-specific PBBS lists are still the missing theorem

One may try to sample a complete uniform injection and add every forbidden
mapping `(s,I)\notin E(G)` as a unary bad event.  Write

\[
 f_s=N-\deg_G(s),\qquad
 g_I=L-\deg_G(I).                                                     \tag{2.28}
\]

For a forbidden unary event, (2.25) gives `mu_1=c/(N-1)`.  Therefore,
even before any genuine coordinate conflict is charged, (2.23)--(2.24)
imply at an allowed edge `(s,I)`

\[
 K_D(s,I)\ge1+{cf_s\over N-1},\qquad
 K_R(s,I)\ge1+{cg_I\over N-1}.                                    \tag{2.29}
\]

Consequently the particular direct dense-space criterion
(2.25)--(2.26) can hold only if

\[
 \boxed{
 \left(1+{cf_s\over N-1}\right)
 \left(1+{cg_I\over N-1}\right)\le c}                             \tag{2.30}
\]

at every allowed edge, with strict room left for the physical conflict
events.  In particular, even ignoring the range side it requires

\[
                         \deg_G(s)\ge1+{N-1\over c}.                \tag{2.31}
\]

Thus this implementation is intrinsically a dense-list theorem.  The
column budget (1.6) controls only the union of the lists and gives no such
row or column density; Proposition 1.4 already shows the gap.  No audited
PBBS result supplies (2.30).

Nor may one simply condition the injection on using allowed edges.
Consider the six-cycle list graph with left vertices `1,2,3`, right
vertices `1,2,3`, and allowed edges

\[
 11,12,22,23,33,31.                                                  \tag{2.32}
\]

It has exactly two perfect matchings,

\[
 M_0=\{11,22,33\},\qquad M_1=\{12,23,31\}.                          \tag{2.33}
\]

The canonical events `A={11}` and `B={23}` have no conflicting prescribed
mapping, but under the uniform allowed-matching law they are mutually
exclusive.  Hence

\[
 \Pr(A\mid\overline B)=1>{1\over2}=\Pr(A),                          \tag{2.34}
\]

which violates (2.22).  Therefore arbitrary list conditioning destroys
the Lu--Szekely negative-dependency graph, even for a 2-regular allowed
graph.

Arbitrary edge weighting is not a substitute, even when the underlying
graph is complete.  On `K_(3,3)` give the edges the weight matrix

\[
 \begin{pmatrix}
 1&1/2&1\\
 1/2&1&1\\
 1&1&1/2
 \end{pmatrix}.                                                       \tag{2.35}
\]

The permanent is `29/8`.  If `A={11}` and `B={22}`, direct deletion of the
corresponding row and column gives

\[
 \Pr(A)=\Pr(B)={12\over29},\qquad
 \Pr(A\cap B)={4\over29},\qquad
 \Pr(A\mid\overline B)={8\over17}>{12\over29}.                     \tag{2.36}
\]

Thus the canonical conflict graph is not a negative-dependency graph for
general weighted complete-injection laws either.

Spread marginals alone also do not control the permanent ratios.  In
weighted `K_(2,2)`, give the two diagonal edges weight `a` and the two
off-diagonal edges weight one.  The diagonal perfect matching has
probability

\[
                         p={a^2\over1+a^2}.                           \tag{2.37}
\]

For its two-edge cylinder the ratio (2.10) is `1/p`, which is unbounded as
`a` tends to zero.  This is the unique maximum-entropy law with its given
marginals.  Hence maximum entropy by itself does not imply a uniform value
of `C_0`.  This two-list example has only a weak marginal cap; a stronger
cap still requires, rather than implies, a separate conditional-distortion
theorem.

The exact surviving list generalization is Theorem 2.4: construct a spread
fractional matching, realize it by weights, prove the permanent-minor bounds
(2.15), and bound the full weighted conflict polynomial (2.14).  These are
separate expansion assertions.  Calling the list graph Hall-sufficient,
high-entropy, or approximately independent without these inequalities does
not prove them.

## 3. Alternative-cluster expansion at every arity

Return temporarily to independent choices from target parts.  A bad event
`E` is a partial assignment and has probability `p_E`.  Join two events
when they prescribe different candidates in a shared target part.  This is
the assignment-incompatible lopsided graph proved in item 1977.

We use the following standard cluster-expansion local lemma in its lopsided
form.  For nonnegative activities `mu_E`, let

\[
 \varphi_E^*(\mu)
 =\sum_{J\subseteq\Gamma^*(E)\atop J\ {\rm independent}}
       \prod_{F\in J}\mu_F,                         \tag{3.1}
\]

where `Gamma^*(E)=Gamma(E) union {E}`.  If

\[
                         p_E\varphi_E^*(\mu)\le\mu_E                \tag{3.2}
\]

for every event, then the probability of avoiding all events is positive.
The usual induction on avoided-event families proves the same statement
for any negative-dependency graph; no ordinary variable-dependency edges
are added.

### Theorem 3.1 (alternative-bucket cluster criterion)

Fix `c>1`, discard zero-probability events, and assume `p_E<1`.  Put

\[
                         \mu_E={c^{|E|}p_E\over1-p_E}.                \tag{3.3}
\]

For `v in V_s`, define

\[
 K(v)=1+\sum_{w\in V_s\setminus\{v\}}
       \left(\prod_{F\ni w}(1+\mu_F)-1\right).      \tag{3.4}
\]

If

\[
                         \boxed{K(v)\le c\quad\text{for every }v,}  \tag{3.5}
\]

then an exact compatible full selector exists.

#### Proof

Fix `E` and order its target parts.  Canonically assign every neighbor `F`
to the first part of `E` on which `F` prescribes an alternative.  In an
independent family of neighbors assigned to one part `V_s`, all its events
must prescribe the same alternative `w`: two different alternatives are
assignment-incompatible.  For fixed `w`, allowing every subset of the
bucket, whether internally independent or not, contributes at most

\[
                         \prod_{F\ni w}(1+\mu_F).    \tag{3.6}
\]

The canonical buckets are disjoint.  Hence the neighbor independence
polynomial satisfies

\[
 \sum_{J\subseteq\Gamma(E)\atop J\ {\rm independent}}
       \prod_{F\in J}\mu_F
 \le\prod_{v\in E}K(v)\le c^{|E|}.                 \tag{3.7}
\]

Since `E` is adjacent to every one of its neighbors, an independent subset
of `Gamma^*(E)` either is `{E}` or lies in `Gamma(E)`.  Thus

\[
                         \varphi_E^*\le\mu_E+c^{|E|}.                \tag{3.8}
\]

The definition (3.3) gives

\[
 p_E(\mu_E+c^{|E|})=\mu_E,                           \tag{3.9}
\]

so (3.2) holds.  The cluster-expansion lemma yields an integral selector.
QED.

The exponential relaxation

\[
 \boxed{
 \sum_{w\ne v}\left(e^{\lambda(w)}-1\right)\le c-1,
 \qquad \lambda(w)=\sum_{F\ni w}\mu_F}             \tag{3.10}
\]

is sufficient.  It retains every arity and clusters only by actual
alternative assignments.

### Corollary 3.2 (uniform-list calibration)

Suppose every list has exactly `M>=2` candidates, choices are uniform, and
`D_j(w)` counts retained size-`j` conflicts containing candidate `w`.
Then

\[
 \lambda(w)\le\sum_{j\ge2}D_j(w){c^j\over M^j-1}.  \tag{3.11}
\]

If, for every candidate and every `j>=2`,

\[
                         D_j(w)\le Q^{j-1},          \tag{3.12}
\]

put `alpha=Q/M` and assume `c alpha<1`.  A sufficient finite condition is

\[
 \boxed{
 (M-1)\left[
  \exp\!\left({c^2\alpha
       \over M(1-c\alpha)(1-M^{-2})}\right)-1
 \right]\le c-1.}                                  \tag{3.13}
\]

#### Proof

Here `p_E=M^(-|E|)`, so (3.3) gives
`mu_E=c^j/(M^j-1)`.  This proves (3.11).  Under (3.12), sum the geometric
series and use `M^j-1>=M^j(1-M^-2)` for `j>=2` to obtain

\[
 \lambda(w)\le {c^2\alpha
       \over M(1-c\alpha)(1-M^{-2})}.               \tag{3.14}
\]

Now (3.13) implies (3.10).  QED.

As `M` tends to infinity, (3.13) permits

\[
 \alpha<{c-1\over c(2c-1)}.                         \tag{3.15}
\]

The right side is maximized at `c=1+1/sqrt(2)` and equals

\[
                         3-2\sqrt2.                  \tag{3.16}
\]

Thus, with a fixed asymptotic gap, the model threshold is

\[
                         \liminf {M\over Q}>3+2\sqrt2,               \tag{3.17}
\]

improving the earlier convenient `M>=10Q` calibration.  This is conditional
on the **upper** bounds (3.12); the PBBS theorem in item 1977 supplied a
lower conflict bank and cannot be substituted for them.

If the total activity `lambda` is equally spread over the `M-1`
alternatives to `v`, condition (3.10) allows

\[
 \lambda\le(M-1)\log\left(1+{c-1\over M-1}\right)\longrightarrow c-1.
                                                               \tag{3.18}
\]

If it is concentrated in one alternative, the threshold is only
`lambda<=log c`.  Alternative spread, not raw incident degree, is the
gain over item 1977.

## 4. Deterministic one-disagreement descent

The next theorem needs neither independence nor a local lemma.  Let
`mathcal E` be any finite family of bad partial transversals.  For two
events define

\[
 \Delta(E,F)=\{s\in\operatorname{supp}(E)\cap\operatorname{supp}(F):
                         E_s\ne F_s\}.               \tag{4.1}
\]

Choose for every event a pivot

\[
                         \sigma(E)\in\operatorname{supp}(E),         \tag{4.2}
\]

whose target part has at least two candidates.  Give every candidate a
strictly positive law `pi_s`, and set

\[
 R_{EF}=
 1_{\{\Delta(E,F)=\{\sigma(E)\}\}}
 {\pi_{\sigma(E)}(F_{\sigma(E)})
  \over1-\pi_{\sigma(E)}(E_{\sigma(E)})}.           \tag{4.3}
\]

### Theorem 4.1 (spectral opposing-assignment descent)

If there are positive event weights `a_E` satisfying

\[
                         \boxed{Ra<a,}               \tag{4.4}
\]

then deterministic single-part switches transform every full transversal
into one containing no bad event.  Equivalently, it is sufficient that

\[
                         \boxed{\rho(R)<1.}          \tag{4.5}
\]

#### Proof

For a full transversal `X`, put

\[
                         \Phi(X)=\sum_{E\subseteq X}a_E.              \tag{4.6}
\]

If `E subseteq X`, replace its pivot value
`v=E_(sigma(E))` by an alternative drawn from `pi` conditioned not to equal
`v`.  Event `E` is destroyed.  A previously false event `F` can become true
only if (i) it uses the changed part with the new value and (ii) it agrees
with `E` on every other common part.  These conditions are exactly

\[
                         \Delta(E,F)=\{\sigma(E)\}.  \tag{4.7}
\]

Events differing from `E` in two or more assignments retain an unsatisfied
coordinate; events compatible with `E` cannot be newly created by changing
the pivot away from its old value.  Therefore

\[
 \mathbb E[\Phi(X')\mid X,E]
 \le\Phi(X)-a_E+\sum_FR_{EF}a_F.                    \tag{4.8}
\]

By (4.4), at least one alternative deterministically lowers `Phi` by at
least

\[
                         \delta_E=a_E-(Ra)_E>0.     \tag{4.9}
\]

Choose a minimizing alternative and repeat with any occurring event.  The
finite event family has `delta=min_E delta_E>0`, so after at most
`Phi(X_0)/delta` switches the process reaches `Phi=0`.

For a finite nonnegative matrix, `rho(R)<1` implies (4.4) by taking
`a=(I-R)^(-1)1`; conversely (4.4) implies `rho(R)<1` by the elementary
Perron--Frobenius/weighted-row bound.  QED.

If every list has size exactly `M` and the laws are uniform, then

\[
                         R={A_\sigma\over M-1},       \tag{4.10}
\]

where `A_sigma` is the adjacency matrix of the directed graph

\[
 E\longrightarrow F
 \quad\Longleftrightarrow\quad
 \Delta(E,F)=\{\sigma(E)\}.                         \tag{4.11}
\]

Thus `rho(A_sigma)<M-1` is sufficient.  The easy row condition is
`outdeg(E)<=M-2`; the spectral condition can hold with much larger maximum
outdegree.  If `A_sigma` is acyclic, it is nilpotent and succeeds for every
`M>=2`.

### Corollary 4.2 (private-pivot peeling)

Call a conflict family **private-pivot peelable** if every nonempty
subfamily `H` contains an event `E` and an eligible pivot part `s in E`
such that no `F in H minus {E}` satisfies `Delta(E,F)={s}`.  Then it has an
exact compatible full selector.

#### Proof

Peel `E`, record `sigma(E)=s`, and continue.  Every directed arc from `E`
goes to an event peeled earlier.  The resulting unique-disagreement matrix
is triangular and nilpotent.  Theorem 4.1 applies.  QED.

Equivalently, it suffices to assign integer heights `h(E)` and eligible
pivots so that

\[
 \Delta(E,F)=\{\sigma(E)\}\quad\Longrightarrow\quad h(F)<h(E).       \tag{4.12}
\]

The exact obstruction to this zero-spectral route is a nonempty
**private-pivot core** in which every event, at every eligible pivot, has a
unique-disagreement successor inside the core.

### Proposition 4.3 (general deterministic potential certificate)

There is also a pivot-free sufficient condition.  Give every bad edge a
positive weight `a_E`.  For selected `v in X` and an alternative `w` in
the same part, define

\[
 D_X(v)=\sum_{E\subseteq X,\ v\in E}a_E,
 \qquad
 C_X(w)=\sum_{F\ni w,\ F\setminus\{w\}\subseteq X}a_F.              \tag{4.13}
\]

Then the exact switch identity is

\[
 \boxed{
 \Phi(X-v+w)-\Phi(X)=C_X(w)-D_X(v).}                \tag{4.14}
\]

Hence, if every bad `X` admits `v,w` with `C_X(w)<D_X(v)`, deterministic
descent terminates.  A static sufficient form is: every bad edge `E`
contains a candidate `v` with

\[
 \min_{w\in V_{s(v)}\setminus\{v\}}
       \sum_{F\ni w}a_F<a_E.                        \tag{4.15}
\]

This follows because `C_X(w)` is bounded by the displayed global load,
while `D_X(v)>=a_E`.

## 5. The known PBBS `D_j` lower bank is not a spectral obstruction by itself

Theorem 6.2 of item 1977 constructs a size-`j` conflict around a singleton
candidate `v=({x},{p})`.  The remaining `d` positions of one central window
are partitioned into nonempty blocks `J_1,...,J_(j-1)`.  A stable set `C`
and omitted coordinate `y in C` provide labels

\[
                         R_h=F(J_h)\cup Z_h.          \tag{5.1}
\]

Fix `v`, the central window, the displayed block partition, `C`, and `y`.
Assume `|C|-1>=j-1` and choose distinct tags
`t_1,...,t_(j-1) in C minus {y}`.  Restrict to the still-exponential tagged
subbank in which

\[
 t_h\in Z_h,
 \qquad t_g\notin Z_h\quad(g\ne h).                \tag{5.2}
\]

Because `F(J_h) cap C=emptyset`, the intersection `R_h cap C=Z_h`
identifies the role `h`.  Within this tagged subbank, orient every event
through the auxiliary candidate

\[
                         w_1=(R_1,J_1).              \tag{5.3}
\]

Assume explicitly that the residual target part `V_(R_1)` has at least two
candidates, so that (5.3) is an eligible pivot.  Eligibility is not implied
merely by the stable-cube construction and must survive exact unit closure.
No shorter-interval alternative follows formally: `P(J_1)` is a union of
erosion states and need not be contained in any one `P_p`.  Thus block
length at least two, by itself, is not an eligibility proof.

If another event uses the same target part `R_1`, (5.2) forces it to use
role one, and its label determines the same `Z_1`; the fixed block then
gives the same candidate `(R_1,J_1)`.  It does not use an alternative at
that part.  Therefore the internal unique-disagreement matrix of this
tagged subbank is identically zero.

This proves a precise correction to raw-degree reasoning: the tagged
exponential subbank contributes no internal arc when its pivot is eligible.
Its size alone is irrelevant to Theorem 4.1.  This does **not** dispose of
the full `D_j` family.  Untagged events and conflicts outside the bank which
use a different candidate in the same auxiliary target part form the exact
external contamination matrix to be bounded, made acyclic, or removed by
candidate pruning.

There is also a direct weighted-alteration calibration.  Suppose a
singleton part has `m_x>=1` uniformly sampled candidates, choose one fixed
stable-cube subbank for each of those `m_x` anchors and each arity, and
suppose every auxiliary candidate in these banks has probability at most
`1/M_0`.  With `alpha=Q/M_0<1`, their total product conflict mass, summed
over all arities, is at most

\[
 \sum_{j=2}^{d+1}{(Q)_{j-1}\over M_0^{j-1}}
 \le {\alpha\over1-\alpha}.                         \tag{5.4}
\]

Indeed, the factor `m_x` counting anchor candidates cancels their sampling
probability `1/m_x`.  Summed over the `k` singleton target parts, this known
bank has mass at most `k alpha/(1-alpha)`.  Thus it is compatible with a
`B(k)+O(k)` alteration whenever `alpha` stays uniformly away from one,
say `sup_k alpha_k<=1-epsilon` for a fixed `epsilon>0`.  This
again concerns the displayed subbank only; external conflicts may dominate.

The same calculation survives interval-matching correlation, with its
permanent-minor loss made explicit.

### Proposition 5.1 (matching-supported stable-bank mass)

Let `x` be the marginals of a matching law satisfying (2.15).  For each of
the `k` singleton target parts choose one fixed displayed stable-cube bank
at every arity and suppose:

1. the anchor marginals in each singleton part sum to one;
2. every auxiliary edge in those banks has `x_e<=C/M_*`; and
3. each anchor lies in at most `(Q)_(j-1)` chosen size-`j` bank events.

Put

\[
                         \beta={C_0CQ\over M_*}.                    \tag{5.5}
\]

If `beta<1`, the expected number of conflicts from these chosen banks is at
most

\[
 \boxed{{kC_0\beta\over1-\beta}.}                                  \tag{5.6}
\]

#### Proof

Fix one singleton part and sum first over its anchor edges.  Their
marginals sum to one.  For a fixed anchor, every size-`j` event contributes
at most

\[
 C_0^j x_{\rm anchor}(C/M_*)^{j-1}.                                 \tag{5.7}
\]

There are at most `(Q)_(j-1)<=Q^(j-1)` such events.  Summing the anchors,
then the `k` parts and all `j>=2`, gives

\[
 k\sum_{j\ge2}C_0(C_0CQ/M_*)^{j-1},                                \tag{5.8}
\]

which is (5.6).  QED.

Thus matching support plus a bounded permanent-minor ratio really does
remove the displayed **singleton** stable-cube `D_4` obstruction at `O(k)`
cost whenever `beta` is bounded below one.  It does not control unchosen
charts, rank-two-and-higher anchors, or external conflicts.  Those terms
must occur in the full polynomial (2.14); no degree-four estimate may
replace them.

The stable construction extends beyond singleton anchors, so this caveat is
real rather than formal.  Retain the notation of Theorem 6.2 in item 1977:
`F_p` and `P_p` are the mandatory core and maximal erosion state at position
`p`, and put `c_0=r-2d-1`.

### Lemma 5.2 (stable bank around a general one-position anchor)

Let `a=(S,{p})` be a retained one-position candidate, so
`F_p subseteq S subseteq P_p`.  Form a `d+2`-position stable intersection
`C` exactly as in Theorem 6.2, for which `|C|>=c_0`.  If
`W>=d+2`, `2<=j<=d+1`, and

\[
                         |S|\le c_0-2,                              \tag{5.8a}
\]

choose `y in C\setminus S`, put

\[
 U=C\setminus(S\cup\{y\}),\qquad Q_S=2^{|U|}-1,                    \tag{5.8b}
\]

and assume `Q_S>=j-1`.  Then for every ordered partition of the remaining
`d` positions into `j-1` nonempty consecutive blocks there are at least

\[
                         (Q_S)_{j-1}                                \tag{5.8c}
\]

distinct size-`j` inclusion-minimal conflicts containing `a`.

#### Proof

The stable-intersection proof of item 1977 gives `|C|>=c_0`; (5.8a) leaves
at least two points of `C\setminus S`, so `y` and a nonempty `U` exist.
For each block `J_h`, the mandatory-core boundary argument used there gives

\[
              (U\cup\{y\})\cap F(J_h)=\varnothing.                \tag{5.8d}
\]

At the anchor end this uses `F_p subseteq S` and
`(U union {y}) cap S=emptyset`; at every other block boundary it uses that
every point of `U union {y} subseteq C` is present in the two neighboring
erosion states.  Choose ordered distinct nonempty `Z_h subseteq U` and put

\[
                         R_h=F(J_h)\cup Z_h.                         \tag{5.8e}
\]

Then `F(J_h) subseteq R_h subseteq P(J_h)`.  The labels are nonempty and
strict because all erosion states in the central window lie in one rank-`r`
owner and `y` belongs to every `P(J_h)` but to no `R_h`; they are
pairwise distinct because `R_h cap U=Z_h`; and none equals `S` because
`Z_h` is nonempty and disjoint from `S`.  All `j` labels omit `y`, while
their disjoint intervals partition the same central `d+1` window.  They
therefore kill its `y` requirement.  For a proper subfamily, the union of
all selected intervals has at most `d` positions.  Hence every coordinate-
deletion component has length at most `d`.  For a selected positive label
`R` on interval `I`, every other selected interval is disjoint from `I`,
while `R subseteq P(I)` gives an occurrence of each `x in R` inside `I`;
thus the positive guard survives.  The exact run-component/positive-guard
normal form of handoff item 1986 proves compatibility of every proper
subfamily.  Finally there are `(Q_S)_(j-1)` ordered choices.  QED.

In particular, after all singleton targets are omitted, every retained
rank-two one-position anchor has `Q_S>=2^(c_0-3)-1`; the bank is nonempty
for `c_0>=4` and exponential at deadline, where `c_0=Theta(k)`.  Omitting
that entire rank would cost `binom(k,2)`, outside an additive `O(k)` budget.

The complete stable-composition bank has a sharper generating-function
bound.  Let `mathcal A_1` be all retained one-position anchors satisfying
Lemma 5.2, and put

\[
                         X_1=\sum_{a\in\mathcal A_1}x_a.             \tag{5.9}
\]

After an anchor and one of its two directions are fixed, the stable
intersection is fixed and there are at most `k` choices of omitted stable
coordinate.  Thus every anchor lies in at most

\[
                         R_*\le2k                                  \tag{5.10}
\]

such charts.  For a consecutive block `J` of length `ell`, let
`mathcal W_a(J)` be all auxiliary candidates allowed by that chart, and
define the socket mass

\[
 \lambda_\ell=\sup_{a,J:\ |J|=\ell}
                 \sum_{w\in\mathcal W_a(J)}x_w,qquad
 A(z)=C_0\sum_{\ell=1}^d\lambda_\ell z^\ell.                         \tag{5.11}
\]

### Proposition 5.3 (full stable-composition generating function)

Under (2.15), the expected conflict count from every stable-composition
event in these charts is at most

\[
 \boxed{
 \Phi_{\rm stab}
 \le R_*C_0X_1[z^d]{A(z)\over1-A(z)}.}                              \tag{5.12}
\]

If `lambda_ell<=lambda` for every length, then

\[
 \boxed{
 \Phi_{\rm stab}
 \le R_*C_0^2X_1\lambda(1+C_0\lambda)^{d-1}.}                       \tag{5.13}
\]

#### Proof

In one chart, a size-`t+1` event consists of its anchor and auxiliary
candidates on an ordered consecutive composition
`ell_1+...+ell_t=d`.  Summing first over all auxiliary labels and dropping
their distinct-target restrictions only enlarges the sum, giving

\[
 C_0x_a\prod_{h=1}^t(C_0\lambda_{\ell_h}).                          \tag{5.14}
\]

Summing all ordered compositions is exactly
`C_0x_a[z^d]A/(1-A)`.  Sum the at most `R_*` charts and all anchors to get
(5.12).  If every socket mass is at most `lambda`, the coefficient is

\[
 \sum_{t=1}^d(C_0\lambda)^t{d-1\choose t-1}
 =C_0\lambda(1+C_0\lambda)^{d-1},                                  \tag{5.15}
\]

which proves (5.13).  QED.

This is an all-arity audit, not a `D_4` estimate.  When `lambda` is small,
its right side is `O(k)` only at the approximate scale

\[
                         \lambda=O\!\left({k\over R_*X_1}\right),  \tag{5.16}
\]

unless additional decay is used.  The previously attractive local scale
`O((R_*d)^(-1))` need not suffice when `X_1` is exponential.

There is also a forced mass identity which explains why `X_1` cannot be
ignored.  Assume `d>=2` and reserve the `W` canonical facet columns, all of
length `d`, as an explicit simultaneous-reservation hypothesis; then omit
the `k` singleton targets and make no other omissions.  The residual
matching has `sigma+k` more columns than targets, and all `W+d` length-one
columns remain.  Since every longer column has capacity one,

\[
 \boxed{
 \sum_{e:\ |I_e|=1}x_e
 \ge\max\{0,W+d-(\sigma+k)\}.}                                     \tag{5.17}
\]

This follows by putting unit mass on all longer columns first; their total
capacity is the number of residual columns minus `W+d`.  Current PBBS
results do not say what fraction of the mandatory length-one mass (5.17)
belongs to `mathcal A_1`: high-label one-position candidates can avoid the
particular stable charts.  The exact new parameter is therefore stable
anchor mass `X_1`, not merely the number of one-position columns.  If some
reserved forced candidates use `f_1` length-one columns, the right side of
(5.17) must be reduced by `f_1`; no unqualified global PBBS reservation
claim is being made here.

For the `B(k)+O(k)` goal there is an even simpler legal pruning.  Omit

\[
                         O_1=\{\{x\}:x\in[k]\}.      \tag{5.18}
\]

It costs exactly `k` appended literal letters and removes every
singleton-anchored bank in item 1977.  Thus survival of exact-gap PBBS
tight ports is a coefficient-one issue, not a necessary `B(k)+O(k)` gate.
Omitting the complete rank-two layer would cost `binom(k,2)`, so this
escape does not extend one rank further.

### Corollary 5.4 (conditional `B(k)+k` theorem)

Let `T_k` be an upper-complete, deadline-resident middle chronology.  Omit
the `k` singleton lower targets, perform exact unit closure, and suppose
the complete residual conflict family is private-pivot peelable using only
parts with at least two candidates.  Then

\[
                         \boxed{\nu(k)\le B(k)+k.}   \tag{5.19}
\]

#### Proof

Choose an arbitrary residual full transversal.  Corollary 4.2 converts it
by integral single-part switches into a compatible selector.  The exact
fixed-middle realization gives a length-`B(k)` word covering all nonsingleton
targets; append each singleton once.  QED.

## 6. Sharp remaining PBBS/Pascal condition

Proved here:

1. a `B(k)+O(k)` atlas cannot discard more than `sigma+O(k)` physical
   interval columns;
2. correlated matching measures eliminate all same-interval conflicts and
   need only total residual conflict mass `O(k)`;
3. the exact spread-matching requirement is the capacitated Hall family
   (2.13a), while all cylinder correlations are the permanent-minor ratios
   (2.10), equivalently the sequential distortions (2.13c);
4. uniform complete injections satisfy both the exact
   `exp(O(j^2/N))` cylinder estimate and the Lu--Szekely canonical-event
   negative-dependency theorem, but a six-cycle list graph and a weighted
   complete `3` by `3` graph disprove both proposed extensions;
5. the full matching-supported alteration cost is the all-arity polynomial
   (2.14), or exactly the weighted link sum (2.14b);
6. the alternative-bucket cluster criterion is summable at every arity
   under the exact finite inequality (3.13);
7. deterministic one-part descent depends only on the unique-disagreement
   spectral matrix, not on ordinary dependency or raw `D_j`; and
8. the explicit exponential PBBS lower-bank construction has a zero-matrix
   tagged subbank when its pivot is eligible, while all singleton-anchored
   versions disappear after the legal `k`-singleton omission.  Lemma 5.2
   shows that low-rank one-position anchors, including rank two, still carry
   the analogous bank.  Its entire stable-composition chart family obeys
   the exact generating-function bound (5.12), conditional on the same
   minor ratios and socket masses.

Not proved:

1. no residence-safe, upper-complete PBBS/Pascal rethreading is known to
   satisfy Hall after a pruning which respects the column budget (1.6);
2. current PBBS theorems prove only the scalar residual surplus
   `sigma+k`, not every capacitated cut (2.13a), so no spread fractional
   matching has been constructed after unit closure;
3. no permanent-minor/deletion-stability estimate is known for the actual
   target-specific PBBS lists; Lu--Szekely cannot be invoked after
   conditioning on those lists;
4. neither the stable-anchor mass `X_1`, the socket masses in (5.11), nor
   the **complete** weighted conflict polynomial (2.14) is presently
   bounded by `O(k)`;
5. current PBBS theorems do not upper-bound every candidate activity as in
   (3.12) or the external contamination matrix in Section 5;
6. private-pivot peelability of the **complete** residual conflict family
   is open; and
7. no unconditional `B(k)+O(k)` theorem follows.

The smallest exact countercondition for the **acyclic/private-pivot peeling**
route is a private-pivot core.  Such a core need not obstruct the full
spectral theorem: a directed cycle may still have `rho(R)<1`.  The exact
spectral obstruction is failure of `rho(R)<1` for every eligible pivot/law,
and Proposition 4.3 is broader still.  For the weighted route the
countercondition is either a Hall-deficient candidate/interval subgraph or
nonsummable alternative-bucket activity in one target part.  For the
matching-supported route it is more precise: failure of one capacitated
Hall cut, unbounded relevant permanent-minor distortion, or a superlinear
full weighted conflict polynomial.  These
conditions must be tested in one physical chronology; independent rankwise
factors or formal candidate profiles do not suffice.

# Depth-one component fusion: an exact defect ledger and two-switch rigidity

Date: 2026-07-26

Method: pure mathematics only.  No computation or search is used.

## 0. Outcome

Let

\[
 n=2m+\varepsilon,\qquad \varepsilon\in\{0,1\},\qquad
 \mathcal X=\binom{[n]}m,\qquad W=|\mathcal X|,
\]

and let `J=J(n,m)`.  For a Johnson edge `e=XY`, put

\[
 \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.                 \tag{0.1}
\]

There are two different depth-one fusion questions, and they have different
answers.

1.  **The defect version is solved.**  If `F_0` is any spanning linear
    forest with `c_0=o(W)` components and with both colour maps in (0.1)
    injective, then endpoint splicing produces a spanning linear forest `F`
    with

    \[
      c(F)\le {W\over m+\varepsilon+1}=O(W/m),                \tag{0.2}
    \]

    while, on each colour shore, the missing-colour count does not increase
    and the collision excess is at most `c_0`.  Hence both missing and repeat
    defects are `o(W)`.  In particular,

    \[
                         Hc(F)=o(W)                            \tag{0.3}
    \]

    for every `H=o(m)`.  Thus the component term of the coefficient-one
    depth-one ledger can be closed without a colour-safe splice theorem.

2.  **Exact injectivity is a genuinely different problem.**  There is no
    nontrivial two-edge switch which preserves simultaneously the complete
    middle-degree vector and the multisets of lower and upper colours.  The
    only nontrivial `2 x 2` switch in the lower--upper flag graph is a
    four-coordinate star switch; it moves all four noncentral middle
    incidences and therefore cannot be a degree-preserving graph switch.

For the exact odd-ground common refinement, once an exact lower-perfect,
upper-injective forest core satisfying the known residual capacitated Hall
cuts exists, the desired component bound is automatic: its completion has at
most

\[
                    d={2W\over m+2}=o(W/H)                    \tag{0.4}
\]

cycles for every `H=o(m)`.  Thus component fusion is not an additional gate
after the exact Hall core has been constructed.  What remains unproved is
the Hall-aware exactification of the known two-sided pseudoforest.

The theorem does **not** produce an exactly two-sided-rainbow cycle or
factor.  Its positive conclusion is the exact `o(W)` defect statement
needed at depth one; its rigidity conclusion explains why ordinary
two-edge switches do not upgrade that statement to exact injectivity.

## 1. Colour defects

For a Johnson graph `G` and a sign `sigma in {-,+}`, let

\[
 \operatorname{supp}_-(G)=\{\ell(e):e\in E(G)\},\qquad
 \operatorname{supp}_+(G)=\{u(e):e\in E(G)\}.          \tag{1.1}
\]

Writing

\[
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},                         \tag{1.2}
\]

define

\[
 M_-(G)=|\mathcal L|-|\operatorname{supp}_-(G)|,
 \quad
 M_+(G)=|\mathcal U|-|\operatorname{supp}_+(G)|,       \tag{1.3}
\]

and

\[
 R_-(G)=|E(G)|-|\operatorname{supp}_-(G)|,
 \quad
 R_+(G)=|E(G)|-|\operatorname{supp}_+(G)|.             \tag{1.4}
\]

The quantities `R_sigma` are the exact collision excesses.  They are zero
when the corresponding colour map is injective.

## 2. Endpoint splicing, including isolated owners

The endpoint estimate below extends the usual nontrivial-path argument to a
spanning forest which may contain isolated owners.

### Theorem 2.1 (deterministic Johnson endpoint fusion)

Let `F_0` be a spanning linear forest in `J(2m+epsilon,m)`, where
`epsilon in {0,1}` and `m>=2`.  Repeatedly join endpoints of two different
current components whenever they are Johnson adjacent.  The process stops
at a spanning linear forest `F` having

\[
 \boxed{
 c(F)\le {W\over m+\varepsilon+1}.}                   \tag{2.1}
\]

Every old edge of `F_0` remains an edge of `F`.

#### Proof

Adding an edge between endpoints of two different paths joins them into one
path.  Thus every step is legal, preserves all old edges, and lowers the
component count by one.  Stop at a maximal forest.

Let `p` be the number of nontrivial path components, `z` the number of
isolated components, and `c=p+z`.  Put a port weight `w_X=1` on each genuine
endpoint of a nontrivial path, put `w_X=2` on each isolated owner, and put
`w_X=0` elsewhere.  Thus

\[
 \sum_Xw_X=2c,\qquad \sum_Xw_X^2=2p+4z=2c+2z.         \tag{2.2}
\]

At maximality, two positive-weight owners in different components cannot
be Johnson adjacent.  The only possible positive-weight edge joins the two
endpoints of one nontrivial path, and both of its endpoint weights are one.
There is at most one such edge per path.  If `A_J` is the adjacency matrix,
then

\[
                         w^T A_Jw\le2p=2(c-z).                 \tag{2.2a}
\]

The Johnson graph `J(2m+epsilon,m)` is

\[
                         k=m(m+\varepsilon)                   \tag{2.3}
\]

regular.  Its eigenvalues are

\[
 \theta_j=(m-j)(m+\varepsilon-j)-j,\qquad 0\le j\le m. \tag{2.4}
\]

Moreover

\[
 \theta_{j+1}-\theta_j=-(2m+\varepsilon-2j)<0
 \quad(0\le j<m),                                    \tag{2.5}
\]

so the least eigenvalue is `theta_m=-m`.  Decomposing an arbitrary real
vector `v` into its constant and orthogonal parts gives

\[
 v^TA_Jv\ge {m(m+\varepsilon+1)\over W}
                  \left(\sum_Xv_X\right)^2-m\sum_Xv_X^2.     \tag{2.6}
\]

Apply this with `v=w` and use (2.2)--(2.2a):

\[
 2(c-z)\ge {4m(m+\varepsilon+1)\over W}c^2
                         -2mc-2mz.                    \tag{2.7}
\]

Consequently

\[
 {4m(m+\varepsilon+1)\over W}c^2
 \le2(m+1)c+2(m-1)z
 \le4mc,                                             \tag{2.8}
\]

where the last inequality uses `z<=c` and `m>=1`.  Dividing by `4mc`
when `c>0` proves (2.1). \(\square\)

The weighted treatment of isolated vertices is necessary: two formal ports
at one isolated owner are not two distinct vertices of an ordinary endpoint
set.  The port vector retains their multiplicity without inventing a loop.

### Theorem 2.2 (exact depth-one defect ledger)

Suppose in addition that both colour maps are injective on `E(F_0)`, and
write `c_0=c(F_0)`.  For the maximal splice forest `F` of Theorem 2.1,

\[
 M_\sigma(F)\le M_\sigma(F_0),
 \qquad
 R_\sigma(F)\le c_0-c(F)<c_0
 \quad(\sigma\in\{-,+\}).                            \tag{2.9}
\]

Consequently, if `c_0=o(W)`, then

\[
 M_-(F)+M_+(F)+R_-(F)+R_+(F)=o(W),                  \tag{2.10}
\]

and (0.3) holds for every `H=o(m)`.

For reference, the initial hole counts are forced exactly by `c_0`.  On
even ground,

\[
 M_-(F_0)=M_+(F_0)=c_0-{W\over m+1},                 \tag{2.9a}
\]

whereas on odd ground,

\[
 M_-(F_0)=c_0-{2W\over m+2},\qquad M_+(F_0)=c_0.     \tag{2.9b}
\]

For the final forest there is also an exact signed conservation law.  For
every graph and either shore,

\[
                         R_\sigma-M_\sigma=|E|-N_\sigma,       \tag{2.9c}
\]

where `N_sigma` is the size of that shore.  Since `|E(F)|=W-c(F)`, on even
ground, with `K=W/(m+1)`,

\[
 R_-(F)-M_-(F)=R_+(F)-M_+(F)=K-c(F),                \tag{2.9d}
\]

whereas on odd ground

\[
 R_-(F)-M_-(F)={2W\over m+2}-c(F),\qquad
 R_+(F)-M_+(F)=-c(F).                                \tag{2.9e}
\]

These identities locate, rather than hide, the repeats introduced by
unrestricted fusion.

#### Proof

Exactly `s=c_0-c(F)` splice edges are added.  Adding an edge never removes a
colour from either support, proving the first inequality in (2.9).  On one
fixed shore, one added edge increases `|E|` by one and increases the support
size by either zero or one.  It therefore increases collision excess by at
most one.  Since the initial excess is zero, `R_sigma(F)<=s`.

If `c_0=o(W)`, the audited two-sided pseudoforest has
`M_sigma(F_0)=o(W)`, so (2.10) follows.  Finally (2.1) gives

\[
 {Hc(F)\over W}
 \le {H\over m+\varepsilon+1}=o(1).                 \tag{2.11}
\]

This proves the theorem. \(\square\)

Every new transition is a literal Johnson edge.  Thus (2.9) measures only
target multiplicity; there are no nonphysical seams hidden in the proof.

## 3. Classification of the two-flag rectangle

A Johnson edge is equivalently a Boolean diamond flag

\[
 (S,U),\qquad S\in\mathcal L,\quad U\in\mathcal U,\quad S\subset U. \tag{3.1}
\]

If `U\setminus S={a,b}`, the corresponding owner edge joins
`S+a` and `S+b`.

### Lemma 3.1 (the only nontrivial `2 x 2` flag switch is a star)

Let `S,T` be distinct lower colours and `U,V` distinct upper colours.
Suppose all four containments

\[
 S\subset U,\quad T\subset V,\quad S\subset V,\quad T\subset U \tag{3.2}
\]

hold.  Then there is a unique middle set

\[
                         X=S\cup T=U\cap V,                   \tag{3.3}
\]

and distinct coordinates `p,q in X`, `a,b notin X` such that

\[
 S=X-p,\qquad T=X-q,\qquad U=X+a,\qquad V=X+b.        \tag{3.4}
\]

The old flags `(S,U),(T,V)` lift to

\[
 X--(X-p+a),\qquad X--(X-q+b),                       \tag{3.5}
\]

whereas the crossed flags `(S,V),(T,U)` lift to

\[
 X--(X-p+b),\qquad X--(X-q+a).                       \tag{3.6}
\]

#### Proof

Both `S` and `T` lie in `U cap V`.  Since `U,V` are distinct
`(m+1)`-sets, `|U cap V|<=m`.  On the other hand, two distinct
`(m-1)`-sets have union of size at least `m`.  Hence equality holds
throughout:

\[
 |S\cup T|=|U\cap V|=m,
 \qquad S\cup T=U\cap V.
\]

This proves (3.3), and (3.4) follows by taking the unique deleted and added
coordinates.  Formulas (3.5)--(3.6) are the two intermediate-rank vertices
in each interval. \(\square\)

## 4. Exact two-switch rigidity

Let `B_0`, `B_-`, and `B_+` be the incidence maps from Johnson edges to,
respectively, their two middle endpoints, lower colour, and upper colour.

### Theorem 4.1 (no exact two-edge fusion switch)

Let `e_1,e_2,f_1,f_2` be Johnson edges.  Assume that `e_1,e_2` have
distinct lower colours and distinct upper colours, and that after cancelling
common edges

\[
 e_1+e_2\ne f_1+f_2.                                  \tag{4.1}
\]

Then one cannot have simultaneously

\[
 B_0(e_1+e_2)=B_0(f_1+f_2),
 \quad
 B_-(e_1+e_2)=B_-(f_1+f_2),
 \quad
 B_+(e_1+e_2)=B_+(f_1+f_2).                          \tag{4.2}
\]

In particular, a nontrivial ordinary graph `2`-switch cannot preserve both
colour multisets.

#### Proof

The last two equalities in (4.2) say that the two new flags use exactly the
same two lower and two upper colours.  If their lower-to-upper pairing is
unchanged, the flag determines the Johnson edge uniquely and the trade is
trivial.  Thus a nontrivial trade must cross the two pairings.  Lemma 3.1
applies.

Use its notation.  The central owner `X` has multiplicity two on both sides
of the proposed trade.  After cancelling it, equality under `B_0` would
require

\[
 e_{X-p+a}+e_{X-q+b}=e_{X-p+b}+e_{X-q+a}.             \tag{4.3}
\]

The four displayed middle sets are pairwise distinct: an equality with the
same deleted coordinate would force `a=b`, an equality with the same added
coordinate would force `p=q`, and a crossed equality forces both.  This
contradicts (4.3). \(\square\)

Thus the flag rectangle is a star-collar transfer, not a component-fusing
degree-preserving switch.  Any exact common-owner fusion must use a larger
compound trade or an augmenting construction which consumes previously
unused colours.

### Corollary 4.2 (colour-capacity floor)

Let `F` and `F'` be spanning two-sided-rainbow linear forests on the same
middle owner set.  Then

\[
 c(F)-c(F')=|E(F')|-|E(F)|
 \le\min\{M_-(F),M_+(F)\}.                           \tag{4.4}
\]

#### Proof

A rainbow extension can use at most one new member of each colour shore.
Hence its net edge increase is bounded by the number of colours absent from
each shore.  For spanning forests, (c=W-|E|). \(\square\)

Equation (4.4) is only a capacity bound.  Achieving it requires the missing
lower and upper colours to pair into physical diamonds whose two owners have
compatible residual degree slots.  This is precisely where capacitated Hall
and common ownership enter.

## 5. Exact odd-ground Hall completion and the component count

Now specialize to `n=2m+1`.  Then

\[
 |\mathcal X|=|\mathcal U|=W,\qquad
 |\mathcal L|=N_1={m\over m+2}W,\qquad
 d=W-N_1={2W\over m+2}.                              \tag{5.1}
\]

Let `F` be a forest with exactly one edge of every lower colour, pairwise
distinct upper colours, and middle degree at most two.  Necessarily
`|E(F)|=N_1`, so, after isolated owners are included, it has exactly

\[
                         W-N_1=d                             \tag{5.2}
\]

components.  Already this exact core has two-sided injectivity, complete
lower support, only `d=o(W)` upper holes, and

\[
                         d=o(W/H)                             \tag{5.3}
\]

for every `H=o(m)`.

For the stronger spanning-factor completion, put

\[
 \delta_F(X)=2-d_F(X),\qquad
 \mathcal U_0=\mathcal U\setminus u(F).               \tag{5.4}
\]

The exact residual theorem is the integral capacitated Hall condition

\[
 \sum_{X\in\mathcal A}\delta_F(X)
 \le
 \sum_{U\in\mathcal U_0}
       \min\{2,|\{X\in\mathcal A:X\subset U\}|\}
 \quad(\mathcal A\subseteq\mathcal X).               \tag{5.5}
\]

Indeed, (5.5) is the max-flow/min-cut criterion for choosing two distinct
middle facets of every unused `U`, while filling every residual middle
degree slot.  Integral capacities make the flow integral.  Adding the
resulting `d` Johnson edges yields a spanning `2`-factor which uses every
upper colour once and every lower colour at least once.

### Proposition 5.1 (the exact component target is automatic after Hall)

Every completion of a forest core `F` satisfying (5.5) has at most `d`
cycle components.  Consequently its number of components is `o(W/H)` for
every `H=o(m)`.

#### Proof

The forest `F` has exactly `d` path or isolated components by (5.2).  Its
degree deficits are precisely the two ports of each such component, counted
with multiplicity for an isolated owner.  The `d` completion edges pair all
`2d` ports.  Contracting every old path component gives a `2`-regular
multigraph on `d` vertices.  Each component of the completed factor is a
cycle of this quotient, so there are at most `d` of them.  Equation (5.3)
finishes the proof. \(\square\)

This proposition is stronger for the present scale than Hamilton fusion:
one does not need to force the quotient to be one cycle.  The Catalan-size
number `d=Theta(W/m)` is already negligible relative to `W/H` throughout
the Gaussian regime.

## 6. Relation to the four available constructions

The exact logical interfaces are now:

1.  A two-level GMM saturating cycle supplies every lower colour exactly
    once and has one nontrivial owner component plus `d` omitted owners, but
    its upper colours can collide.  Saturation alone does not give (5.5).
2.  A Middle Levels Hamilton cycle supplies every upper colour exactly once,
    but does not control its lower-colour histogram.
3.  The audited cloned-hypergraph construction supplies a spanning linear
    forest with both colour maps injective, `W-o(W)` edges, and `o(W)`
    components.  Theorem 2.2 upgrades its component count to `O(W/m)` while
    retaining `o(W)` total two-sided defect.  This is an unconditional
    positive depth-one common refinement in the defect sense.
4.  The capacitated Hall theorem (5.5) completes an exact core integrally,
    and Proposition 5.1 pays the desired component bound for free.  It does
    not construct the exact core, and the known pseudoforest can violate
    even singleton residual cuts after a prescribed local poisoning.

Thus the minimum exact hypothesis still missing is:

> Construct, after at most `o(W/H)` owner/colour loss if a near version is
> allowed, a lower-complete, upper-injective Johnson forest of maximum degree
> two whose residual data satisfy (5.5).

Ordinary two-edge fusion cannot prove this by Theorem 4.1.  A successful
proof must use a larger compound absorber or build Hall extendibility into
the initial four-resource matching.

## 7. Adversarial audit

The strongest positive statement is Theorem 2.2.  Its possible failure
points are as follows.

* Isolated owners cannot be inserted twice into an ordinary endpoint set.
  The proof instead uses a real port vector of weight two there.  Its larger
  squared norm is retained exactly in (2.2), rather than being discarded.
* Maximal endpoint splicing guarantees only that different components have
  no adjacent endpoints.  It does not make the port support independent;
  (2.2a) retains the possible one edge inside each current path.
* Added splice colours need not be fresh and may collide with old colours or
  with one another.  The proof claims only one unit of new collision excess
  per added edge, which is exact; it does not claim continued injectivity.
* The estimate `c_0=o(W)` is enough for `o(W)` colour defect, but not for
  `o(W/H)` colour defect.  No stronger rate is inferred from the
  fixed-uniformity pseudoforest theorem.
* Proposition 5.1 is conditional on both the exact core and every Hall cut
  (5.5).  Acyclicity and marginal colour balance alone do not imply these
  cuts.
* A literal spanning `2`-factor has `W` edges.  On odd ground the lower shore
  has only `N_1<W` colours, so its lower map cannot be injective.  The exact
  spanning formulation is therefore “upper colours once, lower colours at
  least once”; the exact two-sided-injective formulation is the
  `N_1`-edge near-spanning core.  Conflating these two formulations would be
  a counting error.

No step above proves the missing exact core or constant one beyond the
depth-one defect/component interface.

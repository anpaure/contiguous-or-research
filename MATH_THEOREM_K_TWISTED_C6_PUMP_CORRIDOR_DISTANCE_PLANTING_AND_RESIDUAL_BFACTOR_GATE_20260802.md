# Twisted-`C6` pump versus the fixed-`z` seven-ear corridor: deterministic separation and the residual factor gate

**Date:** 2026-08-02  
**Lane:** K, child-native voltage planting  
**Status:** unconditional deterministic separation of the two literal local
banks, exact resource counts, exact residual `b`-factor criterion, and exact
zero-charge fusion interface.  A spanning owner/lower-q1 factor containing
the developed pump is not proved.

## 0. Verdict

Put `k=2m-1` and let the residence depth be `d`.  Fix either oriented branch
of the twisted three-run quotient `C6` from
`MATH_THEOREM_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_AND_HISTORY_APERTURE_20260802.md`.
Its full physical development is a simple Johnson cycle on `3k` rank-`m`
owners, with `3k` distinct rank-`(m-1)` lower colours and `3k` distinct
rank-`(m+1)` immediate upper colours.  It is a literal unit-voltage pump.

The local fixed-`z` seven-ear corridor can be chosen occurrence-disjoint from
this pump by a deterministic Johnson-distance argument.  Define

\[
 B_m(R)=\sum_{j=0}^{R}{m\choose j}{m-1\choose j}.
\tag{0.1}
\]

If

\[
 3k B_m(2d+4)<{2m-2\choose m}
\tag{0.2}
\]

and

\[
 m\ge \max\{3d+4,\,2d+13\},
\tag{0.3}
\]

then there is a rank-`m` anchor `X` avoiding the fixed coordinate `z` such
that the complete local fixed-`z` packet, all fourteen rays, and all seven
explicit connector paths are owner-, lower-colour-, upper-q1-colour-,
incidence-, and occurrence-history-disjoint from the pump.  The same is true
after deleting any one connector to obtain A's opened protected path.

For `d=O(sqrt(m))`, (0.2) holds for all sufficiently large `m`: the left
side is `exp(O(sqrt(m) log m))`, whereas the right side is
`exp((2 log 2+o(1))m)`.

This closes **local resource separation**, not ambient owner/q1 planting.
The closed pump alone has `6k` protected incidence edges, and its open form
has `6k-2`; therefore the repository's small protected-factor theorem,
whose hypothesis is at most `m-2` protected incidences, cannot apply.  The
exact remaining owner/q1 gate is the residual Ore--Ryser system in Section
4.  This is the first genuine obstruction after local separation.

## 1. Exact pump ledger

Let `O_P,F_P,C_P` denote respectively the developed owner, lower-facet, and
immediate-upper banks of the closed pump.  The literal theorem gives

\[
 |O_P|=|F_P|=|C_P|=3k.
\tag{1.1}
\]

Its projected Johnson cycle has `3k` edges and its middle-levels incidence
lift has

\[
                         6k
\tag{1.2}
\]

edges.  Cutting the private physical closure `e_*` leaves

\[
 \begin{array}{c|c}
 \text{resource}&\text{open pump count}\\ \hline
 \text{owners}&3k\\
 \text{lower facets}&3k-1\\
 \text{immediate upper colours}&3k-1\\
 \text{projected edges}&3k-1\\
 \text{incidence edges}&6k-2.
 \end{array}
\tag{1.3}
\]

The omitted lower/upper pair and the oriented occurrence `e_*` are retained
in the branch state

\[
 (0,0,{\cal R}^{\varepsilon},e_*^{\varepsilon},\varepsilon),
 \qquad \varepsilon\in\{+1,-1\}.
\tag{1.4}
\]

These are physical counts.  Quotient support three must not be substituted
for (1.1)--(1.3) in a protected-factor budget.

A's complete seven-connector local cycle has `28d+35` projected edges and
`56d+70` incidence edges.  Deleting one connector `Q_j`, which has
`2d+4` projected edges, leaves a path with

\[
 \begin{array}{c|c}
 \text{resource}&\text{opened fixed-`z` path count}\\ \hline
 \text{owners}&26d+32\\
 \text{lower facets}&26d+31\\
 \text{immediate-upper occurrences}&26d+31\\
 \text{projected edges}&26d+31\\
 \text{incidence edges}&52d+62.
 \end{array}
\tag{1.5}
\]

Thus a disjoint closed pump plus opened fixed-`z` path has

\[
 \begin{aligned}
 v_O&=3k+26d+32,\\
 v_F&=v_C^{\rm occ}=3k+26d+31,\\
 L&=6k+52d+62.
 \end{aligned}
\tag{1.6}
\]

If the pump is also opened, its incidence total in the union is
`6k+52d+60`; this is still linear with leading coefficient six in `k` and
still lies permanently outside the small protected-factor range.

## 2. Radius of the fixed-`z` local bank

Use A's notation.  The anchor is `X`; the two deletion banks
`D^x,D^y` have size `d`, and the two marker banks `M^x,M^y` have size `d`.
Every central endpoint differs from `X` in at most three exchanges.
Every ray owner therefore lies within Johnson distance `d+3` of `X`.

For a connector `Q_i`, start from

\[
 C_0=C-(D^x\cup D^y),\qquad C=X-\{a,b,c\}.
\tag{2.1}
\]

During the first bank, at most all `d` coordinates of `D^x` and a prefix of
at most `d` coordinates of `D^y` are absent.  Let
`t_i=|H_i intersect X|`.  At the end of that bank the distance is at most
`2d+3-t_i`.  Write `H_i={gamma_i,u_i,v_i}` and let the first added active
label be `p_i in G_i-{gamma_i}`.  Immediately after the aperture insertion
the active contribution is

\[
 3-t_i+\mathbf 1_{\gamma_i\in X}
 =3-\mathbf 1_{u_i\in X}-\mathbf 1_{v_i\in X}\le3,
\tag{2.2}
\]

and after `u_i -> p_i` it is

\[
 3-t_i+\mathbf 1_{\gamma_i\in X}
       +\mathbf 1_{u_i\in X}-\mathbf 1_{p_i\in X}
 =3-\mathbf 1_{v_i\in X}-\mathbf 1_{p_i\in X}\le3.
\tag{2.3}
\]

This calculation is independent of the two allowed orders within the
displayed two-sets.  During the second bank the `D^x` coordinates return
monotonically; the last active replacement and aperture return obey the
same complementary identity.  Consequently every connector owner `V`
satisfies

\[
                           d_J(X,V)\le2d+3.
\tag{2.4}
\]

This bound covers the **full seven-connector local cycle**, not merely the
opened retained path.  Deleting one connector only removes resources.

### Lemma 2.1 (one extra unit covers facets and caps)

Let `V` be a local owner and `T` a pump owner.

* If a local lower facet and a pump lower facet are equal, choose their
  incident owners `V,T`; then `d_J(V,T)<=1`.
* If a local immediate-upper colour and a pump immediate-upper colour are
  equal, choose incident owners `V,T` inside that common rank-`(m+1)` set;
  again `d_J(V,T)<=1`.

Hence

\[
 d_J(X,O_P)>2d+4
\tag{2.5}
\]

prevents every owner, lower-facet and immediate-upper collision.  It also
prevents incidence and occurrence-labelled history collisions: an
incidence or transition occurrence contains its literal owner/facet data.
Bare coordinate names are not capacity-one resources and are not claimed
disjoint.

#### Proof

Two distinct rank-`m` supersets of one rank-`(m-1)` set differ in one
exchange.  Likewise two rank-`m` subsets of one rank-`(m+1)` set differ in
one exchange.  Combine either fact with (2.4) and the triangle inequality.
\(\square\)

## 3. Deterministic anchor packing

There are

\[
                    {k-1\choose m}={2m-2\choose m}
\tag{3.1}
\]

rank-`m` anchors avoiding the prescribed fixed coordinate `z`.  A Johnson
ball of radius `R` around one rank-`m` set has exactly `B_m(R)` members,
because a distance-`j` set removes `j` of its `m` coordinates and inserts
`j` of its `m-1` complementary coordinates.

### Theorem 3.1 (literal pump/corridor separation)

Under (0.2), some anchor `X` avoiding `z` obeys (2.5).  Under (0.3), A's
deletion/marker banks, heptagon roles and seven aperture labels can then be
chosen at `X`, and their complete local banks are resource-disjoint from the
pump.

#### Proof

The union of radius-`(2d+4)` balls around the `3k` pump owners contains at
most the left side of (0.2) anchors.  Equation (3.1) and strict inequality
leave an anchor outside the union.  The pump theorem needs
`m>=3(d+1)+1=3d+4`.  A's explicit seven-aperture construction needs
`m>=2d+3` internally and `k-m=m-1>=2d+12` externally, the latter being
`m>=2d+13`.  Thus (0.3) supplies both constructions.  Lemma 2.1 completes
the resource audit. \(\square\)

This is a joint existential choice.  It is not a theorem that an arbitrary
already frozen fixed-`z` anchor is disjoint from the pump.  Indeed choosing
`X` to be a pump owner gives an immediate owner collision.

## 4. Exact owner/q1 extension gate

Let `ML_m=(L,R;E)` be the rank-`(m-1)`/rank-`m` containment graph.  The
closed pump saturates the equal-size shores `F_P subset L` and `O_P subset R`.
Let `Q` be any 2-bounded protected fixed-`z` corridor bank disjoint from
those shores.  Put

\[
 L'=L-F_P,\qquad R'=R-O_P,
\tag{4.1}
\]

delete the already selected edges of `Q`, and define the residual demands

\[
 b(v)=2-d_Q(v),\qquad v\in L'\cup R'.
\tag{4.2}
\]

Let `G` be the resulting residual bipartite graph on `L',R'`.

### Theorem 4.1 (necessary and sufficient residual criterion)

The disjoint union of the closed pump and `Q` extends to a spanning
owner/lower-q1 two-factor if and only if, for every `S subseteq L'`,

\[
 \sum_{x\in S}b(x)
 \le
 \sum_{y\in R'}\min\{b(y),d_G(y,S)\}.
\tag{4.3}
\]

The two shore-demand totals agree automatically.  A violated set `S` is an
exact obstruction certificate.

#### Proof

After fixing the pump and `Q`, every remaining vertex must receive exactly
the demand (4.2).  Equation (4.3) is precisely the Ore--Ryser criterion for
that bipartite `b`-factor.  The shores originally have equal size; the pump
deletes `3k` vertices from each, and every edge of `Q` lowers one demand on
each shore, so the totals agree. \(\square\)

The small protected-factor theorem cannot establish (4.3): even the open
pump has `6k-2=12m-8>m-2` protected incidence edges.  Increasing `m` never
repairs this inequality.  Thus a quotient-equivariant extension theorem, an
explicit ambient factor containing the pump, or a direct proof of (4.3) is
genuinely required.

## 5. Two-edge no-go and the corrected zero-charge topology fusion

Suppose first that Theorem 4.1 supplies a factor in which the pump is a
closed component and A's protected path lies elsewhere.  Choose the branch
`epsilon` once and use the same oriented pump component in both fixed-`z`
terminal phases.  A's seven-ear rethread has relative displacement zero, so
it creates no second pump requirement.

The apparent smallest join would delete the pump private edge `e_*`, delete
one oriented ambient edge `f`, and add two cross seams `g_0,g_1`.  Its
necessary literal rows are the following.

1. **Topology:** the crossed pairing joins the two old components into one.
2. **Both histories:** the four clipped endpoint histories, transported to
   their literal frames, accept `g_0,g_1` in both polarities.
3. **Lower q1:**

   \[
      \{I(g_0),I(g_1)\}=\{I(e_*),I(f)\}
   \tag{5.1}
   \]

   as an occurrence multiset.
4. **Immediate upper:** either the exact multiset identity

   \[
      \{U(g_0),U(g_1)\}=\{U(e_*),U(f)\},
   \tag{5.2}
   \]

   or the explicitly declared support/backup inequalities of the host.
5. **Private state and absolute voltage:** every new seam avoids the other
   protected resources, and

   \[
    \sigma(g_0)+\sigma(g_1)
      -\sigma(e_*)-\sigma(f)=0
   \tag{5.3}
   \]

   in the child deck group.

These rows cannot hold on a nondegenerate exact lower-rainbow face.  The
two-edge theorem in
`MATH_THEOREM_K_TWISTED_C6_PUMP_CORRIDOR_ENDPOINT_AND_TERNARY_FUSION_GATE_20260802.md`
proves that (5.1), for four distinct endpoints, forces the two removed lower
colours to be equal.  Thus consuming `e_*` in a transparent rectangle is not
the corrected planting operation.

Instead retain `e_*` and choose a different pump edge as one old edge of a
literal Boolean hex.  Take two prepared old ambient edges on two other
components.  Replacing the three old edges by the opposite hex matching:

1. merges the three components into one when the old edges lie on three
   distinct components;
2. preserves the complete owner/lower/immediate-upper/tail/head inventories;
3. retains the exact private state (1.4); and
4. preserves voltage exactly when the three-edge signed switch charge is
   zero.

For one coherent physical lift, the last equality follows by cancellation
of the common typed tail and head multisets.  The six changed joins must
still pass the three positive and three negative collar tests; this is the
exact endpoint-state compatibility, not a marginal residence assertion.

There are `3k` pump edges.  Every forbidden coordinate occurs exactly three
times as a deletion and three times as an insertion, so a coordinate bank
`B` excludes at most `6|B|` edges.  Reserving `e_*` and a cyclic radius-`d`
history neighborhood excludes at most another `2d+1`.  Hence a nonprivate
pump target edge remains whenever

\[
                         3k>6|B|+2d+1.
\tag{5.4}
\]

For a fixed target edge, its Cartesian Boolean-hex completion has
`(m-1)(m-2)` raw choices.  If the two free coordinate shores lose
`|B_L|,|B_R|` labels and a typed resource bank deletes at most `lambda_Q`
further choices, a prepared hex remains under the exact sufficient
inequality

\[
       (m-1-|B_L|)(m-2-|B_R|)>\lambda_Q.
\tag{5.5}
\]

A fixed non-target lower, upper, tail, or head resource occurs in at most
`m-1` of these Cartesian options, giving the proof-safe estimate
`lambda_Q<=|Q|(m-1)`.  Inequalities (5.4)--(5.5) are supply conditions only;
they do not prove that the two ambient partner edges lie on distinct
components or have the required six boundary histories.

If the two nonpump components have total absolute voltage `kappa`, the fused
component has voltage `kappa+epsilon`.  To obtain the literal absolute seed
`epsilon`, one still needs `kappa=0`; relative zero displacement of A's two
phases alone does not imply this.  More generally it is enough that
`kappa+epsilon` lie in the required child residue fibre.

## 6. Scope

Proved here:

* explicit all-large-parameter separation of the full pump and full local
  seven-ear banks;
* exact shared-resource load `3k B_m(2d+4)` on anchor choice;
* exact physical pump counts;
* exact residual owner/q1 factor criterion; and
* the exact two-edge obstruction and the supply/compatibility equations for
  a private-edge-preserving ternary fusion.

Not proved here:

* the residual inequalities (4.3) for the twisted pump;
* an upper-complete or globally resident ambient factor;
* exterior all-width shadow preservation;
* terminal common-cap/compiler feasibility; or
* existence of two prepared history-compatible hex partner edges satisfying
  (5.4)--(5.5) and the component condition.

In particular, the local distance theorem must not be advertised as an
ambient planting theorem until the residual `b`-factor and fusion rows are
closed.

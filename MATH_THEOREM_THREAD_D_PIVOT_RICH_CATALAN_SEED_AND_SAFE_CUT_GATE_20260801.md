# Pivot-rich paths are common-independent Catalan seeds; only the global connector and safe-cut rows remain

Date: 2026-08-01  
Lane: Thread D, fixed-`H` upper-decorated Catalan connector  
Status: unconditional seed theorem, exact contracted connector equivalence,
and exact arbitrary-width cut gate.  No all-dimensional connector existence
or `B(k)+O(1)` conclusion is claimed.

## 0. Outcome

Put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

and let `ML_m` be the incidence graph on `mathcal L sqcup mathcal O`.  Write

\[
 W=|\mathcal L|=|\mathcal O|,qquad
 U=|\mathcal U|,qquad
 C=W-U=\operatorname {Cat}_m.                         \tag{0.1}
\]

Take `H` pairwise resource-disjoint copies of the pivot-rich packet in
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`
at rank `m`.  Each copy is a simple Johnson path of `3h` transitions.  Its
incidence lift is an alternating path of `6h` edges with distinct immediate
lower and immediate upper colours.  If

\[
                              6Hh\le m-2,                \tag{0.2}
\]

the small protected-factor theorem puts their union in a spanning
two-factor of `ML_m`.

The new point is that after two-colouring that factor into perfect
matchings `M_0,M_1`, the protected `M_1` half is automatically independent
in all four rooted-Catalan resources:

1. lower incidence tails;
2. middle-owner heads;
3. paired immediate-upper colours; and
4. the graphic matroid of rooted links.

Indeed its rooted links are `H` vertex-disjoint directed paths.  Thus the
pivot-rich packet creates no local ordered-four-transversal obstruction.
It is an admissible seed of size `3Hh`.

The exact global continuation is nevertheless not automatic.  It is the
following two-stage integral problem.

* Extend the seed to a size-`U` common independent set `Q_0` in four
  matroids.  Equivalently, find a protected upper-exact rooted Catalan
  forest.
* On the `C` residual ports find a perfect matching `F` whose contracted
  graphic rank is at least `C-s`.

If `s=O(H)`, then `M_0 union Q_0 union F` is an upper-`q1`-surjective factor
with at most `s` components.  Every component contains an `F`-edge.  Opening
one such edge per component leaves every edge of `Q_0`, hence every
immediate-upper colour, intact.  Therefore the opened forest has

\[
  s\text{ components},\qquad s\text{ lower-}q1\text{ cuts},
  \qquad\boxed{0\text{ immediate-upper holes}}.          \tag{0.3}
\]

The local packet also preserves arbitrary-width old OR occurrences, but
(0.3) does **not** extend automatically to deeper upper targets.  For a cut
set `D`, a target keeps an old occurrence exactly when one of its cyclic
occurrence intervals avoids `D`.  One cut can hit linearly many nested
upper targets.  Hence a full upper theorem needs one additional safe-cut
occurrence row; component count alone is insufficient.

## 1. The protected alternating seed

Let

\[
 V_0,V_1,\ldots,V_\ell,\qquad \ell=3h,                 \tag{1.1}
\]

be one protected rank-`m` Johnson path, and put

\[
 L_i=V_i\cap V_{i+1},\qquad R_i=V_i\cup V_{i+1}
                 \quad(0\le i<\ell).                   \tag{1.2}
\]

Its incidence lift is

\[
 V_0,L_0,V_1,L_1,\ldots,L_{\ell-1},V_\ell.            \tag{1.3}
\]

The pivot-rich theorem says that the `L_i` are distinct and the `R_i` are
distinct.  Resource-disjoint copies make these colours distinct between
different protected paths as well.

Let a spanning two-factor containing the protected paths be two-edge-coloured
as `M_0 dotcup M_1`.  The colour phase on a protected path is not prescribed:
it is the restriction of this global two-colouring.  Put

\[
 P_a=M_a\cap E(P)\qquad(a=0,1).                         \tag{1.4}
\]

For `e=LV in ML_m-M_0`, define

\[
 \operatorname{up}_{M_0}(e)=M_0(L)\cup V,qquad
 \lambda_{M_0}(e)=L\longrightarrow M_0^{-1}(V).        \tag{1.5}
\]

### Theorem 1.1 (pivot-rich common-independent seed)

The set `P_1` is a matching of size `H ell=3Hh`.  Its upper map is
injective, and its rooted links form `H` vertex-disjoint directed paths.
Consequently `P_1` is independent in the two shore-partition matroids, the
upper-colour partition matroid, and the rooted-link graphic matroid.

#### Proof

First suppose the first incidence edge of (1.3) lies in `M_0`.  Then

\[
 M_0(L_i)=V_i,qquad L_iV_{i+1}\in P_1.                \tag{1.6}
\]

Thus

\[
 \operatorname{up}_{M_0}(L_iV_{i+1})=V_i\cup V_{i+1}=R_i. \tag{1.7}
\]

For `i<ell-1`, the protected edge `L_(i+1)V_(i+1)` belongs to `M_0`, so

\[
 \lambda_{M_0}(L_iV_{i+1})=L_i\longrightarrow L_{i+1}. \tag{1.8}
\]

The terminal owner `V_ell` is matched by `M_0` to one lower vertex
`L_out` outside the protected lower vertices.  Hence the last link is

\[
                         L_{\ell-1}\longrightarrow L_{out}. \tag{1.9}
\]

Equations (1.8)--(1.9) are one directed path.  If the first edge of (1.3)
lies in `M_1`, the same argument runs in reverse from the other endpoint.

For several protected paths, every internal lower vertex is already used by
`P_0`.  A perfect matching cannot use it for another terminal owner, and
distinct terminal owners have distinct `M_0` preimages.  Thus the external
vertices in (1.9) are new and pairwise distinct.  The link paths are
vertex-disjoint.  Their edges are therefore graphic-independent.  Matching
independence is inherited from `M_1`, and (1.7) plus the packet's distinct
`R_i` proves upper-colour independence.  \(\square\)

### Corollary 1.2 (what fixed-`H` planting now proves)

Under (0.2), the small protected-factor theorem first supplies the
two-factor and hence some `M_0,M_1`.  Theorem 1.1 then supplies a literal
four-resource independent seed.  No separate local Hall, upper-collision,
or graphic-circuit test remains for the protected packet.

If matching-shore phases are prescribed in advance, one extra parity
condition is required: all prescribed phases lying in one eventual factor
cycle must agree with one of its two alternating edge-colourings.  The
unoriented protected-path theorem used here chooses the phase after the
factor and has no such row.

## 2. Exact contraction to the global Catalan problem

Fix `M_0` as above and let `E=E(ML_m)-M_0`.  On `E` define:

* `mathsf M_L`: at most one edge at each `L in mathcal L`;
* `mathsf M_O`: at most one edge at each `V in mathcal O`;
* `mathsf M_U`: at most one edge of each value
  `up_(M_0)(e) in mathcal U`; and
* `mathsf M_G`: the cycle matroid of the labelled link multigraph
  `lambda_(M_0)(E)`.

Theorem 1.1 says `P_1` is independent in all four.

### Theorem 2.1 (protected rooted-Catalan contraction)

There is an upper-exact rooted Catalan forest `Q_0` containing `P_1` if and
only if the four contracted matroids

\[
 \mathsf M_L/P_1,\quad \mathsf M_O/P_1,\quad
 \mathsf M_U/P_1,\quad \mathsf M_G/P_1                 \tag{2.1}
\]

have a common independent set `Z` of size

\[
                             |Z|=U-3Hh.                 \tag{2.2}
\]

Then `Q_0=P_1 dotcup Z`.  In particular `Q_0` uses every immediate-upper
colour exactly once and its links form a forest with exactly `C` components.

#### Proof

If `Q_0` exists, contraction of an independent subset says exactly that
`Q_0-P_1` is independent in every matroid in (2.1), and its size is (2.2).
Conversely, adjoining a common independent set of the contractions to
`P_1` remains independent in all four original matroids.  The first two
matroids make `Q_0` a matching.  It has `U` edges with `U` distinct upper
colours, so it uses the entire upper layer.  The fourth matroid makes its
links a forest.  A forest with `W` vertices and `U=W-C` edges has exactly
`C` components.  \(\square\)

This is a four-matroid common-extension problem, not ordinary bipartite
Hall or two-matroid intersection.  Each protected packet is already
independent in every individual matroid; the missing issue is integral
correlation between them.

Let `X subset mathcal L` and `Y subset mathcal O` be the shores left unused
by `Q_0`, and put

\[
             B_0=(ML_m-M_0)[X,Y].                       \tag{2.3}
\]

Both shores have size `C`.  Contract the components of
`lambda_(M_0)(Q_0)`, and write `bar lambda(e)` for the contracted labelled
link of `e in B_0`.

### Theorem 2.2 (residual connector equivalence)

For `1<=s<=C`, the following are equivalent.

1. `B_0` has a perfect matching `F` with
   \[
                          r_{\rm gr}(\bar\lambda(F))\ge C-s. \tag{2.4}
   \]
2. `M_0 union Q_0 union F` is an upper-`q1`-surjective two-factor
   containing all protected paths and having at most `s` components.

For each `F`, the component count is exactly

\[
 c(M_0\cup Q_0\cup F)=C-r_{\rm gr}(\bar\lambda(F)).    \tag{2.5}
\]

#### Proof

The union `Q_0 union F` is a perfect matching disjoint from `M_0`, so its
rooted links form a permutation on `mathcal L`.  The `Q_0` forest has rank
`U`; after contracting it, `F` contributes exactly the rank in (2.4).
Permutation cycles are the two-factor components, hence

\[
 c=W-U-r_{\rm gr}(\bar\lambda(F))
   =C-r_{\rm gr}(\bar\lambda(F)).
\]

Upper surjectivity is already supplied by `Q_0`, and protection follows
from `P_0 subset M_0`, `P_1 subset Q_0`.  \(\square\)

Theorems 2.1--2.2 are the exact protected form of the Catalan-forest plus
connector decomposition.  They are a reduction, not an existence proof.

## 3. Opening the connector costs no immediate-upper colour

### Theorem 3.1 (upper-transparent residual opening)

Let `c` be the number of components of the factor in Theorem 2.2.  Every
component contains at least one edge of `F`.  Choose one such edge from each
component and delete the chosen `c` edges.  The result is a `c`-component
incidence path forest which contains every protected path and has

\[
       c\text{ missing lower transitions and no missing
       immediate-upper colour}.                         \tag{3.1}
\]

#### Proof

A factor component containing no `F`-edge would give a cycle using only
`M_0 union Q_0`.  Its rooted links would be a cycle in the forest
`lambda_(M_0)(Q_0)`, impossible.  Thus the indicated cuts exist.  One edge
cut opens each cycle and does not touch a protected edge, since all
protected second-shore edges lie in `Q_0`.

Every immediate-upper colour has its unique selected occurrence in `Q_0`.
No `Q_0` edge is deleted, so all those colours remain.  Each deleted
incidence edge breaks at most the lower transition at its lower endpoint,
giving the first count in (3.1).  \(\square\)

Consequently (2.4) with `s=O(H)` proves precisely the requested
`O(H)`-component, immediate-upper-decorated host, with the stronger bound
zero on immediate-upper holes.  Its `O(H)` lower cuts may be assigned to
the usual boundary sidecar.  Residence at the new joins and a common
compiler cap are separate rows.

## 4. Arbitrary-width upper targets require a safe-cut row

Orient every cyclic owner component.  For an upper target `T`, let
`mathcal I_T` be its set of old cyclic occurrence intervals, and let
`E(I)` be the transition edges strictly traversed by occurrence `I`.
For a cut set `D`, define

\[
 \mathcal H(D)={T:D\cap E(I)\ne\varnothing
                         \text{ for every }I\in\mathcal I_T\}.          \tag{4.1}
\]

### Lemma 4.1 (exact old-occurrence survival)

After opening the cycles at `D`, a target `T` retains an old occurrence if
and only if `T notin mathcal H(D)`.  After arbitrary path concatenation,
the actual upper-hole set is contained in `mathcal H(D)`; equality holds
after deleting any targets newly witnessed across the new seams.

#### Proof

An old cyclic interval remains consecutive in the opened path precisely
when it crosses no cut.  This is exactly `D cap E(I)=empty`.  New seams can
create additional occurrences but cannot destroy a surviving old one.
\(\square\)

The pivot-rich insertion theorem gives occurrencewise preservation of all
old intervals through the packet.  Hence intervals lying wholly in a
protected packet never contribute to (4.1) when `D subset F`.  It gives no
information about unprotected occurrences crossing the global cuts.

### Proposition 4.2 (one cut can lose a linear upper tower)

Let `K` have size `r-1`, take fresh labels
`x_0,...,x_(n-1)`, and consider the cyclic rank-`r` Johnson chronology

\[
                         V_i=K\cup\{x_i\}.              \tag{4.2}
\]

Cut the transition `V_0V_1`.  For `1<=j<=n-2`, the target

\[
                         T_j=K\cup\{x_0,...,x_j\}       \tag{4.3}
\]

has one cyclic occurrence, namely `V_0,...,V_j`, and every such occurrence
crosses the cut.  Thus one cut destroys `n-2` old upper targets, including
`n-3` targets strictly deeper than the immediate upper layer.

#### Proof

An interval in (4.2) has union `K` together with one cyclic consecutive
block of the `x_i`.  The block `{x_0,...,x_j}` is represented uniquely by
the displayed interval.  It traverses `V_0V_1`, so Lemma 4.1 applies.
\(\square\)

Therefore `O(H)` components do not imply `O(H)` arbitrary-width upper
holes.  A sufficient exact global row is

\[
                              |\mathcal H(D)|\le bH       \tag{4.4}
\]

for a choice of one residual `F`-edge per component.  Exact zero damage is
the stronger condition `mathcal H(D)=empty`.  If planned seam gains are
used, replace (4.4) by the literal final occurrence replay; (4.4) remains a
proof-safe upper bound.

## 5. Sharp remaining theorem

The pivot-rich local packet closes all hereditary seed rows.  The remaining
uniform statement is:

> **Protected Catalan connector with safe cuts.**  Starting from the
> common-independent seed `P_1`, find `Q_0` and `F` satisfying Theorems
> 2.1--2.2 with `s<=aH`, and choose one `F`-cut per factor component with
> `|mathcal H(D)|<=bH`, for absolute constants `a,b`.  Preserve the clipped
> residence flags at the packet endpoints and admit all selected rows in
> one terminal common cap.

The first two clauses alone give owner completeness, lower-`q1`, zero
immediate-upper holes, and `O(H)` components.  The safe-cut clause is exactly
what upgrades this to `O(H)` arbitrary-width upper holes.  Endpoint
residence and common-cap compilation remain downstream guarded rows.

No scalar or ordinary-Hall argument proves this theorem.  The first stage
is a four-matroid common extension, while the second is a perfect matching
with near-spanning graphic rank.  With the protected seed deleted it is the
unprotected Catalan linear-matching/connector gate already isolated in the
repository.  Thus the explicit pivot-rich packet removes the local
obstruction but does not bypass the central integral-correlation theorem.

## 6. Scope audit

1. The upper word `upper-decorated` in Sections 2--3 means the immediate
   rank-`m+1` palette.  Arbitrary-width upper coverage is Section 4 and is a
   strictly stronger row.
2. Theorem 1.1 chooses the matching-shore phase after the containing
   two-factor.  Prescribed phases require the parity clause in Corollary
   1.2.
3. Local zero OR damage means every old packet-crossing occurrence
   transports.  It does not constrain the arbitrary completion outside the
   packet or the later component cuts.
4. Opening residual `F`-edges preserves all immediate-upper colours but
   loses one lower transition per component.  Those lower colours are a
   bounded sidecar when `s=O(H)`; they are not silently retained.
5. The theorem contains no assertion that the four contracted matroids have
   a common basis.  Independent extendibility in each matroid separately is
   insufficient.
6. The local common-`Q` witness of the pivot packet does not produce a
   common cap for `Q_0 union F`; that terminal compiler row remains explicit.

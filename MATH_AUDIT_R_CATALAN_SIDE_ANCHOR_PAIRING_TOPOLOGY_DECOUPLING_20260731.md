# Audit of the Catalan side-anchor topology decoupling theorem

Date: 2026-07-31  
Audited source:
`MATH_THEOREM_CATALAN_SIDE_ANCHOR_PAIRING_TOPOLOGY_DECOUPLING_20260731.md`  
Verdict: **PASS**, with the precise physical remainder isolated below.

## 1. Signed charge: valid

A side graph has

\[
 N=\binom{2n}{n-1}\quad\text{vertices},\qquad
 P=\binom{2n}{n-2}\quad\text{edges}.
\]

If it is a forest it has

\[
 H=N-P=C-K
\]

components.  An anchor has side degree at most one, so a path component
contains at most two distinct anchors.  From

\[
 c_0+c_1+c_2=H,qquad c_1+2c_2=C
\]

one gets exactly

\[
                         c_2-c_0=K.                   \tag{1.1}
\]

There is no hidden connectivity or incidence hypothesis in this count.
On the no-empty face `c_0=0`, the two-anchor component pairs form a
`K`-matching and the remaining `C-2K` anchors occur one per component.

## 2. Central partial matching: valid

After deleting arbitrary child edges `Q` from an oriented child path, every
retained component is a consecutive segment.  Such a segment is incident
with at most one deleted-edge head boundary and at most one deleted-edge
tail boundary.  Thus, after contraction, retained child segments induce a
partial matching `P_0` between the left and right copies of the seam-label
set.  Consecutive deleted edges cause no exception: their common intervening
vertex is a length-zero segment and supplies one ordinary `P_0` pair.

## 3. Greedy second-shore theorem: valid

For arbitrary cross matching `P_0` and arbitrary left `K`-matching `P_L`,
the graph `P_0 union P_L` is a forest.  Its components are subpaths of

```text
R-L-L-R,
```

and hence contain at most two as-yet unused right labels.

When a new right pair joins unused labels in two different components, it
preserves acyclicity and leaves at most

\[
                         r_1+r_2-2\le2
\]

unused right labels in the merged component.  Before edge `j+1`, `j<K`,
there are

\[
                       C-2j\ge C-2K+2>2
\]

unused right labels.  Since each component contains at most two, a
cross-component pair always exists.  This constructs the required
`K`-matching `P_R`.

The strict inequality is exact for this proof.  The Catalan recurrence

\[
 {C\over K}=4-{6\over n+2}>2
\]

supplies it for every `n>=2`.

### Theorem 3.1 (sharp completion including the perfect-pairing face)

More generally, let `r<=floor(C/2)` be the desired number of right-shore
pairs, and let `t_1` be the number of components of
`G_0=P_0 union P_L` containing exactly one right label.  Then a right
matching `P_R` of order `r` for which `G_0 union P_R` is a forest always
exists if `2r<C`.  If `2r=C`, it exists if and only if

\[
                              t_1\ge2.                 \tag{3.4}
\]

#### Proof

The strict case is the same greedy proof: before the last insertion there
are at least three unused right labels, while every current component holds
at most two.

Suppose `2r=C`, so every right label must be paired.  Contract the
components of `G_0`.  A contracted component containing one right label
must have final `P_R`-degree one, and one containing two right labels must
have final degree two.  Hence, if `t_1=0`, every nonisolated quotient vertex
has degree two and every completion contains a cycle.

Conversely, `t_1` is even because

\[
 C=t_1+2t_2,
\]

where `t_2` counts components containing two right labels.  If `t_1>=2`,
pair the `t_1` degree-one component nodes into `t_1/2` endpoint pairs and
distribute the `t_2` degree-two nodes along the resulting paths.  This
constructs a path forest with the required component degrees.  Assign its
incident edges bijectively to the one or two actual right labels in each
component.  The resulting `P_R` is a perfect matching of the right labels
and its quotient is that path forest. `square`

Thus the theorem source uses the clean strict face `r=K<C/2`; no parity
case is hidden there.  Equation (3.4) is the sharp abstract obstruction if
future side constructions consume every right anchor in a double-anchor
component.

## 4. Suppression and physical cycle rank: valid

The contracted physical attachment graph is obtained from

\[
                         P_0\cup P_L\cup P_R           \tag{4.1}
\]

by subdividing its three kinds of matching edge by the corresponding
central or side component nodes and by adjoining leaves for one-anchor
components.  Subdivision and leaf attachment preserve cycle rank.  Thus
acyclicity of (4.1), together with the already assumed side forests and
degree caps, is exactly sufficient for a physical linear forest.

This is a topology theorem only.  It neither constructs a diagonal
containment matching nor proves residence, deeper-shadow, or compiler
properties.

## 5. Endpoint order cannot repair a fixed bad pairing

Reversing a side path swaps its two geometric endpoint roles but does not
change the unordered pair of seam labels lying in that component.  Likewise
permuting path components does not change the induced matching.  Therefore
path orientation/order cannot remove a cycle already present in (4.1).

In the general inherited-tail/head model the smallest obstruction is the
four-label rectangle

\[
 P_L=\{l_1l_2\},\qquad P_R=\{r_1r_2\},\qquad
 P_0=\{l_1r_1,l_2r_2\}.                               \tag{5.1}
\]

(In the isolated common-port/prefix specialization, suppressing the common
ports identifies the two label copies and the same obstruction appears as
a parallel two-cycle.)  More generally, a nonempty label set closed under
all incident partial matching involutions is a cyclic obstruction.  One
must change a side pairing, not merely its displayed order.

## 6. Full prescribed-pair universality is false

The source proposes a clean sufficient **prescribed-pair punctured-side
theorem** as its remaining target.  That universal target is false already
at `n=3`.

### Lemma 6.1 (anchor transport budget)

Let a side path forest have `P` edges, and suppose its two-anchor components
realize an anchor matching `P_*`.  Then

\[
       \boxed{\sum_{qq'\in P_*}
       d_J\bigl(b(q),b(q')\bigr)\le P},                \tag{6.1}
\]

where `d_J` is distance in the appropriate Johnson graph on the side's
middle rank.

#### Proof

For each `qq' in P_*`, the unique path in its side component from `b(q)`
to `b(q')` has length at least their ambient Johnson distance.  Distinct
matched pairs occupy distinct components, so these paths are edge-disjoint.
Their total length is at most the total number `P` of side edges. `square`

### Corollary 6.2 (smallest Catalan obstruction)

At `n=3`, every 14-anchor bank on rank four of `[6]` has a requested
five-pair matching violating (6.1).

#### Proof

Here `P=binom(6,1)=6` and `K=Cat_3=5`.  Identify a rank-four anchor with
its missing two-set.  Johnson distance two means that the two missing
two-sets are disjoint.

The anchor bank contains 14 of the 15 two-sets.  It contains four distinct
two-sets which can be divided into two disjoint pairs.  Indeed, if the
omitted set is relabelled to `12`, use

\[
                    (13,24),\qquad(14,23).
\]

These give two requested anchor pairs of distance two.  Choose six further
anchors and pair them arbitrarily into three pairs; every such pair has
distance at least one.  The left side of (6.1) is at least

\[
                         2+2+1+1+1=7>6.
\]

Thus no side path forest can realize this requested matching. `square`

The negative statement concerns universal prescription, not the source's
proved abstract greedy topology theorem.  It also does not contradict the
positive `n=3` braid, which realizes one specially chosen low-transport
matching.

## 7. The viable sequential physical hypothesis

The greedy proof needs much less than arbitrary prescribed-pair
universality.

Here is the exact weaker online condition.  Fix `P_0` and a realized
no-empty left side pairing `P_L`.  A right-side construction has the
**cross-component ear extension property** if there are partial physical
right-side states

\[
                  \varnothing=R_0\subset R_1\subset\cdots
                  \subset R_K,\qquad |R_j|=j,          \tag{7.1}
\]

such that for every `j<K`:

1. `R_j` is a matching on right seam labels and is extendable to a
   saturating punctured right side forest with no anchor-free component;
2. the two endpoints of the new pair in `R_(j+1)-R_j` are unused and lie
   in distinct components of `P_0 union P_L union R_j`; and
3. the physical extension preserves all already installed palette edges,
   side degrees, and acyclicity.

### Theorem 7.1 (sequential physically feasible ear sufficiency)

The automatic common deletion basis, one realized no-empty left side, and
the cross-component ear extension property on the right imply an exact
five-sector linear forest.

#### Proof

Condition 2 is precisely the greedy edge rule in Section 3, so induction
makes `P_0 union P_L union R_K` a forest.  Condition 1 gives the required
`K` right pairs and no anchor-free component.  Condition 3 and the
suppression argument in Section 4 lift this abstract forest to the physical
support. `square`

This is weaker than prescribed-pair universality: the right shore need
realize only one adaptive sequence of cross-component pairs.  Conversely,
without some condition of this kind, the abstract greedy matching need not
belong to the projection of any Boolean side forest.

The exact remaining all-parameter physical theorem can therefore be stated
in either of two ways.

* Prove one no-empty left side plus the adaptive right-ear property (7.1),
  with each chosen pair satisfying the remaining transport budget.
* More generally, construct the two sides jointly while maintaining the
  contracted-forest invariant.

The automatic common-basis theorem closes neither statement; it controls
incidence bases, not their physical anchor-component pairings.

For avoidance of ambiguity, the now-refuted upper-shore universal assertion
had the following literal form.  Put

\[
 D^-=\binom{[2n]}n\setminus\{t_q:q\in Q\}.
\]

Given a requested `K`-matching `P_*` on `Q`, find a containment bijection

\[
 \mu:D^-\longrightarrow\binom{[2n]}{n+2},qquad d\subset\mu(d), \tag{6.2}
\]

and for each pair its forced Johnson edge between the two intermediate
rank-`n+1` sets, such that:

1. the resulting `P`-edge graph on all `N` rank-`n+1` vertices is a path
   forest;
2. every seam anchor `U_q` has degree at most one;
3. `U_q,U_(q')` lie in one component exactly for the pairs
   `qq' in P_*`; every unmatched anchor is the sole anchor of its component;
4. every component contains an anchor.

The lower-shore statement is its complement dual.  Corollary 6.2 shows that
one cannot demand (6.2) for every `P_*`, even on only one shore.  The exact
remaining gate is to show that the physically realizable projection contains
**some adaptive cross-component sequence** of the form (7.1), not that this
projection is the complete matching complex.

## 8. Independent finite corroboration

The retained audit

```text
scratch/catalan_side_anchor_pairing_topology_20260731.audit.json
```

reports `PASS`, checks the Catalan identities through `n=100`, exhausts the
abstract cases `(C,K)=(5,2),(8,3)`, and reconstructs the frozen physical
histograms

```text
n=3: minus 1^4 2^5; plus 1^4 2^5,
n=4: minus 1^14 2^14; plus 0^1 1^12 2^15.
```

These checks corroborate but are not used to infer the all-parameter proof.

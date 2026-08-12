# Odd `h=1`: exact run transfer and the balanced-lollipop gate

**Date:** 2026-08-02  
**Status:** unconditional identities and an exact reduction.  This note does
not construct a resident lollipop, prove upper coverage, solve the compiler,
or prove `nu(17)=24313`.

## 0. Setting

Put

\[
 k=2r-1,\qquad W={k\choose r},\qquad
 C=\operatorname {Cat}_{r-1}={1\over r}{2r-2\choose r-1}.
\]

Let

\[
 T_0,T_1,\ldots,T_{W-1}
\]

be a cyclic order of all rank-`r` sets in which every consecutive pair is a
Johnson edge.  Suppose its rank-`(r-1)` intersection colours use every
coatom once except that `M` is absent and `D` occurs twice.  Necessarily

\[
 |M\cap D|=r-2.
\]

Write

\[
 a\in M\setminus D,\qquad b\in D\setminus M,
 \qquad K=M\cap D.
\]

This is exactly the physical owner chronology decoded from an `h=1`
augmented-incidence lollipop after replacing the artificial edge `MB` by
the physical duplicate edge `DB`, as in
`MATH_THEOREM_K17_H1_INCIDENCE_EULER_REDUCTION_20260802.md`.

## 1. Exact coordinate-run transfer

For a coordinate `x`, let `R_x` be the number of cyclic positive `x`-runs
in the owner order.  Equivalently, it is the number of zero gaps.

### Theorem 1.1

For every coordinate `x`,

\[
 \boxed{R_x=C+\mathbf1_{x\in M}-\mathbf1_{x\in D}.}       \tag{1.1}
\]

Consequently,

\[
 R_a=C+1,\qquad R_b=C-1,\qquad
 R_x=C\quad(x\notin\{a,b\}).                            \tag{1.2}
\]

Thus an `h=1` exceptional port transfers exactly one run component from
coordinate `b` to coordinate `a`; it does not change the run count of any
other coordinate.

#### Proof

Delete one of the two physical adjacencies whose intersection is `D` and
call it exceptional.  The other `W-1` adjacencies have distinct
intersection colours.  In the notation of the near-rainbow run identity,
the missing-colour family is `{M}` and the exceptional seam has
intersection `D`.  Therefore

\[
 m_x^1=\mathbf1_{x\in M},\qquad
 b_x^1=\mathbf1_{x\in D}.
\]

Substitution in

\[
 R_x=C+m_x^1-b_x^1
\]

gives (1.1).  Since `M` and `D` are adjacent coatoms, their symmetric
difference is exactly `{a,b}`, which gives (1.2).  \(\square\)

### Corollary 1.2 (no aggregate residence obstruction)

Every coordinate occurs in exactly `rC` owners and is absent from exactly
`(r-1)C` owners.  Hence its positive-run and zero-gap average lengths are

\[
 \begin{array}{c|ccc}
  &x=a&x=b&x\notin\{a,b\}\\ \hline
  \text{positive average}
   &\dfrac{rC}{C+1}&\dfrac{rC}{C-1}&r\\[6pt]
  \text{zero average}
   &\dfrac{(r-1)C}{C+1}&\dfrac{(r-1)C}{C-1}&r-1.
 \end{array}                                             \tag{1.3}
\]

For `r>=3`, `C+1>=r`.  Therefore

\[
 \left\lfloor{rC\over C+1}\right\rfloor=r-1.            \tag{1.4}
\]

In particular, the extra split at `a` is compatible at the scalar level
with every positive residence floor `h<=r-1`.  At `K17`,

\[
 r=9,\quad C=1430,
\]

so the three positive averages are respectively

\[
 {12870\over1431},\quad {12870\over1429},\quad 9.
\]

The required depth-three source factor has positive owner-run floor four,
well below this scalar ceiling.  Hence any failure is a component-size or
chronology obstruction, not a run-count obstruction.

For completeness, the corresponding zero-gap ceiling at `a` is `r-2`,
because

\[
 \left\lfloor{(r-1)C\over C+1}\right\rfloor=r-2.        \tag{1.5}
\]

Thus one must not infer a common floor `r-1` on both polarities.  The K17
floor four is nevertheless below both ceilings.

## 2. Exact Catalan-forest interpretation

Fix a coordinate `x`.  On the `rC` owners containing `x`, delete `x` and
keep precisely the physical owner adjacencies whose two endpoints both
contain `x`.  The result is a spanning linear forest `F_x^+` on all
rank-`(r-1)` subsets of `[k]-{x}`.  Its component orders are exactly the
positive `x`-run lengths.

Likewise, complementing the owners omitting `x` produces a spanning linear
forest `F_x^-` on the rank-`(r-2)` subsets of `[k]-{x}` whose component
orders are exactly the zero-gap lengths.

### Theorem 2.1 (one-component transfer on both shores)

Both forests have exactly `R_x` components.  Thus

\[
 \#\operatorname{comp}(F_a^\pm)=C+1,
 \qquad
 \#\operatorname{comp}(F_b^\pm)=C-1,                   \tag{2.1}
\]

and every other coordinate section has exactly `C` components.

Moreover, the internal positive-edge count is

\[
 (r-1)C-\mathbf1_{x\in M}+\mathbf1_{x\in D},           \tag{2.2}
\]

which uses every coatom containing `x`, except `M` when it contains `x`,
and uses `D` twice when it contains `x`.

#### Proof

The containing-`x` positions of the cyclic owner order split into exactly
`R_x` maximal blocks, so their induced graph is a linear forest with
`rC-R_x` edges.  Substituting (1.1) gives (2.2).  The complement statement
is the same cyclic block decomposition applied to the zero positions.
\(\square\)

### Corollary 2.2 (exact resident-lollipop criterion)

An `h=1` owner chronology is positively depth-`d` resident if and only if
every component of every `F_x^+` has order at least `d+1`.

It is positively and negatively depth-`d` resident if and only if the same
lower bound also holds for every component of every `F_x^-`.

Thus the central existence theorem plus aggregate run arithmetic reduce the
remaining residence row exactly to a **simultaneous balanced lollipop
forest** problem:

* `2k-4` coordinate forests have `C` components;
* the two forests for `a` have `C+1` components;
* the two forests for `b` have `C-1` components;
* all component orders must meet the required floor.

No other coordinatewise count changes.

## 3. A local safe-transfer sufficient condition

The component interpretation also identifies the only permitted local
shape of a residence-safe `h=1` run transfer.

### Lemma 3.1

Suppose a physical rethread from an exact-q1 resident chronology to the
`h=1` chronology has the following effect on coordinate sections:

1. in the `b` sections it joins two path components;
2. in the `a` sections it splits one path component into two pieces;
3. it preserves every other component order.

If the two pieces created in each `a` section both have order at least
`d+1`, then positive residence is preserved.  If the analogous statement
holds on the complemented zero sections, simultaneous positive/negative
residence is preserved.

#### Proof

Joining components cannot decrease their orders.  By hypothesis the only
new components are the two pieces in the `a` section, and both pass the
floor.  Every other component is unchanged.  Apply the same argument after
complementation for negative residence.  \(\square\)

This lemma is deliberately only sufficient.  The fixed-boundary lollipop
existence theorem does not presently construct its Hamilton path as a
single forest join/split relative to a resident exact-q1 factor, so it
cannot yet invoke Lemma 3.1.

## 4. Sharpened remaining gate

Before stating the remaining gate, there is an exact immediate-upper
conservation law which rules out a tempting but weak calibration source.

### Lemma 4.1 (two-cut immediate-upper bound)

Decode the `h=1` lollipop from an exact-q1 owner cycle by the local path
toggle.  At owner level this is a two-cut rethread: two old unordered owner
adjacencies are deleted and two new unordered owner adjacencies are added;
every other unordered adjacency is unchanged (one of the two intervening
segments may merely be reversed).

Consequently, if the starting owner cycle covers `U` distinct rank-`(r+1)`
immediate-union colours, the rethreaded cycle covers at most `U+2` such
colours.  Equivalently, if it starts with `H` immediate-upper holes, the
new cycle has at least

\[
                         \max(0,H-2)                 \tag{4.1}
\]

immediate-upper holes.

For the linear lollipop chronology the new wrap pair is not an interval.
Only one of the two new cyclic seam pairs is therefore a new internal
adjacency, so its immediate-upper support is at most `U+1` and its hole
count is at least `max(0,H-1)`.

#### Proof

An immediate-upper colour is the union of one unordered adjacent owner
pair.  Reversing a segment preserves every internal unordered adjacent
pair.  Only the two deleted seam pairs disappear and only the two new seam
pairs can introduce colours not previously present.  Hence the number of
distinct colours can increase by at most two.  \(\square\)

The authenticated published shift-one `K17` Middle Levels cycle covers
only `16932` of the `19448` rank-ten colours.  Therefore every single local
`P0` lollipop rethread of that fixed cycle still has at least

\[
                       19448-(16932+2)=2514          \tag{4.2}
\]

rank-ten holes.  Such a materialization remains useful for literal topology
and residence calibration, but it cannot be a K17 upper-complete answer.
The corresponding linear chronology has the stronger lower bound `2515`.
The theorem-guided linear finite search must instead rethread a seed with at
most one immediate-upper hole, preferably an already upper-q1-complete
carrier.

There is an equally sharp localization for residence.

### Lemma 4.2 (two-cut residence locality)

Let `S` be the total number, over all `k` coordinates, of cyclic positive
runs shorter than a prescribed floor `h`.  After reversing one cyclic owner
segment, at least

\[
                             S-4k                       \tag{4.3}
\]

of those original short runs persist with exactly the same lengths.

If the resulting cyclic order is opened at one Johnson edge to form a
linear chronology, at most `r+1` further cyclic positive runs can become
boundary-exempt.  Hence the number of internal short positive runs is at
least

\[
                         S-4k-(r+1).                   \tag{4.4}
\]

#### Proof

Cutting a cyclic binary coordinate word at the two rethread seams divides
it into two linear words.  Segment reversal reverses one of those words but
preserves every internal run and its length.  An original run can fail to
persist only if it contains one of the four seam endpoints.  There are at
most four such runs per coordinate, which proves (4.3).

Opening the final cycle can make at most one original cyclic run per
coordinate boundary-exempt.  Such a run must contain at least one endpoint
of the opening edge.  The two adjacent rank-`r` owners have a rank-`(r+1)`
union, so at most `r+1` coordinates occur at an endpoint.  This proves
(4.4).  \(\square\)

For the published K17 cycle, `S=7293`, so every one-P0 rethread followed by
any linear opening retains at least

\[
                        7293-4(17)-10=7215            \tag{4.5}
\]

internal short positive runs.  Likewise, a fixed seed with `1241` short
cyclic runs cannot be made resident by one two-cut rethread: at least `1163`
remain.  These are fixed-seed edit-radius statements, not global h1 no-go
theorems.  A resident h1 lollipop must be selected globally rather than
obtained by one local rethread of either bad seed.

## 5. Multiport correction is a coordinate-flow divergence

The one-port law extends exactly when several exceptional q1 ports remain
Johnson.

Let `M_1,...,M_b` be the missing coatom colours and let
`D_1,...,D_b` be the intersection colours on the `b` exceptional Johnson
seams, with multiplicity.  Pair the two lists arbitrarily.  The general
near-rainbow identity gives

\[
 R_x-C=\sum_{j=1}^b
       \bigl(\mathbf1_{x\in M_j}-\mathbf1_{x\in D_j}\bigr). \tag{5.1}
\]

### Theorem 5.1 (run-correction flow law)

Assume each paired `M_j,D_j` is Johnson-adjacent as coatoms.  Write

\[
 M_j-D_j=\{a_j\},\qquad D_j-M_j=\{b_j\},
\]

and form the directed coordinate multigraph with edge

\[
                            b_j\longrightarrow a_j.
\]

Then

\[
 \boxed{R_x-C=\operatorname{indeg}(x)-\operatorname{outdeg}(x).} \tag{5.2}
\]

Conversely, every directed coordinate edge `b->a` with `a!=b` is realizable
at the run-count level by choosing any rank-`(r-2)` core `K` disjoint from
`a,b` and taking

\[
                    M=K+\{a\},\qquad D=K+\{b\}.       \tag{5.3}
\]

#### Proof

For adjacent equal-rank sets, the summand in (5.1) is `+1` at `a_j`, `-1`
at `b_j`, and zero elsewhere.  Summing is exactly the directed divergence
in (5.2).  Construction (5.3) has the required symmetric difference and
gives the converse count actuator.  \(\square\)

Thus bounded exceptional ports are universal **component-count transporters**
on the coordinate set.  They can repair a bounded divergence vector without
changing the total number of run components.  This is only a marginal
statement: it neither embeds the ports in one chronology nor controls the
component orders, upper witnesses, or compiler incidences.

## 6. Sharpened remaining gate

Bare lollipop existence is unconditional.  The exact next theorem is now:

> **Balanced fixed-boundary lollipop theorem.**  For every sufficiently
> large `r` and every adjacent `(M,D)`, there is a fixed-boundary lollipop
> whose decoded owner chronology has all positive coordinate runs of length
> at least `d(2r-1)+1` (and, where the chosen source architecture requires
> it, the corresponding zero-gap floor), while retaining the required
> upper witnesses.

For finite `K17`, a materialized lollipop need only be tested against the
component criterion of Corollary 2.2; no age-state or source SAT model is
needed merely to decide residence.  Once that criterion passes, the exact
age-flag theorem supplies the unmarked depth-three source spelling.

The remaining downstream rows are complete upper coverage and the named
lower compiler on the same chronology.

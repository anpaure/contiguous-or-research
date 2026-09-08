# Nested active-column pruning and the compulsory retirement boundary

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** simultaneous all-depth heavy-row compiler proved; uniform
all-start use is quantitatively impossible on the mesoscopic depth scale,
so a retired active schedule is essential

## 0. Outcome

The capacity-`c` row-clone Hall theorem is a one-depth theorem.  At several
depths, one physical start is a column consuming several target resources,
so ordinary row-subfamily Hall is no longer sufficient.  There is,
however, a robust simultaneous fallback.

Consider `m` rows, at most `b` physical starts in each row, and depths
`1,...,H`.  An active column \(x\) in row \(C\) has an active depth set
\(I(C,x)\subseteq[H]\) and a target

\[
                         \lambda_q(C,x)\in\mathcal T_q
 \qquad(q\in I(C,x)).                                      \tag{0.1}
\]

The intended nested case has
\(I(C,x)=\{1,\ldots,\ell(C,x)\}\), but the theorem does not need that
extra property.  Put

\[
 \mu_q(T)=|\{(C,x):q\in I(C,x),\ \lambda_q(C,x)=T\}|,
 \qquad
 Q_* =\sum_{q=1}^H\sum_{T\in\mathcal T_q}(\mu_q(T)-1)_+.
 \tag{0.2}
\]

> **Simultaneous heavy-row compiler.**  For any integer \(c\ge1\), delete
> at most \(2Q_*/c\) rows and dirty at most \(c\) starts in every
> remaining row so that every surviving active target is distinct at every
> depth simultaneously.  If every column is active at at most \(H\)
> depths, then the lost active incidence is at most
> \[
>                    2H Q_*+{2bH Q_*\over c}.                \tag{0.3}
> \]

Thus the heavy-row part of capacity pruning survives all depths without a
growing-rank matching theorem.  Its sufficient quantitative hypothesis is

\[
                H Q_*\left(1+{b\over c}\right)=o(V),        \tag{0.4}
\]

where \(V=\sum_{C,x}|I(C,x)|\) is the active incidence value to be
preserved.

The theorem must be applied **after retirement**.  If every one of the
\(N=\binom{2r+1}r\) middle-factor starts is kept active through every depth
\(q\le H\), then collision-freeness at the final depth alone permits at
most

\[
 \binom{2r+1}{r-H}
 =N\prod_{j=0}^{H-1}{r-j\over r+2+j}                         \tag{0.5}
\]

columns.  At \(H=\Theta(\sqrt{r\log r})\), this is only a polynomially
small fraction of \(N\), not \((1-o(1))N\).  Therefore uniform nested
cleaning of almost every middle start is impossible on the intended
mesoscopic scale.  The alternating Greene--Kleitman theorem's declining
active population is not optional bookkeeping; it is structurally
necessary.

## 1. Repeated incidences and bad columns

Call an active incidence \((C,x,q)\) **repeated** when
\(\mu_q(\lambda_q(C,x))\ge2\).  Let \(E_*\) be the number of repeated
active incidences.  A physical start \((C,x)\) is **bad** if at least one
of its active incidences is repeated, and let \(B_*\) be the number of bad
starts.

### Lemma 1.1 (duplicate demand controls repeated incidences)

\[
                         B_*\le E_*\le2Q_*.                  \tag{1.1}
\]

#### Proof

For fixed \((q,T)\) with multiplicity \(a=\mu_q(T)\ge2\), its contribution
to \(E_*\) is \(a\), while its contribution to \(Q_*\) is \(a-1\).
Since \(a\le2(a-1)\), summing gives \(E_*\le2Q_*\).  Every bad start
contains at least one repeated incidence, so mapping it to any such
incidence injects bad starts into the set counted by \(E_*\).  \(\square\)

## 2. The simultaneous compiler

### Theorem 2.1 (nested heavy-row pruning)

Fix an integer \(c\ge1\).  Delete every row containing more than \(c\)
bad starts, and in every remaining row dirty all its bad starts.  Then:

1. at most \(2Q_*/c\) rows are deleted;
2. at most \(c\) starts are dirtied in a retained row; and
3. at every depth \(q\), all surviving targets are distinct.

If a row has at most \(b\) starts and a start is active at at most \(H\)
depths, the total lost active incidence is at most (0.3).

#### Proof

The sum of the bad-start degrees of all rows is \(B_*\).  Hence the number
of rows with degree greater than \(c\) is at most
\(B_*/c\le2Q_*/c\), proving 1.  Assertion 2 is the definition of a
retained row.

If a target occurrence survives and its original multiplicity was at
least two, then its start was bad and would have been dirtied.  Thus every
surviving occurrence had original multiplicity one, which proves 3
simultaneously for every depth.

Dirtying all bad starts loses at most \(HB_*\le2HQ_*\) active incidences.
Every deleted row contains at most \(bH\) active incidences, so row deletion
loses at most

\[
             bH\,{2Q_*\over c}.
\]

Adding the two terms proves (0.3).  \(\square\)

This construction never uses the false target-demand clone shortcut.
It deletes an actual physical start once, regardless of how many depths on
that start repeat.

### Corollary 2.2 (source-start loss)

The number of source starts removed by Theorem 2.1 is at most

\[
                         2Q_*+{2bQ_*\over c}.                 \tag{2.1}
\]

If the rows are wreath orders and one also wants the remaining source
starts paired into disjoint-middle ribbons, first dirty one arbitrary start
in a retained row having no bad start.  The within-row disjointness graph
is \(C_b\); matching the resulting path components discards at most one
more start per component.  Consequently a coarse source-level bound,
including deleted rows, dirty starts, and unmatched starts, is

\[
                         4Q_*+2m+{2bQ_*\over c}.              \tag{2.2}
\]

#### Proof

The row-deletion term is at most \(2bQ_*/c\), and the bad-start term is
\(B_*\le2Q_*\), proving (2.1).  After the optional padding, the total
number of dirty starts in retained rows is at most \(B_*+m\).  Deleting
these vertices from a \(C_b\) leaves at most the same number of path
components, whose maximum matchings leave at most one start each.  Thus
dirty plus unmatched starts cost at most \(2(B_*+m)\le4Q_*+2m\).  Add the
deleted-row term.  \(\square\)

The ribbon conclusion is only source-level.  It does not say that two
paired columns have equal retirement times, nor that the resulting
fragments instantiate the final product atoms.

## 3. Why the full all-start nested deck cannot be used

Now specialize to a central wreath factor on
\(b=2r+1\) coordinates.  Suppose every middle start is active through
depth \(H\), where its depth-\(q\) target is its same-start cyclic window
of rank \(r-q\).

There are \(N\) active starts at every depth.  At depth \(q\), there are
only

\[
                         L_q=\binom{2r+1}{r-q}                \tag{3.1}
\]

possible targets.  Hence any simultaneously target-disjoint start family
has size at most \(L_H\), proving (0.5).

The exact ratio is

\[
 {L_q\over N}=\prod_{j=0}^{q-1}{r-j\over r+2+j}.             \tag{3.2}
\]

For \(q=o(r^{3/4})\), logarithmic expansion gives

\[
 \log{L_q\over N}
   =-{q(q+1)\over r}+O\!\left({q^2\over r^2}
                              +{q^4\over r^3}\right).       \tag{3.3}
\]

In particular, the unavoidable aggregate duplicate demand of the full
all-start system satisfies, for \(H=o(\sqrt r)\),

\[
 \begin{aligned}
 Q_*&\ge\sum_{q=1}^H(N-L_q)\\
    &=(1+o(1)){N\over r}\sum_{q=1}^Hq(q+1)
      =\left({1\over3}+o(1)\right){NH^3\over r}.
                                                               \tag{3.4}
 \end{aligned}
\]

Since \(m=N/(2r+1)\), this is \(\Theta(mH^3)\).  Thus even the coarse
heavy-row guarantee requires substantial retirement well before the
mesoscopic endpoint.

For \(H=\alpha\sqrt{r\log r}\) with fixed \(\alpha>0\), (3.2) instead
gives

\[
                         {L_H\over N}=r^{-\alpha^2+o(1)}.     \tag{3.5}
\]

So a collision-free family active through depth \(H\) necessarily loses
\((1-o(1))N\) middle starts.  No refinement of the capacity-\(c\) pruning
argument can remove this cardinality obstruction.

## 4. Correct interface with Boolean retirement

Theorem 2.1 should be fed the **retired active schedule**, not all wreath
starts at all depths.  For such a schedule, let

\[
 V=\sum_{C,x}|I(C,x)|
\]

be its intended target-incidence value.  If one can coinstantiate the
abstract schedule in cyclic orders so that its aggregate duplicate demand
satisfies (0.4) for some \(c=o(b)\), then Theorem 2.1 removes all remaining
target collisions with only \(o(V)\) incidence loss and only
\(o(bm)\) source-start loss under the corresponding source version (2.1).

This is a genuine reduction, but it does not prove the required bound on
\(Q_*\).  The Boolean alternating Greene--Kleitman theorem supplies an
abstract target-disjoint retirement schedule before cyclic-order
coinstantiation.  Showing that almost all of it can be embedded with small
physical \(Q_*\) is still the multidepth order-bank gate.

## 5. Scope

The proved content is:

1. a simultaneous all-depth collision compiler with no growing-rank
   matching theorem;
2. exact bad-start, deleted-row, source, and active-incidence bounds;
3. a source-level fragmented-ribbon corollary; and
4. an exact cardinality obstruction to applying uniform all-start pruning
   at mesoscopic depth.

The note does **not** prove small \(Q_*\) for a physical coinstantiation of
the GK retirement schedule.  It does not preserve every abstract chain
when an earlier depth on the same column is dirty.  It does not align
retirement times across ribbon endpoints or compile the final product
atoms.

## 6. Checker

The finite audit is

```text
scratch/audit_nested_active_column_heavy_row_pruning_20260821.py
```

It exhausts and samples finite active-column systems, verifies
\(B_*\le E_*\le2Q_*\), the heavy-row and incidence-loss bounds, and
simultaneous uniqueness after pruning.  It also checks (3.2) and the exact
finite lower bound \(Q_*\ge\sum_q(N-L_q)\) on canonical factors through
\(b=9\).  The asymptotic estimates are analytic.

# Audit: promotion-ring global common history

Date: 2026-07-26

Audited file:
`MATH_ATTACK_O_PROMOTION_RING_GLOBAL_COMMON_HISTORY_20260726.md`.

## 0. Verdict

The paired quotient-chain theorem, compiler ledger, natural-macro
classification, block-factor scale, and projected triangle repair all
check.  The local integrality theorem is genuine and usable: it produces
one nested integral representative system serving both signed traces at
all depths, rather than separate depthwise Hall matchings.  Its natural
macro is a literal physical realization with one deleted phase per root.

The result is nevertheless local.  The hard global content is already
present in its hypotheses: paired fibres must coarsen with depth, both
coordinate projections must be injective, middle and shallow collision
ledgers must be small, and all physical cuts must be recycled.  No
selection with these properties on the complete root set is constructed.

The exact missing theorem is:

> Choose one cyclic frame at every critical root and a globally
> correlated nested occurrence family whose paired lower/upper traces
> form a quotient chain with injective coordinate projections, while
> simultaneously making \(C_0,D_{\ge q_0},q_0\delta_0,C_{<q_0}=o(W)\)
> and leaving only \(O(N_H)\), or at least \(o(W/H)\), final physical
> components after cross-splicing all cuts.

The block theorem proves that this cannot arise from independent shallow
macro blocks with uniform marginals.  It does not obstruct a single
deterministic globally correlated atlas.

## 1. Scale audit

Let

\[
 H=\max\{h:\lambda_h\le m+h\},\qquad M=m+H.
\]

The ratio

\[
 {\lambda_{H+1}\over\lambda_H}={m+H+1\over m-H}
\]

and maximality give

\[
 m-H<\lambda_H\le m+H.
\]

Therefore

\[
 MN_H=W+O(WH/m),\qquad N_H=(1+o(1))W/m,
\]

and \(2HN_H=o(W)\).  The expansion
\(\log\lambda_q=q^2/m+o(1)\) at this scale gives
\(H=(1+o(1))\sqrt{m\log m}\).

For \(q_0=m^{1/4}+O(1)\), direct summation of
\(N_q/W=1-q^2/m+O(m^{-1})\) gives

\[
 2\sum_{q<q_0}(N_q-N_{q_0})
 =\left({4\over3}+o(1)\right){Wq_0^3\over m}
 =O(Wm^{-1/4}).
\]

Thus every scale used in Outcome items 2--4 is compatible with an
\(o(W)\) compiler ledger.

## 2. Paired quotient-chain theorem

The condition

\[
 \Theta_{q+1}=F_q\circ\Theta_q
\]

says exactly that every depth-\(q\) fibre is contained in one
depth-\((q+1)\) fibre.  Starting with one representative per deepest
fibre and extending the representative set upward is valid because
distinct deep representatives cannot collide in a shallower fibre.
This proves nested integral sets

\[
 A_b\subseteq\cdots\subseteq A_a.
\]

Injectivity of both coordinate projections on the paired image then
makes the same representatives simultaneously injective in the lower
and upper targets.  The deficiency formula

\[
 2\sum_q(N_q-|I_q|)
\]

is exact.

This is more than a fractional or marginal result.  It is also less than
a rounding theorem: fibre coarsening and coordinate injectivity are
assumptions, and constructing them globally is the principal remaining
problem.

The cemetery lemma is correct.  On each active set the paired fibres are
singletons; stopped occurrences form one persistent cemetery fibre.  In
applications the cemetery is bookkeeping, not a physical target, so
deficiency counts should continue to use the active images, as the
compiler does.

## 3. Compiler audit

The middle conservation law is

\[
 C_0-Z_0=MN_H-W.
\]

Keeping every middle occurrence and appending missing middle targets
therefore costs exactly \(W+C_0\).  One cut per root contributes
\(2HN_H\).  At deep depths the paired SDR omits exactly
\(D_{\ge q_0}\) signed targets.

At \(q<q_0\), the selected family has size
\(N_{q_0}-\delta_0\), so for either sign

\[
 \#\mathrm{holes}
 =N_q-N_{q_0}+\delta_0+
   \sum_T(\mu_{q,T}-1)_+.
\]

Summing both signs and all shallow depths gives exactly the second line
of (4.5).  In particular, the factor \(q_0\delta_0\) is real; an
unweighted \(\delta_0=o(W)\) does not suffice.

The exterior bound

\[
 e^{-H^2/(8m)}W=m^{-1/8+o(1)}W=o(W)
\]

is consistent with the calibrated \(H\).  Outcome item 2 is therefore
correct.

## 4. Natural macro audit

Put \(s=m-H\) and decompose the ground set into a common ordered
\(2H\)-set \(Q\) and a cyclic \(2s\)-set \(V\).  The \(2s\) tops are

\[
 U_i=Q\cup T_i,
\]

where \(T_i\) is an \(s\)-window of \(V\).

At omitted length \(0<\ell\le2H<s\), equality of masks from rings
\(i\) and \(i+t\) forces omission of the prefix of \(T_i\) and suffix
of \(T_{i+t}\), and equality of the remaining \((s-\ell)\)-intervals
forces \(t=\ell\).  Thus every collision is exactly the displayed
prefix--suffix pair.  At \(\ell=2H\), the possibility that both omitted
sets equal all of \(Q\) gives distinct masks \(T_i\ne T_j\), so it adds
no collision; this endpoint is consistent with the theorem, although it
is worth keeping separate in the proof.

Deleting the suffix phase \(D_i\) in every ring removes exactly one side
of every cross-ring collision.  At lower depth \(q\), the deleted suffix
has its unique retained prefix partner in ring \(i-(H+q)\), so the raw
lower image is unchanged.  At the upper endpoint all phases in one ring
give its top, hence the explicit requirement of at most one depth-\(H\)
tag per ring.

Arbitrary stopping tags then give injective active lower and upper maps
and a cemetery quotient chain.  The macro has exactly
\(2s(M-1)\) retained occurrences and \(2s\) paths.  This is a genuine
literal local common-history block.

The tag arithmetic also checks:

\[
 (M-2)N_H\ge N_{q_0}-N_H,
\]

because \((M-1)N_H\ge W-N_H\ge N_{q_0}\).  Hence the desired census
fits after one deletion and one reserved depth-\(H\) phase per root.
This is only a capacity statement; no global collision-free tag
assignment is inferred.

Outcome item 3 is correct with precisely this local scope.

## 5. Independent-macro depth barrier

For one compatible root, a uniform cyclic frame hits a fixed middle
target with probability

\[
 p={M\over\binom MH},
\]

and the root-star mean is

\[
 \theta=\binom mH p={MN_H\over W}=1+o(1).
\]

One natural macro contains at most \(H+1\) roots from a fixed middle
star.  Thus a block of \(g\) macros has targetwise expected mass at most
\(g(H+1)p\).  Markov inside each block and independence between blocks
give the displayed hole floor exactly.

Stirling gives

\[
 \log(1/p)=\left({1\over2}+o(1)\right)H\log m.
\]

With branching at most \(2m\), a good independent hierarchy must
therefore have

\[
 d\ge(1/2-o(1))H.
\]

If an implementation pays one fresh cut per root at every level, its
collar is at least

\[
 2HdN_H\ge(1-o(1))H^2N_H
 =(1-o(1))W\log m.
\]

These are correct scale claims.  The collar conclusion is conditional
on that literal fresh-cut implementation; it is not a universal lower
bound.  Outcome item 4 states this qualification correctly.

## 6. Amplified triangle audit

The three displayed histories obey literal one-coordinate deletions.
The ground-set budget condition

\[
 m\ge3H+2q_0+1
\]

is sufficient to place them in three owner-disjoint promotion rings.
At each row their common-target incidence is the determinant-two
triangle, so total unimodularity and a universal full-depth quotient
core are indeed false.

After retaining one history, the only incomparable chronological pairs
among the missing targets are consecutive \(O_j,O_{j+1}\).  The two
explicit chains cover the entire missing ladder, and weights on
\(O_0,O_1\) give a matching fractional lower bound of two.  Thus the
unrestricted lower-history cover and fractional dual values are exactly
two, not \(\Theta(H)\).

For \(W/H\) disjoint copies the projected repair uses only
\(2W/H=o(W)\) individual lower histories.  This does not establish a
physical repair, because installing those histories as fresh frames or
paths incurs uncontrolled companions and collars.  Upper traces,
one-frame grouping, tags, middle loads, and cut recycling remain.  The
scale and scope claims in Outcome item 5 are correct.

## 7. Exact remaining global theorem

The natural macro solves local chronology but cannot be composed by
independent choices below correlation depth \((1/2-o(1))H\).  The
determinant-two ladder supplies no growing lower-only obstruction.  The
remaining theorem must therefore perform all of the following in one
globally correlated construction:

1. choose exactly one cyclic frame at every critical root;
2. impose suffix-closed paired fibres from \(q_0\) through \(H\);
3. make both lower and upper paired-image projections injective;
4. achieve
   \[
   C_0+D_{\ge q_0}+q_0\delta_0+C_{<q_0}=o(W);
   \]
5. realize the tag census; and
6. cross-splice all intermediate macro/ring cuts so the final physical
   component count is \(O(N_H)\), or at worst \(o(W/H)\).

Theorem 4.1 then gives coefficient one.  No current theorem supplies
this global correlated atlas, and no audited integer-hull inequality
rules it out.

# Audit of the delayed multistate mixed-rotor lift and combined fractional claims

**Date:** 2026-08-07  
**Audited sources:**

* `MATH_THEOREM_DELAYED_MULTISTATE_QUEUE_MIXED_ROTOR_LIFT_20260807.md`;
* corrected `MATH_THEOREM_BINARY_TOGGLE_VARIABLE_WEIGHT_QUEUE_AND_ROTOR_LIFT_20260807.md`.

**Verdict:** **LOCAL REPAIR PASS; COMBINED FRACTIONAL THEOREM PASS AFTER
TWO BOOKKEEPING CORRECTIONS.**  The delayed construction genuinely keeps
the appended \(1^a\) rail at the terminal ages and repairs the mixed-vertex
failure of the binary queue.  Interval decoding, owner rank, Johnson
adjacency, owner and immediate-palette simplicity, residence, regeneration,
the age profile, and the mixed coefficients all check.  The combined
owner-correlated averaging is valid, but its written proof incorrectly
says that every component has \(2p\) endpoints.  Delayed components have
type-dependent length \(L(d-a+1)\); normalization must be by endpoint mass
for each type.  Also, the stated \(R+O(d)\) coordinate use requires choosing
the minimal admissible clock length rather than an arbitrary \(L\).

## 1. Parameters and literal support

Put

\[
 D=d-a,qquad p=D+1=d-a+1,qquad 1\le a<d.
\]

For positive weights \(h_0,\ldots,h_{p-1}\), let \(H=\sum h_i\).  The
delayed word is

\[
 A_{up+i}=K\cup P_i\cup\{x_{i,u}\},
 \qquad u\in\mathbb Z_L, i\in\mathbb Z_p,
\tag{1.1}
\]

where

\[
 |K|=R-a-H,qquad |P_i|=h_i-1.
\]

Its period is

\[
 N=Lp,
\tag{1.2}
\]

and its exact local ground use is

\[
 (R-a-H)+(H-p)+Lp=R-a+p(L-1).
\tag{1.3}
\]

The conditions \(H\le R-a\) and

\[
 Lp\ge2(d+2)
\tag{1.4}
\]

make all sets legal and ensure that every interval audited below has
length at most half a literal period.

## 2. Interval decoder

Let \(Z_{t,j}\) be the union of the last \(j\) source letters at endpoint
\(t\), for \(1\le j\le d+2\).

If \(j<p\), the phases meeting the interval form a nonempty proper cyclic
phase interval.  The toggle-pair support recovers that interval even when
some \(P_i\) is empty.  Its terminal phase is the endpoint phase, and the
toggle at that phase gives the endpoint clock value.

If \(j\ge p\), every phase occurs.  For each phase \(i\),

\[
 Z_{t,j}\cap X_i
\]

is a nonempty proper directed cyclic interval of clock labels.  It is
proper because (1.4) gives

\[
 |Z_{t,j}\cap X_i|
 \le \left\lceil\frac jp\right\rceil
 \le\left\lceil\frac L2\right\rceil<L;
\]

here \(L\ge3\), since \(p\le d<d+2\).  No toggle repeats, so the sum of
these intersection sizes is exactly \(j\), recovering the interval length.
The last clock label in phase \(b\) is \(u\) for \(b\le i\) and \(u-1\)
for \(b>i\), where \(i\) is the endpoint phase.  The unique cut recovers
\(i\); if there is no cut then \(i=p-1\).  It then recovers \(u\).

Thus \((t,j)\mapsto Z_{t,j}\) is injective throughout the claimed range.
The interval-decoding lemma passes without a reflection ambiguity because
the clock orientation is labelled component data.

## 3. Owner rank and Johnson adjacency

A full owner has length

\[
 d+1=p+a.
\]

It contains every phase at least once, hence all of \(K\) and every
\(P_i\), together with exactly \(d+1\) distinct toggles.  Therefore

\[
 |O_t|
 =(R-a-H)+(H-p)+(d+1)=R.
\tag{3.1}
\]

Upon advancing the window, every phase remains represented, so the
\(K\)- and \(P_i\)-parts do not change.  Exactly one old toggle leaves and
one new toggle enters.  They are distinct because the combined interval
has length \(d+2<N\).  Consecutive owners therefore differ by one deletion
and one insertion.

The decoder at \(j=d+1\) makes all owners distinct, including the cyclic
closing pair.  Thus the flat simple Johnson owner-cycle claim passes.

## 4. Immediate palettes

The consecutive owner windows are the source-position intervals

\[
 [t-d,t]quad\text{and}\quad[t-d+1,t+1].
\]

Their union is \(Z_{t+1,d+2}\).  Their literal intersection is
\(Z_{t,d}\): the overlap of length \(d\) contains every phase because

\[
 d-p=a-1\ge0,
\]

so it already contains every common \(K\)- and \(P_i\)-coordinate;
toggle labels do not repeat inside the combined interval.  Hence

\[
 Q^-_t=Z_{t,d},qquad Q^+_t=Z_{t+1,d+2}.
\tag{4.1}
\]

The one-toggle owner swap gives ranks \(R-1\) and \(R+1\), while the
decoder proves both rows simple.  The complete immediate-palette claim
passes.

## 5. Residence and the delayed age profile

A literal toggle appears in one source position per period.  It belongs to
the next \(d+1\) owner windows and then is absent for

\[
 Lp-(d+1)\ge d+3
\]

windows.  Every \(K\)- and \(P_i\)-coordinate is permanent in the owner
row because every owner window contains every phase.  Thus two-sided owner
residence is exact.

At endpoint \(up+i\), the most recent \(p=D+1\) source positions contain
one copy of each phase.  They contribute

\[
 (R-a-H+h_i,h_{i-1},\ldots,h_{i-D})
\]

at ages \(0,\ldots,D\).  The preceding \(a\) source positions do not add
new \(K\)- or \(P_i\)-coordinates, because those phases already occurred
more recently, but each carries a distinct older toggle.  Their ages are
exactly

\[
 D+1,D+2,\ldots,D+a=d.
\]

Therefore the full age profile is

\[
 \boxed{
 (R-a-H+h_i,h_{i-1},\ldots,h_{i-D},1^a),
 }
\tag{5.1}
\]

and the singleton rail remains terminal as the endpoint advances.  This is
the feature missing from the rejected full-vector binary rotation.

## 6. Mixed-vertex coefficients

For a mixed vertex, put

\[
 B=b-a,qquad H=B+1,qquad R-a-H=R-b-1,
\]

and average over positive compositions of \(B+1\) into \(D+1\) parts.
The first \(D\) proper suffix cuts are the \(D\) uniformly chosen cut
positions among the \(B\) possible positions.  Hence each rank in

\[
 R-b,R-b+1,\ldots,R-a-1
\]

is offered with probability

\[
 \frac DB=\frac{d-a}{b-a}.
\]

The later \(a\) proper suffixes traverse the terminal singleton rail and
offer

\[
 R-a,R-a+1,\ldots,R-1
\]

at every endpoint.  The marked vector is therefore

\[
 \frac{b-d}{b-a}v_a+rac{d-a}{b-a}v_b.
\tag{6.1}
\]

This matches the genuine mixed monotone-rotor vertex exactly.  The repair
is not merely rank-equivalent in aggregate; equation (5.1) gives the exact
age-type orbit.

## 7. Coordinate budget

For the global asymptotic corollary, choose

\[
 L=\left\lceil\frac{2(d+2)}p\right\rceil.
\tag{7.1}
\]

Then

\[
 pL<2(d+2)+p
\]

and (1.3) is \(R+O(d)\), uniformly over every split \(1\le a<d\).
Thus the delayed queues embed when \(k-R\gg d\), as claimed for the
optimal asymptotic regime.

For arbitrary larger \(L\), the theorem remains locally true but its
coordinate use is \(R-a+p(L-1)\), not uniformly \(R+O(d)\).  The combined
corollary should explicitly make the choice (7.1).

## 8. Correct owner-correlated fractional averaging

Let queue type \(c\) have cycle length \(N_c\), and let \(\lambda_c\) be
its weight in the convex combination of endpoint rank profiles, with

\[
 \sum_c\lambda_c=1.
\]

Assign type \(c\) total endpoint mass

\[
 W\lambda_c
\]

and hence total component mass

\[
 \frac{W\lambda_c}{N_c}.
\tag{8.1}
\]

Average its labelled embeddings uniformly into \([k]\).  The symmetric
group is transitive on rank-\(R\) owners and separately on rank-\(s\)
targets.  The total owner endpoint mass is \(W\), so every one of the
\(W=\binom kR\) owners has load one.  The marked rank-\(s\) mass is
\(Wq_s\), so every rank-\(s\) target has load

\[
 \frac{Wq_s}{\binom ks}
 =1-\frac{b_s}{\binom ks}.
\tag{8.2}
\]

This proves the owner-correlated fractional statement on the same literal
components.

The sentence in the current proof of Corollary 3.3 saying

> Since every component has \(2p\) endpoints, its total component mass is
> \(W/(2p)\)

is false for the combined family.  A binary queue has
\(N_c=2(d+1)\), while a delayed mixed queue has
\(N_c=L(d-a+1)\), depending on its split.  Replacing that sentence by
(8.1) repairs the proof.  No equal component length is needed.

## 9. Exact scope

After the two corrections above, the combined local/fractional conclusion
is proof-safe:

* every monotone-rotor vertex has an owner-changing simple resident queue
  lift;
* their convex hull has exact owner and marked-target fractional marginals
  on the same literal components;
* the optimal Ferrers boundary supplies the complementary fractional
  target load.

It remains a convex mixture over many components and embeddings.  It does
not select every owner or named target once, make the components
owner-disjoint, fuse them, preserve arbitrary upper rows, or solve a
common-cap compiler.  Thus this genuinely upgrades the fractional trace
circulation, but it does not by itself advance the integral rounding gate.


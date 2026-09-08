# Audit of the unified rail-queue fractional Shadow--Braid theorem

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_UNIFIED_RAIL_QUEUE_FULL_FRACTIONAL_SHADOW_BRAID_20260807.md`  
**Verdict:** **PASS AFTER AN UPPER-TAIL COUNTING REPAIR AND EXPLICIT
DESIGNATION SCOPE.**  The local rail queue is exact for \(a=0\), every
mixed split, and the pure \(a=d,p=1\) rail.  The maximal-clock universe,
\(\delta v_d\) peeling, and \(\alpha_d\) asymptotics pass.  At the full
period \(j=Lp\), however, all endpoints give the same universe target;
there is one component-to-target incidence, not \(Lp\) distinct
incidences.  The written upper proof overcounts that row.  The all-rank
conclusion nevertheless survives: the full-ground pure-rail reserve alone
covers the boundary rank \(k-d\), the remaining top tail, and rank \(k\),
with the last rank evaluated using component mass rather than endpoint
mass.  Lower exactness refers to designated marks, not every incidental
physical lower interval; the immediate-palette exact loads similarly refer
to the selected component palette rows.

## 1. Unified local construction

Put

\[
 0\le a\le d,qquad p=d-a+1,
\]

and let the source period be \(N=Lp\).  The permanent owner bank has rank

\[
 |K|+\sum_i|P_i|
 =(R-a-H)+(H-p)=R-a-p.
\tag{1.1}
\]

Every source position contributes one label in the single labelled toggle
cycle of length \(N\).

For \(j<p\), an interval rank is

\[
 R-a-H+\sum_{v=0}^{j-1}h_{i-v}.
\tag{1.2}
\]

For \(p\le j\le N\), every phase bank is present and the interval contains
exactly \(j\) toggle labels, so

\[
 |Z_{t,j}|=R-a-p+j.
\tag{1.3}
\]

At the owner length \(j=d+1=p+a\), (1.3) gives rank \(R\).  Advancing an
owner removes the first toggle and adds the next toggle while preserving
the permanent bank.  The two toggles are distinct because
\(N\ge2(d+2)\).  Thus the owner row is a Johnson cycle.  Proper toggle
intervals in one labelled oriented cycle determine both endpoint and
length, proving owner and proper-deck simplicity.

The intersection and union of consecutive owners have the permanent bank
plus respectively \(d\) and \(d+2\) consecutive toggles.  Their ranks are
\(R-1,R+1\), and their toggle intervals prove local palette simplicity.
This argument includes \(a=0\): the source-position overlap then misses
one phase, but that phase's \(P_i\) bank occurs in both the outgoing and
incoming same-phase letters, so it remains in the literal owner
intersection.  The permanent-bank formulation is the correct one.

## 2. Endpoint age profile and boundary cases

The recent \(p\) source positions contain one occurrence of every phase
and give ages \(0,\ldots,p-1\).  The preceding \(a\) positions repeat
their phase banks but contribute distinct old toggles at ages
\(p,\ldots,p+a-1=d\).  Hence

\[
 c(t)=
 (R-a-H+h_i,h_{i-1},\ldots,h_{i-(p-1)},1^a).
\tag{2.1}
\]

The special cases are exact.

* If \(a=0\), then \(p=d+1\), and (2.1) is the ordinary positive
  composition rotor.
* If \(1\le a<d\), the reduced composition rotates while the appended
  \(1^a\) rail stays terminal.
* If \(a=d,p=1,h_0=1\), then
  \[
  c(t)=(R-d,1^d),
  \]
  the saturated short-clock profile \(v_d\).

Every toggle has owner run \(d+1\) and gap \(N-(d+1)\ge d+3\); the
permanent bank is present in every owner.  Residence and regeneration pass.

## 3. Maximal-clock universe

For fixed \((a,p)\), choose

\[
 L_{\max}=1+\left\lfloor\frac{k-R+a}{p}\right\rfloor,
 \qquad
 r_a=(k-R+a)\bmod p.
\]

The used universe is

\[
 U=R-a+p(L_{\max}-1)=k-r_a,
 \qquad0\le r_a<p\le d+1.
\tag{3.1}
\]

Thus \(U\ge k-d\).  At the optimal asymptotic scale the period condition
holds uniformly.  For the pure rail \(p=1\), \(r_a=0\) and \(U=k\).

One scope distinction is essential:

* for every \(u<U\), the corresponding interval length is proper, and the
  component has \(N\) distinct rank-\(u\) target values, one per endpoint;
* for \(u=U\), the interval length is \(N\), and all endpoints give the
  same used-universe target.  The component has only **one** distinct
  rank-\(U\) target value.

## 4. The \(\delta v_d\) peel

For sufficiently large parameters the Ferrers correction is supported
below \(R-d-1\).  Hence

\[
 \alpha_d
 =q_{R-d}-q_{R-d-1}
 =\frac{\binom{k}{R-d}-\binom{k}{R-d-1}}{W}.
\]

Using

\[
 \binom{k}{s}-\binom{k}{s-1}
 =\binom{k}{s}\frac{k-2s+1}{k-s+1},
\]

with \(s=R-d\), the central ratio
\(\binom{k}{R-d}/W\) stays bounded away from zero and infinity, while the
last factor is \(\Theta(d/k)=\Theta(1/d)\).  Therefore

\[
 \alpha_d=\Theta(d^{-1}).
\tag{4.1}
\]

On the other hand

\[
 \delta=\frac{\binom{k}{d}}W=e^{-\Theta(k)},
\]

so \(0<\delta<\alpha_d\) eventually.

Set

\[
 q'=\frac{q-\delta v_d}{1-\delta}.
\tag{4.2}
\]

The only changed monotonicity boundary has increment
\(\alpha_d-\delta\ge0\).  Below that boundary,
\(q_s\le q_{R-d-1}\le1-\alpha_d\le1-\delta\); above it,
\(q_s-\delta\le1-\delta\).  Nonnegativity follows from
\(q_{R-d}\ge\alpha_d\ge\delta\), and

\[
 \sum_s q'_s
 \le\frac{d-d\delta}{1-delta}=d.
\]

Thus \(q'\in\mathcal M_{R,d}\).  The peeling argument passes.

## 5. Exact repaired upper-load calculation

Let every queue type \(c\) receive endpoint mass \(W\lambda_c\) and
component mass \(W\lambda_c/N_c\).  The total endpoint mass is \(W\).

### Ranks \(R+1\le u\le k-d-1\)

Every maximal component has \(U_c\ge k-d>u\).  Its rank-\(u\) interval is
proper, so it contributes one distinct target value per endpoint.  Total
rank-\(u\) incidence mass is \(W\), and symmetry gives each target load

\[
 \frac W{\binom ku}\ge1.
\tag{5.1}
\]

### Ranks \(k-d\le u<k\)

Use only the full-ground pure-rail reserve.  Its endpoint mass is

\[
 \delta W=\binom kd.
\]

Every interval here is proper, hence distinct across endpoints.  Its
uniform rank-\(u\) load is

\[
 \frac{\binom kd}{\binom ku}
 =\frac{\binom kd}{\binom k{k-u}}ge1,
\tag{5.2}
\]

because \(0\le k-u\le d\) and the displayed range has \(u<k\).  At
\(u=k-d\), equality holds.

### Rank \(u=k\)

All full-period intervals in one pure-rail component equal \([k]\).  They
must be counted once at component level.  The pure-rail component length is

\[
 N_*=L_{\max}=1+k-R+d.
\]

Its load on the unique rank-\(k\) target is therefore

\[
 \frac{\delta W}{N_*}
 =\frac{\binom kd}{1+k-R+d}\ge1
\tag{5.3}
\]

for every sufficiently large parameter.  This repairs the repeated-
universe overcount while preserving all-rank upper coverage.

## 6. Designated versus physical occurrences

The lower monotone-rotor vector \(q\) counts **designated marks** on a
selected subset of proper suffix cells.  The rail queues also possess many
unmarked physical lower intervals.  Those incidental cells can only add
literal representations; they are not part of the equality

\[
 Wq_s+ b_s=\binom ks.
\]

Accordingly, the theorem's phrase “every lower target has load exactly
one” must mean designated lower load after adjoining the Ferrers marks, not
total physical occurrence multiplicity.

Likewise, the exact values

\[
 \frac W{\binom{k}{R-1}},
 \qquad
 \frac W{\binom{k}{R+1}}
\]

are the loads of the selected immediate owner-palette rows of the queue
components.  Incidental boundary or nonselected cells are not included in
those equalities.

Upper coverage is different: it uses the set of distinct physical target
values in each component deck.  Proper intervals contribute one value per
endpoint; the full-period universe contributes only one per component, as
accounted for in (5.3).

## 7. Final scope

After these corrections, the unified theorem genuinely removes the
fractional marginal obstructions for:

* owner load;
* designated strict-lower targets plus the Ferrers complement;
* every upper rank;
* the selected immediate palettes;
* local residence, regeneration, and simple topology.

It remains fractional.  It does not select owner- and target-disjoint
components, fuse their cycles, preserve a chosen upper witness under that
fusion, or construct one integral common cap.  Those are the surviving
occurrence-labelled gates.


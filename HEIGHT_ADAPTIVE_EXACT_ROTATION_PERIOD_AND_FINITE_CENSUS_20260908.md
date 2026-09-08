# Exact PBBS periods, finite construction lengths, and the native-construction barrier

2026-09-08. Independent symbolic audits and bounded exact computation of
the user's rotation-period continuation. The period formula, all reported
finite length comparisons, the construction-specific overhead barrier,
and the complete native routing obstruction at17 pass internal review.
The finite corridor, height-sensitive support, particle reduction and
rooted pruning-fibre theorems remain inputs. This is not external or
proof-assistant certification of those inputs.

The strongest recorded asymptotic upper estimate remains
exp[-.93(k(log k)^2)^(1/5)]. This continuation does not improve that
exponent. It evaluates the unchanged construction exactly at moderate
dimensions and proves that this construction cannot attain B(k) merely
through a sharper analysis of its periods.

## 1. Exact returns, including nonprimitive rows

Write n_0=n>n_1>...>n_h=1 for the equality-pruned circumferences. Row s
has p_s=n_(s+1) entries, least cyclic period d_s, and repetition factor
e_s=n_(s+1)/d_s. Put

\[
\sigma_j=\sum_{s=0}^{j-1}\frac1{n_s n_{s+1}}.
\]

With positive physical rotation rho^K, the exact criterion is

\[
f^T(A)=\rho^K(A)
\quad\Longleftrightarrow\quad
e_{j-1}\left(\frac K{n_0}-T\sigma_j\right)\in\mathbb Z
\quad(1\le j\le h).
\]

At one level the displacement identity is T=nm+pK, the row must be
fixed by shift m, and the child must return rotated by -m. Conversely,
the translated child bits together with invariant gaps fix every parent
gap; all particle offsets then agree, and their summed displacement
fixes that offset to K. This proves sufficiency as well as necessity.
The one-site bottom supplies the terminal return condition.

Consequently the exact physical period, for both f and f², is

\[
\boxed{v(A)=\operatorname{lcm}_{1\le j\le h}
\operatorname{den}(e_{j-1}\sigma_j).}
\]

Every denominator is odd, so squaring does not alter the period. Zero
rows have least period1 and are included. For the first L rows,

\[
\frac{M_L}{\gcd(M_L,E_L)}\mid v,
\qquad M_L=\operatorname{lcm}_{s<L}(n_s n_{s+1}),
\quad E_L=\operatorname{lcm}_{s<L}e_s.
\]

The [full independent audit](scratch/PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md)
checks the rotation sign, integer translations, both directions, the
terminal case, and the stated153/51 example. Root read it in full.

## 2. Exact construction census through dimension101

The peak counts m_s=(n_s-n_(s+1))/2 form a positive nonincreasing
partition of r. Their successive differences are row masses. For each
row, divisor subtraction counts compositions of each exact least period.
The rooted inverse-pruning bijection makes a period signature's root
multiplicity the product of those counts. Each root has n distinct
physical rotations because gcd(n,r)=1. Thus a signature with a roots
and period v has exactly na/v cycles, an integer.

Summing (2h-1) times those cycle counts computes the exact collar cost
C_n of the unchanged word N_n=W(n)+C_n. A new implementation processed
every odd dimension3..101 on h100, with300CPU/360wall/4GiB limits.
It passed in26.83seconds after checking1,295,970 partitions and1,702,866
least-period signatures. Every signature quotient was integral; every
dimension's total root count was Catalan_r and state count was W(n).
The counts at17 and19 also agree with the previously independently
constructed literal native banks. A separate agent reviewed the entire
new arithmetic implementation; root also read it in full.

| n | W(n) | Exact native collar cost C_n |
|---:|---:|---:|
|17|24,310|892|
|31|300,540,195|1,355,845|
|41|269,128,937,220|327,229,518|
|61|232,714,176,627,630,544|33,239,463,842,328|
|101|199,804,427,433,372,226,016,001,220,056|1,187,277,484,185,535,019,897,550|

In particular,

\[
\boxed{\nu(101)\le199805614710856411551021117606
<1.000006\,W(101).}
\]

Its relative overhead lies between
0.000005942198075572927182732101 and
0.000005942198075572927182732102: approximately5.9422parts per million.
The exact lower bound is B(101)=W(101)+7, leaving a construction-to-lower
gap of1,187,277,484,185,535,019,897,543. A small relative error at this
dimension therefore remains a large absolute gap; equality is not shown.

Every individual dimension in these ranges was checked by exact integer
comparison, including the ordinary doubling lift for even dimensions:

| Finite range | Strict construction upper bound |
|---|---|
|29<=k<=102|nu(k)<1.01W(k)|
|57<=k<=102|nu(k)<1.001W(k)|
|87<=k<=102|nu(k)<1.0001W(k)|

The six-parts-per-million comparison also holds at102. These are finite
ranges, not thresholds asserting the same percentage at every larger k.
No astronomical literal word was generated or scanned. These are exact
lengths of the construction whose coverage follows from the retained
finite support proof, distinct from a literal all-target word check.

Artifacts: [full finite census certificate](scratch/PBBS_EXACT_ROTATION_PERIOD_PARTITION_CENSUS_THROUGH101_CERTIFICATE_20260908.md),
[standalone new census](scratch/census_pbbs_exact_rotation_period_partitions_20260908.py),
[independent code review](scratch/PBBS_EXACT_PERIOD_PARTITION_CENSUS_CODE_INDEPENDENT_AUDIT_20260908.md),
and the [exact report](scratch/rotation_period_census_20260908/exact_rotation_period_census.json).

## 3. The unchanged word has exponential additive overhead

Split the peak partition into q maximal constant blocks, with boundary
circumferences x_0=n,...,x_q=1. Telescoping on each constant block shows

\[
v\mid\operatorname{lcm}_{1\le j\le q}(x_{j-1}x_j)
\mid\prod_{j=0}^{q}x_j,
\qquad v\le n^q.
\]

There are q distinct positive peak counts, so q(q+1)/2<=r. Put
Q_n=floor((sqrt(4n-3)-1)/2). Since h>=q, averaging the pointwise bound
(2h-1)/v>=(2Q_n-1)/n^Q_n gives

\[
\boxed{C_n\ge
\left\lceil\frac{(2Q_n-1)W(n)}{n^{Q_n}}\right\rceil
\ge\exp\{n\log2-O(\sqrt n\log n)\}.}
\]

The known endpoint-bound excess B(n)-W(n) is only O(sqrt n). Therefore
the unchanged native height-adaptive word exceeds B(n) for all sufficiently
large n. Its word or state inventory must change to reach the exact goal.
This is a lower bound on this construction's actual overhead, **not** on
the optimum nu(n)-W(n).

[Root's proof](scratch/PBBS_CORNER_PERIOD_UPPER_BOUND_AND_EXPONENTIAL_COLLAR_BARRIER_AUDIT_20260908.md)
and a [second independent audit](scratch/PBBS_CORNER_PERIOD_BARRIER_SECOND_INDEPENDENT_AUDIT_20260908.md)
both verify the corner denominators, common-factor handling, and scope.

## 4. Complete native-state routing obstruction at17

A separate bounded h100 reconstruction used the original D_i^h words,
not the later min(h,3) capped sources. All24,310 periodic recency states
were reconstructed and independently replayed by coordinate last times.
Their rank-eight and rank-nine prefixes are bijections of those layers,
and b_9=h. An edge to a different rank-nine label cannot increase b_9;
therefore every directed cycle stays at one height.

For a neutral predecessor P of destination Q, P's eight-prefix must lie
inside Q's nine-prefix. The eight-prefix bijection supplies exactly nine
candidates. Testing the complete move-to-front update for each same-height
candidate exhausts every edge relevant to a cyclic rerouting.

The independent run checked86,972 neutral candidates and found:

- 24,310 native edges;
- 24,310 self-loops;
- 17 extra edges, all canonical cycle83->103, height3, periods153->85;
- no additional same-component edges and no reverse component edge.

The component quotient is acyclic. Every cyclic permutation of these
states therefore remains within its original components; there, it must
use either the whole native cycle or all its self-loops. The minimum
component count is exactly146, and the original routing is uniquely
loop-free. The full [proof, checker and edge certificates](scratch/PBBS_NATIVE_RECENCY_ROUTING_OBSTRUCTION_COMPLETE_AUDIT_20260908.md)
were read by root. The run took1.94seconds with120CPU/150wall/2GiB caps.
Other claimed native graph dimensions were not rerun.

## 5. Consequence for continuing the exact goal

The current independently verified finite bound remains
24313<=nu(17)<=24658, gap345. This continuation supplied no new shorter
literal word, and its reported rewrite search was not replayed.

Our active exact-construction work already changes the state inventory:
it uses capped apertures, variable letters and named-target preservation.
The old native-state obstruction does not automatically apply to those
changed states. The separate canonical every-third-anchor frame has now
been refuted by an exact eight-step support certificate, and one specific
capped equal-context fusion criterion has no ports in the fixed source.
Those are precise restrictions on attempted alternatives, not a proof
that unrestricted exact equality is impossible.

General PBBS fundamental periods have prior literature, including
[Yoshihara, Yura and Tokihiro](https://arxiv.org/abs/nlin/0208042).
The present audit verifies the formula in the stated invariant-gap
coordinates and its construction-length consequences; it makes no
priority claim for general PBBS period theory.

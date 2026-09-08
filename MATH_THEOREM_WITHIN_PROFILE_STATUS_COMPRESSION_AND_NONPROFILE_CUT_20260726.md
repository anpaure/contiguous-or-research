# Within-profile Hall: exact status compression and a genuine non-profile cut

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

Fix an ordered half-rank profile in the independent rank-matching model.
For one fixed allocation, raw Hall cuts can be characterized exactly,
but they do not compress to the half-rank profile.

In one macroblock, identify the relevant rank matching with the identity
between \(A=[d]\) and \(C=[d]\).  A target with half-ranks

\[
                         |T\cap A|=a,\qquad |T\cap C|=c
\]

has a further matching-overlap coordinate

\[
 f=|\{i:a_i,c_i\in T\}|.
\]

Put

\[
 p=a-f,\qquad s=c-f,\qquad e=d-a-c+f.                 \tag{0.1}
\]

These are the numbers of full, \(A\)-only, \(C\)-only, and empty
matching edges, in the order \(f,p,s,e\).

For the one-addition graph, allowing the added endpoint to lie in either
half, define

\[
 \boxed{
 R_{a,c}(f)
 =e\left({1\over p+1}+{1\over s+1}\right).}           \tag{0.2}
\]

If \({\cal F}\) is an arbitrary target subfamily inside the ordered
profile and \({\cal F}_f\) is its overlap-\(f\) part, then

\[
 \boxed{
 |N({\cal F})|
 \ge\sum_f R_{a,c}(f)|{\cal F}_f|.}                   \tag{0.3}
\]

Equality holds when every nonempty \({\cal F}_f\) is the whole
overlap-\(f\) stratum.  Therefore, among unions of complete strata of a
prescribed total size, the minimum neighborhood is obtained by the
usual bathtub ordering in \(R_{a,c}(f)\).  For an arbitrary partial
boundary stratum, (0.3) remains an exact lower bound but need not be
attained.

For a fixed collision-free allocation using one axis in each of \(q\)
specified blocks, the exact tensor form is

\[
 \boxed{
 |N({\cal F})|
 \ge\sum_{\mathbf f}
 \left(\prod_{j=1}^qR_{a_j,c_j}(f_j)\right)
 |{\cal F}_{\mathbf f}|.}                             \tag{0.4}
\]

Thus unions of complete overlap strata are ordered by the global score

\[
                         \sum_{j=1}^q\log R_{a_j,c_j}(f_j).    \tag{0.5}
\]

and the corresponding lower envelope is attained at cumulative stratum
sizes.  These cuts use a growing collection of matching-overlap coordinates.  No
compression to a bounded collection of local half-rank coordinates is
valid.

There is an exact non-profile Hall cut already at \(d=2\),
\(a=c=1\): the two targets which choose opposite endpoints of the
matching have \(f=e=0\), hence no source neighbor, while the whole
half-rank profile has four targets.  Randomizing the matching merely
rotates this two-element cut.

At logarithmic macroblock size this exact local obstruction is sparse.
For the central ordered profile \(a=c=d/2\), a local overlap stratum is
Hall-deficient precisely when

\[
                         f<{d+2\over6}.                \tag{0.6}
\]

For a uniform target in that profile,

\[
 \boxed{
 \Pr\left(f<{d+2\over6}\right)
 =\exp\left[-I_*d+O(\log d)\right],
 \qquad
 I_*={5\over3}\log2-\log3.}                           \tag{0.7}
\]

If \(d=C\log_2m\), this probability is

\[
                         m^{-\beta+o(1)},\qquad
 \beta={CI_*\over\log2}.                              \tag{0.8}
\]

For \(q=A\sqrt m\), if

\[
 C>{\log2\over2I_*}=6.12\ldots,                       \tag{0.9}
\]

a typical ordered-profile target has \(o(q)\) locally deficient blocks,
and the fraction having at least \(q\) such blocks is

\[
 \exp[-\Omega(\sqrt m\log m)].                        \tag{0.10}
\]

In particular the displayed choice \(d=10\log_2m\) passes this local
Gaussian quarantine test.  Having \(q\) deficient blocks can support a
bad fixed allocation using those blocks; it is not an obstruction to the
full allocation union, which may choose different blocks.

This does not prove the full allocation-overlap Hall theorem.  Different
allocations use different independent rank matchings, so their overlap
coordinates \(f_j\) are incompatible and there is no common shifting
order.  Formulae (0.3)--(0.5) disprove an exact reduction to the proved
half-profile flow; (0.7)--(0.10) show why the sharp non-profile cuts may
nevertheless be negligible for an approximate Gaussian injection.

## 1. The local overlap decomposition

Fix a perfect matching \(M\) between \(A\) and \(C\).  Relabeling the
\(C\)-coordinates makes \(M\) the identity matching
\(\{a_ic_i:i\in[d]\}\).

Every target of half-ranks \((a,c)\) has a unique four-status count

\[
 (f,p,s,e)=(f,a-f,c-f,d-a-c+f).                      \tag{1.1}
\]

The number of targets in this overlap stratum is

\[
 \boxed{
 T_{a,c}(f)
 ={d!\over f!\,p!\,s!\,e!}.}                         \tag{1.2}
\]

Adding an \(A\)-endpoint must convert an empty edge into an
\(A\)-only edge.  The resulting source has status counts

\[
                         (f,p+1,s,e-1).
\]

The complete source stratum has size

\[
 S_A(f)
 ={d!\over f!\,(p+1)!\,s!\,(e-1)!},
\]

and therefore

\[
                         {S_A(f)\over T_{a,c}(f)}
 ={e\over p+1}.                                       \tag{1.3}
\]

Similarly, adding a \(C\)-endpoint gives a disjoint source half-profile
with ratio

\[
                         {S_C(f)\over T_{a,c}(f)}
 ={e\over s+1}.                                       \tag{1.4}
\]

Equations (1.3)--(1.4) sum to (0.2).

## 2. Biregularity proves exact compression

Fix \(f\).  In the \(A\)-addition graph, every target has degree \(e\):
choose its empty matching edge.  Every source has reverse degree \(p+1\):
choose which \(A\)-only edge was added.  Thus this graph is biregular.
For an arbitrary \({\cal F}_f\),

\[
 e|{\cal F}_f|
 =e({\cal F}_f,N_A({\cal F}_f))
 \le(p+1)|N_A({\cal F}_f)|,
\]

so

\[
 |N_A({\cal F}_f)|
 \ge{e\over p+1}|{\cal F}_f|.                         \tag{2.1}
\]

The identical argument on the \(C\)-side gives

\[
 |N_C({\cal F}_f)|
 \ge{e\over s+1}|{\cal F}_f|.                         \tag{2.2}
\]

The two source half-profiles are disjoint, and different \(f\)'s remain
different matching-status strata after one addition.  Summing
(2.1)--(2.2) proves (0.3).

If \({\cal F}_f\) is the complete stratum, its neighborhood is the
complete source stratum on each side, so equality holds.  The standard
bathtub argument now characterizes unions of complete strata: moving
one whole target stratum from a larger-\(R\) value to an available
smaller-\(R\) value cannot increase its neighborhood.  No assertion of
equality is made for an arbitrary partial stratum.

This is a genuine combinatorial compression theorem.  Its coordinates
are the matching overlaps \(f\), not the half ranks \((a,c)\).

## 3. Tensor form for a fixed allocation

Take \(q\) specified macroblocks and require one addition in each.  Fix
the target half-ranks \((a_j,c_j)\) in those blocks.  For an orientation
word \(\sigma\in\{A,C\}^q\), the compatibility graph is the tensor
product of the corresponding local \(A\)- or \(C\)-addition graphs.

For a fixed overlap vector
\(\mathbf f=(f_1,\ldots,f_q)\), different orientation words have
disjoint ordered source half-profiles.  Applying biregularity to every
tensor product and summing over \(\sigma\) gives

\[
\begin{aligned}
 { |N({\cal F}_{\mathbf f})|\over
    |{\cal F}_{\mathbf f}|}
 &\ge
 \sum_{\sigma\in\{A,C\}^q}
 \prod_{j=1}^q
 \begin{cases}
 e_j/(p_j+1),&\sigma_j=A,\\
 e_j/(s_j+1),&\sigma_j=C
 \end{cases}\\
 &=\prod_{j=1}^q
 e_j\left({1\over p_j+1}+{1\over s_j+1}\right).
\end{aligned}                                         \tag{3.1}
\]

Different overlap vectors have disjoint source status vectors.
Summing (3.1) proves (0.4).  Complete overlap-vector strata attain
equality, so the same bathtub argument orders complete strata by the
score (0.5).

The score uses all \(q\) selected blocks.  It is not measurable with
respect to any bounded collection of half-rank coordinates.

## 4. Smallest exact counterexample

Let \(d=2\), \(a=c=1\), and use the identity matching.  The four targets
are

\[
 \{a_1,c_1\},\quad\{a_2,c_2\},\quad
 \{a_1,c_2\},\quad\{a_2,c_1\}.
\]

The last two have \(f=0\).  Since \(a+c=d\), equation (0.1) gives
\(e=f=0\).  Neither can be extended by an exposed matching endpoint.
Their neighborhood is empty.

This two-target family is invisible to the ordered half-rank profile,
which contains all four targets.  Under the crossed matching, the first
two rather than the last two are isolated.  Hence two independent rank
matchings have incompatible compression orders already in the smallest
case.

This proves that no deterministic half-rank shifting theorem can replace
all raw Hall cuts by profile cuts.

## 5. Central local deficit threshold

Assume \(d\) is even and \(a=c=d/2\).  Then

\[
                         p=s={d\over2}-f,\qquad e=f,
\]

so (0.2) becomes

\[
                         R(f)={2f\over d/2-f+1}.       \tag{5.1}
\]

Therefore \(R(f)<1\) exactly when

\[
                         3f<d/2+1,
\]

which is (0.6).

For a uniform target in the ordered half profile, \(f\) is
hypergeometric:

\[
 \Pr(f=h)
 ={\binom{d/2}{h}\binom{d/2}{d/2-h}
   \over\binom d{d/2}}
 ={\binom{d/2}{h}^2\over\binom d{d/2}}.               \tag{5.2}
\]

Equivalently, using (1.2),

\[
 \Pr(f=h)
 ={d!\over h!^2(d/2-h)!^2}
 \bigg/\binom d{d/2}^2.
\]

The summands increase up to the mean \(d/4\), so the lower tail in
(0.6) is exponentially governed by \(h=d/6+O(1)\).  Stirling's formula
gives

\[
\begin{aligned}
 -{1\over d}\log\Pr(f\le d/6+O(1))
 &=
 2\log2+{1\over3}\log{1\over6}
          +{2\over3}\log{1\over3}+o(1)\\
 &={5\over3}\log2-\log3+o(1).
\end{aligned}                                         \tag{5.3}
\]

This proves (0.7).

There is also a useful typical-score asymptotic.  Write
\(f=d/4+X\).  The hypergeometric law (5.2) has

\[
 {\mathbb E}X=0,\qquad
 \operatorname {Var}X={d^2\over16(d-1)}.
\]

Taylor expansion of (5.1) gives

\[
 \log R(f)
 =\log2+{8X-4\over d}
   +O\left({X^2+1\over d^2}\right).                  \tag{5.4}
\]

For \(q\) independent central blocks,

\[
 \boxed{
 \sum_{j=1}^q\log R(f_j)
 =q\log2-O(q/d)+O_{\mathbb P}\left(\sqrt{q/d}\right).} \tag{5.5}
\]

At \(q=A\sqrt m\), \(d=\Theta(\log m)\), the leading term is
\(q\log2\).  Thus a typical ordered half-profile overlap vector has
enormous expansion for the orientation-unrestricted fixed allocation.
The Hall-deficient cuts come from genuine lower large deviations, not
from the central Gaussian fluctuations.

## 6. Gaussian number of locally deficient blocks

Let \(d=C\log_2m\) and
\(b=m/d+O(1)\).  Inside the central ordered product profile, the overlap
variables of different blocks are independent.  By (0.7), the number
\(B_{\rm bad}\) of locally deficient blocks is binomial with mean

\[
 {\mathbb E}B_{\rm bad}
 ={m^{1-\beta+o(1)}\over d},
 \qquad
 \beta={CI_*\over\log2}.                              \tag{6.1}
\]

If \(\beta>1/2\), this is \(o(\sqrt m/d)\) and in particular \(o(q)\)
for \(q=A\sqrt m\).  The condition \(\beta>1/2\) is exactly (0.9).

A binomial tail estimate gives

\[
\begin{aligned}
 \Pr(B_{\rm bad}\ge q)
 &\le\left({e\,{\mathbb E}B_{\rm bad}\over q}\right)^q\\
 &=\exp[-(\beta-1/2+o(1))q\log m],
\end{aligned}                                         \tag{6.2}
\]

which proves (0.10).

Thus the sharp one-block non-profile Hall cuts exist in every
realization, but a target containing enough such blocks to form a
\(\Theta(\sqrt m)\)-block all-deficient fixed allocation has
exponentially small density when (0.9) holds.

This is a quarantine estimate, not a matching theorem.  Moderate
overlap deficits, multiple additions in one block, and competition
between different target subsets remain.  Most importantly, the full
allocation union can avoid the deficient blocks, so (6.2) is not a raw
Hall obstruction for that union.

## 7. Why independent rank matchings prevent common shifting

For one matching, Section 2 gives a canonical overlap compression.
For another matching on the same block, the overlap coordinate is

\[
 f_{\pi}(T)
 =|\{a_i\in T:\pi(a_i)\in T\}|.
\]

If two matchings differ, their low-\(f\) strata generally cross rather
than nest.  The \(d=2\) example makes them complementary.  For random
independent matchings, the relative permutation has nontrivial cycles
with probability tending to one, producing the same incompatibility on
its cycle supports.

Hence there is no coordinate order under which all allocation shadows
are simultaneously monotone.  Compressing for one rank matching can
increase the shadow in another rank matching.

The full maximal graph is a union over allocation vectors, and every
allocation uses its own collection of rank matchings.  Its minimum cut
could be repaired by this union, but it cannot be proved so by a
single-matching shifting argument.

## 8. Exact boundary

Proved:

1. arbitrary within-profile target families satisfy the exact
   overlap-compressed inequality (0.3);
2. fixed collision-free allocations satisfy the tensor inequality
   (0.4);
3. minimum cuts for those graphs are global score thresholds, not
   half-profile cylinders;
4. a genuine non-profile Hall cut exists already at \(d=2\);
5. different rank matchings have incompatible compression orders; and
6. locally Hall-deficient central block states obey the exact Gaussian
   quarantine asymptotics (0.7)--(0.10).

Not proved:

1. that every low-neighborhood family in the union over all allocations
   is negligible;
2. a compression theorem for that union;
3. the random-rank maximal raw injection; or
4. packet and chronology grouping.

The proposed reduction of all raw Hall cuts to the already proved
half-profile flow is therefore false exactly.  A viable approximate
replacement would have to combine the quarantine estimate with a robust
multi-allocation expansion theorem.

## 9. Subsequent noncomposition audit

`MATH_THEOREM_OVERLAP_COMPRESSION_CROSS_PROFILE_AND_PACKET_UNION_CUT_20260726.md`
shows that even the stronger all-subsets estimate

\[
                         |N(\mathcal A)|\ge K|\mathcal A|
\]

inside every ordered profile, for arbitrarily large \(K\), does not
compose formally with capacitated profile Hall.  An explicit graph with
empty quarantine satisfies both inputs but has a mixed-profile raw Hall
ratio exactly \(1/2\).  The required new statement is therefore an
arc-resolved cross-profile overlap bound (or an equivalent
source-normalized flow), not merely a sharper estimate on the deficient
overlap tail.  In the authoritative CPCR synthesis this is precisely the
first remaining global item, weighted allocation of shared source-profile
capacity.  It does not reopen the diverse-order compiler's within-packet
injectivity or any common-order syndrome gate.

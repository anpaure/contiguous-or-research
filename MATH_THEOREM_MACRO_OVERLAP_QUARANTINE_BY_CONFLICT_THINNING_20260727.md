# Macro-overlap quarantine by conflict thinning

> **Correction (2026-07-27).**  The later (n^{s/3}) zipper estimate
> cited in (1.6) is false.  A synchronized two-front re-pairing family
> forces list exponent at least (1/2).  Consequently (4.5) and the
> sentence claiming that the macroscopic survivor comparison is closed
> are retracted.  See
> `MATH_AUDIT_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`.

Date: 2026-07-27

> **Correction (2026-07-27).**  The later assertions in this note that
> cite an \(n^{s/3}\) paired-window zipper estimate are retracted.  The
> zipper's two-target-anchor row is false, and a globally aligned
> double-segment family attains exponent \(1/2-o(1)\).  See
> `MATH_COUNTERAUDIT_DOMINO_ZIPPER_TWO_POINT_ANCHOR_20260727.md` and
> `MATH_AUDIT_DOMINO_DOUBLE_SEGMENT_HALF_EXPONENT_AND_COLLAR_OVERLAP_20260727.md`.
> The earlier proved \(\exp(Cn)n^{3s}\) conflict bound and the conditional
> thinning calculations remain separate; equations (1.6), (4.5), and the
> claim that the sharp inverse-stability comparison is closed do not.

> **Audit correction.**  The sharpened estimate (0.1') and every
> conclusion depending on it are retracted.  The paired-window release
> record is not injective, and a globally aligned two-segment family
> contradicts every uniform exponent below \(1/2\).  See
> MATH_AUDIT_PAIRED_WINDOW_ZIPPER_PHASE_RELEASE_INVERSE_FAILURE_20260727.md.
> The unsharpened trace bound (0.1) is not affected.

## 0. Outcome

Let \(\mathcal H^\square\) be the **simple** domino-twin packet
catalogue on the \(R\)-sets of \([n]\), where

\[
 n=2m,\qquad K=2n=4m,
\]

and let \(D\) be its entrance degree.  Thus

\[
 \log D=2m\log m-O(m).
\]

For an integer \(s\), form the conflict graph \(\Gamma_s\) on packets by
joining distinct packets \(F,G\) when

\[
 |F\cap G|>K-s.
\]

The following gives a literal macroscopic-overlap quarantine.

> **Theorem.**  Uniformly for \(1\le s<n/2\),
> \[
>  \Delta(\Gamma_s)\le \exp(Cn)\,n^{3s}.                 \tag{0.1}
> \]
> In the inverse-stability range \(s=o(m)\), the paired-window zipper
> sharpens this to
> \[
>  \boxed{\Delta(\Gamma_s)\le \exp(Cm)n^{s/3}.}          \tag{0.1'}
> \]
> There is an independent subcatalogue \(\mathcal H_s\subseteq
> \mathcal H^\square\) such that, simultaneously for every entrance
> target \(X\) and every pair \(X,Y\),
> \[
>  d_s(X)=(1+o(1))D_s,
>  \qquad
>  d_s(X,Y)\le(1+o(1))\frac{d^\square(X,Y)}{\Delta_s+1}, \tag{0.2}
> \]
> where \(\Delta_s=\Delta(\Gamma_s)\) and
> \[
>  D_s=\frac{D}{\Delta_s+1}.                             \tag{0.3}
> \]
> In particular,
> \[
>  \frac{\Delta_2(\mathcal H_s)}{D_s}
>  \le\frac{5+o(1)}{R(n-R)}=O(m^{-2}),                  \tag{0.4}
> \]
> and no two retained packets have overlap greater than \(K-s\).

Moreover the uniform edge weight \(1/\Delta(\mathcal H_s)\) is a
fractional matching of total weight

\[
 (1-o(1))\frac{N_R}{K},                                  \tag{0.4a}
\]

so the thinning loses no asymptotic **fractional** factor capacity.
An integral near-factor still requires a growing-uniformity matching
argument; (0.4a) is not being advertised as such an argument.

Consequently, whenever \(s=o(m)\),

\[
 \log D_s=2m\log m-O(m+s\log m)
          =(2-o(1))m\log m.                             \tag{0.5}
\]

Thus the macro-overlap quarantine requested by the stopped factorial
audit is compatible with factorial entrance degree and the original
relative pair-codegree scale.  The crude trace estimate (0.1) loses
\(3s\log m\), but the inverse estimate (0.1') loses only
\((s/3)\log m\).  At \(z=m^{-1/2}\), Section 4 therefore closes the
macroscopic survivor comparison at \(s=A m/\log m\).  The remaining
stopped issue is hereditary propagation below that quarantine scale.

## 1. A trace-counting lemma

Write \(E_R(P)\) for the \(n\) cyclic \(R\)-intervals of a cyclic order
\(P\).  Fix a twin packet \(F\), regarded as a set of \(K=2n\)
vertices of the Johnson graph \(J(n,R)\).

### Lemma 1.1

The graph induced by \(F\) in \(J(n,R)\) has maximum degree at most
five.

#### Proof

The radius-one case of the twin-packet ball lemma says that a Johnson
ball of radius one contains at most \(4\cdot1+2=6\) members of \(F\),
including its centre.  Hence there are at most five neighbours. \(\square\)

### Lemma 1.2

The number of cyclic orders \(P\), modulo rotation and reversal, for
which

\[
 |E_R(P)\setminus F|\le s
\]

is at most

\[
 \exp(Cn)n^{3s}.                                        \tag{1.1}
\]

#### Proof

Expose the cyclic trace

\[
 (I_0,I_1,\ldots,I_{n-1}),\qquad I_i\in\binom{[n]}R,
\]

of \(P\).  Consecutive trace vertices are adjacent in \(J(n,R)\).
Mark the at most \(s\) positions whose trace vertex is outside \(F\).
There are at most \(2^n\) choices for the marked set.

The unmarked positions form cyclic runs.  There are at most \(s\) runs.
For the first vertex of every run there are at most \(K\le2n\) choices;
thereafter Lemma 1.1 gives at most five choices per unmarked step.
At a marked step, the Johnson graph has degree

\[
 R(n-R)\le n^2,
\]

so there are at most \(n^2\) choices.  Therefore the number of exposed
traces is at most

\[
 2^n K^s5^n(n^2)^s\le \exp(Cn)n^{3s}.                  \tag{1.2}
\]

Finally, the family of all proper nontrivial cyclic intervals of a cyclic
order determines that order up to reversal; in particular its
length-\(R\) trace does so in the present regime \(2\le R\le n-2\).
Equivalently, the Johnson-distance-one graph induced on the trace is its
cyclic adjacency graph, and successive set differences recover the
cyclic labels.  Thus (1.2) also bounds cyclic orders modulo rotation and
reversal. \(\square\)

### Lemma 1.3 (conflict degree)

\[
 \Delta(\Gamma_s)\le \exp(Cn)n^{3s}.
\]

#### Proof

Fix \(F\), and let \(G=E_R(P)\,\dot\cup\,E_R(P^\tau)\) conflict with
\(F\).  Since both component traces of \(G\) have size \(n\),

\[
 |G\cap F|>2n-s
\]

forces each component, and in particular \(E_R(P)\), to have at least
\(n-s\) members in \(F\).  Apply Lemma 1.2.  Passing from labelled
orders to simple supports can only reduce the count. \(\square\)

### Lemma 1.4 (inverse reduction to paired-cycle cells)

Write \(R=2r+1\).  A simple twin packet is encoded by a cyclic order of
\(m\) unordered dominoes \(B_i\), and its support is the disjoint union
of the \(m\) four-sets

\[
 \mathcal S_i
 =\{A_i\cup\{x\}:x\in B_{i-1}\cup B_{i+r}\},
 \qquad
 A_i=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1}.           \tag{1.3}
\]

If two simple twin packets \(F,G\) satisfy \(|F\cap G|\ge K-s\), then
at least \(m-s\) of the cells \(\mathcal S_i\) of \(F\) occur **as the
same complete cell** of \(G\).

#### Proof

Formula (1.3) is obtained by starting the ordinary and \(\tau\)-shifted
length-\(2r+1\) windows at the two parities: a target consists of \(r\)
consecutive complete dominoes and one of the four elements in the two
adjacent boundary dominoes.  The cells are disjoint and exhaust the
\(4m=K\) targets.

Every \(\mathcal S_i\) is a star \(K_4\) in \(J(n,R)\), with common
\((R-1)\)-core \(A_i\) and union of size \(R+3\).  If all four of its
vertices lie in \(G\), they form a \(K_4\) in the Johnson graph induced
by \(G\).  The exact clique classification for a twin packet says that
every such \(K_4\) is either a canonical star \(K_4\) or a canonical top
\(K_4\).  It cannot be a top \(K_4\), whose union has size at most
\(R+1\).  Hence it is a star cell of \(G\), and its intersection and
union recover the same \(A_i\) and the same boundary four-set.

At most \(s\) cells of the partition of \(F\) can contain a vertex of
\(F\setminus G\).  Every other cell is complete in \(G\), proving the
claim. \(\square\)

Lemma 1.4 isolates the sharper inverse theorem still missing from the
survivor comparison: count paired cyclic orders sharing \(m-s\) of the
literal radius-\(r\) cells (1.3).  It removes arbitrary Johnson paths
from the problem.  A bound

\[
 \#\{G:|F\cap G|\ge K-s\}
 \le \exp(O(m))n^{cs},\qquad c<1/2,                     \tag{1.4}
\]

would be sufficient at \(z=m^{-1/2}\).  The natural disjoint local
two-switch family in Section 5 has exponent \(1/8\), so no known local
construction contradicts (1.4).

There is a further literal rigidity statement.  If two consecutive cells
\(\mathcal S_i,\mathcal S_{i+1}\) are common, their cores recover

\[
 B_i=A_i\setminus A_{i+1},\qquad
 B_{i+r}=A_{i+1}\setminus A_i,
\]

and the boundary four-set of \(\mathcal S_i\) then recovers
\(B_{i-1}\).  Moreover consecutive cells are intrinsically recognizable:
their cores have symmetric difference four, whereas cells at cyclic
distance \(d\) have core symmetric difference \(4d\) for
\(d<\min(r,m-r)\).  Hence the common cells split into at most \(s\)
orientation-consistent runs, and all but \(O(s)\) dominoes are literally
fixed after aligning those runs.  This proves a coarse paired-cycle
stability count \(\exp(O(m+s\log m))\) independently of arbitrary
Johnson-path filling.  At this stage of the argument the sharp entropy
coefficient below \(1/2\) in (1.4) was the remaining issue.

The missing sharp entropy coefficient is supplied by the paired-window
zipper theorem in
`MATH_THEOREM_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`:

\[
 \#\{G:|F\cap G|\ge K-s\}
 \le \exp(Cm)n^{s/3}\qquad(s=o(m)).                     \tag{1.6}
\]

Its essential point is that a cell with two common targets is an anchor,
including in the star-to-top realization, while a cell which releases a
letter has at most one common target and therefore spends at least three
units of defect.  The two paired radius-\(r\) fronts are decoded
together, so an empty cell releases one letter rather than an independent
domino.  Thus (1.4) now holds with \(c=1/3\).

### Lemma 1.5 (one global dihedral alignment)

Assume \(s=o(m)\).  After one rotation or reflection of the cell index
of \(G\), every complete common cell supplied by Lemma 1.4 has the same
index in \(F\) and \(G\).  In particular the common-cell runs cannot be
permuted or independently reversed.

#### Proof

For cell cores in either packet,

\[
 |A_i\cap A_j|=2(r-d)
 \quad\text{when }d=\operatorname{dist}_{C_m}(i,j)\le r, \tag{1.5}
\]

and the intersection is empty for \(r<d\le m-r\).  Thus equality of
common cores preserves every cyclic distance at most \(r\).

Delete the at most \(s\) non-common cell indices.  Start with any two
consecutive common indices (they exist for \(s<m/3\)); their images fix a
rotation/reflection and an orientation.  Traverse the remaining common
indices cyclically.  Across a deleted gap of length \(h\le s\), the next
common index is at distance \(h+1<r\) from the preceding common index.
Its distances to that index and to the preceding already-aligned common
index distinguish the forward continuation from the reflected one.  If
one of the adjacent common runs has length one, use the nearest two
already-aligned common indices; their distances to the new point are at
most \(2s+2<r\).  Hence induction across every deleted gap forces the
same orientation and offset. \(\square\)

Lemma 1.5 removes the apparent \(s!\) entropy from permuting common runs.
All remaining entropy lies in repartitioning the labels at the
\(O(s)\) block positions not recovered by consecutive common cells.

## 2. Nearly regular independent thinning

The action of \(S_n\) is transitive on simple twin packets and preserves
intersection size.  Hence \(\Gamma_s\) is regular, of degree
\(\Delta_s\).

Give every packet an independent continuous priority and retain it iff
its priority is the unique minimum in its closed \(\Gamma_s\)-neighbourhood.
The retained packets form an independent set, and every packet is retained
with probability

\[
 p_s=\frac1{\Delta_s+1}.                                \tag{2.1}
\]

For a target \(X\), write

\[
 Y_X=\sum_{F\ni X}{\bf1}_{\{F\text{ retained}\}}.
\]

Then \(\mathbb EY_X=Dp_s=D_s\).  Two retention indicators are
independent whenever their vertices have conflict-graph distance greater
than two.  Thus the indicators in a fixed entrance link have a dependency
graph of maximum degree at most \((\Delta_s+1)^2\).

A standard dependency-graph Hoeffding bound (obtainable directly by
properly colouring the dependency graph and applying Hoeffding in each
colour class) gives, for every fixed \(\eta>0\),

\[
 \Pr\bigl(|Y_X-D_s|>\eta D_s\bigr)
 \le 2\exp\left[-c\eta^2\frac{D}{(\Delta_s+1)^4}\right]. \tag{2.2}
\]

For \(s=o(m)\), (0.1) and \(\log D=2m\log m-O(m)\) make the exponent in
(2.2) \(\exp((2-o(1))m\log m)\).  This dominates the number
\(\binom nR=\exp(O(m))\) of targets, so a union bound makes all target
degrees simultaneous.

Apply the same argument to

\[
 Y_{X,Y}=\sum_{F\supseteq\{X,Y\}}{f1}_{\{F\text{ retained}\}}.
\]

Its expectation is \(p_sd^\square(X,Y)\).  The largest such expectation
is still factorially large, and an additive error \(o(D_s/m^2)\) is
simultaneously valid over all pairs.  The exact twin pair-codegree table
then gives (0.2)--(0.4).

Taking any priority realization for which these simultaneous conclusions
hold defines \(\mathcal H_s\).

If \(\Delta_s^{\rm hyp}=\max_Xd_s(X)\), assign every retained packet
weight \(1/\Delta_s^{\rm hyp}\).  This is a feasible fractional matching,
and double counting incidences gives

\[
 \sum_F\frac1{\Delta_s^{\rm hyp}}
 =\frac{\sum_Xd_s(X)}{K\Delta_s^{\rm hyp}}
 =(1-o(1))\frac{N_R}{K},
\]

proving (0.4a).

There is also a small but useful symmetry obstruction.  Since \(S_n\)
acts transitively on simple twin packets, an exactly \(S_n\)-invariant
subcatalogue is either empty or the full catalogue.  The full catalogue
contains the near-parallel pairs of Lemma 4.1.  Thus no nontrivial exact
transitive quarantine exists; simultaneous near-regularity is the
strongest symmetry conclusion one can ask from a proper thinning without
changing the group or replacing packets by clusters.

## 3. Degree retained

Combining the original simple-degree estimate with (0.1),

\[
 \log D_s
 \ge 2m\log m-O(m)-Cn-3s\log n,
\]

which proves (0.5).  For example, either of

\[
 s=\frac{m}{\log m},
 \qquad
 s=\frac{m}{\sqrt{\log m}}
\]

removes every pair of overlap \(K-o(m)\) while retaining degree
\(\exp((2-o(1))m\log m)\).

In the range \(s=o(m)\), (0.1') gives the sharper retained-degree
estimate
\[
 \log D_s\ge
 2m\log m-O(m)-\frac{s}{3}\log n.                       \tag{3.1}
\]

## 4. Exact comparison with the survivor tilt

At \(z=m^{-1/2}\), one pair of residual overlap \(r=K-s\) carries
amplification

\[
 z^{-r}=\exp\left[(2m-s/2)\log m\right].                \tag{4.1}
\]

After thinning, the reciprocal-degree normalization satisfies only

\[
 \log D_s^{-1}
 =-2m\log m+O(m+s\log m).                               \tag{4.2}
\]

Therefore the present theorem gives the literal comparison

\[
 \log\frac{z^{-(K-s)}}{D_s}
 \le -\frac{s}{2}\log m+O(m+s\log m).                  \tag{4.3}
\]

Using the explicit trace enumeration in (0.1), the displayed upper bound
is

\[
 \frac52s\log m+O(m),                                   \tag{4.4}
\]

not a negative quantity.  Thus this conflict thinning rigorously removes
the near-parallel class from Lemma 4.1 and preserves all local matching
parameters, but its proved entropy cost does not itself establish the
stopped survivor kernel.  Closing that last comparison requires either

1. a stability count improving \(n^{3s}\) to
   \(\exp(O(m))n^{cs}\) with \(c<1/2\); or
2. a multiscale conflict thinning whose cost is charged once across all
   overlap scales rather than independently at the terminal scale.

The paired-window zipper estimate (1.6) improves the right side of
(4.3) to

\[
 -\frac{s}{6}\log m+O(m),                              \tag{4.5}
\]

which is negative at \(s=A m/\log m\) for a sufficiently large fixed
\(A\).  Hence the macroscopic inverse-stability comparison is closed.
The remaining stopped issue is hereditary propagation of the static
factorial-overlap estimates below the quarantine scale.

## 5. Calibration: a necessary exponential loss, but not a factorial one

The conflict degree is genuinely large.  Choose \(j\) pairwise
nonadjacent cross-domino boundaries of a fixed packet and perform all the
corresponding cross-boundary swaps.  Each single swap changes at most
eight packet targets, so the resulting packet has overlap at least
\(K-8j\) with the original.  The supports are distinct because their
recovered domino partitions are distinct.  Restricting, for example, to
one boundary in every three gives

\[
 \boxed{
 \Delta(\Gamma_s)
 \ge \binom{\lfloor m/3\rfloor}{\lfloor(s-1)/8\rfloor}}
 \qquad(8\le s\le m).                                   \tag{5.1}
\]

Thus every proper conflict colouring sometimes needs exponentially many
colours.  At the important scale \(s=\Theta(m/\log m)\), however, the
logarithm of (5.1) is only

\[
 O\left(\frac m{\log m}\log\log m\right)=o(m),
\]

far below both the factorial degree and the survivor saving
\((s/2)\log m=\Theta(m)\).  Therefore (5.1) does not obstruct the desired
stopped theorem.  Instead it shows that the crude upper exponent
\(3s\log m\) is potentially very far from sharp.  A block-cycle stability
theorem giving \(\log\Delta(\Gamma_s)=O(m+s\log(m/s))\) would make (4.3)
negative for a sufficiently large constant multiple
\(s=m/\log m\), and would close the macroscopic survivor comparison.

There is a stronger calibration which identifies the best possible power
of \(n\).

### Lemma 5.1 (contiguous-segment lower bound)

For \(1\ll \ell<\min(r,m-r)-2\),

\[
 \boxed{
 \Delta(\Gamma_{8\ell+9})
 \ge \frac{(2\ell)!}{2^\ell(2m)}.}                       \tag{5.2}
\]

Consequently no inverse estimate of the form (1.4) can hold with
\(c<1/4\), up to lower-order terms.

#### Proof

Fix one interval of \(\ell\) consecutive domino positions.  Keep every
outside domino fixed, but repartition the \(2\ell\) labels inside the
interval arbitrarily into an **ordered** list of \(\ell\) unordered
dominoes.  This gives \((2\ell)!/2^\ell\) paired cyclic orders.  At most
the dihedral group of size \(2m\) can identify two of the resulting
simple supports, because a support recovers its domino partition and
cyclic block order.

A cell from (1.3) is unchanged whenever its radius-\(r\) core contains
the entire modified segment, or whenever its core and its two boundary
positions avoid the segment.  The only possibly changed cell starts are
those for which the core cuts one of the two segment boundaries, together
with the two starts having a boundary domino in the segment and a
disjoint core.  There are at most \(2\ell+2\) such cells.  Since a cell
has four packet targets, every resulting support shares at least

\[
 K-4(2\ell+2)=K-8\ell-8
\]

targets with the original packet, and hence is adjacent in
\(\Gamma_{8\ell+9}\).  This proves (5.2).

Finally,

\[
 \log\frac{(2\ell)!}{2^\ell(2m)}
 =(2+o(1))\ell\log\ell
 =\left(\frac14+o(1)\right)(8\ell)\log(8\ell),
\]

which forces \(c\ge1/4\) when \(\ell\) is polynomially comparable to
\(n\). \(\square\)

Thus the sharp inverse target is the narrow interval

\[
 \boxed{\frac14\le c<\frac12.}                           \tag{5.3}
\]

The lower endpoint is realized by arbitrary re-pairing inside one local
block segment; the upper endpoint is exactly the survivor threshold at
\(z=m^{-1/2}\).

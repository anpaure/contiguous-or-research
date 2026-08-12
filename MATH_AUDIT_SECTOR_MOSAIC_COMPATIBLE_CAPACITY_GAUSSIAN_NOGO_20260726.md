# Sector mosaic versus the corrected Gaussian profile capacity

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The sector-selected owner near-tiling in
`MATH_THEOREM_SECTOR_MOSAIC_CROSS_FRAME_PACKET_NEAR_TILING_20260726.md`
does **not** escape the Gaussian Hall deficit proved in
`MATH_THEOREM_Q4_MIXED_FRAME_MOSAIC_POTENTIAL_GAUSSIAN_COVER_20260726.md`.

The reason is profile capacity, not potential reachability.  Fix a lower
target profile

\[
                         \pi=(g,h,u,n_0,n_3,n_4),
\]

where \(g\) is the number of good singleton quartet traces, \(h\) the
number of bad singleton traces, \(u\) the number of two-set traces, and the
remaining entries count local ranks \(0,3,4\).  Every safe depth-\(q\)
window producing this profile has its source in the unique profile

\[
                         \pi^\uparrow
 =(g-q,h,u+q,n_0,n_3,n_4).                         \tag{0.1}
\]

Throughout, \(q\le r\), as in the sector compiler regime
\(H/r\to0\).  If some installed compiler windows are not safe, they supply
no correct rank-\((m-q)\) occurrence and only strengthen the deficit below.

Let \(\gamma_{\rm sec}(\pi^\uparrow)\) be the fraction of owners of this
source profile whose product cell contains at least one cross-frame
two-set cell in every sector.  These, and only these, are retained by the
sector packet tiling.  The exact compatible-source/target profile ratio is

\[
 \boxed{
 R_q^{\rm sec}(\pi)
 =\gamma_{\rm sec}(\pi^\uparrow)
   {2^q\binom gq\over\binom{u+q}q}.}                \tag{0.2}
\]

In particular,

\[
                         R_q^{\rm sec}(\pi)
 \le R_q(g,u):={2^q\binom gq\over\binom{u+q}q}.     \tag{0.3}
\]

Sector selection can only delete compatible sources from the already
deficient fixed-profile fibre.  It cannot import a source from another
profile.

For \(q=\lfloor A\sqrt m\rfloor\) and the central positive-density family
of target profiles,

\[
 R_q(g,u)=e^{-6A^2+o(1)}.                           \tag{0.4}
\]

Moreover the sector hypothesis \(r\log m=o(m)\) gives

\[
                         \gamma_{\rm sec}(\pi^\uparrow)=1-o(1)
\tag{0.5}
\]

uniformly on a sufficiently small central profile box.  Thus the sector
ratio has the same sharp central limit:

\[
 \boxed{R_q^{\rm sec}(\pi)=e^{-6A^2+o(1)}<1.}       \tag{0.6}
\]

Consequently the selected owner tiling has a positive-density lower-target
deficit at every fixed nonzero Gaussian depth.  The rank-reversed upper
profile calculation gives the same upper deficit.  Dyadic direction
dispersion, owner-disjointness, and frame change on every selected axis do
not affect this cut.

Any escape must create a positive-density family of **profile-crossing**
windows: either paths crossing the frozen product-cell/quarter-block atlas,
or an owner-dependent re-atlasing which lets a central target draw capacity
from a source profile other than (0.1).  An \(o(W)\)-owner repair cannot
work.

## 1. The common local atlas

Use the quartet labels \(\{0,1,2,3\}\) and the cells from the sector note:

\[
 C_0=\{01,02\},\qquad
 C_1=\{03,13\},\qquad
 C_2=\{12,23\}.                                    \tag{1.1}
\]

Their lower intersections are respectively

\[
                         0,\qquad3,\qquad2.          \tag{1.2}
\]

Thus the three good lower singleton traces are \(0,2,3\), while \(1\) is
bad.  The cross cells selected by the sector construction are \(C_0,C_2\).
They have four two-set endpoints in total; the reference cell \(C_1\) has
two.

This is a relabelling of the local atlas in the \(Q_4\) capacity theorem.
In particular, both notes use the same immutable quartet partition and the
same partition of the six local two-sets into three physical edges.  The
sector rule changes which active edge is retained; it does not change the
local-rank profile relation between an intersection target and its source.

## 2. The forced source profile and the corrected ratio

Let \(\mathcal A_\pi\) be the family of rank-\((m-q)\) targets with profile
\(\pi\).  The number of such targets is

\[
 |\mathcal A_\pi|
 ={b!\over g!h!u!n_0!n_3!n_4!}
   3^g6^u4^{n_3},                                   \tag{2.1}
\]

where \(b=m/2\).  The rank equation is implicit, and profiles with a
negative entry are empty.

A safe \(q\)-window changes \(q\) distinct local two-set blocks into their
intersection singletons.  Each is good.  All other local traces are
unchanged.  Hence (0.1) is necessary, independently of the order of the
directions, the choice of packet cycle, and the sector locations of the
directions.

Let \(\mathcal S_\pi\) be the full owner family of the forced profile
\(\pi^\uparrow\).  Then

\[
 |\mathcal S_\pi|
 ={b!\over(g-q)!h!(u+q)!n_0!n_3!n_4!}
   3^{g-q}6^{u+q}4^{n_3}.                           \tag{2.2}
\]

Dividing (2.2) by (2.1) gives

\[
\begin{aligned}
 { |\mathcal S_\pi|\over|\mathcal A_\pi|}
 &=2^q{g!\,u!\over(g-q)!(u+q)!}\\
 &={2^q\binom gq\over\binom{u+q}q}
 =R_q(g,u).                                         \tag{2.3}
\end{aligned}
\]

This is the corrected ratio.  The denominator \(\binom{u+q}q\) is the
source-side multiplicity: a source of profile \(\pi^\uparrow\) has
\(u+q\) two-set blocks, any \(q\) of which can be collapsed in the
unrestricted potential catalogue.  Omitting it counts paths rather than
available source owners and is not a Hall calculation.

## 3. Exact sector-retention factor

Let the sector lengths be \(\ell_0,\ldots,\ell_{r-1}\).  A source owner is
retained precisely when every sector contains a local two-set belonging to
\(C_0\) or \(C_2\).  Define the one-block profile inventory

\[
 F=x_0+3x_g+x_h+6x_2+4x_3+x_4,                     \tag{3.1}
\]

and its no-cross version

\[
 F_{\rm nc}=F-4x_2
 =x_0+3x_g+x_h+2x_2+4x_3+x_4.                      \tag{3.2}
\]

For a profile vector \(\rho\), write \([\mathbf x^\rho]\) for the
corresponding coefficient.  The exact retained fraction is

\[
 \boxed{
 \gamma_{\rm sec}(\rho)
 ={[\mathbf x^\rho]
     \displaystyle\prod_{s=0}^{r-1}
       \left(F^{\ell_s}-F_{\rm nc}^{\ell_s}\right)
   \over
   [\mathbf x^\rho]F^b}.}                           \tag{3.3}
\]

Indeed, \(F^{\ell_s}\) inventories all local assignments in a sector and
\(F_{\rm nc}^{\ell_s}\) inventories those having no cross two-set state.
The product enforces the good-cell condition in every sector.

Let

\[
 \mathcal S_\pi^{\rm sec}
 =\mathcal S_\pi\cap
   \{\hbox{sector-good product-cell owners}\}.
\]

The exact owner matching theorem in the sector note retains every member of
this family once and retains no owner outside a sector-good product cell.
Therefore

\[
 |\mathcal S_\pi^{\rm sec}|
 =\gamma_{\rm sec}(\pi^\uparrow)|\mathcal S_\pi|.   \tag{3.4}
\]

Combining (2.3) and (3.4) proves (0.2).

This is the exact ratio of the entire relaxed compatible source reservoir
to the target profile, not a potential-path degree.  Every actual safe
compiler window starting from a source in
\(\mathcal S_\pi^{\rm sec}\) collapses \(q\) selected cross axes and has
target profile \(\pi\).  Conversely, a target in \(\mathcal A_\pi\) cannot
be produced from any other source profile.  Since a source owner supplies
one based depth-\(q\) window, at least

\[
 \boxed{
 \left(1-R_q^{\rm sec}(\pi)\right)_+
 |\mathcal A_\pi|}                                  \tag{3.5}
\]

targets of this profile are missed.

For the upper side, use good triple traces in place of good singleton
traces.  There are again three good local traces, and the two cross cells
again supply two of them.  A compatible source profile is obtained by
changing \(q\) good triples into \(q\) two-set blocks.  The cardinality
division is identical to (2.3), and the source-retention factor is again
(3.3), because sector goodness depends only on which source two-set states
belong to the four cross endpoints.  This is a rank-reversed count.  It
should not be replaced by the stronger false statement that the
cross/reference designation of every owner is preserved by complementation.

More explicitly, for an upper target density

\[
 p_+={m+q\over2m},
\]

the central good-triple and two-set counts are

\[
 g_0^+={m\over2}\,3p_+^3(1-p_+),
 \qquad
 u_0^+={m\over2}\,6p_+^2(1-p_+)^2.                 \tag{3.6}
\]

They obey

\[
 {u_0^+\over2g_0^+}={1-p_+\over p_+}
 =1-{2A\over\sqrt m}+O(m^{-1}),                    \tag{3.7}
\]

which is the same expansion as the lower profile.  Substitution in (2.3)
therefore gives \(\log R_q=-6A^2+o(1)\) on the upper side as well.

## 4. Exact target-side sector compatibility

For completeness, one can also count relaxed compatible sources for an
individual target.  This count explains why abundant reachability does not
contradict (3.5).

Within sector \(s\), locate the first block at which the target trace is a
cross-cell two-set, meaning one of the four endpoints of \(C_0,C_2\).  Let
\(a_s(T)\) be the number of cross-good singleton traces \(0\) or \(2\)
strictly before that block; if there is no cross two-set, count such
singletons in the entire sector.  Let

\[
 Z(T)=\{s:\hbox{sector }s\hbox{ has no cross two-set trace}\}.
\]

### Proposition 4.1 (sector-compatible source degree)

The number of selected-packet source owners from which some return-free
\(q\)-face can have lower intersection \(T\) is exactly

\[
 \boxed{
 D_q^{\rm sec}(T)
 =2^q
   \sum_{\substack{J\subseteq[r],\ |J|=q\\Z(T)\subseteq J}}
   \prod_{s\in J}a_s(T).}                           \tag{4.1}
\]

#### Proof

There is one selected axis in each sector: the first cross symbol of the
source product cell.  If it is toggled, the target trace at that block is
the cross-good singleton \(0\) or \(2\), and the block must precede every
cross two-set already visible in the target.  This gives \(a_s(T)\)
choices.  Its source endpoint has two orientations.

At most one axis per sector can be toggled.  Every sector having no target
cross two-set must be among the toggled sectors, or else the source cell
would have no cross symbol there.  Thus the toggled sector set is exactly a
set \(J\) appearing in (4.1).  Choices in distinct sectors are independent,
and the \(q\) local source orientations give the factor \(2^q\).
Conversely every displayed choice makes the chosen singleton the first
source cross symbol in its sector and therefore defines one compatible
selected packet source.  \(\square\)

Formula (4.1) may be very large.  It counts alternative realizations of a
single target, while (0.2) counts distinct source owners available to a
whole target profile.  Hall capacity is governed by the latter.

## 5. The sector factor is asymptotically one on central profiles

Let \(u'=u+q\) be the number of source two-set blocks.  Conditional on this
number and on all other profile counts, their positions are uniform among
the \(b\) quartet positions.  Each of their six local states is uniform;
four are cross and two are reference.

Fix a sector of length \(\ell\).  If \(C\) is the total number of cross
two-set states, then

\[
                         C\sim\operatorname{Bin}(u',2/3).
\]

Conditional on \(C\), the cross positions form a uniform \(C\)-subset of
the \(b\) blocks.  Therefore

\[
\begin{aligned}
 \Pr(\hbox{this sector has no cross state})
 &=\mathbb E{\binom{b-\ell}{C}\over\binom bC}\\
 &\le\mathbb E(1-\ell/b)^C\\
 &=\left(1-{2\ell\over3b}\right)^{u'}\\
 &\le\exp\left(-{2u'\ell\over3b}\right).
                                                               \tag{5.1}
\end{aligned}
\]

A union bound yields the uniform exact-profile estimate

\[
 \boxed{
 1-\gamma_{\rm sec}(\pi^\uparrow)
 \le r\exp\left(-{2(u+q)\ell_{\min}\over3b}\right).}           \tag{5.2}
\]

For the central Gaussian profiles of the \(Q_4\) theorem,

\[
 {u+q\over b}={3\over8}+o(1).                       \tag{5.3}
\]

The sector construction has \(\ell_{\min}=\lfloor b/r\rfloor\) and
\(r\log m=o(m)\).  Hence \(\ell_{\min}\gg\log m\), and (5.2) gives

\[
                         \gamma_{\rm sec}(\pi^\uparrow)=1-o(1) \tag{5.4}
\]

uniformly throughout a sufficiently small \(O(\sqrt m)\) central box.

Thus the sector leave is negligible even conditionally on the hard
profiles.  This does not help: it means the sector construction retains
almost the entire already-insufficient source fibre.

## 6. Gaussian Hall deficit

Put

\[
                         q=\lfloor A\sqrt m\rfloor,
 \qquad A>0\text{ fixed}.
\]

For the central profile values \(g_0,u_0\), the corrected \(Q_4\) ratio
satisfies

\[
                         \log R_q(g_0,u_0)=-6A^2+o(1).           \tag{6.1}
\]

The displayed proof in the \(Q_4\) theorem is consistent with (6.1): the
linear Taylor sum occurs once,

\[
 -{1\over2g_0}\sum_{j=0}^{q-1}\left(j+{5q\over8}\right)
 =-{9q^2\over16g_0}+o(1)=-6A^2+o(1).              \tag{6.2}
\]

Choose the small central box from that theorem so that its target profiles
contain at least a fraction \(c_A>0\) of the rank-\((m-q)\) layer and

\[
                         R_q(g,u)\le e^{-3A^2}       \tag{6.3}
\]

throughout.  The map \(\pi\mapsto\pi^\uparrow\) is injective.  Hence the
source families for distinct target profiles in the box are disjoint, and
(0.3), (3.5) may be summed.

Since

\[
 {\binom{2m}{m-q}\over W}\longrightarrow e^{-A^2}, \tag{6.4}
\]

we obtain the theorem-grade obstruction.

### Theorem 6.1 (sector-selected Gaussian Hall deficit)

For every fixed \(A>0\), at

\[
                         q=\lfloor A\sqrt m\rfloor,
\]

every family of one-owner-output depth-\(q\) windows lying inside the
sector-selected packets misses at least

\[
 \boxed{
 \left(c_A(1-e^{-3A^2})e^{-A^2}-o(1)\right)W}       \tag{6.5}
\]

lower targets.  The same conclusion holds for the installed packet cycle
compiler, regardless of its direction order.  The identical bound holds for
upper targets by the separate rank-reversed profile count following (3.5).

On the central profile itself, the exact compatible capacity ratio is the
sharper

\[
                         e^{-6A^2+o(1)},             \tag{6.6}
\]

by (0.2), (0.4), and (5.4).

#### Proof

Every target in a fixed profile can use only the forced source family
(0.1), and sector selection retains a subset of that family.  A source
owner supplies at most one based window.  Thus (3.5) is a Hall deficit for
each profile.  Sum it over the injective central type box and use
(6.3)--(6.4).  On the upper side, repeat the same count with good triples;
the local multiplicities and sector-retention factor are identical.
\(\square\)

This is a linear deficit.  In particular the desired floor-energy estimate

\[
                         \sum_{q\le H,\varepsilon}Q_{q,\varepsilon}=o(W)
\]

already fails at the one Gaussian depth in Theorem 6.1.

## 7. Sharp escape requirement

Let \(\mathcal A_A\) be the union of the central target types used in
Theorem 6.1, and let \(\mathcal S_A^{\rm sec}\) be their forced selected
source union.  The proved deficit is

\[
 \Delta_A
 :=|\mathcal A_A|-|\mathcal S_A^{\rm sec}|
 \ge\left(c_A(1-e^{-3A^2})e^{-A^2}-o(1)\right)W.    \tag{7.1}
\]

Every additional source owner supplies at most one new based depth-\(q\)
occurrence.  Therefore any repaired architecture needs at least
\(\Delta_A\) windows targeting \(\mathcal A_A\) whose sources are not in
the forced fibres (0.1).  Equivalently, it must break the old profile map on
a positive-density owner set.

The following operations do not do so:

1. changing the order of the \(r\) selected directions;
2. choosing first versus last cross axis within a sector;
3. changing the cycle factor inside the same selected \(Q_r\);
4. using different completed frames while keeping the same quartet product
   cell; or
5. repairing only \(o(W)\) source owners.

Every such window still changes exactly \(q\) old-atlas two-set blocks to
good singleton blocks, so its source profile remains (0.1).

The minimal qualitative escape is one of the following.

* **Intra-quartet re-atlasing.**  The smallest-support profile-breaking move
  already fits in one quartet: use a Johnson edge joining two rank-two
  states that belong to different old cells \(C_i\).  Equivalently, deploy a
  second perfect matching of the six local two-set states which is not a
  relabelling inside the old three cells.  Such an edge can change which
  old good/bad singleton profile receives the source.  Merely renaming the
  completed frame of an old cell is insufficient.

* **Cross-block paths.**  If every old local cell is to remain intact, then
  a profile-breaking move must couple blocks.  The smallest such literal
  trade uses two quartets, hence eight coordinates, and permits a window to
  change the old local-rank/profile ledger jointly rather than through the
  forced map (0.1).

More generally, an owner-dependent second atlas is admissible only if its
profile fibres overlap the deficient old fibres: a central target must
actually receive a source from outside (0.1).

Neither condition is asserted sufficient.  Equation (7.1) is the sharp
necessary scale: the number of profile-crossing based windows must be
\(\Omega_A(W)\), not \(o(W)\).  Thus the sector near-tiling remains a valid
owner resolution, but it cannot be the coefficient-one colored core without
a positive-density cross-block or re-atlasing layer.

## 8. Audited boundary

The sector note correctly proves:

1. pairwise owner-disjoint packets;
2. an owner leave \(o(W/H)\) in its stated range;
3. frame change on every selected active axis; and
4. dyadic dispersion of the selected direction sequence.

It does not prove, and in fact cannot satisfy, the remaining colored target
kernel inside the frozen quartet atlas.  The assertion that the fixed-frame
Gaussian cut no longer applies is too narrow: frame variation defeats the
old whole-frame cut, but the mixed-frame **fixed-block profile-capacity** cut
applies unchanged.  Formula (0.2) is the exact corrected interface between
the two notes.

# A Gaussian zero-winding PBBS return with maximal canonical reframing

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

The linearly reframing residual in
`MATH_ATTACK_HEIGHT_SATURATION_DIFFUSE_REFRAMING_20260725.md` is genuine.
It cannot be removed by a deterministic charge to winding, endpoint
overlap, or a tall preempting forest.

Fix an integer \(s\ge2\) and positive integers

\[
 L_0,L_1,\ldots,L_{s-2}.
\]

Put

\[
 F_i=(10)^{L_i},
 \qquad
 m=s+\sum_{i=0}^{s-2}L_i.                         \tag{0.1}
\]

There is an explicit semilength-\(m\), height-\(s\) Dyck root
\(D_0(\mathbf L)\) with the following properties.

1. Its omitted physical coordinate has a genuine first zero-winding return
   after \(2s+1\) ordinary PBBS steps.
2. Among the first \(s-1\) step-two transitions

   \[
   D_0\longmapsto D_1\longmapsto\cdots
        \longmapsto D_{s-1},
   \]

   every transition changes the canonical first-deepest frame.  Thus, in
   the convention of the partial-atlas theorem,

   \[
   \boxed{R(D_0,s)=s-1.}                           \tag{0.2}
   \]

3. Every preempting forest has relative height exactly one.  If all but
   one of the \(L_i\)'s equal one, then all but one of the frame changes
   have a one-edge witness.
4. In the endpoint-overlap notation

   \[
   \Lambda=\delta(D_0)+\delta(D_s)-2m,
   \]

   one has

   \[
   \boxed{\Lambda=0.}                              \tag{0.3}
   \]

5. For every fixed \(c>0\), choosing

   \[
   m_s=\lceil cs^2\rceil,
   \qquad
   L_0=m_s-2s+2,
   \qquad
   L_i=1\quad(1\le i\le s-2)                     \tag{0.4}
   \]

   gives, for all sufficiently large \(s\), a Gaussian family with

   \[
   {s\over\sqrt{m_s}}\longrightarrow {1\over\sqrt c},
   \qquad {R\over s}\longrightarrow1.            \tag{0.5}
   \]

   Taking \(c>A^{-2}\) puts the return below
   \(H_A=\lceil A\sqrt{m_s}\rceil\).

For fixed \((m,s)\), this construction contains exactly

\[
 \boxed{
 \binom{m-s-1}{s-2}}
 \tag{0.6}
\]

distinct roots, provided \(m\ge2s-1\).  At \(m\asymp s^2\), its logarithm
is \(O(\sqrt m\log m)=o(m)\).  Hence the construction is not a
Catalan-mass near-saturator and does not refute the desired aggregate
bound \(o_A(\operatorname {Cat}_m/\sqrt m)\).  What it rigorously refutes
is every pointwise theorem asserting that zero or bounded winding,
\(\Lambda=0\), or disjoint tall witnesses force \(R=o(s)\).

## 1. The initial star-comb root

Use the first-deepest-spine notation

\[
 D=A_0\,1A_1\,1\cdots1A_{s-1}\,1
       0B_{s-1}0\cdots0B_1\,0B_0.                \tag{1.1}
\]

Define \(D_0=D_0(\mathbf L)\) by

\[
 A_i=F_i=(10)^{L_i}\quad(0\le i\le s-2),
 \qquad A_{s-1}=\varnothing,
 \qquad B_i=\varnothing\quad(0\le i<s).          \tag{1.2}
\]

Equivalently, its contour word is

\[
 \boxed{
 D_0=F_0\,1F_1\,1\cdots1F_{s-2}\,1\,1\,0^s.}
 \tag{1.3}
\]

The displayed spine contributes \(s\) edges, and the star forests
contribute \(\sum_iL_i\), proving the semilength in (0.1).

At depth \(i\le s-2\), every component of \(F_i\) is a single leaf and
therefore reaches total depth only \(i+1\le s-1\).  The displayed spine
is consequently the unique source of height \(s\), and its terminal leaf
is the canonical first deepest leaf.  Thus (1.1)--(1.2) are the actual
canonical sectors, not a prescribed noncanonical overlay.

For \(s=2,L_0=1\), the word is \(101100\).  Its first transition is the
audited smallest example

\[
 101100\overset\tau\longmapsto110100,
\]

where the actual new sector is \(B_1=10\).  This also checks the star-size
bookkeeping used in the induction below: the old transported spine child
joins the unused teeth after the new first tooth, so a star of \(L\) teeth
creates a post-spine star of \(L\), not \(L-1\).

## 2. Exact sector induction

Put \(D_j=\tau^jD_0\).  We give the actual canonical sectors at every
phase.  For \(0\le j\le s-1\), define

\[
 A_i^{(j)}=
 \begin{cases}
 F_{i-j},&j\le i\le s-2,\\
 \varnothing,&\text{otherwise},
 \end{cases}                                      \tag{2.1}
\]

and

\[
 B_i^{(j)}=
 \begin{cases}
 F_{2s-j-i-2},&s-j\le i\le s-1,\\
 \varnothing,&\text{otherwise}.
 \end{cases}                                      \tag{2.2}
\]

At phase \(s\), put

\[
 A_i^{(s)}=\varnothing\quad(0\le i<s),
 \tag{2.3}
\]

\[
 B_i^{(s)}=
 \begin{cases}
 F_{s-i-2},&0\le i\le s-2,\\
 \varnothing,&i=s-1.
 \end{cases}                                      \tag{2.4}
\]

### Theorem 2.1 (maximal-reframing itinerary)

Equations (2.1)--(2.4) are the canonical first-deepest sectors of
\(D_j\).  Every transition \(D_j\mapsto D_{j+1}\) with
\(0\le j\le s-2\) is a frame change, while the transition
\(D_{s-1}\mapsto D_s\) is frame-preserving.

#### Proof

Equations (2.1)--(2.2) at \(j=0\) are exactly (1.2).  Assume they hold at
some \(0\le j\le s-2\).  The formal sector transport is

\[
 \widetilde A_0=B_0^{(j)},
 \qquad
 \widetilde A_i=A_{i-1}^{(j)}\quad(1\le i<s),    \tag{2.5}
\]

\[
 \widetilde B_i=B_{i+1}^{(j)}\quad(0\le i<s-1),
 \qquad
 \widetilde B_{s-1}=\varnothing.                 \tag{2.6}
\]

Since the occupied \(B\)-indices in (2.2) begin at \(s-j\ge2\), one has
\(B_0^{(j)}=\varnothing\).  Formula (2.5) moves the remaining
\(A\)-stars down one level.  In particular,

\[
 \widetilde A_{s-1}=F_{s-j-2}.                   \tag{2.7}
\]

Every earlier transported \(A\)-star is at depth at most \(s-2\) and
therefore remains below height \(s\).  But every leaf in (2.7), now at
depth \(s-1\), reaches height \(s\) before the displayed transported
spine.  Hence the displayed spine is not canonical: this transition is a
frame change, and the first tooth of (2.7) is the new canonical spine
child.

At that depth, the forest after the new spine child consists of the
remaining \(L_{s-j-2}-1\) teeth and the old displayed spine child.  The
latter is also a leaf.  Thus the new post-spine forest has exactly
\(L_{s-j-2}\) teeth and is

\[
 B_{s-1}^{(j+1)}=F_{s-j-2}.                       \tag{2.8}
\]

All other formal sectors retain their order.  Substitution in
(2.5)--(2.6) now gives exactly (2.1)--(2.2) with \(j\) replaced by
\(j+1\).  This proves the induction through phase \(s-1\), and proves a
frame change at every \(0\le j\le s-2\).

At phase \(s-1\), (2.1) has no nonempty \(A\)-sector, while (2.2) has
occupied \(B\)-indices \(1,2,\ldots,s-1\).  The formal transport therefore
has no earlier forest at all and remains canonical.  It merely shifts
those \(B\)-stars down one level, giving (2.3)--(2.4).  The last transition
is frame-preserving.  \(\square\)

The theorem proves (0.2) under the convention that \(R\) counts the first
\(s-1\) transitions among the core roots
\(D_0,D_1,\ldots,D_{s-1}\).  If one also records the endpoint transition
to \(D_s\), there are still exactly \(s-1\) changes, since that last
transition is preserving.

## 3. Exact return, winding, and endpoint overlap

For canonical sectors at height \(s\), the two-step deficit and first
maximum position are

\[
 d(D)=2|B_0|+1,
 \qquad
 \delta(D)=s+2\sum_{i=0}^{s-1}|A_i|.             \tag{3.1}
\]

Equations (2.1)--(2.2) give, for every \(0\le j<s\),

\[
 B_0^{(j)}=\varnothing,
 \qquad
 \boxed{d(D_j)=1.}                                \tag{3.2}
\]

Put \(C_j=\sum_{t<j}d(D_t)\).  Then

\[
 C_j=j\quad(0\le j\le s).                        \tag{3.3}
\]

For \(j<s\), (2.1) and (3.1) give

\[
 \delta(D_j)
 =s+2\sum_{r=0}^{s-j-2}L_r
 \ge s>j=C_j.                                    \tag{3.4}
\]

At phase \(s\), every \(A\)-sector is empty, and hence

\[
 \boxed{\delta(D_s)=s=C_s.}                       \tag{3.5}
\]

All quantities in (3.3)--(3.5) lie strictly below
\(N=2m+1\).  More explicitly, if the initial omitted label is \(u\), then
the even-time labels are

\[
 \lambda_{2j}=u-C_j=u-j\pmod N,                  \tag{3.5a}
\]

and hence do not equal \(u\) for \(1\le j\le s\).  At the following odd
time the label equals \(u\) exactly when
\(C_j\equiv\delta(D_j)\pmod N\).  Equations (3.4)--(3.5), with both sides
in \([0,N)\), exclude every \(j<s\) and give ordinary equality at
\(j=s\).  Thus the return is consecutive, its gap is \(2s+1\), and its
winding is zero.  Since \(m\ge2s-1>s\), the gap is strictly below the
circumference.

At phase zero,

\[
 \delta(D_0)
 =s+2\sum_iL_i
 =2m-s.                                           \tag{3.6}
\]

Together with (3.5), this gives

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m
 =(2m-s)+s-2m=0,                                  \tag{3.7}
\]

proving (0.3).  Thus the maximal frame-changing itinerary lies in the
endpoint no-overlap chamber, not merely in bounded winding.

Finally, (2.7) shows that every change is caused by a height-one star.
Under the specialization (0.4), all but the change associated with
\(F_0\) have a one-edge preemptor.  Hence no injective charge assigning a
positive fraction of the changes to disjoint forests of diverging relative
height or diverging size can be valid.

## 4. Count and Gaussian specialization

The contour (1.3) determines the ordered tuple
\((L_0,\ldots,L_{s-2})\) uniquely.  Conversely every positive tuple with

\[
 \sum_{i=0}^{s-2}L_i=m-s                            \tag{4.1}
\]

gives a root covered by Theorems 2.1 and 3.1.  The number of positive
compositions of \(m-s\) into \(s-1\) parts is

\[
 \binom{(m-s)-1}{(s-1)-1}
 =\binom{m-s-1}{s-2},                              \tag{4.2}
\]

which proves (0.6).  Such compositions exist exactly when
\(m-s\ge s-1\), namely \(m\ge2s-1\).

For (0.4),

\[
 L_0+(s-2)=m_s-s,
\]

so (4.1) holds, and \(L_0>0\) for all large \(s\).  Also

\[
 {s\over\sqrt{m_s}}\to c^{-1/2},
 \qquad
 {R\over s}={s-1\over s}\to1.                    \tag{4.3}
\]

If \(c>A^{-2}\), then \(c^{-1/2}<A\), and hence
\(s\le\lceil A\sqrt{m_s}\rceil\) eventually.

To audit the mass, put \(M=m-s-1\) and \(k=s-2\).  The elementary
binomial estimate gives

\[
 \binom Mk\le\left({eM\over k}\right)^k.          \tag{4.4}
\]

When \(m\asymp s^2\), the logarithm of the right side is

\[
 O(s\log s)=O(\sqrt m\log m)=o(m).                \tag{4.5}
\]

Thus (0.6) is \(\exp(o(m))\), whereas
\(B_m=\exp(m\log4-O(\log m))\).  The star-comb family is exponentially
negligible in Catalan mass.

## 5. Exact boundary

The construction proves that all three proposed deterministic charges fail
with their strongest natural quantifiers.

1. **Winding charge:** every example has winding zero.
2. **Endpoint-overlap charge:** every example has \(\Lambda=0\).
3. **Tall-forest charge:** every frame change is caused by a relative
   height-one forest, and all but one can have a one-edge witness in the
   Gaussian specialization.

Moreover the construction has \(R=s-1\) at every admissible rank and can
be placed in every fixed Gaussian window by (0.4).  Therefore zero winding
does not imply \(R=o(s)\), even at Gaussian height.

What remains possible, and is exactly what coefficient one now requires,
is an **aggregate mass theorem**: linearly reframing Gaussian returns may
still have total edge-disjoint packing
\(o_A(B_m/\sqrt m)\).  The count (0.6) supports that possibility rather
than contradicting it.  Any proof must use the Catalan rarity or mutual
trace compatibility of the complete reframing itinerary; no pointwise
winding, endpoint, or tall-witness inequality can supply the vanishing
factor.

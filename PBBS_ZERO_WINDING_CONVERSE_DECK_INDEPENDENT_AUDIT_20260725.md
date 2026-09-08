# Independent audit of the proposed zero-winding converse and its deck lift

Date: 2026-07-25

Method: pure hand mathematics. No computation, finite search, or external
input is used.

## 0. Verdict

The universal implication asserted in
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md` is false:

\[
 d(D)=1
 \quad\not\Longrightarrow\quad
 \text{a zero-winding return at gap }2\operatorname{ht}(D)+1.
\]

There are two related defects in Lemma 2.1.

1. An original \(A_i\)-forest is transported one level deeper.  It may then
   tie the global height and, because it occurs before the formally displayed
   spine, pre-empt that spine immediately.
2. An original \(B_j\)-forest may be below the global height when it first
   crosses the root seam, but subsequent formal shifts move it down through
   positive-depth \(A\)-sectors.  It may then tie the global height and
   pre-empt the displayed spine.

The proof checks only the relative height of a transported \(B_j\)-forest
when it reaches the root.  That does not control its total height after later
changes of attachment depth, and it does not address the first defect at all.

The failure is not confined to one small word.  For every integer \(t\ge0\),
the primitive Dyck word

\[
 D_t=1(10)^t110011000\in\mathcal D_{t+5}
\]

has height three and \(d(D_t)=1\), but has no return at gap seven.  In fact,
using the already proved necessity that a zero-winding return must occur at
step-two time equal to the height, \(D_t\) has no zero-winding return at all.

Consequently the inference that every root in the family \(\mathcal U_{r,A}\)
starts a short residence is false, and the Catalan-positive packing lower
bound does not follow.  This audit does **not** prove that the lower bound
itself is false by some other argument; it proves that the supplied argument
does not establish it.  Hence neither \((RP_A)\) nor its negation follows
from the proposed converse.

The separate deck statement is sound: every pairwise quotient-edge-disjoint
family of nonwrapping quotient intervals has exactly \(N\) mutually
edge-disjoint spatial lifts per member.  Thus the factor \(N\) is not the
source of the failure.

## 1. The exact tie omitted by Lemma 2.1

Let an \(A_i\)-forest be attached at depth \(i\), and let \(a_i\) be its
relative height.  Because the chosen spine reaches the *first* deepest leaf,
one knows only

\[
 a_i\le h-i-1.
\tag{1.1}
\]

Under the formal update in (2.3) of the audited report, this forest becomes
an \(A_{i+1}'\)-forest, attached at depth \(i+1\).  Its total height can be

\[
 (i+1)+a_i=h.
\tag{1.2}
\]

Equality is allowed by (1.1).  Since an \(A\)-forest is traversed before the
formally displayed spine child, equality in (1.2) means that the canonical
first deepest spine changes.  To rule this out one would need the strictly
stronger inequality \(a_i\le h-i-2\), which is not implied by first-deepest
selection.

There is a second delayed tie.  Let a \(B_j\)-forest have relative height
\(b_j\).  First-deepest selection allows

\[
 b_j\le h-j,
\tag{1.3}
\]

with equality, because a \(B_j\)-forest occurs after the chosen spine.  The
formal shifts move it through

\[
 B_j,B_{j-1},\ldots,B_0,A_0,A_1,\ldots.
\tag{1.4}
\]

When it first reaches \(A_0\), its height is indeed at most
\(h-j<h\) for \(j\ge1\).  But after \(q\) further shifts it is attached in
\(A_q\), so its total height is \(q+b_j\).  If \(b_j=h-j\), then at
\(q=j\) this is exactly \(h\), and the forest now occurs before the formal
spine.  The root-seam estimate used in the proposed proof therefore cannot
be iterated.

The convention that the marked step is the **first** one attaining the
global maximum is essential to the exact formula for \(\delta\) and \(\tau\).
Changing tie-breaking does not repair the proof without changing and
reproving the underlying PBBS formulas.

## 2. A minimal direct failure of the sector formula

Take

\[
 D=101100.
\tag{2.1}
\]

Its height is two.  Its canonical sectors are

\[
 A_0=10,\qquad A_1=B_1=B_0=\varnothing.
\tag{2.2}
\]

In particular \(d(D)=1\).  The literal block rotation gives

\[
 \tau D=110100.
\tag{2.3}
\]

The formal update (2.3) of the audited report assigns the old word \(10\)
to \(A_1'\).  But in \(110100\) that word reaches height two before the
formal spine: the first deepest leaf is the first of the two children at
depth one.  The canonical sectors of \(\tau D\) are instead

\[
 A_0'=A_1'=B_0'=\varnothing,\qquad B_1'=10.
\tag{2.4}
\]

Thus Lemma 2.1 already fails after one shift.  It would predict from its
formal sectors

\[
 \delta(\tau D)=2+2|E(A_1')|=4,
\]

whereas the actual first maximum-reaching step of \(110100\) is step two,
so

\[
 \delta(\tau D)=2.
\tag{2.5}
\]

This example invalidates the sector recursion itself.  It happens still to
satisfy the claimed eventual return, so a separate example is needed to
disprove the converse theorem.

## 3. A primitive counterexample in every rank \(r\ge5\)

Fix \(t\ge0\), put \(X_t=(10)^t\), and define

\[
 D_t=1X_t110011000=1E_t0,
 \qquad E_t=X_t11001100.
\tag{3.1}
\]

The word \(E_t\) is Dyck of height two.  Hence \(D_t\) is primitive of
semilength

\[
 r=t+5,
\tag{3.2}
\]

has height three, and has empty terminal suffix in its canonical
first-maximum factorization.  Therefore

\[
 d(D_t)=1.
\tag{3.3}

We now apply only the exact identity

\[
 D=P1R0S
 \quad\Longrightarrow\quad
 \delta(D)=|P|+1,\quad d(D)=|S|+1,\quad
 \tau D=S1P0R.
\tag{3.4}

First,

\[
 D_t=(1X_t1)\,1\,(001100)\,0,
\tag{3.5}
\]

so

\[
 D_t^{(1)}:=\tau D_t=11X_t10001100,
 \qquad d(D_t)=1.
\tag{3.6}

For \(t\ge1\), writing \(X_{t-1}=(10)^{t-1}\), the next canonical
factorization is

\[
 D_t^{(1)}
 =(11)\,1\,[0X_{t-1}100]\,0\,(1100).
\tag{3.7}

For \(t=0\), it is

\[
 D_0^{(1)}=(11)\,1\,(00)\,0\,(1100).
\tag{3.8}

In both cases,

\[
 \delta(D_t^{(1)})=3,\qquad d(D_t^{(1)})=5.
\tag{3.9}

For \(t\ge1\), (3.4) next gives

\[
 D_t^{(2)}=110011100X_{t-1}100
          =(110011)\,1\,[00X_{t-1}10]\,0.
\tag{3.10}

For \(t=0\),

\[
 D_0^{(2)}=1100111000=(110011)\,1\,(00)\,0.
\tag{3.11}

Thus, for every \(t\ge0\),

\[
 \delta(D_t^{(2)})=7,\qquad d(D_t^{(2)})=1.
\tag{3.12}

Finally, for \(t\ge1\),

\[
 D_t^{(3)}
 =1110011000X_{t-1}10,
\tag{3.13}

while \(D_0^{(3)}=D_0=1110011000\).  In every case the first three
steps are up-steps, the displayed length-ten prefix has height three and
returns to zero, and the remaining suffix has height at most one.  Hence

\[
 \delta(D_t^{(3)})=3.
\tag{3.14}

Let

\[
 C_j=\sum_{i=0}^{j-1}d(D_t^{(i)}).
\]

Equations (3.3), (3.9), and (3.12) give

\[
 C_1=1,\qquad C_2=6,\qquad C_3=7.
\tag{3.15}

The odd-time return comparisons through step-two time three are therefore

\[
 \begin{array}{c|ccc}
 j&1&2&3\\ \hline
 C_j&1&6&7\\
 \delta(D_t^{(j)})&3&7&3.
 \end{array}
\tag{3.16}

No equality occurs.  Moreover \(N=2t+11\ge11\), so none of the differences
in (3.16) is a nonzero multiple of \(N\).  The even-time displacements
\(C_1,C_2,C_3\) are also strictly between zero and \(N\).  Therefore the
initial omitted coordinate does not return at any positive time at most
seven: at time one the displacement is
\(\delta(D_t)=2t+3\in(0,N)\), (3.16) excludes the remaining odd times,
and the displayed \(C_j\)'s exclude the positive even times.  In
particular, it does not return at the asserted gap

\[
 2\operatorname{ht}(D_t)+1=7.
\tag{3.17}

The previously proved necessity theorem says that any zero-winding return
from a height-three word would have step-two time three.  With that theorem,
(3.16) also proves that \(D_t\) has no zero-winding return at any later
time.

The first-deepest sectors of \(D_t\) make both tie mechanisms visible.  At
depth one, the \(t\) preliminary leaves form \(A_1=X_t\), while the second
height-two branch forms \(B_1=1100\).  The \(A_1\)-sector can pre-empt after
the first formal shift; the tied \(B_1\)-sector later crosses the seam and
pre-empts after entering a positive-depth \(A\)-sector.

## 4. Exact impact on the Gaussian primitive family

The proposed family was

\[
 \mathcal U_{r,A}
 =\{1E0:E\in\mathcal D_{r-1},\ \operatorname{ht}(E)
      \le \lceil A\sqrt r\rceil-2\}.
\tag{4.1}

For every \(t\ge0\), the word \(D_t\) in (3.1) has exactly this form with
\(r=t+5\) and \(\operatorname{ht}(E_t)=2\).  Therefore, for every fixed
\(A>0\),

\[
 D_{r-5}\in\mathcal U_{r,A}
\tag{4.2}

for every sufficiently large integer \(r\) satisfying
\(\lceil A\sqrt r\rceil\ge4\).  Yet (3.16) shows that this member does not
start the asserted residence.  Thus the statement “every member” of
\(\mathcal U_{r,A}\) starts a short zero-winding residence fails in every
sufficiently large rank, not merely at a fixed exceptional rank.

The spectral estimate counting \(\mathcal U_{r,A}\) may remain correct as a
count of height-bounded primitive Dyck paths.  What fails is the map from
that counted set to short-return starts.  No lower bound of Catalan order on
the valid subfamily is supplied.  Consequently (5.2), (5.3), and (5.4) of
the audited report are unsupported.

## 5. Independent audit of the physical deck factor

The deck multiplier is correct under precisely the nonwrapping hypothesis
used in Section 5.

### Proposition 5.1 (exact \(N\)-lift packing)

Fix \(r\ge1\), put \(N=2r+1\), and let \(\mathscr F\) be a family of
quotient residence intervals such that:

1. every interval trace contains no repeated quotient transition edge;
2. traces belonging to distinct members of \(\mathscr F\) are
   quotient-edge-disjoint.

Then the union of all spatial lifts of all members of \(\mathscr F\) is a
family of exactly

\[
 N|\mathscr F|
\tag{5.1}

pairwise physical-edge-disjoint residence intervals.

#### Proof

The spatial coordinate \(u\in\mathbb Z_N\) gives the regular \(N\)-sheeted
rotation deck over each quotient transition edge.  A quotient return
criterion depends only on the normalized Dyck root, so one lift implies all
\(N\) translates.

Suppose two translates of one quotient interval shared a physical edge.
Projecting that edge identifies a quotient edge in the trace.  Because the
trace has no repeated quotient edge, the shared edge must occur at the same
trace position in both lifts.  The deck action on the fibre over that edge
is free, so the two translates are equal.  Hence the \(N\) distinct
translates are pairwise edge-disjoint.

If lifts of two different selected quotient intervals shared a physical
edge, its projection would belong to both quotient traces, contrary to
assumption 2.  This proves (5.1). \(\square\)

A residence of projected length at most \(H\) uses at most \(H+1\)
quotient transition edges, including its insertion and removal boundary
edges.  On a quotient cycle of length strictly greater than \(H+1\), those
edges are distinct.  Thus deleting all roots on quotient cycles of length
at most \(H+1\) is enough to invoke Proposition 5.1.

The auxiliary greedy constant is also correct conditionally.  There is at
most one qualifying next-return interval per oriented quotient start.  An
interval containing at most \(H+1\) consecutive edges can intersect only
intervals whose starts lie in a set of at most \(2H+1\) cyclic positions.
Thus a delete-the-intersection-neighbourhood greedy algorithm retains at
least \(R/(2H+1)\) intervals from \(R\) qualifying starts on the long
cycles.  Applying Proposition 5.1 then multiplies this packing by exactly
\(N\).

Therefore the deck and greedy portions of Section 5 would be valid **if**
one had the asserted Catalan-positive set of qualifying starts.  The
counterexample in Section 3 removes exactly that premise.

## 6. Audited boundary

The following statements are proved by this audit.

* Lemma 2.1 of the audited report is false under the frozen first-maximum
  convention.
* For every \(t\ge0\), \(D_t=1(10)^t110011000\) is a primitive
  semilength-\(t+5\), height-three Dyck word with \(d(D_t)=1\) and no
  return at gap seven.
* Hence \(d(D)=1\) is necessary but not sufficient for a zero-winding
  return.
* The claimed Catalan-positive short-return family and the resulting
  \(\Omega_A(B_r\sqrt r)\) physical packing are not proved.
* The exact \(N\)-fold physical deck lift is valid for nonwrapping,
  quotient-edge-disjoint traces.

No assertion about the truth or falsity of \((RP_A)\) follows from this
audit.  The surviving problem is to characterize the additional canonical
tie/sector condition, beyond \(d(D)=1\), that makes the height-time
zero-winding equality hold, and then to count and pack only that valid
subfamily.

# Conditional cyclic-window-simple chronology cut for mechanical clone Hall

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

> **Audited scope correction.**  The one-row gap criterion and staircase
> spectrum \((L-d)_+\) below are exact.  The aggregate bound (0.7) and
> all consequences (0.8)--(0.11) additionally require the witness bank
> to be simple for *all cyclic \(m\)-windows*.  An infinity-cut MSW or
> \(C_8\) factor is only primary-owner-simple.  Away from the ports, a
> target occurs cyclically both in its primary-owner row and in the row
> primarily owning its complement, so the cyclic multiplicity is two.
> The unconditional replacement for (0.7) has an extra factor two and is
> vacuous in the shallow range (0.9).  Therefore this file does not rule
> out the actual complement-paired Catalan bank.  The corrected theorem
> and its exact implication boundary are in
> MATH_THEOREM_K_CATALAN_PROMOTION_CROSS_INTERFACE_AND_CHRONOLOGY_CUT_20260726.md.

## 0. Result

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N_d=\binom{2m}{m-d},
\tag{0.1}
\]

and assume

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 (M-1)N_H\le W.
\tag{0.2}
\]

The mechanical clone-Hall theorem gives separate near-perfect matchings
at every depth.  This note proves that those matchings cannot be lifted
to a common ambient-row assignment which preserves both the complete
promotion-ring order and each nested flag.

The obstruction is statewise.  Fix a promotion top \(U\), an oriented
cyclic order \(\sigma\) on \(U\), and an ambient cyclic row \(\pi\) on
\(V\) satisfying

\[
                         \pi|_U=\sigma.
\tag{0.3}
\]

If \(\pi\) certifies \(L\) middle phases of the \(\sigma\)-ring, then

\[
                         0\le L\le H+1,
\tag{0.4}
\]

those phases form one cyclic interval, and the numbers among them whose
complete nested flags have radius at least \(d\) are exactly

\[
                         (L-d)_+.
\tag{0.5}
\]

Thus the flag radii available from one inherited block are, in some
order,

\[
                         0,1,\ldots,L-1.
\tag{0.6}
\]

Now let the ambient rows form a middle-owner-simple family, as they must
in one literal exact ambient factor.  Rows assigned to the same
promotion top and inducing the same \(\sigma\) have disjoint certified
middle-phase blocks.  Consequently, over all critical promotion tops,
the number of ambient-certified flags of radius at least \(d\) is at
most

\[
 \boxed{
 C_d\le MN_H\left(1-\frac d{H+1}\right).}
\tag{0.7}
\]

The retained-SCD census needs exactly \(N_d\) flags of radius at least
\(d\).  Hence the entire depth-\(d\) demand set is already a failed Hall
cut, of deficiency at least

\[
 \boxed{
 \Delta_d=
 \left[N_d-MN_H\left(1-\frac d{H+1}\right)\right]_+.}
\tag{0.8}
\]

Let

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad
 D=\left\lfloor\frac{m}{4(H+1)}\right\rfloor.
\tag{0.9}
\]

For all sufficiently large \(m\), \(q_0\le D\), and for every
\(q_0\le d\le D\),

\[
 \boxed{
 \Delta_d\ge \frac{Wd}{2(H+1)}.}
\tag{0.10}
\]

In particular,

\[
 \boxed{
 \sum_{d=q_0}^{D}\Delta_d
 \ge
 \left(\frac1{64}+o(1)\right)
       \frac{Wm^2}{H^3}
 =\Omega\!\left(
       \frac{W\sqrt m}{(\log m)^{3/2}}
       \right)
 =\omega(W).}
\tag{0.11}
\]

Therefore no Hall assignment of a middle-owner-simple ambient row bank
to promotion roots can preserve a common complete ring order and supply
all nested flags, even if every cyclic extension of every desired
mechanical order is generously declared available.  Separate clone Hall
at the individual depths does not address this failed grouped cut.

The theorem does **not** forbid a genuine noncellular crossing braid in
which one flag changes ambient rows between depths, or in which an
ambient row agrees with the promotion order only on a proper local
segment and different segments are rethreaded.  Such a construction no
longer inherits one complete nested flag from one ambient row; it must
absorb at least the deficiency (0.11) as cross-row owner--depth
incidences.  No theorem currently converts those crossings to
\(o(W)\) physical cost.

## 1. Gap form of one ambient extension

Fix a top \(U\in\binom VM\), write

\[
 \sigma=(u_0,u_1,\ldots,u_{M-1}),
\tag{1.1}
\]

with indices in \(\mathbb Z_M\), and let \(g_i\) be the gap immediately
after \(u_i\).  If an ambient order \(\pi\) satisfies (0.3), deleting
the labels in \(A=V\setminus U\) from \(\pi\) leaves (1.1).  Define its
nonempty occupied-gap set

\[
 B(\pi,U)={i:g_i\text{ contains at least one label of }A
                    \text{ in }\pi\}.
\tag{1.2}
\]

For a phase \(a\in\mathbb Z_M\) and \(-H\le r\le H\), put

\[
 X_a(r)={u_a,u_{a+1},\ldots,u_{a+m+r-1}\}.
\tag{1.3}
\]

These are exactly the nested sets of the promotion flag at phase \(a\),
up to the harmless global phase convention: the start is fixed and the
terminal coordinate advances once when \(r\) advances once.

### Lemma 1.1 (exact gap criterion)

For \(0\le d\le H\), the whole flag

\[
                         (X_a(r))_{-d\le r\le d}
\tag{1.4}
\]

consists of cyclic intervals of the ambient row \(\pi\) if and only if

\[
 B(\pi,U)\subseteq Q_a(d),
 \qquad
 Q_a(d)=\{a+m+d-1,\ldots,a-1\},
\tag{1.5}
\]

where \(Q_a(d)\) is a cyclic interval of exactly \(H-d+1\) gaps.

#### Proof

The set \(X_a(r)\) is already consecutive in the restricted order
\(\sigma\).  It remains consecutive in \(\pi\) precisely when none of
its internal gaps

\[
                         g_a,g_{a+1},\ldots,g_{a+m+r-2}
\]

is occupied.  Their complementary gap interval is \(Q_a(r)\), of size

\[
                         M-(m+r-1)=H-r+1.
\]

As \(r\) rises from \(-d\) to \(d\), these complementary intervals are
nested and the smallest is \(Q_a(d)\).  This proves (1.5). \(\square\)

### Lemma 1.2 (staircase spectrum of one row)

Let

\[
 P(\pi,U)=\{a:X_a(0)\text{ is an ambient }m\text{-window of }\pi\}.
\tag{1.6}
\]

If this set is nonempty, it is one cyclic phase interval of some length
\(L\le H+1\).  Among its \(L\) phases, the maximum radii certified by
\(\pi\) are exactly

\[
                         L-1,L-2,\ldots,0.
\tag{1.7}
\]

Consequently the exact number certified to radius at least \(d\) is
\((L-d)_+\).

#### Proof

By Lemma 1.1 at \(d=0\), \(P(\pi,U)\) is the set of length-
\((H+1)\) cyclic gap intervals which contain \(B(\pi,U)\), with phase
and gap starts related by a fixed translation.

Because \(m>H+1\) for all sufficiently large \(m\), one has
\(H+1<M/2\).  If \(P(\pi,U)\ne\varnothing\), the occupied gaps have a
unique minimal cyclic hull of some length \(s\le H+1\).  The number of
length-\((H+1)\) gap intervals containing this hull is

\[
                         L=H-s+2\le H+1,
\tag{1.8}
\]

and their starts are consecutive.

Moving through these \(L\) containing intervals, the slack before the
fixed minimal hull is respectively

\[
                         L-1,L-2,\ldots,0.
\]

Passing from \(Q_a(0)\) to \(Q_a(d)\) deletes exactly the first \(d\)
gaps of that containing interval.  Hence its largest permissible \(d\)
is precisely its initial slack.  This proves (1.7) and (0.5).
\(\square\)

Two extreme cases clarify the statement.

* If every label of \(A\) is inserted in one gap of \(\sigma\), then
  \(L=H+1\), and the row supplies the full staircase
  \(H,H-1,\ldots,0\).
* If the occupied gaps themselves span \(H+1\) gaps, then \(L=1\), and
  the one inherited middle phase has no positive-depth inherited flag.

Thus the middle projection ceiling \(H+1\) is only the zeroth member of
an exact all-depth staircase law.

## 2. Middle-owner simplicity forces disjoint phase blocks

Call a family \(\mathcal F\) of ambient cyclic rows
**middle-owner-simple** when no \(m\)-subset of \(V\) is a cyclic
\(m\)-window of two distinct rows of \(\mathcal F\).  Every selected
ambient exact factor has this property.

### Lemma 2.1 (same-root disjointness)

Fix \(U\) and \(\sigma\).  If distinct rows
\(\pi,\rho\in\mathcal F\) both restrict to \(\sigma\), then

\[
                         P(\pi,U)\cap P(\rho,U)=\varnothing.
\tag{2.1}
\]

#### Proof

If phase \(a\) lay in the intersection, the same set \(X_a(0)\) would
be an ambient cyclic \(m\)-window of both rows, contrary to
middle-owner simplicity. \(\square\)

Let the nonempty phase-block lengths at one top be
\(L_1,\ldots,L_b\).  Lemma 2.1 gives

\[
                         \sum_{j=1}^bL_j\le M.
\tag{2.2}
\]

At depth \(d\), Lemma 1.2 gives capacity

\[
                         \sum_{j=1}^b(L_j-d)_+.
\tag{2.3}
\]

For every \(0\le L\le H+1\),

\[
 (L-d)_+
 \le L\left(1-\frac d{H+1}\right).
\tag{2.4}
\]

Indeed the assertion is trivial for \(L\le d\); for \(L>d\), it is
equivalent to \(L\le H+1\).  Combining (2.2)--(2.4) proves the per-top
bound

\[
 \sum_{j=1}^b(L_j-d)_+
 \le M\left(1-\frac d{H+1}\right).
\tag{2.5}
\]

Summing (2.5) over all \(N_H\) critical tops proves (0.7).  Notice that
we have granted all \(M\) phases, although a repaired ring retains only
\(M-1\).  Thus deletion can only strengthen the cut.

## 3. The grouped Hall cut

The exact retained-chain census is

\[
 \#\{\text{chains of tag }e\}=N_e-N_{e+1}
 \quad(q_0\le e<H),
 \qquad
 \#\{\text{chains of tag }H\}=N_H.
\tag{3.1}
\]

Therefore the number of chains whose flags reach radius \(d\) is

\[
 \sum_{e=d}^{H-1}(N_e-N_{e+1})+N_H=N_d.
\tag{3.2}
\]

Form the chronology-aware incidence graph at depth \(d\): its demand
vertices are the \(N_d\) active chain flags reaching depth \(d\), and
its supply positions are the ambient-row phases which certify the
entire prefix flag through that depth.  Middle-owner simplicity gives
unit capacity to every supply position.  Taking the whole demand shore
in Hall's inequality and applying (0.7) yields precisely (0.8).

This is why Theorem 5.1 of the mechanical clone-Hall atlas does not
contradict the present cut.  That theorem makes a new clone matching
separately at each rank.  It neither identifies the depth-\(d\) clone
with the same ambient middle owner at depth zero nor imposes the
staircase spectrum (0.5).  The lost constraint is not a balanced-half
profile constraint; it is the common chronology of one literal owner
flag.

## 4. Quantitative shallow deficiency

The binomial ratio has the exact product form

\[
 \frac{N_d}{W}
 =\prod_{j=0}^{d-1}\frac{m-j}{m+j+1}
 =\prod_{j=0}^{d-1}\left(1-\frac{2j+1}{m+j+1}\right).
\tag{4.1}
\]

Since \(1-\prod_j(1-x_j)\le\sum_jx_j\) for \(0\le x_j\le1\),

\[
                         \frac{N_d}{W}\ge1-\frac{d^2}{m}.
\tag{4.2}
\]

The packing-side calibration in (0.2) gives

\[
 MN_H=(M-1)N_H+N_H
 \le W+\frac{W}{M-1}
 =W\left(1+\frac1{M-1}\right).
\tag{4.3}
\]

Put \(x=d/(H+1)\).  Equations (0.8), (4.2), and (4.3) imply

\[
\begin{aligned}
 \Delta_d
 &\ge W\left(1-\frac{d^2}{m}\right)
 -W\left(1+\frac1{M-1}\right)(1-x)\\
 &\ge W\left(
       \frac d{H+1}-\frac{d^2}{m}-\frac1{M-1}
       \right).
\end{aligned}
\tag{4.4}
\]

For \(d\le D\),

\[
                         \frac{d^2}{m}
 \le\frac d{4(H+1)}.
\tag{4.5}
\]

Uniformly for \(d\ge q_0\), the critical asymptotic gives, for all
sufficiently large \(m\),

\[
                         \frac1{M-1}
 \le\frac d{4(H+1)}.
\tag{4.6}
\]

Substitution in (4.4) proves (0.10).

Finally, \(q_0=o(D)\), and hence

\[
\begin{aligned}
 \sum_{d=q_0}^{D}\Delta_d
 &\ge\frac{W}{2(H+1)}\sum_{d=q_0}^{D}d\\
 &=\left(\frac1{64}+o(1)\right)\frac{Wm^2}{H^3}.
\end{aligned}
\tag{4.7}
\]

This is (0.11).  The whole range in (0.9) satisfies
\(D=o(\sqrt m)\), so it lies inside the direct-entrance range for which
the mechanical atlas separately proved clone Hall.  The contradiction
therefore occurs exactly between separate depthwise Hall and common
nested chronology, not outside the audited atlas range.

## 5. Sharpness and the surviving escape

The local staircase law is sharp.  Given any cyclic phase block of
length \(1\le L\le H+1\), choose occupied gaps whose minimal cyclic hull
has length

\[
                         s=H+2-L.
\tag{5.1}
\]

Insert the \(m-H\) outside labels into the two endpoint gaps of that
hull (or into its unique gap when \(s=1\)).  The resulting ambient
extension has exactly that inherited middle block and exactly the flag
spectrum \(0,1,\ldots,L-1\).  Thus no stronger local loss than (0.5)
comes merely from cyclic extension geometry.

The obstruction instead comes from combining three literal demands:

1. rows simultaneously selected from one ambient exact factor are
   middle-owner-simple;
2. all rows serving one promotion ring inherit its one complete cyclic
   order; and
3. one middle owner carries one complete nested flag rather than
   independently rematched targets at different depths.

Dropping condition 2 permits ambient rows which agree with \(\sigma\)
only on the local pieces they serve.  Dropping condition 3 permits a
flag to switch rows between depths.  Either escape is a genuine
cross-row braid.  It must replace, rather than inherit, at least
\(\sum_d\Delta_d\) owner--depth incidences in the shallow band.  The
present theorem does not assert one unit of physical word cost per such
incidence, because a nonlocal braid may share boundaries across many
depths.  Proving such sharing with aggregate \(o(W)\) cost is precisely
the remaining Catalan-to-promotion interface theorem.

## 6. Exact implication boundary

Proved:

* the exact all-depth extension spectrum \((L-d)_+\);
* the middle-owner-simple capacity cut (0.7);
* the failed whole-shore Hall inequality (0.8);
* the uniform shallow lower bound (0.10); and
* the superlinear aggregate owner--depth deficiency (0.11) throughout a
  range where separate mechanical clone Hall is available.

Not proved:

* impossibility of a nonlocal partial-order braid;
* a lower bound equating owner--depth crossings with physical word
  length;
* impossibility of using globally switched alternative ambient factors
  whose selected rows are not one fixed middle-owner-simple bank; or
* coefficient one.

The precise boundary is therefore: **the direct common-restriction Hall
lift is impossible; only chronology-changing cross-row rethreading
survives.**

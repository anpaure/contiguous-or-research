# Audit of the proposed global-sharing / typed-matching reduction

## Verdict

The fractional orbit calculation and the conditional rounding implication are
correct after one precision fix: if `a_d` is the number of selected atoms of
type `d`, the hypothesis must state

\[
 \sum_{d=0}^h |a_d-\lfloor c_d/H\rfloor|
      =o\!\left(\frac{W}{Hh}\right).
\]

Under this hypothesis, a center matching with no pair of selected atoms
sharing a designated noncentral strip mask does imply
\(\nu(2m)\le (1+o(1))W(2m)\).

It is not a completed new rounding theorem.  The requested conflict-free
matching is exactly (and slightly more prescriptively than) the previously
open disjoint long-run-atom packing problem.  Moreover, the claim that
center packing is already harmless does not follow from the displayed
pair-codegree estimate when \(H\to\infty\).

## 1. Local atoms and fractional loads

For a common block length

\[
 H=m-3\log_2m-h
\]

and every \(d\le h\), the long-run condition \(H+d\le
m-3\log_2m\) is sufficient for the existing atom lemma.  Each atom has
\(H\) distinct designated masks in every supported rank and is one genuine
MTF path.  Its first state costs at most \(2d+2\) updates and its remaining
states cost \(H-1\), hence total cost \(H+2d+1\).

With

\[
 c_d=N_d-N_{d+1}\quad(d<h),\qquad c_h=N_h,
\]

the identity \(\sum_{d\ge q}c_d=N_q\) is exact.  Uniform mass \(c_d/H\)
on a full coordinate orbit gives each depth-\(q\) mask load

\[
 \sum_{d\ge q}\frac{c_d}{H}\frac{H}{N_q}=1.
\]

The total fractional atom mass is \(W/H\), and its weighted reset excess is
at most \((2h+1)W/H=o(W)\).  This part is correct, but it is the fractional
tiling already proved in `GLOBAL_LONG_RUN_MTF_ATOMS.md`, Theorem 6.1.

## 2. The conditional integral implication

Let

\[
 b_d=\lfloor c_d/H\rfloor
\]

and select \(a_d\) atoms of each type.  Assume their center sets are
pairwise disjoint and no two selected atoms share a designated noncentral
strip mask.  The latter two conditions make all designated strip masks
globally distinct.

If

\[
 E:=\sum_d|a_d-b_d|=o(W/(Hh)),
\]

then

\[
 H\sum_db_d=W-O(Hh),\qquad HE=o(W/h).
\]

At depth \(q\), the number of distinct exposed masks is
\(H\sum_{d\ge q}a_d\), so its defect is at most

\[
 H(h-q+1)+HE.
\]

Summed over the \(2h+1\) band ranks, this is

\[
 O(Hh^2)+O(hHE)=o(W),
\]

because \(Hh^2=O(m^2\log m)=o(W)\).  The total atom cost is

\[
 H\sum_da_d+\sum_da_d(2d+1)=W+o(W).
\]

Appending each missing nonempty band mask literally costs \(o(W)\), and
does not invalidate any earlier interval.  Appending each nonempty mask
outside the band also costs \(o(W)\), since for
\(h=\lceil\sqrt{m\log m}\rceil\),

\[
 2\sum_{r=0}^{m-h-1}\binom{2m}{r}-1=O(4^m/m)=o(W).
\]

Thus the conditional theorem is valid.  The empty mask must of course be
excluded in the zero-free count; the `-1` above does this.

## 3. First fatal inference in the claimed progress

For two middle sets at Johnson distance \(a\), the exact normalized
same-row atom codegree is

\[
 \frac{2(H-a)}{H\binom ma^2},
\]

and hence \(\Delta_2/D=(2+o(1))/m^2\).  It is true that
\(H^2\Delta_2/D=o(1)\) for \(H=o(m)\), and is only bounded when
\(H=(1-o(1))m\).

It does **not** follow that center-disjoint atom packing is solved or is
not an obstruction.  All black-box matching theorems audited in
`GLOBAL_MTF_ATOM_INTEGRALITY.md` lose their useful error when the
uniformity \(H\) grows.  In fact even the one-row statement that this
orbit has a matching missing \(o(W)\) vertices remains unproved in the
needed growing-\(H\) regime.  A small pair-codegree ratio alone does not
establish a near-perfect matching for growing uniformity.

The conflict condition is also not a lower-order add-on.  A center matching
plus these pair conflicts is equivalent to matching the complete designated
Pascal-strip atom edges: two atoms are disjoint as full strip edges exactly
when their center edges are disjoint and they have no noncentral conflict.
Thus the reformulation changes the representation (an \(H\)-edge plus
binary conflicts), but does not prove or weaken the old integral packing
gate.  Prescribed near-exact type quotas make it slightly stronger than the
OR-level defect formulation, which permits overlaps and only asks for
\(o(W)\) total rank defect.

## 4. Scope of the salvageable theorem

The correct conclusion is:

> A typed conflict-free matching with the stated asymptotic quota error is
> a sufficient condition for the constant-one upper bound.

It is not correct to claim, on the current evidence, that:

* such a matching exists;
* middle-center matching has already been rounded;
* the conflict degrees satisfy a known conflict-free matching theorem; or
* this is the unique remaining route.

The existing weaker and more faithful OR-level target remains:

\[
 N=W+o(W),\qquad \sum_jd_j=o(W),\qquad
 \sum_r\left(\binom{2m}{r}-|V_r|\right)=o(W),
\]

where different atoms may overlap.  A conflict-free typed packing implies
this target, but is not known to be necessary.


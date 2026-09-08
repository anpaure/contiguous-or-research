# Independent cross-audit of the stronger three-box shell constants

Source audited:
MATH_ATTACK_T_THREEBOX_SHELL_AUDIT_O_AGENT_20260724.md

Date: 2026-07-24

This cross-audit concentrates on Sections 5--6 of the source, which add an
explicit outward-ring certificate with leading constant \(1/4\) and a direct
row interpolation with leading constant \(4/19\). I rederived the
assignments, variation congestion, and final algebra from the common interval
inequality. No solver or finite search was used.

## 1. Verdict

Both stronger constants survive.

1. **Outward-ring constant \(1/4\): valid for the explicitly stipulated
   order (5.1)--(5.3).** The new certificate supplies exactly what was absent
   from the raw report: an index-by-index assignment to internal positive
   runs and a complete \(\alpha/\beta\) congestion ledger. It proves
   \[
   \sum_i d_i
   \le 2a^3+2a^2+2+(5a+1)D
   \qquad(a\ge2),
   \]
   and hence
   \[
   D\ge
   \frac{2a^3+\frac52a^2+\frac32a-3}{8a}
   =\left(\frac14+o(1)\right)a^2.
   \]

2. **Raw “canonical” wording: still under-specified.** The raw report never
   defined its canonical cut. The new proof certifies one natural outward
   enumeration; it cannot establish that this was a unique pre-existing
   convention. The correct claim is therefore “the outward enumeration
   (5.1)--(5.3) has constant \(1/4\), and in particular satisfies the raw
   numerical \(1/5\) inequality,” not “every canonical interpretation has
   constant \(1/4\).”

3. **Raster constant \(4/19\): valid for the stated induced witness order.**
   The maximum-\(y\) endpoint components have size at most three, their
   offset charges have multiplicity at most two, and direct interpolation
   inside disjoint rows gives
   \[
   \sum_i d_i\le(2a+1)(4a+2+8D).
   \]
   Combining this with the rank-capped-start inequality yields exactly
   \[
   D\ge
   \frac{4a^3-\frac72a^2-\frac{13}{2}a-3}{19a+7}
   =\left(\frac4{19}+o(1)\right)a^2.
   \]

4. **Scope remains architectural.** Both conclusions concern the order
   induced by the selected middle-rank witness intervals. They do not apply
   to interleaved radii, noncontiguous rows, nonmonotone row orders, crossing
   occurrence endpoints, or arbitrary literal braids.

The stronger source audit is therefore mathematically sound on the two new
constants, subject to its own repaired wording that distinguishes the
newly defined outward order from the raw report's undefined “canonical”
label.

## 2. Common inequality used by both certificates

Let the selected middle witnesses, ordered by their left endpoints, be
\[
I_i=[i+\alpha_i,i+\beta_i],
\qquad
d_i=\beta_i-\alpha_i,
\]
where both offset sequences are nondecreasing in \([0,D]\).

For an internal positive incidence run \([u,v]\), put \(k=v-u\). The audited
corridor inequality gives, for every \(i\),
\[
d_i\le
\begin{cases}
k+\alpha_{v+1}-\alpha_i,&i<u,\\
k+(\beta_i-\beta_{u-1})+(\alpha_{v+1}-\alpha_i),
   &u\le i\le v,\\
k+\beta_i-\beta_{u-1},&i>v.
\end{cases}
\tag{2.1}
\]

This follows from one occurrence of the relevant coordinate increment in
any positive witness. It does not require one common pin for the whole run.

For the cube \([0,2a]^3\),
\[
M_a=3a^2+3a+1,\qquad
V_a=4a^3+\frac92a^2+\frac32a-1,
\]
and every universal word of length \(M_a+D\) satisfies
\[
V_a\le\sum_i d_i+(3a-1)D.
\tag{2.2}
\]

I independently checked the endpoint-order and rank-capped-start arguments
leading to (2.1)--(2.2). They introduce no extra factorability or
common-pin assumption.

## 3. Outward-ring enumeration and run validation

The center has index \(1\). Radius \(r\) begins at
\[
b_r=2+3r(r-1)
\]
and is divided into the six disjoint length-\(r\) blocks
\[
B_{r,k}=[b_r+kr,b_r+(k+1)r-1],
\qquad 0\le k\le5.
\]

The six coordinate formulas in the source list every radius-\(r\) vertex
exactly once. In that order,
\[
Y_r=[b_r+2r,b_r+3r],\qquad
Z_r=[b_r+4r,b_r+5r]
\]
are the radius-\(r\) components of \(y\ge r\) and \(z\ge r\). Each has
\(r+1\) vertices and therefore run parameter \(r\).

The neighbors immediately before and after \(Y_r\) are \(y\)-negative. The
neighbors of \(Z_r\) are \(z\)-negative. For \(r\ge2\) both are in the same
ring; for \(Z_1\) the right neighbor is the first radius-two point when
\(a\ge2\). Thus every run used by the certificate is internal. Positivity of
the same threshold on a different ring does not merge the runs because the
displayed immediate neighbors are negative.

This validates the exact hypothesis needed to apply (2.1).

## 4. The outward assignment is exhaustive and has the claimed base

The assignment is:

* on radius one, send \(B_{1,0}\cup B_{1,1}\) forward to \(Y_1\), send
  \(B_{1,2}\cup B_{1,3}\) to \(Y_1\), and send
  \(B_{1,4}\cup B_{1,5}\) to \(Z_1\);
* on radius \(r\ge2\), send \(B_{r,0}\cup B_{r,1}\) backward to
  \(Z_{r-1}\), send \(B_{r,2}\cup B_{r,3}\) to \(Y_r\), and send
  \(B_{r,4}\cup B_{r,5}\) to \(Z_r\);
* charge the center by \(d_1\le D\).

These sets are disjoint and cover every middle index exactly once.

Every radius-one index pays base \(1\). At radius \(r\ge2\), the first
\(2r\) indices pay \(r-1\), while the remaining \(4r\) indices pay \(r\).
The exact base is therefore
\[
\begin{aligned}
6+\sum_{r=2}^a\{2r(r-1)+4r^2\}
&=2a^3+2a^2+2.
\end{aligned}
\tag{4.1}
\]

No assumption on the size of \(D\) is used.

## 5. Independent congestion count for the \(1/4\) theorem

Write
\[
\Delta\alpha_j=\alpha_j-\alpha_{j-1},\qquad
\Delta\beta_j=\beta_j-\beta_{j-1}
\qquad(2\le j\le M_a).
\]
Each total variation is at most \(D\).

### 5.1 Alpha charges

For an index inside a run, its alpha interval is
\((i,v+1]\). An index after a run has no alpha term. Hence:

* among the \(2r\) indices assigned to \(Y_r\), precisely the \(r+1\)
  indices in \(Y_r\) have alpha terms;
* the same holds for \(Z_r\);
* the two forward radius-one indices have alpha intervals ending at
  \(v(Y_1)+1\);
* all different \(Y_r/Z_r\) alpha unions are disjoint, except for the
  overlap of those two forward intervals with the \(Y_1\) intervals.

At \(Y_1\), the maximum multiplicity is exactly four. At any other selected
run of radius \(r\), it is at most \(r+1\). Therefore
\[
\operatorname{cong}_{\alpha}\le\max(4,a+1)\le a+2
\qquad(a\ge2),
\tag{5.1}
\]
and the total alpha charge is at most \((a+2)D\).

The \(Z_1\) alpha union may end at the first radius-two index, but the first
two radius-two side blocks are assigned backward and have no alpha term.
Thus this boundary crossing creates no omitted overlap.

### 5.2 Beta charges

For a run beginning at \(u\), every assigned index in or after it has beta
interval \([u,i]\). Thus:

* the \(Y_r\) group has maximum multiplicity \(2r\);
* the \(Z_r\) group has maximum multiplicity \(2r\);
* the first two blocks of radius \(r+1\), assigned backward to \(Z_r\), have
  maximum multiplicity \(2(r+1)\).

The \(Y_r\) beta union ends immediately before the \(Z_r\) union begins.
The backward \(Z_r\) union ends immediately before the \(Y_{r+1}\) union
begins. Consequently the sole possible double overlap is the \(Z_r\) group
with its radius-\((r+1)\) backward group. It has multiplicity
\[
2r+2(r+1)=4r+2\le4a-2
\qquad(r\le a-1).
\tag{5.2}
\]
There is no triple overlap, so the total beta charge is at most
\((4a-2)D\).

### 5.3 Summation and lower bound

Adding the base (4.1), alpha charge, beta charge, and the center's \(D\)
gives
\[
\sum_i d_i
\le2a^3+2a^2+2+(5a+1)D.
\tag{5.3}
\]

Substitution in (2.2) gives
\[
\begin{aligned}
4a^3+\frac92a^2+\frac32a-1
&\le
2a^3+2a^2+2+8aD,
\end{aligned}
\]
and hence
\[
\boxed{
D\ge
\frac{2a^3+\frac52a^2+\frac32a-3}{8a}
=\left(\frac14+o(1)\right)a^2.}
\tag{5.4}
\]

This proves the new constant. It also proves the raw numerical \(1/5\)
bound for this same order, because for integer \(D\ge1\) and \(a\ge2\),
\[
1+(5a+1)D\le7aD.
\]
The \(D=0\) branch is trivial, and \(a=1\) is covered by
\(\sum_i d_i\le7D\).

There is harmless slack in (5.1): for \(a\ge3\) the alpha congestion is
\(a+1\), giving \(5aD\), rather than \((5a+1)D\), after the center is added.
This only improves lower-order terms and does not affect the certified
leading constant \(1/4\).

## 6. Independent raster component audit

At rank \(3a\), the fixed-\(x\) row is
\[
\max(0,a-x)\le y\le\min(2a,3a-x).
\]
It has at most \(B=2a+1\) entries. Let \(e_x\) be its maximum-\(y\)
endpoint and let each row be oriented monotonically in either direction.

For \(x\le a\), the threshold for \(e_x\) is \(y\ge2a\). It contributes one
endpoint in every plateau row. Two such singleton components join only when
one row ends at its maximum and the next begins at its maximum. Since every
row is nontrivial, one endpoint cannot join across both adjacent seams.
Thus these components have size at most two.

For \(x>a\), put \(t=U_x=3a-x\). The threshold \(y\ge t\) contains \(e_x\)
and, at worst, the top two entries of row \(x-1\). It contains nothing in
row \(x+1\). The top-two segment in row \(x-1\) is separated from its other
seam by a negative entry. Hence the component through \(e_x\) has size at
most three.

Only \(e_0\) and \(e_{2a}\) can belong to boundary components. For every
other endpoint, (2.1) with run parameter at most two gives
\[
d_{e_x}\le
2+(\beta_{e_x}-\beta_{u_x-1})
+(\alpha_{v_x+1}-\alpha_{e_x}).
\tag{6.1}
\]

### 6.1 Endpoint variation congestion

The multiplicity-two assertion in the source is correct.

* On the plateau, a joined pair is one two-entry component. Charging (6.1)
  for both selected endpoints gives maximum alpha and beta multiplicity two.
  Different components are separated by a negative entry.
* On the descending side, a three-entry component occurs exactly when the
  maximum endpoint of row \(x-1\) is last and the maximum endpoint of row
  \(x\) is first. Adjacent three-entry components cannot both occur because
  their shared row endpoint would have to be both first and last. The only
  overlap with the neighboring singleton charge is the shared beta
  increment, with multiplicity two.

Thus internal alpha variation costs at most \(2D\), internal beta variation
costs at most \(2D\), and the two boundary endpoints cost at most \(2D\).
The base is at most \(2(2a-1)\). In particular the source's slightly looser
bound is valid:
\[
\sum_xd_{e_x}\le 2(2a+1)+6D.
\tag{6.2}
\]

## 7. Direct row interpolation and the \(4/19\) theorem

Assign every middle target in row \(x\) to that row's own \(e_x\).
Monotonicity alone gives
\[
d_i\le
\begin{cases}
d_{e_x}+\alpha_{e_x}-\alpha_i,&i<e_x,\\
d_{e_x}+\beta_i-\beta_{e_x},&i>e_x.
\end{cases}
\tag{7.1}
\]

All interpolation paths remain within their own row. The rows are disjoint,
each endpoint receives at most \(B\) targets, and each alpha or beta
increment is crossed by at most \(B\) paths. Hence
\[
\begin{aligned}
\sum_i d_i
&\le B\left(\sum_xd_{e_x}+2D\right)\\
&\le(2a+1)(4a+2+8D).
\end{aligned}
\tag{7.2}
\]

The constant term is
\[
(2a+1)(4a+2)=2(2a+1)^2,
\]
and the coefficient of \(D\) after adding the unselected-start term in
(2.2) is
\[
8(2a+1)+(3a-1)=19a+7.
\]
Therefore
\[
\boxed{
D\ge
\frac{V_a-2(2a+1)^2}{19a+7}
=
\frac{4a^3-\frac72a^2-\frac{13}{2}a-3}{19a+7}
=\left(\frac4{19}+o(1)\right)a^2.}
\tag{7.3}
\]

Every coefficient and numerator in the source's formula (6.9) checks.
Again, no hypothesis \(D=O(a)\) is used.

## 8. Scope and remaining qualifications

The stronger constants do not change the global status.

* The \(1/4\) theorem concerns exactly the outward enumeration
  (5.1)--(5.3). It is not a theorem for every cut, orientation, or
  permutation of complete rings; the separate arbitrary-ring theorem has
  certified leading constant \(2/15\).
* The \(4/19\) theorem requires that increasing left endpoints of the
  selected middle witnesses induce increasing \(x\), contiguous rows, and a
  monotone \(y\)-order within each row. A visual raster in an unrelated
  physical order is insufficient.
* Neither result constrains a middle order that genuinely interleaves
  radii/rows or a literal word whose selected middle witnesses do not have
  the stipulated order.
* Neither result proves that successful constructions must use a positive
  density of cross-radius corridors. That remains design guidance.
* Nothing here proves or disproves the compact balanced three-box theorem,
  DRAY, or an unrestricted quadratic lower bound for \(g_3\).

## 9. Final classification

* **New canonical/outward assignment:** accepted.
* **Alpha congestion \(\max(4,a+1)\):** accepted.
* **Beta congestion \(4a-2\):** accepted.
* **Outward sum-width bound (5.6):** accepted.
* **Leading constant \(1/4\):** accepted for the explicitly defined outward
  enumeration.
* **Raw undefined “canonical” label:** not retroactively resolved; it is now
  one stipulated interpretation.
* **Raster endpoint bound (6.4):** accepted, with four units of harmless
  base slack.
* **Direct row interpolation (6.8):** accepted.
* **Leading constant \(4/19\):** accepted under the induced-raster
  hypotheses.

The new explicit assignment and congestion proof therefore closes the
earlier mathematical objection to the \(1/5\) numerical claim for the
stipulated outward order and in fact proves \(1/4\). The direct row argument
independently and correctly improves \(4/35\) to \(4/19\).

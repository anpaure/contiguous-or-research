# Audit of the Catalan-to-promotion cross-interface theorem

Date: 2026-07-26

Audited file:
MATH_THEOREM_K_CATALAN_PROMOTION_CROSS_INTERFACE_AND_CHRONOLOGY_CUT_20260726.md.

Method: independent pure-mathematics audit. No computation, finite
search, solver, or web input is used.

## 0. Verdict

The theorem passes after the cyclic-window multiplicity correction and
the centered-chronology clarification already incorporated in the
audited file.

The following unconditional claims are valid.

1. Under a partial bijection between all but \(o(N)\) promotion roots
   and all but \(o(C_m)\) Catalan roots, the unmerged MSW component
   partition can be \((1-\eta)\)-dominant in at most

   \[
   \left(\frac{5/8}{1-\eta}+o(1)\right)W
   \]

   target stars. The unique top component has \(5/16\) in place of
   \(5/8\).

2. Under the explicit component-capacity hypothesis

   \[
   (M-1)n_\lambda\le (m+1)s_\lambda+e_\lambda,\qquad
   e_\lambda\ge0,\qquad \sum_\lambda e_\lambda=o(W),
   \]

   the component-colour error satisfies

   \[
   \operatorname{Err}(b)\ge
   \left(\frac9{32}-o(1)\right)WR.
   \]

3. Every incidence \(A\subset D\) has a literal promotion-frame witness
   obtained by restricting the primary owner row of \(D\), on either
   overlay shore.

4. The root--target incidence graph is connected. Exact incidencewise
   agreement of a root colour and the owner-component colour therefore
   forces one global fused dependency block.

5. For the natural same-owner continuation, the exact radius-\(d\)
   good-root density is

   \[
   \frac{(H)_d}{(m)_d}.
   \]

   The fixed two-shore union has depth-one density at most \(2H/m=o(1)\);
   granting both reversals changes this safe ceiling to \(4H/m=o(1)\).

6. The one-row inherited-depth spectrum is exactly
   \((L-d)_+\), with \(L\le H+1\), for the actual centered chronology.

7. Cut-only use of the unique top component needs at least
   \((5/16+o(1))W/H\) pieces. Under a separately protected
   \(2H\)-collar for every piece, the collar toll is at least
   \((5/8-o(1))W\).

The aggregate \(1/64\) Hall cut is also correct, but only under the
explicit extra hypothesis that the witness bank is simple for every
cyclic \(m\)-window. It is not an unconditional theorem about one
completed infinity-cut MSW or \(C_8\) state.

## 1. Component-mass and \(9/32\) constants

Let \(j_*\) be the first component level with
\(s_{j_*}\ge R\). The audited Catalan input says that levels
\(j\ge j_*\) carry \((5/8+o(1))C_m\) rows. Moving the threshold to
\((1-\eta)R\), for fixed \(0<\eta<3/8\), changes only \(O(1)\)
boundary levels, each of mass \(o(C_m)\). The regular-incidence identity

\[
 N\binom{m+H}{H}=WR
\]

then proves the \(5/8\) target-star bound by one double count. This
argument requires the stated partial injection/bijection; Catalan row
mass alone does not canonically colour arbitrary promotion roots.

For the stronger owner-colour theorem, delete the boundary level
\(j_*-1\), which has \(o(C_m)\) mass. The remaining deep-small
components own \((3/8-o(1))W\) targets and satisfy

\[
 s_\lambda\le\left(\frac14+o(1)\right)R.
\]

Writing \(a_\lambda=e_\lambda/(M-1)\) gives
\(\sum_\lambda a_\lambda=o(N)\) and

\[
 n_\lambda\le s_\lambda+a_\lambda.
\]

After discarding \(o(W)\) targets in colours with atypically large
\(a_\lambda\), every deep-small target has at most
\((1/4+o(1))R\) correctly coloured roots. Multiplication gives

\[
 \left(\frac38-o(1)\right)
 \left(\frac34-o(1)\right)WR
 =\left(\frac9{32}-o(1)\right)WR.
\]

No normalization or sign error is present.

## 2. Incidence lift, connectivity, and nested provenance

If \(D\) is a consecutive ambient \(m\)-block and
\(A\subset D\), deleting \(A\) leaves \(D\setminus A\) consecutive in
the restricted top order. This proves the literal incidence witness.

For connectivity, adjacent \((m-H)\)-roots have union size
\(m-H+1\le m\), so their union extends to one middle target. The
connected Johnson graph on roots therefore lifts to a connected
root--target incidence graph.

For same-owner nested provenance, rotate the primary row as

\[
 (d_1,\ldots,d_m,e_1,\ldots,e_m).
\]

In the restricted order, the centered upper radius-\(r\) member is the
terminal \(r\)-block of \(J=D\setminus A\) followed by \(D^c\).
It remains an interval of the ambient row through radius \(d\) exactly
when the oriented terminal \(d\)-block of \(D\) lies in \(J\). This
forces \(d\) labels and leaves
\(\binom{m-d}{H-d}\) choices. Two-shore inclusion--exclusion is

\[
 2\binom{m-d}{H-d}-\binom{m-u}{m-H},
\]

with infeasible binomial coefficients read as zero. The displayed
density bounds follow.

## 3. Chronology cut and multiplicity scope

For a complete promotion order \(\sigma\), write the centered owner
flag as

\[
 X_a^-(d)=I_\sigma(a+d,m-d),\qquad
 X_a^+(d)=I_\sigma(a-d,m+d).
\]

Once the middle interval is ambient-consecutive, the lower member is
automatic. The upper member exposes exactly \(d\) additional gaps
before the middle start. Hence the permitted gap interval has length
\(H-d+1\), and a row with \(L\) feasible middle phases has exact
depth-\(d\) capacity \((L-d)_+\).

If cyclic \(m\)-windows are simple across the witness bank, the phase
blocks at one root are disjoint and the conditional capacity is

\[
 MN\left(1-\frac d{H+1}\right).
\]

The derivation of

\[
 \Delta_d\ge\frac{Wd}{2(H+1)}
\]

and the summed constant \(1/64\) is correct.

The needed simplicity does not follow from exact primary ownership.
For one selected cut factor state, every nonport target occurs cyclically
in its primary-owner row and in the row primarily owning its complement.
Thus the cyclic multiplicity is two, giving only

\[
 2MN\left(1-\frac d{H+1}\right),
\]

which is shallowly vacuous. A union of several alternative factor
states may have larger multiplicity. The audited theorem states this
caveat correctly.

## 4. Exact boundary

The report proves an explicit phasewise owner-star map and rigorous
obstructions to:

* unmerged component-root control;
* same-owner nested provenance;
* the unique top component as the sole root-scale controller; and
* separately collared cut-only inheritance.

It does not rule out a global mask, a fusion of many MSW components, use
of the complement-owner mate, or a provenance-changing noncellular
multirow braid. No coefficient-one conclusion is claimed. This is the
correct implication boundary.

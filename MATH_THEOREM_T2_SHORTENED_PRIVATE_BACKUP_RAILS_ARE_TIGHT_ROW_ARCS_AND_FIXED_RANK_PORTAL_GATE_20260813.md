# Shortening the saturated T2 backup rail makes all three providers tight-row arcs

**Date:** 2026-08-13  
**Status:** unconditional local all-height theorem and exact tight-row
embedding; the applicable first-aligned trade and literal fixed-rank suffix
embedding remain explicit gates.

## 1. Data

Use the notation and the prefix masks of
`MATH_THEOREM_T2_SINGLETON_THREE_PRIVATE_BACKUP_RAILS_AND_CATALAN_FACTOR_GATE_20260813.md`.
Thus \(R_B,R_C\) are the paths `(3.1)--(3.2)` there.  Replace its saturated
path by the shortened path

\[
\begin{aligned}
R_H^{\rm sh}={}&(x_H,p_0,D_0),(x_H,p_0,D_1),
 (y_H,p_0,D_1),(z_H,p_0,D_1),(z_H,p_1,D_1),\\
& (z_H,p_1,D_2),\ldots,(z_H,p_1,D_h).
\end{aligned}                                                   \tag{1.1}
\]

It is obtained by deleting the final owner
\((z_H,p_1,D_{h+1})\) from the earlier path.

## 2. Exact support and resource counts

### Theorem 2.1

For every \(h\ge2\), the paths \(R_B,R_C,R_H^{\rm sh}\) have respectively
\(h+1,h+1,h+4\) owners.  They remain pairwise owner/lower-resource
disjoint and disjoint from the protected singleton-T2 factor for the same
three-colour choices as in the frozen rail theorem.  They provide exactly
the same \(2h-1\) ungraded casualties:

* the \(h-1\) forward \(B\)-staircase values;
* the \(h-1\) reflected \(C\)-staircase values; and
* the saturated value
  \[
  H\cup\{p_0,p_1\}\cup\mathbb Z_{2h}.
  \]

The shortened bank has

\[
                         3h+6\quad\hbox{owners},\qquad
                         3h+3\quad\hbox{selected lower facets},       \tag{2.1}
\]

and its two protected-factor exposures satisfy \(\alpha,\beta\le2\).

#### Proof

Only the last H-owner was deleted, so Johnson legality and all earlier
resource separations persist.  The base and tag unions of `(1.1)` are
still \(H\) and \(\{p_0,p_1\}\).  Its clock list contains \(D_0,D_1,
\ldots,D_h\), and \(D_0\cup D_h=\mathbb Z_{2h}\); hence its whole-path
union is the same saturated value.  The B/C support proof is unchanged.
Counting vertices and edges gives `(2.1)`.  Deleting an endpoint cannot
increase either exposure. \(\square\)

The internal coordinate words of the shortened H path are now monotone or
constant.  As before, global \(h\)-biresidence requires endpoint-compatible
collars extending every clipped endpoint run/gap; this theorem does not
assert that arbitrary closures do so.

## 3. Exact geodesic invariant

Let a simple Johnson path \(A_0,\ldots,A_s\) have constant rank \(r_0\).
If every ground coordinate changes at most once along the path, then it is
an arc of a tight cyclic-window row.  This hypothesis is equivalent to

\[
                         s=|A_0\setminus A_s|.                  \tag{3.1}
\]

Indeed, write in order

\[
 d_i=A_{i-1}\setminus A_i,qquad
 e_i=A_i\setminus A_{i-1}\quad(1\le i\le s),                  \tag{3.2}
\]

and \(C=A_0\cap A_s\).  Then the cyclic order

\[
 (d_1,\ldots,d_s, C, e_1,\ldots,e_s, O)                    \tag{3.3}
\]

has the path sets as consecutive rank-\(r_0\) windows; \(O\) is the unused
complement in arbitrary order.  Conversely, an arc of at most \(r_0\)
transitions in a tight row is geodesic exactly when it does not cross both
membership boundaries of a coordinate.  This is the only converse used
below; longer cyclic arcs need not be geodesic.

### Theorem 3.1 (three literal tight-row arcs)

Each of \(R_B,R_C,R_H^{\rm sh}\) satisfies `(3.1)` and therefore embeds
as a consecutive arc of a tight row.  Literal deletion/insertion orders are:

\[
\begin{array}{c|c|c}
&\text{deletions}&\text{insertions}\\ \hline
R_B&1,9,2,3,\ldots,h-1&0,11,h+1,h+2,\ldots,2h-2\\
R_C&\rho(1),9,\rho(2),\ldots,\rho(h-1)&
      \rho(0),11,\rho(h+1),\ldots,\rho(2h-2)\\
R_H^{\rm sh}&0_{\rm clk},8,0_{\rm base},p_0,\ 1,\ldots,h-1&
      h,9,12,p_1,\ h+1,\ldots,2h-1.
\end{array}                                                   \tag{3.4}
\]

Here numbers in the first two rows denote clock labels except the displayed
base labels \(9,11\); in the last row \(0_{\rm clk}\to h\) is the first clock
exchange, \(8\to9\) and \(0\to12\) are base exchanges, and
\(p_0\to p_1\) is the tag exchange.  Grounds are disjoint, so every label
in each deletion list and insertion list is distinct.

#### Proof

For B, the clock exchanges are
\(1\to0\), followed after the base exchange \(9\to11\) by
\(j\to h+j-1\), \(2\le j<h\).  No coordinate repeats.  Reflection gives
the C statement.  In the shortened H path the clock sequence
\(D_0,D_1,\ldots,D_h\) deletes \(0,1,\ldots,h-1\) and inserts
\(h,h+1,\ldots,2h-1\); these lists are disjoint.  Its two base exchanges and
one tag exchange use separate grounds.  Thus `(3.1)` holds in all three
cases, and `(3.3)` supplies explicit host rows. \(\square\)

The omitted last H step would exchange clock coordinate \(h\) for
clock coordinate \(0\).  Those two coordinates would each change twice,
and the path
length would exceed endpoint distance by two.  Hence that one extra owner
was exactly the obstruction to being a tight-row arc.

## 4. Fixed-rank and conformal applicability gates

Abstract row containment is not factor insertion.  For the literal T0V
family, the old suffix has \(|U(V)|=r-6\), while a rail prefix already has
rank \(h+8\).  Appending the old suffix overshoots the required owner rank
\(r+1\) by \(h+1\).  Therefore the auxiliary tag/clock labels must be
chosen inside \(U(V)\), leaving a varying core of size \(r-h-7\).
The constant-suffix disjointness proof is unavailable.

For one fixed embedded rail, `(3.3)` gives every positive tight row
containing it.  A conformal insertion in the canonical MSW factor requires
more: this pointed positive row must be one of the two positive rows of an
applicable inverse-triple trade, and the negative canonical rows must be
disjoint across all suffixes and all three rails.  The universal row
identity alone does not establish those facts.

Thus the exact remaining condition is

\[
\boxed{
\begin{gathered}
\text{choose the rail payload as a subset of each }U(V),\\
\text{complete `(3.3)` to a pointed positive first-aligned trade row},\\
\text{and select pairwise negative-row-disjoint canonical root pairs.}
\end{gathered}}                                               \tag{4.1}
\]

The explicit PBBS spine portal theorem proves `(4.1)` for its special
nested target family by constructing roots \(1100z,1010z\).  No analogous
root formula for these B/C/H staircase rails is proved here.  Arbitrary
pairwise resource-disjoint prescribed rows are not hereditarily extendable,
so this is a substantive gate rather than bookkeeping.

## 5. Finite audit

The existing H100 rail verifier was modified only in memory to stop the
H-clock sweep at \(D_h\).  For every \(2\le h\le30\) it found a
pairwise- and main-factor-disjoint triple; the counts were exactly
\((3h+6,3h+3)\), and the measured exposures were `(2,2)`.  The computation
audits the formulas; Theorems 2.1 and 3.1 are symbolic.

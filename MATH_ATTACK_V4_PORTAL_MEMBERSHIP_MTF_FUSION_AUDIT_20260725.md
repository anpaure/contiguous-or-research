# Independent audit of fourth-wave V portal membership and MTF fusion

Date: 2026-07-25

Audited report:

MATH_ATTACK_V4_PORTAL_MEMBERSHIP_MTF_FUSION_20260725.md

## Verdict

**PASS.**

The isolated-arm incompatibility, the fused depth-one membership theorem,
the constants \(4/15\), \(11/30\), and \(8\sqrt3/(5\pi)\), the
\(3W/(m+1)\) relabelling loss, the \(s-O(1)\) average membership, the
almost-every-box bound, the exact occurrence matching formula, and the
residual-depletion chronology obstruction are all valid.

The report keeps the decisive scope distinction:

* the fused word unconditionally covers the middle and rank-\((m+1)\)
  layers and supplies enough honest endpoint membership;
* it does not unconditionally cover the full Gaussian plateau family;
* high-degree occurrence flags are not promoted to distinct targets without
  the stated Hall/support hypothesis.

No hidden labelled synchronization, MWB, or mixed-factor claim occurs.

## 1. Window and V3 constants

For a window-dominant box,

\[
\Delta=r-p-q,\qquad w=(p+1)(q+1).
\]

The height windows imply

\[
\Delta\ge3\sqrt s-2.2\sqrt s=0.8\sqrt s,
\]

\[
\Delta\le3.1\sqrt s-2\sqrt s=1.1\sqrt s,
\]

and

\[
\frac{\Delta}{r}
=1-\frac{p+q}{r}
\ge1-\frac{2.2}{3}=\frac4{15}.
\]

Also

\[
\frac{\Delta}{r}
\le\frac{1.1\sqrt s}{3\sqrt s}
=\frac{11}{30}.
\]

Thus, with

\[
I_s=\sum_{\mathcal B\in\mathscr D_s}w_{\mathcal B},
\qquad
G_s=\sum_{\mathcal B\in\mathscr D_s}
\left\lceil\frac{w_{\mathcal B}\Delta_{\mathcal B}}
{r_{\mathcal B}}\right\rceil,
\]

one has exactly

\[
\frac4{15}I_s\le G_s
\le\frac{11}{30}I_s+|\mathscr D_s|.
\]

There are

\[
|\mathscr D_s|=(3\kappa_L^2\kappa_H+o(1))W_s^3
\]

boxes after taking all three high-coordinate orientations, and
\(I_s\ge s|\mathscr D_s|\).  Therefore

\[
\liminf\frac{G_s}{W}
\ge
\frac4{15}\cdot3\kappa_L^2\kappa_H
\cdot\frac{2\sqrt3}{\pi}
=\frac{8\sqrt3}{5\pi}\kappa_L^2\kappa_H.
\]

The factors are correct.

The V3 charged graph has at least \(G_s-2E\) edges on the dominant boxes.
One physical membership position supplies at most two oriented incidences
to a fixed box.  Hence

\[
2\sum_{\mathcal B}|\Pi_{\mathcal B}|\ge G_s-2E.
\]

For \(E=o(W)\), division by
\(|\mathscr D_s|=\Theta(W/s)\) gives the necessary average

\[
\left(\frac2{15}-o(1)\right)s.
\]

No factor two is missing.

## 2. Isolated-arm obstruction

Every designated interval is counted once by its left endpoint and once by
its right endpoint, so

\[
\sum_{j\in J}d_j=\sum_i s_i.
\]

For reverse-difference blocks with private starts, \(s_i\le1\), and the
number of available start positions is at most the appendage length \(Q\).
Thus the designated right-sharing excess is at most \(Q\).  Subtracting it
from

\[
\mathcal C_\partial\ge G_s-2E
\]

gives

\[
R_{\mathrm{off}}\ge G_s-2E-Q.
\]

In particular, \(E,Q=o(W)\) force \(R_{\mathrm{off}}=\Omega(W)\).
This conclusion is scoped to isolated/private starts.  It does not rule out
the later MTF fusion, where the arm positions are principal middle updates.

For fixed \(\varepsilon>0\), the isolated construction still has
\(\Theta_\varepsilon(s)\) aggregate membership per dominant box in order:
its useful incidence is \(\Omega(\varepsilon W)\), while only
\(O_\varepsilon(W/\sqrt s)\) incidences can be its one-per-endpoint middle
targets.  The incompatibility is with the exact full charged demand and with
the diagonal coefficient-one regime \(\varepsilon\to0\), not with
surface-order membership at one fixed \(\varepsilon\).

## 3. Fused depth-one theorem

The audited odd cut supplies

\[
B=\frac{W}{m+1}
\]

disjoint complementary geodesics, each with \(m+1\) middle states, and its
internal upper edge unions partition rank \(m+1\).  The canonical
radius-\(H\) lift has total length

\[
W+(2H+1)B.
\]

For \(H=\lceil A\sqrt m\rceil\), the excess is
\(O_A(W/\sqrt m)\).

For one fixed internal pair \(T\subset U\), conditional on a uniformly
relabeled upper mask \(\sigma U\), the lower mask \(\sigma T\) is uniform
among its \(m+1\) lower neighbours.  A three-chain product box containing
\(\sigma U\) has at most three such neighbours.  Hence

\[
\Pr(\sigma T,\sigma U\text{ lie in one box})
\le\frac3{m+1}.
\]

There are

\[
mB=\binom{2m}{m+1}<W
\]

internal pairs.  The expected number of bad pairs is therefore at most
\(3W/(m+1)\), and one common relabelling attains this bound.  No independence
between pairs is used.

The upper targets partition the full rank layer before and after
relabelling.  Therefore the number landing in the fixed dominant-box target
family is exactly \(I_s\), not merely an expectation.  Discarding the bad
pairs leaves at least

\[
I_s-\frac{3W}{m+1}
\]

distinct endpoints, distinct upper targets, and endpoint memberships.

Since

\[
\frac{W/(m+1)}{|\mathscr D_s|}=O(1),
\]

the average membership is at least \(s-O(1)\).  If \(b_{\mathcal B}\) is
the loss in box \(\mathcal B\), then

\[
\sum_{\mathcal B}b_{\mathcal B}=O(|\mathscr D_s|).
\]

At most \(O(|\mathscr D_s|/\sqrt s)\) boxes have
\(b_{\mathcal B}>\sqrt s\), proving the claimed almost-every-box bound.

Each retained endpoint represents its middle mask and its upper mask by
literal suffixes, and these masks lie in distinct boxes.  Thus it contributes
at least one unit of right-sharing surplus.  Finally,

\[
I_s-\frac{3W}{m+1}
-G_s
\ge
\frac{19}{30}I_s-|\mathscr D_s|-O(W/m)>0,
\]

because \(I_s=\Theta(W)\) and
\(|\mathscr D_s|+W/m=o(W)\).  The surplus domination is valid.

It remains essential that this is a membership and partial-coverage theorem.
The full plateau masks away from depths zero and one are not asserted to be
covered.

## 4. Incidence matching

An admissible genuine incidence selection must use each target at most once
and each endpoint--box cell at most once.  This is exactly a matching in the
bipartite target-versus-cell occurrence graph.  Hall deficiency gives

\[
\nu
=
\min_{X\subseteq\mathcal T}
\bigl(|\mathcal T\setminus X|+|N(X)|\bigr).
\]

If \(U\) occurrences have target repetition loss \(R_T\), deleting repeated
targets leaves \(U-R_T\) occurrences.  Deleting cell repetitions then loses
at most

\[
R_C=\sum_c(n_c-1)_+.
\]

Hence

\[
\nu\ge U-R_T-R_C.
\]

Since

\[
(n-1)_+\le\binom n2,
\]

the pair-collision relaxation \(R_C\le C\) is also valid.

The clean sufficient hypothesis is

\[
|\mathcal T(\mathcal O)|=U-R_T\ge c\,hW,
\qquad
C=o(hW),
\]

not \(R_T=o(hW)\).  The latter would be unnecessarily strong and can fail
for the unavoidable reason that a Gaussian off-middle rank has only
\((e^{-a^2}+o(1))W\) targets.  Under the stated support-size hypothesis,
(4.5) gives \(\nu=\Omega(hW)\).

If \(\nu=\Omega(hW)\) is distributed over \(W\) endpoints, the largest
\(\lceil W/h\rceil\) endpoint degrees sum to at least

\[
\frac{\lceil W/h\rceil}{W}\nu=\Omega(W).
\]

The concentrated fusion corollary is therefore correct.  The raw defect
condition is sufficient; the exact necessary-and-sufficient condition is
the displayed Hall formula, as the report states.

## 5. Chronology obstruction

For ordered source and target MTF states, the deletion-suffix formula

\[
d_{\mathrm{MTF}}^+(\Sigma,\Pi)=\max\{1,a_*\}
\]

is exact: positive last-occurrence blocks form a target prefix and the
undeleted source blocks form the target suffix, while cumulative target
prefix updates realize equality.

Under \(m-H\ge2\), a depleted canonical source cannot leave a target suffix
of at least two blocks ending in an \((m-H)\)-residual.  The only source
block of that size is its first block, which cannot remain as the last block
of a nontrivial suffix.  Thus every bridge to a fresh state has length at
least \(2H+1\).

The first initialization contributes \(2H+1\) excess positions.  Every
later bridge may use its last update as the next first owner position, so
its excess is at least \(2H\), not \(2H+1\).  Therefore

\[
(2H+1)+2H(K-1)
\]

is the correct total lower bound.  In particular,
\(K=\Theta(W/H)\) costs \(\Theta(W)\), while \(o(W)\) excess requires
\(K=o(W/H)\).

The odd-factor construction has

\[
K=\frac{W}{m+1}=o(W/H)
\]

and \(m+1\gg H\) owners per component at Gaussian depth.  It correctly
escapes the obstruction.

## 6. Final classification

### Valid

* isolated appendages fail the full surface-membership demand at \(o(W)\)
  length;
* the fused depth-one MTF selection satisfies that membership demand with
  average \(s-O(1)\);
* the occurrence matching theorem is exact;
* fresh residual-consuming short components have linear total reset cost at
  the sharp portal count.

### Conditional, not proved

* a deep central-band occurrence graph with matching number
  \(\Omega(HW)\);
* \(\Theta(W/\sqrt m)\) genuine degree-\(\Theta(\sqrt m)\) portals in the
  unconditional odd-factor word;
* full Gaussian-window coverage or a coefficient-one universal word.

The report's final conclusion is therefore correctly scoped: surface
membership and literal MTF chronology are solved, whereas deep distinct
support remains open.

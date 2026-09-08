# Independent audit of the early-scale `D_4/H_4` statewise hinge

Date: 2026-07-26

Audited source:
`MATH_ATTACK_K_H4_D4_EARLY_SCALE_STATEWISE_HINGE_20260726.md`.

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

The main theorem passes.  For the canonical early parent, the loads on
local targets `2,...,8` are

\[
 (C_s,C_{s-1},C_{s-1},2C_{s-2},2C_{s-2},
                         5C_{s-3},5C_{s-3}).           \tag{0.1}
\]

For

\[
 h=(2\ 3)^\alpha(4\ 5)^\beta(6\ 7)^\gamma,
\]

the complete six-open-start difference `hG-F` is

\[
 2(1-\alpha)e_2+(-3+2\alpha)e_3
 +(-3+4\gamma)e_6+4(1-\gamma)e_7.                    \tag{0.2}
\]

The `beta` bit is invisible.  With cap relief defined as old hinge minus
new hinge, the maximum over all eight states is exactly zero.  Four states
lose two units and four are neutral for `s>=5`; the stated finite `s=4`
correction is also exact.  The result remains zero when
`p-C_(s-1)=O(1)`.

The complementary three starts have difference `-(0.2)`.  Common physical
carriers therefore cancel pointwise before the hinge is applied.  Even if
the two sectors are put on disjoint copies of the same canonical load
vector, their combined new-minus-old hinge is nonnegative, with a neutral
state.  Unequal carrier backgrounds remain outside the theorem.

The direct `F/G` ownership overlay is connected.  Hence it has no proper
ownership-component subtrade.  This conclusion is correctly limited to
the direct two-factor overlay.

## 1. Canonical-load audit

In a size-`s+1` parent, first-return splitting gives

\[
                         w_j=C_{j-1}C_{s+1-j}.         \tag{1.1}
\]

Targets `2j-1` and `2j` carry the two boundary copies of `w_j`.  Taking
`j=1,2,3,4` proves (0.1).

Minimality of `s` gives `C_(s-1)<p<=C_s`.  The exact differences

\[
 C_{s-1}-2C_{s-2}={2(s-3)\over s}C_{s-2},             \tag{1.2}
\]

\[
 C_{s-1}-5C_{s-3}
 ={(s-4)(11s-15)\over s(s-1)}C_{s-3}                 \tag{1.3}
\]

show that every displayed target except `2` is strictly below cap for
`s>=4`.  They also prove

\[
 2C_{s-2}+1\le p,\qquad5C_{s-3}+4\le p\quad(s\ge5).\tag{1.4}
\]

Thus the report includes the collar and background classes rather than
testing only the `C_s` spike.

## 2. Eight-state profile audit

The audited local histograms are

\[
 u_F=(9,9,12,12,12,12,9,9),
 \quad
 u_G=(9,11,9,12,12,9,13,9).                          \tag{2.1}
\]

The `H_4` action preserves the port family and relabels this histogram.
Subtracting `u_F` gives four profiles, each twice:

\[
\begin{array}{c|c}
(\alpha,\gamma)&u_{hG}-u_F\\ \hline
(0,0)&2e_2-3e_3-3e_6+4e_7\\
(0,1)&2e_2-3e_3+e_6\\
(1,0)&-e_3-3e_6+4e_7\\
(1,1)&-e_3+e_6.
\end{array}                                             \tag{2.2}
\]

This is (0.2).  In particular every state keeps or increases the load at
the only target which can meet cap.

## 3. Hinge audit

Put

\[
 R=C_s-p,\qquad A=p-C_{s-1},\qquad
 B=p-2C_{s-2},\qquad C=p-5C_{s-3}.                   \tag{3.1}
\]

For the open sector the exact new-minus-old hinge is

\[
 \Xi_U=2(1-\alpha)+(1-\gamma)(4-C)_+.                 \tag{3.2}
\]

For `s>=5`, the final positive part vanishes.  At `s=4` it is
`(9-p)_+`.  Hence old-minus-new relief is never positive and is zero for
`alpha=gamma=1`.

If the state is repeated on `N` common-carrier suffix packets, the audited
normalization is

\[
 \Xi_U(N)=2N(1-\alpha)
 +(1-\gamma)(5C_{s-3}+4N-p)_+
 +\gamma(2C_{s-2}+N-p)_+.                            \tag{3.2a}
\]

For the natural prefix bank `N=C_(s-4)`, the latter two hinges vanish for
`s>=5`, by

\[
 2C_{s-2}+C_{s-4}\le C_{s-1},\qquad
 5C_{s-3}+4C_{s-4}\le C_{s-1}.                       \tag{3.2b}
\]

Thus its exact best relief is also zero.

On a disjoint complementary carrier with the same canonical preload,

\[
 \Xi_V=-\min\{2(1-\alpha),R\}
 +(3-2\alpha-A)_++(1-\gamma)(3-B)_+.                  \tag{3.3}
\]

Adding (3.2)--(3.3) gives a sum of nonnegative terms exactly as stated in
the source report.  With common carriers, the stronger identity
`Delta_U+Delta_V=0` makes the full gain identically zero for every
background.

This physical hinge calculation is conditional on the parent atlas pushing
the six-start aggregate into the same carrier-labelled target slice as the
Catalan vector (0.1).  The boundary Catalan census by itself counts two
distinguished boundary families and does not prove that alignment.  For
row/start-dependent carriers, only the occurrence-resolved tensor is
authoritative; the aggregate formula is an algebraic common-carrier
projection.

## 4. Direct-overlay audit

The thirteen shared `X` states listed in the source were checked against
the canonical `q_F` words and the displayed `G` paths.  They connect all
fourteen roots and have no repeated root-pair edge.  For example,

\[
 1236\xleftrightarrow{1238}1234,\quad
 1236\xleftrightarrow{1267}1247,\quad
 1247\xleftrightarrow{1567}1256,\quad
 1247\xleftrightarrow{2347}1347,
\]

and the remaining listed edges attach every other root.  After contracting
the identical root-port ties, this connected `X` suboverlay forces one
shore bit on all fourteen rows.  Adding `Y` edges cannot disconnect it.

This proves only that the direct `F/G` overlay is indivisible.  It does not
exclude a subtrade involving the third exact factor `H`, another conjugate,
a recomputed multi-factor overlay, or disjoint contextual copies.  The
source report now states this qualification correctly.

## 5. Multi-state-factor audit

The second exact factor `H` has first-insertion vector

\[
 (8,8,8,6,8,8,6,3,4,2,2,2,4,2)                     \tag{5.1}
\]

and six-open-start histogram

\[
 u_H=(9,10,12,11,12,11,10,9).                        \tag{5.2}
\]

Thus `u_H-u_F=e_2-e_4-e_6+e_7`, whose canonical open-sector hinge cost is
one.  The row `1256` has labels `4,3,7` under `F,H,G`, so a literal local
ternary label and the stated `3 by 2`/`3 by 3` rectangles are real.  The
other rows change simultaneously, and their carrier profiles are not
optional.  The source correctly does not promote this marked-row witness
to an all-occurrence routing theorem.

The reported smaller `F/H` components also check: their nonzero open
profiles are `e_3-e_4` and `e_2-e_3-e_6+e_7`.  The latter is the active
three-row ternary component and still has target-`2` coefficient `+1` (or
`+1,+2` after the possible `H_4` reanchoring), so fragmentation does not
create cap relief.

## 6. Audited boundary

The exact proved conclusion is

\[
 \boxed{\max_{h\in H_4}\text{(canonical six-open-start cap relief)}=0.}
\]

This closes the forward `H_4` conjugate singleton architecture.  It does
not close higher local interval lengths `2,3,6,7`, unequal carrier
backgrounds, or a genuinely new parent-aligned factor which decreases the
open load at target `2`.

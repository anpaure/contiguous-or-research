# The three PBBS height-residual chains have an explicit two-rail protected realization

**Date:** 2026-08-05  
**Method:** two literal Johnson paths and the small protected-factor theorem;
no search or computation  
**Status:** unconditional target-support and owner/`q1` host theorem.  The
three endpoint chains left by the monotone plus `E4` height rails fit on two
owner-disjoint Johnson paths of total `O(H)` size, with every replacement at
the original width.  Their incidence lift extends to a spanning
Middle-Levels two-factor whenever `4H-4<=r-1`.  Correlated upper decoration,
PBBS-relative retention, residence, and the typed cap are not consequences
of that abstract extension.

## 1. Residual targets

Put `n=2r+1` and

\[
 T_b=\{2b+1,2b+3,\ldots,2r-1\}.                        \tag{1.1}
\]

The exact `E4` theorem leaves, for every `b`, only

\[
 X_b^{23}=\{2,3\}\cup T_b,
 \qquad
 X_b^3=\{3\}\cup T_b,
 \qquad
 X_b^2=\{2\}\cup T_b.                                  \tag{1.2}
\]

Their old widths are respectively

\[
                         b-2,\qquad b-1,\qquad b-1.      \tag{1.3}
\]

The issue is not their number: each superscript is a nested chain.  The
issue is that `X_b^2` and `X_b^3` are incomparable and cannot both arise as
nested prefix intersections on one fixed terminal ray.  Two rails are
enough.

## 2. The first rail supplies `X^(23)` and `X^3`

For `b>=3`, retain the mountain states

\[
 A_b=[1,b]\cup T_b.                                    \tag{2.1}
\]

Define two rank-`r` cap states

\[
 E=\{2,3,5\}\cup T_3,
 \qquad
 C=\{3,4,5\}\cup T_3.                                  \tag{2.2}
\]

Then

\[
                         C-E-A_3-A_4-\cdots-A_H          \tag{2.3}
\]

is a simple Johnson path: `C--E` exchanges `4` for `2`, `E--A_3`
exchanges `5` for `1`, and every `A_b--A_(b+1)` exchanges `2b+1` for
`b+1`.

The height-window identity is

\[
                         \bigcap_{j=3}^{b}A_j
                         =\{1,2,3\}\cup T_b.             \tag{2.4}
\]

Therefore

\[
 E\cap\bigcap_{j=3}^{b}A_j=X_b^{23},                   \tag{2.5}
\]

and

\[
 C\cap E\cap\bigcap_{j=3}^{b}A_j=X_b^3.               \tag{2.6}
\]

The path in (2.5) has `b-1` owners and hence width `b-2`; the path in
(2.6) has `b` owners and hence width `b-1`.  These are exactly (1.3).

## 3. The second rail supplies `X^2`

Put

\[
 A'_b=A_b-\{1\}+\{0\}
     =\{0\}\cup[2,b]\cup T_b,                           \tag{3.1}
\]

and define

\[
 F=\{0,2,5\}\cup T_3,
 \qquad
 K=\{2,4,5\}\cup T_3.                                  \tag{3.2}
\]

Then

\[
                         K-F-A'_3-A'_4-\cdots-A'_H       \tag{3.3}
\]

is a simple Johnson path.  Its first two exchanges are `4 -> 0` and
`5 -> 3`; the remaining exchanges are the common images of the mountain
exchanges under the fixed swap `1 -> 0`.

Moreover,

\[
                         \bigcap_{j=3}^{b}A'_j
                         =\{0,2,3\}\cup T_b,             \tag{3.4}
\]

so

\[
 K\cap F\cap\bigcap_{j=3}^{b}A'_j
                         =X_b^2.                         \tag{3.5}
\]

The path in (3.5) has `b` owners and width `b-1`, again exactly the old
width.

## 4. Owner and lower-colour disjointness

The two paths (2.3) and (3.3) are owner-disjoint.

* Every `A'_b` contains `0`, while every `A_b,C,E,K` omits `0`.
* The only second-rail cap containing no `0` is `K`; it omits `1,3` and is
  visibly distinct from all first-rail owners.
* The remaining cap states are distinguished by their intersections with
  `{0,1,2,3,4,5}`.

For the physical lift one must compare the **unions** of adjacent
rank-`r` complement states, because the lower physical facet is the
complement of that union.  On the first rail the union colours are

\[
 \{2,3,4,5\}\cup T_3,
 \quad
 \{1,2,3,5\}\cup T_3,
 \quad
 [1,b+1]\cup T_b\quad(3<=b<H).                          \tag{4.1}
\]

On the second rail they are

\[
 \{0,2,4,5\}\cup T_3,
 \quad
 \{0,2,3,5\}\cup T_3,
 \quad
 \{0\}\cup[2,b+1]\cup T_b\quad(3<=b<H).               \tag{4.2}
\]

The moving families in (4.1) contain `1` and omit `0`; those in (4.2)
contain `0` and omit `1`.  The four cap colours are pairwise distinct.
Thus the alternating lift of the two paths to the Middle-Levels incidence
graph is simple and 2-bounded.

## 5. Protected host consequence

Each rail has `H-1` Johnson edges, so their alternating incidence lift has

\[
                         4H-4                            \tag{5.1}
\]

incidence edges.  The small protected-factor theorem on
`ML_(r+1)` says that every 2-bounded protected bank of at most

\[
                         (r+1)-2=r-1                     \tag{5.2}
\]

incidences extends to a spanning two-factor.  Hence:

### Theorem 5.1 (two-rail protected host)

If

\[
                         4H-4\le r-1,                    \tag{5.3}
\]

there exists a spanning Middle-Levels owner/`q1` two-factor containing
both complete rails (2.3) and (3.3).  In that factor every residual target
in (1.2), and therefore its complementary physical upper target, has a
target-equal occurrence at the old width.

Since the intended ladder height is `H=O(d)=O(sqrt(r))`, condition (5.3)
holds for all sufficiently large `r`.

## 6. What this closes and what it does not

This theorem removes the **support-size** objection to the last three
height residuals:

\[
 \boxed{
 3H\text{ named leftovers}
 \quad\longrightarrow\quad
 2\text{ protected rays of total size }O(H).}
\]

It also proves that owner and immediate-lower capacities do not obstruct
planting those rays.

It does not prove that an arbitrary two-factor extension:

1. retains the PBBS-relative pentagon bodies outside the two rails;
2. is upper-`q1` exact or has the required component count;
3. has a common resident source antecedent;
4. transports the occurrence-labelled typed cap; or
5. contains the quiet opening path.

Thus the remaining synthesis problem is now a **correlated protected host**
problem, not a target-support or local-cap problem.  Any host theorem which
contains the monotone/`E4` PBBS subsystem and these two rails simultaneously
closes the complete forced-edge upper fan up to the single bounded top and
bottom exceptions already identified.

## 7. Dependencies

Used:

* `MATH_THEOREM_PBBS_HEIGHT_E4_REFLECTED_RAIL_LEAVES_THREE_ENDPOINTS_PER_HEIGHT_20260805.md`;
* `MATH_THEOREM_PBBS_HEIGHT_SEAM_FAN_CALCULUS_AND_MIDDLE_INTERVAL_RESIDUAL_20260805.md`;
* the small protected Middle-Levels two-factor theorem recorded in
  `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.

No probabilistic packing or multiplicity estimate is used.

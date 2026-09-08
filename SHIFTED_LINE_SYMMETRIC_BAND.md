# A shifted line spine covers a symmetric sublinear band

## 1. Result

Put

\[
 P_m=[0,m]^4,\qquad L_s=\{x\in P_m:|x|=s\},\qquad
 M_m=|L_{2m}|.
\]

The direct line construction need not be placed immediately below the
middle layer.  Shifting it downward converts its longer windows into lower
*and* upper central coverage at once.

### Theorem 1 (shifted symmetric band)

For integers `m>=2` and `0<=q<=m-1`, there is a nonzero word of length at
most

\[
 M_m+4q(m+1)(2m+1)                                 \tag{1.1}
\]

whose contiguous coordinatewise maxima contain every point in the ranks

\[
             2m-1-q,\ 2m-q,\ldots,\ 2m-1+q.       \tag{1.2}
\]

Consequently, if `q=o(m)`, this whole two-sided band has a word of length

\[
                         M_m+o(m^3).                \tag{1.3}
\]

This is a band theorem, not a full four-box theorem.  Linear-depth tails
remain uncovered when `q=o(m)`.

## 2. Shifted line spine

Set

\[
                         R=2m-1-q.                  \tag{2.1}
\]

For every fixed transverse pair `(c,d)`, list the complete rank-`R`
coordinate-`{1,2}` line

\[
 (L,K-L,c,d),(L+1,K-L-1,c,d),\ldots,(U,K-U,c,d),   \tag{2.2}
\]

where

\[
 K=R-c-d,\qquad L=\max(0,K-m),\qquad U=\min(m,K).
\]

Concatenate all nonempty lines.  This lists every point of `L_R` exactly
once, so the spine has length

\[
                         |L_R|\le M_m.               \tag{2.3}
\]

The inequality is unimodality of the rank numbers of the symmetric box.
There is no need for the direct-line theorem's literal rank-`R+1` tail:
the slice fan below covers exactly the targets for which the line criterion
fails.

An interval from line parameters `p` through `r` has maximum

\[
                         (r,K-p,c,d).                \tag{2.5}
\]

It follows exactly as in the direct-line theorem that a target `y` of rank

\[
                         |y|=R+s                    \tag{2.6}
\]

occurs inside its transverse line if and only if

\[
                         y_1\ge s,\qquad y_2\ge s.  \tag{2.7}
\]

## 3. Boundary slices

Append, for every integer `a=0,...,2q-1`,

* a universal three-chain word in the slice `x_1=a`, and
* a universal three-chain word in the slice `x_2=a`.

The standard three-chain hook word has length at most

\[
                         G_m=(m+1)(2m+1)             \tag{3.1}
\]

after the fixed coordinate is attached to every entry.  When the fixed
coordinate is zero, the all-zero local target is irrelevant here because
every rank in (1.2) is positive.  Hence all appended slices cost at most

\[
                         4qG_m.                      \tag{3.2}
\]

Let `y` have any rank in (1.2).  Then `|y|=R+s` for some
`0<=s<=2q`.  If both inequalities (2.7) hold, the shifted line spine covers
`y`.  Otherwise, one of `y_1,y_2` is an integer in

\[
                         \{0,1,\ldots,s-1\}
             \subseteq \{0,1,\ldots,2q-1\}.         \tag{3.3}
\]

The corresponding fixed-coordinate slice word covers `y`.  Thus every
target in (1.2) occurs.  Equations (2.3) and (3.2) prove (1.1), and
`M_m=Theta(m^3)` proves (1.3).

If `2q>m+1`, nonexistent slices may simply be omitted; the stated bound
remains valid.  The restriction `q<=m-1` only keeps the bottom rank in
(1.2) positive and the shifted spine in the upper half where the inherited
presentation is clean.

## 4. Significance and limitation

The earlier shallow-band theorem began at rank `2m-1` and extended only
upward.  The shift shows that no separate erosion or pinning theorem is
needed for any sublinear **symmetric** band: the same physical line windows
serve its lower and upper sides.

This does not yet prove the Boolean constant-one conjecture through the
fixed-dimensional chain-box aggregation.  Typical chain boxes arising from
a fixed block decomposition have total side length of order `sqrt(k)`, the
same order as the global concentration window.  Covering only
`q=o(m)` local depths therefore does not cover those boxes completely.  A
full four-box theorem still needs either linear-depth line splicing or a
higher-dimensional aggregation that amortizes the remaining tails.

# Affine-opposite wreath GK phases are an exact circular-gap profile

**Status (2026-08-21).**  This note gives an exact formula for every
GK-orientation phase in an affine-opposite genuine wreath pair.  All physical
phase antidiagonals are monochromatic.  Their colors are the jump word of the
minimum occupancy of a circular interval, equivalently the maximum-span word
of the circular gaps of one arithmetic half-orbit.

This strictly extends the standard/reverse calculation, but it does not prove
that the resulting color word has a linear disagreement with the persistent
almost-alternating word.  That final one-dimensional statement is left as an
explicit number-theoretic gate.

## 1. Affine-opposite physical orders

Let

\[
                    b=2r+1\ge5,\qquad (a,b)=1,           \tag{1.1}
\]

and identify the fixed GK coordinate labels with `Z_b`.  Constants added to
either order only shift counters, so take

\[
             \alpha_i=ai,\qquad \beta_i=-ai
             \quad(i\in\mathbb Z_b).                    \tag{1.2}
\]

Let `X_i` be the rank-`r` window of `alpha` ending at counter `i`, and let
`Y_j` be the rank-`r+1` window of `beta` ending at counter `j`.  Put
`Z_j=Z_b\setminus Y_j`.  Directly from (1.2),

\[
 \begin{aligned}
 X_i&=ai+a\{-r+1,\ldots,0\},\\
 Z_j&=-aj+a\{-r,\ldots,-1\}.
 \end{aligned}                                         \tag{1.3}
\]

On physical phase `p`, where `j=p-i`, this becomes

\[
              Z_{p-i}=X_i-a(p+1).                       \tag{1.4}
\]

Thus increasing `i` translates both sets by `a`.  Translation of the fixed
coordinate labels cyclically rotates the interleaved balanced word by an even
number of positions.  It can change the depth of the anchored minimum by an
even integer, but not its parity.  Consequently every physical phase is
GK-orientation monochromatic.

It remains to compute the color for one pair `(X,X+t)`, where

\[
                 X=\{0,a,2a,\ldots,(r-1)a\}.            \tag{1.5}
\]

The harmless simultaneous translation taking the set in (1.3) to (1.5)
does not change the orientation.  Under that translation, phase `p` has

\[
                         t_p=-a(p+1).                    \tag{1.6}
\]

## 2. Prefix minima are minimum circular occupancies

Write

\[
 x_q=2{\bf1}_{q\in X}-1,
 \qquad
 P(s)=\sum_{q=0}^{s-1}x_q,\qquad P(s+b)=P(s)-1.         \tag{2.1}
\]

For `0<=t<=b-1`, define the minimum signed weight of a circular coordinate
interval of length `t` by

\[
 L_t=\min_u\sum_{q=0}^{t-1}x_{u+q}
     =\min_u\bigl(P(u+t)-P(u)\bigr).                    \tag{2.2}
\]

### Lemma 2.1 (exact phase-color derivative)

For the middle source `(X,Y)` with `Y=Z_b\setminus(X+t)`, the minimum over
even interleaved prefixes is

\[
                         P(-t)+L_t,                     \tag{2.3}
\]

and the minimum over odd prefixes, immediately after an `A` coordinate, is

\[
                         P(-t)+L_{t+1}.                 \tag{2.4}
\]

Hence

\[
 \boxed{\quad
  (X,Z_b\setminus(X+t))\text{ is }A\text{-first}
  \iff L_{t+1}-L_t=-1.\quad}                            \tag{2.5}
\]

It is `B`-first exactly when the difference in (2.5) is `+1`.

#### Proof

The `B`-sign at coordinate `q` is `-x_(q-t)`.  After `s` complete
coordinate pairs, the interleaved prefix height is

\[
 P(s)-P(s-t)+P(-t).                                    \tag{2.6}
\]

Minimizing over `s` gives (2.3), because the first two terms are the signed
weight of a length-`t` circular interval.  Immediately after the next `A`
coordinate the height is

\[
 P(s+1)-P(s-t)+P(-t),                                  \tag{2.7}
\]

whose minimum is (2.4).  Extending an interval by one coordinate changes its
signed weight by one, and deleting one endpoint from a minimizing
length-`t+1` interval gives the reverse bound.  Thus
`L_(t+1)-L_t` is exactly `-1` or `+1`.  The odd prefix wins precisely in the
first case, which is the `A`-first orientation.  \(\square\)

Let

\[
        n_t=\min\{|X\cap I|:I\text{ is a circular interval of length }t\}.
                                                                  \tag{2.8}
\]

Then `L_t=2n_t-t`.  Therefore (2.5) says that the color is `A` when
`n_(t+1)=n_t`, and is `B` when the minimum occupancy increases by one.

## 3. The equivalent circular-gap maximum formula

List `X` in increasing fixed-coordinate order as

\[
             0\le u_0<u_1<\cdots<u_{r-1}<b             \tag{3.1}
\]

and put

\[
       g_i=u_{i+1}-u_i\pmod b\in\{1,\ldots,b-1\},
       \qquad \sum_i g_i=b.                            \tag{3.2}
\]

For `1<=m<=r`, define the maximum span of `m` consecutive circular gaps

\[
                  T_m=\max_i\sum_{q=0}^{m-1}g_{i+q}.   \tag{3.3}
\]

### Theorem 3.1 (exact affine phase word)

The `B`-first relative translations are exactly

\[
                  \boxed{\{T_m-1:1\le m\le r\}}.       \tag{3.4}
\]

Consequently physical phase `p` is `B`-first exactly when

\[
             -a(p+1)\equiv T_m-1\pmod b               \tag{3.5}
\]

for some `m`; every other phase is `A`-first.  The values `T_m` are strictly
increasing and `T_r=b`, so (3.4) has exactly `r` elements.  Thus the affine
phase word has exactly `r` `B` phases and `r+1` `A` phases, as required by
the orientation-biregularity identity.

#### Proof

A circular interval containing at most `m-1` points of `X` may start just
after some `u_i` and end just before `u_(i+m)`.  Its greatest possible
length is

\[
               \max_i(u_{i+m}-u_i\pmod b)-1=T_m-1.     \tag{3.6}
\]

Hence the minimum occupancy `n_t` first reaches `m` at `t=T_m`; equivalently
`n_(t+1)-n_t=1` exactly for `t=T_m-1`.  Lemma 2.1 gives (3.4), and (1.6)
gives (3.5).  Since all gaps are positive, extending a maximizing `m`-gap
block by its next gap proves `T_(m+1)>T_m`; summing all gaps gives `T_r=b`.
\(\square\)

## 4. Exact remaining scope

Theorem 3.1 settles orientation monochromaticity and gives every color for
every affine-opposite multiplier.  To turn this affine family into the
persistent compiler, one would still need its phase word to agree with a
one-defect alternating cyclic word on `b-o(b)` positions.  Conversely, a
uniform linear-disagreement bound for the maximum-span words (3.3)--(3.5)
would rule out the whole affine-opposite family, but not arbitrary non-affine
order pairs.

Finite H100 enumeration finds no alternating cyclic run of length four in
these affine phase words for every coprime multiplier and every odd
`5<=b<=101`.  This is a diagnostic, not a theorem in this note.

## 5. H100 audit

The checker

`scratch/audit_affine_opposite_wreath_gk_gap_profile_20260821.py`

constructs the literal interleaved sources, verifies (1.3)--(1.6), compares
their orientations with both the occupancy derivative (2.5) and the gap
formula (3.4)--(3.5), checks the exact `r/(r+1)` color counts, and separately
records the finite no-four-alternation diagnostic.

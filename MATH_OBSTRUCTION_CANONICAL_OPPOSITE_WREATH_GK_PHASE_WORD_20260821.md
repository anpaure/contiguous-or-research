# The canonical opposite-order wreath has a two-run GK phase word

**Status (2026-08-21).**  The scoped obstruction below is proved.  Pairing
the standard cyclic order on one block with the reverse cyclic order on the
other makes every physical phase antidiagonal GK-orientation monochromatic,
but its phase-orientation word is one `B` run followed by one `A` run.  It
therefore agrees with the persistent alternating half-step phase word on at
most about half the phases.  This canonical product atom cannot compile the
`b-O(H)` phase diagonals used by integral GK retirement when `H=o(b)`.

The theorem does not cover arbitrary pairs of cyclic orders.  Such pairs
usually have nonmonochromatic phase antidiagonals, but no asymptotic theorem
here rules out a specially correlated family with `b-o(b)` correctly
monochromatic phases.

## 1. Exact phase word

Put `b=2r+1` and identify both local label indices with `Z_b`.  Take

\[
 \alpha=(0,1,\ldots,2r),\qquad
 \beta=(0,2r,2r-1,\ldots,1).                              \tag{1.1}
\]

Let `X_i` be the rank-`r` window of `alpha` ending at counter `i`, and let
`Y_j` be the rank-`r+1` window of `beta` ending at counter `j`.  In the
two-block torus atom, physical phase `p` consists of the antidiagonal

\[
                  \{(X_i,Y_{p-i}):i\in\mathbb Z_b\}.       \tag{1.2}
\]

Simultaneously increasing `i` translates both label sets by one in the
fixed interleaved coordinate order.  This rotates the balanced zero--one
word by two coordinates, so it preserves the parity of its minimum depth.
Thus every antidiagonal in (1.2) has one common GK orientation.

### Lemma 1.1 (literal top-excess formula)

Let `k_p` be the top excess of the GK chain through `(X_0,Y_p)`.  Then

\[
 k_p=
 \begin{cases}
   2p,&0\le p<r,\\
   2r-1,&p=r,\\
   2(2r-p)+1,&r+1\le p\le2r.
 \end{cases}                                               \tag{1.3}
\]

Consequently the monochromatic phase-orientation word, with odd top excess
called `A`, is

\[
                         \boxed{B^rA^{r+1}}                 \tag{1.4}
\]

up to cyclic shift and simultaneous exchange of the block names.

#### Proof

For the representative in (1.2),

\[
 X_0=\{-r+1,-r+2,\ldots,0\},\qquad
 Y_p=\{-p,-p+1,\ldots,r-p\}                               \tag{1.5}
\]

in `Z_b`.  Scan their membership bits in the fixed interleaved order
`A_0,B_0,A_1,B_1,...`.  The minimum after complete `A,B` pairs and the
minimum immediately after an `A` coordinate are respectively

\[
\begin{array}{c|c|c}
 p& E_p&O_p\\ \hline
 0\le p<r&-2p&1-2p\\
 p=r&2-2r&1-2r\\
 r+1\le p\le2r&-2(2r-p)&-2(2r-p)-1.
\end{array}                                                \tag{1.6}
\]

This table follows directly by splitting the scan at the four endpoints
of the two cyclic intervals in (1.5); between endpoints the pair-prefix
height has slope `-2`, `0`, or `2`.  Taking
`k_p=-min(E_p,O_p)` gives (1.3).  Its parity gives (1.4).  \(\square\)

The longest alternating cyclic subword of (1.4) has length two for `r>=2`.

## 2. Incompatibility with the persistent half-step phases

At the central split, the half-step type word has exactly one equal-letter
cyclic edge and every other edge alternates.  More generally, let `tau` be
any odd cyclic binary word with that property.

### Lemma 2.1 (two runs versus an almost alternating word)

For every relative cyclic shift,

\[
  |\{p:(B^rA^{r+1})_p=\tau_p\}|\le {b+3\over2}.            \tag{2.1}
\]

#### Proof

On a constant run of length `ell`, an alternating word contains at most
`ceil(ell/2)` copies of either prescribed bit.  The unique equal edge of
`tau` can improve this bound in at most one of the two runs, and by at most
one.  Therefore the agreement is at most

\[
 \left\lceil{r\over2}\right\rceil
 +\left\lceil{r+1\over2}\right\rceil+1
 ={b+3\over2}.                                             \tag{2.2}
\]

\(\square\)

For the half-step schedule, `d_r=1`, so the integral GK retirement theorem
uses

\[
 n=\left\lfloor{b-H+1\over2}\right\rfloor                \tag{2.3}
\]

full phase diagonals of each orientation.  It therefore needs `2n=b-O(H)`
correctly oriented phase diagonals in every fully compiled atom.  Lemma 2.1
supplies at most `(b+3)/2`.  Hence the canonical opposite-order atom has
phase-diagonal shortfall

\[
                    2n-{b+3\over2}={bover2}-O(H),          \tag{2.4}
\]

which is positive and linear for `H=o(b)`.

### Theorem 2.2 (scoped compiler no-go)

The standard/reverse wreath pairing (1.1), and any version obtained by
cyclically shifting the orders or exchanging the two block names, cannot
realize the longest-top integral GK phase selection with `o(b)` missing
phase diagonals when `H=o(b)`.  In particular, making every phase diagonal
monochromatic by this canonical opposite-order trick is incompatible with
the persistent alternating physical schedule.

This is a phase-capacity statement for the specified atom family.  It does
not preclude partial diagonal use, a non-GK chain assignment, atom-dependent
changes of coordinate order, or a different cyclic-order pairing.

## 3. H100 audit

The checker
`scratch/audit_canonical_opposite_wreath_gk_phase_word_20260821.py`
constructs all `b^2` sources literally for every odd `5<=b<=101`, verifies
antidiagonal monochromaticity and (1.3), measures the longest alternating
cyclic run, constructs the half-step word, exhausts every relative shift,
and checks (2.1)--(2.4) whenever the displayed shortfall is positive.

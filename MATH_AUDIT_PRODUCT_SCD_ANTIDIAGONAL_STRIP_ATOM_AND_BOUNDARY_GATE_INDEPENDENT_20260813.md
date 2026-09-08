# Independent audit of the product-SCD antidiagonal-strip theorem

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_PRODUCT_SCD_ANTIDIAGONAL_STRIP_ATOM_AND_BOUNDARY_GATE_20260813.md`  
**Source SHA-256:**
`ca9465999ae3cf4b597179e4ce485ef99e190f6a9d65112797c960396229bcc4`  
**Audited verifier:** `verify_product_scd_antidiagonal_strip_atlas.py`  
**Verifier SHA-256:**
`0e0af22655db1aa5c063bb23e7ecf97f388b83794f41fd7ea9131108e44ccebb`  
**Verdict:** PASS with no mathematical correction required.

## 1. The antidiagonal atom

For `Z_t=C_t union D_(s-t)`, monotonicity on the two disjoint coordinate
alphabets gives

\[
 \bigcup_{t=x}^{y}Z_t=C_y\cup D_{s-x}.
\]

Its rank is `u+v+s+y-x`, and consecutive letters lose exactly
`d_(s-t)` and gain exactly `c_(t+1)`.  The index hypotheses ensure these
increments exist on every asserted edge.  Strictness of both saturated
chains makes the two interval endpoints recoverable from the value, so the
distinctness assertion is exact.

## 2. The covered triangle and boundary wedges

An interval `[x,y]` of `W_q` maps to

\[
                         (i,j)=(y,q-x)
\]

with width `i+j-q+1`.  Conversely the inequalities in `(3.4)` recover
`x=q-j` and `y=i` in the diagonal index range, while `i+j>=q` is exactly
`x<=y`.  Hence the triangle is neither missing nor adding cells.

If `i<=r_q` fails, then `r_q` cannot be `a-1`; therefore `r_q=q` and
`i>=q+1`.  If the other endpoint bound fails, the symmetric argument gives
`j>=q+1`.  This proves the exact two-wedge assertion.

## 3. Boundary-fan cost

In the right wedge, translate `i=q+1+i'`.  The strip inequality becomes

\[
                         i'+j\le\tau-2.
\]

Only the first `tau-1` indices on either axis can occur, giving exactly the
dimensions `A_R,B_R` in `(4.2)`.  The diagonal-fan word has physical length
`Gamma(A_R,B_R)`.  The upper wedge is identical after swapping axes.
The two fans may overlap only in target values; assigning each overlap to
one physical fan preserves injectivity.  The central word and both fan
words occupy separate physical positions.  Thus `(4.4)` is the literal
charged length of the stated atlas.

The possible empty-core normalization from the general diagonal-fan note
does not affect these boundary fans: a nonempty right fan is rooted at
local rank at least `q+1`, and similarly for the upper fan.

## 4. Rank-`R-d` owner words

With `m=R-d` and `q=m-u-v`, every source letter has rank `m`.  A
`d+1`-letter window has value

\[
                         C_{x+d}\cup D_{q-x}
\]

and rank `R`.  Moving one start forward deletes `d_(q-x)` and inserts
`c_(x+d+1)`, two labels in disjoint coordinate halves, so consecutive
owners are literal Johnson neighbours.  The same calculation gives rank
`m+w-1` at every shorter width.

Because the `C` coordinates only enter and the `D` coordinates only leave,
the source word has only suffix, prefix, full, or empty coordinate traces;
there is no bounded internal positive run.

Product-SCD grids partition the Boolean lattice.  Their local
rank-`m-u-v` diagonals therefore partition the global rank-`m` layer,
proving `(6.5)`.  A word of length `L` has exactly `max(L-d,0)` internal
windows of length `d+1`, proving `(6.6)`.  These owner values are distinct
across grids because the product-SCD cells themselves are disjoint.

## 5. Verifier and scope

The verifier implements the displayed diagonal lengths, boundary-fan
dimensions, strip phases, and product-SCD multiplicities.  Its assertion

\[
 \texttt{source\_rank\_letters}=\binom{k}{R-d}
\]

is exactly the independent census `(6.5)`.  Its small self-test checks
literal cell containment for every tested strip.  The proof above, rather
than that finite containment test, supplies interval uniqueness and the
Johnson-owner identities.

The sharp scope is correctly stated: the antidiagonal cores are a valid
partial carrier-compatible source atlas, but the boundary-complete charged
construction has coefficient larger than one and the rank-`R-d` layer has
too few owner windows for a full chronology.  Cross-grid stitching or a
multi-rank chronology remains genuinely open.

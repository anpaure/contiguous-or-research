# A fixed target SCD cannot absorb the invariant square cover by contraction

Date: 2026-09-07. This is an incidence obstruction for a specified
contraction of the coordinate-invariant fractional square family. It is not
a lower bound against non-invariant integral selection or unrestricted words.

## 1. Objects and the proposed contraction

Put `k=2b` and `W=binom(2b,b)`. A centered square pair of side `ell`, with
`2<=ell<=b`, is specified by disjoint coordinate sets/lists

\[
F,G,X=(x_1,\ldots,x_{\ell-1}),Y=(y_1,\ldots,y_{\ell-1}),
\quad |F|=|G|=b-\ell+1.
\]

Its target support is `R union R^c`, where

\[
R=\{F\cup X_{[i]}\cup Y_{[j]}:0\le i,j<\ell\},
\qquad R^c=\{[2b]\setminus S:S\in R\}.
\]

The two orientations are disjoint and have no containment flags between
them: one contains `F` and omits `G`, the other contains `G` and omits `F`.
The pair has exactly `2ell` middle targets and principal charge `2ell`.

Fix any symmetric-chain decomposition `D` of the entire target Boolean
cube. Each of its `W` chains contains exactly one middle target. A literal
chain-token contraction declares a square incident to a token only if the
square contains **every required target of that SCD chain**, or every target
of its intersection with the prescribed central band. Merely containing the
token's middle set is not enough to preserve target incidence.

This note shows that coordinate symmetrization and this contraction do not
commute: the near-width invariant fractional target cover becomes a very
sparse fractional token incidence family.

## 2. Exact prescribed-chain incidence

Fix a saturated chain

\[
K_{-h}\subset\cdots\subset K_0\subset\cdots\subset K_h,
\qquad |K_j|=b+j,
\quad 1\le h\le b,
\]

with every coordinate addition specified, and uniformly relabel one
side-`ell` square pair. Let `D_0` be its probability of containing `K_0`,
and let `lambda_h` be its probability of containing the entire displayed
chain. Define

\[
A_{\ell,h}(i)=
\sum_{r=\max(0,h-(\ell-1-i))}^{\min(h,i)}\binom hr,
\qquad 0\le i<\ell,
\]

where an empty sum is zero. Then

\[
\boxed{
\frac{\lambda_h}{D_0}
=\frac{\sum_{i=0}^{\ell-1}A_{\ell,h}(i)^2}
       {\ell(b)_h^2}
\le\frac{4^h}{(b)_h^2}.}                         \tag{1}
\]

Here `(b)_h=b(b-1)...(b-h+1)`. If `h>=ell`, the numerator is zero.
If `2h<ell`, then also

\[
\frac{\lambda_h}{D_0}
\ge\left(1-\frac{2h}{\ell}\right)
             \frac{4^h}{(b)_h^2}.                 \tag{2}
\]

In particular, for the prescribed three-set chain at adjacent ranks,

\[
\boxed{\frac{\lambda_1}{D_0}
       =\frac{4-6/\ell}{b^2}.}                   \tag{3}
\]

### Proof

There are `W(b)_h^2` saturated labeled chains through the middle with the
displayed ranks: choose the middle set, the ordered `h` removals below it,
and the ordered `h` additions above it. Coordinate permutations act
transitively on this family.

Inside `R`, a middle target has prefix indices `(i,j)` with `i+j=ell-1`.
A downward path of length `h` uses `r` removals from the `X` prefix and
`h-r` from the `Y` prefix. The orders within each prefix are forced; the
two removal sequences can be interleaved in `binom(h,r)` ways. The capacity
conditions are exactly the limits defining `A_(ell,h)(i)`.

The available upward prefix lengths are `j` in `X` and `i` in `Y`.
Interchanging the names of the two rails therefore gives the same number
of upward paths. The number of full centered `2h+1`-target chains through
this middle target is `A_(ell,h)(i)^2`. Sum over `i` and both orientations.
Divide by `W(b)_h^2`, then by `D_0=2ell/W`, to obtain (1).

Each `A` is at most `2^h`. For `h<=i<=ell-1-h`, all interleavings are
possible, so `A=2^h`; there are `ell-2h` such indices. This proves (2).
For `h=1`, the two endpoint values of `A` are one and the remaining
`ell-2` values are two. Hence `sum A^2=4ell-6`, giving (3).

## 3. Capacity loss for a common-SCD token cover

Let `F` be any nonnegative coordinate-invariant weighted family of these
square pairs, with sides allowed to vary and total principal charge `M`.
Every middle target receives total weight `M/W`, because each pair's
middle incidence equals its charge.

For any fixed SCD chain whose required segment reaches both ranks
`b-h,b+h`, its contracted token incidence is consequently at most

\[
\boxed{\frac MW\frac{4^h}{(b)_h^2}.}              \tag{4}
\]

Thus, if this invariant family is required to be a fractional cover of
those literal chain tokens, its charge must satisfy

\[
\boxed{M\ge W\frac{(b)_h^2}{4^h}.}               \tag{5}
\]

Already `h=1` forces `M>=b^2W/4`, instead of `M=(1+o(1))W`.
This is not an exceptional-chain effect. Every SCD of the `2b`-cube has
exactly `binom(2b,b+h)` chains reaching both offset ranks `b-h,b+h`:
these are precisely the chains containing a target at rank `b+h`.
For fixed `a>0` and `h=floor(a sqrt(b))`, their number is
`(e^(-a^2)+o(1))W`. Hence a positive fraction of all tokens suffers the
much stronger bound (4); the logarithm of its factor is

\[
\log\frac{4^h}{(b)_h^2}=-2h\log b+O(h+h^2/b).
\]

The conclusion applies to the inherited weights, and indeed to any
coordinate-invariant reweighting. Choosing a common SCD first and then
strongly biasing the square distribution toward it is outside this
obstruction and would require a new construction.

## 4. A capacity test without invariance

There is also a simple necessary test for an arbitrary integral selected
family. Let its pair sides be `ell_1,...,ell_t`, its charge be
`M=2 sum ell_i`, and suppose `U` of the fixed SCD tokens are left
uncovered under literal full-chain containment. For every `h>=1`,

\[
\boxed{
U\ge\left[
\binom{2b}{b+h}-2\sum_{i=1}^t(\ell_i-h)_+
\right]_+.}                                      \tag{6}
\]

Indeed `binom(2b,b+h)` distinct SCD chains have a target at rank `b+h`.
Every such covered token supplies a distinct target at that rank inside
one of the selected squares. Their total number is bounded by the sum of
the squares' rank-`b+h` support sizes, namely `2 sum(ell_i-h)_+`.

Unlike (5), (6) survives non-invariant selections, but it is only a rank
capacity test. The convex-profile fractional construction was designed to
pass such rank tests. Passing it does not preserve the specified chains;
the labeled-chain loss in (1)--(4) is the additional obstruction to the
proposed common-SCD contraction.

## 5. Why this is not a pointwise obstruction to biased selection

Highly compatible exceptional squares do exist. Take SCDs on two disjoint
`b`-coordinate halves, and form a global SCD by decomposing every product
of two half chains into symmetric chains. If two half chains `C,D` have
the same length `ell<=b` and their bottoms together are nonempty, their
square `C x D` is exactly a union of `ell` complete chains of this global
SCD. All `ell` of its middle targets therefore have their full fixed-SCD
tokens inside that one orientation.

Explicitly, on the square's prefix grid `[ell]^2`, the hooks indexed by
`j=0,...,ell-1` are

\[
(0,j),(1,j),\ldots,(\ell-1-j,j),
(\ell-1-j,j+1),\ldots,(\ell-1-j,\ell-1).
\]

They partition the grid and have endpoint-rank sums `2ell-2`, so they are
symmetric about its middle rank, which is also the Boolean middle rank.
The same elementary product decomposition on every other half-chain pair
completes the global SCD. This example prevents extrapolating the invariant
loss into a bound on every individual square.

The remaining constructive possibility is to select and coordinate such
exceptional compatible squares. The present invariant fractional cover
does not carry enough weight on them to justify contraction at its old cost.

Relevant archived comparisons inspected: the constant-side product-SCD
assignment of 2026-08-21, the affine-schedule/SCD-diagonal obstruction of
2026-08-21, and the exported product-SCD global Hall cut of 2026-07-26.
Those concern different carriers and do not supply the literal incidence
required here. No master file was changed.

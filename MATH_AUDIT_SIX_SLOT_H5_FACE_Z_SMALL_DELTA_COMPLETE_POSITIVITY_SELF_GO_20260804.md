# Self-audit: six-slot `h=5` face `Z` small-excess closure

**Date:** 2026-08-04  
**Verdict:** `GO_SELF`.  The theorem below was re-read against every cited
source, its face geometry was rederived from the compact polytope, and all
rational margins were recomputed independently.  This is a pure
mathematical audit; no search, optimizer, sampler, or finite chamber scan
is used.

## 1. Audited theorem

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_SIX_SLOT_H5_FACE_Z_SMALL_DELTA_COMPLETE_POSITIVITY_20260804.md` | `5b9fc5880b0b8717036b744c2639928cfd84d27f57d0b4d5aca125afec0243d5` |

## 2. Dependency authentication

| role | SHA-256 checked |
|---|---|
| exact reflected `h=5` polytope | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| large-`delta` closure and two-fifths anchor | `34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a` |
| global compact price and monotonicity from `4A/25` | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| no-interior-minimum theorem | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| quarter anchor | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta positivity | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |

All six current bytes have exactly these hashes.

## 3. Geometry replay

On face `Z`, `A-2m=delta`, so

\[
 m=(A-\delta)/2.
\]

For `0<delta<A/15`, this gives

\[
 7A/15<m<A/2.
\]

The rows `m>=x+v`, `v>=(A+4u)/5`, and the global density rows give

\[
 v\le m-x\le m<A/2,
 \quad v\ge(A+4u)/5,
 \quad x\le A/5,
 \quad y\le2A/5,
 \quad u<A/6.
\]

No reflection of `v` beyond `A/2` is used.  The quarter and
two-fifths no-interior-minimum applications are valid because

\[
 C<F(A/4),
 \qquad F(2A/5)<C.
\]

Thus `F(x)>=C` and `F(y)>=F(2A/5)` follow on the stated ranges.

## 4. New compact estimates

The Jacobi identity was checked with the two notationally distinct theta
quantities kept separate:

\[
 f(t)=1-\vartheta(t)+H(t)+R(t),
 \qquad |\vartheta(t)-2|<\varepsilon.
\]

On `[0,1/16]`,

\[
 {d\over dt}\left(
 \log{2-t\over t}-\pi(1-t)
 \right)
 =\pi-{2\over t(2-t)}<0,
\]

and the value at `1/16` is positive.  Hence `H` increases there; every
term of `R` plainly increases there as well.

The endpoint ledgers are

\[
 {9993\over10000}+{6\over125}+{1\over1000}
 -1+{1\over20000}
 ={967\over20000}<{49\over1000},
\]

and

\[
 {99695\over100000}+{21\over400}+{29\over25000}
 -1+{1\over20000}
 ={2533\over50000}<{51\over1000}.
\]

For the residual tails,

\[
 {99/100000\over1-1/200}={99\over99500}<{1\over1000},
\]

\[
 {23/20000\over1-1/200}={23\over19900}<{29\over25000}.
\]

The listed finite Taylor degrees are sufficient after the strict lower
substitution `pi>333/106`; all denominators are positive.

## 5. Point-anchor replay

At `9A/40`, the four retained lower Gaussian certificates sum to

\[
 {6238+3076+204\over10000}+{27\over100000}
 ={95207\over100000},
\]

so

\[
 F(9A/40)<{4793\over100000}<{48\over1000}.
\]

At `7A/15`, they sum to

\[
 {799790+184610+8400+79\over1000000}
 ={992879\over1000000},
\]

so

\[
 F(7A/15)<{7121\over1000000}.
\]

Both use only lower bounds on adverse Gaussian terms; dropping the
remaining adverse tail is in the safe direction.  Combining the latter
anchor with the frozen lower two-fifths anchor gives

\[
 F(y)-F(m)>{18879-7121\over1000000}
 ={11758\over1000000}.
\]

## 6. Three-case ledger

Since `C>L=44024/1000000`, the bank `2C-F(u)-F(v)` has the following
strict lower prices.

| `u` range | `F(u)` price | forced `v` | `F(v)` price | compact loss | possible theta cost | final margin |
|---|---:|---:|---:|---:|---:|---:|
| `[0,A/32]` | `49000` | `A/5` | `49730` | `-10682` | `100` | `976` |
| `[A/32,A/16]` | `51000` | `9A/40` | `48000` | `-10952` | `100` | `706` |
| `[A/16,A/6)` | `53300` | `A/4` | `45160` | `-10412` | `50` | `1296` |

Every number in the last four columns is in units of `10^-6`.  The
compact-loss checks are

\[
 88048-49000-49730=-10682,
\]

\[
 88048-51000-48000=-10952,
\]

\[
 88048-53300-45160=-10412.
\]

The final checks are

\[
 11758-10682-100=976,
\]

\[
 11758-10952-100=706,
\]

\[
 11758-10412-50=1296.
\]

All six period gains were discarded in the safe nonnegative direction.
The theta charges are correct: `Theta(m)>0` in all cases; in Case III,
also `Theta(v)>0` because `v>=A/4`.

## 7. Scope audit

The conclusion is exactly:

* face `Z` is positive for `0<delta<A/15`, with margin `706/10^6`;
* together with the already closed threshold and large-`delta` ranges,
  face `Z` is completely positive.

It does not claim positivity of faces `X` or `Y`, the interior of the
three-face union, the full unsigned `Gamma_5`, a general grid theorem, or
an OR-word result.

**Final self-audit verdict:** `GO_SELF`.

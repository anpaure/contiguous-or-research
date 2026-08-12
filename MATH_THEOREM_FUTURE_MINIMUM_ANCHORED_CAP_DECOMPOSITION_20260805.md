# Future-minimum decomposition gives the maximal anchored socket bank

**Date:** 2026-08-05  
**Method:** pure real analysis; no computation, search, or solver  
**Status:** unconditional exact decomposition.  Every continuous socket
density vanishing at the left endpoint splits canonically into its maximal
nondecreasing minorant and one nonnegative cap vanishing at both endpoints.
The first part has only upper-anchored uniform layers; every layer of the
cap is nonanchored.  For the first Rayleigh residual the cap is nonzero but
is the smallest possible cap under any such monotone-minorant split.

## 1. Canonical split

Let `g:[0,B]->[0,infinity)` be continuous, with

\[
 g(0)=0,
 \qquad g(y)>0\quad(0<y\le B).
\]

Define the future minimum

\[
 h(y)=\min_{y\le t\le B}g(t),                    \tag{1.1}
\]

and the cap

\[
 k(y)=g(y)-h(y).                                  \tag{1.2}
\]

### Theorem 1.1 (maximal anchored-minorant decomposition)

The functions `h,k` satisfy:

1. `h` is continuous and nondecreasing;
2. `0<=h<=g`, `h(0)=0`, and `h(B)=g(B)>0`;
3. `k` is continuous and nonnegative, with `k(0)=k(B)=0`;
4. if `v` is any nondecreasing function with `0<=v<=g`, then `v<=h`.

Thus `h` is the unique maximal nondecreasing minorant of `g`, and `k` is
the pointwise-minimal cap left by any decomposition of `g` into a
nondecreasing minorant plus a nonnegative remainder.

### Proof

If `y_1<y_2`, then `[y_2,B]` is contained in `[y_1,B]`, so its minimum
cannot be smaller.  Hence `h` is nondecreasing.  Clearly `h(y)<=g(y)`, and
the endpoint identities follow from the hypotheses.

Continuity is a standard compact-minimum argument, included for
completeness.  Uniform continuity of `g` gives, for nearby `y,y'`, an
arbitrarily small change in `g` on the short interval between them.  If a
minimizer for the larger tail lies in their common part, both minima differ
by at most that oscillation; if every minimizer lies in the deleted short
interval, its value differs from `g(y')` by the same oscillation, while
`g(y')` is admissible for the larger tail.  Thus `h(y')->h(y)` cannot jump.
Monotonicity rules out the opposite jump.  Therefore `h` is continuous,
and so is `k=g-h`.

Finally, if `v` is nondecreasing and `v<=g`, then for every `t>=y`,

\[
 v(y)\le v(t)\le g(t).
\]

Taking the minimum over `t in[y,B]` gives `v(y)<=h(y)`. `square`

## 2. Exact layer geometry

Use the canonical superlevel-component decomposition of densities into
uniform interval layers.

### Corollary 2.1

Every nonempty superlevel component of `h` has right endpoint `B`.  Every
positive superlevel component of `k` has both endpoints strictly inside
`(0,B)`.

### Proof

Because `h` is nondecreasing, `{h>s}` is either empty or a terminal
interval ending at `B`.  Since `k` is continuous and vanishes at both
endpoints, the closure of every component of `{k>s}` for `s>0` is a compact
subinterval of `(0,B)`. `square`

Hence `g=h+k` has an exact two-bank layer representation

\[
 \Lambda_g^{\rm split}
 :=\Lambda_h+\Lambda_k
 =\Lambda_{\rm anc}+\Lambda_{\rm cap}.           \tag{2.1}
\]

Every interval in `Lambda_anc=Lambda_h` is upper-anchored and every interval
in `Lambda_cap=Lambda_k` is internal.  Equation (2.1) names the sum of the
two layer measures; it does **not** assert equality with the canonical layer
measure obtained by decomposing `g` without first splitting the density.
That distinction is harmless for packet construction, because the
barycenter of the two banks is exactly `g(y)dy`.

## 3. First Rayleigh residual

For

\[
 g_2(y)=-K'(y)-u'(y),\qquad0<y<b,
\]

the one-well theorem gives `g_2>0`, while `g_2(0)=0`.  The endpoint theorem
gives

\[
 g_2'(b-)<0.
\]

Therefore `g_2` is strictly larger just to the left of `b` than at `b`.
Equation (1.1) then gives `h<g_2` on a nonempty interval, so the cap `k` is
nonzero and has positive layer mass.

Combining Corollary 2.1 with the cap-pair transport theorem yields the exact
two-stage analytic route:

1. neutralize the single cap bank by two-socket cap packets;
2. solve endpoint composition on the maximal anchored bank left by `h`.

Maximality of `h` proves that no other decomposition using one
nondecreasing whole-role density can leave a smaller pointwise cap.  The
remaining issue is resource transport, not how to choose the monotone
minorant.

## 4. Frozen dependencies

1. `MATH_THEOREM_NONANCHORED_UNIFORM_CAP_PAIR_TRANSPORT_20260805.md`,
   SHA at use
   `3da210b29584a930fb217a0b3a8d5e4a6cd7c95984d752839eeba64b94705a77`.
2. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`,
   SHA at use
   `78e017354f77b21e6ba0c53301027e25cec3ffd020872727cbe9aab8802469c7`.

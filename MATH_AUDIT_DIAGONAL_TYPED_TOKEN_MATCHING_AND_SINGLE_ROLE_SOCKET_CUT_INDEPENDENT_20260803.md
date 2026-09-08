# Independent audit: diagonal typed-token matching and the single-role socket cut

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_DIAGONAL_TYPED_TOKEN_MATCHING_AND_SINGLE_ROLE_SOCKET_CUT_20260803.md`  
**Audited theorem SHA-256:**
`96ce831d86412f151a2d9abcc89e62cb9e9a988709759467f8d694443f370efa`  
**Verdict:** **GO after scope corrections.**  The cyclic occurrence matching,
the exact-length capacity cut, the conditional fixed-charge cut, and both
numerical calibrations are correct under the hypotheses now stated in the
theorem.  The result is a no-alias, single-role obstruction; it is not an
impossibility theorem for a dual-role compiler or for `nu(k)<=B(k)+O(1)`.

No finite search was used in this audit.

## 1. Corrections made during the audit

The original file had SHA-256
`ef9b1d8c384d28536c5a60170efeaaa569166eeb5fa82bcd8b58abde21b9517e`.
Four proof-scope points were repaired.

1. The cap-two transversal paragraph requires `m>=3`.  At `m=2`, the
   duplicate budget `C` exceeds the number `U` of upper colours, so the
   simple `1+1_D` model with `D` a set is unavailable.
2. The `W`-token alternating-cycle matching is a theorem on the cyclic
   carrier.  A linear word of length `W+d` has only `W-1` internal q1 seams
   unless the wrap token is separately realized.  The terminal cut remains
   correct because it deliberately grants all `W` cyclic candidates.
3. The `B+1` and fixed-`c` reservations of `W` owner cells require the same
   width-`d+1` diagonal-owner band.  This hypothesis is now explicit.
4. The displayed deficiency bounds are written with positive part.  This is
   the exact consequence of a terminal bank of size at most `C+sigma`; a
   negative untruncated lower bound would only be vacuous.

These repairs do not change either calibration or the substantive cut.

## 2. Central binomial and Catalan identities

For `k=2m-1`,

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1}
   ={m-1\over m+1}W.
\]

Therefore

\[
 C=W-U={2W\over m+1}
   ={1\over m+1}{2m\choose m}=\operatorname{Cat}_m.
\]

All three identities in (0.1) are exact.

## 3. Cyclic typed-token matching

The chronological occurrence graph has edges

\[
 Q_iT_i,\qquad Q_iT_{i+1}\qquad(i\in\mathbb Z_W).
\]

Hence it is literally the alternating cycle

\[
 T_0,Q_0,T_1,Q_1,\ldots,T_{W-1},Q_{W-1},T_0.
\]

Its two perfect matchings are `T_i--Q_i` and `T_i--Q_(i-1)`.
Their types are valid because

\[
 \operatorname{OR}(Q_i)=T_i\cup T_{i+1}.
\]

This proves the occurrence-level claim on the cyclic carrier.  It does not
manufacture the missing wrap seam in a literal linear opening.  Conversely,
using all `W` cyclic turns in an upper bound on available socket capacity is
safe: it can only weaken the obstruction.

## 4. Independent check of the transversal/contraction paragraph

Let the left shore consist of rank-`m+1` colours and the right shore of
rank-`m` owners, with inclusion edges.  Their degrees are respectively
`m+1` and `m-1`.

For every upper-colour family `Y`, edge counting gives

\[
 |N(Y)|\ge {m+1\over m-1}|Y|\ge |Y|.
\]

Thus one base copy of every upper colour is independent in the transversal
matroid.  For every owner family `X`,

\[
 |N(X)|\ge {m-1\over m+1}|X|,
\]

and two formal copies of every neighbouring upper colour give

\[
 2|N(X)|\ge {2(m-1)\over m+1}|X|\ge |X|
\]

exactly when `m>=3`.  The two-copy ambient transversal matroid therefore has
rank `W`.  Contracting the `U` independent base copies leaves rank
`W-U=C`.  A `C`-set `D` of duplicate colours is a basis of the contraction
exactly when the base copies together with the duplicates indexed by `D`
saturate the owner shore.  Hall's condition is precisely

\[
 |N(X)|+|D\cap N(X)|\ge |X|
\]

for every owner family `X`.  Thus (1.6) and the contraction-rank claim are
correct.  A realized cap-two cyclic row supplies the stronger literal token
matching from Section 3.

## 5. Exact-length short-cell capacity

At length `n=W+d`, the number of interval addresses of lengths at most `d`
is

\[
 \sum_{\ell=1}^{d}(n-\ell+1)
 =dW+{d(d+1)\over2}=dW+\tau_d.
\]

Every one of the `Lambda` distinct strict-lower targets needs a distinct
interval address.  On the exact diagonal face the `W` width-`d+1` cells are
the central owners, so every longer interval contains a rank-`m` owner;
hence a strict-lower target can only use the counted short pool.  At most

\[
 \sigma=dW+\tau_d-\Lambda
\]

short addresses remain unused.  Ferrers boundary cells are members of this
same address pool.  If assigned to lower targets, they are among the
`Lambda` consumed cells and cannot be added again as terminal sockets.

The q1 band has width `d+2`, disjoint in address from the short pool.  An
upper-complete cyclic q1 row has `W` tokens and `U` required colours, so
after retaining one token per colour at most `W-U=C` are surplus.  A linear
opening has only `W-1` internal q1 cells; granting `W` is a valid relaxation.
Thus the admitted no-alias single-role terminal bank has size at most

\[
 C+\sigma.
\]

A unit-capacity linkage of `W` owner tickets has corank at least

\[
 W-\min(W,C+\sigma)=(W-C-\sigma)_+.
\]

The same statement follows from the exact Rado/gammoid formula by choosing
the full ticket set in one occurrence coordinate.  No product-closure or
typing assumption can enlarge the rank past the cardinality of this bank.

## 6. The `B+1` reservation

At length `W+d+1`, the pool through width `d+1` has size

\[
 (d+1)W+\tau_{d+1}.
\]

Relative to the exact-length short pool, the increase is

\[
 (d+1)W+\tau_{d+1}-(dW+\tau_d)=W+d+1.
\]

On the stated width-`d+1` diagonal-owner face, `W` cells in this pool are
reserved as the central owner row.  After also reserving `Lambda` lower
cells, the number of remaining short/new addresses is at most

\[
 (d+1)W+\tau_{d+1}-\Lambda-W=\sigma+d+1.
\]

Adding the at-most-`C` q1 surplus gives the exact asserted upper bound
`C+sigma+d+1` and corank lower bound

\[
 (W-C-\sigma-d-1)_+.
\]

The theorem correctly does not assert this reservation for an arbitrary
`B+1` architecture whose owner witnesses are not the stated diagonal band.

## 7. Fixed additive charge

Let `e=d+c`, `c>=1`.  The complete interval pool through width `e` has
size

\[
 eW+\tau_e.
\]

Under the explicit graded-upper-exact diagonal-band hypothesis, distinct
physical addresses must be reserved for:

* `Lambda` strict-lower targets;
* `W` rank-`m` owners; and
* every rank-`m+j` target for `1<=j<c`.

Subtracting these reservations gives

\[
\begin{aligned}
 &(d+c)W+\tau_{d+c}-\Lambda-W
   -\sum_{j=1}^{c-1}{2m-1\choose m+j}\\
 &=\sigma+(\tau_{d+c}-\tau_d)
   +\sum_{j=1}^{c-1}
       \left(W-{2m-1\choose m+j}\right).
\end{aligned}
\]

For `c=1`, the q1 band lies just outside this pool and its `C` surplus is a
separate allowed bank.  For `c>=2`, q1 is already the `j=1` admitted band;
adding `C` again would double count its addresses.  Extra endpoint cells in
all admitted bands are already included in `tau_(d+c)-tau_d`.

For fixed `j`,

\[
 { {2m-1\choose m+j}\over W}
 =\prod_{\ell=1}^{j}{m-\ell\over m+\ell},
\]

so its deficit from `W` is `O_j(W/m)`.  Also

\[
 \tau_{d+c}-\tau_d=cd+{c(c+1)\over2}=O_c(d).
\]

Since `C=2W/(m+1)=O(W/m)`, the `c=1` indicator term is likewise `o(W)`.
Thus (0.9)--(0.10) are correct.  Without graded exactness for all included
upper bands, this subtraction is not valid; the theorem now keeps that
hypothesis explicit.

## 8. Numerical calibrations

For `k=9`,

\[
 m=5,\quad W={9\choose5}=126,\quad
 U={9\choose6}=84,\quad C=42,
\]

\[
 \Lambda=\sum_{s=1}^{4}{9\choose s}=255,\qquad
 d=2,\qquad \sigma=2(126)+3-255=0.
\]

Hence the exact single-role bank has capacity at most `42` and deficiency
at least `84`; at `B+1` these become `45` and `81`.

For `k=17`,

\[
 m=9,\quad W={17\choose9}=24310,\quad
 U={17\choose10}=19448,\quad C=4862,
\]

\[
 \Lambda=\sum_{s=1}^{8}{17\choose s}=65535,\qquad
 d=3,\qquad \sigma=3(24310)+6-65535=7401.
\]

Therefore the exact bank has capacity at most

\[
 4862+7401=12263
\]

and deficiency at least

\[
 24310-12263=12047.
\]

At `B+1`, capacity is at most `12267` and deficiency at least `12043`.
All four numbers in the theorem are exact.

## 9. Scope conclusion

The theorem proves a large cut only for a terminal design that requires an
*unused*, distinct, single-role socket for every routed owner ticket and
draws those sockets from the counted short/q1 inventory.  It does not apply
to a valid role-coinstantiation in which one load-bearing occurrence carries
both semantics, nor to a separate capacity-faithful `W-O(1)` sink bank.

The known `k=9` optimum is therefore a calibration of the scope, not a
counterexample: that optimum necessarily escapes this restricted inventory.
With the corrections in Section 1, the theorem is proof-safe.

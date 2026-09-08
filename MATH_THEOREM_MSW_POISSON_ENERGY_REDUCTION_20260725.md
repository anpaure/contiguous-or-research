# Canonical MSW Poisson energy: exact collision-pair reduction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

For every depth, bounded Euclidean load energy is exactly a factorial
pair-collision theorem.  At depth one of the canonical MSW factor, the
pair count splits into two intrinsic Chung--Feller maps plus an endpoint
term which is unconditionally `O(W)`.

Consequently the depth-one Poisson-energy assertion reduces exactly to

\[
 \sum_S\binom{|\alpha^{-1}(S)|}{2}
 +\sum_T\binom{|\Gamma^{-1}(T)|}{2}=O(W),
\]

where

\[
 \alpha(x_i)=x_i\cap x_{i+1},\qquad
 \Gamma(x_i)=y_{i-1}\cup y_i.
\]

This note proves the reduction and isolates a recursion-level marked-tree
count which would finish it.  It does not prove that marked-tree bound.

## 1. Energy is exactly pair-collision excess

Fix a depth `q`, let

\[
 N_q=\binom{2m+1}{m-q},\qquad
 \lambda_q={W\over N_q},
\]

and let `mu_q` be the target load of any exact wreath factor.  Put

\[
 P_q=\sum_S\binom{\mu_q(S)}2.
\tag{1.1}
\]

Since `sum_S mu_q(S)=W`, one has

\[
 \sum_S\mu_q(S)^2=W+2P_q.
\]

Therefore

\[
 \boxed{
 \|\mu_q-\lambda_q\mathbf1\|_2^2
 =2P_q-(\lambda_q-1)W.}
\tag{1.2}
\]

Uniformly for `q<=A sqrt(m)`, the mean `lambda_q` is bounded above and
below by constants depending only on `A`.  Hence

\[
 \boxed{
 \|\mu_q-\lambda_q\mathbf1\|_2^2=O_A(W)
 \quad\Longleftrightarrow\quad
 P_q=O_A(W).}
\tag{1.3}
\]

Equivalently, the required theorem counts unordered pairs of distinct
pointed cyclic intervals having the same target.

## 2. The two intrinsic MSW depth-one maps

Let `B=Cat_m=W/(2m+1)`.  In one canonical Chung--Feller column write

\[
 x_0,x_1,\ldots,x_m,qquad
 y_i=g(x_i)=x_i\cup x_{i+1}\quad(0\le i<m).
\]

Let `D^i` be the `i`-flaw class.  As the Dyck root and column position
vary, `x_i` runs bijectively through `D^i`, and every `D^i` has size `B`.

Define

\[
 \alpha(x)=x\cap f(x)
 \quad(x\in\mathcal X_-:=D^0\sqcup\cdots\sqcup D^{m-1}),
\tag{2.1}
\]

and

\[
 \Gamma(x)=g(f^{-1}x)\cup g(x)
 \quad(x\in\mathcal X_+:=D^1\sqcup\cdots\sqcup D^{m-1}).
\tag{2.2}
\]

Thus `|X_-|=mB` and `|X_+|=(m-1)B`.

If the flip permutation of the column is

\[
 (a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1}),
\]

then the exact formulas are

\[
 \alpha(x_i)
 =\{a_0,\ldots,a_{i-1}\}
   \cup\{b_{i+1},\ldots,b_{m-1}\},
\tag{2.3}
\]

and

\[
 \Gamma(x_i)=x_i\cup\{a_i,b_{i-1}\}
 \qquad(1\le i<m).
\tag{2.4}
\]

The complete canonical odd-wreath first-shadow multiset consists of

1. the `mB` no-`infinity` targets `alpha(x)`;
2. the `2B` no-`infinity` endpoint targets
   `[2m] setminus y_0` and `[2m] setminus y_(m-1)`;
3. the `(m-1)B` targets
   `\{infinity\} union ([2m] setminus Gamma(x))`.

These are precisely the three families in the exact path formula for the
MSW odd factor.

## 3. Exact depth-one pair decomposition

For a no-`infinity` target `S`, let

\[
 a(S)=|\alpha^{-1}(S)|,
 \qquad e(S)=\#\{\text{endpoint occurrences equal to }S\}.
\]

For an `(m+2)`-set `T subseteq[2m]`, put

\[
                         c(T)=|\Gamma^{-1}(T)|.
\]

Then the full first-shadow pair moment is exactly

\[
 \boxed{
 P_1=P_\alpha+P_\Gamma+P_{\rm end},}
\tag{3.1}
\]

where

\[
 P_\alpha=\sum_S\binom{a(S)}2,
 \qquad
 P_\Gamma=\sum_T\binom{c(T)}2,
\tag{3.2}
\]

and

\[
 P_{\rm end}
 =\sum_S\left(a(S)e(S)+\binom{e(S)}2\right).
\tag{3.3}
\]

There are exactly `2B` endpoint occurrences.  The universal depth-one
matching cap says that the total load of every target is at most

\[
                         M_m=\left\lfloor{m+2\over2}\right\rfloor.
\]

Thus `a(S)+e(S)<=M_m`, and

\[
 a(S)e(S)+\binom{e(S)}2
 ={e(S)(2a(S)+e(S)-1)\over2}
 \le {2M_m-1\over2}e(S).
\]

Summing and using `sum_S e(S)=2B` gives

\[
 \boxed{
 P_{\rm end}\le(2M_m-1)B=O(W).}
\tag{3.4}
\]

Combining (1.2), (3.1), and (3.4) proves:

### Theorem 3.1 (exact canonical depth-one gate)

The canonical MSW factor satisfies

\[
 \|\mu_1-\lambda_1\mathbf1\|_2^2=O(W)
\]

if and only if

\[
 \boxed{P_\alpha+P_\Gamma=O(W).}
\tag{3.5}
\]

No endpoint or odd-tag issue remains in this criterion.

## 4. The precise Dyck-recursive pair theorem

The flip word obeys

\[
 \pi(1u0v)=
 (|u|+2,\ |u|+2-\pi(\operatorname{rev}u),\ 1,\
                  |u|+2+\pi(v)).
\tag{4.1}
\]

Thus (2.3)--(2.4) make every collision in (3.5) recursively decidable from
two rooted plane trees with one distinguished column position.

The exact missing combinatorial statement is:

### MSW marked-tree collision theorem

There is an absolute constant `C` such that, for every `m`,

\[
 \boxed{
 \#\{\{x,x'\}\subseteq\mathcal X_-:
          x\ne x',\ \alpha(x)=\alpha(x')\}
 +
 \#\{\{x,x'\}\subseteq\mathcal X_+:
          x\ne x',\ \Gamma(x)=\Gamma(x')\}
 \le C m\operatorname{Cat}_m.}
\tag{4.2}
\]

Since

\[
                         m\operatorname{Cat}_m=\Theta(W),
\]

(4.2) is exactly (3.5).

A particularly useful sufficient proof form would give a bounded-to-one
encoding of every collision pair by

\[
       (\text{one Dyck root of semilength }m,
        \text{one marked tree edge/corner},
        \text{one of finitely many local types}).
\tag{4.3}
\]

There are `O(m Cat_m)=O(W)` such marked objects.  The contextual
`1100/1010` insertion collision already has exactly this form and supplies
`(2m-3)Cat_(m-2)=Theta(W)` disjoint pointed pairs.  It proves that the
scale in (4.2), if true, is sharp; it does not upper-bound all collisions.

What remains is a first-discrepancy theorem for the recursion (4.1): equal
prefix--suffix sets in (2.3), or equal two-boundary enlargements in (2.4),
must be recoverable from one marked local rotation with bounded ambiguity.
That statement is not presently proved.

## 5. Full Gaussian-window version

For the canonical omitted-label word `widehat(pi)(w)`, let

\[
 L_{m,q}(w,i)
 =\{\widehat\pi(w)_{i+1},\widehat\pi(w)_{i+3},\ldots,
      \widehat\pi(w)_{i+2(m-q)-1}\}
\tag{5.1}
\]

with cyclic subscripts, and define

\[
 \mathcal P_{m,q}
 =\#\left\{
   \{(w,i),(w',j)\}: (w,i)\ne(w',j),\
   L_{m,q}(w,i)=L_{m,q}(w',j)
  \right\}.
\tag{5.2}
\]

This is exactly `P_q`.  Hence the hypothesis needed by prime-cycle band
smoothing is precisely:

### Gaussian MSW collision theorem

For every fixed `A<infinity`, there is `C_A<infinity` such that

\[
 \boxed{
 \mathcal P_{m,q}\le C_AW
 \qquad(1\le q\le A\sqrt m).}
\tag{5.3}
\]

By (1.3), (5.3) is equivalent to the uniform Poisson-energy hypothesis.
The depth-one theorem (4.2) is its first nontrivial case.

The currently proved extension-packing cap

\[
 (q+1)\mu_q(S)\le\binom{m+q+1}{q}
\]

does not imply (5.3): it permits collision mass far larger than `W`.
The required input is genuinely the recursive distribution of canonical
MSW interval collisions, not merely pointwise capacity.


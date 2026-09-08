# Gate B: a uniform shallow-orbit factor from unique-interval witnesses

**Date:** 2026-08-22  
**Status:** proved for every `r>=4` and every `2<=j<=r-2`

This note closes the orbit-factor part of the depth-two Gate-B scalar.  Put

\[
 b=2r+1,\qquad k=r-2,\qquad N={b\choose k}.
\]

For every harmonic module `2<=j<=k`, the relative shallow-current orbit
factor satisfies

\[
 \boxed{
 \Theta_{r,j}\ge
 {N\over b^2k(k-1)(b-k)(b-k-1)}
 \ge {N\over36r^6}.}                                      \tag{0.1}
\]

Thus \(\Theta_{r,j}\) is not a small factor anywhere in the whole
depth-two band.  In particular, any polynomial lower bound for the
corresponding four-column angle already implies a polynomial lower bound
for their product.  The angle and the stopped/full-exposure transfers are
not proved here.

## 1. Harmonic interval vectors

Fix `j` disjoint ordered coordinate pairs
\((a_1,b_1),\ldots,(a_j,b_j)\).  For a `k`-set `A`, put

\[
 H_k(A)=\prod_{i=1}^j
 \bigl(\mathbf1_{\{a_i\in A\}}-\mathbf1_{\{b_i\in A\}}\bigr).
                                                               \tag{1.1}
\]

On the position cycle \(\mathbb Z_b\), let
\(I_k(t)=\{t,t+1,\ldots,t+k-1\}\), with positions read modulo `b`.
For a uniform permutation \(g\in S_b\), define

\[
 d_t(g)=H_k(gI_k(t)),\qquad q(g)=\sum_{t\in\mathbb Z_b}d_t(g),
 \qquad \kappa_{k,j}=\|d_0\|_2^2.                            \tag{1.2}
\]

The `2j` positions
\(g^{-1}a_1,g^{-1}b_1,\ldots,g^{-1}a_j,g^{-1}b_j\)
are a uniform ordered injection into \(\mathbb Z_b\).  The square
\(d_0^2\) is one precisely when every distinguished pair is split by
\(I_k(0)\).  Choosing the endpoint lying inside, and then assigning the
inside and outside endpoints injectively, gives the exact norm

\[
 \boxed{
 \kappa_{k,j}=
 {2^j(k)_j(b-k)_j\over(b)_{2j}}.}                            \tag{1.3}
\]

Here \((x)_s=x(x-1)\cdots(x-s+1)\), with \((x)_0=1\).

## 2. A counted event on which the cyclic sum is exactly one in modulus

Write

\[
 I_k(0)=\{0,1,\ldots,k-1\}.
\]

Its two boundary edges are
\(\{b-1,0\}\) and \(\{k-1,k\}\).  Consider the following event
\(\mathcal E\) for the endpoint positions of the distinguished pairs:

1. the endpoints of pair `1` occupy \(\{b-1,0\}\), in either order;
2. the endpoints of pair `2` occupy \(\{k-1,k\}\), in either order;
3. for each remaining pair, one endpoint lies injectively in
   \(\{1,\ldots,k-2\}\), the other lies injectively in
   \(\{k+1,\ldots,b-2\}\), and either orientation is allowed.

The capacity conditions are automatic: `j<=k` gives
\(j-2\le k-2\), while
\(j-2\le b-k-2\).  Counting ordered endpoint injections gives

\[
 \boxed{
 \Pr(\mathcal E)=
 {2^j(k-2)_{j-2}(b-k-2)_{j-2}\over(b)_{2j}}.}                \tag{2.1}
\]

A proper cyclic interval separates the endpoints of an adjacent-position
pair only if one of its two boundary edges is the edge joining those
positions.  Consequently, any `k`-interval which splits both pairs `1`
and `2` must have exactly the two boundary edges displayed above.  Those
edges delimit two cyclic arcs, of lengths `k` and `b-k`.  Since
\(k\ne b-k\), the unique arc of length `k` is \(I_k(0)\).

On \(\mathcal E\), every distinguished pair is split by \(I_k(0)\).
It follows that \(d_0=\pm1\), while every \(d_t\) with \(t\ne0\) is zero.
Therefore

\[
                         q^2=1\quad\hbox{on }\mathcal E,      \tag{2.2}
\]

and hence, using (1.3),

\[
 {\|q\|_2^2\over\kappa_{k,j}}
 \ge {\Pr(\mathcal E)\over\kappa_{k,j}}
 ={1\over k(k-1)(b-k)(b-k-1)}.                              \tag{2.3}
\]

The cancellation of all `j`-dependent falling factorials in (2.3) is the
reason this witness remains uniform through the top module.

## 3. Identification with the Gate-B orbit factor

For completeness, define

\[
 F_{r,j}:=N\theta_{r,j},\qquad p={b\over N},\qquad
 \Theta_{r,j}:={\theta_{r,j}\over p^2}.                      \tag{3.1}
\]

The usual shallow-current orbit formula is exactly

\[
                         F_{r,j}={\|q\|_2^2\over\kappa_{k,j}}.\tag{3.2}
\]

Here is a direct verification.  For two cyclic `k`-intervals, there is
one relative shift with intersection `k`, two shifts with each
intersection size `1,...,k-1`, and

\[
                         b-2k+1=6
\]

shifts with intersection zero.  If
\(\zeta_{k,k,j}(h)=\langle d_0,d_t\rangle\) when the intersection
has size `h`, cyclic stationarity gives

\[
 {\|q\|_2^2\over\kappa_{k,j}}
 =b\left(1+2\sum_{h=1}^{k-1}
 {\zeta_{k,k,j}(h)\over\kappa_{k,j}}
 +6{\zeta_{k,k,j}(0)\over\kappa_{k,j}}\right).               \tag{3.3}
\]

This is precisely the Hahn-shell expression for \(N\theta_{r,j}\): its
shell weights are `1`, `2`, and `6` at intersection `k`, a proper positive
intersection, and zero, respectively.  This proves (3.2) without an
asymptotic step.

Equations (3.1)--(3.2) yield

\[
 \Theta_{r,j}={N\over b^2}{\|q\|_2^2\over\kappa_{k,j}}.
                                                               \tag{3.4}
\]

Substitution of (2.3) proves the first inequality in (0.1).  Finally,
for `r>=4`,

\[
 b\le3r,\quad k(k-1)\le r^2,\quad
 (b-k)(b-k-1)=(r+3)(r+2)\le4r^2.
\]

Their product is at most \(36r^6\), proving the second inequality in
(0.1).  \(\square\)

## 4. Exact scope

This theorem removes the orbit factor from the list of possible
depth-two bottlenecks.  It does not prove a lower bound for the angle
between the shallow current and the four compensated columns.  In the
cyclic-difference route, the remaining complete-state scalar is a
polynomial coercivity bound for the normalized four-column difference
Gram matrix.  The transfer from the second-order columns to full exposure,
simultaneous delocalized inversion, stopped stability, and hole-aligned
positive accumulation also remain separate.

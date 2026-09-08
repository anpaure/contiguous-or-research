The compact four-box theorem remains unproved. I did obtain a strict, independently audited improvement of the reset-free complementary portal: the unchanged near-once word covers an additional \(\Theta(q^4)\) family of line-easy targets, with an exact leading constant.

## Spill-completed portal theorem

Let \(R=2m-1\) and \(1\le q\le\lfloor m/3\rfloor\). In one high/low orientation set

\[
X_t(A,B)=(m-A-t,B+t,m-B-1,A),
\]

\[
Y_t(A,B)=(m-A-1,B,m-B-t,A+t).
\]

The known word \(W_{m,q}\) contains, for every \(A,B\ge0\) with \(A+B\le q-1\), the block

\[
X_{q-1-B},\ldots,X_0,Y_0,\ldots,Y_{q-1-A}.
\]

It has exact length

\[
|W_{m,q}|=|L_R|+4q(q-1)
=w_4(m,m,m,m)-(m+1)+4q(q-1).
\]

Besides the previously proved doubly-missed targets, it covers the following spill families.

For

\[
A+B\le q-1,\qquad
1\le h\le\min(A,B),\qquad
1\le u\le q-1-B,
\]

the line-easy target

\[
Z^X_{A,B;h,u}
=(m-A+h,B+u,m-B-1,A)
\]

is represented inside the neighboring portal block \((A-h,B+1)\). Indeed,

\[
\bigvee_{t=-h}^{u}X_t(A,B)
=Z^X_{A,B;h,u},
\]

while the actual stored interval

\[
X_{u-1}(A-h,B+1),\ldots,X_0,
Y_0,\ldots,Y_h
\]

has exactly the same maximum.

Symmetrically, if \(1\le v\le q-1-A\),

\[
Z^Y_{A,B;h,v}
=(m-A-1,B,m-B+h,A+v)
\]

is represented in block \((A+1,B-h)\), since

\[
\bigvee_{t=-h}^{v}Y_t(A,B)
=Z^Y_{A,B;h,v}.
\]

All displayed receiving labels and arm parameters lie in the existing word. The depth is automatically at most \(q-1\), because \(h\le B\) and \(u\le q-1-B\), or symmetrically \(h\le A\) and \(v\le q-1-A\). Merely assuming \(h+u\le q\) would not suffice.

These are genuinely new targets: for \(s=h+u\),

\[
(Z^X)_1-s=m-A-u\ge0,\qquad
(Z^X)_2-s=B-h\ge0,
\]

so \(Z^X\) has a complete \(\{1,2\}\)-line witness and is excluded from the previously covered doubly-missed family.

The \(X\)-spill targets are injectively parametrized. Their exact count in one orientation is

\[
C_X(q)=
\sum_{B=1}^{q-2}(q-1-B)
\sum_{A=1}^{q-1-B}\min(A,B)
=\frac5{96}q^4+O(q^3).
\]

The four orientations are disjoint because designated low coordinates are at most \(q-1\), while designated high coordinates are at least \(m-2q+1>q-1\). Hence the unchanged word covers

\[
4\binom{q+3}{4}+4C_X(q)
=\frac38q^4+O(q^3)
\]

certified targets through depth \(q\), versus the previous

\[
4\binom{q+3}{4}
=\frac16q^4+O(q^3).
\]

Thus the guaranteed positive-volume upper family more than doubles at zero additional length.

## Why the transfer does not close the braid

The balanced odd-seam inward prefix also transfers exactly to a neighboring odd rectangle. However, retaining every literal balanced even/odd portal remains cubic.

On the line shared by \(E(A,B)\), \(A+B=2r\), and \(O(A,B+1)\), the rays are

\[
E:p_0,p_1,p_2,\ldots,\qquad
O:p_1,p_2,\ldots,
\]

with different required predecessors of \(p_1\). For

\[
0\le r\le\left\lfloor\frac{q-2}{2}\right\rfloor,
\]

there are legal depth-\(q\) even and odd targets forcing a duplicated common tail. Per orientation the exact forced count is

\[
D_q=\sum_r(2r+1)(q-1-r),
\]

namely

\[
D_{2t}=\frac{t(8t^2-3t+1)}6,\qquad
D_{2t+1}=\frac{t(8t^2+3t+1)}6
=\frac16q^3+O(q^2).
\]

This only refutes an all-balanced literal closure. Every target used in this obstruction is doubly missed and already covered by the swapped-baseline core, so a hybrid atlas remains possible.

A second attempted escape also fails locally. An odd rectangle can borrow the rays of the next even seam by inserting its two old corners; the resulting interval has the exact desired maximum. But one inserted corner raises a high coordinate by one and therefore contaminates every direct cross-rectangle of that even seam. The construction transfers the conflict rather than eliminating it.

The alternative triangular-fold route has a separate scoped obstruction: in the canonical outer-fan realization, \(D_x=(x+1,x)\) is the unique height-\(x\) provider for \([0,x+1]\times[0,x]\). Deleting the inherited diagonal before the next lift destroys one forced boundary witness for every \(x\), so the hoped-for \(o(R)\)-per-level pruning recurrence is invalid unless all those witnesses are rerouted.

## Exact remaining scope

The next unproved statement is a hybrid atlas lemma:

> For fixed \(0<\alpha\le1/3\), arrange the residual complementary line segments around the swapped-baseline blocks so every line-easy target through \(q=\lfloor\alpha m\rfloor\) receives either an intact line witness or one of the proved spill transfers, using \(o(m^3)\) repeated occurrences.

Pointwise cross-foliation identities do not prove this: successive points move to different block labels and acquire negative arm parameters, so contiguity is lost.

Even that lemma would only finish one equal-box upper band. The compact theorem would still require:

1. all remaining upper depths without additive slab resets;
2. an integral lower-factor/pinning construction, or a direct literal word;
3. uniform extension to \(\delta R\le\ell_i\le CR\).

Accordingly, no bound \(g_4=w_4+o(R^3)\) or new asymptotic OR coefficient is claimed. The proved advance is the spill-completed reset-free portal theorem and the exact localization of the next hybrid obstruction.

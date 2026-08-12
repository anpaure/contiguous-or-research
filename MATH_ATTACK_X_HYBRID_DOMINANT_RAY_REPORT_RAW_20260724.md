The hybrid route yields a genuine reduction: the full three-box theorem is unnecessary. It is enough to solve three-chain boxes in the strongly anisotropic plateau sector where one side is at least twice both others.

The earlier idea of merely excluding the cubic ray was valid bookkeeping but not a real weakening: face extension from \(((L-1)h,Lh,Lh)\) recovers the cubic ray with normalized loss at most \(2/L\). The recursive construction below avoids that redundancy.

## Dominant-ray reduction

Let \(g_3(a,b,c)\) be the minimum nonzero contiguous-maximum word length for \([0,a]\times[0,b]\times[0,c]\), and let \(w_3\) be its width.

The sole unproved input is:

> **Dominant RAY — UNPROVED.** For every primitive triple
> \[
> 0<a<b,\qquad c>2b,
> \]
> one has
> \[
> g_3(at,bt,ct)=(at+1)(bt+1)+o_{a,b,c}(t^2).
> \tag{DRAY}
> \]

Here the width is exactly \((at+1)(bt+1)\), since \(ct\ge at+bt\), placing the middle coefficient on the full plateau.

The strict scalene sector suffices. The face-extension lemma makes the set of valid rays projectively closed, so (DRAY) extends to the closed cone
\[
0<a\le b,\qquad c\ge2b.
\tag{D}
\]
This cone is not projectively dense in the positive simplex, so unlike “all non-diagonal rays,” it does not recover balanced three-boxes automatically.

### Exact recursive decomposition

For \(P_h(u)=1+u+\cdots+u^h\), the outer-hook identity is
\[
P_r(u)P_s(u)
=
P_{r+s}(u)+uP_{r-1}(u)P_{s-1}(u),
\qquad 1\le r\le s.
\tag{1}
\]

Take a residual four-box, sort its heights as
\[
h_1\le h_2\le h_3\le h_4,
\]
and apply (1) to its two largest factors.

- Emit the three-box
  \[
  (x,y,z)=(h_1,h_2,h_3+h_4).
  \]
- Recurse on the translated residual four-box with heights
  \[
  h_1,\ h_2,\ h_3-1,\ h_4-1,
  \]
  after re-sorting.
- When at most one height remains positive, emit that terminal chain as a degenerate three-box.

Every emitted child satisfies
\[
\boxed{z=h_3+h_4\ge2h_2=2\max(x,y).}
\tag{2}
\]

Thus every nondegenerate child lies in the dominant cone.

If the parent side sum is \(S\), each nonterminal step reduces the residual sum by two. Hence the number \(N\) of children obeys
\[
\boxed{N\le\left\lfloor\frac S2\right\rfloor+1.}
\tag{3}
\]

### Exact width accounting

After \(j\) peeling steps, the residual bottom rank has increased by \(j\), while its side sum has fallen from \(S\) to \(S-2j\). Iterating (1) gives an exact polynomial identity
\[
\prod_{i=1}^4P_{\ell_i}(u)
=
\sum_{j=0}^{N-1}
u^jP_{x_j}(u)P_{y_j}(u)P_{z_j}(u).
\tag{4}
\]

For \(r=\lfloor S/2\rfloor\),
\[
r-j=\left\lfloor\frac{S-2j}{2}\right\rfloor
=\left\lfloor\frac{x_j+y_j+z_j}{2}\right\rfloor.
\]
Therefore, for both parities and arbitrary Boolean-chain bottom shifts,
\[
\boxed{
w_4(\boldsymbol\ell)=\sum_{j=0}^{N-1}w_3(x_j,y_j,z_j).
}
\tag{5}
\]

This is an exact integral partition, not fractional width averaging.

Each child is a literal product of three saturated chains. Its local word therefore maps directly to a Boolean OR word. Every child after the first has a nonzero shifted origin, so
\[
\boxed{
g_4(\boldsymbol\ell)
\le (N-1)+\sum_{j=0}^{N-1}g_3(x_j,y_j,z_j).
}
\tag{6}
\]
A nonempty Boolean parent minimum costs at most one additional anchor.

## Uniform \(o(R^3)\) parent error

Fix \(C\). Consider every parent with
\[
0\le\ell_i\le CR.
\]
Then
\[
N\le2CR+1,\qquad z_j\le2CR.
\]

Fix \(\varepsilon>0\).

For children with \(x_j<\varepsilon R\), the elementary slice word gives
\[
g_3(x_j,y_j,z_j)+1
\le(x_j+1)(y_j+z_j+1)
\le(\varepsilon R+1)(3CR+1).
\]
Their total full cost is therefore
\[
O_C(\varepsilon R^3+R^2).
\tag{7}
\]

Every remaining child has
\[
\varepsilon R\le x_j\le y_j\le z_j/2,\qquad z_j\le2CR.
\]
Dominant RAY, finite-mesh uniformization, and face extension give
\[
g_3(x_j,y_j,z_j)-w_3(x_j,y_j,z_j)
\le\eta_{\varepsilon,C}(R)R^2,
\qquad \eta_{\varepsilon,C}(R)\to0.
\]
Since \(N=O_C(R)\), their total excess is \(o_{\varepsilon,C}(R^3)\).

Combining this with (5)–(7) and the \(O_C(R)\) anchors,
\[
\limsup_{R\to\infty}
\sup_{0\le\ell_i\le CR}
\frac{(g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell))_+}{R^3}
=O_C(\varepsilon).
\]
Letting \(\varepsilon\downarrow0\),
\[
\boxed{
\sup_{0\le\ell_i\le CR}
\frac{(g_4-w_4)_+}{R^3}\longrightarrow0.
}
\tag{8}
\]

Notably, no lower compactness cutoff is needed.

## Global \(o(W)\) aggregation

Split the Boolean coordinates into four balanced blocks, choose arbitrary SCDs, and put
\[
R=\sqrt{k},\qquad W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]
The number of four-chain parents is
\[
B_4=\Theta\!\left(\frac{W(k)}{R^3}\right).
\tag{9}
\]

Process every parent with \(\max_i\ell_i\le CR\) by the recursive decomposition. Equation (5) gives exact global width:
\[
\sum_{\text{long parents}}w_4
+\sum_{\text{recursive children}}w_3
=W(k).
\tag{10}
\]

By (8), the total nonlong excess is
\[
B_4\,o_C(R^3)=o_C(W(k)).
\]
All shifted child origins cost
\[
O_C(B_4R)=O_C(W(k)/R^2)=o(W(k)),
\]
and parent minima cost \(O(B_4)=o(W(k))\).

For parents with some \(\ell_i>CR\), the crude bound
\[
g_4(\boldsymbol\ell)+1
\le\left(1+\sum_i\ell_i\right)^3
\]
and the SCD Gaussian height tail give
\[
\sum_{\max\ell_i>CR}(g_4+1)
=O(e^{-cC^2}W(k))
\]
after weakening the absolute constant \(c>0\) if necessary.

Consequently,
\[
\nu(k)
\le W(k)+o_C(W(k))+O(e^{-cC^2}W(k)).
\]
First let \(k\to\infty\), then \(C\to\infty\). Thus (DRAY) implies
\[
\boxed{
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
}
\]

## Sharpness and remaining gap

The factor \(2\) is sharp for recursive pair-hook decompositions. Starting from \((R,R,R,R)\), the recursion alternately emits
\[
(r,r,2r),\qquad (r-1,r-1,2r),
\]
for \(r=R,\ldots,1\). Hence \(\Theta(R)\) children have dominance ratio equal to or arbitrarily close to \(2\); no fixed threshold \(2+\eta\) can replace \(2\) while relegating only \(o(R)\) children to crude treatment.

The dominant local theorem remains unproved. The existing hook word has length
\[
(x+1)(y+z+1)-1,
\]
whereas \(w_3=(x+1)(y+1)\), leaving exact excess
\[
(x+1)z-1=\Theta(R^2)
\]
on every compact dominant ray. Thus none of the audited slice, face-extension, or independently reset slab constructions supplies (DRAY).

This is a direct literal-word route. It neither proves nor uses MWB, exact-wreath overload, or labelled common-owner synchronization.

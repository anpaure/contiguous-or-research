# Independent audit of the compact three-box aggregation theorem

Date: 2026-07-24

## 1. Verdict

The conditional reduction is valid.  Let (R=\sqrt{k}), split the Boolean
coordinates into three balanced blocks, and use an arbitrary symmetric-chain
decomposition in each block.  If, for every fixed (0<\delta<C<\infty),

\[
 g_3(p,q,r)
 \le w(p,q,r)+\eta_{\delta,C}(R)R^2,
 \qquad
 \delta R\le p,q,r\le CR,
\tag{CB}
\]

uniformly with \(\eta_{\delta,C}(R)\to0\), then

\[
 \nu(k)=(1+o(1))W(k).
\]

The claimed exceptional-box estimates have the right normalization:

* boxes with a side below \(\delta R\) cost
  (O(\delta W(k))+O(W(k)/\sqrt{k}));
* boxes with a side above (CR) cost
  (O(e^{-cC^2}W(k))), after harmlessly weakening (c>0);
* the compact-box errors total (o(W(k))) for fixed \(\delta,C\).

Two bookkeeping details must be explicit in a proof.

1. A product box whose common Boolean minimum is nonempty needs one literal
   anchor entry for its local origin.  The total anchor cost is only
   (O(W(k)/k)).
2. Take limits in the order: fix \(\delta,C\), let (k\to\infty), then let
   \(\delta\downarrow0\) and (C\uparrow\infty).  No uniformity of
   \(\eta\) in moving \(\delta,C\) is assumed.

The theorem remains conditional because (CB) is unproved.  Existing
three-box lower bounds force a linear excess on cubic boxes, but do not yet
force a quadratic excess, so they do not contradict (CB).

## 2. The exact slice word

Let (0\le a\le b\le c).  The rectangle
([0,a]\times[0,c]) has the hook SCD

\[
\begin{aligned}
D_t={}&(t,0),(t,1),\ldots,(t,c-t),\\
     &(t+1,c-t),\ldots,(a,c-t),
\qquad 0\le t\le a.
\end{aligned}
\tag{2.1}
\]

The (a+1) hooks partition all ((a+1)(c+1)) rectangle points.  Pair the
full chain ([0,b]) with each (D_t).  The standard suffix--prefix word for
two chains has length

\[
 b+|D_t|.
\]

Summing over the hooks gives

\[
 (a+1)b+(a+1)(c+1)=(a+1)(b+c+1).
\tag{2.2}
\]

Only the gadget containing the global local origin contains a zero entry;
delete it.  Therefore

\[
 \boxed{g_3(a,b,c)\le(a+1)(b+c+1)-1.}
\tag{2.3}
\]

This is the best coordinate permutation of the previously audited hook
bound.  It remains exact when (a=0), reducing to
(g_2(b,c)=b+c).

## 3. Product boxes and exact width additivity

Split

\[
 [k]=X_1\sqcup X_2\sqcup X_3,
 \qquad |X_i|=k_i,
 \qquad |k_i-k_j|\le1.
\]

For a chain (C_i) in an SCD of (2^{X_i}), let (a_i) be its bottom
rank and (p_i=k_i-2a_i) its height.  The three-chain product box has rank
polynomial

\[
 \prod_{i=1}^3(1+z+\cdots+z^{p_i}).
\]

Its Boolean ranks range from (A=\sum_i a_i) to
(A+\sum_i p_i=k-A).  Hence its members in global rank
(\lfloor k/2\rfloor) are exactly its local central-rank members, because

\[
 \lfloor k/2\rfloor-A
 =\left\lfloor\frac{\sum_i p_i}{2}\right\rfloor.
\tag{3.1}
\]

Products of chains partition the Boolean cube.  Their central coefficients
therefore satisfy the exact identity

\[
 \boxed{
 \sum_{C_1,C_2,C_3}w(p_1,p_2,p_3)
 =\binom{k}{\lfloor k/2\rfloor}=W(k).}
\tag{3.2}
\]

No asymptotic estimate and no special choice of SCD is involved.

## 4. Number and moments of the boxes

An SCD of an (s)-cube contains exactly

\[
 B_s=\binom{s}{\lfloor s/2\rfloor}
\tag{4.1}
\]

chains.  Thus the number of three-chain boxes is

\[
 B=B_{k_1}B_{k_2}B_{k_3}.
\]

Stirling's formula gives

\[
 \boxed{B=\Theta(W(k)/k)=\Theta(W(k)/R^2).}
\tag{4.2}
\]

The chain-height multiset is also independent of the SCD.  The number of
chains with bottom rank (a), and hence height (s-2a), is

\[
 \binom{s}{a}-\binom{s}{a-1}.
\tag{4.3}
\]

Telescoping (4.3) and the central-binomial Gaussian ratio bound give, for
each fixed integer (j\ge0),

\[
 \sum_{C}(1+p(C))^j=O_j(B_s s^{j/2}).
\tag{4.4}
\]

The needed truncated form is, for (j=0,1,2),

\[
 \sum_{C:p(C)>C_0\sqrt{k}}(1+p(C))^j
 \le K_j B_s k^{j/2}(1+C_0)^{j+1}e^{-cC_0^2},
\tag{4.5}
\]

uniformly for the balanced block sizes.  Polynomial factors in (C_0) can
be absorbed by decreasing (c) when (C_0\ge1).

## 5. Thin boxes

Classify a box as thin if some side (p_i<\delta R).  The sorted-side slice
bound implies, for every chosen coordinate (i),

\[
 g_3(p_1,p_2,p_3)+1
 \le (p_i+1)(1+p_1+p_2+p_3)
\tag{5.1}
\]

whenever (p_i) is merely known to be an upper bound for the minimum side.
Indeed, if (x=\min p_j\le p_i), then

\[
 (x+1)(1+\textstyle\sum_jp_j-x)
 \le(p_i+1)(1+\textstyle\sum_jp_j).
\]

For one fixed thin coordinate,

\[
 \sum_{C_i:p_i<\delta R}(p_i+1)
 \le(\delta R+1)B_{k_i},
\]

and similarly the squared sum is at most
((\delta R+1)^2B_{k_i}).  Factorizing the other two chain sums and using
(4.4) yields

\[
 O\!\left(B(\delta R^2+R+1)\right)
 =O(\delta W(k))+O(W(k)/R).
\tag{5.2}
\]

A union bound over the three possible thin coordinates changes only the
constant.  This proves the claimed

\[
 \boxed{O(\delta W(k))+O(W(k)/\sqrt{k})}
\tag{5.3}
\]

full-length cost, rather than merely an excess estimate.

## 6. Long boxes

For every height triple, (2.3) implies the crude symmetric bound

\[
 g_3(p,q,r)+1\le(1+p+q+r)^2.
\tag{6.1}
\]

If a chosen coordinate exceeds (CR), expand the square in (6.1), apply
the truncated moments (4.5) in that coordinate and the ordinary moments
(4.4) in the other two, and then sum over the three choices.  This gives

\[
 O\!\left(BR^2(1+C)^3e^{-cC^2}\right)
 =O(e^{-c'C^2}W(k))
\tag{6.2}
\]

for another absolute (c'>0).  Boxes which are both thin and long may be
assigned to the thin class first; alternatively, double-counting them in
the two upper bounds is harmless.

## 7. Compact boxes and anchors

The remaining boxes satisfy

\[
 \delta R\le p_i\le CR\qquad(i=1,2,3).
\]

By (CB), their summed local error is at most

\[
 \eta_{\delta,C}(R)R^2 B=O(\eta_{\delta,C}(R)W(k))=o(W(k))
\tag{7.1}
\]

for fixed (\delta,C).  Their main widths sum to at most the exact total
(W(k)) from (3.2).

One local issue is easy to miss.  A product box has common Boolean minimum

\[
 B_{C_1,C_2,C_3}=C_{1,0}\cup C_{2,0}\cup C_{3,0}.
\]

Adding this base to every local word entry transfers every nonzero local
target witness.  If the base itself is nonempty, prepend it literally to
cover the local origin.  This costs at most one entry per box, hence

\[
 O(B)=O(W(k)/k)=o(W(k)).
\tag{7.2}
\]

The unique global-empty target is not required.

## 8. Limit accounting

Concatenate one anchored local word for every product box.  All witnesses
remain within their own block.  Sections 3--7 give

\[
\begin{aligned}
 \nu(k)\le W(k)
 &+O(\delta W(k))+O(W(k)/\sqrt{k})\\
 &+O(e^{-cC^2}W(k))
 +O(\eta_{\delta,C}(\sqrt{k})W(k))
 +O(W(k)/k).
\end{aligned}
\tag{8.1}
\]

For fixed (\delta,C), let (k\to\infty).  Then

\[
 \limsup_{k\to\infty}\frac{\nu(k)}{W(k)}
 \le1+O(\delta)+O(e^{-cC^2}).
\tag{8.2}
\]

Now let (\delta\downarrow0) and (C\uparrow\infty).  Together with the
central-width lower bound, this proves the conditional coefficient-one
conclusion.

The order of limits is essential: (CB) supplies convergence separately for
each fixed compactness window, not uniformly over a moving window.

## 9. Conditional status

The product-box width identity, slice construction, height distributions,
thin/long estimates, anchoring cost, and limit passage all pass audit.

What remains is exactly the local compact-box hypothesis (CB).  The proved
cube lower bound

\[
 g_3(R,R,R)\ge w(R,R,R)+\Omega(R)
\]

is compatible with an (o(R^2)) error.  A quadratic lower bound is an active
but still incomplete obstruction program.  Accordingly, this is a clean
conditional reduction, not an unconditional proof of the original
constant-one theorem.

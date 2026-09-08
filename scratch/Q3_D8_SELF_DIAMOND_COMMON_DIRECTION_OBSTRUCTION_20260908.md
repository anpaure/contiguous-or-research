# Self-complementary three-diamond rows miss every class-C critical target

2026-09-08. Author: direct_route. Pure analysis; no computation.
Root and appendix_a independently read and passed the full mathematical
argument, including the direction proof, the 840/336 physical-orbit counts,
and the two full normal forms. The direction argument below rules out
coverage by the entire stated self-diamond family, including full endpoint
restorations. It does not apply to generic diamond/complement bundles.

## 1. The family and its two structural identities

Coordinates are \(E=\mathbb F_2^3\), with addition written \(+\).
Let \(H\) be an affine four-point plane, let \(H_0\) be its direction
space, and choose \(v\notin H_0\), so the complementary shore is
\(H+v\). Write \(H=\{a,b,c,d\}\), with \(a\ne b\), and put
\(h=a+b=c+d\).

The first shore's full geodesic has increment word
\[
                 C=(a,p_1,q_1,p_2,q_2,p_3,q_3,b),
\]
and the second, before translation by \(v\), has word
\[
                 D=(a,q_1,p_1,q_2,p_2,q_3,p_3,b).                  \tag{1}
\]
Each coordinate is used exactly twice. Each \(p_i\ne q_i\), and
\[
                         (p_3,q_3)=(q_1+h,p_1+h).                 \tag{2}
\]
The unordered middle pair is either \(\{c,d\}\), for the Hamilton
case, or \(\{a,b\}\), for the double-edge case. Thus translation
by \(h\) reverses the middle ordered pair. Equation (2), together
with \(a+h=b\), shows that translating either entire word by \(h\)
gives its reversal. For the shore states this says
\[
                D_{8-r}(p+h)=2-D_r(p),
                \qquad C_{8-r}(p+h)=2-C_r(p).                     \tag{3}
\]
In particular value complementation of either full or doubly truncated
row is its coordinate translate by \(h\). Its full translation orbit
is complement closed.

The three reversed adjacent pairs in (1) also imply
\[
                            D_{i+1}-C_i=e_{t_i}
                    \quad(0\le i\le7)                            \tag{4}
\]
for some shore coordinate \(t_i\). Indeed the two paths agree at
every odd rank. If \(i\) is odd, take the next step of \(D\); if
\(i\) is even, their next odd state is the common next state, and
take the next step of \(C\). The same argument includes the endpoints.

## 2. Every rank-seven target has a common direction

A rank-seven target has *direction* \(w\ne0\) if its four unordered
coordinate pairs \(\{p,p+w\}\) have value sums \(2,2,2,1\).

**Theorem.** Every rank-seven target in the full row
\(C\times(D+v)\) has direction \(w=h+v\). The same is consequently
true after either or both endpoints are removed.

Every such target is \(x=(C_i,D_{7-i}+v)\) for some \(0\le i\le7\).
The coordinate \(p\in H\) is paired under \(w\) with
\(p+h+v\in H+v\). By (3)--(4),
\[
 \begin{aligned}
  x(p)+x(p+h+v)
    &=C_i(p)+D_{7-i}(p+h)\\
    &=2+C_i(p)-D_{i+1}(p)\\
    &=2-\mathbf1_{p=t_i}.
 \end{aligned}                                                     \tag{5}
\]
There are therefore three sums equal to two and exactly one equal to
one. Since \(h\in H_0\) and \(v\notin H_0\), \(w\ne0\), as required.

This proof is stronger than a class-multiset calculation: it handles
every permitted word at once and includes all endpoint cells. It does
not depend on the number of distinct critical orbits contributed by a row.

## 3. An explicit omitted target and all 28 class-C orbits

Consider, in coordinate order \(0,\ldots,7\),
\[
                              x=(2,1,1,1,2,0,0,0).                 \tag{6}
\]
Its rank is seven. It has twos at \(0,4\), ones at \(1,2,3\), and
zeros at \(5,6,7\). Under a direction with pair sums \(2,2,2,1\),
each two must be paired with a zero. The two zero partners must differ
by four, just as the two-valued positions do. But the differences among
\(5,6,7\) are \(1,2,3\). Thus (6) has no direction and cannot belong
to any row in the family.

More generally let \(L\) be a Fano line, set \(H_0=L\cup\{0\}\),
and choose \(t\notin H_0\). Put ones at \(L\), twos at \(0,t\),
and zeros at the other three points outside \(H_0\). The difference
of any two zeros lies in \(H_0\setminus\{0\}\), whereas the two-valued
positions differ by \(t\notin H_0\). The same argument excludes every
direction. These are the canonical class-C targets.

There are seven choices of \(L\) and four choices of \(t\), giving
28 different translation orbits. The canonical one-set has xor zero,
and its odd size makes this normalization unique under translation.
Thus the entire self-diamond family omits all 28 class-C critical
orbits, or 224 individual rank-seven targets. In particular one full
orbit and twenty short orbits cannot cover the cube, regardless of
their nominal charge 2384 or their other critical capacities.

## 4. Counts of physical translation orbits (not needed above)

For fixed \(H,v,a,b\), the three unordered diamond edges have degrees
one at \(a,b\) and two at \(c,d\). A loop-free multigraph with these
degrees is either a Hamilton path from \(a\) to \(b\), or the edge
\(ab\) together with two copies of \(cd\).

In the Hamilton case choose which of \(c,d\) is adjacent to \(a\),
choose whether the first edge is incident to \(a\) or to \(b\), choose
its orientation, and choose the middle edge's orientation. There are
\(2\cdot2\cdot2\cdot2=16\) words; (2) forces the third orientation.
In the double-edge case the first and third edge are \(cd\), with
two first orientations and two middle \(ab\) orientations, giving four
words. Thus there are twenty ordered word pairs per \(H,v,a,b\).

There are fourteen affine planes, four complementary translations,
and twelve ordered choices of distinct \(a,b\). The ordered-shore
parameter count is \(14\cdot4\cdot12\cdot20\). Every physical row
has exactly two such descriptions, from exchanging its shores. There
is no further duplication: its abstract seven-by-seven grid determines
the two chain factors up to exchange, every shore coordinate varies,
and the visible first and last states recover the omitted endpoints
and hence the full words. The first coordinates on the two shores
then recover \(v\).

Every translation orbit has size eight. For a short row the minimum
has ones exactly at \(a,a+v\), so any stabilizing translation is zero
or \(v\). Translation by \(v\) would exchange \(C\) and \(D\), but
they differ at rank two. The full row has the same restriction from
its two atoms. Hence the number of short translation orbits is exactly
\[
                  \frac{14\cdot4\cdot12\cdot20}{2\cdot8}=840.     \tag{7}
\]
The same count holds if all endpoints are restored.

A full orbit repairs all 34 axis/coaxis extremes precisely when one
of its two words starts with two equal increments. This is equivalent
to the first diamond edge being incident to \(a\): exactly the forward
Hamilton case. There are eight such oriented words per \(H,v,a,b\),
so the number of eligible full orbits is
\[
                  \frac{14\cdot4\cdot12\cdot8}{2\cdot8}=336.       \tag{8}
\]
Translation supplies every coordinate's axis targets, and (3) supplies
their coaxis complements. Without an initial repeated increment, no
row in the orbit contains a target \(2e_p\).

Under \(\operatorname{GL}(3,2)\), the eligible full orbits have exactly
two normal forms. Translate \(a\) to zero, choose the word starting
with \(aa\) as \(C\), and send the basis \((h,c,v)\) to \((1,2,4)\).
Then \(H=\{0,1,2,3\}\), and the two middle orientations give
\[
                           00223311,\qquad00232311.                 \tag{9}
\]
The partner is obtained by the three swaps in (1). The equality patterns
of positions in these two words differ, so coordinate relabeling cannot
identify them; the first-\(aa\) shore distinguishes it from its partner.

## 5. Scope

The essential hypotheses are the individual complement symmetry (3)
and the interlacing (4). They hold for every self-diamond row specified
here. They need not hold for a generic independent diamond pair and
its separately adjoined complement. The theorem consequently does not
exclude those larger families, arbitrary independent partner chains,
or a general balanced ternary cover. The orbit counts are supplementary;
the explicit omitted target already proves the stated impossibility.

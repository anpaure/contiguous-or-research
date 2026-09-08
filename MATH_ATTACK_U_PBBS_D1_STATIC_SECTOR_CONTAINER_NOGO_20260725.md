# Lane U: the static \(d=1\) sector container is sparse and its advertised ports fail

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

## 0. Outcome

Put

\[
N=2r+1,\qquad B_r=\operatorname{Cat}_r,\qquad W=NB_r,
\qquad H\le A\sqrt r+1,
\]

where \(A>0\) is fixed. The proposed Catalan-dense shared-fusion reservoir
consisting of all \(d=1\) first-deepest-spine sectors is not a family of the
claimed PBBS returns. The implication

\[
d(D)=1
\quad\Longrightarrow\quad
\text{a return of gap }2\operatorname{ht}(D)+1
\]

is false, even for primitive roots. Thus
PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md has been
retracted, and it does not disprove \((RP_A)\).

There is, however, an exact theorem for the static sector atlas. Write the
first-deepest-spine decomposition of a height-\(h\) root as

\[
D=A_0\,1A_1\,1\cdots1A_{h-1}\,1
  0B_{h-1}0\cdots0B_1\,0B_0.                     \tag{0.1}
\]

Let the height of an ordered forest be its maximum relative component
height, with the empty forest having height zero. The formal \(h\)-round
sector shift remains the canonical first-deepest-spine shift at every round
\(0,1,\ldots,h\) if and only if

\[
\boxed{
A_k=\varnothing,\qquad
\operatorname{ht}(B_k)\le k
\quad(0\le k<h).}                                \tag{0.2}
\]

Every root satisfying (0.2) does have a first zero-winding return of gap
\(2h+1\). But if \(\mathcal S_r\) is the union of this protected class over
all \(h\), then, with

\[
\boxed{\kappa=\bigl(\pi^2(\log2)^2\bigr)^{1/3},}
\]

one has the optimized two-container estimate

\[
\boxed{
|\mathcal S_r|
\le 4^r\exp\!\left[-(\kappa-o(1))r^{1/3}\right].} \tag{0.3}
\]

Consequently, even if every physical lift of every protected root is
repaired independently at cost \(O_A(H^2)\), the total charge is

\[
\boxed{N\,O_A(H^2)|\mathcal S_r|=o_A(W).}         \tag{0.4}
\]

So an \(o(H^2)\)-per-packet fusion theorem is neither needed nor the
missing coefficient-one gate on the largest class justified by this static
sector atlas. Outside the protected class the atlas supplies no
identity-phase common ports: for the primitive word \(1110011000\), the
alleged gap-seven endpoint in the same spatial lift has physical label
\(u-4\pmod {11}\), not the starting label \(u\).

This closes the proposed unchanged static \(d=1\) first-deepest-sector
container route. It does not rule out a fusion indexed by the complete,
reframing \(\tau\)-itinerary, and it neither proves nor disproves
\((RP_A)\).

## 1. Exact one-round update and formal itinerary

At the first up-step reaching the maximum, write

\[
D=P\,1\,R\,0\,S.
\]

For (0.1),

\[
\begin{aligned}
P&=A_0\,1A_1\cdots1A_{h-1},\\
R&=0B_{h-1}0\cdots0B_1,\\
S&=B_0.
\end{aligned}                                    \tag{1.1}
\]

The exact two-step quotient map is

\[
\tau D=S\,1\,P\,0\,R,
\]

and hence

\[
\tau D
=B_0\,1A_0\,1A_1\cdots1A_{h-1}\,0
 0B_{h-1}0\cdots0B_1.                            \tag{1.2}
\]

If the displayed old spine is still the canonical first deepest spine,
the sector update is

\[
A'_0=B_0,\qquad A'_i=A_{i-1}\quad(1\le i<h),     \tag{1.3}
\]

and

\[
B'_i=B_{i+1}\quad(0\le i<h-1),\qquad
B'_{h-1}=\varnothing.                            \tag{1.4}
\]

Iterating these identities formally gives, at round \(j\),

\[
A_i^{[j]}=
\begin{cases}
B_{j-1-i},&i<j,\\
A_{i-j},&i\ge j,
\end{cases}                                      \tag{1.5}
\]

and

\[
B_i^{[j]}=
\begin{cases}
B_{i+j},&i+j<h,\\
\varnothing,&i+j\ge h.
\end{cases}                                      \tag{1.6}
\]

The brackets emphasize that (1.5)--(1.6) describe the canonical PBBS
factorization only while no transported earlier forest pre-empts the
displayed spine.

## 2. Exact protection criterion

### Theorem 2.1

The formal sectors (1.5)--(1.6) are the canonical first-deepest-spine
sectors of \(\tau^jD\) for every \(0\le j\le h\) if and only if (0.2)
holds.

### Proof: sufficiency

Assume (0.2). All original \(A\)-forests are empty. Once an original
\(B_k\) has crossed to the earlier side at round \(j\), formula (1.5)
places it at depth

\[
i=j-1-k.
\]

Every leaf in that forest therefore has total depth at most

\[
i+\operatorname{ht}(B_k)
\le j-1-k+k=j-1<h.                               \tag{2.1}
\]

Thus no forest preceding the displayed spine reaches height \(h\). The
spine itself still reaches height \(h\), so it remains the first deepest
spine.

Before crossing the spine, an original \(B_k\) remains a later forest.
The original height-\(h\) condition gives

\[
\operatorname{ht}(B_k)\le h-k.                   \tag{2.2}
\]

At round \(j\le k\), formula (1.6) places it at depth \(k-j\), so its
total height is at most \(h-j\le h\). A tie is harmless because this
forest follows the displayed spine. Hence the formal itinerary is
canonical at every round.

### Proof: necessity

Assume the formal itinerary is canonical through round \(h\). If some
\(A_k\) is nonempty, take

\[
j=h-1-k.
\]

Formula (1.5) places \(A_k\) in the earlier sector at depth \(h-1\).
Every nonempty forest has relative height at least one, so it reaches total
height at least \(h\) before the displayed spine child. The displayed
spine is then not first deepest, a contradiction. Thus every \(A_k\) is
empty.

If \(\operatorname{ht}(B_k)\ge k+1\), then at round \(h\), formula (1.5)
places \(B_k\) in the earlier sector at depth \(h-1-k\). It reaches total
height at least

\[
(h-1-k)+(k+1)=h,
\]

again before the displayed spine. This is a contradiction. Hence
\(\operatorname{ht}(B_k)\le k\) for all \(k\), proving (0.2).
\(\square\)

The condition \(B_0=\varnothing\), equivalently \(d(D)=1\), is only the
\(k=0\) member of (0.2); it does not imply the remaining inequalities or
the vanishing of the \(A\)-forests.

### Theorem 2.2 (exact partial-horizon atlas)

More generally, fix \(0\le q\le h\). The formal sectors are canonical
through rounds \(0,1,\ldots,q\) if and only if, for every \(0\le k<h\),

\[
\operatorname{ht}(A_k)
\le\max\{h-k-q-1,0\},                             \tag{2.3}
\]

and

\[
\operatorname{ht}(B_k)
\le\min\{h-k,h-q+k\}
=h-\max\{k,q-k\}.                                 \tag{2.4}
\]

Indeed, an original \(A_k\) is at earlier depth \(k+j\) at round \(j\);
the strongest strict-height condition occurs at
\(j=\min\{q,h-1-k\}\), giving (2.3). An original \(B_k\) stays at later
depth \(k-j\) for \(j\le k\), where its strongest condition is the
original bound \(h-k\). For \(j>k\), it is at earlier depth \(j-1-k\);
the strongest condition occurs at \(j=q\), giving \(h-q+k\). This proves
(2.4), and the same depth comparisons prove sufficiency.

Let \(C_L(z)\) be the generating function for ordered Dyck forests of
height at most \(L\), with

\[
C_0(z)=1,\qquad C_L(z)=\frac1{1-zC_{L-1}(z)}.
\]

The exact number of semilength-\(r\), height-\(h\) roots certified through
round \(q\) is therefore

\[
\boxed{
[z^{r-h}]
\prod_{k=0}^{h-1}
C_{\max\{h-k-q-1,0\}}(z)\,
C_{h-\max\{k,q-k\}}(z).}                          \tag{2.5}
\]

At \(q=h\), (2.3) forces all \(A_k\) empty and (2.4) becomes
\(\operatorname{ht}(B_k)\le\min\{k,h-k\}\), where the second cap is the
original height condition. Thus Theorem 2.2 specializes exactly to
Theorem 2.1. Partial protection with \(q<h\) does not certify the
advertised height-\(h\) endpoint and therefore does not restore the false
return theorem.

## 3. Return law on the protected class

In this section \(|A_i|\) and \(|B_i|\) denote forest edge counts,
equivalently half the lengths of their contour words. For a canonical
first-deepest-spine factorization, put

\[
d(D)=2|B_0|+1,\qquad
\delta(D)=h+2\sum_{i=0}^{h-1}|A_i|.              \tag{3.1}
\]

Let \(D_j=\tau^jD\) for a protected root and define

\[
C_j=\sum_{t=0}^{j-1}d(D_t),\qquad C_0=0.
\]

Equations (1.5)--(1.6), together with \(A_i=\varnothing\), give

\[
d(D_j)=2|B_j|+1\quad(0\le j<h),                  \tag{3.2}
\]

\[
\delta(D_j)=h+2\sum_{t<j}|B_t|
\quad(0\le j\le h),                              \tag{3.3}
\]

and

\[
C_j=j+2\sum_{t<j}|B_t|.                          \tag{3.4}
\]

Therefore

\[
\delta(D_j)-C_j=h-j>0\quad(j<h),\qquad
\delta(D_h)=C_h.                                 \tag{3.5}
\]

After \(j\) applications of the even-time skew product, the spatial root
is \(u-C_j\pmod N\); the following odd step adds \(\delta(D_j)\).
Equation (3.5) gives a return at time \(2h+1\) and excludes every earlier
odd return. Moreover, since a protected tree has

\[
r=h+\sum_{k=0}^{h-1}|B_k|,
\]

one has

\[
0<C_j<C_h
=h+2\sum_k|B_k|
=2r-h<N
\quad(0<j\le h).                                 \tag{3.6}
\]

Thus no earlier even time returns. The return is consecutive and has zero
winding.

## 4. Optimized entropy/container bound

Let \(s_{r,h}\) be the number of protected semilength-\(r\) roots of
height \(h\).

### Container I: forced initial run

Because every \(A_k\) is empty, (0.1) begins with \(h\) consecutive
up-steps. Forgetting all subsequent Dyck and height restrictions gives

\[
s_{r,h}
\le {2r-h\choose r-h}
\le 2^{2r-h}
=4^r\exp(-h\log2).                               \tag{4.1}
\]

### Container II: height ceiling

Let \(M_h\) be the adjacency matrix of the path graph on
\(\{0,1,\ldots,h\}\). Every height-at-most-\(h\) Dyck word is a
length-\(2r\) walk from zero to zero, so

\[
s_{r,h}
\le (M_h^{2r})_{0,0}
\le \|M_h\|^{2r}
=\left(2\cos\frac{\pi}{h+2}\right)^{2r}.          \tag{4.2}
\]

Using \(\cos x\le e^{-x^2/2}\) for \(0\le x\le\pi/2\),

\[
s_{r,h}
\le4^r\exp\!\left(-\frac{\pi^2r}{(h+2)^2}\right). \tag{4.3}
\]

Combining the two independent containers yields

\[
s_{r,h}\le4^r\exp[-M_r(h)],
\quad
M_r(h)=\max\!\left\{
h\log2,\frac{\pi^2r}{(h+2)^2}\right\}.            \tag{4.4}
\]

Put

\[
\kappa=\bigl(\pi^2(\log2)^2\bigr)^{1/3}.
\]

Uniformly in \(1\le h\le r\),

\[
\inf_h M_r(h)\ge(\kappa-o(1))r^{1/3}.             \tag{4.5}
\]

Indeed, if \(h<r^{1/6}\), the second term in (4.4) is
\(\Omega(r^{2/3})\). If \(h\ge r^{1/6}\), then

\[
\begin{aligned}
M_r(h)
&\ge
\left[
(h\log2)^2\frac{\pi^2r}{(h+2)^2}
\right]^{1/3}\\
&=\kappa r^{1/3}
\left(\frac h{h+2}\right)^{2/3}
=\bigl(\kappa-o(1)\bigr)r^{1/3}.
\end{aligned}
\]

Summing (4.4) over at most \(r\) heights and absorbing
\(\log r=o(r^{1/3})\) proves (0.3).

The Wallis lower bound

\[
B_r\ge c_0\,4^r r^{-3/2}
\]

then gives, for every fixed \(K\),

\[
\boxed{|\mathcal S_r|=o(B_r/r^K).}               \tag{4.6}
\]

This is the relevant entropy statement: the only roots for which the
unchanged static \(h\)-round sector pattern certifies common return ports
lose \((\kappa-o(1))r^{1/3}\) in the exponent relative to the full
Catalan scale.

## 5. Consequence for literal seam cost

Suppose, generously, that every physical lift of every root in
\(\mathcal S_r\) is charged an independent repair of at most
\(C_AH^2\) letters. There are at most \(N\) physical lifts per root, so
the total charge is at most

\[
C_A N H^2|\mathcal S_r|.
\]

As \(H^2=O_A(r)\), division by \(W=NB_r\) and (4.6) give

\[
\frac{C_A N H^2|\mathcal S_r|}{W}
\le C'_A r\frac{|\mathcal S_r|}{B_r}
=o_A(1).                                         \tag{5.1}
\]

Thus (0.4) holds. More generally, any per-lift cost
\(\exp(o(r^{1/3}))\) is harmless on this protected class. There is no
coefficient-one gain to be obtained by compressing its quadratic repair
to \(o(H^2)\); the quadratic repair is already negligible in aggregate.

## 6. Identity-phase failure and the exact full-deck balance

Take

\[
D_0=1110011000,\qquad r=5,\qquad N=11.
\]

It is primitive, has height three, and has \(d(D_0)=1\). Exact
applications of \(\tau D=S1P0R\) give

\[
\begin{array}{c|c|c}
D_j&\delta(D_j)&d(D_j)\\ \hline
1110011000&3&1\\
1110001100&3&5\\
1100111000&7&1
\end{array}
\qquad D_3=D_0.                                  \tag{6.1}
\]

At the alleged height-three return, the accumulated even-time displacement
is

\[
C_3=1+5+1=7,
\]

whereas \(\delta(D_3)=3\). The following odd endpoint therefore has label

\[
u-C_3+\delta(D_3)=u-4\not\equiv u\pmod {11}.      \tag{6.2}
\]

So the two advertised ports in the same spatial lift are not occurrences
of the same physical coordinate. An identity-phase seam which identifies
them does not repair a residence; it joins events with different labels.

For completeness, repeating (6.1) twice gives
\(C_6=14\equiv3=\delta(D_6)\pmod {11}\). Direct comparison at
\(j=1,\ldots,5\) excludes every earlier odd or even equality. The first
return is at gap \(13\), not gap \(7\).

The example does not prove that every unprotected root fails. It proves
the exact statement needed here: \(d=1\), primitivity, and the initial
first-deepest sector table do not determine an identity-phase return port
and hence cannot define the claimed Catalan-dense residence family.

There is an exact full-deck qualification. For an arbitrary quotient
segment

\[
D_0=D,\ D_1=\tau D,\ldots,D_q=\tau^qD,
\]

put

\[
C_q(D)=\sum_{j=0}^{q-1}d(D_j),\qquad
\Delta_q(D)=\delta(D_q)-C_q(D)\pmod N.             \tag{6.3}
\]

The terminal odd event of the lift starting in phase \(u\) has physical
label

\[
\boxed{u+\Delta_q(D)\pmod N.}                     \tag{6.4}
\]

Thus, as \(u\) runs through the complete spatial deck, the start-to-end
label incidence is exactly the permutation matrix of the translation
\(u\mapsto u+\Delta_q(D)\). The deck is integrally endpoint-balanced even
when \(\Delta_q(D)\ne0\): to match physical label \(u\), use the endpoint
from starting phase \(u-\Delta_q(D)\).

Equation (6.4) is only a port-inventory statement. It does not construct a
Johnson seam, a contiguous-OR word, or a return of one coordinate inside
one lifted trajectory. It shows that the example (6.2) refutes
identity-phase fusion but does not refute a genuinely cross-phase,
full-deck braid.

The endpoint offset is also not determined by coarse sector sizes and
heights. For \(f\ge2\) and \(0\le a\le f-2\), put

\[
F_a=(10)^a1100(10)^{f-a-2},\qquad
D_a=11100F_a0.                                    \tag{6.5}
\]

All \(D_a\) are primitive height-three roots with \(d(D_a)=1\), and all
have the identical initial sector profile

\[
A_0=A_1=A_2=B_0=B_2=\varnothing,\qquad
|B_1|=f,\quad\operatorname{ht}(B_1)=2.            \tag{6.6}
\]

Exact block rotation gives

\[
C_3(D_a)=2f+3,\qquad
\delta(\tau^3D_a)=2a+3,
\]

and hence

\[
\boxed{\Delta_3(D_a)=-2(f-a)\pmod {2f+7}.}        \tag{6.7}
\]

These are \(f-1=\Theta(r)\) distinct offsets. Therefore a container whose
port pattern fixes one phase displacement cannot be indexed merely by the
sector sizes and heights; it needs recursive first-maximum data or an
occurrence-specific deck translation. At Gaussian scale,
when \(H=H_A=\lceil A\sqrt r\rceil\),
\(\Theta(r)=\Theta_A(H_A^2)\), so a nonparametric catalogue would already
need quadratically many phase classes. Under the weaker standing bound
\(H\le A\sqrt r+1\), the valid relation is only
\(r=\Omega_A(H^2)\). The translation formula (6.4) is the exact mechanism
by which an occurrence-specific full-deck scheme can escape that catalogue
count.

## 7. Independent audit of the decisive steps

1. **Canonicality.** At round \(h-1-k\), a nonempty \(A_k\) appears at
   earlier depth \(h-1\); at round \(h\), a \(B_k\) of height at least
   \(k+1\) appears at earlier depth \(h-1-k\). These are exact equality
   cases and show necessity, not merely sufficiency, of (0.2).
2. **Original-height condition.** Later \(B\)-forests use the independent
   bound \(\operatorname{ht}(B_k)\le h-k\); ties occur after the displayed
   spine and are legal.
3. **Return integrality.** On the protected class,
   \(C_h=2r-h<N\), so the endpoint congruence is literal equality and all
   earlier exclusions are valid without winding ambiguity.
4. **Entropy sign.** Both (4.1) and (4.3) are upper bounds, so their
   minimum corresponds to the maximum of their two exponential losses in
   (4.4). The optimized constant is
   \(\kappa=[\pi^2(\log2)^2]^{1/3}\).
5. **Literal scope.** Equation (6.2) compares physical ground-coordinate
   labels inside one fixed spatial lift. The deck translation (6.4)
   balances the label inventory but is not itself a literal seam.
6. **Implication scope.** The theorem closes only the unchanged
   first-deepest-sector container/fusion premise. A full-orbit,
   frame-changing seam or a suitable unprotected subclass could still
   exist. This report makes no claim that \((RP_A)\) is false and no claim
   of coefficient one.

## 8. Final proved and conditional boundary

Proved:

* the exact iff criterion (0.2) for the full formal sector itinerary;
* the partial-horizon criterion and exact coefficient formula
  (2.3)--(2.5);
* the protected-class first return at gap \(2h+1\);
* the optimized entropy/container estimate (0.3);
* negligibility of independent \(O_A(H^2)\) repair on that class; and
* an explicit physical-label obstruction to extending the advertised
  identity-phase ports to all primitive \(d=1\) roots;
* the exact full-deck endpoint permutation (6.4); and
* a \(\Theta(r)\)-offset family with identical coarse sector profiles.

Not proved:

* a classification or Catalan-scale lower bound for the true Gaussian PBBS
  return family;
* \((RP_A)\) or its negation;
* an \(o(H^2)\) braid for arbitrary exact-return packets; or
* coefficient one.

The next legitimate fusion object must be indexed by the complete
canonical \(\tau\)-itinerary, including every first-deepest reframe and the
physical endpoint label, not by the initial \(d=1\) sector data alone.

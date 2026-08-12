# Second-wave lane X: hierarchical product aggregation

Date: 2026-07-24

## 1. Outcome

This lane gives a proper-subcone conditional local gate relative to the
dominant-ray gate from the first wave.

For \(d\ge 1\), let \(g_d(\ell_1,\ldots,\ell_d)\) be the minimum length of a
nonzero contiguous-maximum word for the chain box

\[
Q(\boldsymbol\ell)=\prod_{i=1}^d[0,\ell_i],
\]

and let

\[
w_d(\boldsymbol\ell)
=[u^{\lfloor(\ell_1+\cdots+\ell_d)/2\rfloor}]
\prod_{i=1}^d(1+u+\cdots+u^{\ell_i})
\]

be its width. Put

\[
W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

For the singleton zero box, the convention is
\(g_d(0,\ldots,0)=0\) and \(w_d(0,\ldots,0)=1\).

Fix an integer \(M\ge2\). The only unproved statement used in the new
reduction is the following.

> **Hierarchical ray theorem \(\mathrm{HRAY}_M\) — UNPROVED.** For every
> primitive positive integer triple \((a,b,c)\) satisfying
> \[
> b>Ma,\qquad c>Mb,
> \]
> one has
> \[
> g_3(at,bt,ct)=(at+1)(bt+1)+o_{a,b,c}(t^2).
> \tag{HRAY}
> \]

The displayed main term is the exact width: \(c>Mb\ge2b>a+b\).

### Main conditional theorem

For every fixed integer \(M\ge2\),

\[
\boxed{\mathrm{HRAY}_M\Longrightarrow
\nu(k)=(1+o(1))W(k).}
\tag{1.1}
\]

Thus it is enough to solve all primitive rays in any one chosen fixed,
arbitrarily far doubly anisotropic cone

\[
0<a<\frac bM<\frac c{M^2}.
\]

This is formally weaker in quantified ray-set scope than first-wave DRAY,
which asked for every fixed ray \(0<a<b,\ c>2b\): the hierarchical cone is a
proper subcone. No converse implication between the two statements about the
actual function \(g_3\) is claimed. The proof uses three Boolean coordinate
blocks with
dimensions asymptotic to

\[
\varepsilon^4k,\qquad \varepsilon^2k,\qquad
(1-\varepsilon^2-\varepsilon^4)k,
\tag{1.2}
\]

lets \(k\to\infty\) at fixed \(\varepsilon\), and only then lets
\(\varepsilon\downarrow0\). The total **full literal-word cost**, not merely
the width, of boxes outside the hierarchical cone is

\[
O_M(\varepsilon W(k)).
\tag{1.3}
\]

The lane also proves four structural facts.

1. Arbitrary height-adaptive outer-hook refinements, with mixed-dimensional
   leaves, preserve the middle width exactly.
2. The greedy four-to-three refinement has an exact global leaf and origin
   ledger; all independently paid origins total \(O(W(k)/k)\).
3. Every fixed positive-proportion block split, and every fixed random mixture
   of such splits, puts a positive fraction of exact width in every nonempty
   interior aspect-ratio sector. Random anisotropy cannot erase the balanced
   sector unless the block proportions escape to the boundary.
4. Fully merging many atomic blocks along any binary outer-hook tree merely
   produces an ordinary SCD of the corresponding macroblock. Its height
   histogram is tree-independent, so extra full merge levels create no new
   concentration mechanism.

No unconditional coefficient-one theorem is proved. The sole unproved input
in (1.1) is \(\mathrm{HRAY}_M\). In particular, the existing slice word has
leading relative cost \(1+\varepsilon^{-1}\) on (1.2), and does not prove the
new gate.

## 2. Exact SCD height laws

For \(s\ge0\), let \(c_s(h)\) be the number of height-\(h\) chains in any SCD
of the \(s\)-cube. This number is independent of the chosen SCD. If
\(h\equiv s\pmod2\) and \(a=(s-h)/2\), then

\[
c_s(h)
=\binom{s}{a}-\binom{s}{a-1}
=\frac{2(h+1)}{s+h+2}\binom{s}{(s-h)/2};
\tag{2.1}
\]

otherwise \(c_s(h)=0\). Also

\[
\sum_hc_s(h)=W(s),\qquad
\sum_hc_s(h)(h+1)=2^s.
\tag{2.2}
\]

Two estimates will be used repeatedly.

### Lemma 2.1: lower tail and moments

There are absolute constants \(C\) and, for each fixed \(p\ge0\), \(C_p\)
such that

\[
A_s(T):=\sum_{0\le h\le T}c_s(h)
\le C W(s)\min\left\{1,\frac{(T+2)^2}{s+1}\right\},
\tag{2.3}
\]

and

\[
\sum_hc_s(h)(h+1)^p
\le C_pW(s)(s+1)^{p/2}.
\tag{2.4}
\]

#### Proof

Let \(m=\lfloor s/2\rfloor\). The number of SCD chains of height at least
\(2d\), with the harmless parity adjustment in the odd case, is

\[
\binom{s}{m-d}.
\]

Divide by \(W(s)=\binom{s}{m}\) and write the quotient as the product of its
successive central-binomial ratios. The standard product estimate gives

\[
\frac{\binom{s}{m-d}}{\binom{s}{m}}
\le e^{-d^2/s}.
\tag{2.5}
\]

Summation by parts yields (2.4). For the lower tail, subtract the appropriate
crossing count from \(W(s)\) and use

\[
1-\prod_jr_j\le\sum_j(1-r_j)=O((T+2)^2/(s+1))
\]

for the same successive ratios. This proves (2.3), after enlarging the
constant for \(T\gg\sqrt s\) and for the finite small cases. \(\square\)

### Lemma 2.2: Rayleigh limit

Suppose \(s/k\to\alpha>0\), choose an SCD chain uniformly, and let \(L\) be
its height. Then

\[
\frac{L}{\sqrt k}\Longrightarrow X_\alpha,
\qquad
f_\alpha(x)=\frac{x}{\alpha}e^{-x^2/(2\alpha)},\quad x>0.
\tag{2.6}
\]

Equivalently, \(L/\sqrt s\) tends to the standard Rayleigh density
\(r(y)=ye^{-y^2/2}\). All fixed polynomial moments converge.

#### Proof

For \(h=x\sqrt k\) in a compact positive interval, (2.1) and the local
central-binomial ratio give

\[
\frac{c_s(h)}{W(s)}
=\frac{2}{\sqrt k}\left(
\frac{x}{\alpha}e^{-x^2/(2\alpha)}+o(1)
\right).
\]

The mesh is \(2/\sqrt k\). Equation (2.4), or the Gaussian tail (2.5), gives
uniform integrability. \(\square\)

## 3. Adaptive exact product refinements

Put \(P_h(u)=1+u+\cdots+u^h\).

### Theorem 3.1: adaptive outer-hook refinement

Partition

\[
[k]=X_1\sqcup\cdots\sqcup X_t,
\qquad |X_i|=k_i,
\]

and fix an SCD in every \(2^{X_i}\). A tuple of component chains gives a
literal Boolean product parent \(Q(\boldsymbol\ell)\). Let its Boolean bottom
rank be \(A\) and its side-height sum be \(S\). Then

\[
2A+S=k.
\tag{3.1}
\]

Inside each product parent, make arbitrary choices depending on its realized
height vector and on the current branch. At any node, choose two positive
factors and apply the outer-hook partition. Stop independently on arbitrary
branches, so leaves may have different dimensions.

If a leaf \(\lambda\) has translation rank \(\delta_\lambda\), dimension
\(d_\lambda\), and side heights
\(h_{\lambda,1},\ldots,h_{\lambda,d_\lambda}\), then the leaves form a
literal disjoint partition and

\[
\prod_{i=1}^tP_{\ell_i}(u)
=\sum_\lambda u^{\delta_\lambda}
  \prod_{j=1}^{d_\lambda}P_{h_{\lambda,j}}(u),
\tag{3.2}
\]

\[
2\delta_\lambda+\sum_jh_{\lambda,j}=S.
\tag{3.3}
\]

Consequently every leaf is centered at the parent middle rank:

\[
\delta_\lambda+
\left\lfloor\frac{\sum_jh_{\lambda,j}}2\right\rfloor
=\left\lfloor\frac S2\right\rfloor,
\tag{3.4}
\]

and the widths add exactly:

\[
\boxed{
w_t(\boldsymbol\ell)
=\sum_\lambda
w_{d_\lambda}(h_{\lambda,1},\ldots,h_{\lambda,d_\lambda}).
}
\tag{3.5}
\]

Applying unrelated adaptive trees in all Boolean product parents still gives

\[
\boxed{\sum_{\text{all leaves }\lambda}w(\lambda)=W(k).}
\tag{3.6}
\]

#### Proof

For \(r,s>0\), the literal outer hook

\[
H_{r,s}
=\{(0,j):0\le j\le s\}
 \cup\{(i,s):1\le i\le r\}
\]

is a saturated chain of height \(r+s\). Its complement is

\[
(1,0)+([0,r-1]\times[0,s-1]).
\]

Thus

\[
P_rP_s=P_{r+s}+uP_{r-1}P_{s-1}.
\tag{3.7}
\]

Tensoring with the untouched factors proves literal disjointness. More
precisely, at every node each factor is a saturated Boolean chain supported
on a coordinate group disjoint from the supports of the other factors. The
hook \(H_{r,s}\) is a nested saturated chain on the union of the two selected
supports, while the residual is a product of chain segments on those two
supports. Induction therefore shows that every leaf is join-isomorphic to its
abstract product of chains. Hence every local contiguous-maximum witness maps
literally to a Boolean contiguous-OR witness.

The hook child preserves the translation and side sum; the residual raises
the translation by one and lowers the side sum by two. This proves
(3.2)--(3.3) by induction. Equation (3.4) follows from

\[
\delta+\left\lfloor\frac{S-2\delta}{2}\right\rfloor
=\left\lfloor\frac S2\right\rfloor
\]

for both parities. Taking the coefficient at the parent middle rank gives
(3.5). Finally,

\[
A+\left\lfloor\frac S2\right\rfloor
=\left\lfloor\frac k2\right\rfloor,
\]

so summing over the original disjoint Boolean product parents gives (3.6).
\(\square\)

### Exact origin ledger

At every hook split exactly one branch retains its node translation and the
residual branch increases it. Induction shows that a parent tree with \(N\)
leaves has exactly one leaf of translation zero. If the original product
decomposition has \(P\) parents and the adaptive refinement has \(L\) leaves
in total, then

\[
\#\{\text{shifted leaf origins}\}=L-P,
\tag{3.8}
\]

\[
\#\{\text{nonempty parent minima}\}=P-1,
\tag{3.9}
\]

and hence

\[
\boxed{\#\{\text{distinct nonempty leaf minima}\}=L-1.}
\tag{3.10}
\]

Prepending each such leaf minimum to an independently constructed nonzero
local word gives the exact global inequality

\[
\boxed{
\nu(k)
\le \sum_\lambda g(\lambda)+L-1
=W(k)+\sum_\lambda(g(\lambda)-w(\lambda))+L-1.
}
\tag{3.11}
\]

The count \(L-1\) is exact for the omitted nonempty minima and is a sufficient
anchor count for independent leaf concatenation. It is not a lower bound on
a global word whose intervals cross leaf boundaries.

### Greedy four-to-three refinement

At a residual four-box, sort

\[
h_1\le h_2\le h_3\le h_4.
\]

Emit the three-box

\[
(h_1,h_2,h_3+h_4),
\tag{3.12}
\]

replace the residual heights by

\[
h_1,h_2,h_3-1,h_4-1,
\]

re-sort, and continue. When at most one coordinate is positive, emit the
terminal degenerate box. Every nonterminal child satisfies

\[
h_3+h_4\ge2h_2=2\max(h_1,h_2).
\tag{3.13}
\]

For an initial vector \(\boldsymbol\ell\), put

\[
S=\sum_i\ell_i,\qquad M_0=\max_i\ell_i.
\]

The exact number of hook steps and leaves is

\[
J(\boldsymbol\ell)
=\min\left\{\left\lfloor\frac S2\right\rfloor,S-M_0\right\},
\qquad
N(\boldsymbol\ell)=J(\boldsymbol\ell)+1.
\tag{3.14}
\]

Indeed no pairing process can use more than \(\lfloor S/2\rfloor\) pairs or
more than \(S-M_0\) pairs. Greedily decrementing the two largest coordinates
attains that bound. If \(M_0>S/2\), one step reduces \(S-M_0\) by one. If
\(M_0\le S/2\), after one step the new maximum is at most
\(\lceil(S-2)/2\rceil\), and the balanced bound drops by one. This proves
(3.14) inductively.

Now take four Boolean blocks. Write

\[
V_i=2^{k_i},\qquad W_i=W(k_i),\qquad
P=\prod_{i=1}^4W_i,\qquad \epsilon_k=k\bmod2.
\]

Every chain height satisfies \(\ell_i\equiv k_i\pmod2\), so every parent sum
has parity \(\epsilon_k\). The total number of shifted leaves is exactly

\[
L-P
=\sum_{\boldsymbol C}
\min\left\{
\frac{S_{\boldsymbol C}-\epsilon_k}{2},
S_{\boldsymbol C}-M_{\boldsymbol C}
\right\}.
\tag{3.15}
\]

Since

\[
\sum_{C_i}\ell(C_i)=V_i-W_i,
\tag{3.16}
\]

one obtains the exact first-moment upper bound

\[
\boxed{
L-P\le\frac12\left[
\sum_{i=1}^4(V_i-W_i)\prod_{j\ne i}W_j
-\epsilon_kP
\right].
}
\tag{3.17}
\]

For balanced \(k_i=k/4+O(1)\),

\[
P=\Theta\left(\frac{W(k)}{k^{3/2}}\right),
\qquad
L=O\left(\frac{W(k)}k\right).
\tag{3.18}
\]

When \(k=4n\), the right side of (3.17) is

\[
\left(\frac{32}{\pi}+o(1)\right)\frac{W(k)}k.
\tag{3.19}
\]

This is the leading constant of the first-moment upper bound, not necessarily
of the exact greedy leaf count, because parents with one strongly dominant
side use \(S-M_0<S/2\) steps.

Equations (3.5), (3.11), and (3.17) are the exact global width/error/origin
ledger for the first-wave hybrid construction. If the aggregate local leaf
excess is \(o(W(k))\), then every origin may be paid independently and the
global error is still \(o(W(k))\). Sharing all origins could save only
\(O(W(k)/k)\), so it cannot repair a leading-order local excess.

More explicitly, put \(R=\sqrt k\). For four balanced Boolean blocks, the
number of parents is

\[
P=\Theta(W(k)/R^3).
\]

If every compact parent \(\max_i\ell_i\le CR\) has total refined-leaf excess
\(o_C(R^3)\), uniformly in its height vector, then their aggregate excess is
\(P\,o_C(R^3)=o_C(W(k))\). Parents outside the compact height window are
handled by the crude cubic box word together with the truncated zeroth and
third SCD-height moments, giving \(O(e^{-cC^2}W(k))\). Equation (3.17) adds
only \(O(W(k)/R^2)\) origins. Thus the exact order is first \(k\to\infty\) at
fixed \(C\), then \(C\to\infty\), and the resulting total error is \(o(W(k))\).

## 4. Why fixed or randomly mixed positive proportions do not suffice

The following theorem describes exact width, not merely the number of product
cells.

### Theorem 4.1: width-biased aspect-ratio law

Fix \(t\ge2\) and suppose

\[
\sum_{i=1}^tk_i=k,\qquad \frac{k_i}{k}\to\alpha_i>0.
\]

For a product cell with chain heights \(\boldsymbol L\), define the exact
width probability measure

\[
\mu_k(E)
=\frac1{W(k)}
\sum_{\boldsymbol\ell/\sqrt k\in E}
\left(\prod_{i=1}^tc_{k_i}(\ell_i)\right)
w_t(\boldsymbol\ell).
\tag{4.1}
\]

The exact SCD middle-layer identity makes \(\mu_k\) a probability measure.
Put

\[
\omega_t(\boldsymbol x)
=\frac1{(t-1)!}
\sum_{J\subseteq[t]}(-1)^{|J|}
\left(
\frac12\sum_ix_i-\sum_{j\in J}x_j
\right)_+^{t-1},
\tag{4.2}
\]

and

\[
A(\boldsymbol\alpha)
=\left(\frac2\pi\right)^{(t-1)/2}
\prod_i\alpha_i^{-1/2}.
\tag{4.3}
\]

Then \(\mu_k\) converges weakly on the positive orthant to the continuous
density

\[
\boxed{
\rho_{\boldsymbol\alpha}(\boldsymbol x)
=A(\boldsymbol\alpha)\,
\omega_t(\boldsymbol x)
\prod_{i=1}^t
\left(
\frac{x_i}{\alpha_i}e^{-x_i^2/(2\alpha_i)}
\right).
}
\tag{4.4}
\]

This density is strictly positive at every point of
\((0,\infty)^t\).

#### Proof

Inclusion-exclusion for the central coefficient gives, uniformly on compact
sets,

\[
k^{-(t-1)/2}w_t(\boldsymbol\ell)
\longrightarrow\omega_t(\boldsymbol x),
\qquad \boldsymbol\ell/\sqrt k\to\boldsymbol x.
\tag{4.5}
\]

Also the central-binomial asymptotic gives

\[
k^{(t-1)/2}\frac{\prod_iW(k_i)}{W(k)}
\longrightarrow A(\boldsymbol\alpha).
\tag{4.6}
\]

Combine (4.5)--(4.6) with the independent Rayleigh limits (2.6). The bound

\[
w_t(\boldsymbol\ell)
\le\prod_{i\ne j}(\ell_i+1)
\le(1+\textstyle\sum_i\ell_i)^{t-1}
\]

and (2.4) give uniform integrability. Formula (4.2) is the
convolution-normalized central slice volume of the continuous box.
Equivalently, it is the lattice normalization naturally arising from the
coefficient asymptotic; Euclidean Hausdorff slice measure would differ by the
constant \(\sqrt t\). It is positive because the slice through
\((x_1/2,\ldots,x_t/2)\) contains a relative open neighborhood. \(\square\)

Let

\[
\Delta^\circ=\{\boldsymbol r:r_i>0,\ \sum_ir_i=1\},
\qquad
\pi(\boldsymbol x)=\frac{\boldsymbol x}{\sum_ix_i}.
\]

For every nonempty open \(U\subset\Delta^\circ\), Theorem 4.1 gives

\[
\liminf_{k\to\infty}
\mu_k(\pi^{-1}U)>0.
\tag{4.7}
\]

If all \(\alpha_i\ge\delta>0\), the lower bound is uniform over the block
proportions: place a compact Euclidean box inside \(\pi^{-1}U\) and use the
positive minimum of (4.4) on that box and on the compact proportion simplex.

Consequences:

* Unequal but fixed positive block proportions do not make any interior
  aspect-ratio sector \(o(W(k))\).
* Randomly permuting coordinates among fixed block sizes changes no height
  histogram.
* For a fixed mixing law compactly supported in the open proportion simplex,
  the limiting density is the positive mixture
  \(\int\rho_{\boldsymbol\alpha}\,d\lambda(\boldsymbol\alpha)\). For an
  arbitrary fixed law supported in the open simplex, a compact exhaustion
  still puts positive probability on some fixed compact interior set, so
  every nonempty interior sector retains positive expected exact width.
* If a random size rule has probability at least \(p>0\) of keeping all
  proportions at least \(\delta\), its expected width in every fixed interior
  sector is at least \(p c(t,U,\delta)W(k)\).

Thus randomization can erase the balanced sector in expected exact width only
if its proportion law escapes every compact subset of the open simplex.

### Boundary concentration

This escape is genuine but does not itself construct a word. If \(t\) is
fixed and \(k_i=o(k)\), then under the exact width measure

\[
\frac{L_i}{\sum_jL_j}\longrightarrow0
\quad\text{in probability}.
\tag{4.8}
\]

Here the ratio is defined to be zero on the all-zero height tuple.

To see this, use
\(w_t(\boldsymbol\ell)\le\prod_{h\ne i}(\ell_h+1)\), (2.2), and (2.4) to
obtain

\[
\mathbb E_{\mu_k}(1+L_i)^3
\le C\sqrt{k+1}(k_i+1).
\tag{4.9}
\]

Choose \(j\ne i\) of maximum block size; then \(k_j\ge k/[2(t-1)]\) for all
large \(k\). From (2.3),

\[
\mu_k(L_j\le T)
\le C_t\frac{(T+2)^2}{k}.
\tag{4.10}
\]

On \(L_i/\sum_hL_h\ge\eta\), either
\(L_j\le\varepsilon\sqrt k\) or
\(L_i\ge\eta\varepsilon\sqrt k\). Equations (4.9)--(4.10), first with
\(k\to\infty\) and then \(\varepsilon\downarrow0\), prove (4.8).

The interpretation is important. Boundary block proportions move the exact
width to a lower-dimensional projective face; they do not prove a
coefficient-one word on that face. A local theorem or a new exact coupling is
still required.

## 5. The doubly hierarchical reduction

We now prove (1.1).

### 5.1 Positive closed-cone uniformization

Assume \(\mathrm{HRAY}_M\). For every fixed \(0<\delta<C<\infty\),

\[
\sup_{\substack{
\delta R\le x,y,z\le CR\\
y\ge Mx,\ z\ge My}}
\frac{(g_3(x,y,z)-w_3(x,y,z))_+}{R^2}
\longrightarrow0.
\tag{5.1}
\]

This includes the positive boundary walls \(y=Mx\) and \(z=My\), although
\(\mathrm{HRAY}_M\) was stated strictly.

#### Proof

Fix a mesh integer \(L>4/\delta\) and put \(h=\lfloor R/L\rfloor\). Define

\[
A=\lfloor x/h\rfloor,\qquad
B=\lfloor y/h\rfloor,\qquad
D=\lfloor z/h\rfloor,
\]

and take the inner coefficient triple

\[
a=A-2,\qquad b=B-1,\qquad c=D.
\tag{5.2}
\]

Because \(M\) is integral,

\[
B\ge MA,\qquad D\ge MB.
\]

Hence

\[
b>Ma,\qquad c>Mb.
\]

The inner box \((ah,bh,ch)\) lies coordinatewise below \((x,y,z)\), with
coordinate gaps less than \(3h,2h,h\). At fixed
\((\delta,C,L)\), only finitely many coefficient triples occur. Divide each
by its gcd and apply \(\mathrm{HRAY}_M\) at the resulting scale. The proved
face-extension inequality

\[
\begin{aligned}
g_3(p,q,r)\le g_3(p_0,q_0,r_0)
&+(p-p_0)(q+r+1)\\
&+(q-q_0)(p_0+r+1)\\
&+(r-r_0)(p_0+q_0+1)
\end{aligned}
\]

for \(p_0\le p,\ q_0\le q,\ r_0\le r\) covers the coordinate shells at cost
\(O_C(hR)\). The inequality is obtained by adjoining the three coordinate
shells in turn and covering every new fixed-coordinate face by the elementary
rectangle word.
Both boxes lie in the plateau sector, and therefore

\[
w_3(ah,bh,ch)=(ah+1)(bh+1)
\le(x+1)(y+1)=w_3(x,y,z).
\]

First let \(R\to\infty\) at fixed \(L\), then let \(L\to\infty\). This proves
(5.1).

This closure is only inside the positive cone. A zero coordinate is handled
below by the crude slice word, not by projective closure. \(\square\)

### 5.2 Exact exceptional-sector cost

Fix \(0<\varepsilon\le1/2\) and choose integer block sizes with

\[
\frac{k_1}{k}\to\varepsilon^4,\qquad
\frac{k_2}{k}\to\varepsilon^2,\qquad
\frac{k_3}{k}\to1-\varepsilon^2-\varepsilon^4.
\tag{5.3}
\]

Write their SCD chain heights as \(x,y,z\), and put

\[
B_1=\{y<Mx\},\qquad B_2=\{z<My\}.
\]

The elementary literal slice word gives, for every box,

\[
g_3(x,y,z)+1\le(x+1)(y+z+1).
\tag{5.4}
\]

We prove the stronger estimate

\[
\boxed{
\sum_{B_1\cup B_2}
c_{k_1}(x)c_{k_2}(y)c_{k_3}(z)
\bigl(g_3(x,y,z)+1\bigr)
=O_M(\varepsilon W(k)).
}
\tag{5.5}
\]

Here \(S_{\rm bad}(k,\varepsilon)\) denotes the left side of (5.5).
Precisely, there is a constant \(C_M\), independent of
\(0<\varepsilon\le1/2\), such that

\[
\limsup_{k\to\infty}\frac{S_{\rm bad}(k,\varepsilon)}{W(k)}
\le C_M\varepsilon.
\]

The threshold in \(k\) may depend on \(\varepsilon\) and on the chosen
integer block-size sequences. No simultaneous limit
\(\varepsilon=\varepsilon(k)\) is being used here.

For \(B_1\), sum over \(z\) first. By (2.2),

\[
\sum_zc_{k_3}(z)(y+z+1)=yW_3+V_3,
\tag{5.6}
\]

where \(W_i=W(k_i)\) and \(V_i=2^{k_i}\). Applying (2.3) to
\(A_{k_2}(Mx)\) and then (2.4) gives

\[
\begin{aligned}
S(B_1)
&:=\sum_{B_1}c_{k_1}(x)c_{k_2}(y)c_{k_3}(z)
  (x+1)(y+z+1)\\
&\le
C_M\frac{W_1W_2W_3}{k_2+1}
\left(
(k_1+1)^2+
\frac{V_3}{W_3}(k_1+1)^{3/2}
\right).
\tag{5.7}
\end{aligned}
\]

On \(B_2\), \(y+z+1\le(M+1)(y+1)\). Apply (2.3) to
\(A_{k_3}(My)\), sum \((x+1)\) exactly using (2.2), and use the third moment
in (2.4):

\[
S(B_2)
\le C_MV_1W_2W_3
\frac{(k_2+1)^{3/2}}{k_3+1}.
\tag{5.8}
\]

Finally,

\[
\frac{W_1W_2W_3}{W(k)}
=O\left(
\frac{\sqrt k}{\sqrt{(k_1+1)(k_2+1)(k_3+1)}}
\right),
\qquad
\frac{V_i}{W_i}=O(\sqrt{k_i+1}).
\tag{5.9}
\]

Substituting (5.3) into (5.7)--(5.9) yields

\[
S(B_1)=O_M((\varepsilon+\varepsilon^3)W(k)),
\qquad
S(B_2)=O_M(\varepsilon^2W(k)),
\]

which proves (5.5).

As an independent constant check, Lemma 2.2 turns the normalized bad cost
into a Rayleigh integral. If

\[
\gamma=\sqrt{1-\varepsilon^2-\varepsilon^4},
\]

then one obtains

\[
\limsup\frac{S(B_1\cup B_2)}{W(k)}
\le
\left(\frac{4M}{\pi\gamma}+\frac32M^2\right)\varepsilon
+\frac32(M^2+M^3)\frac{\varepsilon^2}{\gamma^3}.
\tag{5.10}
\]

Thus two independent derivations give the required \(O_M(\varepsilon)\)
scale.

### 5.3 Good boxes and exact global aggregation

Call a box good when

\[
y\ge Mx,\qquad z\ge My.
\tag{5.11}
\]

Then

\[
z\ge2y\ge x+y,
\]

so its width is exactly

\[
w_3(x,y,z)=(x+1)(y+1).
\tag{5.12}
\]

Fix \(\varepsilon\), and first restrict all three heights to a positive compact
window, for example

\[
\eta\sqrt{k_i}\le L_i\le C\sqrt{k_i}.
\tag{5.13}
\]

For fixed \((\varepsilon,\eta,C)\), (5.1) gives a uniform \(o(k)\) excess on
every good box in this window: in the common scale \(R=\sqrt k\), the lower
cutoff is
\(\delta=\eta\min_i\sqrt{k_i/k}\asymp_\varepsilon\eta>0\).
The number of three-chain parents is

\[
B_3=W_1W_2W_3
=\Theta_\varepsilon\left(
\frac{W(k)}{\varepsilon^3k}
\right).
\tag{5.14}
\]

Therefore the total good compact-sector excess is \(o_\varepsilon(W(k))\).

For good boxes outside (5.13), use the full slice cost (5.4). At fixed
\(\varepsilon\), Lemma 2.2 and polynomial uniform integrability show that its
normalized mass outside the window tends to zero as
\(\eta\downarrow0\) and \(C\uparrow\infty\). This includes zero and short
coordinates; they are not attributed to face extension.

The product parents partition the Boolean cube, and their middle widths sum
exactly to \(W(k)\). Every nonempty parent minimum may be paid independently;
by (5.14), all such anchors cost \(o_\varepsilon(W(k))\). Hence (5.5) and the
good-sector estimate give

\[
\limsup_{k\to\infty}
\frac{\nu(k)}{W(k)}
\le1+C_M\varepsilon.
\tag{5.15}
\]

Let \(\varepsilon\downarrow0\), and combine with the width lower bound
\(\nu(k)\ge W(k)\). This proves (1.1).

The quantifier order is essential:

1. fix \(M\) and \(\varepsilon>0\);
2. fix positive compact cutoffs and a finite mesh;
3. let \(k\to\infty\);
4. refine the mesh and remove the compact cutoffs;
5. only then let \(\varepsilon\downarrow0\).

A single construction for all \(k\) follows by the usual staircase
diagonalization. It may choose \(\varepsilon=\varepsilon(k)\downarrow0\) so
slowly that all three block dimensions tend to infinity and every estimate
selected at the previous stages is valid. No uniform rate in
\(\mathrm{HRAY}_M\) over infinitely many rays is assumed.

## 6. Full merge trees flatten to macroblock SCDs

Iterating the full hook identity gives

\[
P_aP_b
=\sum_{j=0}^{\min(a,b)}u^jP_{a+b-2j}.
\tag{6.1}
\]

### Theorem 6.1: flattening

Group any fixed collection of atomic Boolean blocks of total dimension \(K\).
Choose arbitrary atomic SCDs and fully merge their chain factors along any
binary tree using (6.1). The resulting chains form a literal SCD of the
\(K\)-cube. Write an output chain's **absolute** Boolean rank polynomial as
\(u^rP_h\). If its atomic product parent has bottom rank \(A\) and its
relative hook translation is \(\delta\), then \(r=A+\delta\), and

\[
2r+h=K,
\tag{6.2}
\]

After union over all atomic chain tuples, the number of output chains of
height \(h\) is exactly \(c_K(h)\), independent of the atomic partition,
merge-tree shape, and merge order. Relative to one atomic product parent the
invariant is \(2\delta+h=S\), where \(S\) is that parent's side-height sum.

#### Proof

Each full hook step is a literal saturated-chain partition of a product of
two symmetric chains. By (3.3),

\[
2r+h=2(A+\delta)+h=2A+S=K.
\]

Thus every final chain is saturated and symmetric in the \(K\)-cube, and the
union covers the cube exactly. It is therefore an SCD. Formula (2.1) fixes
the height multiplicities in every SCD. \(\square\)

Consequently, starting with \(q+2\) atomic blocks, fully merging \(q\) of
them, and leaving two unmerged is exactly a three-macroblock construction.
It can realize the hierarchical sizes in Section 5, but it cannot sharpen
the chain-height distribution beyond the ordinary macroblock law. Randomizing
a full merge tree likewise changes no histogram.

Partial and branch-dependent merge trees are covered by Theorem 3.1, but
their leaves have mixed dimensions. No theorem here says that such a tree
can concentrate all width on one ray or improve \(\mathrm{HRAY}_M\). That
possibility remains open.

There is also an exact locality warning. If one first replaces two atomic
blocks by a macroblock SCD, a single hard macrochain cannot generally be
"split back" into its two atomic chain factors: its original product
rectangle also contains the sibling macrochains. Undoing only one chain
would overlap them. A genuinely height-adaptive keep-or-refine rule must
start from the finer product parents and apply Theorem 3.1 inside those
disjoint parents.

## 7. Architecture checks and no-go statements

### 7.1 The existing slice word does not become coefficient one

Apply the explicit word

\[
g_3(x,y,z)+1\le(x+1)(y+z+1)
\]

in every cell of a three-block product decomposition. Summing exactly gives

\[
\sum_{x,y,z}c_{k_1}(x)c_{k_2}(y)c_{k_3}(z)
(x+1)(y+z+1)
=V_1(V_2W_3+W_2V_3-W_2W_3).
\tag{7.1}
\]

If \(k_i/k\to\alpha_i>0\), then

\[
\frac{V_1(V_2W_3+W_2V_3-W_2W_3)}{W(k)}
\longrightarrow
\alpha_2^{-1/2}+\alpha_3^{-1/2}.
\tag{7.2}
\]

The negative term is lower order. Even if the first block proportion is
then sent to zero, minimizing over
\(\alpha_2+\alpha_3=1\) gives

\[
\inf(\alpha_2^{-1/2}+\alpha_3^{-1/2})=2\sqrt2.
\tag{7.3}
\]

For the hierarchy (5.3), the ratio in (7.2) is asymptotic to
\(1+\varepsilon^{-1}\). Thus anisotropic block sizes alone do not repair the
known word. Equations (7.1)--(7.3) concern this displayed slice construction;
they are not lower bounds for arbitrary three-box words.

### 7.2 Multiple overlapping decompositions cannot be cherry-picked

Every complete product decomposition has exact total width \(W(k)\). Taking
several decompositions and choosing the cheapest cell witness separately does
not define a disjoint partition: their cells overlap. Paying all of them pays
several copies of the width. A randomized averaging argument proves the
existence of one whole decomposition with at most its expected cost, but it
does not create a cellwise exact allocation across decompositions. Any such
hybrid requires a new integral partition or matching theorem.

### 7.3 Scope of the factor-two barrier

The equal four-box parent forces the first-wave largest-pair recursion to emit
\(\Theta(R)\) children on or arbitrarily near the ratio-two wall. Hence that
specific balanced recursion cannot replace \(2\) by \(2+\eta\) while treating
only \(o(R)\) exceptions.

The hierarchical theorem shows that this is not a global product-aggregation
barrier. Degenerating the block proportions makes the full crude cost outside
the much farther cone \(b\ge Ma,\ c\ge Mb\) only \(O_M(\varepsilon W)\).
There is no contradiction: the first statement concerns every child of one
balanced four-box recursion, while the second changes the global Boolean
block proportions and then takes an additional outer limit.

### 7.4 Origin sharing is lower order

For the balanced four-block **greedy four-to-three refinement of Section 3**,
all nonempty leaf origins total \(O(W/k)\) by (3.17). No analogous bound is
asserted for an arbitrary adaptive outer-hook tree: such a tree requires its
own global leaf-count estimate and may have as many as \(W(k)\) leaves.

For the hierarchical three-block construction, all parent origins total

\[
O_\varepsilon(W/k)
\]

by (5.14). Thus even perfect cross-cell origin sharing changes only an
\(o(W)\) term. It cannot supply the missing \(o(k)\) local excess on good
hierarchical three-boxes.

## 8. Final implication ledger and caveats

The proved implications are

\[
\boxed{
\mathrm{HRAY}_M
\Longrightarrow
\text{uniform control on the positive closed hierarchical cone}
\Longrightarrow
\nu(k)=(1+o(1))W(k).
}
\tag{8.1}
\]

The decisive exceptional estimate (5.5) was independently checked in two
ways: by direct finite-\(k\) SCD lower-tail/moment summation and by the
Rayleigh limiting integral (5.10). The constants, normalization by \(W(k)\),
and order of limits agree.

What is proved:

* all product parents and all adaptive leaves are literal integral Boolean
  pieces;
* all middle-width identities are exact, including parity and affine bottom
  shifts;
* the exceptional hierarchical sector has \(O_M(\varepsilon W)\) full word
  cost;
* all independent origin charges in the two constructions for which a leaf
  count was proved—the balanced greedy four-to-three refinement and the
  hierarchical three-block construction—are \(o(W)\); arbitrary adaptive
  trees require a separate leaf-count bound;
* fixed positive proportions and their fixed random mixtures cannot erase an
  interior aspect-ratio sector;
* full higher-dimensional merge trees flatten to ordinary macroblock SCDs.

What remains unproved:

* \(\mathrm{HRAY}_M\) for even one fixed finite \(M\ge2\);
* any unrestricted three-box or balanced three-box coefficient-one theorem;
* any adaptive partial merge tree that reduces the local gate beyond
  \(\mathrm{HRAY}_M\);
* any integral allocation that cherry-picks cells from overlapping product
  decompositions;
* any leading-order saving from cross-leaf braiding.

The construction is a direct literal contiguous-OR reduction. It neither
uses nor proves MWB, exact-wreath overload, or labelled common-owner
synchronization.

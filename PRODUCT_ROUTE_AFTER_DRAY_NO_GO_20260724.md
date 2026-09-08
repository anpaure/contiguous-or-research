# The product route after the DRAY obstruction

## Executive conclusion

Let the coordinates of the Boolean cube be split into three blocks, take an
SCD in each block, and cover every resulting three-chain product box by its
own contiguous-maximum word, with that segment's letters and witnesses
confined to the translated box.  This architecture cannot have leading
constant one.

The obstruction is not confined to a negligible family of aspect ratios.
For three equal blocks, if the three SCD chains are selected independently
and uniformly and their heights are sorted as

\[
L_{(1)}<L_{(2)}<L_{(3)},
\]

then

\[
\boxed{
\Pr\bigl(L_{(3)}>2L_{(2)}\bigr)\longrightarrow \frac15.
}
\tag{1}
\]

Every compact subcone of this event bounded away from its walls has, by the
audited finite DRAY lower bound, a quadratic local excess.  Since the number
of three-chain boxes is of order \(W(k)/k\), these boxes alone force an
\(\Omega(W(k))\) global excess.

More strongly, changing the three block sizes does not help: for **every**
sequence of three-way coordinate splits, including splits approaching the
boundary of the dimension simplex, separate local-box concatenation has

\[
\boxed{
\liminf_{k\to\infty}\frac{L_{\rm sep}(k)-W(k)}{W(k)}>0.
}
\tag{2}
\]

If only one or two block dimensions remain macroscopic, elementary pure-axis
or interval-counting bounds replace the DRAY obstruction.

Extra atomic blocks do not help if they are fully merged into three
macroblocks and the resulting three-boxes are still paid separately: the
SCD height histogram of a macroblock is invariant.  The first surviving
fixed-dimensional product gate is therefore genuinely fused.  For four
positive-proportion blocks it is exactly the Gaussian-averaged condition

\[
\boxed{
\mathbb E E_4(L_1,L_2,L_3,L_4)
=o(k^{3/2}).
}
\tag{GF4}
\]

One concrete way to prove such a fused estimate is a literal packet theorem
which shares witnesses across adjacent three-box children of a four-box.
Such sharing has to save quadratic order per bad child; boundary-size
connectors or independently reset child words cannot do it.

No web search, computational search, or finite experiment is used below.

---

## 1. SCD height law and notation

Let

\[
W(s)=\binom{s}{\lfloor s/2\rfloor}.
\]

In every SCD of the \(s\)-cube, the number of chains of edge height \(h\) is

\[
c_s(h)=
\binom{s}{(s-h)/2}-\binom{s}{(s-h)/2-1}
\tag{3}
\]

when \(h\equiv s\pmod 2\), and is zero otherwise.  In particular the
height multiset does not depend on the chosen SCD.

If a chain is selected uniformly from an SCD of the \(s\)-cube and its
height is \(L_s\), then

\[
\frac{L_s}{\sqrt s}\Longrightarrow Y,
\qquad
f_Y(y)=ye^{-y^2/2}\quad(y>0).
\tag{4}
\]

Thus \(Y\) is standard Rayleigh.  Heights selected from different block
SCDs are independent.

For a \(d\)-tuple \(\boldsymbol\ell=(\ell_1,\ldots,\ell_d)\), write

\[
P(\boldsymbol\ell)=\prod_{i=1}^d[0,\ell_i],
\]

let \(w_d(\boldsymbol\ell)\) be its width, and let
\(g_d(\boldsymbol\ell)\) be the least length of a word whose contiguous
coordinatewise maxima cover every nonzero point.  Put

\[
E_d(\boldsymbol\ell)
=\max\{g_d(\boldsymbol\ell)-w_d(\boldsymbol\ell),0\}.
\tag{5}
\]

Allowing a zero relative letter in a translated Boolean box does not alter
\(g_d\): delete every such letter.  Every nonzero target witness remains a
contiguous interval after the deletion and has the same maximum.  A
translated local origin costs at most one additional literal entry.  If the
box has positive total height, its nonzero points contain an antichain of
size \(w_d\), so the maximum in (5) is redundant.  It only repairs the
all-zero abstract box, where \(g_d=0\) and \(w_d=1\); a nonempty translated
origin then restores that one unit.

---

## 2. The dominant cone has positive limiting mass

### Theorem 2.1 (exact balanced-block mass)

Let \(Y_1,Y_2,Y_3\) be independent standard Rayleigh variables.  Then

\[
\Pr(Y_1<Y_2,\ Y_3>2Y_2)=\frac1{30},
\tag{6}
\]

and consequently

\[
\Pr\bigl(Y_{(3)}>2Y_{(2)}\bigr)=\frac15.
\tag{7}
\]

Hence (1) holds for three equal Boolean blocks.

#### Proof

Put \(Z_i=Y_i^2/2\).  The \(Z_i\)'s are independent exponential random
variables of mean one.  The event in (6) is

\[
Z_1<Z_2,\qquad Z_3>4Z_2.
\]

Conditioning on \(Z_2=t\) gives

\[
\begin{aligned}
\Pr(Z_1<Z_2, Z_3>4Z_2)
&=\int_0^\infty (1-e^{-t})e^{-4t}e^{-t}\,dt\\
&=\frac15-\frac16
=\frac1{30}.
\end{aligned}
\]

There are three choices of the largest variable and two orders for the
other two.  The six corresponding events are disjoint up to null tie sets,
which proves (7).  Equation (4) and joint weak convergence prove (1).
\(\square\)

The same qualitative conclusion holds for every fixed positive block
proportion.  If \(s_i/k\to\alpha_i>0\), then

\[
\frac{L_{s_i}}{\sqrt k}\Longrightarrow X_i,
\qquad
f_{\alpha_i}(x)=\frac{x}{\alpha_i}e^{-x^2/(2\alpha_i)},
\tag{8}
\]

independently.  The density in (8) is positive at every positive finite
point.  Therefore every nonempty open box compactly contained in

\[
\mathcal D=\{(x,y,z):0<x<y,\ z>2y\}
\tag{9}
\]

has positive limiting probability.

---

## 3. Uniformizing the audited DRAY lower bound

The audited finite theorem in
`MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md` says the following.  For

\[
0<p<q,\qquad r>p+q,
\]

put

\[
M=(p+1)(q+1),\quad
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,
\quad s_0=p+q+2,
\]

\[
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\quad
B=s_0+\left\lceil\frac{M-Ks_0}{K}\right\rceil.
\]

When \(K\ge2\), every local word has excess \(D=g_3(p,q,r)-M\)
satisfying

\[
D\ge
\frac{M((r-\varepsilon)/2-q)-1}{h-1+2B},
\qquad \varepsilon\in\{0,1\}.
\tag{10}
\]

### Lemma 3.1 (compact dominant sectors cost quadratic order)

Let \(C\) be a compact subset of \(\mathcal D\).  There is
\(\kappa_C>0\) such that, uniformly whenever

\[
\frac1{\sqrt k}(p,q,r)\in C,
\]

one has

\[
\boxed{E_3(p,q,r)\ge \kappa_C k}
\tag{11}
\]

for all sufficiently large \(k\).

#### Proof

Compactness gives constants \(u,C_0>0\) such that throughout \(C\)

\[
x\ge u,\qquad y-x\ge u,\qquad z-2y\ge u,
\qquad x+y+z\le C_0.
\tag{12}
\]

Thus \(M=\Theta_C(k)\), while

\[
\frac{r-\varepsilon}{2}-q\ge \frac{u}{3}\sqrt k
\tag{13}
\]

for large \(k\).  Also \(M/s_0=\Theta_C(\sqrt k)\), so \(K\ge2\).
For large \(k\),

\[
K\ge\frac{M}{2s_0},
\qquad
B\le3s_0+1=O_C(\sqrt k).
\tag{14}
\]

Hence the numerator of (10) is \(\Omega_C(k^{3/2})\) and its denominator
is \(O_C(\sqrt k)\).  This proves (11).  \(\square\)

More precisely, on compact subsets of \(\mathcal D\), (10) gives

\[
\frac{E_3(p,q,r)}k
\ge
\frac{xy(z-2y)}{z+5x+5y}-o_C(1),
\qquad (x,y,z)=\frac{(p,q,r)}{\sqrt k}.
\tag{15}
\]

---

## 4. Fixed positive-proportion three-block splits fail

Let

\[
k=s_1+s_2+s_3,
\qquad \frac{s_i}{k}\longrightarrow\alpha_i>0.
\]

Choose arbitrary SCDs in the three blocks.  The number of product boxes is

\[
\mathcal B_k=W(s_1)W(s_2)W(s_3),
\tag{16}
\]

and, if \(L_i\) are independent uniform SCD heights, the exact sum of the
isolated local excess statistics is

\[
\mathcal B_k\,\mathbb E E_3(L_1,L_2,L_3).
\tag{17}
\]

Including every abstract local origin, the length of a fully anchored
separate concatenation lies between \(W(k)\) plus (17) and that quantity
plus \(\mathcal B_k\).  Under the nonzero-word convention the unique global
empty mask may be deleted, shifting the lower ledger by at most one.

Central-binomial asymptotics give

\[
\frac{k\mathcal B_k}{W(k)}\longrightarrow
\frac{2}{\pi\sqrt{\alpha_1\alpha_2\alpha_3}}.
\tag{18}
\]

### Theorem 4.1 (width-order loss)

For every fixed positive triple \((\alpha_1,\alpha_2,\alpha_3)\), there is
\(\epsilon_{\boldsymbol\alpha}>0\) such that

\[
\boxed{
\liminf_{k\to\infty}
\frac{\mathcal B_k\,\mathbb E E_3(L_1,L_2,L_3)}{W(k)}
\ge\epsilon_{\boldsymbol\alpha}>0.
}
\tag{19}
\]

#### Proof

Choose a closed rectangular box \(C\) with nonempty interior and
\(C\subset\mathcal D\).  By (8),

\[
\Pr\left(\frac{(L_1,L_2,L_3)}{\sqrt k}\in C\right)
\longrightarrow \pi_C>0.
\tag{20}
\]

Lemma 3.1 gives local excess at least \(\kappa_Ck\) on this event.
Equations (17)--(18) now give

\[
\liminf
\frac{\mathcal B_k\mathbb E E_3}{W(k)}
\ge
\frac{2\kappa_C\pi_C}
     {\pi\sqrt{\alpha_1\alpha_2\alpha_3}}>0.
\]

\(\square\)

For three equal blocks one can use the exact mass (6) or any compact
subevent of it.  Thus the DRAY obstruction occupies positive **box mass**,
and (19) shows that it also occupies positive **global width scale**.

The exact width ledger for Boolean product boxes is

\[
\sum_{\rm boxes}w_3(L_1,L_2,L_3)=W(k).
\tag{21}
\]

Therefore separate local concatenation has length at least

\[
(1+\epsilon_{\boldsymbol\alpha}+o(1))W(k).
\tag{22}
\]

Incidental translated-origin entries only increase this lower bound.

---

## 5. No three-way dimension split rescues separate concatenation

The preceding theorem assumed fixed positive proportions.  Let now

\[
s_1(k)+s_2(k)+s_3(k)=k
\]

be arbitrary, and relabel so that

\[
0\le s_1\le s_2\le s_3.
\]

Let \(L_{\rm sep}(k)\) be the sum of the optimal local lengths when every
translated three-chain box is required to cover all Boolean masks it
contains (apart from the one global empty mask).  Thus local origins are
included, and Section 1 shows that they differ from the relative
nonzero-target convention by at most one entry per box.  The local segment
is confined to its translated box; allowing outside-box letters or
cross-box witnesses is the fusion regime of Section 8.  We prove (2).

We use the absolute central-binomial estimates

\[
W(s)\asymp\frac{2^s}{\sqrt{s+1}},
\tag{23}
\]

and hence

\[
\frac{W(s_1)W(s_2)W(s_3)}{W(k)}
\asymp
\frac{\sqrt{k+1}}
{\sqrt{(s_1+1)(s_2+1)(s_3+1)}}.
\tag{24}
\]

### Case 1: \(s_1\to\infty\)

Use the positive-probability height windows

\[
\sqrt{s_1}\le p\le2\sqrt{s_1},
\quad
4\sqrt{s_2}\le q\le5\sqrt{s_2},
\quad
12\sqrt{s_3}\le r\le13\sqrt{s_3}.
\tag{25}
\]

The Rayleigh limit shows that the proportion of chain triples in these
windows is bounded below by a positive absolute constant.  Since
\(s_1\le s_2\le s_3\), these windows imply

\[
p<q,\qquad r-2q\ge2\sqrt{s_3}.
\]

The finite estimate (10), with the same bounds as in Lemma 3.1 but in the
three natural scales, gives

\[
E_3(p,q,r)\ge c\sqrt{s_1s_2}
\tag{26}
\]

for an absolute \(c>0\).  Multiplying (24) by the right side of (26) gives

\[
\sqrt{s_1s_2}\,
\frac{W(s_1)W(s_2)W(s_3)}{W(k)}
\asymp \sqrt{\frac{k}{s_3+1}}=\Omega(1).
\tag{27}
\]

Thus this case has width-order excess.

### Case 2: \(s_1=d\ge1\) is fixed and \(s_2\to\infty\)

Select the unique longest chain of the first block, so \(p=d\), and choose
\(q\asymp\sqrt{s_2}\).  Choose the third height in a Rayleigh window

\[
C_d\sqrt{s_3}\le r\le(C_d+1)\sqrt{s_3},
\tag{28}
\]

where \(C_d\) is a sufficiently large fixed constant.  This event has a
positive probability depending only on \(d\).

A word of length \(N\) has at most \(N(N+1)/2\) intervals.  Since the box
contains

\[
T=(d+1)(q+1)(r+1)-1
\]

nonzero targets,

\[
g_3(d,q,r)\ge
\frac{\sqrt{8T+1}-1}{2}.
\tag{29}
\]

For \(C_d\) large enough, (29) is at least

\[
(1+\delta_d)(d+1)(q+1),
\]

while \(r>d+q\) makes the width exactly \((d+1)(q+1)\).  Hence

\[
E_3(d,q,r)\ge c_d\sqrt{s_2}.
\tag{30}
\]

By (24), the aggregate normalized contribution is again bounded below,
because

\[
\sqrt{s_2}\,
\frac{W(d)W(s_2)W(s_3)}{W(k)}
\asymp_d\sqrt{\frac{k}{s_3+1}}=\Omega_d(1).
\tag{31}
\]

### Case 3: \(s_2\) is bounded

After passing to a subsequence, \(s_1,s_2\) are fixed.  If both are
positive, choose their longest chains and choose
\(r\asymp\sqrt{s_3}\) with positive probability.  Equation (29) gives

\[
E_3(s_1,s_2,r)=\Omega(s_3^{1/4}),
\tag{32}
\]

because the width is fixed while the number of targets grows linearly in
\(r\).  Formula (24) says that the selected boxes already have
\(\Theta(W(k))\) cardinality, so their normalized excess tends to infinity.

### Zero-dimensional blocks

If \(s_1=0<s_2\), the local boxes are two-dimensional.  For
\(p,q>0\), every word covering \([0,p]\times[0,q]\) has

\[
g_2(p,q)\ge p+q.
\tag{33}
\]

Indeed each pure-axis target \((i,0)\), \(1\le i\le p\), requires an
occurrence whose value is \((i,0)\), and similarly for the \(q\) targets
\((0,j)\); these occurrences are distinct.  If \(p\le q\), the width is
\(p+1\), so

\[
E_2(p,q)\ge q-1.
\tag{34}
\]

Rayleigh height windows and the two-factor version of (24) show that (34)
aggregates to \(\Omega(W(k))\), for every choice of \(s_2,s_3\).

If \(s_1=s_2=0\), then \(g_1(r)\ge r\); a positive fraction of SCD chains
have height \(\Theta(\sqrt k)\), so the excess is much larger than
\(W(k)\).

### Completion of the proof

Suppose (2) failed.  There would be a subsequence on which the normalized
excess tends to zero.  On a further subsequence, either \(s_2\) is bounded
or tends to infinity; in the latter case \(s_1\) is either fixed or tends
to infinity.  The corresponding case above gives a contradiction.  This
proves (2).

Thus neither balanced nor escaping-to-the-boundary three-block splits can
rescue box-by-box product aggregation.

---

## 6. More atomic blocks followed by three macroblocks still fail

Suppose the coordinates are first split into any fixed number of atomic
blocks.  Fully merge some atomic factors, by arbitrary outer-hook/SCD merge
trees, into three macroblocks of dimensions \(S_1,S_2,S_3\), and then pay
for every resulting three-chain box independently.

The chain-height histogram of an SCD of an \(S\)-cube is always (3).
Therefore the final macroblock height laws depend only on
\((S_1,S_2,S_3)\), not on the number of atomic blocks or the merge trees.
Section 5 applies verbatim.

Hence

\[
\boxed{
\text{extra block counts plus full merging into separately paid
three-boxes do not evade the obstruction.}
}
\tag{35}
\]

If a fixed number \(d\ge4\) of chain factors is retained and each
\(d\)-box is covered as one fused object, the DRAY lower bound no longer
applies.  That is a genuinely different local problem.

If the number of retained factors tends to infinity with \(k\), the local
dimension is no longer fixed; at the extreme of one coordinate per factor
the local object is the original Boolean cube.  Such a choice is not a
fixed-dimensional product reduction.

---

## 7. Exact averaged gate for a fused fixed dimension

Fix \(d\ge2\) and positive proportions

\[
s_i=\alpha_i k+O(1),
\qquad \alpha_i>0,\quad \sum_i\alpha_i=1.
\]

Let

\[
\mathcal B_{d,k}=\prod_{i=1}^dW(s_i),
\]

and let \(L_i\) be independent uniform SCD heights.  Exact width
telescoping gives

\[
\sum_{\rm boxes}w_d(\boldsymbol L)=W(k).
\tag{36}
\]

Using an optimal local word in each translated box, plus at most one local
origin anchor, gives

\[
L_{d,\rm sep}(k)
=W(k)+\mathcal B_{d,k}\,\mathbb E E_d(L_1,\ldots,L_d)
+O(\mathcal B_{d,k}).
\tag{37}
\]

Moreover

\[
\frac{\mathcal B_{d,k}}{W(k)}
\sim
\frac{(2/\pi)^{(d-1)/2}}
{\sqrt{\alpha_1\cdots\alpha_d}\,k^{(d-1)/2}}.
\tag{38}
\]

Since \(\mathcal B_{d,k}=o(W(k))\), equations (37)--(38) prove:

### Theorem 7.1 (exact fused-box replacement gate)

For a fixed positive-proportion \(d\)-block split, independent local-box
aggregation has leading constant one if and only if

\[
\boxed{
\mathbb E E_d(L_1,\ldots,L_d)
=o\bigl(k^{(d-1)/2}\bigr).
}
\tag{39}
\]

For \(d=3\), Theorem 4.1 proves that (39) is false.  The first surviving
fixed-dimensional candidate is

\[
\mathbb E E_4(L_1,L_2,L_3,L_4)=o(k^{3/2}),
\]

which is precisely (GF4).

This averaged statement is strictly less uniform than asking

\[
E_4(\ell_1,\ell_2,\ell_3,\ell_4)=o(R^3)
\]

for every compact \(R\)-scale aspect ratio.  It asks only for the average
under the four independent SCD height laws.  It is therefore the sharp
replacement gate for the fixed four-block product architecture.

---

## 8. What cross-box witness sharing must accomplish

Let \(\mathscr C_k\) be the positive-density family of bad three-boxes in
the compact sector used in Theorem 4.1.  There are

\[
\Theta(W(k)/k)
\]

such boxes and every one has isolated excess \(\Theta(k)\).  Thus

\[
\sum_{C\in\mathscr C_k}E_3(C)=\Theta(W(k)).
\tag{40}
\]

Suppose a packet construction replaces independently optimal child words
by words covering unions of children.  If the final length is
\(W(k)+o(W(k))\), its sharing saving relative to the isolated sum must be

\[
\Omega(W(k)).
\tag{41}
\]

Equivalently, averaged over the bad children, it must save

\[
\Omega(k)
\tag{42}
\]

per child.  Therefore:

* adding \(o(W(k))\) seam connectors to unchanged child words cannot help;
* a sharing rule whose saving is only \(o(k)\) per bad child cannot help;
* boundary-order or reset-order corrections cannot absorb the DRAY gap.

The rescue, if it exists, must replace the isolated words and share a
leading quadratic amount of witness infrastructure across their boundary.
The complementary exact activity/endpoint ledger in
CROSS_BOX_SHARING_AFTER_DRAY_20260724.md makes this quantitative for equal
blocks: bounded-degree portals, including \(O(R)\)-length corridors per
\(R\)-scale child, have insufficient capacity, while full
\(\Theta(R^2)\)-surface sharing and unbounded-degree global portals remain
open.

### A concrete sufficient packet gate

Take four balanced Boolean blocks and one four-chain parent with side
heights \(O(R)\), where \(R=\sqrt k\).  Use an exact rank-centered
outer-hook drain which partitions the parent into \(O(R)\) translated
three-box children

\[
C_0,C_1,\ldots,C_s
\]

and satisfies

\[
\sum_{j=0}^s w_3(C_j)=w_4(\text{parent}).
\tag{43}
\]

The following is sufficient:

> **Adjacent packet fusion (APF).**  Consecutive children can be paired so
> that each translated union \(C_{2j}\cup C_{2j+1}\) has one literal word
> of length
> \[
> w_3(C_{2j})+w_3(C_{2j+1})+o(R^2),
> \tag{44}
> \]
> uniformly on compact parent aspect sets.

There are \(O(R)\) pairs, so (44) gives a parent word of length

\[
w_4(\text{parent})+o(R^3).
\]

The four-block width ledger and the SCD height tails then give
\(W(k)+o(W(k))\).

APF is not contradicted by the DRAY theorem.  The lower bound (10) applies
to a word confined to one isolated three-box.  In (44), witnesses may cross
the common child boundary and may use letters from both translated
children.  Exactly the quadratic saving required by (42) is permitted.

One may instead attack (GF4) directly, without choosing a drain or pairing.
Thus (GF4) is the exact averaged gate, while APF is one concrete sufficient
route to it:

\[
\boxed{
\text{Gaussian-averaged fused four-box excess }o(k^{3/2}),
}
\]

or

\[
\boxed{
\text{adjacent-child packet excess }o(k)
\text{ inside a four-box.}
}

---

## 9. Self-audit

1. **The bad cone, not one ray.**  Equation (6) computes its exact limiting
   mass for one ordering in the balanced split.  The local lower bound is
   applied only on a compact subcone bounded away from \(p=q\) and
   \(r=2q\).

2. **Correct global scale.**  A typical bad local excess is \(\Theta(k)\),
   while the number of three-boxes is \(\Theta(W(k)/k)\).  Equation (18)
   makes this multiplication exact.

3. **Parity.**  SCD heights live on a parity-two mesh.  Joint weak
   convergence applies to rectangles whose boundaries have Rayleigh
   measure zero; no forbidden exact height is prescribed in Sections 2--4.

4. **Highly unbalanced splits.**  The DRAY estimate is used only when the
   smallest block height grows.  When it is fixed, the interval-counting
   bound (29) is used instead.  When a block is absent, the pure-axis bound
   (33) is used.

5. **Translated zero.**  A zero relative letter can be deleted without
   damaging any nonzero maximum witness.  Local origins change the upper
   ledger by at most one entry per box, which is \(o(W(k))\) for every fixed
   positive-proportion block count.

6. **Scope of the no-go.**  Theorem 4.1 and Section 5 rule out separately
   paid three-boxes.  They do not lower-bound an arbitrary four-box word or
   a packet word spanning several children.

7. **More blocks.**  The no-go applies after full reduction to three
   macroblock SCDs because their height histograms are invariant.  Retaining
   four or more factors as one fused local object is deliberately left open
   and is captured exactly by (39).

8. **No hidden claim of rescue.**  (GF4) and APF are precise sufficient
   gates, not proved constructions.

---

## Final status

The audited DRAY lower bound kills the complete three-block
box-by-box SCD product route, not merely its previously advertised primitive
ray lemma.  The killing sector has positive limiting height mass and forces
a positive fraction of global width in extra length.  Neither rebalancing
the three dimensions nor constructing them from more atomic SCD blocks
changes this conclusion.

The Boolean product strategy survives only after a genuine fusion step.
The sharp fixed-dimensional averaged replacement is (GF4).  APF is one
concrete cross-child sufficient gate, not a necessary form of arbitrary
sharing.  Any successful fusion must share quadratic order per bad
three-box, rather than repair it with lower-order seams.

# Cross-audit of the endpoint-potential DRAY dual

Date: 2026-07-24

## Verdict

The principal endpoint-potential claims in
`MATH_ATTACK_S2_DRAY_DUAL_20260724.md` pass an independent reconstruction.
In particular, for

\[
1\le p\le q,\qquad r\ge p+q,\qquad
W=(p+1)(q+1),
\]

the unrestricted bound

\[
\boxed{
g_3(p,q,r)
\ge W+\left\lceil\frac{W(r-p-q)}{2r}\right\rceil
}
\tag{A.1}
\]

is valid for every range-maximum word and every arbitrary choice of one
literal witness per selected target.

The sloped-band strengthening is also correct: for every integer
$0\le k\le p$,

\[
\boxed{
g_3(p,q,r)-W
\ge
\max\!\left\{
0,
\left\lceil
\frac{
(r-p-q+2k)W+\dfrac{k(k+1)(k-6p-6q-4)}3
}{2(r+2k)}
\right\rceil
\right\}.
}
\tag{A.2}
\]

At $r=p+q$, (A.2) gives a positive quadratic excess on every fixed ray.
All denominator signs, integer divisibility claims, floors, positive parts,
and ceilings have the stated directions.

No counterexample or hidden endpoint-choice assumption was found. The only
terminology clarification is that the scarce objects are vertical
**target-poset cover edges**, not physical adjacencies or coordinate
occurrences in the word.

This audit was reconstructed from the definitions and displayed claims; it
does not rely on the internal audit sections of the source report.

---

## 1. Normalization and the precise endpoint choice

Let a word of length $n$ represent the required targets. For every target
$T$ in the target family under consideration, choose one literal witness

\[
I_T=[\ell_T,r_T]
\]

whose coordinatewise maximum is $T$.

The same selected interval supplies both endpoints. This coupling is
essential for orthogonality, but it is not an extra assumption: every
represented target has at least one witness, and the proof works for every
arbitrary simultaneous selection of one witness per target. The proof does
not choose left endpoints and right endpoints independently.

Group targets with equal left endpoint. If two such intervals have right
endpoints $r_1\le r_2$, the first interval is contained in the second, so
their maxima are comparable. Thus every nonempty left-endpoint class is a
poset chain. Equal-right-endpoint classes are chains by the symmetric
containment argument.

The two chain partitions are orthogonal. If two distinct targets lay in
one common left class and one common right class, their selected intervals
would have the same left and right endpoints. They would therefore be the
maximum of the same physical interval, contradicting distinctness.

Unused physical endpoint positions simply give empty classes. Hence each
endpoint partition has at most $n$ nonempty chains. No chain saturation,
canonical witness, unique pin, or common-pin property is used.

When $r\ge p+q$, projection onto $(x,y)$ bounds every antichain by $W$,
while each rank between $p+q$ and $r$ contains one point over every
$(x,y)$. Thus the width is exactly $W$ and every universal word has
$n\ge W$. We may write

\[
n=W+D,\qquad D\in\mathbb Z_{\ge0}.
\tag{A.3}
\]

---

## 2. Independent proof of the flat endpoint-potential bound

Put

\[
P=p+q,\qquad H=r-P.
\]

For $0\le j\le H$, take the full plateau layer

\[
\Lambda_j=
\{(x,y,P+j-x-y):0\le x\le p,\ 0\le y\le q\}.
\tag{A.4}
\]

Every layer has $W$ points.

### 2.1 Covers forced in one endpoint partition

Fix either endpoint partition, and let $C$ be its number of nonempty
chains. Since each $\Lambda_j$ is a $W$-element antichain,

\[
W\le C\le n=W+D.
\]

Write

\[
C=W+\delta,
\qquad 0\le\delta\le D.
\tag{A.5}
\]

Let $A_j$ be the set of chains occupied by $\Lambda_j$. Every chain meets
an antichain in at most one point, so $|A_j|=W$. Therefore

\[
|A_j\cap A_{j+1}|
\ge |A_j|+|A_{j+1}|-C
=W-\delta.
\tag{A.6}
\]

A chain common to the two occupied sets contains comparable points whose
ranks differ by one. Those points form an actual cover edge of the box
poset. Consequently this endpoint partition uses at least

\[
H(W-\delta)
\tag{A.7}
\]

target-poset cover edges between adjacent plateau ranks.

This does not presume that the endpoint chain is saturated. A chain may
skip other ranks; membership in both particular adjacent layers already
forces the cover in (A.6).

### 2.2 Potential bounds the horizontal covers

Use

\[
\phi(x,y,z)=x+y,
\qquad 0\le\phi\le P.
\tag{A.8}
\]

Exactly $W$ chains meet the bottom layer, and exactly $W$ meet the top
layer. Hence exactly $\delta$ chain minima and $\delta$ chain maxima are
internal to the plateau slab. The bottom and top $\phi$-multisets are
identical. Telescoping over all chains therefore gives

\[
\begin{aligned}
\sum_C\bigl(\phi(\max C)-\phi(\min C)\bigr)
&=\sum_{\rm internal\ ends}\phi
  -\sum_{\rm internal\ starts}\phi\\
&\le P\delta.
\end{aligned}
\tag{A.9}
\]

Every horizontal box cover raises $\phi$ by one; every vertical $z$-cover
raises it by zero. All skipped comparable steps have nonnegative
$\phi$-increase. Thus at most $P\delta$ covers counted in (A.7) can be
horizontal. The partition uses at least

\[
H(W-\delta)-P\delta
=HW-(H+P)\delta
=HW-r\delta
\tag{A.10}
\]

vertical target-poset covers.

### 2.3 Coupling the two endpoint partitions

The slab contains exactly $WH$ vertical covers: one in each of the $W$
columns for each of its $H$ rank transitions.

No vertical cover can be used by both endpoint partitions. If its two
endpoint targets belonged to one common left chain and one common right
chain, those two chains would have two common targets, contradicting the
orthogonality proved in Section 1.

Let the two chain-count defects be $\delta_L,\delta_R$. Applying (A.10)
to both partitions and using the vertical capacity gives

\[
2HW-r(\delta_L+\delta_R)\le WH.
\]

Therefore

\[
WH\le r(\delta_L+\delta_R)\le2rD.
\tag{A.11}
\]

Since $D$ is integral and $r>0$,

\[
D\ge
\left\lceil\frac{WH}{2r}\right\rceil
=\left\lceil\frac{W(r-p-q)}{2r}\right\rceil.
\]

Together with (A.3), this proves (A.1). At $H=0$, the numerator is zero
and the conclusion correctly reduces to $D\ge0$.

---

## 3. Independent reconstruction of the sloped band

Fix an integer $0\le k\le p$, retain ranks

\[
P-k,P-k+1,\ldots,r+k,
\]

and define

\[
J=r-P+2k,
\qquad
F=\frac{k(k+1)}2,
\qquad
G=\frac{k(k+1)(k+2)}3.
\tag{A.12}
\]

There are $J+1$ layers and $J$ adjacent-rank transitions.

### 3.1 Layer and vertical-capacity counts

At rank $P-j$, the omitted $(x,y)$ pairs form the upper-right corner whose
complementary coordinates have sum below $j$. At rank $r+j$, the omitted
pairs form the lower-left corner with $x+y<j$. Because
$j\le k\le p\le q$, neither triangle is truncated by a side boundary, and
both have size

\[
\frac{j(j+1)}2.
\]

Thus the two boundary layers have the common size

\[
B_0=W-F.
\tag{A.13}
\]

The total shoulder deficit is

\[
2\sum_{j=1}^k\frac{j(j+1)}2
=\frac{k(k+1)(k+2)}3=G.
\]

Hence the exact number of band targets is

\[
T=(J+1)W-G.
\tag{A.14}
\]

Every vertical column intersects the band in a nonempty contiguous
interval. The total number of vertical covers is therefore the number of
band targets minus the number of columns:

\[
A_v=T-W=JW-G.
\tag{A.15}
\]

### 3.2 Boundary potential difference

Put

\[
S_k=\sum_{u=0}^{k-1}u(u+1)
=\frac{k(k-1)(k+1)}3.
\tag{A.16}
\]

The bottom boundary omits $F$ upper-right points. Their total $\phi$-mass
is $PF-S_k$. The top boundary omits the $F$ lower-left points, whose
total mass is $S_k$. Therefore

\[
\Delta_\phi
:=\sum_{\rm top}\phi-\sum_{\rm bottom}\phi
=PF-2S_k.
\tag{A.17}
\]

The sign and orientation in (A.17) are correct: the top boundary contains
the high-$\phi$ part of the grid, whereas the bottom boundary contains the
low-$\phi$ part.

### 3.3 One endpoint partition

Let one endpoint partition contain $C$ nonempty chains, and let the layer
sizes be $m_0,\ldots,m_J$. For adjacent layers, occupied-chain-set
intersection gives at least

\[
m_i+m_{i+1}-C
\]

covers. This remains a valid lower bound if it is negative. Summing gives

\[
\begin{aligned}
\sum_{i=0}^{J-1}(m_i+m_{i+1}-C)
&=2T-m_0-m_J-JC\\
&=2T-2B_0-JC.
\end{aligned}
\tag{A.18}
\]

Exactly $B_0$ chains start on the bottom boundary and $B_0$ end on the
top. The other $C-B_0$ starts and $C-B_0$ ends are internal. Consequently

\[
\begin{aligned}
\sum_C\bigl(\phi(\max C)-\phi(\min C)\bigr)
&=\Delta_\phi
  +\sum_{\rm internal\ ends}\phi
  -\sum_{\rm internal\ starts}\phi\\
&\le\Delta_\phi+P(C-B_0).
\end{aligned}
\tag{A.19}
\]

Subtracting this upper bound for horizontal covers from (A.18), the
partition uses at least

\[
2T-2B_0-\Delta_\phi+PB_0-(J+P)C
\tag{A.20}
\]

vertical covers.

### 3.4 Coupling, the negative coefficient, and exact algebra

For the left and right partitions, with chain counts $C_L,C_R$, vertical
orthogonality and (A.15) imply

\[
2(2T-2B_0-\Delta_\phi+PB_0)
-(J+P)(C_L+C_R)
\le A_v.
\tag{A.21}
\]

Each partition has at most one nonempty class per physical word endpoint,
so

\[
C_L+C_R\le2n.
\]

The coefficient of this chain-count sum in (A.21) is negative. Therefore

\[
\begin{aligned}
&2(2T-2B_0-\Delta_\phi+PB_0)-2(J+P)n\\
&\qquad\le
2(2T-2B_0-\Delta_\phi+PB_0)
-(J+P)(C_L+C_R)
\le A_v.
\end{aligned}
\tag{A.22}
\]

This verifies the potentially delicate substitution direction.

Insert $n=W+D$ and the values from (A.12)--(A.17). Since $J+P=r+2k$,
(A.22) becomes

\[
2(r+2k)D
\ge JW-3G+4F+4S_k-4PF.
\tag{A.23}
\]

The non-$W$ terms simplify as follows:

\[
\begin{aligned}
-3G+4F+4S_k-4PF
&=k(k+1)\left(
-(k+2)+2+\frac{4(k-1)}3-2P
\right)\\
&=\frac{k(k+1)(k-6P-4)}3.
\end{aligned}
\tag{A.24}
\]

Since $J=r-P+2k$, (A.23)--(A.24) yield

\[
2(r+2k)D
\ge
(r-P+2k)W
+\frac{k(k+1)(k-6P-4)}3.
\tag{A.25}
\]

This is exactly the pre-ceiling form of (A.2).

---

## 4. Finite integrality, positive-part, and ceiling audit

The denominator $2(r+2k)$ is strictly positive. The cubic term in (A.25)
is integral because, modulo $3$,

\[
k(k+1)(k-6P-4)
\equiv k(k+1)(k-1),
\]

which is a product of three consecutive integers.

Let the right numerator of (A.25) be $N_k$. Since $D$ is a nonnegative
integer,

\[
D\ge\frac{N_k}{2(r+2k)}
\]

implies exactly

\[
D\ge
\max\!\left\{
0,
\left\lceil\frac{N_k}{2(r+2k)}\right\rceil
\right\}.
\tag{A.26}
\]

There is no reversed ceiling or missing additive one. At $k=0$, (A.26)
reduces exactly to (A.1).

For later reference, at the boundary $r=P$, the numerator admits the exact
factorization

\[
2kW+\frac{k(k+1)(k-6P-4)}3
=\frac{k}{3}
\left(6pq+k^2-(6P+3)k+2\right).
\]

Thus (A.2) specializes to

\[
\boxed{
D\ge
\max\!\left\{
0,
\left\lceil
\frac{k\bigl(6pq+k^2-(6P+3)k+2\bigr)}
     {6(P+2k)}
\right\rceil
\right\}.
}
\tag{A.27}
\]

This finite formula can be vacuous for small boxes; that is not a
counterexample. The fixed-ray positive term appears at quadratic scale.

---

## 5. Fixed-ray and boundary normalization

Let

\[
p=at,\qquad q=bt,\qquad r=ct,
\qquad s=a+b,
\]

where $0<a\le b$ and $c\ge s$ are fixed. Choose

\[
k=\lfloor xt\rfloor,
\qquad 0\le x\le a.
\]

The numerator in (A.25) is

\[
t^3\left(
ab(c-s+2x)-2sx^2+\frac{x^3}{3}
\right)+O_{a,b,c,x}(t^2),
\tag{A.28}
\]

and the denominator is

\[
2(c+2x)t+O(1).
\tag{A.29}
\]

Therefore the quotient is

\[
\Gamma_{a,b,c}(x)t^2+O(t),
\]

where

\[
\Gamma_{a,b,c}(x)
=\frac{ab(c-s+2x)-2sx^2+x^3/3}{2(c+2x)}.
\tag{A.30}
\]

The floor in $k$ changes the cubic numerator by $O(t^2)$ and hence the
quotient by $O(t)$. The final ceiling changes it by less than one. For each
fixed $x$ with $\Gamma(x)>0$, the positive part is inactive for all
sufficiently large $t$.

Because (A.30) is continuous on the compact interval $[0,a]$, choosing one
fixed maximizer before taking the limit gives

\[
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge\max_{0\le x\le a}\Gamma_{a,b,c}(x).
\tag{A.31}
\]

There is no illicit interchange of a $t$-dependent maximization and a
limit.

### 5.1 Strict plateau

At $x=0$,

\[
\Gamma_{a,b,c}(0)
=\frac{ab(c-a-b)}{2c}.
\]

This proves the strict-plateau normalization. If $c>2b$ and $a<b$, then

\[
\frac{c-a-b}{2c}>
\frac{b-a}{4b},
\]

because the difference has the sign of

\[
(a+b)(c-2b)>0.
\]

Thus the strict sign in the relative lower bound is correct.

### 5.2 Boundary $c=s=a+b$

At the boundary,

\[
\Gamma_{a,b,s}(x)
=\frac{x(2ab-2sx+x^2/3)}{2(s+2x)}.
\tag{A.32}
\]

Choose

\[
x_0=\frac{ab}{4s}.
\]

It is admissible because $x_0\le a/4\le a$. Put

\[
u=\frac{ab}{s^2}\le\frac14.
\]

Direct substitution gives

\[
\Gamma_{a,b,s}(x_0)
=s^2u^2\frac{72+u}{192(2+u)}.
\tag{A.33}
\]

Moreover,

\[
\Gamma_{a,b,s}(x_0)
-\frac{a^2b^2}{6s^2}
=s^2u^2\frac{8-31u}{192(2+u)}>0,
\tag{A.34}
\]

because $u\le1/4$ gives $8-31u\ge1/4$. Hence

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,(a+b)t)-(at+1)(bt+1)}{t^2}
\ge\frac{a^2b^2}{6(a+b)^2}>0.
}
\tag{A.35}
\]

This includes $a=b$. With $k=\lfloor x_0t\rfloor$, the floor error is only
$O(t)$ after division by the linear denominator, so it cannot affect the
positive quadratic constant.

---

## 6. Adversarial counterexample audit

The following possible evasions were checked explicitly.

1. **Choosing different witnesses.** The proof works for every arbitrary
   choice of one interval per target. It only requires that the left and
   right partitions be formed from the two endpoints of that same chosen
   interval. Choosing a different common system of witnesses changes the
   partitions but preserves every inequality.

2. **Unused endpoint positions.** Chain counts are counts of nonempty
   endpoint classes, so they are at most $n$ and need not equal $n$.

3. **Rank-skipping chains.** A chain that meets two adjacent ranks contains
   a genuine cover between its two targets. Other skips only add
   nonnegative potential and cannot reduce the forced cover count.

4. **Nonsaturated endpoint chains.** Neither (A.6) nor (A.18) assumes that
   a chain contains every intermediate target. Only occupied-layer sets
   are used.

5. **Physical pins or multiple occurrences.** The proof never assigns a
   pin to a target-poset edge. Vertical capacity concerns comparable target
   pairs. Arbitrarily many physical occurrences of a coordinate increment
   do not allow the two endpoint partitions to share such a pair.

6. **Sharing only an abstract vertical edge.** This is exactly what
   orthogonality forbids. If both endpoint partitions use the same two
   target vertices as one chain edge, those two targets lie in the same
   left class and the same right class.

7. **Chains internal at both ends.** Such a chain contributes once to the
   internal-start sum and once to the internal-end sum. Equations (A.9) and
   (A.19) remain exact before their one-sided estimates.

8. **Negative intersection lower bounds.** They are harmless: the actual
   intersection size is nonnegative and therefore still at least the
   displayed negative number. Summing these weaker inequalities remains
   valid.

9. **Negative sloped numerator.** The universal width bound gives $D\ge0$;
   this is why the positive part in (A.2) is necessary and sufficient.

10. **Tiny boxes.** The finite sloped certificate can equal zero for small
    parameters. The boundary theorem is an asymptotic fixed-ray statement,
    and its leading coefficient is strictly positive.

No conceptual word construction evades the argument. For example, if
$D=0$ in a strict plateau, each endpoint partition would have exactly $W$
chains. The matching bottom and top potential multisets would force every
one of its $HW$ plateau covers to be vertical. Both partitions would then
need all $WH$ available vertical covers, contradicting orthogonality. This
is the extremal core of (A.11).

---

## 7. Corrections and scope

No mathematical correction to (0.1), (0.4), or the boundary quadratic
excess is required.

For maximum precision, occurrences of “vertical edge” in the source proof
should be read as “vertical target-poset cover edge.” The argument does not
claim that such an edge is a physical adjacency in the representing word.
This is a terminology clarification only.

The endpoint-potential theorem disproves the proposed DRAY and compact
three-box width-plus-subquadratic gates on the full width plateau. It does
not by itself give a lower bound for unrestricted Boolean contiguous-OR
words, since the product-box reductions were sufficient rather than
necessary.

No web search, finite search, or computational search was used in this
cross-audit.

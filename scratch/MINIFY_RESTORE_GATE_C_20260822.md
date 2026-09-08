# Compact restoration block: all-pairing coherent-tour orbit

**Insertion/notation.** Insert after current I.3 and before I.4 as I.3A;
I.2 supplies the equivalent FIFO description. The support is
\(\mathcal K\) to avoid collision with H.14's \(K=r-4\). All assertions
are [I] except the explicitly conditional final corollary.

## I.3A The all-pairing coherent-tour orbit [I]

Let \(b\ge5\) be odd and
\[
 \Omega=\mathbb Z_b\times\mathbb F_2,\qquad P_h=\{h^0,h^1\},\qquad
 \mathcal V={\Omega\choose b},\qquad W=|\mathcal V|={2b\choose b}. \tag{I.3A.1}
\]
Order the pairs cyclically and initially choose \(h^0\) from each. At
stage \(t\), keep the selected member of the special pair \(P_t\), flip
the other selected members in FIFO order, and rotate the pair queue. Every
coordinate is flipped \(b-1\) times, so the \(b\) packets close.

For \(t\ne i\), the internal middle window with empty pair \(P_t\) and
doubled pair \(P_i\) is
\[
 T_{t,i}=P_i\cup\{h^{\chi_{t,i}(h)}:h\notin\{t,i\}\},\qquad
 \chi_{t,i}(h)=t+\mathbf1_{(h-i)(t-i)>0}\pmod2,             \tag{I.3A.2}
\]
using integer representatives \(0,\ldots,b-1\). Before stage \(t\), the
bit at \(h\) is \(t+\mathbf1_{h<t}\pmod2\); the open arc from \(t\) to
\(i\) is then flipped once more, proving (I.3A.2). The empty/doubled
signature recovers \((t,i)\), hence
\[
 \mathcal K=\{T_{t,i}:t\ne i\},\qquad q=|\mathcal K|=b(b-1). \tag{I.3A.3}
\]

A label consists of a perfect pairing, rooted directed cyclic order, and
initial transversal, modulo the free \(b\) phase shifts. Therefore
\[
 |\mathcal E_{\rm lab}|={ (2b)!\over2^bb!}{b!2^b\over b}
 ={(2b)!\over b}.                                          \tag{I.3A.4}
\]
Parallel labels are retained temporarily.

### Theorem I.3A.1 (exact census and maximum codegree)

For \(M_d=|\{(A,B)\in\mathcal K^2:|A\setminus B|=d\}|\),
with empty ranges omitted,
\[
\boxed{\begin{aligned}
M_0&=b(b-1),&M_1&={b(b^2-5)\over2},\\
M_d&=b(b^2+1)&&(2\le d\le b-3,\ d\ {\rm even}),\\
M_d&=b(b^2-3)&&(3\le d\le b-4,\ d\ {\rm odd}),\\
M_{b-2}&={b(b+1)(3b-5)\over2},&
M_{b-1}&=2b^2,\qquad M_b=0.
\end{aligned}}                                              \tag{I.3A.5}
\]
The labelled orbit has
\[
 D_{\rm lab}=(b-1)(b!)^2,\qquad
 {\lambda_d^{\rm lab}\over D_{\rm lab}}
 ={M_d\over b(b-1){b\choose d}^2},                         \tag{I.3A.6}
\]
and consequently
\[
 \boxed{{\Delta_2\over D_{\rm lab}}
 ={b^2-5\over2b^2(b-1)}={1\over2b}+O(b^{-2}).}              \tag{I.3A.7}
\]

#### Proof

Substitution in (I.3A.2) gives this disjoint relation census; a count on a
range is the count at each displayed distance:
\[
\begin{array}{c|c|c}
\text{relation for }(t,i),(u,j)&d&\text{ordered pairs}\\ \hline
(t,i)=(u,j)&0&b(b-1)\\
t=u,\ i\ne j&1\le d\le b-2&2b(b-1-d)\\
i=j,\ t\ne u&1&b(b-1)(b-3)/2\\
i=j,\ t\ne u&b-2&b(b-1)^2/2\\
(u,j)=(i,t)&d\in\{2,4,\ldots,b-1\}&2b\\
\text{exactly one of }t=j,\ i=u&2\le d\le b-1&2b(b-1)\\
|\{t,i,u,j\}|=4&2\le d\le b-2&
b\{b^2-4b+3+4\lfloor d/2\rfloor\}.
\end{array}                                                 \tag{I.3A.8}
\]
For a common empty coordinate, doubled positions \(r,s\in[1,b-1]\) give
\(|r-s|\). For a common doubled coordinate, the two parities give only
\(1,b-2\). Reversed roles give every positive even distance; one crossed
role gives every distance \(2,\ldots,b-1\). In the four-distinct case fix
\(t=0\), write \(1\le x<y<z\le b-1\), and order the remaining roles as
\(IUJ,IJU,UIJ,UJI,JIU,JUI\) (first-double, second-empty,
second-double). For even second-empty position, the six distances are
\[
 z-x,\ b+x-y-1,\ 1-y+z,\ 1-y+z,\ b+x-y-1,\ b+x-z;          \tag{I.3A.9}
\]
for odd position they are their complements to \(b\). Solving these six
linear differences and pairing cases \(1/6,2/5,3/4\) cancels the endpoint
floors and gives the last row of (I.3A.8). The five nonidentity class
totals are
\[
 q(b-2),\quad q(b-2),\quad q,\quad2q(b-2),\quad
 q(b-2)(b-3),                                              \tag{I.3A.10}
\]
which sum to \(q(q-1)\). Thus the census is exhaustive, and summing it by
distance gives (I.3A.5).

The symmetric group is transitive on middle vertices and on ordered pairs
at each Johnson distance. There are \(W{b\choose d}^2\) ambient ordered
pairs at distance \(d\); double counting with (I.3A.4) proves
(I.3A.6). For \(2\le d\le b-2\), use
\(M_d\le M_{b-2}\) and \({b\choose d}\ge{b\choose2}\), obtaining
\[
 {2(b+1)(3b-5)\over b^2(b-1)^3}
 <{b^2-5\over2b^2(b-1)}.                                  \tag{I.3A.11}
\]
The cross-multiplied difference is
\(b^4-2b^3-16b^2+18b+15>0\) for \(b\ge5\). At \(d=b-1\)
the value is \(2/[b(b-1)]\), tying \(d=1\) only at \(b=5\).
This proves (I.3A.7). \(\square\)

Reversal preserves a tour support, so the labelled orbit is not simple.
All supports form one \(S_{2b}\)-orbit. If their common multiplicity is
\(\mu_b\), then
\[
 D_{\rm simp}=D_{\rm lab}/\mu_b,\qquad
 \lambda_{d,\rm simp}=\lambda_d^{\rm lab}/\mu_b,            \tag{I.3A.12}
\]
so (I.3A.6)--(I.3A.7) survive collapse. No value of \(\mu_b\) is used.

### Theorem I.3A.2 (exact fractional middle/adjacent loads)

For one packet's consecutive middle windows \(C_0,\ldots,C_b\), define
\[
 L_i=C_{i-1}\cap C_i,\qquad U_i=C_i\cup C_{i+1}
 \quad(1\le i<b).                                          \tag{I.3A.13}
\]
Each tour has \(q\) distinct targets separately at ranks \(b-1,b,b+1\).
The adjacent occurrence-degrees are
\[
 D_-=D_+={|\mathcal E_{\rm lab}|q\over{2b\choose b-1}}
 =(b-1)(b-1)!(b+1)!,\qquad
 {D_-\over D_{\rm lab}}={D_+\over D_{\rm lab}}={b+1\over b}. \tag{I.3A.14}
\]
Thus uniform tour weight \(1/D_{\rm lab}\) gives exact loads
\[
 \left({b+1\over b},1,{b+1\over b}\right),                 \tag{I.3A.15}
\]
and weight \(1/D_-\) gives \((1,b/(b+1),1)\).

#### Proof

An empty pair identifies a lower target's packet, and targets within the
packet are distinct vertices of its cube path. An internal upper target is
identified by its empty pair and consecutive doubled pairs; a packet-end
upper target has no empty pair and one doubled pair. Incidence counting on
the three transitive layers now gives (I.3A.14)--(I.3A.15). \(\square\)

These fractional loads do not prove an integral augmented matching:
middle-disjoint tours may share adjacent tokens. Also
\(q=b(b-1)\to\infty\), so fixed-uniformity matching theorems do not follow
from (I.3A.7).

### Corollary I.3A.3 (conditional seam implication)

If the simple middle-tour orbit has a matching covering
\((1-o(1))W\) middle targets, it uses at most \(W/[b(b-1)]\) closed
tours. Linearize each tour once and concatenate the singleton words.
There are no internal FIFO seams; each join destroys fewer than
\(2(b+H)\) starts of lengths in \([b-H,b+H]\), and the \(b\) packet
boundaries have the same order of cost. If \(H=o(b)\), the total loss is
\[
 O\!\left({(b+H)W\over b(b-1)}\right)=o(W).                \tag{I.3A.16}
\]
Hence that matching would settle middle coverage and seam cost, but not
cross-tour adjacent collisions or literal coverage at offsets
\(2,\ldots,H\).


# Mathematical attack F2: fused four-chain endpoint braids

Date: 2026-07-25

## 0. Outcome

Let

\[
Q(p,q,r,s)=[0,p]\times[0,q]\times[0,r]\times[0,s]
\]

with coordinatewise maximum, and let $g_4(p,q,r,s)$ be the least length of
a word whose contiguous maxima contain every nonzero point of $Q$.

This exploration gives both a genuine fused construction and a stronger
quantitative obstruction.

1. **Exact two-endpoint-surface equivalence.** A range-maximum word is
   equivalent to two orthogonal endpoint chain partitions, an acyclic
   pairing of their endpoint classes, and explicit coordinate-pin
   inequalities. This is an exact two-dimensional shared-endpoint model,
   not merely a necessary condition.

2. **Explicit two-dimensional portal.** One word of $a+b+1$ points covers
   an $(a+1)(b+1)$ rectangle of targets by literal intervals sharing one
   seam. This is the elementary reset-free four-coordinate braid.

3. **Explicit central-band OR braid.** In the equal box $[0,m]^4$, every
   nonzero target of ranks $2m-D$ through $2m+D$ is covered by one literal
   word of length at most

   \[
   \boxed{M_m+D(11m^2+13m+3)},
   \qquad
   M_m=\frac{2m^3+6m^2+7m+3}{3}.
   \tag{0.1}
   \]

   Hence every sublinear band $D=o(m)$ has a width-plus-$o(m^3)$ fused
   max-word. This is a band theorem, not a full-box theorem.

4. **New bridge-band endpoint obstruction.** The endpoint-potential dual
   extends strictly below the dominant cone. In particular,

   \[
   \boxed{
   \liminf_{t\to\infty}
   \frac{g_4(t,t,t,2t)-w_4(t,t,t,2t)}{t^3}
   \ge\frac5{1344}>0.
   }
   \tag{0.2}
   \]

   It reaches the still closer-to-equal integral ray $(2t,2t,2t,3t)$:

   \[
   \boxed{
   \liminf_{t\to\infty}
   \frac{g_4(2t,2t,2t,3t)-w_4(2t,2t,2t,3t)}{t^3}
   \ge\frac{1791}{25231360}>0.
   }
   \tag{0.3}
   \]

5. Consequently, a full theorem

   \[
   g_4=w_4+o(R^3)
   \]

   cannot hold uniformly on compact comparable four-boxes. The equal ray
   $(1,1,1,1)$ is not ruled out by this dual and remains the primary local
   construction problem.

6. The smallest surviving positive gate is a **pin-compatible selectable-
   rectangle braid** on the equal middle surface. It is stated exactly in
   Section 8. It must share peaks and endpoints across the two-dimensional
   family of hook rectangles; separate fan blocks or separate SCD-chain
   connectors incur a critical $\Theta(m^3)$ loss.

No web search or finite/computational search was used.

---

## 1. Endpoint surfaces: an exact characterization

Let $P$ be any finite product of chains, and let $P^*=P\setminus\{0\}$.

### Definition 1.1 (endpoint scheme of order $n$)

An endpoint scheme consists of:

- a chain partition $\mathcal L$ of $P^*$ into at most $n$ left classes;
- a chain partition $\mathcal R$ of $P^*$ into at most $n$ right classes;
- orthogonality,

  \[
  |L\cap R|\le1
  \qquad(L\in\mathcal L, R\in\mathcal R);
  \tag{1.1}
  \]

- after padding both families by distinct labelled empty dummy classes to
  size $n$, a bijection

  \[
  \mu:\mathcal R\longrightarrow\mathcal L;
  \]

- acyclicity of the directed graph on $\mathcal L$ having, for every
  target $x$, an arc

  \[
  L(x)\longrightarrow\mu(R(x)),
  \tag{1.2}
  \]

  after loops are deleted; and

- a topological bijection $\tau:\mathcal L\to[n]$ for which the pin
  condition below holds.

It assigns the target $x$ the interval

\[
I_x=[\tau(L(x)),\tau(\mu(R(x)))].
\tag{1.3}
\]

For a physical position $j$, put

\[
\mathcal C_j=\{y\in P^*:j\in I_y\}.
\tag{1.4}
\]

The coordinate-pin condition is: for every target $x$ and every coordinate
$c$ with $x_c>0$, some $j\in I_x$ satisfies

\[
\boxed{
\min_{y\in\mathcal C_j}y_c=x_c.
}
\tag{1.5}
\]

### Theorem 1.2 (exact endpoint-surface equivalence)

One has $g(P)\le n$ if and only if an endpoint scheme of order $n$ exists
and satisfies (1.5).

#### Proof: a word gives a scheme

Choose one literal witnessing interval $I_x=[\ell_x,r_x]$ for every target.
Targets with one common left endpoint form a chain, because increasing the
right endpoint enlarges the interval and its maximum. Fixed-right classes
are chains symmetrically.

If two distinct targets belonged to one common left class and one common
right class, their chosen intervals would be identical, hence have the same
maximum. Thus (1.1) holds.

If the word has fewer than $n$ positions, first add unused labelled
positions. Pad the physical endpoint positions by distinct labelled empty
dummy classes and pair the right class at position $j$ with the left class
at position $j$. This is $\mu$.
The physical order is a topological order of (1.2), because every selected
interval satisfies $\ell_x\le r_x$.

Fix $x_c>0$. Some word position $j\in I_x$ attains coordinate $x_c$. Every
target $y$ whose selected interval contains $j$ dominates the word letter
at $j$, so $y_c\ge x_c$. Since $x\in\mathcal C_j$, equality (1.5) follows.

#### Proof: a scheme gives a word

For $\mathcal C_j\ne\varnothing$, define

\[
A_j=\bigwedge_{y\in\mathcal C_j}y
\tag{1.6}
\]

coordinatewise; put $A_j=0$ when $\mathcal C_j$ is empty. If $j\in I_x$,
then $x\in\mathcal C_j$, so $A_j\le x$. Hence

\[
\bigvee_{j\in I_x}A_j\le x.
\]

For every positive coordinate of $x$, condition (1.5) supplies a position
where the corresponding coordinate of $A_j$ equals $x_c$. Therefore

\[
\bigvee_{j\in I_x}A_j=x.
\]

Delete any zero letters. The surviving part of every nonzero witnessing
interval remains contiguous and retains all its coordinate pins. The
resulting word has length at most $n$. $\square$

### Consequence

The four-box problem is genuinely a two-dimensional endpoint problem. The
two partitions alone are insufficient: after endpoint counts and precedence
are solved, (1.5) is the exact remaining contamination condition.

---

## 2. Literal two-dimensional portal braid

Let $i,i',j,j'$ be four distinct coordinates. Suppose all points below are
legal box points, and put

\[
A_u=v-ue_i+ue_{i'}\quad(0\le u\le a),
\qquad
B_z=v+ze_j-ze_{j'}\quad(0\le z\le b).
\tag{2.1}
\]

### Lemma 2.1 (complementary portal)

The word

\[
A_a,A_{a-1},\ldots,A_1,v,B_1,\ldots,B_b
\tag{2.2}
\]

has length $a+b+1$ and, for every $0\le u\le a$ and $0\le z\le b$,
the literal interval from $A_u$ through $v$ to $B_z$ has maximum

\[
\boxed{
v+ue_{i'}+ze_j.
}
\tag{2.3}
\]

Here $A_0=B_0=v$, with the evident endpoint conventions.

#### Proof

On the $A$-arm, coordinate $i'$ is maximized at $A_u$, while coordinate
$i$ is restored to its value at $v$. On the $B$-arm, coordinate $j$ is
maximized at $B_z$, while coordinate $j'$ is maximized at $v$. The four
coordinates are distinct, and every other coordinate is constant. This is
exactly (2.3). $\square$

Thus one shared endpoint seam represents a quadratic rectangle of targets
with only linear physical length. A full braid must arrange a
two-dimensional family of these portals so that their arms can share
physical occurrences without violating the pin condition (1.5).

---

## 3. A direct two-rank sheet word

The portal phenomenon already gives a useful literal surface theorem.
Assume $m\ge1$ and let

\[
P_m=[0,m]^4,
\qquad
M_m=[z^{2m}](1+z+\cdots+z^m)^4.
\]

For $(c,d)\in[0,m]^2$, put

\[
K=2m-1-c-d,
\qquad
L=\max(0,K-m),
\qquad
U=\min(m,K).
\tag{3.1}
\]

When $L\le U$, form the line

\[
W_{c,d}=
(L,K-L,c,d),(L+1,K-L-1,c,d),\ldots,(U,K-U,c,d).
\tag{3.2}
\]

Concatenate all nonempty $W_{c,d}$ and then append once every middle-rank
point whose first or second coordinate is zero. We retain these literal
appendices even if a cross-line seam happens to represent one of them as an
additional maximum.

### Theorem 3.1 (two-rank fused sheet)

This is a literal word of exact length

\[
\boxed{M_m+m^2+2m}
\tag{3.3}
\]

covering every target of ranks $2m-1$ and $2m$.

#### Proof

The lines (3.2) partition rank $2m-1$, so their singleton intervals cover
that rank. Adjacent letters satisfy

\[
(u,K-u,c,d)\vee(u+1,K-u-1,c,d)
=(u+1,K-u,c,d).
\tag{3.4}
\]

These maxima are precisely the middle targets with positive first and
second coordinates. The number of nonempty lines is $(m+1)^2-1=m^2+2m$.
If $C$ is that number, the line-internal adjacent pairs number
$|L_{2m-1}|-C$. Therefore the number of middle points appended literally is

\[
M_m-|L_{2m-1}|+C,
\]

and the total length is $M_m+C$, proving (3.3). $\square$

This is a near-width construction with a two-dimensional family of line
labels $(c,d)$. It covers two ranks only; deeper ranks require the fan
braid below.

---

## 4. Explicit sublinear-depth factor braid

This section gives a single actual max-word, rather than separate join and
meet shadows.

### 4.1 Hook coordinates

For $0\le H\le m$ and $-H\le u\le H$, define

\[
\gamma_H(u)=
\begin{cases}
(H+u,m-H),&u\le0,\\
(H,m-H+u),&u\ge0.
\end{cases}
\tag{4.1}
\]

Every point of $P_m$ is uniquely

\[
X(H,p;K,q)=(\gamma_H(p),\gamma_K(q)),
\tag{4.2}
\]

and its rank is $2m+p+q$.

The middle diagonal in one hook rectangle is

\[
T_{H,K}(u)=(\gamma_H(u),\gamma_K(-u)),
\qquad |u|\le\min(H,K).
\tag{4.3}
\]

Its intervals give all central-square joins and meets. Assume first
$H\ge K$. If $p+q\ge0$ and $|p|\le K$, then

\[
\bigvee_{u=-q}^{p}T_{H,K}(u)=X(H,p;K,q),
\tag{4.4}
\]

and the interval contains $p+q+1$ points. The reversed inequalities give
the lower meet with the same depth-plus-one length. When $H<K$, transpose
the two coordinate pairs; the central-square condition is then
$|q|\le H$.

### 4.2 Tail fans

Assume $H>K$ and fix $1\le r\le H$. Define the upper arms

\[
U_x=(\gamma_H(r-x),(x,m-r))\quad(0\le x<r),
\]

\[
V_t=(\gamma_H(r-t),(0,m-r+t))\quad(1\le t\le r),
\tag{4.5}
\]

in the order

\[
U_{r-1},\ldots,U_0,V_1,\ldots,V_r.
\]

The interval from $U_x$ to $V_t$ has join

\[
(\gamma_H(r),(x,m-r+t))
\tag{4.6}
\]

and has exactly $x+t+1$ points. Its target has rank depth $x+t$ above
$2m$.

Define the lower arms

\[
A_x=(\gamma_H(-x),(x,m))\quad(0\le x\le r),
\]

\[
B_t=(\gamma_H(-t),(r,m-r+t))\quad(1\le t<r),
\tag{4.7}
\]

in the order

\[
A_0,\ldots,A_r,B_{r-1},\ldots,B_1.
\]

The appropriate interval from $A_x$ through $A_r$ and then through $B_t$
has meet

\[
(\gamma_H(-r),(x,m-r+t)),
\tag{4.8}
\]

has $2r-x-t+1$ points, and its target has depth $2r-x-t$ below the middle.

Thus every canonical tail witness again has length exactly depth plus one.
When $t=r$, the interval ends at $A_r$ and the displayed formula is read
with that convention.

### 4.3 Truncation, padding, and erosion

Fix $1\le D\le2m$. In an upper fan put

\[
a_D=\min(D-1,r-1),
\qquad b_D=\min(D,r),
\]

and retain

\[
U_{a_D},U_{a_D-1},\ldots,U_0,V_1,\ldots,V_{b_D}.
\tag{4.13}
\]

In a lower fan put

\[
c_D=\min(D,r),
\qquad e_D=\min(D-1,r-1),
\]

and retain

\[
A_{r-c_D},A_{r-c_D+1},\ldots,A_r,
B_{r-1},B_{r-2},\ldots,B_{r-e_D},
\tag{4.14}
\]

with the $B$-part empty when $e_D=0$. These are exactly the fan terms
needed by **residual** lower witnesses $x<r$ of depth at most $D$; the case
$x=r$ belongs to the central square and is handled by a complete diagonal.
Each retained fan block has length at most $2D$. Include the transposed
blocks for the opposite hook orientation, and retain all complete middle
diagonals (4.3).

In every block, repeat its first and last point $D$ additional times. In
every upper block, also repeat its peak $U_0$ an additional $D$ times.
Concatenate the padded blocks in any order, obtaining

\[
T_1,T_2,\ldots,T_L.
\]

For every coordinate threshold atom, its incidence inside a diagonal is a
prefix or suffix; inside a lower fan it is a prefix union a suffix; inside
an upper fan every internal positive run contains $U_0$. The padding
therefore makes every global internal positive run have length at least
$D+1$.

Define the factor word

\[
A_j=\bigwedge_{i=\max(1,j-D)}^{\min(L,j)}T_i,
\qquad1\le j\le L+D.
\tag{4.9}
\]

The run condition gives the exact erosion identities

\[
T_i=\bigvee_{j=i}^{i+D}A_j,
\tag{4.10}
\]

\[
\bigvee_{j=v}^{u+D}A_j
=\bigwedge_{i=u}^{v}T_i
\quad(v-u\le D),
\tag{4.11}
\]

and, for every interval,

\[
\bigvee_{i=u}^{v}T_i
=\bigvee_{j=u}^{v+D}A_j.
\tag{4.12}
\]

Equations (4.4), (4.6), and (4.8), together with the depth-plus-one
ledger, show that (4.9) represents every target within distance $D$ of the
middle as a literal contiguous maximum.

### 4.4 Exact length ledger

The complete diagonals contain every middle point once, contributing
$M_m$. There are

\[
N=\frac{m(m+1)}2
\]

parameter pairs $(H,r)$ in total. The two orientations and two signs give
four blocks per pair, contributing at most

\[
8DN=4Dm(m+1).
\]

The number of blocks is

\[
(m+1)^2+4N=(m+1)(3m+1).
\]

Endpoint padding costs at most

\[
2D(m+1)(3m+1),
\]

and upper-peak padding costs at most

\[
Dm(m+1).
\]

Hence

\[
L\le M_m+D(11m^2+13m+2).
\]

The factor word (4.9) has $L+D$ positions. Deleting zero letters preserves
all nonzero witnesses, proving (0.1).

### Theorem 4.1 (sublinear-band braid)

For every $D$, the word above covers every nonzero target in the complete band

\[
2m-D\le |x|\le2m+D
\]

and has length at most (0.1). In particular, if $D=o(m)$, its length is

\[
M_m+o(m^3).
\]

---

## 5. A full-box fused connector and a thin-side regime

The best full-box constructor obtained here is still critical-order in the
balanced case.

Assume $h\le a\le b\le c$ and put

\[
d=(h+a-b)_+,
\qquad
\Psi(d)=
\left\lceil\frac d2\right\rceil
\left(\left\lfloor\frac d2\right\rfloor+1\right).
\tag{5.1}
\]

### Theorem 5.1 (three-short-side SCD connector)

There is an explicit full range-maximum word satisfying

\[
\boxed{
g_4(h,a,b,c)
\le(h+1)(a+1)(b+c+1)-1-c\Psi(d).
}
\tag{5.2}
\]

#### Proof

Decompose $[0,h]\times[0,a]$ into its standard symmetric hooks. The hook
indexed by $t=0,\ldots,h$ has edge height

\[
q_t=h+a-2t.
\]

Pairing it with $[0,b]$ and applying the two-chain hooks produces
$\min(q_t,b)+1$ symmetric chains. Hence the nested hook decomposition of

\[
[0,h]\times[0,a]\times[0,b]
\]

has exactly

\[
R_3=(h+1)(a+1)-\Psi(d)
\tag{5.3}
\]

chains, because

\[
\sum_{t=0}^{h}(q_t+1)=(h+1)(a+1)
\]

and

\[
\sum_{t\ge0}(d-2t)_+=\Psi(d).
\]

Pair each chain $C=(C_0<\cdots<C_L)$ with $[0,c]$. The literal arm word

\[
(C_L,0),(C_{L-1},0),\ldots,(C_0,0),
(C_0,1),\ldots,(C_0,c)
\tag{5.3a}
\]

has $c+|C|$ occurrences. The interval from $(C_i,0)$ through $(C_0,j)$
has maximum $(C_i,j)$, so it covers the whole rectangle
$C\times[0,c]$ with internal witnesses. Concatenating
the rectangles and deleting the unique global zero gives length

\[
\begin{aligned}
|[0,h]\times[0,a]\times[0,b]|+cR_3-1
&=(h+1)(a+1)(b+c+1)-1-c\Psi(d).
\end{aligned}
\]

Every four-box target lies in one of the chain rectangles, so the word is
universal. $\square$

For the equal box,

\[
g_4(m,m,m,m)\le\frac74m^3+O(m^2),
\tag{5.4}
\]

whereas

\[
w_4(m,m,m,m)=M_m=\frac23m^3+O(m^2).
\]

Thus this full constructor fuses all fourth-coordinate slices along each
three-side SCD chain, but it does not fuse distinct chains and retains a
$13m^3/12+O(m^2)$ excess.

There is nevertheless a genuine full-box partial regime. If all sides are
at most $CR$ and the shortest side $h=o(R)$, then (5.2) gives, for the
positive-part excess $E_4=(g_4-w_4)_+$,

\[
0\le E_4\le g_4=O((h+1)R^2)=o(R^3).
\tag{5.5}
\]

The obstruction below shows why this cannot be promoted uniformly to the
compact sector $h\asymp R$.

---

## 6. Symmetric bridge-band endpoint dual

This section proves the new quantitative obstruction.

Put

\[
P=p+q+r,
\qquad
V=(p+1)(q+1)(r+1),
\qquad
m_0=\min(p,q,r).
\]

Choose an integer $0\le k\le m_0$ such that

\[
J=s-P+2k\ge0,
\tag{6.1}
\]

and define

\[
\ell=(P-s-k)_+.
\tag{6.2}
\]

Then $0\le\ell\le k$. Put

\[
F_j=\binom{j+2}{3},
\qquad
S_j=3\binom{j+2}{4},
\tag{6.3}
\]

and

\[
E_{\ell,k}=\sum_{j=\ell}^{k}F_j
=\binom{k+3}{4}-\binom{\ell+2}{4}.
\tag{6.4}
\]

Retain every rank from $P-k$ through $s+k$. The endpoints of this band sum
to the total box rank $P+s$, so it is symmetric about the middle.

### Lemma 6.1 (exact bridge-band ledger)

Let $B$ be either boundary size, $T$ the total number of band targets,
$C_0$ the number of base columns meeting the band, and $A_v$ the number of
fourth-coordinate target-poset covers in the band. Then

\[
\boxed{
B=V-F_k-F_\ell,
}
\tag{6.5}
\]

\[
\boxed{
T=(J+1)V-2E_{\ell,k},
}
\tag{6.6}
\]

\[
\boxed{
C_0=V-2F_\ell,
\qquad
A_v=T-C_0.
}
\tag{6.7}
\]

For the potential $\phi=x+y+z$, the top-minus-bottom boundary mass is

\[
\boxed{
\Delta_\phi
=P(F_k-F_\ell)+2(S_\ell-S_k).
}
\tag{6.8}
\]

#### Proof

At a band rank $u$, a base triple is omitted at the low corner when
$x+y+z<u-s$ and at the high corner when its complementary base sum is
less than $P-u$. Across the band the two corner depths run from $\ell$ to
$k$ in opposite orders. The bound $k\le m_0$ makes every tetrahedral corner
untruncated, proving (6.5)--(6.6).

A base column of sum $a$ has ranks $a,a+1,\ldots,a+s$. It meets the band
exactly when

\[
\ell\le a\le P-\ell.
\]

The two omitted base corners each have $F_\ell$ columns. Every active
column contributes one fewer vertical edge than vertices, proving (6.7).

The total base potential is $PV/2$ by complement symmetry. The bottom
boundary omits a low corner of mass $S_\ell$ and a high corner of mass
$PF_k-S_k$. Hence its potential mass is

\[
\frac{PV}{2}-S_\ell-PF_k+S_k.
\]

The top boundary is its complement, so subtracting twice the bottom mass
from $PB$ gives (6.8). $\square$

### Theorem 6.2 (exact bridge-band lower bound)

Let $w=w_4(p,q,r,s)$. Every universal word satisfies

\[
\boxed{
g_4(p,q,r,s)
\ge
\max\left\{
w,
V+\left\lceil
\frac{\mathcal N_{p,q,r,s}(k)}{2(s+2k)}
\right\rceil
\right\},
}
\tag{6.9}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal N_{p,q,r,s}(k)
={}&JV-6E_{\ell,k}+4(S_k-S_\ell)\\
&+4(1-P)F_k+2F_\ell.
\end{aligned}
}
\tag{6.10}
\]

#### Proof

Choose one arbitrary literal witness for every target in the band, using
the same interval to form the left- and right-endpoint chain partitions.
Let one partition have $C$ nonempty chains and let the successive layer
sizes be $b_0,\ldots,b_J$. Adjacent occupied-chain sets force at least

\[
2T-2B-JC
\tag{6.11}
\]

target-poset covers.

Exactly $B$ chains start at the bottom and $B$ end at the top. Telescoping
$\phi$ gives

\[
\sum_C(\phi(\max C)-\phi(\min C))
\le\Delta_\phi+P(C-B).
\tag{6.12}
\]

Every nonvertical cover consumes one unit of this potential. Therefore the
partition uses at least

\[
2T-2B-\Delta_\phi+PB-(J+P)C
\tag{6.13}
\]

vertical covers.

The two endpoint partitions cannot share a vertical target-poset cover,
because its two targets would then lie in one common left class and one
common right class. Their selected intervals would have both endpoints in
common, contradicting orthogonality.

If the physical word has length $n$, both chain counts are at most $n$.
The coefficient of their sum in (6.13) is negative, so substituting the
upper bound $2n$ has the valid direction and yields

\[
2(2T-2B-\Delta_\phi+PB)-2(J+P)n\le A_v.
\tag{6.14}
\]

Since $J+P=s+2k$, substitution of (6.5)--(6.8) simplifies exactly to

\[
2(s+2k)(n-V)\ge\mathcal N_{p,q,r,s}(k).
\tag{6.15}
\]

The quantity $n-V$ is integral even when $V$ is not the width. Taking the
ceiling in (6.15) and combining it with the independent width bound
$n\ge w$ proves (6.9). $\square$

### Checks

- When $s\ge P$, one has $\ell=0$, and (6.9) reduces to the previously
  known dominant sloped-band theorem.
- When $s<P$, the active-column correction $2F_\ell$ is essential. Omitting
  it gives the wrong finite normalization.
- No physical adjacency or common coordinate pin is assumed. The scarce
  objects in (6.14) are target-poset cover edges.

---

## 7. Comparable non-dominant ray obstructions

Let

\[
(p,q,r,s)=(at,bt,ct,dt),
\qquad
A=a+b+c,
\qquad
\delta=A-d>0.
\]

Assume $\delta/2\le\min(a,b,c)$. For the positive-width band, take

\[
k=\lfloor xt\rfloor,
\qquad
\frac\delta2<x\le\min(\delta,a,b,c),
\]

and put $y=\delta-x$. The endpoint lower bound has leading length
coefficient

\[
\boxed{
L_{a,b,c,d}(x)=
\frac{
abc(2A+6x-3\delta)
-\dfrac23Ax^3
+\dfrac14(x^4-y^4)
}{2(A-\delta+2x)}.
}
\tag{7.1}
\]

The central-layer width is

\[
\boxed{
w_4(at,bt,ct,dt)
=\left(abc-\frac{\delta^3}{24}\right)t^3+O(t^2).
}
\tag{7.2}
\]

Indeed, projection onto the first three coordinates removes two
untruncated tetrahedral corners of depth $\delta t/2+O(1)$.

Writing

\[
x=\frac\delta2+e,
\]

one has the useful exact leading factorization

\[
\boxed{
L(x)-\left(abc-\frac{\delta^3}{24}\right)
=
\frac{
e\left[
\Theta-A\delta e+\left(\delta-\frac{2A}{3}\right)e^2
\right]
}{2(A+2e)},
}
\tag{7.3}
\]

where

\[
\Theta=2abc-\frac{A\delta^2}{2}+\frac{5\delta^3}{12}.
\tag{7.4}
\]

Thus, whenever

\[
\frac\delta2<\min(\delta,a,b,c),
\]

every sufficiently small admissible $e>0$ gives cubic excess if
$\Theta>0$. At the endpoint $x=\delta/2$, parity should instead be handled
with $k=\lceil(P-s)/2\rceil$; that zero-thickness choice recovers width but
does not itself give excess.

### Corollary 7.1 (a broad comparable cone)

If

\[
0<a\le b\le c\le d,
\qquad d\ge b+c,
\]

then

\[
g_4(at,bt,ct,dt)
\ge w_4(at,bt,ct,dt)+\Omega_{a,b,c,d}(t^3).
\tag{7.5}
\]

#### Proof

If $d>A$, the strict dominant flat-band bound already gives positive cubic
excess. If $d=A$, the dominant sloped boundary theorem does so. It remains
to consider $b+c\le d<A$, for which

\[
0<\delta=A-d\le a.
\]

After division by $\delta^3$, write
$a/\delta,b/\delta,c/\delta\ge1$. The function

\[
2xyz-\frac{x+y+z}{2}
\]

is coordinatewise increasing on $[1,\infty)^3$ and equals $1/2$ at
$(1,1,1)$. Hence $\Theta/\delta^3\ge11/12>0$. Apply (7.3) with small
$e>0$. $\square$

### Corollary 7.2 (ray $(1,1,1,2)$)

Take $a=b=c=1$, $d=2$, $\delta=1$, and $x=3/4$. Equation (7.1) gives

\[
L(3/4)=\frac{431}{448},
\]

while (7.2) gives

\[
\frac{w_4(t,t,t,2t)}{t^3}=\frac{23}{24}+O(t^{-1}).
\]

Their difference is

\[
\frac{431}{448}-\frac{23}{24}=\frac5{1344},
\]

proving (0.2). For completeness, the exact parity width counts are

\[
w_4(2u,2u,2u,4u)
=(2u+1)^3-2\binom{u+2}{3},
\]

and, with the obvious substitution $t=2u+1$,

\[
w_4(t,t,t,2t)
=(t+1)^3-\binom{(t-1)/2+2}{3}
             -\binom{(t-1)/2+3}{3}.
\]

Both have leading coefficient $23/24$.

### Corollary 7.3 (closer ray $(2,2,2,3)$)

Normalize first to $(1,1,1,3/2)$. Then

\[
\delta=\frac32,
\qquad
x=\frac{193}{256}=\frac\delta2+\frac1{256}.
\]

In (7.3),

\[
\Theta=\frac1{32},
\]

and the bracket equals

\[
\frac{1791}{131072}.
\]

Therefore the normalized cubic excess is

\[
\frac{1791}{201850880}.
\]

For the integral ray $(2t,2t,2t,3t)$, take

\[
k=\left\lfloor\frac{193}{128}t\right\rfloor.
\]

Replacing the normalized scaling parameter by $2t$ multiplies the
coefficient by eight and gives (0.3).

This dual does not reach the equal cube. There $\delta=2$ and the only
admissible bridge band has $J=0$, so (6.9) reduces to the ordinary width
bound.

---

## 8. Exact remaining construction lemma

For paired equal sides, the central surface has an especially flexible
two-dimensional rectangle structure.

### Lemma 8.1 (selectable central rectangles)

Let

\[
Q=[0,p]^2\times[0,r]^2,
\qquad h=p+r.
\]

Every target of rank $h+d$ is the join of a rectangle of middle-rank
points, and every target of rank $h-d$ is the meet of such a rectangle.

More precisely, if $x=(x_1,x_2,x_3,x_4)$ has rank $h+d$, choose
nonnegative integers $\alpha,\beta$ with $\alpha+\beta=d$ and

\[
\alpha\le\min(x_1,x_2),
\qquad
\beta\le\min(x_3,x_4).
\]

Then, with $u=x_1+x_2-\alpha$, the points

\[
(i,u-i,j,h-u-j),
\quad
x_1-\alpha\le i\le x_1,
\quad
x_3-\beta\le j\le x_3,
\tag{8.1}
\]

have join $x$.

For rank $h-d$, choose nonnegative integers $\alpha,\beta$ with
$\alpha+\beta=d$ and

\[
\alpha\le p-\max(x_1,x_2),
\qquad
\beta\le r-\max(x_3,x_4),
\]

put

\[
u=x_1+x_2+\alpha.
\]

Then the points

\[
(i,u-i,j,h-u-j),
\quad
x_1\le i\le x_1+\alpha,
\quad
x_3\le j\le x_3+\beta,
\tag{8.2}
\]

have meet $x$.

#### Proof

In the upper case,

\[
\min(x_1,x_2)+\min(x_3,x_4)
\ge |x|-(p+r)=d,
\]

so an admissible split exists. The four coordinate extrema of (8.1) are
exactly $x_1,x_2,x_3,x_4$. In the lower case,

\[
(p-\max(x_1,x_2))+(r-\max(x_3,x_4))
\ge h-|x|=d,
\]

so the required split again exists, and the four coordinate minima in
(8.2) are exactly those of $x$. $\square$

The split $d=\alpha+\beta$ is selectable; it is not fixed by the target.
That freedom is precisely what a global braid may use to avoid the endpoint
dual collisions.

### Proposition 8.2 (canonical fixed-delay peak obstruction)

In an upper fan (4.5) with $r\ge2$, the threshold atom in the second
coordinate of the first pair at level

\[
m-H+r
\]

occurs only at the peak $U_0$. Its two canonical neighbours $U_1,V_1$
omit that atom. Hence, if the fan is retained as one ordered block in a
delay-$q$ erosion factor, its peak region must contain at least $q$
additional occurrences carrying this atom.

#### Proof

Along the fan, the first-pair hook parameter rises to $r$ at $U_0$ and
then falls. For nonnegative parameter $z$, the relevant coordinate of
$\gamma_H(z)$ is $m-H+z$, so the level $m-H+r$ occurs only at $z=r$.
It is therefore an internal singleton positive run. The delay-$q$ run
criterion forces every internal positive run to have at least $q+1$
positions. $\square$

There are $\Theta(m^2)$ disjoint canonical upper-fan blocks. Translating
all canonical lower fan meets by one fixed delay requires $q\ge2m-1$, since
the longest lower witness has $2m$ terms. Thus this literal blockwise
architecture pays $\Omega(m^3)$ peak repetitions. The proposition does not
apply after global peak interleaving or after abandoning a common delay.

### Unproved selectable-rectangle factor braid

The smallest full equal-box gate is the following.

> Order the $M_m$ middle points as a row
> $T_1,\ldots,T_L$ with $L=M_m+o(m^3)$, assign one selectable rectangle
> from Lemma 8.1 to every off-middle target, and choose carrier intervals
> $J_i\subseteq[N]$, where $N=M_m+o(m^3)$. Define
>
> \[
> A_k=\bigwedge_{i:k\in J_i}T_i,
> \]
>
> using $A_k=0$ when no carrier covers $k$. Require:
>
> 1. every middle label has all coordinate pins in its own carrier $J_i$,
>    so that $\bigvee_{k\in J_i}A_k=T_i$;
> 2. every selected upper rectangle is one consecutive row interval
>    $[a,b]$, and $\bigcup_{i=a}^bJ_i$ is a physical interval;
> 3. every selected lower rectangle is one consecutive row interval
>    $[a,b]$ having a nonempty physical interval
>    $K_{a,b}\subseteq\bigcap_{i=a}^bJ_i$; and
> 4. for each positive coordinate of the lower meet, some position in
>    $K_{a,b}$ has the corresponding coordinate pin against every carrier
>    covering that position.

Then every upper target is the OR over its contiguous carrier union, while
every lower target is the OR over its pinned common core. Thus this would
give

\[
g_4(m,m,m,m)=M_m+o(m^3).
\]

This lemma is unproved.

The depth-truncated construction proves it for every prescribed
$D=o(m)$ after discarding targets outside the central band. What fails at
linear depth is global peak sharing: retaining the canonical fan blocks and
one common delay forces $\Theta(m^2)$ separate peak runs, each needing
$\Theta(m)$ padding, hence $\Theta(m^3)$ extra occurrences. This is an
architecture-specific obstruction, not a lower bound for unrestricted
$g_4(m,m,m,m)$.

---

## 9. Adversarial audit and final status

The main claims were attacked independently. The following points were
checked.

1. **Endpoint choice.** One arbitrary witness is selected per target, and
   both endpoint partitions use that same interval. No canonical or
   shortest witness is assumed.

2. **Endpoint equivalence.** Necessity uses an actual coordinate pin from
   the word. Sufficiency uses the maximal legal letter (1.6); zero deletion
   preserves all nonzero factors.

3. **Bridge-band overlap.** When $s<P$, both low and high corners can be
   missing from one layer. The active-column correction $2F_\ell$ and the
   boundary low-corner mass $S_\ell$ are both retained.

4. **Cover-edge meaning.** Orthogonality concerns target-poset covers, not
   physical word adjacencies. Multiple physical coordinate occurrences do
   not evade (6.14).

5. **Negative coefficient.** Replacing the two endpoint chain counts by
   their upper bound $2n$ in (6.14) has the correct direction.

6. **Floors and ceilings.** Changing $k=xt$ by $O(1)$ changes the bridge
   numerator by $O(t^3)$ and the quotient by $O(t^2)$, harmless after
   $t^3$ normalization. Equation (6.9) uses the ceiling of the possibly
   negative integer defect $n-V$ and separately retains $n\ge w$.

7. **Band word.** The erosion identities (4.10)--(4.12) are global after
   block concatenation. Padding is per physical point, not per atom, and
   the exact coefficient in (0.1) includes the final $D$ factor positions.

8. **Scope.** Equations (0.2)--(0.3) disprove a uniform compact four-box
   width-plus-subcubic theorem. They do not disprove such a theorem on the
   single equal ray, and they do not lower-bound unrestricted Boolean
   contiguous-OR words.

### Stable conclusion

The four-chain geometry genuinely supports two-dimensional shared-endpoint
fusion: portals cover quadratic target sheets with linear arms, and an
entire sublinear central band has a near-width literal max-word. But a
standalone width-plus-$o(R^3)$ theorem is impossible on compact comparable
boxes as a class. The equal box survives only behind the precise
pin-compatible selectable-rectangle braid stated in Section 8.

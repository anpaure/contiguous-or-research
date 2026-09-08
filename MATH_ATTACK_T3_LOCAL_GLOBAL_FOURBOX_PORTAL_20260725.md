# Third-wave T: local-to-global four-box portal braids

Date: 2026-07-25

## 0. Verdict

The box-confined four-chain theorem is already false on compact dominant
rays, so the only viable fixed-four-block route must share letters or
physical endpoints between product boxes. This report gives several exact
positive portal constructions and several scoped negative theorems.

1. **Positive adjacent-box portal.** Two geometrically adjacent
   four-chain boxes admit a directed dominated-endpoint atlas. Earlier-box
   arm letters replace one whole arm of a later-box boundary portal. For
   balanced side \(m\), one interface word of length

   \[
   (m+1)(2m+1)
   \]

   covers the entire \((m+1)^3\)-point bottom face of the later box and
   \(m(m+1)\) earlier endpoint targets. Relative to the two separate
   canonical catalogues it saves exactly \(m(m+1)\) occurrences. Every
   interval is displayed below. Repeating the module through all shifted
   layers covers the entire later four-box in length
   \((m+1)^2(2m+1)\), with the same exact saving. A reoriented alternating
   braid gives a complete word for both adjacent boxes of length
   \(3m^3+7m^2+6m+1\), saving exactly \(m^2(m+1)\) against the two
   corresponding separate alternating words.

2. **Exact balanced drain seam.** In the alternating outer-hook drain of
   \([0,m]^4\), a word of length \(m(m+1)\) crosses all \(m\) adjacent
   child pairs and certifies

   \[
   \frac{m(m+1)(m+2)}3
   \]

   displayed cross-child targets, \(m(m+1)/2\) earlier-child singleton
   targets, and \(m-1\) free inter-block seam targets. This is a genuine
   reset-free face atlas, but not a universal word for the child pairs.

3. **Complete balanced child-pair braid.** The first two outer-hook
   children of \([0,m-1]^2\times[0,m]^2\) have a literal word covering
   every nonzero point of their union, of length

   \[
   6m^2-5m+1.
   \]

   This saves exactly \(m\) occurrences against the two explicit
   separate alternating-slice words. Its excess above the pair width is
   nevertheless \(4m^2-5m+1\).

4. **Adjacent-packet fusion is false.** For the parent
   \([0,t]^3\times[0,4t]\) with odd \(t\), some consecutive exact-drain
   child pair has
   unavoidable excess among words whose letters lie anywhere in that
   ambient parent:

   \[
   \left(\frac1{12}-o(1)\right)t^2
   \]

   above the sum of its two exact child widths. Thus the former uniform
   \(o(R^2)\) adjacent-packet gate cannot hold.

5. **Subvolume endpoint-interface no-go.** For two aligned closed-dominant
   four-chain product boxes, a near-sum-width packet requires
   \(\Theta(R^3)\) typed same-side endpoint coincidences. Any portal
   architecture with only \(O(R^2)\) typed endpoint sites therefore leaves
   \(\Omega(R^3)\) excess. For two boxes of shape
   \((t,t,t,3t)\), an explicit certified leading sharing demand is at least

   \[
   \left(\frac{49}{128}-o(1)\right)t^3.
   \]

The slab atlas of Section 2 and the aligned-box endpoint theorem concern
different adjacency geometries. The former is rank-staggered: the later
baseline strictly dominates the earlier endpoint. Sections 3 and 4 do
concern the same exact-drain adjacency, but are also compatible:
Theorem 3.1 is only a face atlas, and Theorem 3.2 retains
\(\Theta(m^2)\) excess, whereas Theorem 4.1 rules out a uniform
\(o(R^2)\)-excess theorem for every adjacent pair. Product boxes from a
four-block SCD have aligned middle layers. Their same-rank targets cannot
share same-side endpoints, and the endpoint-potential toll must instead
be amortized through volume-order interleaving.

No width-scale global braid is constructed. The sharp remaining escape is
unbounded-degree or volume-order endpoint sharing across many boxes,
possibly through a full three-dimensional interface, not a fixed-size
packet joined by the \(O(R^2)\)-support modules constructed here.

---

## 1. Conventions and two notions of adjacency

For a translated product of four chains \(B\), let \(w(B)\) denote its
width. A literal ambient word may use letters outside \(B\); it covers a
target \(T\in B\) when one contiguous interval has coordinatewise maximum
\(T\).

Two notions of adjacency must be separated.

1. **Geometric slab adjacency.** Two axis-parallel four-boxes occupy
   consecutive integer intervals in one coordinate. Their middle ranks
   need not align. This is where the positive dominated-endpoint portal
   lives.

2. **Aggregation adjacency.** Two disjoint product boxes are placed next
   to one another in a packet of a global four-block SCD construction. If
   a box has bottom rank \(A\) and total side height \(N-2A\), the ambient
   rank of its local middle layer is

   \[
   A+\left\lfloor\frac{N-2A}{2}\right\rfloor
   =\left\lfloor\frac N2\right\rfloor.
   \]

   The summand after \(A\) is the local middle rank; the displayed sum is
   its ambient rank. Thus every product-box middle layer lies in the same
   Boolean rank.
   Width layers from distinct boxes form one disjoint ambient antichain.

The second alignment is exactly what makes widths add globally and what
forces the endpoint-sharing no-go.

---

## 2. Directed dominated-endpoint portal

### Lemma 2.1 (one-arm endpoint substitution)

Let \(x,y\in\mathbb Z_{\ge0}^d\), let \(i\ne j\), and suppose

\[
x\le y,\qquad x_i=y_i,\qquad x_j=y_j.
\tag{2.1}
\]

Assume the following points are legal in the ambient product:

\[
X_u=x+u e_i,\qquad1\le u\le a,
\]

\[
Y_z=y+z e_j,\qquad0\le z\le b.
\]

Then the literal word

\[
\boxed{
X_a,X_{a-1},\ldots,X_1,Y_0,Y_1,\ldots,Y_b
}
\tag{2.2}
\]

has length \(a+b+1\), and for every \(0\le u\le a\),
\(0\le z\le b\),

\[
\boxed{
\bigvee
\begin{cases}
[Y_0,\ldots,Y_z],&u=0,\\
[X_u,\ldots,X_1,Y_0,\ldots,Y_z],&u\ge1
\end{cases}
=y+u e_i+z e_j.
}
\tag{2.3}
\]

#### Proof

For coordinates other than \(i,j\), the maximum is \(y\) because
\(x\le y\). In coordinate \(i\), the \(X\)-suffix has maximum
\(x_i+u=y_i+u\), while every \(Y\)-letter has value \(y_i\). In coordinate
\(j\), every \(X\)-letter has value \(x_j=y_j\), and the \(Y\)-prefix has
maximum \(y_j+z\). This proves (2.3). \(\square\)

The omitted point \(X_0=x\) is dominated by \(Y_0=y\). A common-base portal
would contain both endpoints; here the later endpoint substitutes for the
earlier one. The direction \(x\le y\) is essential.

### Theorem 2.2 (adjacent four-box face atlas)

Fix nonnegative integers \(a,b,c,c',d\), with \(b,d\ge1\), and let

\[
Q^-=[0,a]\times[0,b]\times[0,c]\times[0,d],
\]

\[
Q^+=[0,a]\times[0,b]\times[c+1,c+1+c']\times[0,d].
\tag{2.4}
\]

These are disjoint geometrically adjacent four-chain boxes. For
\(0\le h\le a\), define

\[
X_u^{(h)}=(h,u,c,0),\qquad1\le u\le b,
\]

\[
Y_z^{(h)}=(h,0,c+1,z),\qquad0\le z\le d.
\tag{2.5}
\]

Concatenate the blocks

\[
\mathcal P_h=
X_b^{(h)},X_{b-1}^{(h)},\ldots,X_1^{(h)},
Y_0^{(h)},Y_1^{(h)},\ldots,Y_d^{(h)}
\tag{2.6}
\]

in any order of \(h\). The resulting seam atlas \(\mathcal P\) has exact
length

\[
\boxed{|\mathcal P|=(a+1)(b+d+1).}
\tag{2.7}
\]

It represents:

- every earlier endpoint target

  \[
  \mathcal E^-=
  \{(h,u,c,0):0\le h\le a,\ 1\le u\le b\}
  \tag{2.8}
  \]

  as a singleton; and

- every point of the later bottom interface

  \[
  \mathcal F^+=
  \{(h,u,c+1,z):
  0\le h\le a,\ 0\le u\le b,\ 0\le z\le d\}
  \tag{2.9}
  \]

  by the interval (2.3) internal to \(\mathcal P_h\).

#### Proof

For fixed \(h\), apply Lemma 2.1 with

\[
x=(h,0,c,0),\qquad y=(h,0,c+1,0),\qquad i=2,\quad j=4.
\]

All displayed letters lie in the indicated adjacent boxes. Different
\(h\)-blocks are disjoint because their first coordinates differ. The
count (2.7) and both coverage claims follow. \(\square\)

### 2.3 Exact cost ledger

The independent canonical catalogues would:

1. list the \(b(a+1)\) earlier endpoint targets in \(\mathcal E^-\); and
2. use, for every \(h\), a fresh later-box arm

   \[
   (h,b,c+1,0),\ldots,(h,1,c+1,0)
   \]

   followed by \(Y_0^{(h)},\ldots,Y_d^{(h)}\), at total cost
   \((a+1)(b+d+1)\).

Their combined length is

\[
(a+1)(2b+d+1).
\tag{2.10}
\]

The cross-box atlas reuses the earlier \(X\)-arms in place of the fresh
later arms and saves exactly

\[
\boxed{(a+1)b}
\tag{2.11}
\]

occurrences relative to those canonical catalogues.

For two adjacent equal boxes of side \(m\),

\[
|\mathcal P|=(m+1)(2m+1),
\tag{2.12}
\]

the canonical saving is \(m(m+1)\), and the atlas represents

\[
(m+1)^3+m(m+1)
\tag{2.13}
\]

distinct displayed targets. This is a balanced nontrivial seam theorem.
Its saving is surface-order \(\Theta(m^2)\), not volume-order
\(\Theta(m^3)\).

The comparison in (2.10)--(2.11) is an exact construction ledger, not an
optimality theorem for arbitrary words.

### 2.4 One-sided whole-box portal raster

The same seam can be repeated layer by layer to cover the entire later
four-box. For \(0\le h\le a\) and \(0\le\tau\le c'\), define occurrence
copies

\[
X_u^{(h,\tau)}=(h,u,c,0)\quad(1\le u\le b),
\]

\[
Y_z^{(h,\tau)}=(h,0,c+1+\tau,z)\quad(0\le z\le d),
\tag{2.14}
\]

and concatenate, in any order of \((h,\tau)\), the blocks

\[
\mathcal P_{h,\tau}=
X_b^{(h,\tau)},\ldots,X_1^{(h,\tau)},
Y_0^{(h,\tau)},\ldots,Y_d^{(h,\tau)}.
\tag{2.15}
\]

The \(X\)-letters with fixed \(h\) have the same value in different
\(\tau\)-blocks, but are distinct physical occurrences.

### Corollary 2.3 (one-sided whole-box raster)

The word

\[
\mathcal R=\mathop{\Vert}_{h,\tau}\mathcal P_{h,\tau}
\]

has exact length

\[
\boxed{|\mathcal R|=(a+1)(c'+1)(b+d+1)}
\tag{2.16}
\]

and covers every point

\[
(h,u,c+1+\tau,z)\in Q^+.
\]

For \(u=0\), the witness is
\([Y_0^{(h,\tau)},\ldots,Y_z^{(h,\tau)}]\). For \(u\ge1\), it is

\[
[X_u^{(h,\tau)},\ldots,X_1^{(h,\tau)},
Y_0^{(h,\tau)},\ldots,Y_z^{(h,\tau)}],
\tag{2.17}
\]

whose maximum is literally \((h,u,c+1+\tau,z)\) by Lemma 2.1. Every
target in \(\mathcal E^-\) is also a singleton at any one of its
\(\tau\)-copies.

The canonical separate comparison lists \(\mathcal E^-\) once and uses,
in every \((h,\tau)\)-layer, a fresh arm lying in \(Q^+\) followed by the
\(Y\)-arm. It has length

\[
(a+1)b+(a+1)(c'+1)(b+d+1).
\]

Thus the exact one-sided whole-box portal saving is still only

\[
\boxed{(a+1)b.}
\tag{2.18}
\]

For equal side \(m\), the raster has length
\((m+1)^2(2m+1)\), covers all \((m+1)^4\) later-box targets plus
\(m(m+1)\) distinct earlier endpoint targets, and saves \(m(m+1)\)
against the displayed separate raster. It does not cover the remaining
points of \(Q^-\), and no arbitrary-pair optimality is asserted.

### 2.5 A complete adjacent-four-box double portal

Continue under the parameters of Theorem 2.2, in particular \(b,d\ge1\).
One can cover both boxes, rather than only \(Q^+\), by fusing the last
layer of \(Q^-\) to the first layer of \(Q^+\). For fixed \(h\), put

\[
L_z^{(h)}=(h,0,c,z)\quad(1\le z\le d),
\qquad A_h=(h,0,c,0),
\]

\[
X_u^{(h)}=(h,u,c,0)\quad(1\le u\le b),
\qquad R_z^{(h)}=(h,0,c+1,z)\quad(0\le z\le d).
\tag{2.19}
\]

Define the seam block

\[
\begin{split}
\mathcal S_h={}&
L_d^{(h)},L_{d-1}^{(h)},\ldots,L_1^{(h)},\\
&[A_h\ \text{if }A_h\ne0],\\
&X_1^{(h)},X_2^{(h)},\ldots,X_b^{(h)},
X_{b-1}^{(h)},\ldots,X_1^{(h)},\\
&R_0^{(h)},R_1^{(h)},\ldots,R_d^{(h)}.
\end{split}
\tag{2.20}
\]

The descending \(X\)-leg is empty when \(b=1\). The bracket omits exactly
the global zero, which occurs only when \(h=c=0\).

For every other fixed \((h,t)\)-layer of \(Q^-\), namely
\(0\le t<c\), use the ordinary rectangle block

\[
(h,b,t,0),\ldots,(h,1,t,0),\,
[(h,0,t,0)\ \text{if nonzero}],\,
(h,0,t,1),\ldots,(h,0,t,d).
\tag{2.21}
\]

For every higher \((h,c+1+\tau)\)-layer of \(Q^+\), where
\(1\le\tau\le c'\), use the same rectangle block translated to that
layer. Concatenate all ordinary blocks and all \(\mathcal S_h\) in any
order.

### Theorem 2.4 (complete double-portal raster)

The resulting word \(\mathcal D\) covers every nonzero point of
\(Q^-\cup Q^+\), has exact length

\[
\boxed{
|\mathcal D|
=(a+1)\bigl((c+c')(b+d+1)+2b+2d+1\bigr)-1,
}
\tag{2.22}
\]

and saves exactly \(a+1\) occurrences against the two separate ordinary
layer rasters.

#### Proof

An ordinary block (2.21) covers its entire nonzero rectangle layer:
for \(u,z\ge1\), start at \((h,u,t,0)\) on the decreasing \(u\)-arm and
end at \((h,0,t,z)\); targets on an axis are singletons, and the nonzero
base point is displayed when needed.

It remains to audit \(\mathcal S_h\). Every point
\((h,u,c,z)\) of the earlier boundary layer has one of the following
witnesses:

- if \(u=0,z>0\), the singleton \(L_z^{(h)}\);
- if \(u>0,z=0\), a displayed occurrence of \(X_u^{(h)}\), using the
  unique peak when \(u=b\);
- if \(u,z>0\), the interval from \(L_z^{(h)}\) through the decreasing
  \(L\)-arm, the optional base, and the increasing \(X\)-arm, ending at
  the first \(X_u^{(h)}\);
- if \(u=z=0\), the singleton \(A_h\), unless it is the excluded global
  zero.

Every point \((h,u,c+1,z)\) of the later bottom layer has witness

\[
[R_0^{(h)},\ldots,R_z^{(h)}]\qquad(u=0)
\tag{2.23}
\]

or

\[
[X_u^{(h)},X_{u-1}^{(h)},\ldots,X_1^{(h)},
R_0^{(h)},\ldots,R_z^{(h)}]\qquad(u\ge1),
\tag{2.24}
\]

where the occurrence of \(X_u^{(h)}\) is on the descending side of the
rainbow; for \(u=b\), it is the unique peak. The maxima in the four
earlier cases are exactly \((h,u,c,z)\), and those in
(2.23)--(2.24) are exactly \((h,u,c+1,z)\). Thus all seam intervals are
literal and uncontaminated.

Every ordinary layer has length \(b+d+1\), except that when \(c>0\) the
\((h,t)=(0,0)\) earlier block is shorter by one. There are \(c\)
ordinary earlier layers and \(c'\) ordinary later layers for each \(h\).
A seam block has length \(2b+2d+1\), except that when \(c=0,h=0\) its
global-zero occurrence is omitted. Exactly one of these two zero
exceptions occurs. Therefore the total length is (2.22).

The two separate layer rasters have combined length

\[
N_{\rm sep}=(a+1)(c+c'+2)(b+d+1)-1.
\tag{2.25}
\]

Since

\[
2(b+d+1)-(2b+2d+1)=1,
\]

each \(h\)-seam saves one occurrence, proving

\[
\boxed{N_{\rm sep}-|\mathcal D|=a+1.}
\tag{2.26}
\]

\(\square\)

For two equal side-\(m\) boxes, with \(m\ge1\),

\[
\boxed{
|\mathcal D|=4m^3+10m^2+7m,
\qquad
N_{\rm sep}=4m^3+10m^2+8m+1,
}
\tag{2.27}
\]

so the exact complete-pair raster saving is \(m+1\). This is a
whole-pair theorem, but its length is not near the sum of the two widths.

Here the **single-\(X\)-corridor model** fixes the displayed outer
\(L\)- and \(R\)-arm order, permits only letters
\(X_s^{(h)}\), \(1\le s\le b\), in the central corridor, and requires
the earlier and later mixed seam targets to use witnesses internal to this
one seam block. In that precisely scoped model, the saving is optimal.
Indeed the
central \(X\)-corridor must have prefix maxima \(1,\ldots,b\) for the
earlier layer and suffix maxima \(1,\ldots,b\) for the later layer. Choose
the first-attainment prefix representative and one suffix representative
for each level. There are \(b+b\) representatives. At most one physical
position can represent both systems. If its prefix and suffix levels are
\(u,v\), respectively, then the maximum over the entire corridor is
\(\max(u,v)=b\), so \(u=b\) or \(v=b\). There is only one chosen
prefix representative of level \(b\) and one chosen suffix representative
of level \(b\). Moreover the first prefix attainment of \(b\) contains an
actual level-\(b\) letter, so its suffix level is also \(b\). Hence an
overlap involving the prefix representative of level \(b\) must also use
the suffix representative of level \(b\). If instead the first overlap has
\(v=b\) and \(u<b\), then the unique suffix representative of level \(b\)
has already been used. Any second overlap would therefore have to use the
prefix representative of level \(b\); but that position has suffix level
\(b\), so it could overlap only the already-used suffix representative of
level \(b\), a contradiction. Thus in either branch no second overlap is
possible.
Hence the corridor has at least \(2b-1\) occurrences. The rainbow in
(2.20) attains that bound, so no layer-separated single-\(X\)-corridor
seam can save more than one occurrence per \(h\). This optimality is
strictly scoped: the two outer arms are fixed and nonlocal cross-layer
interleaving is excluded.

### 2.6 A volume-order alternating portal braid

The layer raster is not the best complete construction. A different
orientation of the alternating slice word shares an entire transverse arm
system across the geometric seam.

Assume now \(c,c'\ge1\), retain \(b,d\ge1\), and put

\[
C_\ast=c+c'+1.
\tag{2.28}
\]

In three local coordinates define

\[
\mathsf X_s=(s,0,0),\qquad
\mathsf Y_j=(0,j,0),\qquad
\mathsf Z_k=(0,0,k),
\]

\[
M_q(\mathsf Q)=
\mathsf Q_1,\ldots,\mathsf Q_q,
\mathsf Q_{q-1},\ldots,\mathsf Q_1.
\tag{2.29}
\]

The descending leg is empty for \(q=1\). Construct
\(\mathcal A_{b;d,C_\ast}\) as follows:

1. start with
   \(\mathsf Y_d,\mathsf Y_{d-1},\ldots,\mathsf Y_1\);
2. for \(s=1,\ldots,b\), append
   \(M_{C_\ast}(\mathsf Z),\mathsf X_s\) when \(s\) is odd and append
   \(M_d(\mathsf Y),\mathsf X_s\) when \(s\) is even;
3. finish with \(\mathsf Y_1,\ldots,\mathsf Y_d\) when \(b\) is odd,
   and with \(\mathsf Z_1,\ldots,\mathsf Z_{C_\ast}\) when \(b\) is
   even.

For \(0\le h\le a\), embed a local letter by

\[
\iota_h(x,y,z)=(h,x,z,y).
\tag{2.30}
\]

Thus the local sliced coordinate is the second box coordinate, while the
two arm coordinates are the fourth coordinate and the full joined third
coordinate \(0,\ldots,C_\ast\). Every embedded letter lies in
\(Q^-\cup Q^+\). Concatenate the \(a+1\) embedded words and add the
singleton

\[
O_h=(h,0,0,0)
\]

for each \(1\le h\le a\). Call the result \(\mathcal V\).

### Theorem 2.5 (volume alternating portal)

The word \(\mathcal V\) covers every nonzero point of
\(Q^-\cup Q^+\), and

\[
\boxed{
|\mathcal V|
=(a+1)(b+1)(d+c+c'+1)+a.
}
\tag{2.31}
\]

#### Proof: literal intervals

Fix \(h\). For local sliced coordinate \(s=0\), the virtual seam between
the initial decreasing \(\mathsf Y\)-arm and the first increasing
\(\mathsf Z\)-arm gives every nonzero target \((0,y,z)\). For
\(y,z\ge1\), use

\[
[\mathsf Y_y,\mathsf Y_{y-1},\ldots,\mathsf Y_1,
\mathsf Z_1,\ldots,\mathsf Z_z].
\]

An axis target uses the corresponding singleton or one-sided interval.

For \(1\le s\le b\), the hub \(\mathsf X_s\) has one adjacent
\(\mathsf Y\)-half-arm and one adjacent \(\mathsf Z\)-half-arm. If \(s\)
is odd and \(y,z\ge1\), use

\[
[\mathsf Z_z,\mathsf Z_{z-1},\ldots,\mathsf Z_1,
\mathsf X_s,\mathsf Y_1,\ldots,\mathsf Y_y].
\]

Here the \(\mathsf Z_z\) occurrence is on the descending side of its
mountain. If \(s\) is even, use

\[
[\mathsf Y_y,\mathsf Y_{y-1},\ldots,\mathsf Y_1,
\mathsf X_s,\mathsf Z_1,\ldots,\mathsf Z_z].
\]

Either interval has maximum exactly

\[
(s,y,z).
\tag{2.32}
\]

If exactly one of \(y,z\) vanishes, omit that absent arm and take the
one-sided interval between the remaining arm level and the hub, in the
parity-dictated order. If both vanish, use the hub singleton.
After applying \(\iota_h\), this maximum is

\[
(h,s,z,y).
\]

When \(z\le c\), it is a target of \(Q^-\); when
\(c+1\le z\le C_\ast\), it is a target of \(Q^+\). In the latter case
the witness literally uses the arm system based in \(Q^-\) together with
a \(\mathsf Z_z\)-letter in \(Q^+\). The only local target omitted by
\(\mathcal A\) is \((0,0,0)\). It is the excluded global zero for
\(h=0\), and is supplied by \(O_h\) for \(h\ge1\).

It remains to count. If \(b=2q\), the word length is

\[
d+q(2C_\ast)+q(2d)+C_\ast
=(b+1)(d+C_\ast).
\]

If \(b=2q+1\), it is

\[
d+(q+1)(2C_\ast)+q(2d)+d
=(b+1)(d+C_\ast).
\]

There are \(a+1\) fibers and \(a\) added nonzero origins, proving
(2.31). \(\square\)

#### Exact comparison and balanced sector

Apply the same alternating construction separately to \(Q^-\) and
\(Q^+\), using the same sliced-coordinate orientation. The first word
has length

\[
N^-=(a+1)(b+1)(d+c)+a,
\]

and the translated second word has length

\[
N^+=(a+1)(b+1)(d+c')+(a+1).
\]

The extra terms insert precisely the local origins which are nonzero in
the ambient boxes. Hence

\[
\boxed{
N^-+N^+-|\mathcal V|
=(a+1)\bigl((b+1)(d-1)+1\bigr).
}
\tag{2.33}
\]

For

\[
a=b=c=c'=d=m\ge1,
\]

this gives the exact identities

\[
\boxed{
|\mathcal V|=3m^3+7m^2+6m+1,
}
\tag{2.34}
\]

\[
\boxed{
N^-+N^+=4m^3+8m^2+6m+1,
\qquad
N^-+N^+-|\mathcal V|=m^2(m+1).
}
\tag{2.35}
\]

The exact width of one equal four-chain box is

\[
\begin{split}
w_4(m,m,m,m)
&=\binom{2m+3}{3}-4\binom{m+2}{3}\\
&=\frac{2m^3+6m^2+7m+3}{3}.
\end{split}
\tag{2.36}
\]

Consequently

\[
|\mathcal V|-2w_4(m,m,m,m)
=\frac{5m^3+9m^2+4m-3}{3},
\tag{2.37}
\]

and

\[
\frac{|\mathcal V|}{2w_4(m,m,m,m)}\longrightarrow\frac94.
\tag{2.38}
\]

Thus the portal saves a genuine volume-order number of occurrences
against separate explicit words, but it is not a near-sum-width
construction. Its mechanism is rank-staggered: later-box targets borrow
arms based at third-coordinate level \(0\). It does not transfer to
aligned SCD product boxes without a new volume-order endpoint-sharing
device. Permuting the three non-\(h\) coordinate roles gives analogous
sector bounds and permits the best sliced-coordinate orientation.

There is also a sharp architecture-level stopping point. Consider the
class with the \(b+1\) canonical sliced-coordinate vertices on a path,
one whole \(d\)-arm and one whole \(C_\ast\)-arm incident to each vertex,
and at most one merge of two facing equal-coordinate whole arms in each
of the \(b\) internal gaps. Arm interiors are otherwise private, and
fragmented or nonlocal identifications are excluded. Before gluing, the
arm incidence is \((b+1)(d+C_\ast)\). A shared height-\(q\) rainbow needs
at least \(2q-1\) record letters and therefore saves at most one
occurrence per gap, at most \(b\) total; the \(b\) positive hubs cost
exactly \(b\) occurrences. Hence every word in this class has length at
least

\[
\boxed{(b+1)(d+C_\ast),}
\tag{2.39}
\]

and \(\mathcal A_{b;d,C_\ast}\) attains equality. Any improvement on
(2.31) within this fixed orientation must therefore leave the stated
class, for example by using fragmented arms, multiple carriers, or
nonlocal sharing across the \(h\)-fibers. One should first minimize over
the available coordinate orientations. This is a scoped optimality
statement only.

---

## 3. Exact balanced outer-hook seam atlas

The preceding mechanism also occurs inside one exact four-chain factor.
This version is aligned with the outer-hook drain, but its adjacent
children are three-chain subposets; they must not be called independent
four-dimensional product boxes.

Fix \(m\ge1\) and use the alternating outer-hook drain of \([0,m]^4\). At stage
\(k=0,\ldots,m-1\), put \(n=m-k\). The residual box is

\[
[k,m]\times[0,n]\times[k,m]\times[0,n].
\tag{3.1}
\]

Peel coordinates \(3,4\), then coordinates \(1,2\). The adjacent emitted
children have dimensions

\[
E_k\cong[0,n]\times[0,n]\times[0,2n],
\]

\[
O_k\cong[0,n-1]\times[0,n-1]\times[0,2n].
\tag{3.2}
\]

Define

\[
A_u^{(k)}=(k,u,k,0),\qquad1\le u\le n,
\]

\[
B_z^{(k)}=(k,0,k+1,z),\qquad0\le z\le n-1.
\tag{3.3}
\]

Here \(A_u^{(k)}\in E_k\) and \(B_z^{(k)}\in O_k\). Put

\[
\mathcal P_k=
A_n^{(k)},A_{n-1}^{(k)},\ldots,A_1^{(k)},
B_0^{(k)},B_1^{(k)},\ldots,B_{n-1}^{(k)}.
\tag{3.4}
\]

### Theorem 3.1 (balanced adjacent-child face portal)

For every

\[
0\le u\le n,\qquad0\le z\le n-1,
\]

the target

\[
T_{u,z}^{(k)}=(k,u,k+1,z)
\tag{3.5}
\]

has the literal witness

\[
[B_0^{(k)},\ldots,B_z^{(k)}]\qquad(u=0),
\tag{3.6}
\]

or

\[
[A_u^{(k)},\ldots,A_1^{(k)},
B_0^{(k)},\ldots,B_z^{(k)}]\qquad(u\ge1).
\tag{3.7}
\]

The maximum in either case is exactly \(T_{u,z}^{(k)}\).

#### Proof

The first coordinate is constantly \(k\). The \(A\)-suffix supplies
second-coordinate maximum \(u\); the \(B\)-prefix supplies third-coordinate
maximum \(k+1\) and fourth-coordinate maximum \(z\). No other coordinate
increases. \(\square\)

The would-be earlier endpoint

\[
A_0^{(k)}=(k,0,k,0)
\]

is dispensable because

\[
B_0^{(k)}=(k,0,k+1,0)\ge A_0^{(k)}.
\tag{3.8}
\]

Thus this is literal dominated-endpoint fusion, not equality of two
disjoint child points.

### 3.2 Global atlas and exact counts

Concatenate \(\mathcal P_0,\ldots,\mathcal P_{m-1}\). All letters are
distinct, because different blocks have different first coordinate \(k\).
The total length is

\[
\boxed{
2\sum_{n=1}^m n=m(m+1).
}
\tag{3.9}
\]

The number of distinct targets in (3.5) is

\[
\boxed{
\sum_{n=1}^m n(n+1)
=\frac{m(m+1)(m+2)}3.
}
\tag{3.10}
\]

Between successive blocks, the final and initial letters have maximum

\[
\max\bigl(
(k,0,k+1,n-1),
(k+1,n-1,k+1,0)
\bigr)
=(k+1,n-1,k+1,n-1).
\tag{3.11}
\]

Hence the concatenation also has \(m-1\) explicit two-letter seam
witnesses. They lie in the next even child and are distinct from all
targets in (3.5).

In addition, every \(A_u^{(k)}\) is a distinct earlier-child singleton
target. There are

\[
\sum_{n=1}^m n=\frac{m(m+1)}2
\]

of these, and none belongs to (3.5) or to the seam family (3.11).
Consequently the word certifies at least

\[
\frac{m(m+1)(m+2)}3+\frac{m(m+1)}2+(m-1)
\tag{3.12}
\]

distinct displayed targets. Formula (3.11) verifies that no separator is
required. This is a lower count of the explicitly catalogued witnesses,
not a claim that no other interval of the word certifies another target.

The exact pair widths are

\[
w(E_k)+w(O_k)=(n+1)^2+n^2=2n(n+1)+1,
\tag{3.13}
\]

and exact drain additivity gives

\[
\boxed{
w_4(m,m,m,m)
=\sum_{n=1}^m\bigl((n+1)^2+n^2\bigr)+1
=\frac{2m(m+1)(m+2)}3+m+1.
}
\tag{3.14}
\]

If \(Q\) denotes the target count (3.10), then

\[
w_4(m,m,m,m)=2Q+m+1.
\tag{3.15}
\]

The seam atlas handles essentially half a width's worth of displayed
target labels using only \(O(m^2)\) physical occurrences. The targets are
highly comparable, so this is not a width packing and not adjacent-packet
fusion.

### 3.3 A complete balanced adjacent-child braid

There is also a literal construction covering an entire consecutive
child pair. It gives genuine endpoint sharing, although its excess remains
quadratic.

Fix \(m\ge2\) and put

\[
Q_m=[0,m-1]^2\times[0,m]^2.
\tag{3.16}
\]

In the last two coordinates define

\[
o_a=(a,0)\quad(0\le a\le m),\qquad
u_b=(m,b)\quad(1\le b\le m),
\]

\[
i_a=(a,1)\quad(0\le a\le m-1),\qquad
v_b=(m-1,b)\quad(1\le b\le m),
\tag{3.17}
\]

so \(v_1=i_{m-1}\). The first two hooks of \([0,m]^2\) are the
coordinatewise chains

\[
H_0=(o_0<o_1<\cdots<o_m<u_1<\cdots<u_m),
\]

\[
H_1=(i_0<i_1<\cdots<i_{m-1}=v_1<v_2<\cdots<v_m).
\tag{3.18}
\]

Thus two consecutive outer-hook children are

\[
C_0=[0,m-1]^2\times H_0,\qquad
C_1=[0,m-1]^2\times H_1,
\tag{3.19}
\]

of abstract dimensions \((m-1,m-1,2m)\) and
\((m-1,m-1,2m-2)\).

The word “consecutive” uses a specified valid drain tie-breaking. After
emitting \(H_0\) by peeling labelled coordinates \(3,4\), all four
residual edge heights equal \(m-1\). Retaining coordinates \(3,4\) in
that tie emits \(H_1\) next.

Partition the short square into the symmetric chains

\[
D_t=((0,t),(1,t),\ldots,(m-1-t,t),
(m-1-t,t+1),\ldots,(m-1-t,m-1))
\tag{3.20}
\]

for \(0\le t\le m-1\), with the corner written only once. Write

\[
D_t=(d_{t,0}<d_{t,1}<\cdots<d_{t,L_t}),
\qquad L_t=2(m-1-t).
\tag{3.21}
\]

The chains \(D_t\) partition \([0,m-1]^2\), and

\[
\sum_{t=0}^{m-1}L_t=m(m-1).
\tag{3.22}
\]

For a short point \(d\) and a long point \(h\), write
\(\langle d,h\rangle\) for their point in \(Q_m\). Define the bipolar
long corridor

\[
\begin{split}
\mathcal K={}&
o_1,o_2,\ldots,o_m,\,
v_1,v_2,\ldots,v_m,\\
&v_{m-1},v_{m-2},\ldots,v_2,\,
o_{m-1},o_{m-2},\ldots,o_1 .
\end{split}
\tag{3.23}
\]

Descending ranges whose initial index is below their terminal index are
empty; in particular the \(v\)-descent is empty when \(m=2\). Thus the
corridor length is \(4m-3\). If \(0\le t\le m-2\), abbreviate
\(d_j=d_{t,j}\), \(L=L_t\), and define

\[
\begin{split}
\mathcal B_t={}&
\bigl[\langle d_0,o_0\rangle\ \text{if }t\ge1\bigr]\\
&\Vert\,
\langle d_L,o_0\rangle,\langle d_{L-1},o_0\rangle,
\ldots,\langle d_1,o_0\rangle\\
&\Vert\,\langle d_0,\mathcal K\rangle\\
&\Vert\,
\langle d_0,i_0\rangle,\langle d_1,i_0\rangle,
\ldots,\langle d_L,i_0\rangle .
\end{split}
\tag{3.24}
\]

Here \(\langle d_0,\mathcal K\rangle\) means that every letter of
\(\mathcal K\) is paired with \(d_0\). The omitted letter at \(t=0\)
would be the global zero.

For the terminal singleton chain \(D_{m-1}=\{d\}\), put

\[
\begin{split}
\mathcal B_{m-1}={}&
\langle d,o_0\rangle,\langle d,i_0\rangle,\,
\langle d,o_1\rangle,\ldots,\langle d,o_m\rangle,\\
&\langle d,v_2\rangle,\ldots,\langle d,v_m\rangle .
\end{split}
\tag{3.25}
\]

Finally concatenate

\[
\mathcal B=\mathcal B_0\Vert\mathcal B_1\Vert\cdots
\Vert\mathcal B_{m-1}.
\tag{3.26}
\]

### Theorem 3.2 (complete balanced pair braid)

The word \(\mathcal B\) covers every nonzero point of \(C_0\cup C_1\),
and

\[
\boxed{|\mathcal B|=6m^2-5m+1.}
\tag{3.27}
\]

#### Proof: literal witnesses

Fix a nonterminal block \(\mathcal B_t\) and suppress the index \(t\).
Subscripts \(\uparrow\) and \(\downarrow\) below distinguish the first
ascending and last descending occurrences in the corridor.

The \(C_0\) targets have the following witnesses.

- \(\langle d_i,o_0\rangle\) is its displayed singleton whenever it is
  nonzero.

- For \(1\le a\le m\) and \(i\ge1\), start at
  \(\langle d_i,o_0\rangle\) on the decreasing short arm and end at
  \(\langle d_0,o_a\rangle_\uparrow\). The short maximum is \(d_i\)
  and the long maximum is \(o_a\). For \(i=0\), use the corridor prefix
  from \(\langle d_0,o_1\rangle\) through
  \(\langle d_0,o_a\rangle_\uparrow\).

- For \(1\le b\le m\) and \(i\ge1\), use the same start and end at
  \(\langle d_0,v_b\rangle_\uparrow\). The corridor prefix has long
  maximum

  \[
  o_m\vee v_b=(m,b)=u_b.
  \tag{3.28}
  \]

  For \(i=0\), start at \(\langle d_0,o_1\rangle\).

The \(C_1\) targets have the following witnesses.

- Every \(\langle d_i,i_0\rangle\) is a displayed singleton.

- For \(1\le a\le m-1\), start at the last occurrence
  \(\langle d_0,o_a\rangle_\downarrow\) and end at
  \(\langle d_i,i_0\rangle\) on the final increasing short arm. The
  maximum is

  \[
  \langle d_i,o_a\vee i_0\rangle
  =\langle d_i,i_a\rangle.
  \tag{3.29}
  \]

- For \(2\le b<m\), start at
  \(\langle d_0,v_b\rangle_\downarrow\) and end at
  \(\langle d_i,i_0\rangle\). For \(b=m\), start at the peak
  \(\langle d_0,v_m\rangle\). All intervening long letters are at most
  \(v_b\), so the maximum is exactly \(\langle d_i,v_b\rangle\).
  The remaining point \(v_1=i_{m-1}\) was covered by (3.29).

Every listed interval stays inside one block. The decreasing first short
arm ensures that no short coordinate exceeds \(d_i\) in a \(C_0\)
witness, and the increasing last short arm ensures the same for a \(C_1\)
witness. Equations (3.28)--(3.29) show that the long-coordinate joins are
literal and uncontaminated.

For the terminal block, \(\langle d,o_0\rangle\),
\(\langle d,i_0\rangle\), every \(\langle d,o_a\rangle\), and every
\(\langle d,v_b\rangle\) with \(b\ge2\) are singletons. Moreover,

\[
\max[\langle d,i_0\rangle,\langle d,o_1\rangle,\ldots,
\langle d,o_a\rangle]=\langle d,i_a\rangle
\qquad(1\le a\le m-1),
\tag{3.30}
\]

\[
\max[\langle d,i_0\rangle,\langle d,o_1\rangle,\ldots,
\langle d,o_m\rangle]=\langle d,u_1\rangle,
\tag{3.31}
\]

and, for \(2\le b\le m\),

\[
\max[\langle d,o_m\rangle,\langle d,v_2\rangle,\ldots,
\langle d,v_b\rangle]=\langle d,u_b\rangle.
\tag{3.32}
\]

This exhausts both terminal fibers.

For the length, (3.24) gives

\[
|\mathcal B_t|
=2L_t+4m-2+\mathbf 1_{\{t\ge1\}}
\qquad(0\le t\le m-2),
\tag{3.33}
\]

whereas \(|\mathcal B_{m-1}|=2m+1\). Using (3.22),

\[
\begin{split}
|\mathcal B|
&=2m(m-1)+(m-1)(4m-2)+(m-2)+(2m+1)\\
&=6m^2-5m+1.
\end{split}
\tag{3.34}
\]

This proves the theorem. \(\square\)

#### Exact comparison ledger

For reference, when \(0\le A\le B\le C\) and \(B,C\ge1\), the explicit
alternating-slice word for
\([0,A]\times[0,B]\times[0,C]\) covers all nonzero local points in length

\[
(A+1)(B+C).
\tag{3.35}
\]

Here is the literal word. Put

\[
X_s=(s,0,0),\qquad Y_j=(0,j,0),\qquad Z_k=(0,0,k),
\]

and, for \(Q=Y\) or \(Z\), put

\[
M_h(Q)=Q_1,Q_2,\ldots,Q_h,Q_{h-1},\ldots,Q_1.
\]

The descending leg is empty when \(h=1\), and \(M_0(Q)\) is empty.
Start with \(Y_B,Y_{B-1},\ldots,Y_1\). For
\(s=1,\ldots,A\), append \(M_C(Z),X_s\) when \(s\) is odd and append
\(M_B(Y),X_s\) when \(s\) is even. Finish with
\(Y_1,\ldots,Y_B\) when \(A\) is odd and with
\(Z_1,\ldots,Z_C\) when \(A\) is even. For \(A=0\), use simply the
initial decreasing \(Y\)-arm followed by the increasing \(Z\)-arm.

The \(x=0\) slice uses the virtual seam between the initial decreasing
\(Y\)-arm and the first increasing \(Z\)-arm. Every positive hub \(X_s\)
has one adjacent \(Y\)-half-arm and one adjacent \(Z\)-half-arm; the
interval between levels \(y,z\) has maximum exactly \((s,y,z)\).
A two-sided arm of height \(h\) has length \(2h-1\). Directly grouping
successive odd-even appendages, including the two exterior half-arms,
gives \((A+1)(B+C)\), proving (3.35).

Applied separately to the two children in (3.19), these words have
lengths

\[
m((m-1)+2m)=3m^2-m
\]

and

\[
m((m-1)+(2m-2))=3m^2-3m.
\]

The second child's translated local origin is nonzero in \(Q_m\), so
including it costs one further occurrence. The exact separate
construction ledger is therefore

\[
N_{\mathrm{sep}}=6m^2-4m+1.
\tag{3.36}
\]

The complete pair braid saves exactly

\[
\boxed{N_{\mathrm{sep}}-|\mathcal B|=m.}
\tag{3.37}
\]

Both child widths equal \(m^2\), because their long sides are at least
the sum of their two short sides. Hence

\[
|\mathcal B|-w(C_0)-w(C_1)=4m^2-5m+1.
\tag{3.38}
\]

Thus (3.27) is a complete adjacent-child endpoint-sharing theorem but not
an \(o(m^2)\)-excess pair theorem. No unrestricted optimality is claimed.

For \(m=1\), the exceptional word

\[
\langle d,i_0\rangle,\langle d,o_1\rangle
\]

covers the pair: its singletons give \(i_0,o_1\), and their join is
\(u_1\). Formula (3.27) still gives the correct length \(2\).

### 3.4 A quadratic obstruction to short-chain-separated pair words

The preceding braid still treats each short symmetric chain \(D_t\) in
its own block. The following lower bound shows that no construction with
that separation can have \(o(m^2)\) excess, however its internal corridor
is redesigned.

### Proposition 3.3 (short-SCD-blocked pair no-go)

Let \(m\ge2\). Suppose

\[
\mathcal W=\mathcal W_0\Vert\cdots\Vert\mathcal W_{m-1},
\]

where every letter of \(\mathcal W_t\) lies in
\(D_t\times(H_0\cup H_1)\), and intervals internal to
\(\mathcal W_t\) cover every nonzero point of
\(D_t\times(H_0\cup H_1)\). Then

\[
\boxed{|\mathcal W|\ge3m^2-m.}
\tag{3.39}
\]

Consequently every such architecture has excess at least

\[
\boxed{|\mathcal W|-w(C_0)-w(C_1)\ge m^2-m.}
\tag{3.40}
\]

#### Proof

Fix \(t\), write \(D_t=(d_0<\cdots<d_L)\), and consider three disjoint
requirements.

First, for each \(1\le i\le L\), the target
\(\langle d_i,o_0\rangle\) forces a literal occurrence of that point.
Indeed every letter of its witness has long coordinate \(o_0\), and the
short coordinates lie on the chain \(D_t\); their maximum can equal
\(d_i\) only if \(d_i\) itself occurs. These give \(L\) positions.

Second, for each \(1\le a\le m\), the target
\(\langle d_0,o_a\rangle\) forces a literal occurrence of that point.
Its short coordinate is the minimum \(d_0\), its fourth coordinate is
zero, and the eligible long points form the chain
\(o_0<\cdots<o_m\). These give \(m\) further positions.

Third, for each \(1\le b\le m\), any witness for
\(\langle d_0,u_b\rangle\) contains a letter whose fourth coordinate is
exactly \(b\): a maximum equal to \(b\) cannot be attained otherwise.
The \(m\) values of \(b\) require \(m\) distinct positions, all disjoint
from the first two families because those have fourth coordinate zero.
Therefore

\[
|\mathcal W_t|\ge L_t+2m.
\]

Summing and using (3.22) gives

\[
|\mathcal W|\ge m(m-1)+2m^2=3m^2-m.
\]

Subtracting the exact pair width \(2m^2\) proves (3.40). \(\square\)

The scope is essential: (3.39) does not constrain words whose intervals
or letters share across different \(D_t\)-fibers. It proves precisely that
cross-\(D_t\) sharing is necessary for a subquadratic-excess construction.

---

## 4. The former adjacent-packet gate is false

Consider

\[
Q_t=[0,t]^3\times[0,4t],
\tag{4.1}
\]

with odd \(t\). Its exact outer-hook drain performs \(3t\) two-height peels
and then has one terminal child, so it has exactly \(3t+1\) children. Pair
them consecutively.

For pair \(r\), let \(h_r\) be the minimum length of one literal word
whose letters lie in the ambient parent \(Q_t\) and which covers the union
of its two translated child subposets, and put

\[
e_r=h_r-w(C_{2r})-w(C_{2r+1}).
\tag{4.2}
\]

The two child middle layers lie in the parent middle rank and form a
disjoint antichain, so \(e_r\ge0\).

### Theorem 4.1 (quadratic APF obstruction)

Some adjacent pair satisfies

\[
\boxed{
e_r\ge
\frac{2\left\lceil (t+1)^3/8\right\rceil}{3t+1}
=\left(\frac1{12}-o(1)\right)t^2.
}
\tag{4.3}
\]

#### Proof

Concatenate optimal pair words. Every target stays in one exact child
subposet, so the concatenation is a universal word for \(Q_t\). Exact drain
width additivity gives

\[
\sum_r e_r\ge g_4(t,t,t,4t)-w_4(t,t,t,4t).
\tag{4.4}
\]

Here \(w_4=(t+1)^3\). The flat four-box endpoint theorem gives

\[
g_4-w_4
\ge
\left\lceil
\frac{(t+1)^3(4t-3t)}{2\cdot4t}
\right\rceil
=\left\lceil\frac{(t+1)^3}{8}\right\rceil.
\tag{4.5}
\]

There are \((3t+1)/2\) pairs. Averaging (4.4)--(4.5) proves (4.3).
\(\square\)

Therefore no uniform statement assigning every consecutive drain pair a
word of length

\[
w(C_{2r})+w(C_{2r+1})+o(t^2)
\]

can hold. This kills the former APF gate, including arbitrary intervals
crossing the child boundary. It does not prohibit one global word with
intervals crossing many pair boundaries simultaneously.

---

## 5. Intrinsic endpoint demand of one four-box

The next theorem is the key local-to-global ledger. It remains valid when
the selected witness intervals leave their own box.

Let

\[
Q=Q(p,q,r,s),\qquad
P=p+q+r,\qquad
V=(p+1)(q+1)(r+1),
\]

with \(p,q,r\ge1\) and

\[
s\ge P.
\tag{5.1}
\]

Projection to the first three coordinates is injective on every
antichain, while rank \(P\) contains
\((x_1,x_2,x_3,P-x_1-x_2-x_3)\) for every short triple. Hence

\[
w(Q)=V.
\]

For

\[
0\le k\le\min(p,q,r),
\]

put

\[
\Xi_k=
(s-P+2k)V
+6\binom{k+2}{4}
-(4P+2)\binom{k+2}{3},
\tag{5.2}
\]

and define

\[
\boxed{
K_4(Q)=
\max_{0\le k\le\min(p,q,r)}
\max\left\{
0,\
\left\lceil\frac{\Xi_k}{s+2k}\right\rceil
\right\}.
}
\tag{5.3}
\]

Choose one ambient literal witness for every target in the rank band

\[
P-k,\ P-k+1,\ldots,s+k
\]

corresponding to a maximizing \(k\). Let \(L_Q,R_Q\) be the sets of
physical left and right endpoints used.

### Theorem 5.1 (intrinsic two-endpoint toll)

\[
\boxed{
(|L_Q|-V)+(|R_Q|-V)\ge K_4(Q).
}
\tag{5.4}
\]

#### Proof

Grouping chosen targets by common left endpoint gives a chain partition;
the same is true on the right. A left endpoint class and a right endpoint
class meet in at most one target: two targets in their intersection would
have chosen intervals with the same two physical endpoints and hence the
same maximum. Let the two chain counts be

\[
C_L=|L_Q|=V+\delta_L,\qquad
C_R=|R_Q|=V+\delta_R.
\]

Both deltas are nonnegative because the band contains a layer of size
\(V\). Put

\[
J=s-P+2k,\qquad
F=\binom{k+2}{3},\qquad
E=\binom{k+3}{4},\qquad
G=\binom{k+2}{4}.
\]

There are \(J+1\) layers. At shoulder depth \(j\), the missing corner has
\(\binom{j+2}{3}\) points. Since
\(k\le\min(p,q,r)\), no side truncates that corner. Therefore each
boundary layer has size

\[
B_0=V-F,
\]

and the total number of targets in the band is

\[
T=(J+1)V-2E.
\]

Here \(E=\sum_{j=1}^k\binom{j+2}{3}\).

Every vertical base column meets the band in one nonempty interval, so
the exact number of fourth-coordinate target-poset covers is

\[
A_v=T-V.
\]

Now fix either endpoint partition, with \(C\) chains, and let its layer
sizes be \(m_0,\ldots,m_J\). The sets of chains meeting consecutive layers
intersect in at least \(m_i+m_{i+1}-C\) members. A common chain contains
two comparable targets of consecutive ranks and hence uses their
target-poset cover. Summing over the \(J\) transitions, the partition uses
at least

\[
2T-2B_0-JC
\]

band covers.

Use the horizontal potential

\[
\phi(x_1,x_2,x_3,x_4)=x_1+x_2+x_3,\qquad0\le\phi\le P.
\]

The missing low corner has potential mass

\[
S=\sum_{x_1+x_2+x_3<k}(x_1+x_2+x_3)=3G.
\]

Indeed the triples of sum \(h\) contribute
\(h\binom{h+2}{2}=3\binom{h+2}{3}\). Reflection in the three short
coordinates sends the low corner to the complementary high corner and
sends \(\phi\) to \(P-\phi\). The bottom boundary omits that high corner,
whereas the top boundary omits the low corner. Hence their potential
imbalance is

\[
\Delta_\phi=PF-2S=PF-6G.
\]

Exactly \(B_0\) chains meet each boundary. Thus there are \(C-B_0\)
internal chain starts and \(C-B_0\) internal chain ends. Telescoping
\(\phi\) along the chains gives

\[
\sum_{\mathcal C}
\bigl(\phi(\max\mathcal C)-\phi(\min\mathcal C)\bigr)
\le\Delta_\phi+P(C-B_0).
\]

Every horizontal cover raises \(\phi\) by one, while a vertical cover
leaves it fixed. Rank skips only add nonnegative unused potential.
Consequently this partition uses at least

\[
Z(C)=
2T-2B_0-\Delta_\phi+PB_0-(J+P)C
\]

vertical covers. No vertical cover can occur in both endpoint partitions,
because its two endpoints would lie in one common left class and one
common right class. Therefore

\[
Z(C_L)+Z(C_R)\le A_v.
\]

Substitute \(C_L+C_R=2V+\delta_L+\delta_R\), the displayed formulas for
\(T,B_0,A_v,\Delta_\phi\), and \(J+P=s+2k\). After collecting terms,

\[
\begin{split}
(s+2k)(\delta_L+\delta_R)
&\ge JV-6E+4S+4(1-P)F\\
&=(s-P+2k)V+6G-(4P+2)F\\
&=\Xi_k.
\end{split}
\tag{5.5}
\]

Taking the positive part and the integer ceiling proves (5.4).
\(\square\)

All objects in this proof are target-poset chains and covers. No word
letter is assumed to lie in \(Q\), so ambient fusion does not invalidate
the bound.

### 5.2 Fixed-ray constant

On an integer sequence satisfying (5.1) for every sufficiently large
\(t\), with

\[
(p,q,r,s)=(at,bt,ct,dt)+o(t),
\qquad a,b,c>0,\qquad d\ge a+b+c,
\]

\[
\frac{K_4(Q)}{t^3}
\ge\lambda_4(a,b,c,d)-o(1),
\tag{5.6}
\]

where

\[
\boxed{
\lambda_4=
\max_{0\le x\le\min(a,b,c)}
\frac{
abc(d-a-b-c+2x)
-\frac23(a+b+c)x^3
+\frac14x^4
}{
d+2x
}>0.
}
\tag{5.7}
\]

To verify the asymptotic and its quantifiers, fix first
\(0\le x<\min(a,b,c)\) and take \(k=\lfloor xt\rfloor\). Then

\[
\Xi_k=
\left(
abc(d-a-b-c+2x)
-\frac23(a+b+c)x^3+\frac14x^4
\right)t^4+o(t^4),
\]

while \(s+2k=(d+2x)t+o(t)\). Apply (5.3), then let \(x\) approach a
boundary maximizer; continuity gives (5.6). If \(d>a+b+c\), \(x=0\)
already makes the quotient positive. If \(d=a+b+c\), its numerator is

\[
2abc\,x-\frac23(a+b+c)x^3+\frac14x^4,
\]

which is positive for every sufficiently small \(x>0\). This proves the
strict positivity in (5.7).

At the boundary \((a,b,c,d)=(1,1,1,3)\), the choice \(x=1/2\) gives

\[
\lambda_4\ge\frac{49}{256}.
\tag{5.8}
\]

Indeed the numerator in (5.7) is \(49/64\) and the denominator is \(4\).

---

## 6. Exact packet sharing theorem

Let \(B_1,\ldots,B_m\) be disjoint nondegenerate translated product boxes
whose chosen width layers consist of covered nonzero targets and lie in
one ambient rank. All-zero singleton factors may simply be discarded.
Write

\[
W_i=w(B_i),\qquad W=\sum_iW_i.
\]

Let an ambient literal word covering their union have length

\[
n=W+D.
\tag{6.1}
\]

For each box choose a target family with intrinsic endpoint demand

\[
(|L_i|-W_i)+(|R_i|-W_i)\ge K_i.
\tag{6.2}
\]

Define endpoint-box degrees

\[
d_L(s)=|\{i:s\in L_i\}|,\qquad
d_R(s)=|\{i:s\in R_i\}|.
\tag{6.3}
\]

### Theorem 6.1 (endpoint-sharing conservation law)

\[
\boxed{
\sum_s(d_L(s)-1)_+
+\sum_s(d_R(s)-1)_+
\ge\sum_iK_i-2D.
}
\tag{6.4}
\]

#### Proof

Summing (6.2),

\[
\sum_i(|L_i|+|R_i|)
\ge2W+\sum_iK_i.
\tag{6.5}
\]

On the other hand,

\[
\sum_i|L_i|
=\left|\bigcup_iL_i\right|
+\sum_s(d_L(s)-1)_+
\le n+\sum_s(d_L(s)-1)_+,
\]

and similarly on the right. Substitute \(n=W+D\) and compare with (6.5).
\(\square\)

For two boxes,

\[
\boxed{
|L_0\cap L_1|+|R_0\cap R_1|
\ge K_0+K_1-2D.
}
\tag{6.6}
\]

Every unit of intrinsic endpoint excess must therefore be paid either by
two units of physical length excess or by one same-side cross-box endpoint
coincidence.

### Corollary 6.2 (endpoint-support bound)

Suppose all shared left endpoints lie in \(\Sigma_L\) and all shared right
endpoints lie in \(\Sigma_R\). Then

\[
\boxed{
D\ge
\max\left\{
0,\
\left\lceil
\frac{K_0+K_1-|\Sigma_L|-|\Sigma_R|}{2}
\right\rceil
\right\}.
}
\tag{6.7}
\]

If one physical seam set \(\Sigma\) supports both types, replace the two
cardinalities by \(2|\Sigma|\).

For two aligned boxes of shape \((t,t,t,3t)\), equations (5.8) and (6.6)
show that a near-sum-width word must have

\[
\boxed{
|L_0\cap L_1|+|R_0\cap R_1|
\ge
\left(\frac{49}{128}-o(1)\right)t^3.
}
\tag{6.8}
\]

Thus an \(O(t^2)\)-site portal surface leaves

\[
D\ge\left(\frac{49}{256}-o(1)\right)t^3.
\tag{6.9}
\]

This is a sharp scale no-go on a fixed compact sector.
It does not rule out a full geometric face of a four-dimensional box:
such a face has \(\Theta(t^3)\) sites and is already a volume-order
endpoint resource.

### 6.3 Compatibility-graph sharpening

Let \(G\) be the bipartite cross-comparability graph between the two local
target families. A shared left endpoint gives a comparable target pair;
different shared left endpoints give a matching \(M_L\subseteq G\).
Shared right endpoints give a second matching \(M_R\). The matchings are
edge-disjoint: if one target pair shared both endpoints, the two selected
intervals and hence their maxima would be identical.

Let \(\nu_2(G)\) be the maximum number of edges in a bipartite subgraph of
maximum degree two, equivalently in a union of two edge-disjoint matchings.
Then

\[
\boxed{
D\ge
\max\left\{
0,\
\left\lceil
\frac{K_0+K_1-\nu_2(G)}2
\right\rceil
\right\}.
}
\tag{6.10}
\]

The same statement holds with \(G\) replaced by an architecture's allowed
endpoint-compatibility graph. In particular, distinct co-ranked targets
are incomparable, so co-ranked same-side endpoint identification saves
nothing.

---

## 7. The aligned middle queue

The width layers of the packet form an antichain of size \(W\). Select one
witness for each and order the witnesses by increasing left endpoint:

\[
I_i=[\ell_i,r_i],\qquad1\le i\le W.
\]

Both endpoint orders are strict and identical. Since \(n=W+D\),

\[
\ell_i=i+\alpha_i,\qquad
r_i=i+\beta_i,
\tag{7.1}
\]

where \(\alpha,\beta\) are nondecreasing in \([0,D]\) and
\(\beta_i\ge\alpha_i\).

Consequently:

1. no two middle witnesses, even from different boxes, share a left or
   right endpoint;
2. every middle witness has span at most \(D\);
3. the left- and right-endpoint sets satisfy

   \[
   |\{\ell_i\}\cap\{r_i\}|\ge W-D.
   \tag{7.2}
   \]

If \(r_i=\ell_j\), then \(i\le j\). The seam letter at that physical
position belongs to both intervals and is coordinatewise below both
targets:

\[
A_{r_i}\le T_i\wedge T_j.
\tag{7.3}
\]

Thus cross-side identifications form a forward partial matching in one
common queue order. At \(D=0\), every middle witness is a singleton. A
block-ordered two-box braid can share cross-side endpoints only from the
earlier box toward the later one; bidirectional seams require genuine
interleaving.

This explains the directionality of Lemma 2.1. The rank-staggered later
baseline dominates an earlier endpoint. Same-rank same-side identification
would violate incomparability.

---

## 8. Global consequence for four-block aggregation

Assume the four Boolean blocks have fixed positive-proportion sizes, and
write \(R\asymp\sqrt N\) for the chain-height scale. Then all product-box
middle layers are aligned. By the established Rayleigh-window box census,
a fixed positive fraction of boxes have heights in a sufficiently small
one-sided compact neighborhood of a closed-dominant profile such as
\((1,1,1,3)R\), contained in \(s\ge p+q+r\); on that family,
\(K_4\ge\kappa R^3\) for a fixed \(\kappa>0\). Equivalently one may center
at the strict profile \((1,1,1,3+\eta)R\).

Packet the boxes into bounded-size adjacent groups and concatenate the
resulting packet words. Here measure same-side sharing by the left side
of (6.4), namely by endpoint-site multiplicity beyond one. Suppose this
quantity is uniformly \(o(R^3)\) on every relevant packet containing at
least one obstructed box
(or, more generally, its total over those packets is
\(o(\#\text{packets}\,R^3)\)). In particular this holds if each packet has
size at most \(K\) and only a fixed number of \(O(R^2)\) portal surfaces.
Assume here that every repeated same-side endpoint lies on those modules.
If \(S\) is the disjoint union of their typed left- and right-endpoint
supports, then

\[
\sum_s(d_L(s)-1)_++\sum_s(d_R(s)-1)_+
\le (K-1)|S|=O(R^2).
\]

Then Theorem 6.1 forces \(\Omega(R^3)\) excess on every relevant packet,
or the corresponding aggregate lower bound under the total-support
hypothesis.

The compact window contains \(\Theta(W(N)/R^3)\) obstructed four-chain
boxes and hence \(\Theta(W(N)/R^3)\) relevant bounded-size packets.
Summation gives \(\Omega(W(N))\) global excess. Therefore:

\[
\boxed{
\text{fixed-size packets with only }o(R^3)\text{ typed endpoint support
cannot yield coefficient one.}
}
\tag{8.1}
\]

This is scoped to aligned fixed-four-block product boxes and bounded
packets. It does not exclude:

- volume-order endpoint interleaving inside packets;
- a full three-dimensional \(\Theta(R^3)\)-site geometric interface;
- packet size tending to infinity;
- endpoint sites of unbounded box degree;
- one global corridor shared across many packets;
- changing or abandoning the fixed four-block product decomposition.

---

## 9. Exact status

The positive adjacent-box atlas proves that literal endpoint substitution
works and gives its exact surface-order saving. The volume alternating
portal then covers both geometrically adjacent equal four-boxes and saves
\(m^2(m+1)\) occurrences against separate alternating words. This is
genuine volume-order sharing, but its length remains
\((9/4+o(1))\) times the sum of the individual widths and its mechanism
uses rank staggering.

The balanced drain atlas shows endpoint substitution inside one exact
four-chain factor, while the complete child-pair braid proves that the
mechanism extends to every nonzero target of a nontrivial balanced
adjacent drain pair. Its exact saving is only linear and its excess
remains quadratic. The short-SCD-blocked lower bound shows that eliminating
quadratic-order excess requires sharing across the short fibers. The
negative theorems explain why iterating only boundedly many
subvolume-endpoint-support modules inside bounded-size aligned packets
cannot close the global gap: closed-dominant boxes carry a volume-order
intrinsic endpoint toll.

The smallest surviving theorem for this route is therefore:

> **Volume endpoint braid — UNPROVED.** Construct one global word of length
> \(W(N)+o(W(N))\) in which the positive-density closed-dominant product
> boxes realize \(\Omega(W(N))\) total same-side endpoint sharing through
> volume-order interleaving or unbounded-degree global corridors, while
> retaining literal uncontaminated interval witnesses.

Within bounded-size packets, a fixed family of adjacent \(O(R^2)\)-site
portal modules supporting all same-side repetitions is rigorously
insufficient.

## 10. Audit and scope

- Every face-atlas witness is written explicitly in (2.3), (3.6), and
  (3.7); every complete-pair witness is listed in the proof of
  Theorem 3.2 and in (3.28)--(3.32).
- The complete adjacent-four-box raster witnesses are listed in the proof
  of Theorem 2.4, including (2.23)--(2.24), and the stronger
  volume-portal witnesses are written parity by parity in the proof of
  Theorem 2.5.
- The saving (2.11) is relative to the stated canonical separate
  catalogues; no unrestricted optimality is claimed.
- The volume saving (2.33) is relative to the two stated separate
  alternating words. The lower bound (2.39) is only for the explicitly
  defined adjacent-whole-arm path class.
- The geometric constructions in Section 2 are rank-staggered; none is
  asserted for aligned four-block SCD product boxes.
- The outer-hook children in Section 3 are three-chain subposets of one
  four-chain parent, not two independent four-dimensional boxes.
- The APF obstruction concerns the former pairwise exact-drain gate. It
  does not lower-bound a word crossing many child-pair boundaries.
- The endpoint toll uses arbitrary selected ambient witnesses and does not
  assume that word letters stay inside their local box.
- The surface no-go counts distinct same-side endpoint sites. High target
  capacity at one site does not help for two boxes because one site
  contributes only one unit to each endpoint-set intersection.
- No implication is made to labelled synchronization or MWB.
- No web search, finite search, computational search, or probabilistic
  experiment was used.

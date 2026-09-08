# A width-order construction for both outer tails

## 1. Tail problem

Let `k=2m`, split the ground set into two disjoint `m`-sets `P,Q`, and fix
an integer `0<=r<=m`.  We seek one OR word covering every nonempty mask `S`
with

\[
                         |S|\le r
 \quad\hbox{or}\quad
                         |S|\ge2m-r.                    \tag{1.1}
\]

The point is that the length can be controlled by the width
`binom(2m,r)`, rather than by the total number of masks in the tails.

## 2. Chain connectors

Take arbitrary symmetric-chain decompositions `C_P,C_Q` of the two
half-cubes.  If

\[
                 C=(C_a\subset C_{a+1}\subset\cdots
                         \subset C_{m-a})
\]

has minimum rank `a`, define its connector

\[
 \omega(C)=
 [C_a\text{ if }a>0],
 C_{a+1}-C_a,\ldots,C_{m-a}-C_{m-a-1},
 [P-C_{m-a}\text{ if }a>0].                           \tag{2.1}
\]

The ground set is changed from `P` to `Q` on the other side.  Prefix ORs
of `omega(C)` contain every nonempty member of `C`; suffix ORs contain every
nonempty member of the complement-dual chain `C^*`.

The number of chains of minimum rank `a` is

\[
 N_m(a)=\binom ma-\binom m{a-1},                       \tag{2.2}
\]

and their connector length is

\[
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+2,&a>0.
 \end{cases}                                          \tag{2.3}
\]

The number of half-cube chains whose minimum rank is at most `t` is

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \binom mt,&0\le t\le\lfloor m/2\rfloor,\\
 \binom m{\lfloor m/2\rfloor},&t>\lfloor m/2\rfloor.
 \end{cases}                                          \tag{2.4}
\]

## 3. Threshold Euler graph

Make a bipartite graph with the chains of `C_P` on the left and those of
`C_Q` on the right.  Join chains of minimum ranks `a,b` exactly when

\[
                              a+b\le r.                \tag{3.1}
\]

Replace each edge by both directed arcs.  The non-isolated part is connected
through the two chains of minimum rank zero, and every vertex has equal
indegree and outdegree.  It therefore has an Euler circuit.

Write the connector of each visited vertex.  At a left-to-right boundary

\[
                         \omega(C)\mid\omega(D),
\]

the crossing intervals cover the rectangle `C^* x D`; the reverse boundary
covers `D^* x C`.

### Theorem 1 (exact tail construction)

The resulting cyclic word covers every mask in (1.1).  After cutting and
duplicating one connector it has length at most

\[
 L(m,r)=
 2\sum_{a=0}^{\lfloor m/2\rfloor}
       N_m(a)w_m(a)C_m(r-a)+m.                         \tag{3.2}
\]

### Proof

Write a target as `S=X union Y`, with `X subset P`, `Y subset Q`.

For the lower tail, let `C` be the chain containing `P-X` and `D` the chain
containing `Y`.  Then `X in C^*`, `Y in D`, and

\[
 a(C)\le|X|,\qquad a(D)\le|Y|.
\]

Thus `a(C)+a(D)<=|S|<=r`, so the boundary `C to D` represents `S`.
If `X` or `Y` is empty, use only the corresponding canonical suffix or
prefix inside the connector; the relevant chain still occurs because it is
adjacent to the minimum-zero chain on the other side.

For the upper tail use the same chains.  Symmetry of a chain also gives

\[
 a(C)\le|P-X|,\qquad a(D)\le|Q-Y|.
\]

Hence

\[
 a(C)+a(D)\le2m-|S|\le r,
\]

and the same rectangle represents `S`.

A chain of minimum rank `a` has degree `C_m(r-a)`.  Summing its connector
length over both sides proves (3.2); duplicating the cut connector costs at
most `m`.  QED.

## 4. Moderate-deviation estimate

Put

\[
                         r=m-h,
 \qquad h=c\sqrt m,
\]

where

\[
                 c\longrightarrow\infty,
 \qquad c=o(m^{1/6}).                                  \tag{4.1}
\]

### Theorem 2

Uniformly in (4.1),

\[
 L(m,m-h)
   =O\!\left((1+c^2)\binom{2m}{m-h}
       +c e^{-2c^2}\binom{2m}{m}\right).              \tag{4.2}
\]

Consequently

\[
                         L(m,m-h)=o\binom{2m}{m}.       \tag{4.3}
\]

### Proof

From (2.2)--(2.3), for `0<=a<=m/2`,

\[
 N_m(a)w_m(a)
 \le {2(m-2a+2)^2\over m}\binom ma.                   \tag{4.4}
\]

First consider `a>=m/2-h`, where (2.4) equals
`binom(m,m-h-a)`.  Extend the nonnegative sum to all `a`.  Vandermonde's
identity and the hypergeometric variable

\[
 \Pr(A=a)={\binom ma\binom m{m-h-a}\over
                    \binom{2m}{m-h}}
\]

give

\[
 \mathbb E(m-2A)^2
   =h^2+4\operatorname{Var}(A)=O(h^2+m).               \tag{4.5}
\]

Equations (4.4)--(4.5) bound this part by the first term of (4.2).

For `a<m/2-h`, the degree in (2.4) saturates at the half-cube width.
The local central-binomial estimate, followed by a Gaussian-tail integral,
gives

\[
 \sum_{a<m/2-h}N_m(a)w_m(a)
       =O\!\left(c\,2^m e^{-2c^2}\right).             \tag{4.6}
\]

Multiplication by `binom(m,floor(m/2))=O(2^m/sqrt m)` gives the second term
of (4.2), with the harmless normalization absorbed into the constant.

Finally the local de Moivre--Laplace estimate yields

\[
 {\binom{2m}{m-h}\over\binom{2m}{m}}
       =\exp(-(1+o(1))c^2).                            \tag{4.7}
\]

Both terms in (4.2), divided by the middle width, tend to zero.  QED.

## 5. Consequence for the central-shadow programme

Literal tail repair required central shadow depth
`Theta(sqrt(m log m))`.  Theorem 2 replaces that requirement by

\[
                         H=\sqrt m\,\omega(1),          \tag{5.1}
\]

where the divergent factor may be arbitrarily slow (subject to (4.1)).
Indeed the threshold Euler word covers both outer tails in `o(W)` entries.

This does not remove the fixed-pair capacity barrier: one fixed coordinate
matching already fails when `H/sqrt(m)->infinity`.  It does, however, reduce
the depth demanded of the mixed-coordinate construction from
`sqrt(m log m)` to the sharp moderate-deviation scale (5.1).

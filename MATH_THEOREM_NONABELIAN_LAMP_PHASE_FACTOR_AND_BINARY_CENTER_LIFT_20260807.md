# A nonabelian lamp factor closes the equal-degree phase and center gates

**Date:** 2026-08-07  
**Method:** a semidirect binary lamp group and a codimension-two tail
subgroup  
**Status:** theorem.  For every odd role length \(w\ge5\), there is a finite
simple \(w\)-regular bipartite phase-role factor with noncommuting phase
monodromy, exact all-depth proper-chain pairing, disjoint first exchange
pairs, and literal rank-\((r-2)\) centers.  It uses only \(4w\) active
coordinate labels.  It does not yet group the roles into forward rectangle
blocks or make all role-owner stars globally disjoint.

## 1. The binary lamp group

Let

\[
 V=\left\{x\in\mathbb F_2^{\mathbb Z_w}:
                  \sum_{i\in\mathbb Z_w}x_i=0\right\},             \tag{1.1}
\]

and let \(\tau\) cyclically shift the coordinates.  Form

\[
                         \mathcal G=V\rtimes_\tau C_w              \tag{1.2}
\]

with multiplication

\[
                         (v,i)(v',j)=(v+\tau^iv',i+j).              \tag{1.3}
\]

Let \(e_i\) be the standard coordinate vectors and put

\[
                         u=e_0+e_1,
 \qquad                 a=(0,1),
 \qquad                 b=(u,1).                                  \tag{1.4}
\]

Both \(a\) and \(b\) have order \(w\).  Indeed,

\[
 b^w=\left(\sum_{i=0}^{w-1}\tau^iu,0\right)=(0,0),                \tag{1.5}
\]

while their projections to \(C_w\) have order \(w\).

Define the kernel elements

\[
 x_i=a^iba^{-i-1}=e_i+e_{i+1}.                                   \tag{1.6}
\]

Let

\[
 \mathcal H
   =\left\langle e_2+e_j:3\le j\le w-1\right\rangle
   \le V.                                                         \tag{1.7}
\]

The displayed generators are independent, so

\[
                         |\mathcal H|=2^{w-3},
 \qquad
                         [\mathcal G:\mathcal H]=4w.               \tag{1.8}
\]

Finally put

\[
                         c=a^2b^{-2}=x_1^{-1}x_0^{-1}=e_0+e_2.     \tag{1.9}
\]

For \(1\le s\le w-3\),

\[
 q_s:=a^2b^sa^{-s-2}
       =x_2x_3\cdots x_{s+1}
       =e_2+e_{s+2}\in\mathcal H.                                \tag{1.10}
\]

Neither \(c=e_0+e_2\) nor

\[
                         cba^{-1}=x_1^{-1}=e_1+e_2                 \tag{1.11}
\]

belongs to \(\mathcal H\).

## 2. The phase-role graph

Take two copies \(E_+,E_-\) of \(\mathcal G\), matched by the identity.
On \(E_+\), positive phase advance is left multiplication by \(a\); on
\(E_-\), negative phase advance is left multiplication by \(b\):

\[
                         P(g)=ag,
 \qquad                 N(g)=bg.                                  \tag{2.1}
\]

Thus positive roles are the right cosets \(\langle a\rangle g\), negative
roles the right cosets \(\langle b\rangle g\), and every role has \(w\)
phases.

### Lemma 2.1 (the role graph is simple)

The phase matching defines a simple \(w\)-regular bipartite graph on the two
role shores.

#### Proof

For \(0<t<w\),

\[
                         b^t=(e_0+e_t,t),
 \qquad                 a^t=(0,t),                                  \tag{2.2}
\]

so \(\langle a\rangle\cap\langle b\rangle=1\).  Two right cosets of these
subgroups therefore intersect in at most one group element.  Each phase atom
is one such intersection, giving a simple edge.  Every subgroup orbit has
size \(w\), giving degree \(w\). \(\square\)

The two phase rotations do not commute: their kernel commutator is nonzero.
Thus this factor lies strictly outside the commuting-monodromy obstruction.

## 3. Exact leaf labels

Let

\[
                         \Omega=\mathcal H\backslash\mathcal G             \tag{3.1}
\]

be the set of left \(\mathcal H\)-cosets, so \(|\Omega|=4w\).  Define

\[
 \alpha(g)=\mathcal Hg,
 \qquad
 \beta(g)=\mathcal Hcg.                                 \tag{3.2}
\]

For a positive role \(\langle a\rangle g\), use the cyclic leaf word

\[
                         F_+(g)=(\mathcal Ha^tg)_{t\in\mathbb Z_w}.    \tag{3.3}
\]

For the negative role \(\langle b\rangle g\), use

\[
                         F_-(g)=(\mathcal Hcb^tg)_{t\in\mathbb Z_w}.   \tag{3.4}
\]

Both words are simple.  For example,
\(\mathcal Ha^sg=\mathcal Ha^tg\) would put \(a^{t-s}\) in
\(\mathcal H\le V\), impossible unless \(s=t\); the negative case is the
same after observing the nonzero \(C_w\)-projection of a nontrivial power
of \(b\).

### Theorem 3.1 (all tail offsets agree, first pairs are disjoint)

For every phase atom \(g\) and every

\[
                         2\le t\le w-1,
\]

we have

\[
 \boxed{
                         \alpha(a^tg)=\beta(b^tg).}                 \tag{3.5}
\]

At offsets zero and one, the four labels

\[
                         \mathcal Hg,
                         \mathcal Hag,
                         \mathcal Hcg,
                         \mathcal Hcbg                                \tag{3.6}
\]

are pairwise distinct.

#### Proof

At \(t=2\), \(cb^2=a^2\).  For \(3\le t\le w-1\), put \(s=t-2\).
Equation (1.10) gives

\[
                         cb^t=a^2b^{t-2}=q_sa^t,
 \qquad                 q_s\in\mathcal H.                           \tag{3.7}
\]

Hence \(\mathcal Hcb^tg=\mathcal Ha^tg\), proving (3.5).

Within each pair in (3.6), distinctness follows from the nonzero cyclic
projection.  The cross-pair equalities at offset zero would require
\(c\in\mathcal H\).  The only cross-pair equality with equal cyclic
projection is

\[
                         \mathcal Hag=\mathcal Hcbg,
\]

which would require \(cba^{-1}\in\mathcal H\).  Both possibilities are
excluded by (1.9)--(1.11); the other cross pairs have different cyclic
projections. \(\square\)

Thus every matched role pair has the forced rank-two form: the two first
leaf pairs are disjoint, and the remaining \(w-2\) positions agree exactly.
In particular, the same construction works at every deadline \(D\le w\).

## 4. Literal center lift on the same \(4w\) coordinates

For a positive role through \(g\), regard the **set** underlying (3.3) as
\(F_+(g)\subset\Omega\), and similarly define \(F_-(g)\).  Theorem 3.1
gives

\[
 F_-(g)=F_+(g)
   -\{\mathcal Hg,\mathcal Hag\}
   +\{\mathcal Hcg,\mathcal Hcbg\}.                        \tag{4.1}
\]

Define active center parts by complementation inside \(\Omega\):

\[
 C_+(g)=\Omega-F_+(g),
 \qquad
 C_-(g)=\Omega-F_-(g).                               \tag{4.2}
\]

Then \(|C_+(g)|=|C_-(g)|=3w\) and

\[
 C_-(g)=C_+(g)
   -\{\mathcal Hcg,\mathcal Hcbg\}
   +\{\mathcal Hg,\mathcal Hag\}.                         \tag{4.3}
\]

### Theorem 4.1 (binary center and target realization)

Assume

\[
                         r-2\ge3w,
 \qquad                 r+w-2\le n.                 \tag{4.4}
\]

Choose a common filler set \(K\), disjoint from \(\Omega\), of size

\[
                         |K|=r-2-3w.                 \tag{4.5}
\]

Assign centers

\[
                         G_+(g)=K\cup C_+(g),
 \qquad                 G_-(g)=K\cup C_-(g).         \tag{4.6}
\]

Then every center has rank \(r-2\), every leaf word is disjoint from its
center, and for every phase \(g\) the positive and negative proper-target
chains agree at every depth \(2\le h\le w\).  Their two complete role-owner
stars are disjoint.

#### Proof

The cardinalities and disjointness follow from (4.2), (4.5), and the fact
that leaf words are the complementary \(w\)-sets in \(\Omega\).  Equation
(4.3) says the two centers are at distance two, exchanging exactly the two
first leaf pairs in (3.6).  Equation (3.5) says all later leaf coordinates
agree positionwise.  The forced transplant normal form therefore gives
proper-target equality at every depth.  Two rank-\((r-2)\) centers at
distance two have no common rank-\((r-1)\) superset, proving complete
role-owner-star disjointness. \(\square\)

For the application \(n=2r-1\) and \(w=d+O(1)=O(\sqrt r)\), both inequalities
in (4.4) hold for all sufficiently large \(r\).  The construction therefore
fits inside the original coordinate set with linear-in-\(w\), rather than
exponential, active support.

## 5. What this closes and what remains

The theorem supplies an exact positive answer to the post-obstruction
monodromy problem on the equal-degree role sector:

* the phase graph is simple and exactly regular;
* positive and transported negative rotations are noncommuting;
* every proper target is paired coherently at all depths;
* the exchanged first pairs integrate to binary rank-\((r-2)\) centers; and
* each matched role pair has disjoint complete owner stars.

It does **not** yet give an owner-disjoint family of whole forward
rectangles.  Different roles in the lamp factor may have overlapping owner
stars, and the positive/negative centers have not been grouped into the
common-core \(K_{q,q+1}\) blocks required by a rectangle.  Nor does it solve
the unequal-degree \((p+2,p)\) role sector of the two-size ledger.

The exact surviving construction is now narrower:

> extract from the lamp role factor a rectangle-grouped, globally
> owner-disjoint subfactor, and couple it to an unequal-degree nonabelian
> factor for the \(P_{p+1}-N_p\) sector.

There is no remaining leaf-tail, phase-monodromy, coordinate-count, or
binary-center obstruction on the equal-degree sector.

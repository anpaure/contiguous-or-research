# Higher-depth slab IDP and the literal face-image congruence

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, common-order
syndrome assumption, probabilistic rounding, or web input is used.

## 0. Result

The \(Q_{r+1}\) recoupling extends to every protected depth at the
direction-incidence level, but not to literal target faces.

### Normalized slab theorem

Let \(Q_{r+k}\) be a physical slab.  For every \(k\)-set \(I\) of its
directions, freezing \(I\) in all \(2^k\) orientations partitions the
slab into \(2^k\) parallel \(Q_r\) packets active on the complementary
\(r\)-set.  At depth \(q<r\), after division by

\[
                    2^kqg_r,\qquad g_r={2^r\over r}, \tag{0.1}
\]

the direction-incidence vectors of these resolutions are exactly the
bases of \(U_{r,r+k}\).  Bundles of slabs therefore have the integer
decomposition property in this normalized projection.

### Literal obstruction

For arbitrary diverse cycle orders and affine compiler conjugates, every
whole isometric \(Q_r\) packet satisfies:

1. every literal lower \(q\)-face occurs together with its antipodal
   face;
2. the same holds above the middle;
3. after identifying an empty lower \(q\)-face with the corresponding
   full upper \(q\)-face, the two incidence vectors are equal;
4. the number of occurrences with any fixed physical \(q\)-support is
   even; and
5. every active direction belongs to exactly \(qg_r\) depth-\(q\)
   occurrences.

These are exact lattice equalities for every packet and hence for every
Minkowski sum, of any size.  In particular, no slab bundle made from
whole isometric \(Q_r\) packets has an unscaled literal-face
hypersimplex.

At each depth separately the normalized direction projection can be
rounded with error \(O(qW/r)\).  Summing through \(H\) gives
\(O(WH^2/r)\), which is not \(o(W)\) in the central regime.  The literal
face error is not controlled by this projection and may be larger.

Thus the slab mechanism closes a normal quotient but exposes a genuine
higher-depth congruence/common-flag obstruction.  A coefficient-one lift
requires target-labelled trades inside that congruence lattice, not
another marginal IDP argument.

## 1. Literal faces of an orientation cube

Fix a physical \(Q_r\) packet with direction set \(A\).  A return-free
depth-\(q\) window uses a \(q\)-set \(J\subset A\).  The orientations on
\(A\setminus J\) are fixed throughout the window; write them as

\[
                              y\in\mathbb F_2^{A\setminus J}.       \tag{1.1}
\]

The lower target has both endpoints absent on the pairs in \(J\) and
orientation \(y\) outside \(J\).  The upper target has both endpoints
present on \(J\) and the same outside orientation \(y\).  Denote these
literal face images by

\[
                         F^-_{J,y},\qquad F^+_{J,y}. \tag{1.2}
\]

Thus the natural sign identification is

\[
                         F^-_{J,y}\longleftrightarrow F^+_{J,y}.   \tag{1.3}
\]

The target identities also include every exterior status coordinate of
the product cell; those coordinates are fixed and are suppressed in the
notation.

## 2. Antipodal pairing

### Lemma 2.1 (packet face-pair identity)

Let one factor cycle have length \(2r\), and let \(q<r\).  If
\(F^\sigma_{J,y}\) occurs from one cyclic start, then
\(F^\sigma_{J,\bar y}\) occurs from the antipodal start \(r\) steps
later, for both signs \(\sigma\in\{-,+\}\).

Consequently, for the incidence vector \(x^\sigma_q\) of the whole
packet,

\[
 x^\sigma_q(J,y)=x^\sigma_q(J,\bar y),               \tag{2.1}
\]

and, under (1.3),

\[
                              x^-_q=x^+_q.            \tag{2.2}
\]

#### Proof

An isometric \(C_{2r}\) has direction word \(\pi\pi\), with
\(\pi\) a permutation of its \(r\) directions.  Starts separated by
\(r\) therefore use the same ordered \(q\)-window.  Their owner vertices
are antipodal in \(Q_r\), so every unused orientation is complemented.
This proves (2.1).

For one fixed start, the intersection and union use the same support
\(J\) and the same untouched orientations \(y\); only the empty/full
status on \(J\) changes.  This proves (2.2). \(\square\)

There are no fixed points in (2.1) because \(q<r\), so every orbit has
size two.

### Corollary 2.2 (support parity)

For every physical \(q\)-set \(J\subset A\),

\[
              \sum_yx^\sigma_q(J,y)\equiv0\pmod2.   \tag{2.3}
\]

This parity is independent of the direction order on every cycle.

## 3. Exact direction degree

### Lemma 3.1 (depth-\(q\) direction regularity)

In one \(Q_r\) packet, every active direction belongs to exactly

\[
                              qg_r=q{2^r\over r}      \tag{3.1}
\]

depth-\(q\) occurrences.  Inactive directions belong to none.

#### Proof

On one \(C_{2r}\), a fixed direction occurs twice in the cyclic word.
Each occurrence belongs to exactly \(q\) cyclic windows of length \(q\);
the two start sets are disjoint because \(q<r\).  Hence the direction
belongs to \(2q\) windows on one cycle.  The packet factor has
\(2^r/(2r)\) cycles, giving

\[
                       2q\,{2^r\over2r}=qg_r.
\]

No relation between the direction orders of different cycles or packets
is used. \(\square\)

If \(c_q(J)=\sum_yx_q(J,y)/2\) counts antipodal face pairs, then (3.1)
is equivalently

\[
                    \sum_{J\ni i}c_q(J)
                         ={qg_r\over2}               \tag{3.2}
\]

for every active \(i\), with the evident factor two restored if literal
faces rather than pairs are counted.

## 4. The \(Q_{r+k}\) slab resolution

Let \(R\) have size \(r+k\).  For a \(k\)-set \(I\subset R\), freeze
the coordinates in \(I\) in all \(2^k\) orientations.  This gives the
resolution

\[
 \mathcal R_I
   =\{Q_{R\setminus I}\times\{z\}:z\in\mathbb F_2^I\}.             \tag{4.1}
\]

It consists of \(2^k\) disjoint \(Q_r\) packets and partitions
\(Q_R\) exactly.  Every packet may use an independent direction order
and affine compiler conjugate.

By Lemma 3.1, its depth-\(q\) direction-incidence vector is

\[
                 d_{I,q}=2^kqg_r\,\mathbf1_{R\setminus I}.         \tag{4.2}
\]

Thus

\[
 \left\{{d_{I,q}\over2^kqg_r}:I\in\tbinom Rk\right\}
        =\{\mathbf1_A:A\in\tbinom Rr\},              \tag{4.3}
\]

the bases of \(U_{r,r+k}\).

## 5. Integer decomposition in the normalized projection

### Theorem 5.1 (slab-bundle IDP)

For \(K\) disjoint \(Q_{r+k}\) slabs with the same labelled carrier
\(R\), the normalized aggregate direction vectors are exactly

\[
 \boxed{
 \left\{u\in\mathbb Z^R:
      0\le u_i\le K,\qquad
      \sum_{i\in R}u_i=Kr\right\}.}                  \tag{5.1}
\]

#### Proof

Every choice of \(K\) resolutions is a sum of \(K\) \(r\)-set
indicators, so it lies in (5.1).

Conversely, take \(u\) in (5.1).  Construct a bipartite graph with
\(K\) left vertices, each required to have degree \(r\), and right
degrees \(u_i\).  The Gale--Ryser inequalities hold: for \(s\le K\),

\[
 sr\le\sum_{i\in R}\min(u_i,s),                      \tag{5.2}
\]

because the right side, subject to \(0\le u_i\le K\) and total \(Kr\),
is minimized by concentrating the mass on \(r\) coordinates, where it
equals \(sr\).  Hence a simple bipartite graph with those degrees exists.
The neighbor set of each left vertex is an \(r\)-set resolution, and the
sum of their indicators is \(u\). \(\square\)

This proves normality after division by the scale in (4.2).  It says
nothing yet about which literal faces the independently ordered compilers
select.

## 6. Failure of literal M-convex exchange

Quotient literal faces only by the forced antipodal pairing (2.1).  One
packet option is then a \(0/1\) vector on face-pair coordinates
\((J,[y])\).

Take two options with different \(q\)-support counts.  Removing one
selected face pair of support \(J\) and inserting one of support \(K\)
changes the direction-degree vector by

\[
                              \mathbf1_K-\mathbf1_J. \tag{6.1}
\]

Every legal option with the same active set has the fixed degree vector
(3.2).  Hence a unit symmetric exchange is legal only if
\(\mathbf1_J=\mathbf1_K\), that is, \(J=K\).  In particular every legal
unit exchange preserves the entire support-count profile
\((\sum_{[y]}x(J,[y]))_J\).

An \(M\)-convex set is connected by its symmetric unit exchanges:
repeatedly applying the exchange axiom decreases the
\(\ell^1\)-distance between any two of its points.  Therefore, if the
option library contains two different support-count profiles, it cannot
be \(M\)-convex.  If every option has the same profile, there is no
support transport at all.  Either way, Theorem 5.1 does not lift by the
unit-exchange argument used for polymatroid bases.

Nontrivial support motion requires a balanced multi-support trade in the
integer kernel of the point-versus-\(q\)-set incidence matrix.

The smallest possible support changes are symmetric exchanges such as

\[
             e_J+e_K-e_{J-a+b}-e_{K-b+a},            \tag{6.2}
\]

not single-coordinate moves.  Realizing (6.2) by legal diverse-order
cycle factors, with literal orientations and common all-depth labels,
is a new trade theorem not contained in the slab IDP.

## 7. Common-depth flag constraint

For a fixed start, the supports

\[
            J_1\subset J_2\subset\cdots\subset J_H   \tag{7.1}
\]

are prefixes of one ordered return-free window.  Include the untouched
orientations and write \(\mathcal F_H\) for the set of literal signed
\(H\)-flags.  Every option determines one incidence vector

\[
                              z_H\in\mathbb Z^{\mathcal F_H}.       \tag{7.2}
\]

The depth-\(q\) face vector is a fixed linear truncation

\[
                              x_q=P_qz_H.             \tag{7.3}
\]

Thus the feasible all-depth image is contained in

\[
 \{(x_1,\ldots,x_H):
          \exists z_H,\ x_q=P_qz_H\ \text{for all }q\}.             \tag{7.4}
\]

Taking separate IDP decompositions in (5.1) for different \(q\)'s does
not ensure (7.4).  The same statement holds jointly for the lower and
upper vectors, which are coupled by (2.2).

## 8. Quantitative rounding boundary

For \(k=1\), the normalized resolution polytope is
\(\Delta(r,r+1)\).  As in the depth-one slab theorem, rounding one
fractional resolution changes its normalized direction vector by at most
two in \(\ell^1\).  Restoring the depth-\(q\) scale \(2qg_r\), the cost
per slab is at most \(4qg_r\).

There are \(W_0/2^{r+1}\) slabs, so the depth-\(q\) direction error is at
most

\[
              {W_0\over2^{r+1}}\,4q{2^r\over r}
                         ={2qW_0\over r}.            \tag{8.1}
\]

Summing through \(H\) gives

\[
              \sum_{q=1}^H{2qW_0\over r}
                   ={W_0H(H+1)\over r}.              \tag{8.2}
\]

In the central regime \(H/\sqrt m\to\infty\) and \(r=o(m)\), (8.2) is
not \(o(W)\).  Using a larger frozen dimension \(k\) does not improve the
scale: it increases both the slab size and the direction atom by the
same factor \(2^k\), while the nearest-base error can only grow.

Equations (2.1)--(2.3), (3.2), and (7.4) show why the literal problem is
strictly harder than (8.1): face orientations, antipodal pairing,
support-degree balance, both signs, and all nested depths must be rounded
together.

## 9. Audited conclusion

Proved:

* an exact \(Q_{r+k}\) owner recoupling with arbitrary diverse packet
  orders;
* a normal uniform-matroid direction projection at every depth;
* exact antipodal, parity, direction-degree, sign-coupling, and common
  flag constraints for literal face images; and
* the quantitative \(WH^2/r\) failure of separate direction rounding.

Not proved:

* normality of the literal antipodal face-pair semigroup;
* legal realization of the support exchanges (6.2);
* a common all-depth integer decomposition; or
* \(o(W)\) literal discrepancy.

Hence the higher-depth slab bundle does not close coefficient one.  It
reduces the next positive theorem to a target-labelled realization and
packing of balanced support exchanges inside the common flag lattice.

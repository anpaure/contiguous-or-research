# Odd-slot adjacent necklaces: every unique-zero shell vertex can be matched

**Date:** 2026-08-05  
**Method:** a disjoint-pair parity involution followed by an injective
two-zero boundary map; no computation  
**Status:** unconditional.  It saturates the entire unique-zero stratum of
every boundary shell.  The remaining matching problem is confined to the
multi-zero core after deleting the explicitly consumed two-zero vertices.

## 1. Unique rooting

Let `q=2h+1` be odd, with `h>=1`, and let

\[
 \partial\mathcal N_{q,s}
 =\{[x_0,\ldots,x_{q-1}]:x_i\ge0,\ \sum_i x_i=s,\ \min_i x_i=0\}.
\]

A necklace with exactly one zero has a unique representative

\[
                         [0,a_1,a_2,\ldots,a_{2h}],
 \qquad a_i\ge1.                                      \tag{1.1}
\]

The zero is a literal root: no nontrivial rotation of (1.1) starts with a
zero.  We may therefore perform rooted operations on the ordered positive
coordinates without a canonical-representative ambiguity.

Put

\[
                         u_j=a_{2j-1}-1,
 \qquad v_j=a_{2j}-1,
 \qquad 1\le j\le h.                                 \tag{1.2}
\]

## 2. The parity involution

Call pair `j` quiet when

\[
                         u_j\equiv0\pmod2,
 \qquad v_j=0.                                        \tag{2.1}
\]

For a unique-zero vertex having a nonquiet pair, let `j` be its first
nonquiet pair and make the following adjacent transfer.

* If `u_j` is odd, move one unit from coordinate `2j-1` to coordinate
  `2j`.
* If `u_j` is even and `v_j>0`, move one unit from coordinate `2j` to
  coordinate `2j-1`.

### Lemma 2.1

This rule is a fixed-point-free involution on the unique-zero vertices
having at least one nonquiet pair, and every matched pair is an edge of
`G_(q,s)`.

#### Proof

In the first case, `u_j>=1`; after the transfer the pair becomes

\[
                         (u_j-1,v_j+1),
\]

whose first coordinate is even and whose second is positive.  The second
branch therefore reverses the move.  In the second case the new pair is

\[
                         (u_j+1,v_j-1),
\]

whose first coordinate is odd, so the first branch reverses the move.

Every earlier pair remains quiet, so the selected index stays `j` in both
directions.  The donor coordinate has value at least two before either
move, hence all `a_i` remain positive and the rooted zero remains unique.
The two changed coordinates are consecutive, so this is a legal adjacent
unit transfer.  `square`

The vertices not covered by Lemma 2.1 are exactly

\[
 R(z_1,\ldots,z_h)
 =[0,2z_1+1,1,2z_2+1,1,\ldots,2z_h+1,1],
 \qquad z_j\ge0.                                      \tag{2.2}
\]

In particular this residual exists only when `s` is even, and then

\[
                         \sum_j z_j={s\over2}-h.       \tag{2.3}
\]

## 3. Injecting the residual into the two-zero core

For a residual vertex (2.2), move the unique unit in coordinate `2` into
coordinate `1`.  This gives

\[
 F(z_1,\ldots,z_h)
 =[0,2z_1+2,0,2z_2+1,1,\ldots,2z_h+1,1].             \tag{3.1}
\]

### Lemma 3.1

The map `F` is injective on necklace classes, and

\[
                         R(z)\sim F(z)                \tag{3.2}

is one adjacent-transfer edge.  Every image has exactly two zero
coordinates.

#### Proof

Equation (3.2) is the displayed transfer from coordinate `2` to coordinate
`1`.  All omitted entries in (3.1) are positive, so the image has zeros
exactly at positions `0` and `2`.

For `q>=5`, rooting (3.1) at its other zero puts the second zero at position
`q-2`, not at position `2`.  Since odd `q` is never four, this rotated word
cannot have form (3.1).  Thus equality of two image necklaces must preserve
the displayed root, after which every `z_j` is read directly from the
coordinates.  For `q=3` there is only one variable and its value is fixed
by the total mass `s`, so injectivity is immediate.  `square`

The images of `F` were not touched by Lemma 2.1 because that involution was
confined to the unique-zero stratum.

## 4. Saturation theorem

### Theorem 4.1

For every odd `q>=3` and every `s`, the boundary graph
`\partial\mathcal N_{q,s}` has a matching which saturates every vertex having exactly
one zero coordinate.

The matching consists of:

1. all involution edges from Lemma 2.1;
2. all residual-to-core edges `R(z)F(z)` from Lemma 3.1.

It additionally consumes the explicitly described, pairwise distinct
two-zero vertices (3.1), and no other multi-zero vertex.

#### Proof

Lemma 2.1 matches all nonresidual unique-zero vertices internally.  The
remaining unique-zero vertices are precisely (2.2).  Lemma 3.1 matches
each of them to a distinct, previously unused two-zero vertex.  The two
edge families are vertex-disjoint and together saturate the unique-zero
stratum.  `square`

## 5. Exact reduced core

Let

\[
 \mathcal K_{q,s}
 =\{[x]\in\partial\mathcal N_{q,s}:x\text{ has at least two zeros}\}
   \setminus F(\mathbb Z_{\ge0}^h).                  \tag{5.1}
\]

Theorem 4.1 gives the exact implication

\[
 \operatorname{def}(\partial\mathcal N_{q,s})
 \le \operatorname{def}(G[\mathcal K_{q,s}]).        \tag{5.2}
\]

For `q=3` and `s>=1` this reduction is already exact and complete.  The multi-zero
stratum consists only of the concentrated necklace `[0,0,s]`.  When `s` is
even it is the unique image `F(s/2-1)` and is consumed; when `s` is odd the
residual family (2.2) is empty and the concentrated necklace remains as
the sole monomer.  Hence the construction itself proves

\[
 \operatorname{def}(\partial\mathcal N_{3,s})
 =s\pmod2,                                           \tag{5.3}
\]

with the right side interpreted as `0` or `1`.  This recovers the matching
part of the three-slot shell theorem directly.  The mass-zero terminal
shell is the separate singleton degeneracy.

The same reduction holds with protected sockets, provided any socket used
by (2.1) or (3.1) is first excluded and its finite local orbit is handled
as a boundary state.

There is one especially useful compatibility with the radial square.  For
`q>=5` and `s>=q`, its two inner-facing shell sockets are

\[
\begin{aligned}
 A_s&=[0,1^{q-2},s-q+2],\\
 B_s&=[0,1^{q-3},2,s-q+1].
\end{aligned}                                         \tag{5.4}
\]

All pairs before the last pair in (1.2) are quiet on `A_s`; the last pair
has `u_h=0` and `v_h=s-q+1>0`.  The parity involution therefore selects
exactly

\[
                         A_sB_s.                       \tag{5.5}
\]

The radial outer-facing sockets `C_s,D_s` have respectively `q-1` and
`q-2` zero coordinates.  For `q>=5` neither is an image (3.1), whose
members have exactly two zeros.  Consequently the unique-zero matching can
be chosen so that:

1. `A_sB_s` is one explicit matching edge;
2. deleting that edge exposes both radial inner-facing sockets and changes
   nothing else;
3. both radial outer-facing sockets remain entirely inside the reduced
   multi-zero core.

Moreover `C_sD_s` is itself an adjacent-transfer edge, disjoint from the
unique-zero matching and from `A_sB_s`.  We may add it immediately.  Hence
there is a shell matching containing **both** protected radial edges and
saturating:

* every unique-zero vertex;
* both vertices `C_s,D_s`;
* the explicit two-zero receiver family `F(z)`.

The unsaturated induced core is exactly (5.1) with `C_s,D_s` additionally
deleted.  If that residual core has a perfect or parity-optimal matching,
the whole shell inherits one while retaining both protected edges.  Across
two consecutive shells, the alternating four-cycle switch

\[
 \{A_sB_s,C_{s-q}D_{s-q}\}
 \longleftrightarrow
 \{A_sC_{s-q},B_sD_{s-q}\}                           \tag{5.6}
\]

preserves saturation exactly.

This does not yet give the one-monomer states required for full radial
flexibility, but it gives the exact two-port switch used by a cycle splice
or a paired radial attachment.

This is the first dimension-lowering step in the radial-shell programme:
an obstruction cannot be supported on the open facet (exactly one zero).
It must live in the codimension-at-least-two core, after removal of one
explicit parity-compressed image family.

## 6. Scope

Proved:

1. a literal adjacent-transfer involution on all nonresidual unique-zero
   necklaces;
2. an injective one-edge absorption of every residual unique-zero necklace
   into a two-zero necklace;
3. complete saturation of the unique-zero stratum for every odd `q`.

Not proved:

1. a near-perfect matching of the reduced multi-zero core (5.1);
2. radial four-socket flexibility of the whole boundary shell;
3. simultaneous PBBS marked-port/q2-halo placement;
4. the full adjacent-necklace theorem or `nu(k)<=B(k)+O(1)`.

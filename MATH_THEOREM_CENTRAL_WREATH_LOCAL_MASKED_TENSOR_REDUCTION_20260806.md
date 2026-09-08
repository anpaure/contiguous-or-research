# Central wreath factors are globally resident and expose the masked tensor locally

## Status

The Mütze--Standke--Wiechert central wreath factor already partitions the
two middle Boolean layers exactly.  Every one of its components has a
cyclic coordinate-order normal form.  This note proves two facts which are
useful for the new masked-`C6` programme.

1. Every wreath component has an explicit depth-`(h-1)` antecedent and is
   automatically biresident for every `h<=q-1`.
2. Every cut of that antecedent exposes the complete local masked tensor:
   its left and right cumulative profiles have one common `s=q-h` core and
   independent ordered prefix banks.

Consequently the exact owner/root ring-resolution problem would be
unnecessary if a component-spanning family of wreath pulls met the displayed
three-cut alignment condition.  The later audit
`MATH_THEOREM_MSW_WREATH_STANDARD_PULL_COLLAR_AND_QUOTIENT_NOGO_20260806.md`
proves that the published standard pull does **not** provide this: it acts
on a different factor, is binary (`2+1`) at component level, and the native
MSW factor contains no same-phase directed common-core `C6`.  Thus the
alignment remains a genuinely new construction, not an imported theorem.
Nor does an arbitrary central wreath factor have the required
immediate-upper palette: that is exactly the pointed-wreath lower-turn (or
AGCF) gate.

No computation or search is used.

## 1. One central wreath and its source antecedent

Put

\[
             N=2q-1,
 \qquad 2\le h\le q-1,
 \qquad s=q-h.                                        \tag{1.1}
\]

Let

\[
                   w=(w_0,w_1,\ldots,w_{N-1})          \tag{1.2}
\]

be a cyclic ordering of the coordinates.  After choosing an orientation
and phase, the owner and root rows of its middle-level lift may be written

\[
 \begin{aligned}
 O_i&=\{w_i,w_{i+1},\ldots,w_{i+q-1}\},\\
 Q_i&=O_i\cap O_{i+1}
     =\{w_{i+1},\ldots,w_{i+q-1}\}.                  \tag{1.3}
 \end{aligned}
\]

All indices are cyclic modulo `N`.  Define source letters

\[
                   A_i=\{w_i,w_{i+1},\ldots,w_{i+s}\}. \tag{1.4}
\]

### Theorem 1.1 (literal wreath antecedent)

The word (1.4) satisfies

\[
                   D^{h-1}A=O,
 \qquad             D^{h-2}A=(Q_{i-1})_i.             \tag{1.5}
\]

Every coordinate has one owner run of length `q` and one owner gap of
length `q-1`.  In particular the component is positively and negatively
resident at deadline `h-1`.

#### Proof

The union of the `h` consecutive `(s+1)`-windows
`A_i,...,A_(i+h-1)` is the coordinate interval

\[
             \{w_i,\ldots,w_{i+s+h-1}\}
             =\{w_i,\ldots,w_{i+q-1}\}=O_i.
\]

Using `h-1` source windows gives the `(q-1)`-interval ending one coordinate
earlier, which is the displayed root row after a phase shift.  A coordinate
belongs to exactly `q` consecutive `q`-windows among the `N` cyclic starts;
the complementary block has length `N-q=q-1`.  Both are at least `h`,
proving residence. \(\square\)

### Corollary 1.2 (the central one-copy shores are already solved)

The Mütze--Standke--Wiechert factor partitions the rank-`(q-1)` shore into
central wreaths.  The bipartite lift of every odd wreath cycle contains
each of its rank-`(q-1)` intervals and the complementary rank-`q`
intervals once.  Hence its lifted cycles partition both root and owner
shores, and Theorem 1.1 supplies a resident source antecedent on every
component.

This statement concerns the owner/root factor only.  It does not assert
that consecutive owner unions cover rank `q+1`.

## 2. Every cut is a full local masked tensor

Open (1.4) between positions `0` and `1`.  For positive `i,j`, define the
left and right cumulative source profiles

\[
 \begin{aligned}
 L_i&=A_{1-i}\cup\cdots\cup A_0,\\
 R_j&=A_1\cup\cdots\cup A_j.                          \tag{2.1}
 \end{aligned}
\]

As long as the displayed coordinate intervals do not wrap around each
other,

\[
 \begin{aligned}
 L_i&=\{w_{1-i},\ldots,w_s\},\\
 R_j&=\{w_1,\ldots,w_{s+j}\}.                         \tag{2.2}
 \end{aligned}
\]

Put

\[
 K=\{w_1,\ldots,w_s\},\quad
 \lambda_a=w_{1-a},\quad
 \rho_b=w_{s+b}.                                      \tag{2.3}
\]

### Theorem 2.1 (local tensor normal form)

For every admissible `i,j`,

\[
 \begin{aligned}
 L_i&=K\cup\{\lambda_1,\ldots,\lambda_i\},\\
 R_j&=K\cup\{\rho_1,\ldots,\rho_j\},\\
 L_i\cap R_j&=K,\\
 |L_i\cup R_j|&=s+i+j.                                \tag{2.4}
 \end{aligned}

Thus a globally core-free central wreath has, at every cut, exactly the
same cumulative-profile tensor as a masked ring with local core `K`.

#### Proof

Equations (2.2)--(2.3) give the first two identities.  Their two exterior
coordinate intervals are disjoint and both are disjoint from `K`, proving
the intersection and rank assertions. \(\square\)

For the buffered value

\[
 t_0=\lceil\sqrt{3h-2}\rceil,
 \qquad P=h+t_0,                                      \tag{2.5}
\]

all pairs `1<=i,j<=P-1` are admissible whenever

\[
                         s+2P-2\le N.                  \tag{2.6}
\]

Condition (2.6) is the same eventual inequality
`q>=h+2t_0-1` used by the buffered masked collar.

## 3. Exact sufficient alignment for a masked wreath pull

Take three wreath cuts, indexed by `t in Z/3Z`.  Suppose their local data
can be labelled so that

\[
 \begin{aligned}
 K_t&=H\cup\{a_t\},\\
 (\lambda^t_1,\lambda^t_2,\ldots)
   &=(a_{t+1},\lambda_2,\lambda_3,\ldots),\\
 (\rho^t_1,\rho^t_2,\ldots)
   &=(\rho_1,\rho_2,\ldots),                          \tag{3.1}
 \end{aligned}
\]

where all displayed banks are disjoint in the usual masked-collar way.
Reconnect the left profile of cut `t` to the right profile of cut `t+1`.

### Theorem 3.1 (zero-current local wreath splice)

Under (3.1), every protected crossing value is transported pointwise:

\[
               L_i^t\cup R_j^{t+1}
                    =L_i^t\cup R_j^t                 \tag{3.2}
\]

for every displayed address `(i,j)`.  Hence roots, owners, immediate
uppers, and the buffered rows through source width `P` have zero signed
current.  The cyclic tail permutation merges the three input components
when the three cut edges lie in distinct components.

#### Proof

The left profile contains `H,a_t,a_(t+1)` and its common left-prefix bank.
The old right profile contains `H,a_t` and its right-prefix bank; the new
right profile contains `H,a_(t+1)` and the same right-prefix bank.  Taking
the union with the fixed left profile gives the same set.  The component
claim is the standard three-tail permutation. \(\square\)

Theorem 3.1 is a sufficient local dictionary, not an assertion about the
published pull catalogue.  A standard incidence hexagon fixes only the six
central ports.  It does not by itself force the `Theta(h)` neighbouring
coordinates in the three cyclic wreath orders to satisfy (3.1).

## 4. The remaining MSW-to-masked bridge

The exact bypass theorem one might hope for is:

> **Buffered coherent-wreath pull lemma.**  The central MSW wreath factor
> has a component-spanning hypertree of alternating incidence hexagons for
> which the three cyclic coordinate orders satisfy (3.1) through depth
> `P`, with disjoint or regenerating collars and legal final capped ages.

If this lemma held, Corollary 1.2 would supply the exact owner/root factor
and Theorem 3.1 would supply its zero-charge resident component joins.  The
near-maximal necklace-ring resolution would then be unnecessary.  The
native/published-pull no-go cited above proves that this lemma cannot be
obtained by simply identifying the standard plane-tree pull catalogue with
the MSW wreath components.  A noncanonical wreath factor, an
exterior-moving zero-monodromy packet, or a different multirow transport is
required.

Two further gates remain even under that lemma.

1. An arbitrary MSW wreath factor need not have complete rank-`(q+1)`
   consecutive-owner unions.  Under the pointed-wreath dictionary this is
   the missing lower-turn rainbow, equivalently the AGCF decoration gate.
2. The depth-`(h-1)` antecedent must still carry every strict-lower target
   in one common-cap assignment.  The local tensor alone does not prove
   that compiler.

Thus the central wreath route is a genuine simplification of exact
owner/root selection, but it is not by itself a proof of `B(k)+O(1)`.

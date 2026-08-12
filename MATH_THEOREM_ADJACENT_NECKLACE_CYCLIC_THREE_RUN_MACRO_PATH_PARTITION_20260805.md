# Adjacent necklaces: a canonical unrooted three-run macro partition

**Date:** 2026-08-05  
**Method:** collapse maximal runs of gap-threes, then apply the odd-group
Cartesian-path quotient theorem; no computation  
**Status:** unconditional.  This removes the root-selector problem from the
all-one full-merge fibre.  Every cyclic gap composition belongs to one
canonical product-of-paths fibre.  The unmatched fibres are characterized
exactly by three residue classes modulo six.

## 1. Cyclic gap compositions

The all-one full-merge critical states are nonempty cut sets on an odd
`q`-cycle with cyclic gaps at least three.  Equivalently, they are cyclic
compositions

\[
                    g=(g_1,\ldots,g_k),
                    \qquad g_i\ge3,quad\sum_i g_i=q. \tag{1.1}
\]

Deleting a cut merges two neighboring gaps.  Inserting a cut splits one
gap into two parts at least three.  In particular,

\[
                     h+3\longleftrightarrow(3,h),
                     \qquad h\ge3,                  \tag{1.2}
\]

is one literal vertical exit toggle.

## 2. The unrooted macro normal form

Assume first that not every part of `g` equals three.  Decompose `g`
cyclically and uniquely into macroblocks

\[
                         3^{r_i},h_i,
                         \qquad r_i\ge0,quad h_i\ge4. \tag{2.1}
\]

That is, each non-three part terminates the maximal run of threes
immediately preceding it.  Collapse this macroblock to

\[
                              H_i=3r_i+h_i.          \tag{2.2}
\]

Denote the resulting cyclic composition by

\[
                              \mathcal M(g)=(H_1,\ldots,H_s). \tag{2.3}

Every `H_i` is at least four and their sum is `q`.

### Lemma 2.1 (canonical cyclic normal form)

The map `M` is well defined on unrooted cyclic compositions and commutes
with rotation.  Its fibres are disjoint and exhaustive away from the
all-three word.

#### Proof

Every non-three part is an intrinsic cyclic delimiter.  Assign to it the
unique maximal run of threes immediately before it.  These blocks are
disjoint and cover the cyclic word.  Changing the displayed starting point
only cyclically rotates the list of blocks.  Formula (2.2) therefore gives
an unrooted cyclic composition independent of all choices. \(\square\)

This is the cyclic replacement for the protected-root scan: no
lexicographic root or tie-break is required.

## 3. Exact path-product fibre

Fix a macro base

\[
                          H=(H_1,\ldots,H_s),
                          \qquad H_i\ge4.             \tag{3.1}
\]

For each part put

\[
                    L_i=\left\lfloor{H_i-4\over3}\right\rfloor. \tag{3.2}

Its possible expansions are

\[
                3^{r_i},\ H_i-3r_i,
                \qquad 0\le r_i\le L_i.             \tag{3.3}

The terminal part in (3.3) is always at least four.  Increasing or
decreasing `r_i` by one is exactly (1.2).

### Theorem 3.1 (literal macro fibre)

Before rotations, the fibre over `H` is exactly

\[
                         P_{L_1+1}\square\cdots\square P_{L_s+1}. \tag{3.4}

\]

If `A` is the rotational stabilizer of the cyclic macro base `H`, the
corresponding necklace fibre is exactly

\[
             (P_{L_1+1}\square\cdots\square P_{L_s+1})/A.       \tag{3.5}

\]

The group `A` has odd order.

#### Proof

Formula (3.3) gives all and only the preimages of each macro part, and the
choices are independent.  This proves (3.4).

If two expanded states are rotations, their canonical macro bases are the
same rotation by Lemma 2.1; hence the rotation lies in `A`.  Conversely
every element of `A` permutes equal macro factors and gives the quotient
identification (3.5).

If `A` has order `a`, the macro word is `a` repeats and therefore `a`
divides its total sum `q`.  Since `q` is odd, `a` is odd. \(\square\)

## 4. Attaching the all-three word

If every gap equals three, then `3|q`; write `q=3a`.  Since `q` is odd,
`a` is odd.  Attach this word to the single-part macro fibre `H=(q)`.

The ordinary expansions of `(q)` are

\[
              3^r,q-3r,
              \qquad0\le r\le a-2,                 \tag{4.1}

\]

ending at `3^(a-2),6`.  One final split `6 -> 3,3` gives the all-three
word.  Thus the enlarged single-part fibre is the path on

\[
                              a=q/3                 \tag{4.2}

\]

vertices.  It is odd.

This attachment is collision-free: the all-three word is the only cyclic
composition with no non-three delimiter.

## 5. Exact matching and critical residues

Apply the odd-group Cartesian-path quotient theorem to (3.5), choosing on
every odd local path the endpoint `r_i=0` as its critical endpoint.

### Theorem 5.1 (unrooted macro matching)

Every macro fibre is perfectly matched unless every local path order
`L_i+1` is odd.  In the exceptional case it has a matching missing exactly
the unexpanded macro necklace

\[
                              (H_1,\ldots,H_s).       \tag{5.1}

\]

For a macro part `H>=4`, its path order is odd exactly when

\[
                          H\equiv0,4,5\pmod6.        \tag{5.2}

\]

The enlarged all-three/single-part fibre is exceptional as well, and its
chosen monomer is the unexpanded one-part state `(q)` when

\[
                          q\equiv3\pmod6.            \tag{5.3}

\]

#### Proof

The path-product quotient theorem is perfect if one factor order is even
and has exactly the tensor of selected local endpoints as its sole critical
orbit otherwise.  This proves (5.1).

Write `H=3u+s`, `s in {0,1,2}`.  From (3.2),

\[
 L=
 \begin{cases}
 u-2,&s=0,\\
 u-1,&s=1,2.
 \end{cases}
\]

The order `L+1` is odd precisely for residues `0,4,5` modulo six.
Section 4 gives an odd path of order `q/3` for (5.3), and the endpoint
orientation leaves `(q)`. \(\square\)

Thus the complete first-stage critical family is

\[
 \mathcal R_q=
 \left\{
   [H_1,\ldots,H_s]:
   H_i\ge4,quad H_i\equiv0,4,5\pmod6,quad\sum H_i=q
 \right\},                                          \tag{5.4}

\]

together with the special one-part state `(q)` when `q=3 mod 6`.

## 6. The surviving five-skeleton is odd

### Corollary 6.1

Every critical macro necklace in (5.4) contains a positive odd number of
parts congruent to five modulo six.

#### Proof

Parts congruent to zero or four are even; parts congruent to five are odd.
Their total `q` is odd.  Hence the number of five-residue parts is odd and
nonzero. \(\square\)

This supplies an intrinsic odd cyclic skeleton inside every ordinary
critical state.  It is the natural root-free object for the next
hub-rainbow induction.

For `q=15`, the ordinary critical macro bases are

\[
 (5,5,5),\quad(4,5,6),\quad(4,6,5),\quad(4,11),\quad(5,10). \tag{6.1}

\]

and the special critical base is `(15)`.  Thus exactly six macro-fibre
monomers remain.  The earlier four-term list omitted the two distinct
orientations of the cyclic three-part multiset `{4,5,6}`; reversal is not
a necklace rotation.  The explicit `q=15` circulation closure uses a
different vertical matching and is not a census check for this matching.

## 7. Exact remaining theorem

The cyclic-root problem is closed.  What remains is now the following
strictly smaller statement.

> **Five-skeleton hub-rainbow theorem.**  Pair the critical macro necklaces
> in `R_q`, apart from at most one optional socket, by horizontal adjacent
> gap transfers whose deleted-cut hubs are distinct; or route them serially
> through the corresponding odd circulation blossoms.

The allowed critical-to-critical residue transitions include

\[
             05\leftrightarrow50,qquad
             45\leftrightarrow54,qquad
             55\leftrightarrow04                 \pmod6.               \tag{7.1}

\]

The first two move a five-marker; the third removes or creates a pair of
five-markers.  Since their number is always odd, these moves suggest a
same-parity strong induction on the odd five-skeleton size.

## 8. Scope

Proved:

1. a canonical, unrooted, rotation-equivariant macro normal form;
2. exact product-of-paths fibres modulo odd stabilizers;
3. a complete matching in every noncritical fibre;
4. the exact critical residue set `R_q`;
5. correct attachment of the all-three word; and
6. an intrinsic odd five-residue skeleton in every critical base.

Not proved:

1. the five-skeleton hub-rainbow theorem;
2. protected composition of its circulation interiors with earlier stages;
3. one optional prescribed radial socket; or
4. the complete adjacent-necklace theorem.

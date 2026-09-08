# Resolvable decompositions of a power-of-two cube into maximal isometric cycles

Date: 2026-07-26

Method: explicit finite-group and linear-algebra arguments only.

This note separates three assertions which are easy to conflate:

1. a cycle of length `2h` in `Q_h`;
2. an **isometric** cycle of length `2h`;
3. a resolvable edge decomposition of `Q_h` into such cycles.

For every power of two `h>=2`, assertion 3 is true.  The construction below
is self-contained.  It is a linear-syndrome construction, but its kernel is
generally **not** a binary Hamming code.  The earlier cycle-transversal
argument by itself supplies only one vertex partition, not an edge
decomposition.

Throughout, write

\[
 X=\mathbb F_2^h,
 \qquad Q_h=\operatorname{Cay}(X; e_1,\ldots,e_h).
\]

An edge retains its coordinate label even when two labels have the same
syndrome below.

## 1. Exact characterization of the isometric `2h`-cycles

Let a cycle `C` of length `2h` have cyclic transition-direction sequence

\[
 a_0,a_1,\ldots,a_{2h-1}\in[h].
\]

### Lemma 1.1

The cycle `C` is isometric in `Q_h` if and only if there is a permutation
`pi` of `[h]` for which its transition sequence is

\[
 \boxed{\pi_1,\ldots,\pi_h,\pi_1,\ldots,\pi_h.}       \tag{1.1}
\]

#### Proof

Suppose `C` is isometric.  The endpoints of every cyclic arc of length `h`
have distance `h` along `C`, and hence Hamming distance `h`.  A walk of
length `h` in a cube has endpoint distance `h` precisely when none of its
transition coordinates repeats.  Thus every cyclic block of `h`
consecutive transition directions is a permutation of `[h]`.

Compare the blocks

\[
 a_i,a_{i+1},\ldots,a_{i+h-1}
 \quad\hbox{and}\quad
 a_{i+1},\ldots,a_{i+h}.
\]

Both contain every direction once, so the direction removed from the first
must equal the direction inserted into the second:

\[
 a_{i+h}=a_i.
\]

This proves (1.1).

Conversely, in the doubled-permutation sequence (1.1), every cyclic block
of at most `h` consecutive directions has no repetition.  Therefore the
Hamming distance between the endpoints of such an arc equals its length.
Every two vertices of a `2h`-cycle have a shorter connecting arc of length
at most `h`, so all distances on `C` agree with the ambient cube distances.
Thus `C` is isometric.  QED.

In particular, the standard sequence

\[
 1,2,\ldots,h,1,2,\ldots,h                         \tag{1.2}
\]

is genuinely isometric, whereas an arbitrary cycle of length `2h` need not
be.

## 2. A syndrome transversal giving one resolution class

Let

\[
 h=2^r,\qquad r\ge1.
\]

Take an `r`-dimensional binary vector space `U`, choose a nonzero linear
functional

\[
 \lambda:U\longrightarrow\mathbb F_2,
\]

and put

\[
 \Sigma=U\oplus\langle v\rangle,
 \qquad \dim\Sigma=r+1.
\]

Choose a cyclic enumeration

\[
 u_0=0,u_1,\ldots,u_{h-1}
\]

of all elements of `U` which alternates the two `lambda`-classes:

\[
 \lambda(u_i)=i\pmod2.                              \tag{2.1}
\]

Here is a completely explicit choice.  Pick `z in U` with
`lambda(z)=1`, enumerate

\[
 \ker\lambda=\{a_0=0,a_1,\ldots,a_{h/2-1}\},
\]

and put

\[
 u_{2j}=a_j,\qquad u_{2j+1}=a_j+z
 \quad(0\le j<h/2).                                \tag{2.1a}
\]

This lists every element of `U` once.  Since `h` is even, the closing pair
`u_(h-1),u_0` also has opposite `lambda`-values.

Define a linear syndrome map

\[
 \phi:X\longrightarrow\Sigma                         \tag{2.2}
\]

by

\[
 \begin{aligned}
 g_i:=\phi(e_i)&=u_i+u_{i-1}, &&1\le i<h,\\
 g_h:=\phi(e_h)&=v+u_{h-1}.
 \end{aligned}                                      \tag{2.3}
\]

Let

\[
 p_i=e_1+\cdots+e_i\quad(0\le i\le h)
\]

and let `C_0` be the standard cycle (1.2), with vertex set

\[
 P=\{p_i:0\le i<h\}\mathbin{\dot\cup}
   \{\mathbf1+p_i:0\le i<h\}.                     \tag{2.4}
\]

Telescoping gives

\[
 \phi(p_i)=u_i\quad(0\le i<h),
 \qquad
 \phi(\mathbf1)=v,                                 \tag{2.5}
\]

and hence

\[
 \phi(\mathbf1+p_i)=v+u_i.                         \tag{2.6}
\]

Consequently `phi` maps `P` bijectively onto `Sigma`.  In particular `phi`
is surjective.  Put

\[
 K=\ker\phi,
 \qquad |K|=2^{h-r-1}=\frac{2^{h-1}}h.              \tag{2.7}
\]

Exactly as for any group transversal, the cycles

\[
 \mathcal R_0=\{C_0+k:k\in K\}                     \tag{2.8}
\]

have pairwise disjoint vertex sets and partition `X`: if `p+k=p'+k'`, then
applying `phi` first gives `p=p'` and then `k=k'`.  Thus (2.8) is one
resolution class.  Every member is isometric by Lemma 1.1.

## 3. The additional translates that decompose every edge

For `q in U`, choose any lift `x_q in X` satisfying

\[
 \phi(x_q)=q,
\]

and define

\[
 \mathcal R_q=\{C_0+x_q+k:k\in K\}.                 \tag{3.1}
\]

The choice of lift is immaterial, because two lifts differ by an element of
`K`.  Each `R_q` is a translate of `R_0`, hence is again a vertex partition
into isometric `2h`-cycles.

Set

\[
 T=\ker\lambda\subset U,
 \qquad |T|=h/2.                                    \tag{3.2}
\]

### Theorem 3.1

The family

\[
 \boxed{\{\mathcal R_q:q\in T\}}                   \tag{3.3}
\]

is a resolvable edge decomposition of `Q_h` into isometric cycles of length
`2h`.

#### Proof

It remains only to prove exact edge coverage.  We do this separately for
each coordinate direction.

For `i<h`, the two `i`-edges of the syndrome image of `C_0` are

\[
 \{u_{i-1},u_i\},
 \qquad
 \{v+u_{i-1},v+u_i\}.                              \tag{3.4}
\]

They are translates of one another by `v`.  For `i=h`, they are

\[
 \{u_{h-1},v\},
 \qquad
 \{v+u_{h-1},0\},                                  \tag{3.5}
\]

again translates by `v`.

Write `A_i` for the two-edge set in (3.4) or (3.5).  Translation by a
syndrome `q in U` changes it to `A_i+q`.  Its translation stabilizer in
`Sigma` is

\[
 \{0,v,g_i,v+g_i\}.                                 \tag{3.6}
\]

Indeed, an individual undirected edge with difference `g_i` has stabilizer
`{0,g_i}`, and the additional translation `v` interchanges the two edges.
All four elements in (3.6) are distinct: `g_i` is neither zero nor `v`, by
(2.1)--(2.3).

Intersecting (3.6) with `U` shows that for `q,q' in U`,

\[
 A_i+q=A_i+q'
 \quad\Longleftrightarrow\quad
 q'=q\ \hbox{ or }\ q'=q+\bar g_i,                 \tag{3.7}
\]

where

\[
 \bar g_i=
 \begin{cases}
 u_i+u_{i-1},&i<h,\\
 u_{h-1},&i=h.
 \end{cases}                                       \tag{3.8}
\]

Moreover, two translates of `A_i` cannot share just one edge: if one
constituent edge of `A_i+q` equals one constituent edge of `A_i+q'`, then
`q+q'` is one of the four translations in (3.6), and consequently the two
entire two-edge sets are equal.  Thus distinct sets in (3.7) are disjoint.

By the alternating choice (2.1),

\[
 \lambda(\bar g_i)=1\qquad(1\le i\le h).          \tag{3.9}
\]

Therefore `T=ker(lambda)` contains exactly one member of every pair
`{q,q+bar g_i}`.  It follows from (3.7) that, as `q` ranges over `T`, the
sets `A_i+q` are pairwise disjoint.

There are `h/2` of them and each has two syndrome edges, hence together they
contain `h` labelled `i`-edges.  This is every labelled `i`-edge on the
`2h` syndrome vertices.  Finally, every labelled syndrome edge has exactly
`|K|` coordinate-`i` edge lifts in `X`, and (3.1) contains all of those
lifts.  Thus the classes in (3.3) cover every coordinate-`i` edge of `Q_h`
exactly once.  This holds for every `i`, proving both edge-disjointness and
coverage.  QED.

The numerical ledger agrees:

\[
 \begin{aligned}
 \#\text{cycles per class}
   &=|K|=\frac{2^{h-1}}h,\\
 \#\text{classes}
   &=\frac h2,\\
 \#\text{cycles in all}
   &=2^{h-2},\\
 (2h)2^{h-2}
   &=h2^{h-1}=|E(Q_h)|.
 \end{aligned}                                      \tag{3.10}
\]

## 4. Exact audit of the terminology

1. **Vertex versus edge.**  Formula (2.8) alone is a partition of the
   vertices into cycles.  It uses only `2^h` of the `h2^(h-1)` cube edges,
   a fraction `2/h`.  The parity-selected translates (3.3) are the extra
   ingredient that proves an edge decomposition.

2. **Resolution.**  Under the standard meaning, every resolution class is
   a vertex partition.  Here there are exactly `h/2` such classes; not just
   one of them, but all of them partition `V(Q_h)`.

3. **Isometric versus merely long.**  Length `2h` alone is insufficient.
   Lemma 1.1 gives the exact condition: the transition word must be a
   permutation repeated in the same order.

4. **The role of a code.**  The kernel `K` is a binary linear code of
   codimension `r+1`, but it is generally not the standard Hamming or
   extended Hamming code.  When `h>=4`, the first `h-1` columns `g_i` all
   lie in the `h/2`-element affine hyperplane `lambda=1` of `U`, so two of
   them must repeat.  Their two coordinate unit vectors then sum to a
   weight-two word in `K`.  Calling
   Theorem 3.1 a "Hamming-code theorem" is therefore historically or
   terminologically misleading unless "code" is being used generically.
   The standard extended Hamming code is also unsuitable for the displayed
   transversal when `r>=2`, because it contains the all-one word, while
   (2.5) requires \(\phi(\mathbf1)=v\ne0\).

5. **Why powers of two occur.**  A vertex partition into `2h`-cycles
   requires

   \[
   2h\mid 2^h,
   \]

   so `h` must be a power of two.  Thus the hypothesis is not an artifact of
   this construction.  The exceptional value `h=1` has no cycle in the
   simple graph `Q_1`; the theorem begins at `h=2`.

This proves the claimed resolvable edge decomposition, with the stated
terminological corrections.

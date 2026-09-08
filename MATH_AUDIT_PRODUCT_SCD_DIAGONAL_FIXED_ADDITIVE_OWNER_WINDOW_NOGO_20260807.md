# Audit: long product-SCD diagonal runs are incompatible with a fixed-additive central row

**Date:** 2026-08-07  
**Primary theorem audited:**
`MATH_THEOREM_PRODUCT_SCD_DIAGONAL_ALL_DEPTH_STAR_FACTOR_20260806.md`  
**Method:** intersect all marked suffix constraints, then evaluate every
central-length window  
**Verdict:** the diagonal target factor, theta count, boundary tickets, and
static containing-owner paths are valid.  However, a marked diagonal run of
unbounded length cannot occur in a word of length (B(k)+C) for fixed
(C): its target equations force an internal central-length window to have
rank strictly below the middle rank.  The canonical owner lift is only a
static containment map and is not the derivative of the literal source row.

## 1. Diagonal targets

Use the notation of the primary theorem.  A diagonal source skeleton is

\[
                         B_i=C_i\cup K_{s-i},              \tag{1.1}
\]

and its marked suffix targets are

\[
 Z_{i,j}=C_i\cup K_{s-i+j-1},
 \qquad1\le j\le d.                                      \tag{1.2}
\]

Let a consecutive endpoint interval

\[
                         J=[L,U],\qquad \ell=U-L+1,        \tag{1.3}
\]

carry every target (1.2).  Let (A) be **any** source word realizing those
target values; (A) need not equal the skeleton (B).

The union of all marked intervals is

\[
                         G=[L-d+1,U].                      \tag{1.4}
\]

## 2. Exact forced envelope

### Lemma 2.1

For every (p\in G), every realizing word satisfies

\[
 A_p\subseteq H_p,
\]

where

\[
 H_p=
 \begin{cases}
 C_L\cup K_{s-p},&L-d+1\le p\le L,\\
 C_p\cup K_{s-p},&L\le p\le U.
 \end{cases}                                             \tag{2.1}
\]

#### Proof

Every marked interval containing (p) imposes containment of (A_p) in
its declared union.  For a fixed endpoint (i\ge p), the shortest marked
suffix containing (p) has length (j=i-p+1), and (1.2) gives

\[
                         Z_{i,i-p+1}=C_i\cup K_{s-p}.      \tag{2.2}
\]

If (p<L), intersect (2.2) over the available endpoints beginning at
(i=L); the (C_i)'s increase, so their intersection is (C_L), while
the (K)-part is fixed.  If (p\in J), the depth-one target at endpoint
(p) is already (C_p\cup K_{s-p}), and every other marked target through
(p) contains it.  This proves (2.1). \(\square\)

### Lemma 2.2 (window-rank cap)

Let ([r,r+h-1]\subseteq G) be a source interval which meets (J).  Then

\[
 \boxed{
   \left|\bigcup_{p=r}^{r+h-1}A_p\right|\le s+h-1.}       \tag{2.3}
\]

#### Proof

By Lemma 2.1, the largest (X)-shore set available in the interval is
(C_{r+h-1}), while the largest (Y)-shore set is the one at its leftmost
position, (K_{s-r}).  Hence

\[
 \bigcup_{p=r}^{r+h-1}A_p
   \subseteq C_{r+h-1}\cup K_{s-r},                       \tag{2.4}
\]

whose rank is

\[
                         (r+h-1)+(s-r)=s+h-1.             \tag{2.5}
\]

\(\square\)

## 3. Fixed-additive contradiction

In the top merged-PBBS parameters,

\[
                         s=m-2d.                           \tag{3.1}
\]

At physical length (B(k)+C), put (e=d+C).  The architecture-free
endpoint-interval lemma
(`MATH_THEOREM_ARCHITECTURE_FREE_ENDPOINT_CHAIN_UNIT_SLACK_20260803.md`,
Lemma 1.1) says that every interval of length (e+1) contains one of the
(W) selected rank-(m) witness intervals.  Its union therefore has rank
**at least** (m).  Here

\[
                         h=d+C+1                           \tag{3.2}
\]

(equivalently, depth (d+C)).

The forced band (G) has length

\[
                         |G|=d+\ell-1.                     \tag{3.3}
\]

If

\[
                         \ell\ge C+2,                      \tag{3.4}
\]

then (G) contains an interval of length (h=d+C+1).  Lemma 2.2 bounds
its union rank by

\[
 s+h-1=(m-2d)+(d+C+1)-1=m-d+C<m                         \tag{3.5}
\]

for every sufficiently large (d>C).  This contradicts the
architecture-free rank-(m) witness containment stated above.

### Theorem 3.1 (fixed-additive diagonal-run no-go)

For every fixed (C), and all sufficiently large dimensions, a word of
length (B(k)+C) cannot contain a product-SCD diagonal run with more than
(C+1) consecutive fully marked endpoints of depths (1,\ldots,d).

In particular, the primary theorem's counted runs of length
(rac15d-O(1)) cannot be placed in the direct PBBS/row-identity
architecture for any fixed additive constant.

## 4. Why the static owner lift does not answer the audit

The primary theorem defines the rank-(t=m-d) boundary ticket

\[
                         P_i=C_i\cup K_{t-i}               \tag{4.1}
\]

and the containing rank-(m) set

\[
                         \Omega_i=C_{i+d}\cup K_{t-i}.     \tag{4.2}
\]

Those sets do form a simple, doubly-rainbow Johnson path, and
(P_i\subseteq\Omega_i).  But the literal diagonal skeleton has

\[
 \bigcup_{p=i}^{i+d}B_p
   =C_{i+d}\cup K_{s-i},                                  \tag{4.3}
\]

which has rank (s+d=t), not (m), and is not (Omega_i).  More
strongly, Theorem 3.1 applies to every alternative source realization of
the same marked targets, not only to the skeleton (B).

Thus (4.2) proves static containment capacity, not the PBBS derivative or
maximal-envelope condition.

## 5. Proof-safe scope after correction

Still proved by the primary theorem:

* the product-diagonal partition of the rank-(s) layer;
* exact all-depth target disjointness;
* the theta-beating count of standalone full endpoints;
* distinct rank-(t) boundary tickets;
* a static/canonical containing central Johnson path.

Not supplied—and for long fully marked runs refuted in the fixed-additive
row architecture:

* a source word whose central derivative is the canonical owner path;
* placement inside the PBBS maximal envelopes;
* a (B(k)+C) construction for fixed (C).

The diagonal factor may remain useful after **sparsifying the marked
endpoints to at most (C+1) per overlap component**, or in a different
architecture whose middle owners are not the internal central-length
windows.  Its long-run warm-up amortization cannot be imported unchanged.

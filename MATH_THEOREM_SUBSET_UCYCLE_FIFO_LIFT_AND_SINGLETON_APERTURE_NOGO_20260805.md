# A subset universal cycle gives the FIFO lift exactly, but has no singleton aperture

**Date:** 2026-08-05  
**Method:** literal sliding windows and the mandatory erosion-endpoint lemma;
no computation or search  
**Status:** unconditional conditional-on-ucycle theorem. A symbol universal
cycle for the rank-\(r\) layer automatically supplies a delay-\(d\) queue
cycle which is bijective on owners. Its maximal antecedent is the rank-
\((r-d)\) shorter-window trace of the same symbol word. However every
mandatory source core then has two distinct endpoints, so no depth-\(d\)
antecedent of this owner cycle can represent a singleton target. Thus the
plain ucycle solves the owner/FIFO row but cannot by itself yield an
additive-constant universal OR word.

## 1. Subset universal cycles

Let

\[
                         z=(z_i)_{i\in\mathbb Z_W}               \tag{1.1}
\]

be a cyclic word on the symbol set \([k]\), where

\[
                         W={k\choose r}.                         \tag{1.2}
\]

Assume every length-\(r\) cyclic window has \(r\) distinct symbols and that
the window sets

\[
                         T_i=\{z_i,z_{i+1},\ldots,z_{i+r-1}\}    \tag{1.3}
\]

enumerate \({[k]\choose r}\) exactly once. Thus \(z\) is a symbol universal
cycle for the \(r\)-subsets.

Fix \(1\le d<r\), and put \(t=r-d\). Define

\[
 Q_i=\{z_i,\ldots,z_{i+d-1}\},
 \qquad
 S_i=\{z_{i+d},\ldots,z_{i+r-1}\}.                              \tag{1.4}
\]

## 2. Exact FIFO realization

### Theorem 2.1 (ucycle queue lift)

The word \(S\) is a rank-\(t\) Johnson trace with

\[
 S_{i+1}=S_i-\{z_{i+d}\}+\{z_{i+r}\}.                           \tag{2.1}
\]

Its delayed deletion queue is exactly \(Q_i\), and

\[
                         T_i=S_i\mathbin{\dot\cup}Q_i.           \tag{2.2}
\]

All queue conditions hold. The owner projection is bijective, and

\[
 \boxed{
   S_i=\bigcap_{h=0}^{d}T_{i+h}.}                               \tag{2.3}
\]

The maximal depth-\(d\) antecedent is therefore

\[
 \boxed{
   P_j=S_{j-d}=\{z_j,z_{j+1},\ldots,z_{j+t-1}\}.}                \tag{2.4}
\]

#### Proof

Distinctness of the symbols in (1.3) gives
\[
 |Q_i|=d,\qquad |S_i|=t,\qquad Q_i\cap S_i=\varnothing.
\]
Sliding the shorter window proves (2.1). Its deletion labels are
\(a_i=z_{i+d}\), so
\[
 \{a_{i-d},\ldots,a_{i-1}\}=\{z_i,\ldots,z_{i+d-1}\}=Q_i.
\]

The new insertion \(z_{i+r}\) is different from
\(z_{i+1},\ldots,z_{i+r-1}\), since these symbols lie together in
\(T_{i+1}\). It is also different from \(z_i\): otherwise
\(T_{i+1}=T_i\), contradicting the one-copy owner enumeration. Hence
\(z_{i+r}\notin Q_i\), and all FIFO conditions hold.

Equation (2.2) is (1.3)--(1.4). The owners are bijective by the ucycle
hypothesis. Equation (2.3) now follows from the delay-\(d\) queue-lift
identity, and shifting its index gives (2.4). \(\square\)

Thus a subset ucycle simultaneously closes:

1. the literal FIFO queue constraints;
2. the rank-\(r\) owner Hamiltonicity condition; and
3. the maximal-antecedent factorization.

It does **not** imply that the shorter windows \(S_i\) contain every
rank-\(t\) subset, nor that their duplicate occurrences have any favourable
spacing.

## 3. The mandatory cores have size two

Since every length-\(r\) window has distinct symbols and \(t<r\), the
successive maximal-antecedent letters satisfy

\[
 P_{j+1}=P_j-\{z_j\}+\{z_{j+t}\}.                               \tag{3.1}
\]

The mandatory erosion core at position \(j\) is

\[
 F_j=(P_j\setminus P_{j-1})\cup(P_j\setminus P_{j+1})
     =\{z_{j+t-1},z_j\}.                                       \tag{3.2}
\]

For \(t\ge2\), these two symbols are distinct.

### Theorem 3.1 (singleton-aperture obstruction)

Assume \(t\ge2\). Let \(A\) be any nonempty cyclic source word with

\[
                         A_j\subseteq P_j,
 \qquad
                         D^dA=T.                                \tag{3.3}
\]

Then

\[
                         |A_j|\ge2\qquad\hbox{for every }j.      \tag{3.4}
\]

Consequently no interval of \(A\) has singleton union. In particular, this
owner cycle has no depth-\(d\) antecedent which represents every nonempty
subset of \([k]\).

#### Proof

The mandatory erosion-endpoint lemma gives \(F_j\subseteq A_j\) for every
\(j\). Equation (3.2) has two distinct elements, proving (3.4). A union of
one or more such letters has rank at least two, so no singleton target is
represented. \(\square\)

Appending all missing singleton targets separately would cost \(k\)
positions, not \(O(1)\). Thus a plain subset ucycle cannot prove
\(\nu(k)\le B(k)+O(1)\) on this factorization face.

The obstruction is structural rather than scalar. The owner positive run
created by one occurrence of a symbol in \(z\) has length \(r\), whereas a
singleton source cell requires an owner positive run of the minimum length
\(d+1\). A ucycle has no such minimum run.

## 4. Relation to the duplicate-block and chart targets

The ucycle representation turns the lower fibre problem into the transparent
short-window problem

\[
                         X=\{z_i,\ldots,z_{i+t-1}\}.              \tag{4.1}
\]

Hence a proposed free bank is fibre-safe precisely when every rank-\(t\)
window used in the bank occurs at another start outside it. This may be a
useful language for concentrated duplicates.

Moreover a length-\(g\le d\) free block has private incoming markers
\(z_j,\ldots,z_{j+g-1}\), and its maximal letters have a large common
internal core. It therefore satisfies the local hypotheses of the
payload-plus-marker triangular-chart theorem. Nevertheless (3.2) shows
that every chart value contains at least a two-marker address. Such charts
cannot supply the singleton layer.

A viable hybrid would have to modify the ucycle chronology at enough places
to create one minimum owner run for every coordinate, while preserving the
owner bijection, concentrated lower duplicates, and the upper deck. This is
a nontrivial \(\Theta(k)\)-site structural modification, although it need
not add \(\Theta(k)\) positions.

## 5. Arithmetic and existence scope

In the central odd case \(k=2r+1\),

\[
                         W={2r+1\choose r}=(2r+1)\operatorname{Cat}_r.
                                                                    \tag{5.1}
\]

Thus the basic divisibility by the symbol-set size is automatic. This is
only an arithmetic check. Standard Euler-tour constructions which prove
subset ucyles for fixed subset size do not automatically furnish the
growing regime \(r\sim k/2\), and this note assumes rather than proves the
existence of \(z\).

Even if such a ucycle is supplied, Theorem 3.1 remains: the unmodified
ucycle is an owner/FIFO solution but not a complete lower compiler.

## 6. Dependencies and scope

The queue equivalence is in

MATH_THEOREM_DELAY_D_JOHNSON_QUEUE_LIFT_AND_DUPLICATE_BLOCK_TARGET_20260805.md.

The mandatory erosion-endpoint lemma and the local chart theorem are in

MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md.

This theorem proves no ucycle existence result, no duplicate-block
concentration, no upper-witness theorem, and no universal OR word.

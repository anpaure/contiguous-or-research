# Exact short-block target pins in a resident Johnson antecedent

**Date:** 2026-08-06  
**Method:** maximal envelopes, forced event pairs, and short-block freedom;
no computation or search  
**Status:** unconditional exact one-block theorem and separated-bank
corollary.  It reduces ordinary-word realization of the PBBS gap-section
compiler to a concrete forced-label/envelope block selector.  It does not
construct that selector for every deep target.

## 1. Resident trace data

Let

\[
                         T=(T_i)_{i\in\mathbb Z_W}
\]

be a cyclic simple rank-`r` Johnson trace which is `d`-resident.  Write

\[
 T_{i+1}=T_i-\{D_i\}+\{I_i\}.
\tag{1.1}
\]

Its maximal antecedent envelopes and forced source sets are

\[
 P_j=\bigcap_{h=0}^{d}T_{j-h},
 \qquad
 F_j=\{D_j,I_{j-d-1}\}.
\tag{1.2}
\]

Every antecedent letter satisfies

\[
                         F_j\subseteq A_j\subseteq P_j.
\tag{1.3}
\]

Conversely, arbitrary letters satisfying (1.3) on one block of at most `d`
positions, with maximal letters elsewhere, still form an antecedent.

## 2. Exact one-block criterion

Let `J` be a nonempty cyclic interval of source positions with

\[
                         |J|\le d,
\tag{2.1}
\]

and let `S` be a nonempty strict-lower target.

### Theorem 2.1 (short-block target pin)

There is a depth-`d` antecedent `A` of `T`, equal to the maximal antecedent
outside `J`, for which

\[
                         \bigcup_{j\in J}A_j=S
\tag{2.2}
\]

if and only if

\[
 \boxed{
   \bigcup_{j\in J}F_j\subseteq S
   \subseteq\bigcup_{j\in J}P_j.}
\tag{2.3}
\]

#### Proof

If (2.2) holds, (1.3) gives

\[
 \bigcup_{j\in J}F_j
 \subseteq\bigcup_{j\in J}A_j=S
 \subseteq\bigcup_{j\in J}P_j,
\]

so (2.3) is necessary.

Conversely assume (2.3).  For every `x in S`, choose one position
`j(x) in J` with `x in P_(j(x))`.  Define

\[
 H_j=F_j\cup\{x\in S:j(x)=j\}
 \qquad(j\in J).
\tag{2.4}
\]

The left inclusion in (2.3) gives `H_j subseteq S`, while the choice of
`j(x)` and (1.2) give `H_j subseteq P_j`.  Each `F_j` is nonempty on a
Johnson trace, so every `H_j` is nonempty.  Moreover

\[
                         \bigcup_{j\in J}H_j=S.
\]

Put `A_j=H_j` on `J` and `A_j=P_j` elsewhere.  Short-block freedom applies
because `|J|<=d`, proving that `A` is an antecedent.  Its union on `J` is
`S`, proving (2.2).  \(\square\)

Thus a proposed source cell has no hidden coordinatewise feasibility
condition beyond (2.3).

## 3. A separated target bank

Let `(S_a,J_a)`, `a in I`, be target/block pairs such that:

1. every `J_a` has length at most `d`;
2. the blocks are pairwise disjoint; and
3. between consecutive blocks there is at least one source position left at
   its maximal letter.

Assume every pair satisfies (2.3).

### Corollary 3.1 (separated literal atlas)

There is one antecedent of `T` in which every `J_a` has exact union `S_a`.
The cells `J_a` are distinct occurrence addresses.  Hence if the targets
`S_a` are distinct, the assignments

\[
                         S_a\longmapsto J_a
\tag{3.1}
\]

form a literal compiler matching.

#### Proof

Choose the letters (2.4) independently on every block.  The
separated-short-block freedom theorem says that the one unaltered maximal
position between blocks separates all new coordinate-support gaps; hence
all modifications coexist in one antecedent.  Theorem 2.1 gives every
declared union, and disjoint blocks give distinct occurrence addresses.
\(\square\)

The separation hypothesis is sufficient rather than necessary.  Overlapping
target blocks require the pinned maximal-envelope criterion on their complete
joint halo.

## 4. Consequence for the PBBS gap section

The canonical PBBS gap section assigns every strict-lower target `S` an
owner-intersection occurrence.  For intersection depth `q<=d`, the maximal
antecedent row identity already supplies the literal source interval

\[
 J(i,q)=[i+q,i+d],
 \qquad
 \bigcup_{j\in J(i,q)}P_j=S.
\tag{4.1}
\]

These are the automatic top-`d` rows.

For a selected target at depth `q>d`, no source interval follows from the
owner label alone.  The exact replacement question is now:

> Find a source block `J_S`, of length at most `d`, such that
> \[
>  \bigcup_{j\in J_S}F_j\subseteq S
>  \subseteq\bigcup_{j\in J_S}P_j,
> \tag{4.2}
> \]
> and choose the blocks occurrence-disjointly (or verify their joint pinned
> envelopes on overlapping halos).

Once (4.2) is solved for the deep gap-section targets, Theorem 2.1
materializes them in an ordinary word.  The terminal compiler-transport
theorem then carries the resulting one-copy matching through every planted
PBBS `C6`, pentagon, and split macro.  No two-coordinate typed terminal cap
is needed on the final branch.

## 5. Smallest remaining combinatorial lemma

For a simultaneous (possibly overlapping) choice of blocks, put

\[
 E_p^*=P_p\cap\bigcap_{S:p\in J_S}S,
\tag{5.1}
\]

where an empty target intersection is the whole ground set.  The pinned
maximal-envelope theorem says that the chosen atlas is realized by one
antecedent **if and only if**

\[
 E_p^*\ne\varnothing\quad\hbox{for every }p,
\tag{5.2}
\]

\[
 \bigcup_{p\in[i,i+d]}E_p^*=T_i
       \quad\hbox{for every owner window},
\tag{5.3}
\]

and

\[
 \bigcup_{p\in J_S}E_p^*=S
       \quad\hbox{for every selected target }S.
\tag{5.4}
\]

Thus overlaps introduce no further existential word variables: after the
blocks are selected, (5.2)--(5.4) are the exact deterministic test.

The initial lower-side problem is therefore the following block selector.

> **Deep gap-section block-selection lemma.**  In the chosen resident
> canonical PBBS trace, assign every selected target of depth greater than
> `d` a distinct short block satisfying (4.2), while preserving the already
> fixed top-`d` cells and the protected local-history halos, so that the
> joint envelopes (5.1) satisfy (5.2)--(5.4).

This statement is strictly smaller than constructing a full cap network:
it has only source positions, forced pairs, maximal envelopes, and target
containment.  It is also genuinely open.  The one-sided owner occurrence
SDR proves neither inclusion in (4.2), and aggregate short-cell capacity
does not imply the required occurrence-disjoint block assignment.

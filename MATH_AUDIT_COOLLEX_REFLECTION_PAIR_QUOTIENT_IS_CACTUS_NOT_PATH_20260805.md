# Audit: a reflected partial matching folds a path to a cactus, not always a path

**Date:** 2026-08-05  
**Object audited:** the quotient consequence of
`MATH_THEOREM_COOLLEX_SIBLING_PARENT_TORUS_MULTIPLICITY_TWO_20260805.md`  
**Method:** nested-interval quotient of a path; no computation  
**Status:** exact correction.  The promoted-torus multiplicity-two theorem
and common-reflection formula remain valid.  The claim that the simple
quotient is always a folded path is too strong.

## 1. Valid input

Inside one cool-lex sibling family, the proved bank-multiset calculation
shows that labels sharing one unmarked promoted torus form singleton blocks
or pairs

\[
                         a\longleftrightarrow C-a.       \tag{1.1}
\]

The realized pairs form a partial matching `M`.  If

\[
 a_1<a_2<\cdots<a_t<C/2,
\]

then their partners satisfy

\[
 C-a_1>C-a_2>\cdots>C-a_t.
\]

Thus the paired intervals are nested and never cross.  This part of the
existing theorem is correct.

## 2. The quotient can have degree four

Take the label path

\[
                         1-2-3-4-5-6-7-8-9-10
\]

and let the only realized reflected pair be `3<->8` (so `C=11`).  After
identification, the paired block `X={3,8}` has neighbors

\[
                         2,4,7,9.
\]

These four neighbors are distinct.  The simple quotient therefore has

\[
                         \deg(X)=4,                   \tag{2.1}
\]

and contains the cycle

\[
                         X-4-5-6-7-X                 \tag{2.2}
\]

with a path tail on each side.  Hence a partial matching contained in one
reflection does **not** imply that identifying its pairs leaves a path or
a maximum-degree-two graph.

This is a logical counterexample to that implication.  It does not assert
that this exact one-pair pattern occurs for every PBBS exterior word; the
bank-multiset theorem supplies no converse or interval-saturation statement
that would exclude it.

## 3. Correct quotient theorem

### Theorem 3.1

The quotient of a path by a partial matching contained in one reflection
is a cactus whose cycle blocks form a path; at most two ordinary path tails
attach at the outermost articulation.  Its maximum simple degree is at most
four.

#### Proof

List the realized left endpoints as

\[
 a_1<a_2<\cdots<a_t
\]

and put `r_i=C-a_i`.  Then

\[
 a_1<a_2<\cdots<a_t<r_t<\cdots<r_2<r_1.             \tag{3.1}
\]

After identifying `a_i` with `r_i`, call the resulting vertex `X_i`.
For each `i<t`, the left interval from `X_i` to `X_(i+1)` and the reflected
right interval from `X_(i+1)` back to `X_i` are internally disjoint.  Their
union is one cycle block (with the usual parallel-edge degeneration when
an interval has length one).  The innermost interval from `a_t` to `r_t`
gives the final cycle block, unless it degenerates to a loop.  The portions
before `a_1` and after `r_1` are tails incident with `X_1`.

Different cycle blocks meet only in consecutive articulation vertices
`X_i`.  Hence the quotient is a cactus and its cycle-block chain has the
linear order

\[
                         X_1,X_2,\ldots,X_t.
\]

An internal `X_i` has two incident edges from each of its two neighboring
cycle blocks.  At `X_1`, two cycle edges and the two possible tails give
the same bound.  Thus degree four can occur and no larger degree can.
`square`

## 4. Consequence for the splice target

The correct recursive third-shore target is therefore not an arbitrary
port permutation, but it is also not merely a folded path.  It is a
singleton/pair **cactus chain** with:

1. maximum block degree two;
2. maximum vertex degree four;
3. one linear nesting order;
4. possible loop and parallel-edge terminal degeneracies.

This remains a major reduction.  A constant-state proof may process the
cactus blocks serially from the innermost reflected pair outward.  But a
proof that assumes every paired block has only two quotient neighbors is
invalid unless it separately proves that the realized reflection pairs are
interval-saturated.

## 5. Scope

Preserved:

* at most two ports of one sibling family on one promoted torus;
* one common reflection containing every realized pair;
* absence of crossing pair chords.

Corrected:

* the quotient is a cactus chain, not necessarily a path;
* degree four, rather than degree two, is the sharp abstract bound.

Still open:

* a port-order splice through the cactus chain;
* literal composition of the overlapping q2 halos;
* global integration across different sibling calls.

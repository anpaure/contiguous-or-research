# One native PBBS hook component carries every consecutive low target

**Date:** 2026-08-06  
**Method:** one-pile hook rotor, exact root recurrence, and short-gap
mandatory-core thinning; no search  
**Status:** unconditional for `d>=1`, `d+1<m`.  On one untouched hook
component, every cyclic coordinate interval of every rank
`1,...,d` occurs literally and all these occurrences coexist.  Targets
with two or more cyclic runs remain a separate gate.

## 1. One-pile rotor

Put

\[
 n=2m+1,
 \qquad h=d+1,
 \qquad p=2d+1,
 \qquad b=m-d-1>0.
\tag{1.1}
\]

Take a hook angle whose `p`-slot weak composition has one entry equal to
`b` and all other entries zero.  Its slot period is exactly `p`, so its
hook torus is one PBBS component of length `np`.

As the slots rotate past the terminal position, there are exactly

\[
                         p-1=2d
\tag{1.2}

consecutive zero-terminal phases, followed by the unique nonzero-terminal
phase.  At a phase of terminal occupancy `z`, the exact hook formula is

\[
 r_{t+1}=r_t-(2z+1),
 \qquad
 F_t=\{r_t,r_t-2z\}.
\tag{1.3}

Hence along the zero-terminal stretch,

\[
 r_{t+a}=r_t-a,
 \qquad
 F_{t+a}=\{r_t-a\}.
\tag{1.4}

After one full slot period,

\[
                         r_{t+p}=r_t+2\pmod n.
\tag{1.5}

## 2. Simultaneous singleton thinning

In each of the `n` consecutive `p`-position periods around the component,
choose the same `d`-position subblock inside the `2d`-position zero stretch.
Let its first root be `r_j`.  Thin its maximal-envelope letters to

\[
 \{r_j\},\{r_j-1\},\ldots,\{r_j-d+1\}.
\tag{2.1}

Every chosen letter equals its mandatory core by (1.4).  The changed
positions form `n` blocks of length exactly `d`, and successive changed
blocks are separated by

\[
                         p-d=d+1
\tag{2.2}

unchanged positions.  The mandatory-core short-gap theorem therefore
gives an exact depth-`d` antecedent:

\[
                         D^dA=T.
\tag{2.3}

No owner or factor edge has moved.

## 3. Complete consecutive atlas

For `1<=s<=d`, the first `s` letters of block `j` have union

\[
                         \{r_j,r_j-1,\ldots,r_j-s+1\}.
\tag{3.1}

Equation (1.5) gives

\[
                         r_j=r_0+2j\pmod n.
\tag{3.2}

Because `n` is odd, `2` is invertible modulo `n`; as `j` runs from zero
to `n-1`, the starts `r_j` run through every coordinate.

### Theorem 3.1 (all consecutive low targets on one component)

The single thinned one-pile hook component above contains, simultaneously,
one literal source interval for every target of the form

\[
                         \{a,a-1,\ldots,a-s+1\},
 \qquad 1\le s\le d,
 \qquad a\in\mathbb Z_n.
\tag{3.3}

The occurrences are compatible even when their source intervals overlap,
because they all read the one fixed singleton word (2.1).

Every inherited owner-interval upper witness remains valid: (2.3) implies

\[
 \bigcup_{i=u}^{v}T_i=\bigcup_{t=u}^{v+d}A_t.
\tag{3.4}

The component is untouched by the full rigid one-/two-soliton rethread in
the eventual regime, since its action partition `(d+1,1^(m-d-1))` has at
least three solitons.

## 4. Scope

This theorem closes every low target having one cyclic positive run.  It
does not cover an arbitrary low target with two or more separated runs.
The exact next language is obtained by allowing several nonzero hook slots:
zero slots emit consecutive singleton rails, while a nonzero slot `z`
has mandatory bridge core `{r,r-2z}`.  A general all-low theorem must show
that these rails and bridges encode every at-most-`d` subset with a
component-disjoint Hall selection.

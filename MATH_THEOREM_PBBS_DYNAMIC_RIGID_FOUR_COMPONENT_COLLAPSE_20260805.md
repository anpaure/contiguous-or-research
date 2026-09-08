# Dynamic escape from the rigid PBBS component with two rotated neutral connectors

**Date:** 2026-08-05  
**Method:** permutation-cycle calculus and cyclic-rotation separation; no
computation or search  
**Status:** unconditional for all sufficiently large `m`.  The statically
isolated single-soliton component can be absorbed dynamically, after its
unique neutral split, into a subsystem with exactly two completely selected
cycles.  The theorem is local to four named input components; it does not
prove the global PBBS quotient has boundedly many blocks.

## 1. Inputs

Put `n=2m+1` and let `F` be the centered PBBS Johnson two-factor with its
max-height q1 section.

Use the following two already proved connector families.

1. The **rigid connector** `R` is the unique q2-neutral clean `C6` through
   a single-soliton edge.  It uses one old edge on the single-soliton
   component `S` and two old edges on the unique `(m-1,1)` component `T`.
   Switching it replaces `S,T` by two cycles.  If the two open directed
   `T`-arcs are denoted `Pi_1,Pi_2`, one output contains `Pi_1` together
   with the opened `S` path, and the other contains `Pi_2`.

2. The **promotion connector** `E` is the explicit selected q2-neutral
   three-component clean `C6` on components

   \[
      A:(m-2,1,1),\qquad B:(m-2,2),\qquad T:(m-1,1).
   \tag{1.1}
   \]

   Every cyclic coordinate translate `rho^j E` uses the same three PBBS
   components `A,B,T`.  Its `T`-edge positions are spaced by

   \[
                         p=2m-3
   \tag{1.2}
   \]

   directed steps around `T`.  The two arcs cut by `R` have lengths

   \[
                         p(m+1),\qquad pm-2.
   \tag{1.3}
   \]

All four components in (1.1), together with `S`, are wholly selected when
`m>=6`: their largest two soliton parts differ by at least two.  Therefore
every connector occurrence used below belongs to the selected section.

## 2. A bounded forbidden-rotation lemma

For a connector `G`, let `Sigma(G)` contain every rank-`m` factor vertex
on a changed edge and every rank-`m` factor vertex on an unchanged
companion edge used in its q2 identity.  This is a fixed finite set; for a
clean `C6`, the six changed-shore vertices and at most six other companion
endpoints give

\[
                         |Sigma(G)|\le 12.
\tag{2.1}
\]

### Lemma 2.1

Let `U,V` be two fixed finite sets of rank-`m` subsets of `Z_n`.  The
number of rotations `j in Z_n` for which

\[
                         rho^j U\cap V\ne\varnothing
\tag{2.2}
\]

is at most `|U||V|`.

#### Proof

No rank-`m` subset has a nontrivial rotational stabilizer.  Indeed, if a
nonidentity rotation stabilized such a set, that set would be a union of
orbits of a common size `q>1` dividing `n`; then `q` would divide `m`,
contrary to `gcd(m,2m+1)=1`.

For each ordered pair `(u,v) in U times V`, there is consequently at most
one rotation with `rho^j u=v`.  Summing over the pairs proves the bound.
`square`

### Corollary 2.2

For all sufficiently large `m`, there are two translates `E_1,E_2` of
`E` such that

1. the `T`-edge of `E_i` lies in the interior of `Pi_i`;
2. `Sigma(R),Sigma(E_1),Sigma(E_2)` are pairwise disjoint.

#### Proof

The rotation positions on `T` have gap exactly `p`.  An open interval of
length `p(m+1)` contains at least `m` interior positions and one of length
`pm-2` contains at least `m-2`.  Thus each arc supplies a number of
candidate rotations tending to infinity with `m`.

After one finite support is fixed, Lemma 2.1 excludes at most `12^2`
rotations of `E`; after two supports are fixed it excludes at most twice
that number.  Hence, once `m` exceeds an absolute constant, choose first a
candidate on `Pi_1` avoiding `R`, and then a candidate on `Pi_2` avoiding
both earlier supports.  `square`

No optimization of the finite threshold is needed for an all-dimensional
additive-constant theorem; the finitely many smaller dimensions can be
absorbed in its terminal constant.

## 3. Exact dynamic topology

### Theorem 3.1

Apply `R`, then `E_1`, then `E_2`.  On the vertex set originally carried
by `S,T,A,B`, the final factor has exactly two cycles.  The transported q1
section is still one-occurrence and q2-complete, and both final cycles are
completely selected.

#### Proof

The switch `R` replaces `S,T` by two cycles `H_1,H_2`, with the interior
of `Pi_i` lying on `H_i`.  Components `A,B` are untouched.  Thus there are
four cycles on the displayed subsystem.

The three old edges of `E_1` now lie on the three distinct cycles

\[
                         H_1,A,B.
\]

A clean three-way switch merges them into one cycle `M`.  The subsystem
therefore has exactly two cycles, `M,H_2`.

For `E_2`, its `T`-edge lies on `H_2`, while its `A`- and `B`-edges both
lie on `M`.  Cut these three old edges.  Cutting one edge of `H_2` gives
one directed path; cutting two edges of `M` gives two directed paths.
Hence there are exactly three paths before reconnection, so the new factor
has at most three cycles on this subsystem.

On the fixed subsystem vertex set, the clean reconnection multiplies the
successor permutation by a 3-cycle, which is even.  Since
`sgn(pi)=(-1)^(N-c(pi))`, the parity of the number `c(pi)` of permutation
cycles is therefore unchanged.  The pre-switch component count is two, so
the post-switch count is even.  It is positive and at most three, and
consequently equals two.

All three switches have pairwise disjoint protected supports and each is
q1- and q2-neutral.  Their palette identities therefore compose.  Every
input occurrence on `S,T,A,B` was selected, and each removed selected edge
is replaced by a selected edge.  Hence no omission is created anywhere in
the subsystem: both final cycles are wholly selected.  `square`

## 4. Bounded-defect consequence

The bounded-graphic-defect q2 Pascal theorem may puncture one selected
turn on each of these two residual cycles.  With two residual cycles, its
q2/owner interface charge is at most

\[
                         2\cdot2=4
\tag{4.1}
\]

named sidecar occurrences.

Thus the static degree-zero obstruction of the single-soliton component is
not an unbounded obstruction: the rigid four-component subsystem has an
explicit dynamic reduction to constant graphic defect.

## 5. Scope

This theorem does **not** absorb the exponentially many other wholly
selected PBBS components.  It removes only the exceptional static
isolation at the top of the soliton poset.  The remaining global theorem is
an angle-level loose-forest or dynamic-collapse statement for the other
action tori, followed by the already separate residence, arbitrary-upper,
and common-cap interfaces.

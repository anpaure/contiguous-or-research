# Symmetric Hall witnesses by uncrossing

Date: 2026-07-27

## 1. Lemma

Let `G=(L,R;E)` be a finite bipartite graph and let a finite group
`Gamma` act by automorphisms of `G`.  For `A subseteq L`, write

\[
\delta(A)=|A|-|N(A)|.
\]

### Theorem 1 (invariant Hall witness)

If Hall's condition fails in `G`, then it fails on a `Gamma`-invariant
subfamily.  Explicitly, there is a union `U` of complete `Gamma`-orbits in
`L` such that

\[
|N(U)|<|U|.
\]

### Proof

First observe the uncrossing inequality

\[
\delta(A\cup B)+\delta(A\cap B)
\ge \delta(A)+\delta(B).
\tag{1.1}
\]

Indeed,

\[
N(A\cup B)=N(A)\cup N(B),
\qquad
N(A\cap B)\subseteq N(A)\cap N(B),
\]

so the sum of the two neighbourhood sizes on the left is at most
`|N(A)|+|N(B)|`.

Choose an inclusion-minimal deficient family `A`, so `delta(A)>0` and every
proper subset of `A` has nonpositive deficiency.  Enumerate the translates
`gA`, and build their union one at a time.  Suppose the current union `U` is
deficient and add `gA`.  If `gA subseteq U`, nothing changes.  Otherwise
`U cap gA` is a proper subset of `gA`; translating back makes it a proper
subset of `A`, hence

\[
\delta(U\cap gA)\le0.
\]

Using (1.1),

\[
\delta(U\cup gA)
\ge
\delta(U)+\delta(gA)-\delta(U\cap gA)>0.
\]

Thus the union of all translates of `A` remains deficient.  It is invariant
and is a union of complete orbits.  \(\square\)

## 2. Consequence for translation quotients

For a translation-equivariant bipartite graph under `Z_p`, Hall's condition
can be checked on unions of translation orbits.  When both shores are free,
the invariant Hall inequalities divide by `p` and become the ordinary Hall
inequalities of the quotient multigraph.

This does **not** say that singleton orbit inequalities suffice: an arbitrary
union of quotient orbits may still be the obstruction.  It does show that no
genuinely phase-asymmetric Hall witness is needed.

## 3. Application to the exact compiler

Before cutting a Catalan rotor, its cyclic erosion envelopes and their
canonical shadow pins are translation-equivariant.  Once a
translation-equivariant hitting core is fixed, the low-target sandwich graph

\[
C_j\subseteq S\subseteq P_j
\]

inherits the translation action.  Theorem 1 reduces every possible bulk
PCSH obstruction to the Catalan quotient.  A linear cut and its nested flag
alter only the boundary positions; those must be handled separately.

Accordingly, a promising route to a dimension-uniform compiler theorem is:

1. prove quotient Hall expansion for the cyclic bulk sandwich graph;
2. reserve an `O(d)` boundary reservoir;
3. absorb the nested endpoint flag inside that reservoir.

The lemma does not prove the required expansion, but it removes all
phase-specific subsets from the dual obstruction and makes precise why the
translation rotor is a useful proof coordinate rather than merely a search
speedup.

## 4. Application to the sigma design

The same uncrossing applies to each bipartite matching subproblem in a
translation-equivariant sigma construction.  It cannot replace the coupled
middle-degree, upper-load, and chronology constraints by separate Hall
checks, but any genuine Hall obstruction inside one frozen stage has an
orbit-union witness.  Thus exact coverdown and absorption arguments may be
formulated entirely on necklace orbits, with phase handled by voltage.

# A Hamilton path in the GK root-rotation graph fuses all root hinges into one incidence cycle

**Date:** 2026-08-07  
**Status:** exact conditional fusion theorem and exact odd-semilength
obstruction.  A Hamilton path would fuse all root hinges, but the Catalan
parity imbalance proves that such a path is impossible for odd
`m>=5`.  The theorem therefore identifies a valid even-subsequence route
and proves that an all-`m` argument needs a higher circuit or a second
distinguished-upstep phase.

## 1. Root circuits

Use the root-rotation graph `R_m` and its edge circuit `C_e` from
`MATH_THEOREM_GK_ROOT_ROTATION_C6_AND_PARITY_NOGO_20260807.md`.
For an edge `e=UV`, the circuit `C_e` is an alternating incidence `C_6`.
It contains the two fixed root edges

\[
                 f_U=X_Ut(X_U),\qquad f_V=X_Vt(X_V),  \tag{1.1}
\]

and one auxiliary fixed edge

\[
                              Z_e t(Z_e).             \tag{1.2}
\]

Distinct edge colours `a_e` give distinct `Z_e`, and no `Z_e` is a fixed
root facet `X_U`.  Therefore

\[
 C_e\cap C_{e'}=
 \begin{cases}
  f_U,&e\cap e'=\{U\},\\
  \varnothing,&e\cap e'=\varnothing,
 \end{cases}                                          \tag{1.3}
\]

as physical incidence subgraphs.

## Theorem 1.1 (path fusion)

Let

\[
 U_0e_1U_1e_2\cdots e_{r}U_r                 \tag{1.4}
\]

be a simple path in `R_m`.  Then

\[
                         C(P)=\mathop{\triangle}_{i=1}^{r} C_{e_i}
                                                               \tag{1.5}
\]

is one simple incidence cycle of length

\[
                              4r+2.                            \tag{1.6}
\]

It contains every root facet `X_{U_i}` and its fixed successor
`t(X_{U_i})`, and hence tickets every root on the path.

### Proof

For `r=1` this is the root `C_6`.  Suppose the first `r-1` circuits fuse to
one cycle.  Its terminal root edge `f_{U_{r-1}}` occurs once: it belongs to
`C_{e_{r-1}}` and no earlier circuit.  By (1.3), `C_{e_r}` meets the fused
cycle in exactly this edge.  The symmetric difference of two simple cycles
meeting in exactly one edge is one simple cycle; it deletes the common edge
and joins the two complementary paths.  Its length increases by `6-2=4`.
Induction gives (1.6).

At an internal root `U_i`, the shared fixed edge `f_{U_i}` cancels, but its
two endpoints remain, each joined to one edge from the circuit on the left
and one from the circuit on the right.  At the two endpoint roots the fixed
edge remains.  Thus every displayed root facet and successor is present.
\(\square\)

## Corollary 1.2 (Hamilton-path root block)

If `R_m` has a Hamilton path, the `Cat_m-1` root circuits indexed by its
edges fuse to one incidence cycle of length

\[
                         4\operatorname {Cat}_m-2.              \tag{1.7}
\]

The cycle tickets every Greene--Kleitman singleton root.  Its two shores
each have

\[
                         2\operatorname {Cat}_m-1               \tag{1.8}
\]

vertices: all `Cat_m` fixed root facets, plus one private auxiliary vertex
`Z_e` for every path edge.

In particular, the Catalan inversion-parity imbalance obstructs only
**disjoint** paired-root circuits.  It does not obstruct a path fusion:
internal roots are overlap sockets, and each has physical degree two after
the shared fixed edge is cancelled.

## 2. Exact boundary of the path route

The smallest root-host question is now:

> with moves
> \[
> 1A1B0C0D\longleftrightarrow1A0B1C0D
> \]
> has a Hamilton path.
For even `m`, the natural remaining graph question is whether the graph on
Dyck words with moves

\[
 1A1B0C0D\longleftrightarrow1A0B1C0D                 \tag{2.1}
\]

has a Hamilton path.

There can be no all-`m` version of this statement.  For `m=2s+1`, the two
inversion-parity shores differ by `Cat_s`.  A Hamilton path in a bipartite
graph alternates between the two shores and hence their sizes differ by at
most one.  Therefore

\[
 \boxed{R_{2s+1}\text{ has no Hamilton path for every }s\ge2.} \tag{2.2}
\]

More generally, any vertex-disjoint path cover of `R_{2s+1}` has at least
`Cat_s` paths.  Thus boundedly many path fusions cannot yield an all-`m`
root block.
> with moves
> \[
> 1A1B0C0D\longleftrightarrow1A0B1C0D
> \]
> has a Hamilton path.

Ordinary Catalan Gray-code theorems cannot be imported without checking
their move set.  The full binary-tree rotation graph is denser than `R_m`,
and a Gray code using one or two leaf pulls does not by itself prove the
conjecture above.

Even a Hamilton path on the even subsequence would close only the
omission-ticket block.
The fused cycle must still be joined to the exterior factor while retaining
intersection-colour surjectivity, upper colours, residence, and deeper OR
guards.  The immediate next palette calculation is the exact sequence of
intersection colours created at the cancelled internal root edges.

For odd semilength, the exact next object must cross the parity shore.  Two
minimal possibilities remain:

1. a length-three/four root hypercircuit which tickets unequal numbers of
   the two inversion parities while remaining degree two physically; or
2. a second hinge phase based on a different distinguished upstep, whose
   parity imbalance is complementary to the first phase.

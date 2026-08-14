# The flat D5 router--token incidence graph is a 33-component pseudoforest

**Date:** 2026-08-14  
**Status:** exact symbolic theorem with H100 replay.  It reduces the global
flat-atlas compiler to tree propagation plus eight independent holonomy
closures.  It does not construct the required Johnson collars.

## 0. Outcome

Form the bipartite graph whose left vertices are the 226 three-cycle
routers in the flat minimum D5 atlas, whose right vertices are the 477
logical head tokens, and whose incidences record membership of a token in a
router triple.  Then:

```text
router vertices                         226, all degree 3
token vertices                          477
token degrees                  1:292, 2:169, 3:16
incidences                               678
connected components                      33
tree components                           25
unicyclic components                       8
two-core of every unicyclic component     K2,2 = C4.
```

Each of the 25 odd target cycles gives one tree component.  Each of the
eight paired-even target blocks gives one unicyclic component.  Thus the
global cycle rank is exactly eight, not proportional to the 226 routers or
477 tokens.

This is the relevant constraint geometry for a physical compiler.  If a
local extension relation is total on every encountered boundary state and
its successive choices preserve the global resource constraints, then it
propagates greedily on the tree blocks; only eight independent four-cycle
closure subproblems remain.  The graph theorem alone supplies neither
totality nor resource compatibility.

## 1. Odd target cycles give trees

For an odd target cycle

\[
               (v_1\ v_2\ \cdots\ v_{2r+1}),
\]

the flat factorization uses the `r` router triples

\[
 (v_1v_2v_3),\ (v_3v_4v_5),\ldots,
 (v_{2r-1}v_{2r}v_{2r+1}).                       \tag{1.1}
\]

Their incidence graph is connected: consecutive router vertices meet at
the token `v_(2j+1)`.  It has

\[
 r+(2r+1)=3r+1\quad\hbox{vertices},
 \qquad 3r\quad\hbox{edges}.                     \tag{1.2}
\]

Hence it is a tree.  The chain-junction tokens have degree two and every
other token has degree one.

There are 25 odd target cycles in the frozen D5 selection, giving the 25
tree components.

## 2. A paired-even block is unicyclic

Let the two even target cycles have lengths `2r` and `2s`.  Their odd
prefix chains use respectively `r-1` and `s-1` routers.  Write their
residual transpositions as

\[
                         (a\ b),\qquad(c\ d).
\]

The flat factorization adds the two bridge routers

\[
                         (a\ c\ b),\qquad(a\ c\ d).          \tag{2.1}
\]

The complete incidence block is connected.  It has

\[
 (r+s)\ \hbox{router vertices},qquad
 2r+2s\ \hbox{token vertices},qquad
 3(r+s)\ \hbox{edges}.                              \tag{2.2}
\]

Thus its cycle rank is one.  Peeling all leaves and the two attached prefix
chains leaves precisely the four incidences

\[
 a--(a\ c\ b)--c--(a\ c\ d)--a,                  \tag{2.3}
\]

so its two-core is `K_(2,2)=C4`.  The tokens `a,c` have degree three; all
other chain junctions have degree two and the remaining tokens degree one.

The 16 even target cycles are paired into eight blocks, producing the eight
unicyclic components and exactly 16 degree-three tokens.

## 3. Global count and compiler reduction

Adding Sections 1--2 gives 33 connected components and global cycle rank
eight.  The degree identities also force the exact exposure histogram:

\[
 292+169+16=477,qquad
 292+2(169)+3(16)=678.                            \tag{3.1}
\]

This supports a sharper physical strategy than 226 independently closed
router boxes.

1. Assign the three port-edge parameters of one router.
2. Propagate compatible parameters across token collars along each tree
   edge.
3. At a degree-one token, use one dummy phase-common identity cut if an
   owner-simple q1-exact two-edge splice is forbidden.
4. At a degree-two token, seek one three-cut q1-exact C6 collar; at a
   degree-three token, seek one four-cut q1-exact C8 collar.
5. Solve only the eight `C4` two-core holonomies simultaneously.

The resulting menu target is

```text
461 prospective C6 strand collars = 292 dummy-completed leaves + 169 joints,
 16 prospective C8 strand collars = the degree-three tokens,
  8 independent holonomy closures.
```

These counts are exact, but the word “prospective” is essential.  The
theorem does not prove prescribed-edge extendability of the C6/C8 collars,
owner/palette disjointness, q2 transparency, residence, or compatibility
with the native factor.  The audited bare-splice obstruction shows that the
dummy/coupled collar layer cannot simply be omitted.

## 4. H100 replay

The independent verifier reconstructs the bipartite graph only from the
flat atlas certificate, computes every connected component and two-core,
checks that the provenance blocks are exactly the graph components, and
reproduces all degree and cycle-rank counts.

```text
verifier
  scratch/verify_d5_flat_router_token_pseudoforest_20260814.py
  SHA256 016d9cd911363e8a5bc0de9f61a0da495906c0d37f8ed687b6bcaf5f92848393

H100 output
  scratch/verify_d5_flat_router_token_pseudoforest_20260814.h100.out
  SHA256 d7a7f39e13e2543344f9c5eb6bf321e113c9511f79e5976f7053aa9358e672c1

flat atlas certificate
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.h100.out
  SHA256 2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc
```

All graph reconstruction, verification and hashing were run through SSH on
H100.  The local Mac was used only to edit, transfer and operate Git.

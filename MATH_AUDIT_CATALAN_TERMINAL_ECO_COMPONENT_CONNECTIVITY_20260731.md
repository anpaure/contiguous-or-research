# Terminal fixed-rotation ECO connectivity: exact reduction and finite audit

Date: 2026-07-31  
Status: superseded finite audit.  The all-`n` terminal leaf-shuttle lemma
and component-connectivity theorem are now proved in
`MATH_THEOREM_CATALAN_TERMINAL_LEAF_SHUTTLE_CONNECTIVITY_20260731.md`.

## Supersession

The finite computations and negative centroid-potential result below remain
valid.  The former open lemma is no longer open: every blocked leaf pull has
an explicit label-preserving replacement by three or five terminal pulls.
The cited theorem gives the exhaustive local case split and an independent
literal replay through `n=12`.  Read statements below that call the all-`n`
step open as historical audit context only.

## 0. Verdict

Let the fixed-rotation coherent ECO atoms be indexed by

\[
                         D=1u0v\in\mathcal D_{n-1}.
\]

The common physical/forced-colour collision forest has arrows

\[
                 1p100v\longrightarrow1p010v.                    \tag{0.1}
\]

Its terminal vertices are exactly the parents for which `u` is empty or
does not end in the primitive leaf `10`.  Keep only those atoms.

There is a sharper component statement than the three-role ECO
formulation.  The two old component roles `a,b` alone give the plane-tree
edge

\[
       [1u100v]\;--\;[1u010v],\qquad u=\varnothing
       \text{ or }u\not\equiv *10.                              \tag{0.2}
\]

The graph (0.2) is connected for every `2<=n<=12`.  The last audited row
has

\[
 8714\text{ plane-tree vertices},\qquad41990\text{ terminal labels}.
\]

An independent longer replay also reached `n=13` (28640 vertices and
149226 terminal labels), but it is not included in the bounded frozen
audit below.  No counterexample is known.

This does **not** yet constitute an all-dimension proof.  In particular,
the standard centroid-potential arborescence cannot prove it: genuine local
minima appear first at `n=5` and then in counts

\[
                    1,1,2,3,5,11\quad(n=5,\ldots,10).            \tag{0.3}
\]

The first is the plane tree `1010110100`; its only terminal neighbour has
larger centroid potential.

## 1. Why the two-role reduction is exact

For `D=1u0v`, the three old factor components of the ECO atom are the plane
trees obtained by putting one new leaf in the three consecutive corners
around the distinguished root edge.  The first two rooted contour words are

\[
                         A(D)=1u100v,
       \qquad            B(D)=1u010v.                              \tag{1.1}
\]

Thus every retained atom contains the edge `[A(D)][B(D)]` in its component
two-section.  Proving that the graph of these edges is connected is already
sufficient for terminal-bank two-section connectivity; the third role is
not used.

The collision arrow (0.1) is just the case where the child-side insertion
corner is preceded by another leaf.  Indeed, if `u=p10`, then moving the
root across that terminal child changes the parent word from

\[
                           1p100v\quad\text{to}\quad1p010v.
\]

Hence terminal retention has the following intrinsic plane-tree meaning:

> a leaf may be pulled across an oriented edge when the child-side corner
> is empty after a nonleaf branch (or the child has no other branch).

Call this a **safe leaf pull**.  Equation (0.2) is exactly the safe-pull
graph on unrooted plane trees.

## 2. The exact missing all-dimension lemma

The unrestricted MMM leaf-pull graph is connected.  Therefore the terminal
theorem would follow from the following local replacement statement.

### Terminal leaf-shuttle lemma (open)

Every blocked pull

\[
 [1p\,10\,100v]\;--\;[1p\,10\,010v]                            \tag{2.1}
\]

is replaceable by a path of safe pulls.  Equivalently, every edge deleted
from the unrestricted leaf-pull graph has its endpoints in one component
of (0.2).

Finite replay through `n=11` gives the stronger bound that every deleted
edge has a replacement path of length at most five.  This is highly
suggestive of one associahedral pentagon/leaf-buffer identity.  It is not
yet a proof that the same five-step identity exists with arbitrary Dyck
forests substituted in the untouched corners.

The obstruction is concentrated in a consecutive leaf block.  For a block
of odd length, pair its first leaves into pendant two-paths; the final leaf
then has a nonleaf predecessor, can be pulled safely, and the pairings can
be undone.  This gives a literal safe-pull simulation.  The unresolved
base is a block of exactly two consecutive leaves.  Every such tree has a
third leaf on the other side of the pull edge, but a rigorous shuttle of
that third leaf into and back out of the local buffer corner—without
assuming a rooted-cylinder connectivity statement, which is false—is the
remaining step.

This formulation is useful because it rules out two tempting invalid
proofs.

1. **Centroid potential.**  It has the local minima (0.3).
2. **Rooted cylinder induction.**  The safe-pull graph on rooted Dyck words
   is already disconnected at semilength three; plane rerooting is
   load-bearing.

## 3. Scope for the post-glue route

The present statement concerns only component supply.  If the terminal
leaf-shuttle lemma is proved, it gives a connected terminal component
two-section.  It does not by itself choose a pairwise-disjoint incidence
hypertree or prove that simultaneous symmetric difference is Hamiltonian.

For the current post-glue architecture, no owner, alternating-SDR or router
condition is imposed during this first topology stage: a final packet is
allowed to create the joint alternating SDR after Hamiltonization.  The
stronger transparent-decoration criterion is therefore deliberately out of
scope here.  Physical support disjointness, component-faithful hypertree
selection, and final post-glue repair remain separate gates.

## 4. Deterministic audit

Run

```text
python3 scratch/audit_catalan_terminal_eco_component_connectivity_20260731.py
```

It constructs plane-tree keys directly, retains exactly the terminal
parents, and unions only the `A--B` edges (0.2).  It also checks the Catalan
counts

\[
 |\mathcal D_{n-1}^{\rm nonterminal}|=\operatorname{Cat}_{n-2},
 \qquad
 |\mathcal D_{n-1}^{\rm terminal}|
   =\operatorname{Cat}_{n-1}-\operatorname{Cat}_{n-2}              \tag{4.1}
\]

for `n>=3`, and reproduces the potential-local-minimum obstruction through
`n=10`.

The frozen output is

```text
scratch/catalan_terminal_eco_component_connectivity_20260731.audit.json
```

This is a finite exact audit, not an all-`n` certificate.

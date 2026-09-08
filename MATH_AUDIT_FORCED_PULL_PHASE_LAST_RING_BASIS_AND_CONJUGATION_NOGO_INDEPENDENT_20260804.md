# Independent audit: forced pull phases, last-ring basis, and finite-conjugate no-go

**Date:** 2026-08-04  
**Method:** independent symbolic proof audit; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_FORCED_PULL_PHASE_LAST_RING_BASIS_AND_CONJUGATION_NOGO_20260804.md`  
**Verdict:** `GO_AFTER_CORRECTION` in the theorem's declared fixed,
pairwise-support-disjoint, tree-compatible pull-system scope.

The mathematical core is correct.  This audit found and corrected one real
omission in the typed-cap paragraph: the original version required the forced
labels `A_D` to preserve the fixed typed state but did not impose the same
requirement on the final ring pull `g`.  The corrected theorem requires the
whole forced family `J_D=A_D\cup\{g\}` to be jointly valid and defines the
residual forbidden set outside `J_D`.  The tree-compatibility hypothesis was
also rewritten explicitly in component-count form, removing an ambiguity in
the phrase "contracting `A` in `H`."

## 1. Exact scope of the result

The theorem is conditional on one fixed pull host with two strong properties:

1. complete physical pull supports are pairwise edge-disjoint; and
2. every graphic forest of pull labels is physically compatible, with one
   factor component for each connected component of `(V(H),A)`.

Under these hypotheses a forest of `t` labels merges exactly `t` base-factor
components.  This component correspondence, rather than mere connectivity of
the quotient multigraph `H/A`, is what proves the two-component assertion
after deleting the final tree label.

Nothing in the theorem proves that an independently constructed reservoir or
typed cap admits such a host.  The result is an exact test *after* the pull
system and protected occurrence bank are fixed.

## 2. Forced-phase normal form

Let `D` be disjoint from the distinguished pull support `Z_g`.  Split its
edges into old factor edges and nonfactor edges.

For `p\in D\setminus F_0`, accessibility says that `p` lies in some `N_e`,
`e\ne g`.  Pairwise disjointness of complete supports makes this label unique.
Therefore every pull set producing `D` contains every label in

\[
 A_D=\{e\ne g:D\cap N_e\ne\varnothing\}.
\]

For `p\in D\cap F_0`, the edge survives a selected family `A` exactly when
no `O_e`, `e\in A`, contains it.  A different pull cannot reinstall it:
`p\in F_0`, every `N_f` is disjoint from `F_0`, and complete supports are
pairwise disjoint.  Consequently

\[
 D\subseteq F_A
 \iff
 \bigl[D\text{ accessible},\ A_D\subseteq A,\
 D\cap O_e=\varnothing\ (e\in A)\bigr].
\]

If `D` is accessible and phase-consistent, choosing `A=A_D` proves
sufficiency.  Conversely every cover contains `A_D`.  Hence `A_D` is the
unique inclusion-minimal pull set, and a forest cover exists exactly when
`A_D` itself is a graphic forest.  No additional phase choice remains.

## 3. Graphic basis and contracted connectivity

Put `J_D=A_D\cup\{g\}` and let `B_D` contain precisely the residual labels
whose old phases delete protected old edges.

### Necessity

If a spanning tree `T` contains `J_D` and avoids `B_D`, then `J_D\subseteq T`
is a forest.  Contracting `J_D` in `T` gives a spanning tree of
`(H-B_D)/J_D`, so that quotient is connected.

### Sufficiency

If `J_D` is a forest and `(H-B_D)/J_D` is connected, take a spanning tree of
the quotient and lift its nonloop representatives.  Their union with `J_D`
has

\[
 |J_D|+\bigl(|V(H)|-|J_D|-1\bigr)=|V(H)|-1
\]

edges, is connected, and is acyclic; it is therefore a spanning tree of
`H-B_D` containing `J_D`.  This proves both the basis-extension statement and
the equivalent graphic-rank formula

\[
 r_{\rm gr}^{H/J_D}
 \bigl(E(H)\setminus(B_D\cup J_D)\bigr)
 =|V(H)|-1-|J_D|.
\]

Parallel edges and contraction loops cause no problem: a quotient spanning
tree ignores loops and one lifts one representative of each chosen edge.

The cut formulation is also exact.  Connectivity of `(H-B_D)/J_D` is
equivalent to every nontrivial partition of its contracted vertex set having
an edge outside `B_D` across the partition.

## 4. Exactly two components before the last ring pull

Let `T` be the spanning tree above and set `A=T\setminus\{g\}`.  Because `g`
is a tree edge, `(V(H),A)` has exactly two connected components.  The explicit
tree-compatibility hypothesis therefore gives exactly two physical factor
components in `F_A`, not merely at most two.

The forced-phase theorem applies to `A`:

- `A_D\subseteq A`;
- labels in `A_D` are phase-consistent;
- any other selected label meeting a protected old edge would lie in `B_D`,
  which `T` avoids.

Thus `F^- = F_A` contains `D`.  Since no selected support meets `Z_g`, it also
contains `O_g`.  Selecting `g` completes the tree, replaces `O_g` by `N_g`,
preserves `D`, and yields one Hamilton component.  The transition changes no
vertex and incurs no physical-length charge.

Conversely, any spanning-tree realization in this same static pull system
with `g` designated as its last edge must contain `A_D`, avoid `B_D`, and
contain `g`.  Hence its existence forces precisely the forest and quotient
connectivity conditions.  The claimed necessity is correctly limited to the
canonical last-`g` scheme; it does not cover arbitrary alternating circuits
or arbitrary Hamilton cycles.

## 5. Typed-cap correction

The original typed paragraph had a genuine logical gap.  A fixed common typed
state can survive all forced labels in `A_D` and still be destroyed by the
final pull `g`.  Moreover, allowing a forbidden set to contain `g` while also
contracting `J_D` in `H-B` makes the displayed quotient ill-defined.

The corrected formulation is exact:

1. `Theta` is a fully fixed occurrence-labelled state required in both ring
   phases;
2. the whole forced family `J_D`, including `g`, is jointly valid for it;
3. `B_{D,Theta}` is a subset of `E(H)\setminus J_D` containing every residual
   label that invalidates a named resource of `Theta`; and
4. `(H-B_{D,Theta})/J_D` is connected.

Then the same graphic-basis proof selects only residual labels preserving the
fixed state.  This is a sufficient one-state certificate.  It does not infer
the existence of `Theta`, a typed cap route, or simultaneous background
compiler compatibility.

## 6. Finite-conjugate aperture bound

At one lower vertex `I`, the base factor has two selected incidence edges.
Pairwise support disjointness permits at most one pull label through each of
those two edges, hence at most two labels can change the local wedge.  Its
state depends only on the chosen subset of those labels, so at most
`2^2=4` wedges are accessible in one pull system.  This argument is preserved
under conjugation.

For `s` conjugates, the union of accessible wedge sets therefore has size at
most `4s`; no disjointness between the `s` sets is assumed.  A rank-`(m-1)`
lower vertex has `m` owner neighbours and exactly `binom(m,2)` wedges.  If

\[
                         \binom m2>4s,
\]

some wedge `I+x,I+y` is absent from every conjugate.

The literal ring reconstruction is valid.  Choose `a\in I`, set
`B=I\setminus\{a\}` and the common ring label `b=x`, and put `y` immediately
before active label `a` in the cyclic ring order.  Then the protected old
hinge at `I=B+a` has owners

\[
 B+a+x=I+x,
 \qquad
 B+a+y=I+y.
\]

The complement of `B\cup\{a,x,y\}` has size `m-2`, so a third active label
exists for `m\ge3`.  A depth-`d` nonempty history partition exists when
`d\le m-2`.  Hence the ring is literal, and any phase cover of its protected
old phase would have to realize the omitted wedge.  Building the independent
clipped reservoir afterward does not change that hinge.

For the synchronous cyclic family, `s\le2m-1`, and

\[
 \binom m2>4(2m-1)
 \iff m^2-17m+8>0.
\]

The larger root of the quadratic lies strictly between `16` and `17`, so the
inequality holds exactly for every integer `m\ge17` in the relevant range.
Thus the claimed `4s` obstruction and the rotation no-go are correct.

## 7. Retained frontier

The audited theorem closes the static topology decision problem but does not
close the all-dimensional construction.  The unresolved positive theorem is
still to choose, in correlation,

- the ring and its clipped reservoir,
- an accessible phase-consistent forced forest,
- enough residual pull labels to retain contracted connectivity, and
- one common typed cap/background state preserved by every forced and
  residual pull.

The finite-conjugate result proves that rotating a fixed canonical pull system
cannot replace that joint choice.


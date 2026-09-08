# The strict direct-edgewise chain extends through child parameter six

Date: 2026-07-31  
Status: solver-produced finite certificate; independent literal replay;
positive chained evidence through ambient parameter seven; no all-parameter
existence theorem

## 0. Result

The strict direct-edgewise recursion of
`MATH_THEOREM_CATALAN_DIRECT_EDGEWISE_SIDE_LIFT_RECURSION_20260731.md`
has now succeeded at the next chained scale.  Starting from the same
authenticated child at parameter `n=3`, and feeding every output literally
into the next step, it succeeds at child parameters

\[
                             n=3,4,5,6.               \tag{0.1}
\]

The new `n=6 -> 7` step chooses

\[
 (M,N,P,C,R)=(924,792,495,429,363),                  \tag{0.2}
\]

uses `|Q|=429`, selects `495` strict upper lifts and `495` strict lower
projections, and produces an exact `Cat_7=429`-path Catalan linear forest
on the parameter-seven middle layer.

This is materially stronger than four unrelated finite examples: the child
for every row after the first is exactly the physical output of the
preceding row.  It is still finite evidence.  The uniform coupled
common-basis/representative/graphic theorem remains open.

## 1. Search ledger

The remote CPU search used the same encoding and lazy literal cycle cuts as
the retained `n=3,4,5` chain.  The exact rows are

\[
\begin{array}{c|rrrrrrr}
n&|Q|&|S^-|&|S^+|&\#\text{paths}&\text{cycle cuts}&
 \text{variables}&\text{clauses}\\ \hline
3&14&6&6&14&1&75&421\\
4&42&28&28&42&1&392&3289\\
5&132&120&120&132&0&1890&21312\\
6&429&495&495&429&11&8712&123361.
\end{array}                                           \tag{1.1}
\]

The final row required eleven genuine cycle cuts.  Thus separate palette
feasibility does not make the graphic row automatic even in the positive
chain.

## 2. Independent replay

The replay does not trust the claimed palettes or topology.  For every
row it reconstructs all child atoms, validates every selected lift and
projection from its parent edge and coordinate, and checks:

* exact child lower and upper palettes;
* exact punctured middle and extreme side palettes;
* injective physical tail/head roles and seam-anchor caps;
* both side forests and the contracted three-rail forest;
* the complete ambient lower and upper palettes;
* maximum ambient degree two, zero cycle rank, and the Catalan component
  count; and
* literal chaining of each output into the next input.

The final authenticated row is

\[
 \boxed{\text{ambient components}=429,\quad
        \Delta=2,\quad \text{cycle rank}=0.}          \tag{2.1}
\]

## 3. What did not propagate

The earlier chain happened to have no anchor-free upper side component
through child `n=5`, and only `0,1,2` anchor-free lower components.  That
was never imposed.  At child `n=6` the two exact histograms are

\[
 (c_0,c_1,c_2)^-=(12,141,144),\qquad
 (c_0,c_1,c_2)^+=(16,133,148).                       \tag{3.1}
\]

They satisfy the exact charge law

\[
                 c_2-c_0=\operatorname{Cat}_6=132,  \tag{3.2}
\]

but refute the tentative propagation guess that one shore remains
rooted/no-empty automatically.  The central DERF construction survives;
the stronger rooted-side state does not survive this unconstrained choice.

This sharpens the next theorem.  One must either impose the rooted-tree
graphic base jointly, tolerate and route a controlled empty-component bank,
or use a different recursively preserved topology state.  The positive
central certificate alone does not choose among those options.

## 4. Artifacts and scope

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
scratch/audit_catalan_direct_edgewise_side_lift_n3_n6_20260731.py
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.audit.json
```

The witness was produced remotely; the audit is a separate standard-library
consumer.  Their SHA-256 hashes are, respectively,

```text
220994673d2b6f091c8c3493c4ef82023770211ca38df2548eace392a8efa26d
f824304ffb8ff59db8fac86d71542521bd7436a8c3806114864edf100d0a0ed5
69e95c7635d2d99d75af17994394212037b3bb2a95591fcd8a4567ba97d2e173
```

The audit payload hash is

```text
e7a8a2b8382271e2942f0e5aef522dd683abffd0af1772d71d3eb5065bd0946a
```

No residence, deep-shadow, compiler, or all-`n` claim is made here.

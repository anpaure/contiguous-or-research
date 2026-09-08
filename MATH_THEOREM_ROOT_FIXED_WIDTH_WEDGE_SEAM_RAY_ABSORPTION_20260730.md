# Fixed-width wedge cuts are repaired at every upper depth by one facet seam

Date: 2026-07-30  
Status: proof; upper-shadow statement only.  Component/facet-socket
existence, seam residence, middle ownership, and the lower compiler remain
separate.

## 1. Setting

Let

\[
C=(A_0,A_1,\ldots,A_{N-1})
\]

be a directed simple cycle in `J(k,r)`.  Write
`e_i=A_i A_(i+1)`, cyclically.  A directed `q`-edge witness of an upper
target `Y` is

\[
 A_s,A_{s+1},\ldots,A_{s+q},\qquad
 Y=\bigcup_{j=0}^{q}A_{s+j},\quad |Y|=r+q.
\tag{1.1}
\]

The rank equality makes the interval geodesic: each of its `q` transitions
introduces one element not previously present in the interval union.

Assume there is a wedge at `A_i`:

\[
 U=A_{i-1}\cup A_i=A_i\cup A_{i+1},\qquad |U|=r+1.
\tag{1.2}
\]

Cut the **right flank** `e_i`.  The resulting directed path starts at

\[
 S=A_{i+1}
\]

and ends at

\[
 E=A_i.
\]

Let `B` be an `r`-set, supplied as the end of the preceding opened
component, satisfying the facet-socket equation

\[
                         B\cup S=U=E\cup S.          \tag{1.3}
\]

Since `B` and `S` are distinct `r`-facets of the `(r+1)`-set `U`, the new
seam `B--S` is automatically a Johnson edge.

## 2. The simultaneous ray-repair theorem

### Theorem 2.1

Every fixed-width geodesic witness on `C` survives the cut-and-seam
operation.  More precisely, let (1.1) be a selected `q`-edge witness.

* If its edge span avoids `e_i`, it remains an internal path interval.
* If its edge span contains `e_i`, then it is necessarily

  \[
  A_i,A_{i+1},\ldots,A_{i+q},                         \tag{2.1}
  \]

  and the new seam-crossing interval

  \[
  B,A_{i+1},\ldots,A_{i+q}                            \tag{2.2}
  \]

  has exactly the same union.

Consequently one facet seam restores, simultaneously, every selected upper
witness of every depth that crossed the cut.

#### Proof

Only the second case needs proof.  A directed `q`-edge interval containing
the right wedge edge `e_i` cannot also contain the left wedge edge
`e_(i-1)`: across the two wedge transitions one insertion repeats an element
already present, so an interval containing both has union rank at most
`r+q-1`, contradicting `|Y|=r+q`.

A directed `q`-edge interval containing `e_i` but not its immediate
predecessor `e_(i-1)` must start at `A_i`; hence it is (2.1).  Using (1.3),

\[
\begin{aligned}
B\cup A_{i+1}\cup\cdots\cup A_{i+q}
 &= (B\cup S)\cup A_{i+2}\cup\cdots\cup A_{i+q}\\
 &= (E\cup S)\cup A_{i+2}\cup\cdots\cup A_{i+q}\\
 &= A_i\cup A_{i+1}\cup\cdots\cup A_{i+q}=Y.
\end{aligned}
\]

Thus (2.2) is a replacement witness of the same width and value. QED.

The left-flank form is the reversal of the theorem: after cutting
`e_(i-1)`, a successor endpoint `D` with
`A_(i-1) union D=U` restores every left outward ray.

## 3. Factor-wide corollary

### Corollary 3.1 (assigned fixed-width tower)

Let a factor have components `C_1,...,C_b`.  For every upper target `Y` of
rank `r+q`, assign one directed `q`-edge witness on one component.  On every
component choose a wedge and cut its right flank, obtaining start `S_a`, end
`E_a`, and wedge union `U_a=E_a union S_a`.

Suppose the opened paths can be cyclically ordered so that

\[
                 E_{a-1}\cup S_a=U_a                 \tag{3.1}
\]

for every `a` (indices cyclic).  Then concatenating them with these seams
preserves at least one witness of **every upper target**.

#### Proof

Apply Theorem 2.1 to the assigned witness on its provider component.  It is
either untouched or repaired by that component's incoming seam. QED.

This conclusion is stronger than old-witness `(PWI)`: the seam is allowed to
create the replacement witness, which `(PWI)` deliberately ignores.

### Corollary 3.2 (linear opening with one distinguished safe cut)

Order the opened paths linearly as `C_1,...,C_b`.  Suppose the selected
witness of every upper target assigned to `C_1` avoids the cut of `C_1`, and
suppose

\[
                 E_{a-1}\cup S_a=U_a
                 \qquad(2\le a\le b).                \tag{3.2}
\]

Then the linear concatenation preserves every assigned upper target.

#### Proof

Assigned witnesses on `C_1` remain internal by hypothesis.  For each later
component, Theorem 2.1 repairs every assigned witness intersecting its cut at
the incoming seam; the others remain internal. QED.

Thus a two-component construction needs one genuinely safe distinguished
cut and one facet socket, rather than two independently safe cuts.  This is
the precise shape seen in the existing big-cycle/small-cycle seam analyses.

## 4. Exact remaining interface

For opened-component options, define a directed socket edge

\[
 (a,\text{cut})\longrightarrow(c,\text{cut})
 \quad\Longleftrightarrow\quad
 E_a\cup S_c=U_c.                                    \tag{4.1}
\]

A directed cycle through one option from each component gives the upper-safe
**cyclic** concatenation of Corollary 3.1.  To obtain a linear carrier word,
one must still choose a final opening whose lost witnesses survive elsewhere,
or instead use the distinguished-safe-cut chain of Corollary 3.2.  Thus,
under a fixed-width assigned tower,
the upper gate is no longer a kernel-dispersion inequality; it is a finite
facet-socket matching/cycle problem.

What this theorem does **not** prove:

1. that the protected factor has a wedge option on every component;
2. that the socket graph has the required component-spanning directed cycle;
3. that the new seams preserve the minimum coordinate residence condition;
4. that the lost lower `q=1` colours are boundary-absorbable;
5. that the lower COMP_d Hall system is feasible.

For `b<=2`, item 4 has the familiar capacity of at most two cut colours, but
its eligibility and the compiler must still be checked.  The mathematical
gain is exact: once (4.1) and the fixed-width witness assignment hold, no
additional upper-shadow SPILL estimate is needed at any depth.

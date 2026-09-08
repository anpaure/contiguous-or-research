# The coatom U5 native columns, the q1 hinge, and the exact return-Hall gate

Date: 2026-08-01  
Lane: Thread D, additive-constant coatom tensor  
Status: exact local column calculation, exact alternating-return reduction,
and a local trace-guarded no-go.  Exterior return cells remain a live global
construction input.  No `B(k)+O(1)` theorem is claimed.

## 0. Verdict

The two lower-support chains in the mixed coatom tensor do have literal
maximal-erosion cells.  Their phase change has a particularly simple
exchange graph:

* at every depth `2<=q<=d`, two native cell columns join one old-only target
  to its corresponding new-only target;
* at depth one, the two targets are common and the two columns swap them,
  forming one closed two-column hinge; and
* after one phase-zero compiler matching is fixed, all remaining U5 work is
  exactly one bipartite return matching.  Its deficiency is the number of
  open alternating components.

This does **not** close locally.  In the planted maximal-erosion word, every
apparently eligible return cell fails the middle-row trace guard: capping it
deletes a complete maximal-erosion occurrence of one filler coordinate.
This failure is monotone under further caps.  Consequently the exact local
return graph is empty and

\[
                    \delta_{\rm ret}=2(d-1).                    \tag{0.1}
\]

The q1 hinge contributes no endpoint.  Thus the hoped-for local ladder with
`O(1)` endpoint deficiency is false.  The exact live theorem is instead:
construct invariant **exterior** return cells whose return graph has
absolute Hall deficiency.  If its deficiency is `t`, the exchange consists
of cycles and `t` paths; there are `t` unmatched lower obligations in the
new phase, or two banks of `t` boundary targets if both orientations must be
exported simultaneously.

This replaces the former fail-closed declaration `A_tau=emptyset` by an
explicit native-column/return-graph interface.  It does not manufacture a
positive return edge.

## 1. Literal native cells

Use the canonical active row

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab
```

with union screens at zero-based transitions `{1,3,5,7}`.  Put

\[
 I=\{\infty,c\},\qquad V_0=I\cup\{b\},\qquad
 V_1=I\cup\{a\}.                                                \tag{1.1}
\]

The active block at index five is `V_0` in phase zero and `V_1` in phase
one; the next active block has the opposite label.  Let

\[
 B=5(d+3),\qquad u=B+d+2=6d+17                                  \tag{1.2}
\]

be respectively the start of block five and its following screen in the
middle-owner chronology.  Let the canonical backward maximal erosion be

\[
 E_p^\epsilon=\bigcap_{i=p-d}^{p}T_i^\epsilon                   \tag{1.3}
\]

at an interior source position.  Boundary truncation is irrelevant here.

For `2<=q<=d`, write `h=d-q+1` and define the two physical compiler cells

\[
 C_q^-=[u,u+d-q],\qquad C_q^+=[u+q,u+d].                         \tag{1.4}
\]

Both have length `h`.  Direct coatom intersection gives

\[
\begin{aligned}
 E^\epsilon(C_q^-)
   &=K\cup V_\epsilon\cup\{f_1,\ldots,f_h\},\\
 E^\epsilon(C_q^+)
   &=K\cup V_{1-\epsilon}\cup
                  \{f_{d-h+1},\ldots,f_d\}.                    \tag{1.5}
\end{aligned}
\]

Here `E(C)` denotes the union of the maximal-erosion letters on the cell.
These are exactly the two values in the lower-exposure formula.  Indeed the
corresponding owner windows are `[u-q,u]` and `[u,u+q]`.  On this
depth-`d` resident fragment the morphological identity

\[
 \bigcap_{i=a}^{b}T_i=\bigcup_{p=b}^{a+d}E_p
 \quad\text{when }b-a=q\le d                                  \tag{1.6}
\]

gives (1.4): every positive run meeting either short owner window has length
at least `d+1`, and hence contains one of the erosion windows in the displayed
source interval.  Thus the displayed cells are literal compiler addresses, not
Johnson coordinate labels.

At `q=1`, put

\[
 C_1^-=[u,u+d-1],\qquad C_1^+=[u+1,u+d].                        \tag{1.7}
\]

There are only two target values at this level:

\[
 U=K\cup V_0\cup\{f_1,\ldots,f_d\},\qquad
 V=K\cup V_1\cup\{f_1,\ldots,f_d\}.                            \tag{1.8}
\]

Phase zero assigns `(C_1^-,C_1^+)` to `(U,V)`, while phase one assigns them
to `(V,U)`.  This is the q1 hinge.

## 2. The native exchange graph

For `2<=q<=d`, denote the values in (1.5) by

\[
 A_q^\epsilon=E^\epsilon(C_q^-),\qquad
 B_q^\epsilon=E^\epsilon(C_q^+).                                \tag{2.1}
\]

The four values at a fixed `q` are distinct, and the old/new support
difference is exactly

\[
 \{A_q^0,B_q^0\}\quad\longleftrightarrow\quad
 \{A_q^1,B_q^1\}.                                               \tag{2.2}
\]

Represent one physical column by an edge joining its phase-zero target to
its phase-one target.  The native exchange graph is then

\[
 \{A_q^0A_q^1,B_q^0B_q^1:2\le q\le d\}
 \quad\dot\cup\quad
 \{UV,UV\}.                                                     \tag{2.3}
\]

Hence it consists of `2(d-1)` isolated deep rungs and one doubled q1 edge.
The doubled edge is already an alternating cycle.  In particular, the
nested set containments by themselves do not join the deep rungs into a
ladder.

## 3. Exact return-Hall theorem

Let

\[
 O=\{A_q^0,B_q^0:2\le q\le d\},\qquad
 N=\{A_q^1,B_q^1:2\le q\le d\},qquad m=2(d-1),                 \tag{3.1}
\]

and let `pi:O->N` be the native pairing in (2.3).  Fix a phase-zero
trace-guarded compiler matching with the following decomposition:

1. every `o in O` uses its native cell `c_o`;
2. every `n in N` uses a nonnative cell `e_n`; and
3. `U,V` use the two q1 native cells.

The cells `e_n` may lie outside the packet.  They are the only possible
return bank after the native columns are switched in phase one.  Assume that
all retained return incidences, together with the fixed native incidences,
belong to one complete co-selectable trace-guarded bank.  This is the
load-bearing hypothesis which makes every marginal matching a simultaneous
common-cap solution.  Define the return graph

\[
 \mathcal R\subseteq O\times N,qquad
 o\sim n
 \quad\Longleftrightarrow\quad
 e_n\text{ is a trace-guarded legal cell for }o
 \text{ in phase one}.                                         \tag{3.2}
\]

All incidences in (3.2) belong to that one bank and include the exact
middle-row, fixed-pin, residence, and common-cap trace guards.  Envelope
containment alone is not an edge.  Without a complete guarded bank, (3.3)
is only the marginal matching gate and the residual conflict hypergraph must
be imposed separately.

### Theorem 3.1 (phase exchange equals return Hall)

Keeping the same physical cell basis, there is a phase-one matching which
uses `c_o` for `pi(o)`, swaps the q1 cells, and saturates every target if and
only if `mathcal R` has a matching saturating `O`.  More generally the
minimum number of old deep targets left unmatched is

\[
 \boxed{
 \delta_{\rm ret}=m-\nu(\mathcal R)
 =\max_{X\subseteq O}\bigl(|X|-|N_{\mathcal R}(X)|\bigr).}       \tag{3.3}
\]

The union of the two phase assignments decomposes into alternating cycles
and `delta_ret` alternating paths.  The q1 hinge is one closed alternating
cycle and contributes zero to (3.3).  Each path has one old and one new
target endpoint.  Thus one chosen orientation has exactly `delta_ret`
unmatched target obligations; a phase-independent exported endpoint bank
has two shores of size `delta_ret`.

#### Proof

In phase one, assigning every native cell `c_o` to `pi(o)` saturates `N`
and frees exactly the cells `{e_n:n in N}`.  The only remaining obligations
are `O`.  Assigning those obligations injectively to the freed cells is
precisely a matching in (3.2).  This proves the equivalence.  The deficient
formula is Hall's theorem.

Compose the fixed native bijection `pi` with any maximum partial return
matching.  The resulting directed partial permutation has indegree and
outdegree at most one, hence consists of cycles and paths.  Its unmatched
left and right shores both have size `delta_ret`.  The two q1 columns swap
`U,V` and form their own cycle, so they add no path endpoint.  \(\square\)

An alternating ladder with `O(1)` endpoint deficiency is therefore neither
a metaphor nor a scalar-capacity assertion: it is exactly the rank bound

\[
                  \nu(\mathcal R)\ge2(d-1)-O(1).                \tag{3.4}
\]

## 4. Why the planted maximal erosion supplies no return edge

There is a tempting unguarded picture.  For each opposite-phase target, the
maximal-envelope containment test produces `1+binom(q,2)` proper-prefix
cells.  Their interval incidences form nested fans, and one can draw a
width-plus-one return ladder.  Every one of those incidences is false in the
exact physical compiler.

It is enough to treat an old target in the new phase; phase symmetry gives
the converse.  The classification below is exhaustive.

### Lemma 4.1 (prefix-chain trace obstruction)

For the old prefix target

\[
 S_q^-=K\cup V_0\cup\{f_1,\ldots,f_{d+1-q}\},                  \tag{4.1}
\]

every maximal-envelope cell containing `S_q^-` in the new phase is one of
the following.

1. The right q1 hub, with source cell `[u+1,u+d]`.  Capping it to
   `S_q^-` deletes `f_d`.  The middle
   `f_d`-run is `[u-1,u+d]`, so its maximal-erosion run
   `[u+d-1,u+d]` lies wholly in the capped source cell.
2. An internal `V_0` tail-coatom cell.  More precisely, choose

   \[
    1\le q'\le q-1,\qquad d+2-q\le s,qquad s+q'\le d+1,         \tag{4.1a}
   \]

   where `s,...,s+q'` is the corresponding owner subwindow in the right
   coatom block.  Its source cell is

   \[
                 [u+1+s+q',\ u+1+s+d].                          \tag{4.1b}
   \]

   Capping it deletes `f_0`.  The
   middle `f_0`-run is `[u+2,u+d+3]`, so its maximal-erosion run
   `[u+d+2,u+d+3]` lies wholly in the capped source cell.

In either case some derivative window loses the displayed filler, and
`D^dA=T` fails.

### Lemma 4.2 (suffix-chain trace obstruction)

For the old suffix target

\[
 S_q^+=K\cup V_1\cup\{f_q,\ldots,f_d\},                        \tag{4.2}
\]

every containing cell is one of the following.

1. The left q1 hub `[u,u+d-1]`, whose cap deletes `f_1`.  The middle `f_1`-run
   `[u-d,u+1]` has maximal-erosion run `[u,u+1]` wholly inside the cell.
2. An internal `V_1` head-coatom cell.  Choose

   \[
       1\le q'\le q-1,\qquad 0\le s,qquad s+q'\le q-1,          \tag{4.2a}
   \]

   in the left coatom block.  With `B=u-d-2`, its source cell is

   \[
                         [B+s+q',\ B+s+d].                       \tag{4.2b}
   \]

   Its cap deletes `f_(d+1)`.  The
   middle run `[u-d-3,u-2]` has maximal-erosion run `[u-3,u-2]` wholly
   inside the cell.

Again `D^dA=T` fails.

#### Proof of Lemmas 4.1--4.2

Inside a constant active block, maximal-erosion supports are consecutive
one- or two-filler intervals.  Active containment first forces the target
to the unique block carrying its active triple.  Filler containment then
leaves the q1 hub and the indicated head/tail coatom intervals; this gives
`1+sum_(q'=1)^(q-1)(q-q')=1+binom(q,2)` candidates.  Direct
substitution of the coatom order gives
the four middle runs displayed above.

For a middle positive run `[a,b]`, its backward maximal-erosion run is
`[a+d,b]`.  If a cap omits that coordinate on an interval containing this
whole erosion run, the corresponding middle row cannot recover it.  This is
also exactly the mandatory-core condition `F(J) subseteq S` in the
run-boundary compiler theorem.  The four containments above therefore rule
out every candidate.  Reversing the two phases exchanges `a,b` and changes
none of the filler-run arguments.  \(\square\)

Further caps cannot repair these failures: maximal common caps only
intersect source letters and hence only delete coordinates.  They cannot
restore a filler already absent from all `d+1` source letters of a middle
row.

### Corollary 4.3 (exact local Hall obstruction)

Let `R_loc` use every proper-prefix maximal-erosion cell wholly inside the
planted tensor and retain only literal trace-guarded return incidences.  Then

\[
                         E(R_{loc})=\varnothing,                 \tag{4.3}
\]

and every single deep target is a zero-neighbour Hall witness.  Consequently

\[
                      \nu(R_{loc})=0,
               \qquad\delta_{ret,loc}=2(d-1).                   \tag{4.4}
\]

This is stronger than the unguarded two-hub/fan deficiency.  The smallest
obstruction already occurs at `d=2,q=2`.

## 5. Exact surviving construction gate

The local no-go does not rule out the coatom tensor.  It says exactly what a
regenerative embedding must export.

1. Plant the native columns (1.4), including the closed q1 hinge.
2. Choose a phase-zero compiler matching and record the actual exterior
   cells `e_n` serving the opposite deep bank.
3. Build the literal trace-guarded return graph (3.2), including every
   middle-row and fixed-pin guard.
4. Prove (3.4), ideally with deficiency zero; then toggle the corresponding
   alternating cycles/paths.

Equivalently, before a phase-zero matching is fixed, one needs a joint
three-shore selection of native tasks, exterior return cells, and lower
targets.  Separate marginal matchings do not imply (3.3).  A nonflat source
rethread which creates new filler occurrences may also evade Lemmas
4.1--4.2, but then `D^dA=T`, upper support, and residence must be replayed on
that new word.

Thus the sharp current statement is

\[
 \boxed{\text{native phase columns and q1 hinge: exact; }\quad
        \text{local return ladder: impossible; }\quad
        \text{exterior return Hall: open}.}                       \tag{5.1}
\]

Dependencies:

* `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`;
* `MATH_THEOREM_K_ZERO_OWNER_COATOM_U5_REGENERATIVE_RECURRENCE_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_UNUSED_BASIS_FRONTIER_MATCHING_AND_MOBILITY_20260731.md`;
* `MATH_THEOREM_PROSPECTIVE_COMMON_BASIS_AVOIDANCE_AND_COMPILER_DUAL_RADO_20260731.md`; and
* `MATH_THEOREM_K_ALLK_SCARCE_FIRST_PORT_HALL_AND_POSITIVE_DENSITY_COMPILER_20260730.md`.

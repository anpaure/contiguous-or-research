# Paste-ready MASTER integration: structured Gate-C offset tracks

This is an integration prescription only.  It does not modify
MASTER_HANDOFF.md.  Equation labels begin after the current Appendix-I label
I.22.

## A. Insertion anchors and ledger edits

### A.1 Central status

Insert the following bullet immediately after the central-status bullet
beginning “[I] For fragments, Appendix I proves exact degree”.

> - **[I]/[C]/[O]** The fragment band is not a collection of generic
>   rank tokens.  Appendix I.6 proves that every lower/upper band color is
>   exactly the intersection/union of two nearby middle windows.  Abstractly,
>   one nested flag through every middle set can always be chosen with
>   optimally balanced loads at every band rank, but independent choices are
>   asymptotically nonserializable.  Appendix I.8 gives a sharper sufficient
>   Gate-C antecedent: a matching of extended middle-window tracks leaving
>   \(o(Wb^{-1/3})\) middle vertices and having aggregate offset-color
>   overflow \(o(W)\).  Small annealed influence
>   \(O(H/b+LH/b^2)\) is not a quenched nibble hypothesis, because exposed
>   neighboring windows can determine an offset color with probability one.

### A.2 Architecture ledger

Keep the existing whole-atom row.  Replace the existing logarithmic-fragment
row by these two rows.

| layer | status | exact remaining content |
|---|---|---|
| logarithmic fragment quota compiler | [C] | correlated integral selection with aggregate band overflow \(o(W)\); disjoint domains and \(L\gg bH\) are unnecessary |
| structured extended-track compiler and abstract balanced flag flow | [I]/[C] | product-specific extended-track matching leaving \(o(Wb^{-1/3})\) middle vertices and aggregate intersection/union-color overflow \(o(W)\) |

### A.3 Gate C

In Section “Gate C: coherent atom/product serialization”, replace the first
four paragraphs, ending with “small pair parameter proves this correlated
assertion”, by the following.

> Appendix I closes literal serialization and support overlap once a suitable
> correlated selection is supplied.  Any one of the following **alternative
> sufficient antecedents** would finish Gate C:
>
> 1. select \(\lceil W/b^2\rceil\) phase-refined whole atoms with aggregate
>    Gaussian-band overflow \(o(W)\);
> 2. for \(g\ll L\ll W\), select \(\lceil W/L\rceil\) labelled fragments
>    with aggregate designated-token overflow \(o(W)\); or
> 3. at \(L\asymp b\log b/\log\log b\), select a matching of
>    \(K=L+2H\) extended middle-window tracks which leaves
>    \(o(Wb^{-1/3})\) middle vertices and whose induced nearby-window
>    intersection/union colors have aggregate balanced-quota overflow
>    \(o(W)\).
>
> These are not asserted to be equivalent selection theorems.  They are
> separate sufficient inputs to internally proved compilers.  Equal total
> mass makes one-sided overflow pay for holes, and separate singleton-block
> linearization prevents overlapping target domains from creating a physical
> conflict.
>
> The third formulation exploits additional structure.  Every band token is
> an intersection or union of two nearby middle windows, and an abstract
> optimally balanced nested-flag bank always exists by integral flow.
> Nevertheless independently choosing its columns leaves only \(o(W)\)
> columns incident with a FIFO-compatible neighbor.  The natural independent
> overlap ledger \(O(H/b+LH/b^2)\) is only annealed: after neighboring middle
> windows are exposed, some offset colors are deterministic.  Appendix C.6
> also rules out a growing-rank matching theorem based only on regularity,
> maximum codegree, and squared local influence.  Thus the remaining
> obstruction is a product-specific correlated track matching or an
> equivalent conditional expansion theorem, not generic quota integrality,
> domain disjointness, or a black-box nibble.

Leave all subsequent older-route paragraphs beginning “Appendix F records”
unchanged.

### A.4 Appendix insertion

In the current final paragraph of I.5, replace
“The exact remaining Gate-C statement is one of the following equivalent
compiler antecedents” by
“The whole-atom and fragment compilers have the following alternative
sufficient antecedents”.  Replace its final sentence
“This is now the sole product-atom selection obstruction; support overlap and
serialization are already paid for by (I.10) or (I.18)” by
“This is an open product-atom selection obstruction; support overlap and
literal block serialization are already paid for by (I.10) or (I.18), and
I.8 below gives a third structured sufficient antecedent.”

Insert Sections I.6–I.8 from Part B below immediately after the current final
paragraph of Appendix I.5.

### A.5 Reproducibility map

Insert this row after the existing fragment-compiler provenance row.

| result | complete proof in this file | optional frozen provenance |
|---|---|---|
| offset-pair structure, balanced flag flow, independent serialization obstruction, and extended-track compiler | Appendix I.6–I.8 | source SHA c18c4e7fa0d45c74e175ae18ddd548056ccff86a6a0c2e2cd13dc69aafbbba67; checker SHA 6c5e362fb8148f7e3602905727ff14b676f7146516d286aa1cf191de51a7e675 |

### A.6 Completion audit

Insert the following rows after the existing fragment row, and replace
“correlated integral atom/fragment quota selection” by “correlated integral
atom/fragment/extended-track selection”.

| requirement | evidence | state |
|---|---|---|
| exact offset intersection/union structure and optimally balanced abstract flag bank | Appendix I.6–I.7 | [I] |
| independent flag serialization and annealed-to-quenched overlap obstruction | Appendix I.7 | [I] |
| quantitative extended-track matching/overflow compiler | Appendix I.8 | [C] |
| product-specific extended-track matching leaving \(o(Wb^{-1/3})\) vertices with \(o(W)\) offset overflow | Gate C | [O] |

The final assembled-construction row and every existing [O] status remain
unchanged.

## B. Exact appendix text

### I.6 Nearby-window representation and abstract flag balance

Retain the phase-refined atom notation of I.2:
\[
 C_t=\{w_t,\ldots,w_{t+b-1}\},\qquad t\in\mathbb Z_{b^2}.
\]
For \(1\le q\le H\le b-2\), define its lower and upper offset colors
\[
 T_q^-(t)=\{w_t,\ldots,w_{t+b-q-1}\},\qquad
 T_q^+(t)=\{w_t,\ldots,w_{t+b+q-1}\}.                \tag{I.23}
\]
The recurrence-gap proof in I.2 says that every block of at most \(2b-2\)
emissions is injective.  Applying it to the positional unions of two
length-\(b\) windows gives the exact identities
\[
 \boxed{T_q^-(t)=C_{t-q}\cap C_t,\qquad
 T_q^+(t)=C_t\cup C_{t+q},\qquad d_J(C_t,C_{t+q})=q.} \tag{I.24}
\]
Indeed the first intersection is exactly the positional overlap; the second
union is the full positional span; and exactly \(q\) elements leave and
enter.  Thus the entire band ledger at the \(L\) core starts
\(a,\ldots,a+L-1\) is determined by the one extended middle track
\[
 C_{a-H},C_{a-H+1},\ldots,C_{a+L+H-1}.              \tag{I.25}
\]

A band flag through a middle set \(C\) is a nested sequence
\[
 S_{b-H}\subset\cdots\subset S_b=C\subset\cdots\subset S_{b+H}. \tag{I.26}
\]

**Balanced-flag theorem [I].**  One can choose one band flag through every
\(C\in{\Omega\choose b}\) so that, simultaneously at every controlled rank
\(s\), every \(s\)-set has load
\[
 \left\lfloor {W\over{2b\choose s}}\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil {W\over{2b\choose s}}\right\rceil.       \tag{I.27}
\]

For the lower half, take the layered containment digraph from rank \(b\)
down to rank \(b-H\).  Put
\(\mu_s=W/{2b\choose s}\) and give every rank-\(s\) node the integral
throughput interval
\([\lfloor\mu_s\rfloor,\lceil\mu_s\rceil]\); supply one unit at every
middle node.  The fractional flow which divides the \(\mu_s\) units at an
\(s\)-set equally among its \(s\) immediate subsets is feasible, because an
\((s-1)\)-set receives
\[
 {2b-s+1\over s}\mu_s=\mu_{s-1}.                    \tag{I.28}
\]
Split every node into an in-node and an out-node, with its throughput
interval on the joining arc.  After subtracting integer lower bounds this is
an ordinary capacitated circulation.  Directed incidence matrices are
totally unimodular: in any square submatrix, expand at a column with at most
one nonzero, while if every column has two nonzeros the row sum is zero.
Thus the feasible circulation has an integral point.  Decomposing its
acyclic part into unit paths gives one lower chain from each middle set and
the loads (I.27).  Reversing inclusions proves the upper half; pair the two
paths with their common middle source.

Every individual flag embeds in a phase-refined atom if \(H\le b-4\).
Order its \(b-H\) bottom elements arbitrarily, follow them by the \(H\)
central elements in their lower-chain order and then by the \(H\) upper
additions.  This is an injective prescribed sequence of length \(b+H\).
Assign its positions to shores using a translate of the type period in I.2.
In at most \(2b-4\) consecutive type positions neither type occurs more than
\(b\) times.  Fill each shore with the unused coordinates, extend the
encountered same-shore order to a cyclic order, and choose the corresponding
root-pair coset.  Equation (I.24) recovers the prescribed flag.  This proves
individual supply, not joint FIFO compatibility.

For comparison, choose two abstract flags independently and uniformly
through middle sets \(C,C'\) at Johnson distance \(d\).  Their lower
depth-\(q\) colors agree, and likewise their upper colors agree, with
probability
\[
 p_{q,d}=
 \begin{cases}
 \displaystyle{{b-d\choose q-d}\over{b\choose q}^2},&d\le q,\\
 0,&d>q.
 \end{cases}                                                   \tag{I.29}
\]
A common lower target is a \((b-q)\)-subset of \(C\cap C'\); a common
upper target is a \((b+q)\)-superset of \(C\cup C'\), giving the same
count.  For \(q\le(b-1)/2\),
\[
 p_{q,0}\le {1\over b},\qquad \max_{d\ge1}p_{q,d}\le {1\over b^2}. \tag{I.30}
\]
For the second inequality the numerator decreases with \(d\), and at
\(d=1\) the probability is \((q/b)/{b\choose q}\le1/b^2\), since
\({b\choose q}\ge bq\).  Summing both shores, one same-column and
\(L-1\) different-column comparisons therefore have annealed influence
\[
 O\!\left({H\over b}+{LH\over b^2}\right).            \tag{I.31}
\]
This is not a quenched estimate.  Equation (I.24), already at \(q=1\),
makes the offset color a deterministic function of two exposed neighboring
middle windows, so a corresponding conditional collision probability can
be one.

### I.7 Independent columns do not serialize

A band flag through one middle set has
\[
 R_H=(b)_H^2                                             \tag{I.32}
\]
representatives: order the \(H\) deleted central elements and the \(H\)
added outside elements.  Represent it by its bottom set \(R\) of size
\(b-H\), its ordered central tail \(u_1,\ldots,u_H\), and future entries
\(v_1,\ldots,v_H\).  A one-step FIFO successor is obtained by choosing
\[
 z\in R,\qquad
 v_{H+1}\in\Omega-(C\cup\{v_1,\ldots,v_H\}).           \tag{I.33}
\]
Its middle set, bottom, tail, and future are respectively
\[
 \begin{split}
 C'&=C-z+v_1,\qquad R'=(R-z)\cup\{u_1\},\\
 u'&=(u_2,\ldots,u_H,v_1),\qquad
 v'=(v_2,\ldots,v_H,v_{H+1}).
 \end{split}                                           \tag{I.34}
\]
Hence one flag has exactly \((b-H)^2\) compatible successor flags,
distributed \(b-H\) apiece over \(b-H\) successor middle sets.

If one flag is now chosen independently and uniformly through every middle
set, and \(Z\) counts directed compatible adjacencies, conditioning on the
flag at \(C\) gives
\[
 {\mathbb EZ\over W}={(b-H)^2\over(b)_H^2}.             \tag{I.35}
\]
For \(H\ge2\) this is at most \(1/(b-1)^2\).  The number \(I\) of selected
columns incident with any compatible adjacency satisfies \(I\le2Z\);
Markov at \(I/W=b^{-1/2}\) proves \(I=o(W)\) with probability \(1-o(1)\).
Thus marginally balanced independent columns are almost entirely
unserializable.

This also marks the limit of a parameter-only nibble.  Apply the
self-contained equipartition construction of Appendix C.6 with \(D\ge4\)
and \(r\ge64\log(2eDr)\).  It gives arbitrarily large \(r\)-partite,
\(r\)-uniform, \(D\)-regular multihypergraphs with \(\Delta_2\le2\).
For a fixed block vertex \(v\), write \(t_B\le2\) for its intersection
with a block \(B\) of another partition.  Since those blocks partition the
\(D\) points of \(v\), \(\sum_Bt_B=D\) and
\(\sum_Bt_B^2\le2D\).  Summing over the other \(r-1\) partitions gives
\[
 \Delta_2\le2,\qquad
 \max_v\sum_{w\ne v}
 \left({\operatorname{codeg}(v,w)\over D}\right)^2
 \le {2(r-1)\over D},                                  \tag{I.36}
\]
The common-partial-transversal calculation in C.6 says that a maximum
matching covers at most \(32\log(2eDr)/r\) of the vertices for all
sufficiently large instances.  Taking \(D=r^2\), and if desired
inflating every edge by parallel labelled copies, makes all normalized local
parameters tend to zero without improving the matching.  Consequently
(I.31), regularity, codegree, and absolute degree cannot alone imply the
needed track matching; a product-specific expansion or conditional-exposure
theorem is required.

### I.8 Extended-track compiler and exact open gate

Take
\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,\qquad
 K=L+2H,\qquad K\le b^2/2.                              \tag{I.37}
\]
For every labelled atom and core start \(a\), make the \(K\)-uniform
extended-track edge in (I.25).  There are \(W\widehat D\) labelled edges.
A middle target occurs in \(K\) starts in each atom through it, so its exact
degree is \(D_K=K\widehat D\).  Two distinct positions in one atom occur
together in at most \(K-1\) cyclic tracks.  Combining this with the
full-atom profile (I.14) gives
\[
 {\Delta_2\over D_K}\le {K-1\over K}{4\over b^2},
 \qquad {K\Delta_2\over D_K}\le{4K\over b^2}.           \tag{I.38}
\]

Choose a matching of \(t\) extended tracks and retain their \(L\) core
starts.  Put \(M=Lt=(1-\delta)W\).  For every \(s=b\pm q\),
\(0\le q\le H\), let \(a_s(T)\) be its offset-color load.  Choose balanced
quotas
\[
 q_s(T)\in\{\lfloor M/N_s\rfloor,\lceil M/N_s\rceil\},
 \quad N_s={2b\choose s},\quad\sum_Tq_s(T)=M,
\]
and put \(V_s=\sum_T(a_s(T)-q_s(T))_+\).
Unlike I.3–I.4, these quotas may be zero.  Equal total load and quota still
give
\[
 h_s\le(N_s-M)_++V_s.                                  \tag{I.39}
\]
Indeed positive-quota holes cost deficit, whose total equals \(V_s\), while
there are exactly \((N_s-M)_+\) zero quotas.

**Extended-track compiler [C].**  If
\[
 {b+H\over L}=o(1),\qquad
 \delta=o(b^{-1/3}),\qquad
 \sum_{s=b-H}^{b+H}V_s=o(W),                           \tag{I.40}
\]
then \(\nu(2b)=(1+o(1))W\).

For each selected track, write the singleton block
\(w_a,\ldots,w_{a+L+b+H-2}\).  Every core offset witness is internal to its
block, and the total length is
\[
 t(L+b+H-1)\le W+{W(b+H)\over L}=W+o(W).               \tag{I.41}
\]
The matching makes the \(M\) core middle colors distinct.  It remains to
bound the extra term in (I.39).  For \(q\ge1\),
\[
 {N_{b\pm q}\over W}
 =\prod_{i=0}^{q-1}{b-i\over b+i+1}
 \le e^{-q^2/(2b)}.                                    \tag{I.42}
\]
If \(N_{b\pm q}>(1-\delta)W\), then
\(q<2\sqrt{b\delta}\) for \(\delta\le1/2\).  Each positive deficit is at
most \(\delta W\), so
\[
 \sum_{s=b-H}^{b+H}(N_s-M)_+
 =O\!\left(W\delta(1+\sqrt{b\delta})\right)=o(W).       \tag{I.43}
\]
Equations (I.39)–(I.43) leave only \(o(W)\) band holes.  Append those holes
as set-valued letters.  The binomial tail proof in I.3 shows that the number
of outside-band targets is \(o(W)\), so append any of those still absent.
This proves the upper bound; the middle-layer ending-position argument in
I.3 proves the matching lower bound \(W\).

At \(L\asymp b\log b/\log\log b\), one has
\((b+H)/L=o(1)\), \(H/L=o(b^{-1/3})\), and the weighted pair parameter in
(I.38) is \(o(1)\).  If the matching leaves an \(\eta\)-fraction of middle
vertices, then
\[
 \delta=1-{L\over K}(1-\eta)=O(H/L+\eta).              \tag{I.44}
\]
The exact new sufficient Gate-C input is therefore
\[
 \boxed{\eta=o(b^{-1/3}),\qquad
 \sum_{s=b-H}^{b+H}V_s=o(W).}                          \tag{I.45}
\]
An unspecified \(o(1)\) matching leave is not enough for this proof.
Neither (I.38), the balanced flag theorem, nor the annealed ledger (I.31)
proves (I.45).  Grouping one flag column as a Greene--Kleitman chain changes
its internal representation but not the FIFO compatibility in (I.34).
Thus (I.45), or a different correlated selection satisfying I.9 or I.19,
is the exact open product-selection gate.

## C. Integration cautions

1. Do not replace the existing whole-atom or fragment compiler by the
   extended-track compiler; retain all three as alternative sufficient
   antecedents.
2. Do not label (I.31) as a conditional or quenched influence bound.
3. Do not say the balanced-flag theorem serializes its columns.
4. Do not weaken \(o(Wb^{-1/3})\) to \(o(W)\) in the extended-track gate.
5. Do not call Appendix C.6 a counterexample to the actual product-track
   hypergraph; it only rules out parameter-only matching theorems.
6. Preserve the finite breakthrough table verbatim.

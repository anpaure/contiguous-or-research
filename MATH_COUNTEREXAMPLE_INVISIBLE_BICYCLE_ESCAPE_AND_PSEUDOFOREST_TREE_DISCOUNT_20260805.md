# The unrestricted invisible-bicycle escape lemma is false

**Date:** 2026-08-05  
**Method:** a rooted capacity-two orientation cube, literal receiver
squares, and the exact edge-to-endpoint Hall deficiency; no computation  
**Status:** unconditional counterexample and corrected reduction.  The
counterexample has trivial rotational stabilizer, so it occurs before any
necklace coalescence.  A positive theorem below reduces the initially
packable case to one explicit tree-component escape inequality.

## 1. The claim being tested

For an even labelled capacity-two sector, let `G=(L,R;E)` be the ordinary
sector graph and let the paired-petal jobs have receiver rectangles

\[
                         A_j\mathbin\square B_j.
\]

For `U subseteq L`, put

\[
 D=N_G(U),\qquad J_U=\{j:A_j\cap U=\varnothing\},
\]

and form the residual endpoint multigraph `Q_U` from the lists
`B_j setminus D`, `j in J_U`.  The proposed invisible-bicycle escape
inequality was

\[
 \sum_{C\in\operatorname{Comp}(Q_U)}
       (|E(C)|-|V(C)|)_+
 \le |D|-|U|.                                      \tag{1.1}
\]

Equation (1.1) is not automatic for actual paired-petal rectangles.

## 2. A literal orientation cube inside one even sector

Use the labelled sector

\[
                         \mathcal T_{18,27}.
\]

Partition the eighteen cyclic coordinates into the nine consecutive
pairs

\[
 P_i=(2i,2i+1),\qquad 0\le i\le8.
\]

On each pair write

\[
 s_i(0)=12,\qquad s_i(1)=21.
\]

Fix the last pair in state `s_8(0)`.  On the first eight pairs allow both
states.  Thus

\[
 t(\epsilon)=s_0(\epsilon_0)\cdots s_7(\epsilon_7)s_8(0),
 \qquad \epsilon\in\{0,1\}^8,                       \tag{2.1}
\]

has total mass twenty-seven.  Flipping one bit of `epsilon` is exactly the
legal local move `12 <-> 21`, so (2.1) is an eight-dimensional cube in the
ordinary token sector.

The use of local mass three is essential for literal parent criticality.
Deleting the moved cut merges two child parts whose residue digits sum to
three; the merged macro part has residue

\[
                         4+4+3\equiv5\pmod6,
\]

and is therefore itself critical.  Thus every boundary edge of every
square below has a critical parent endpoint, exactly as required by the
paired-petal construction.

Group the first eight bits into four ordered pairs

\[
 G_g=(\epsilon_{2g},\epsilon_{2g+1}),\qquad0\le g<4.
\]

For each group use the two cross states

\[
                         0:=10,\qquad1:=01.           \tag{2.2}
\]

If all other bits are fixed, freeing the two bits of one `G_g` gives a
literal receiver square.  Designate its cross diagonal `10,01` as the
`B`-list and its other diagonal `00,11` as the `A`-list.  The two local
moves use disjoint coordinate boundaries, so this is precisely the
double-expansion square of a pair of endpoint-disjoint petals over their
common double-deleted hub.

There is no quotient issue hidden here.  Choose, for example, the critical
macro background

\[
                         a_i=2^i\qquad(0\le i<18).
\]

Then every macro part `6a_i+4+t_i` is critical, the total ambient length
is odd, and the superincreasing background has trivial stabilizer.  Its
adjacent merged background values are also distinct.  Hence all the rooted
states, deleted-edge hub colours, and squares above remain distinct after
passing to necklace orbits.

## 3. Eight jobs whose endpoint graph is a tight handcuff

Use the shorthand `x_0x_1x_2x_3` for the four group states in (2.2).
Select the four receiver squares whose `B`-diagonals are the edges of

\[
 0000-1000-1100-0100-0000,                           \tag{3.1}
\]

and the four receiver squares whose `B`-diagonals are the edges of

\[
 0000-0010-0011-0001-0000.                           \tag{3.2}
\]

Every displayed edge changes one group state and is therefore the cross
diagonal of the corresponding literal double-expansion square.

The eight squares have pairwise edge-disjoint boundaries.  Indeed,
consecutive squares meet only at their displayed cross-diagonal endpoint,
where they use disjoint coordinate-pair directions; opposite squares in
one four-cycle have different fixed context; and squares from (3.1) and
(3.2) use disjoint direction groups and meet only at `0000`.

The four deleted-edge hub colours of one receiver square are the four
endpoints of its two passive parent petals.  In this rooted construction
distinct square-boundary edges also have distinct deleted-edge states:
equal directions have different fixed contexts, while unequal directions
delete different marked coordinate boundaries.  The aperiodic background
prevents rotational identification.  Thus the sixteen passive parent
petal edges form a matching.

To realize the free-hub parity convention literally, give each of the
eight double-deleted hubs one additional active petal in a private split
block.  The superincreasing gaps may be chosen large enough to provide
these eight mutually disjoint blocks, compatible with all displayed cuts.
Their sixteen endpoints are fresh.  Each fan then has three petals: the
private petal is the fixed active anchor and the displayed two petals are
the unique passive pair.  Hence the eight squares are a legitimate fixed
passive-petal bank with no incoming-hub sidecar.

The resulting `B`-endpoint multigraph is exactly two four-cycles meeting
at the single vertex `0000`.  It has

\[
                              e=8,\qquad v=7,
\]

and hence bicircular surplus one.

Take `U=emptyset`.  Then `D=N_G(U)=emptyset`, every job is invisible, and
no endpoint is deleted.  Therefore

\[
 \sum_C(|E(C)|-|V(C)|)_+=1
 \quad\hbox{but}\quad
 |D|-|U|=0.                                          \tag{3.3}
\]

This contradicts (1.1).

The construction can be repeated on disjoint groups of eight orientation
bits.  All copies may share the all-zero group state because their
incident direction sets there are disjoint.  Consequently the unsupported
bicircular surplus can be made arbitrarily large while the empty-shore
ordinary slack remains zero.

### Theorem 3.1 (labelled counterexample)

The invisible-bicycle escape lemma is false for arbitrary actual
paired-petal banks, already in an even labelled capacity-two sector with
trivial rotational stabilizer.  Neither cross-hub geometry nor the absence
of quotient coalescence forces the initial receiver endpoint lists to be
bicircular-independent.

In particular, the one-unit strict Hall theorem cannot repair this
example: strict Hall concerns proper nonempty shore sets, whereas the
counterexample is the endpoint-packing cut `U=emptyset`.

## 4. The correct first premise: initial pseudoforest packing

For two-element endpoint lists, the empty-shore Hall row is equivalent to
saying that the full endpoint multigraph is a pseudoforest: every connected
component has at most one cycle.  Thus any positive escape theorem must at
least assume, or jointly construct, initial endpoint SDRs on both receiver
shores.

After that premise is imposed, there is a useful exact reduction for every
later deletion cut.

Let `Q` be any pseudoforest on an endpoint set `R`, with its edges carrying
the job labels.  Let `D subseteq R`.  An edge keeps the list of its endpoints
outside `D`; a one-element residual list is a loop and an empty list is a
zero-vertex edge component.  Let `delta_Q(D)` be the resulting transversal
deficiency.

For a tree component `T` of `Q`, put

\[
                         d_T=|D\cap V(T)|,
\]

and let `tau_Q(D)` be the number of tree components with `d_T>0`.

### Theorem 4.1 (pseudoforest tree discount)

If `Q` is a pseudoforest, then

\[
 \boxed{
 \delta_Q(D)
 \le |D\cap V(Q)|-\tau_Q(D).}                        \tag{4.1}
\]

The same bound holds after an arbitrary set of job edges is discarded.

#### Proof

Hall deficiency for the edge-to-endpoint incidence graph is

\[
 \delta_Q(D)=
 \max_{F\subseteq E(Q)}
       \bigl(|F|-|V(F)\setminus D|\bigr).             \tag{4.2}
\]

In a tree component, every nonempty `F` is a forest.  If it has `c(F)`
nontrivial components, then

\[
 |F|-|V(F)\setminus D|
   =|D\cap V(F)|-c(F)
   \le \max(0,d_T-1).                                 \tag{4.3}
\]

In a unicyclic component every subgraph satisfies `|F|<=|V(F)|`, so

\[
 |F|-|V(F)\setminus D|
   \le |D\cap V(F)|
   \le |D\cap V(C)|.                                  \tag{4.4}
\]

Deficiencies add over components.  Summing (4.3)--(4.4) gives (4.1).
Discarding edges leaves a pseudoforest and cannot invalidate either
componentwise estimate.  \(\square\)

## 5. The corrected proper-cut target

Return to a receiver Hall cut `U subseteq L`, and put `D=N_G(U)`.  Assume
the full `B`-endpoint graph `Q` was initially a pseudoforest.  Discard the
visible jobs; this can only improve Theorem 4.1.  Let

\[
 D_{\rm out}=D\setminus V(Q).
\]

Theorem 4.1 proves the desired invisible-job inequality whenever

\[
 \boxed{
 |D_{\rm out}|+\tau_Q(D)\ge |U|.}                    \tag{5.1}
\]

Indeed,

\[
 \delta_Q(D)
 \le |D\cap V(Q)|-\tau_Q(D)
 \le |D|-|U|.                                         \tag{5.2}
\]

Thus, after initial endpoint packing, every ordinary neighbour outside
the receiver endpoint bank and every touched tree component supplies one
unit of automatic escape.  Only deleted endpoints lying in unicyclic
receiver components fail to earn this discount.

Condition (5.1) is the sharpened remaining geometric statement.  It is
strictly stronger than ordinary strict Hall: `|D|>=|U|+1` counts endpoint
vertices, whereas (5.1) counts the resources which remain free after the
initial bicircular orientation.  Proving (5.1), or its exact matroidal
replacement, requires a correlated choice of the passive-petal pairing;
it does not follow from the labelled sector matching theorem alone.

## 6. Quotient boundary

The counterexample uses a trivial background stabilizer.  Therefore
periodic quotient folding is not the source of the failure and cannot be
used to repair the unrestricted statement.

For a semiregular odd quotient, the existing strict-Hall descent still
pays one surplus unit on every proper nonempty quotient cut.  It says
nothing about the empty-shore endpoint-packing row and nothing about two
or more surplus units.  In nonsemiregular periodic sectors, loops and
parallel endpoint edges created by orbit coalescence must be retained in
`Q`; Theorem 4.1 remains valid once the quotient endpoint graph is known
to be a pseudoforest, but pseudoforest packing itself must be proved in the
quotient rather than inferred from the labelled cover.

## 7. Corrected proof target

The even receiver programme should replace the unrestricted
invisible-bicycle escape lemma by the following two correlated tasks.

1. Choose the passive-petal pairing so that both full endpoint diagonal
   multigraphs are pseudoforests after quotienting and fixed deletions.
2. For every proper shore cut, prove the tree/outside escape inequality
   (5.1), or directly prove the corresponding bicircular-matroid rank
   inequality when visible edges are removed.

The first task is genuinely necessary by Theorem 3.1.  The second is the
remaining proper-cut content; it is not supplied merely by one-unit strict
Hall expansion.

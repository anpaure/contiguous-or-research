# Preplanted loose trees reduce exact cover-down to prescribed matching extension

Date: 2026-07-31  
Status: exact planting reduction, unconditional uniform near-bulk theorem,
and an explicit linear-size loose-tree extension obstruction.  This does
**not** construct an exact zero-leave bulk or regenerate the recursive common
cap.

## 0. Verdict

The loose-tree bank and the arbitrary-`Q` Delcourt--Postle forest theorem
combine cleanly, but not in the way needed for coefficient one.

Let `h` clean loose packet trees be planted.  If tree `j` has `e_j` packets,
then its full target set has `2e_j+1` pairwise-resource-disjoint atoms.  Put

\[
 b=\sum_{j=1}^h(2e_j+1).                                      \tag{0.1}
\]

Choosing one port in each tree installs `b-h` off-state atoms and leaves the
chosen `h` target atoms uncovered.  Crucially, the **complete resource union
reserved from the bulk is independent of the port choices**.  Therefore:

> A bulk with precisely those `h` holes and no others exists if and only if
> the `b` target atoms comprising the trees extend to an exact side matching.

Loose-tree flexibility chooses the locations of the `h` holes and can help
with the physical topology of activation.  It does not make the exact bulk
matching more feasible.

What Delcourt--Postle does give, uniformly for every fixed common basis `Q`,
is a bulk leaving only

\[
             O(P/n+b+P D_0^{-\alpha})=o(P)                    \tag{0.2}
\]

additional atoms when `b=o(P)`.  Literal outer palettes, owner slots, cap-two
owners, and cap-one anchors are respected automatically.  A protected forest
and root-star guard can be retained at a further cost equal to the size of
the protected graph.  Thus preplanting is asymptotically compatible with the
arbitrary-`Q` forest theorem.

The extra `o(P)` leave cannot be deleted from the conclusion.  In the more
generous unpunctured host, an explicit bank of only `2n` disjoint one-packet
loose trees has `6n=o(P)` target atoms.  Its root atoms saturate the two slots
of all `n` owners above one unused lower colour, making that colour isolated.
Hence even "the planted object is an `o(P)` resource-private loose-tree bank"
does not imply exact extension.

The sharp remaining object is consequently a **correlated extendable bank**:
choose the common basis, loose-tree target matching, exact residual matching,
and graphic/root/common-cap state simultaneously.

## 1. Exact port-independence theorem

Work in the normalized fixed-`Q` capacity-slot host `G_Q`, with active typed
resource classes

```text
                         D, U, S
```

of orders `P,P,2P`.  Every atom uses one lower resource, one upper resource,
and two literal owner slots.  Equivalently, before deleting the affine
unused-slot baseline, an exact side state is outer-perfect and respects all
owner capacities.  The arguments below are identical in the two models.

Let `T_1,...,T_h` be pairwise-resource-disjoint clean loose packet trees.
Write

\[
 B=\dot\bigcup_{j=1}^h V(T_j)                                  \tag{1.1}
\]

for their full target-atom matching, and let `b=|B|`.  Choose a port
`r_j in V(T_j)` in every tree.  Theorem 4.1 of the multislice-router note
gives an off configuration `O_j(r_j)` which partitions
`V(T_j)-{r_j}`.  Put

\[
 O(\mathbf r)=\dot\bigcup_j O_j(r_j).                           \tag{1.2}
\]

Then

\[
 |O(\mathbf r)|=b-h,qquad
 \operatorname {res} O(\mathbf r)
   =\operatorname {res} B-\dot\bigcup_j\operatorname {res}(r_j).
                                                                    \tag{1.3}
\]

### Theorem 1.1 (exact bulk-extension equivalence)

The following are equivalent.

1. There is a bulk matching `M` such that `M union O(r)` has complete typed
   leave exactly `dot union_j res(r_j)`.
2. The residual host

   \[
                    G_{Q,B}=G_Q-\operatorname {res}(B)          \tag{1.4}
   \]

   has a perfect matching `M` of order `P-b`.
3. The partial target matching `B` extends to a perfect matching of `G_Q`.

These statements are independent of the chosen port vector `r`.

#### Proof

The off configuration consumes every resource of `B` except the selected
ports.  If those ports and no other resources are to remain uncovered, the
bulk must consume every resource outside `res(B)` and no resource inside it.
This is exactly statement 2.  Adding `B` to a residual perfect matching gives
statement 3, and deleting `B` from an extension gives statement 2.  Equation
(1.3) proves the equivalence with statement 1 and the independence from the
port vector. `square`

Activating one incident packet in each tree replaces `O(r)` by a matching of
`b` atoms covering exactly `res(B)`.  Hence a residual perfect matching from
Theorem 1.1 also gives a final exact side matching.  Different port choices
may give different physical edge sets in that final state, even though they
do not change the resource-extension problem.

### Corollary 1.2 (exact fractional gate)

Let `D_B,U_B` be the outer resources used by `B`, and let `s_B(x)` be the
number of literal slots at owner `x` used by `B`.  Put

\[
 c_B(x)=c(x)-s_B(x).                                            \tag{1.5}
\]

The residual host is fractionally outer-perfect only if

\[
\begin{aligned}
 \rho(Q;B)=\max\quad&
   \sum_{D\notin D_B}a_D+\sum_{V\notin U_B}b_V
       -\sum_x c_B(x)z_x\\
 \text{subject to}\quad&
   a_D+b_V\le z_{x_e}+z_{y_e}
       \quad(e=(D,V)\text{ residual}),\\
 &0\le z_x\le1,qquad a_D,b_V\in\mathbb R
\end{aligned}                                                   \tag{1.6}
\]

being zero.  Conversely `rho(Q;B)=0` is exactly fractional residual
feasibility.

#### Proof

This is Theorem 2.1 of the fixed-`Q` dummy-dual note applied after deleting
the outer resources of `B` and subtracting its occupied literal slots from
the capacities. `square`

Thus `rho(Q;B)>0` rules out every port choice, every Delcourt--Postle colour,
and every subsequent graphic repair.  The condition `rho(Q;B)=0` is not
sufficient for an integral four-resource matching, much less for a physical
forest or a downstream common cap.

## 2. Uniform near-bulk extension around any small clean bank

Let

\[
 D_0=2(n+1)(n+2).                                               \tag{2.1}
\]

Fix a cycle cutoff `L`.  Let `alpha=alpha(L)>0` be the exponent in the
Delcourt--Postle colouring theorem used by the arbitrary-`Q` physical-forest
theorem.

### Theorem 2.1 (preplanted arbitrary-`Q` near-bulk)

For every fixed common basis `Q` and every legal target matching `B` of order
`b`, the residual host `G_(Q,B)` contains a matching `M` whose projected
physical graph has no cycle of length at most `L` and

\[
 |M|\ge
 \left({|E(G_Q)|\over D_0}-4b\right)(1-D_0^{-\alpha}).          \tag{2.2}
\]

Consequently

\[
 (P-b)-|M|
 \le {8P\over n}+3b
       +O(P/n^2+P D_0^{-\alpha}+bD_0^{-\alpha}).                \tag{2.3}
\]

The bound is uniform over `Q` and `B`.  In particular it is `o(P)` whenever
`b=o(P)`.

#### Proof

The matching `B` uses exactly `4b` literal host resources.  Deleting those
resources removes at most `4bD_0` atoms, because `Delta(G_Q)<=D_0`.  Thus

\[
                 |E(G_{Q,B})|\ge |E(G_Q)|-4bD_0.                \tag{2.4}
\]

Vertex degrees, pair codegrees, and all short-cycle configuration degrees
can only decrease on passage to the residual host.  The same
Delcourt--Postle colouring therefore partitions its atoms into at most
`D_0(1+D_0^{-alpha})` short-cycle-avoiding matchings.  The largest colour
class has the size in (2.2), using
`(1+x)^(-1)>=1-x`.

The exact arbitrary-`Q` edge ledger gives

\[
 {|E(G_Q)|\over D_0}
 \ge P\left(1-{8\over n}+{16\over n^2}-{34\over n^3}
                 +O(n^{-4})\right).                             \tag{2.5}
\]

Subtracting (2.2) from the residual outer target `P-b` gives (2.3).
`square`

For a loose-tree bank, let the trees have total target order `b` and choose
one port in each of their `h` components.  Adding their off states to `M`
gives a legal matching of order

\[
 |M|+b-h=(P-h)-\delta,\qquad
 \delta=(P-b)-|M|.                                              \tag{2.6}
\]

Its typed leave contains the `h` selected target ports plus exactly `delta`
additional lower resources, `delta` additional upper resources, and
`2delta` additional literal slots.  Formula (2.3) is therefore the precise
unconditional remainder after correlated preplanting.

For logarithmic trees `b=O(h\log n)`.  Any

\[
                         h=o(P/\log n)                           \tag{2.7}
\]

is asymptotically compatible with this theorem.  The stronger orbit-packing
range from the multislice-router note is also admissible whenever its chosen
bank has `b=o(P)`.

## 3. Physical forest and root guards

The resource matching in Theorem 2.1 already enforces:

* no repeated lower or upper outer colour;
* ordinary owner degree at most two; and
* seam-anchor degree at most one.

The remaining physical graphic row can be retained asymptotically without
changing the exact extension conclusion of Section 1.

### Lemma 3.1 (protected-forest pruning)

Let `A` be a protected physical forest, including any declared packet-phase
edges, seam attachments, and root-star guard edges.  Let `M` be a host
matching whose projected graph has no cycle of length at most `L`.  There is
a submatching `M' subseteq M` such that

\[
 A\cup\operatorname {proj}(M')\text{ is a forest},qquad
 |M'|\ge |M|-{|M|\over L+1}-|A|.                               \tag{3.1}
\]

#### Proof

First delete one atom from each cycle of `proj(M)`.  Its maximum degree is
at most two, its cycles are edge-disjoint, and every cycle has length at
least `L+1`, so this costs at most `|M|/(L+1)` atoms and leaves a forest
`F`.

Add the edges of `A` to `F` one at a time.  Whenever an added protected edge
creates a cycle, that cycle contains an unprotected edge because `A` itself
is a forest; delete one such edge of `F`.  At most `|A|` deletions occur.
`square`

If both the off and activated packet edges must be legal in a common
intermediate support, take `A` to be their union together with the root
guards.  Lemma 3.1 applies provided this complete protected union is itself
a forest.  If it already contains a cycle, no choice of bulk can repair that
protected cycle.  If only the terminal state matters, it suffices to put the
terminal activated phase in `A`.

Taking fixed `L`, then a slow diagonal `L=L(n)->infinity`, and assuming
`|A|=o(P)`, Theorem 2.1 plus Lemma 3.1 leaves `o(P)` total deficiency while
preserving the declared physical/root forest.  It does **not** ensure that
every component contains a root or seam anchor, nor does it regenerate a
pointwise downstream common cap.

## 4. A linear-size loose-tree bank can destroy exact extension

The failure of exactness is not an artefact of the estimate (2.4).  It is
possible for a resource-private bank of only `O(n)` one-packet loose trees to
make one otherwise unused lower colour isolated.

Consider the more generous unpunctured side catalogue on
`Omega=D_0 dot union A`, where

\[
 D_0=\{d_0,\ldots,d_{n-1}\},\qquad
 A=\{a_0,\ldots,a_{n-1}\},                                    \tag{4.1}
\]

and every rank-`(n+1)` owner has two slots.  Indices below are modulo `n`.
For `n>=5`, `i in Z_n`, and `t in {1,2}`, define

\[
\begin{aligned}
 D_{i,t}&=D_0-d_{2i+t}+a_i,\\
 V_{i,t}&=D_0+a_i+a_{i+t},\\
 x_i&=D_0+a_i,\\
 y_{i,t}&=D_0-d_{2i+t}+a_i+a_{i+t}.                            \tag{4.2}
\end{aligned}
\]

Let `e_(i,t)` be the diamond atom `(D_(i,t),V_(i,t))`, whose two owners are
`x_i,y_(i,t)`.  Assign its occurrence at `x_i` to literal slot `t`, and its
occurrence at `y_(i,t)` to either slot.

### Theorem 4.1 (explicit `2n`-atom nonextendable matching)

The atoms

\[
                        B_n=\{e_{i,t}:i\in Z_n, t\in\{1,2\}\} \tag{4.3}
\]

form a legal literal matching.  They do not use the lower colour `D_0`, but
`D_0` has no residual candidate after `B_n` is planted.  Hence `B_n` has no
outer-perfect extension.

#### Proof

The outside element `a_i` and deleted element `d_(2i+t)` recover `(i,t)`
from `D_(i,t)`, so all lower colours are distinct.  The unordered pairs

\[
                  \{i,i+1\},\quad\{i,i+2\}\qquad(i\in Z_n)     \tag{4.4}
\]

are all distinct for `n>=5`, so all upper colours are distinct.  Every
`y_(i,t)` is determined by its unique upper pair and deleted `d`-element;
the auxiliary owners are distinct from each other and from every `x_i`.
Finally `x_i` occurs exactly in `e_(i,1),e_(i,2)`, on its two different
literal slots.  Thus (4.3) is a matching.

Every atom with lower colour `D_0` has upper colour
`D_0+a_i+a_j` and physical owners `x_i,x_j`.  Both slots of every `x_i` are
already occupied by (4.3).  No residual candidate above `D_0` remains.
`square`

The roots (4.3) are not merely an arbitrary precolouring.  They extend to a
clean bank of single-packet loose trees.  For root `(i,t)`, retain the
notation in (4.2), put

\[
 b=d_{2i+t+1},                                                   \tag{4.5}
\]

and choose the other two exchanged coordinates as follows:

\[
\begin{array}{c|cc}
 t&a&c\\ \hline
 1&a_{i+1}&a_{i+3}\\
 2&d_{2i+2}&a_{i+1}.
\end{array}                                                     \tag{4.6}
\]

Here `(b,a,c)` are respectively the selected coordinates in the root's
`D,P,R` classes.  Apply the two cyclic rotations (1.3) of the multislice
router theorem to obtain the complete packet line `L_(i,t)`.

### Theorem 4.2 (explicit nonextendable clean loose-tree bank)

For every `n>=7`, the `2n` packet lines

\[
                  \{L_{i,t}:i\in\mathbb Z_n, t\in\{1,2\}\}   \tag{4.7}
\]

are pairwise resource-disjoint.  Thus they are `2n` clean one-packet loose
trees whose full target matching has `6n` atoms.  Their full target matching
does not use `D_0`, while its root submatching is (4.3); consequently the
full loose-tree bank has no exact bulk extension.

#### Proof

It is enough to compare the deleted `D_0` indices and inserted `A` indices.
The six lower colours for a fixed `i` range over the following types:

\[
\begin{array}{c|c|c}
\text{type}&D_0\text{-indices deleted}&A\text{-indices inserted}\\ \hline
1&\{2i+1\}&\{i\}\\
2&\{2i+2\}&\{i\}\\
3&\{2i+3\}&\{i\}\\
4&\{2i+1,2i+2\}&\{i,i+1\}\\
5&\{2i+1,2i+2\}&\{i,i+3\}\\
6&\{2i+2,2i+3\}&\{i,i+1\}.
\end{array}                                                     \tag{4.8}
\]

For `n>=7`, singleton insertions identify `i`; adjacent pairs and
distance-three pairs are distinct cyclic edge classes; and the deleted pair
distinguishes types 4 and 6.  Hence all `6n` lower colours are distinct, and
none is `D_0`.

The upper colours have the corresponding types

\[
\begin{array}{c|c|c}
\text{type}&D_0\text{-indices deleted}&A\text{-indices inserted}\\ \hline
1&\varnothing&\{i,i+1\}\\
2&\varnothing&\{i,i+2\}\\
3&\varnothing&\{i,i+3\}\\
4&\{2i+2\}&\{i,i+1,i+3\}\\
5&\{2i+3\}&\{i,i+1,i+2\}\\
6&\{2i+2\}&\{i,i+1,i+2\}.
\end{array}                                                     \tag{4.9}
\]

The three cyclic chord classes are distinct for `n>=7`; a consecutive
triple cannot equal the gapped triple in row 4; and rows 5--6 have different
deleted indices.  Thus all upper colours are distinct.

Finally, write an owner by the same pair
`(deleted D_0 indices, inserted A indices)`.  Directly adding each of the two
`P`-coordinates to the six rows in (4.8) shows that every owner has
multiplicity one except

* `(empty,{i})`, which occurs in the two roots with fixed `i`; and
* `({2i+2},{i,i+1})`, which occurs in two auxiliary targets.

Both have multiplicity exactly two.  Assign their two occurrences to the
two literal slots; all other owners use either slot.  Therefore the `6n`
targets form a literal matching.  Since the root submatching already
saturates both slots of every `x_i`, Theorem 4.1 still isolates `D_0` after
all auxiliary targets are added. `square`

Choose any balanced lower outer class containing `D_0` and all the
`D_(i,t)` and all auxiliary lower colours; this is possible because its
required order is exponential while only `6n+1` sets have been prescribed.
The obstruction then lives inside a balanced outer instance.  Since
`6n=o(P)`, Theorem 4.2 disproves exact extension for arbitrary small clean
loose-tree banks even in a host with more capacity than the punctured
common-basis host.  Puncturing, graphic constraints, and root guards can only
make extension harder.  A successful planting theorem must therefore choose
a special **extendable** packet bank jointly with the bulk; resource privacy,
tree flexibility, and small order are insufficient.

## 5. The exact remaining theorem

The strongest honest target exposed by the calculation is the following.

> **Correlated extendable loose-tree planting theorem.**  For some
> synchronized common basis `Q`, choose `h=o(P)` mutually private clean
> loose packet trees so that their full target matching `B`:
>
> 1. satisfies `rho(Q;B)=0` and extends integrally to an exact residual side
>    matching on both shores;
> 2. admits port choices whose off and activated physical phases, together
>    with the residual matching and protected root/seam edges, form the
>    required linear forest (or serializable ear system);
> 3. preserves every residence and upper witness; and
> 4. lies on a face with a feasible maximal common cap and recursive endpoint
>    reset.

Theorem 2.1 proves that reserving such a bank is asymptotically cheap.
Theorem 1.1 proves that exact palette/slot completion is precisely item 1,
not a probabilistic leave-alignment consequence.  Lemma 3.1 makes the
unprotected part of item 2 asymptotically cheap.  The zero-defect integral
correlation in items 1--4 remains open.

## 6. Independent audit

The dependency-free script

```text
scratch/audit_catalan_preplanted_bank_extension_obstruction_20260731.py
```

checks Theorems 4.1--4.2 for every `7<=n<=20`: all `2n` root lower colours,
upper colours, and `4n` literal slots are distinct as required; each `x_i`
has root-slot load exactly two; all `6n` full-tree lower and upper colours
are distinct; full-tree owner load is at most two; `D_0` is unused; and its
residual candidate count is zero.
It writes

```text
scratch/catalan_preplanted_bank_extension_obstruction_20260731.audit.json.
```

The audit payload SHA-256 is

```text
a58d436eb0d5b9dcd357115c6d9f989b2fa4a6835dac1f4351a6251c28e9f94b
```

The script and JSON SHA-256 hashes are respectively

```text
55c57852b3c072415b6f57666ca7b13b21334ec639f91c3f734bc865300db23c
d781225e1ac49ef7453e345697dcbb82dc77c4db5d89a17af7f2562ad13d0789
```

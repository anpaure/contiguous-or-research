# Coupled local-move circulations and triple-assisted carrier-path closure

Date: 2026-07-27

## 1. Owner-level circulation normal form

Let $F=\{C_1,\ldots,C_T\}$ be an exact wreath factor. A local modification
of $C_i$ replaces it by a wreath $C_i'$ with

$$
R_i=\mathcal M(C_i)\setminus\mathcal M(C_i'),\qquad
A_i=\mathcal M(C_i')\setminus\mathcal M(C_i),\qquad |R_i|=|A_i|.
$$

Choose at most one modification from each factor row. Form a directed
multigraph on the chosen modifications: for every owner $S\in A_i$, draw
an arc $i\to j$ when $S\in R_j$.

### Lemma 1 (coupled circulation criterion)

The chosen modifications form an exact support-matched wreath trade if and
only if

1. every added owner lies in exactly one selected $R_j$; and
2. every removed owner is hit exactly once.

Equivalently, the directed owner multigraph is a circulation with

$$
d^+(i)=d^-(i)=|R_i|=|A_i|. \tag{1.1}
$$

#### Proof

The unchanged owners cancel row by row. The union of the new supports equals
the union of the old supports, without repetitions, precisely when the added
boundary multiset $\bigsqcup_i A_i$ equals the removed boundary multiset
$\bigsqcup_i R_i$. Assigning each common owner to its unique removed row
gives the arcs and (1.1). Conversely, the two incidence conditions give
equality of the boundary multisets, hence equality of the full support
unions. QED.

The weak components of this multigraph are themselves trades. Thus a trade
is primitive exactly when the owner multigraph is weakly connected.

The earlier pair- and triple-cycle constructions are the special case in
which all $|R_i|$ parallel arcs from $i$ go to one successor and all arcs
entering a node come from one predecessor. Lemma 1 is strictly more general:
owners from one atom may split among several successors.

The verifier is `scratch/local_move_circulations.py`.

## 2. Triple-assisted closure of a pair-carrier path

Adjacent swaps have $|R|=|A|=2$. Separated double swaps have
$|R|=|A|=3$. Let $P$ denote the partial adjacent-carrier map on boundary
pairs.

### Theorem 2 (triple-assisted path macro)

Let $X,Y$ be separated-double-swap atoms satisfying

$$
A_X=R_Y. \tag{2.1}
$$

Suppose $R_X\cap A_Y=\{z\}$, and put

$$
P_{\rm start}=A_Y\setminus\{z\},\qquad
P_{\rm end}=R_X\setminus\{z\}. \tag{2.2}
$$

If there is a simple adjacent-carrier path

$$
P_{\rm start}=Q_0\longrightarrow Q_1\longrightarrow
\cdots\longrightarrow Q_s=P_{\rm end} \tag{2.3}
$$

whose factor rows are distinct from one another and from the rows of $X,Y$,
then $X,Y$ together with the $s$ adjacent-swap atoms of (2.3) form an exact
support-matched trade.

#### Proof

The three owners of $A_X$ pass wholesale to $R_Y$. Of the three owners in
$A_Y$, the owner $z$ returns directly to $R_X$; the other two form
$P_{\rm start}$. The adjacent path transports that pair to
$P_{\rm end}=R_X\setminus\{z\}$. All boundary owners are therefore matched
once. Lemma 1 proves exact support closure. QED.

Because the adjacent carrier map is a partial function on the $W$ factor
edges, the path from $P_{\rm start}$ is deterministic. Indexing equal triple
handoffs in (2.1) therefore gives a linear structural generator, implemented
in `scratch/mixed_wreath_carrier_paths.py`.

## 2.1 The omitted-coordinate decomposition

Color an odd-graph edge $e=\{A,B\}$ by the unique coordinate

$$
\chi(e)=[n]\setminus(A\cup B).
$$

For a fixed color $z$, every edge is an unordered complementary pair in
$[n]\setminus\{z\}$. Consequently two edges of color $z$ are either equal
or have no common odd-graph vertex: sharing one endpoint forces the other
endpoint to be its unique complement.

### Lemma 3 (color preservation)

1. Every adjacent-swap carrier atom has
   $\chi(R)=\chi(A)$.
2. In every one-owner full-triple handoff from Theorem 2, the residual pairs
   $P_{\rm start}$ and $P_{\rm end}$ are odd-graph edges of the same color.

#### Proof

For (1), write the cyclic order locally as

$$
(P,x,y,Q,z),\qquad |P|=|Q|=m-1.
$$

The removed and added pairs are

$$
\{P+x,Q+y\},\qquad \{P+y,Q+x\},
$$

and both omit $z$.

For (2), write a separated double swap as

$$
(a,b,X,c,d,Y),\qquad |X|=m-2,\quad |Y|=m-1.
$$

Its removed and added triples are the two odd-graph paths

$$
R=\{Y+a,\ X+b+c,\ Y+d\},
$$

$$
A=\{Y+b,\ X+a+d,\ Y+c\}. \tag{2.4}
$$

If the added triple of the first atom is the removed triple of the second,
the unique middle vertices and the two endpoints of these paths are
identified. In particular the second atom has the same endpoint core $Y$.
Substituting (2.4), the intersection of the first removed triple and the
second added triple has size only $0,1$, or $3$. In the size-one case the
common owner is an endpoint $Y+u$. Deleting that endpoint from either path
leaves an odd-graph edge omitting $u$. These are precisely
$P_{\rm end}$ and $P_{\rm start}$. QED.

It follows that the adjacent carrier map splits into $n=2m+1$ independent
partial functional graphs, one per omitted coordinate. A one-owner triple
handoff is a colored routing request $(P_{\rm start},P_{\rm end})$. The
triple-assisted macro exists exactly when the deterministic carrier orbit of
$P_{\rm start}$ hits $P_{\rm end}$ before exiting, cycling, or reusing a
factor row. Because of the fixed-color dichotomy, a failed terminal edge is
disjoint from the requested edge; there is no one-endpoint near hit.

`triple_assisted_supply_profile` now counts every stage of this routing
funnel separately.

## 2.2 Multi-junction colored carrier cycles

The terminal pair of one failed request need not equal its own target.  It
may equal the target of a second request.  This gives the missing higher-order
closure operation.

For a one-owner triple handoff $J$, write

$$
 s(J)=P_{\rm start},\qquad t(J)=P_{\rm end}.
$$

Follow any simple prefix of the adjacent carrier path from $s(J)$ and stop at
the pair $e(J)$.  After cancelling the full triple handoff and this carrier
prefix, the only remaining boundary is

$$
 A(J)=e(J),\qquad R(J)=t(J). \tag{2.5}
$$

### Theorem 4 (multi-junction port-cycle criterion)

Let $J_1,\ldots,J_r$ be routed one-owner handoffs whose underlying factor
rows are pairwise distinct.  If

$$
 e(J_i)=t(J_{i+1})\quad(1\le i\le r),
 \qquad J_{r+1}=J_1, \tag{2.6}
$$

then all triple atoms and adjacent atoms used by the $J_i$ form an exact
support-matched wreath trade.  Each equality in (2.6) lies inside one
omitted-coordinate color class.

#### Proof

Inside each $J_i$, one full triple cancels, one owner cancels directly, and
the adjacent prefix transports the residual added pair from $s(J_i)$ to
$e(J_i)$.  Thus (2.5) is its complete uncancelled boundary.  Equations
(2.6) match every added owner to exactly one removed owner.  Pairwise row
disjointness makes all removed owners distinct.  Lemma 1 now gives exact
support closure.  Lemma 3 gives color preservation. QED.

The loop case $r=1$ is Theorem 2.  The implementation
`scratch/multi_junction_carrier_cycles.py` enumerates simple port cycles for
$r\ge2$, verifies their full atomic circulation with
`local_move_circulation_certificate`, and then independently checks equality
and disjointness of the complete middle supports.

This is stronger than following every request to its terminal exit: every
carrier prefix is a legal stopping point.  The code therefore indexes all
prefixes that hit any request target, not just successful self-hits.

## 3. Exact finite identification at $m=5$

Around `scratch/m5_adjacent_carrier_next.txt`, the complete catalogue of
adjacent swaps alone has exactly three legal trades even when all 42 factor
rows may be replaced. They are precisely the three whole-pair carrier cycles;
there is no split adjacent-only circulation of any size. The complete report
is `scratch/m5_adjacent_owner_circulations_full_report.json`.

Adding the $W$ separated-double-swap atoms creates exactly three primitive
size-six trades. Theorem 2 generates exactly those three. The improving one
uses four pair atoms and two triple atoms. In the order reconstructed by
`scratch/audit_local_move_trade_certificate.py`, its transition matrix is

$$
\begin{pmatrix}
0&0&0&2&0&0\\
2&0&0&0&0&0\\
0&0&0&0&0&3\\
0&0&0&0&2&0\\
0&0&2&0&0&0\\
0&2&1&0&0&0
\end{pmatrix}. \tag{3.1}
$$

The last triple atom is the unique split source and the first triple atom is
the unique split target. Matrix (3.1) is exactly the macro of Theorem 2: one
owner returns directly while two traverse the four-edge pair path.

The first macro lowers weighted MWB from $185/4$ to $91/2$. Repeated
mixed-macro search, allowing temporary worsening and tabu/beam exploration,
then produces the replayable exact factors

$$
\frac{185}{4}\longrightarrow\frac{319}{8}
\longrightarrow\boxed{\frac{289}{8}}. \tag{3.2}
$$

The terminal factor and certificate are

```text
scratch/m5_mixed_beam_best_round2.txt
scratch/m5_mixed_beam_best_round2_certificate.json
```

For a single end-to-end audit from the previous $185/4$ factor, the nine
intermediate certificates have also been composed into one 23-step replay:

```text
scratch/m5_mixed_macro_full_path_certificate.json
```

`scratch/compose_wreath_trade_certificates.py` checks every intermediate
base/terminal match before writing this composite certificate.

Its full metrics are

$$
(O_1,O_2,O_3)=(12,40,33),\qquad \sum_q O_q/c_q=289/8,
$$

with CPCR 193, balanced $L^1=85$, 15 lower holes, and PCap zero at every
depth. The next depth-eight, width-128 mixed beam examined 6157 additional
states and found no improvement; this is a bounded search statement, not a
global optimum.

As a calibration, canonical MSW has two assisted macros at $m=3$ and none
for $m=4,\ldots,8$. The path-closing supply is therefore generated by factor
deformation rather than already present in the canonical seed. At $m=4$, the
same mixed beam lowers weighted MWB from $2$ to $1$, while preserving zero
holes; a second bounded beam finds no zero-MWB state.

The MSW audit has since been extended through $m=10$. For every
$4\le m\le10$ it gives the exact finite identity

$$
\#\{\text{one-owner handoffs}\}=4(m-2)C_{m-2}, \tag{3.3}
$$

including $(m-2)C_{m-1}$ same-start handoffs and
$3(m-2)C_{m-2}/m$ handoffs of each start displacement $+1$ and $-1$.
Every residual start pair is a factor edge, but every carrier path exits at
an edge disjoint from the requested endpoint. Formula (3.3) and the universal
exit statement are finite-verified patterns, not yet claimed for all $m$.
They show why handoff abundance alone is insufficient: MSW has
$\Theta(W)$ requests and zero hits.

The multi-junction audit sharpens this finite picture.  At $m=4,5$, canonical
MSW has cross-request target hits but no row-disjoint port cycle.  Thus the
obstruction is not absence of colored routing supply; it is incompatibility
of the requests at the circulation level.  On the deformed factor
`scratch/m4_mixed_beam_best.txt`, there is one exact two-junction trade of
size eight, with carrier-prefix lengths one and three.  On
`scratch/m5_mixed_escape_round2.txt`, the generator produces a size-seven
two-junction trade, explaining the previously unclassified size-seven term
in the complete adjacent-plus-triple support census.  The size-nine census
trade is a pure adjacent carrier cycle and was already generated by the pair
atlas.

In fact, on each of

```text
scratch/m5_adjacent_carrier_next.txt
scratch/m5_mixed_escape_round2.txt
scratch/m5_mixed_beam_best_round2.txt
```

the union of pure triple carrier cycles, pure adjacent cycles, one-junction
macros, and multi-junction macros equals the **entire** exact-trade set in the combined
$924$-candidate adjacent-plus-triple catalogue.  The counts are respectively
$21,22,14$, with no missing or extra trade.  This is a complete finite audit,
not a general classification theorem; its replayable report is
`scratch/m5_structural_mixed_atlas_completeness_report.json` and its verifier
is `scratch/audit_structural_mixed_atlas_completeness.py`.

## 4. Remaining asymptotic statement

The relevant supply question is no longer whether carrier cycles already
exist. A pair forest can be made useful when two triple atoms expose matching
one-owner defects at its ends. A sufficient quantitative theorem is:

> **Triple-assisted compensation theorem.** For every fixed
> $\varepsilon>0$, whenever an exact factor has weighted floor-corrected
> defect at least $\varepsilon W$, a bounded sequence of triple-cycle and
> triple-assisted path macros has final coherent gain exceeding total
> Dirichlet noise, while every intermediate object remains an exact factor.

Together with the quadratic trade identity, this would give strict descent
until the weighted defect is $o(W)$, hence MWB. What remains is to count
compatible triple handoffs against the endpoints of the abundant noncyclic
pair-carrier paths and correlate their orientation with the current shadow
imbalance. The finite computation proves that this mechanism is real and can
cross the previous local minima; it does not yet supply the required
asymptotic density.

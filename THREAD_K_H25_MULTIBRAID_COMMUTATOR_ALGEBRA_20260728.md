# H25 multi-braid commutators: exact overlay algebra and the common-`Q` portal gate

**Date:** 2026-07-28  
**Lane:** K, nonlocal segment-braid algebra  
**Status:** unconditional structural theorems and an explicit genuinely
non-one-braid five-piece pattern.  A subsequent exact instantiation now gives
a projected H24 carrier; no complete common-`Q` lower compiler is claimed.

## 0. Result

The complete resident/all-upper-safe one-braid neighbourhood of the audited
H25 carrier is exhausted.  That does not exhaust two-braid macros.  The
reason is algebraically exact.

1. The overlay of two three-cut braids is a signed permutation of at most
   seven intervals of the original carrier.  It is a member of the exhausted
   one-braid catalogue only when this signed permutation coarsens to the
   four-piece normal form

   \[
        A\,C^{\epsilon_C}B^{\epsilon_B}D.
   \]

2. There is a concrete two-braid five-piece shuffle

   \[
   P_0P_1P_2P_3P_4P_5P_6
       \longmapsto
   P_0P_3P_1P_5P_2P_4P_6,                         \tag{0.1}
   \]

   requiring exactly six new endpoint Johnson tests.  It has seven monotone
   runs in the original index order and therefore is not any single
   `FF/RF/FR/RR` braid.

3. Every all-depth union/intersection change of a multi-braid is the exact
   signed sum of its old and new connector collars.  Hence two individually
   unsafe braids may form a safe macro: their signed upper defects may cancel
   even though neither intermediate carrier has complete upper support.

4. Shadow cancellation is deliberately weaker than compiler cancellation.
   The full decorated `(H,3)` connector germ (the `H`-state shadow collar
   together with the depth-three controller/pin data) maps onto the
   upper-shadow germ.
   A macro can preserve all upper shadows while changing lower compiler-cell
   shores only if it is in the kernel of the former projection but not in the
   kernel of the full controller/pin germ.  If the full decorated germs also
   cancel, the lower Hall graph and the common-`Q` feasibility system are
   isomorphic; no H25 DM escape is possible.

5. There is an exact common-`Q` protected-transport theorem.  Interior pins
   move with the oriented blocks.  Only central windows and target-pin
   intervals meeting the final seam closure have to be rechecked, but they
   must be checked simultaneously through the maximal cores `K_p`; ordinary
   target--cell Hall edges do not suffice.

6. The last certified descent has a concrete reversible backtrack:

   \[
   H26\xrightarrow{\operatorname{FR}(3259,3823,5264)}H25,
   \qquad
   H25\xrightarrow{\operatorname{RF}(3259,4701,5264)}H26.       \tag{0.2}
   \]

   Therefore the first exact two-neighbourhood to inspect is not an
   unrestricted six-cut search.  It is the known inverse in (0.2), followed
   by every resident/all-upper-safe H26 braid whose pulled-back cuts do not
   coarsen to a single H25 braid.  The final common-`Q` core, rather than the
   intermediate Hall score, is decisive.

7. After this algebra was isolated, the interlaced pair

   \[
   H25\xrightarrow{\operatorname{RF}(2612,3222,3766)}H25_{\rm pivot}
   \xrightarrow{\operatorname{FF}(2125,2769,6201)}H24             \tag{0.3}
   \]

   was independently reconstructed.  Its seven-block order is

   \[
   X_0,\overleftarrow X_3,X_2,X_5,X_1,\overleftarrow X_4,X_6,
   \]

   so it is exactly a noncoarsening overlay of the type proved here.  It has
   a literal common-`Q` realization of the complete old DM-right shore, but
   not a simultaneous compiler for all `16383` lower targets.  The exact
   witness and audit are in
   `THREAD_K_H25_INTERLACED_C6_PLATEAU_PIVOT_AND_COMMON_Q_20260728.md`.

The theorems below prove these statements and isolate the exact certificate
which would turn such a macro into a literal H25-to-H24 descent.

## 1. Signed block substitutions

Let

\[
                 T=(T_0,\ldots,T_{N-1})
\]

be a Johnson path.  A block is a nonempty contiguous subpath.  If `P` is a
block, write `P^+` for its old orientation and `P^-` for its reversal, and
write

\[
 \ell(P^\epsilon),\qquad r(P^\epsilon)
\]

for its first and last states in that orientation.

Suppose the old path is partitioned into nonempty blocks

\[
                         P_0P_1\cdots P_t.             \tag{1.1}
\]

For a permutation `pi` and signs `epsilon_j`, form

\[
 T'=P_{\pi(0)}^{\epsilon_0}P_{\pi(1)}^{\epsilon_1}
          \cdots P_{\pi(t)}^{\epsilon_t}.             \tag{1.2}
\]

### Theorem 1.1 (general signed-block path theorem)

The word (1.2) is a deck-exact Johnson path if and only if

\[
 r(P_{\pi(j)}^{\epsilon_j})\sim
 \ell(P_{\pi(j+1)}^{\epsilon_{j+1}})
 \qquad(0\le j<t).                                    \tag{1.3}
\]

Here `~` is Johnson adjacency.  No other deck or path test is needed.

#### Proof

Reversal preserves every undirected internal Johnson edge.  Thus all
internal edges of all blocks survive, and the only unverified edges are the
displayed connectors.  The blocks still partition the indexed states of
`T`, so (1.2) has exactly the old deck.  This proves both directions. ∎

### Lemma 1.2 (two-braid overlay normal form)

The composition of two three-cut segment braids is a signed permutation of
at most seven contiguous intervals of the original path.

#### Proof

The first braid is a piecewise isometry of the index line with three
internal cuts.  Pull the three cuts of the second braid back through that
piecewise isometry.  Together the two cut sets have at most six distinct
internal positions and hence partition the original line into at most seven
intervals.  On each interval the composition is a translation or a
reflection. ∎

### Corollary 1.3 (uniform two-braid boundary bounds)

After internal block transport, a two-braid overlay has at most six old and
six new connectors.  Consequently:

1. at shadow depth `q`, at most `6q` old and `6q` new window starts enter
   the signed ledger, and its multiplicity `L1` norm is at most `12q`;
2. for depth-three erosion, at most `18` final controller columns are new;
3. using the exact `9+10+11=30` target-cell dependency bound per seam, at
   most `180` old and `180` new lower cell shores enter the contracted Hall
   boundary.

All bounds count overlaps only once, so collisions can only improve them.

#### Proof

At most seven transported atoms have at most six internal connectors.  One
connector is crossed by at most `q` windows of length `q+1`.  An interior
depth-three connector changes only its three crossing controller columns.
Finally, cells of lengths one, two, and three have respectively `9,10,11`
possible dependency starts at one seam.  Summing proves the claims. ∎

### Proposition 1.4 (exact reduction to the exhausted catalogue)

A signed block substitution is one `FF/RF/FR/RR` braid if and only if, after
coalescing consecutive atoms whenever their original indices and
orientations continue monotonically, its signed order has the form

\[
       A^+\,C^{\epsilon_C}B^{\epsilon_B}D^+,          \tag{1.4}
\]

where `A,B,C,D` are consecutive original intervals (with `A` or `D`
possibly empty and `B,C` nonempty).

In particular, any two-braid overlay whose reduced signed order has more
than four monotone runs is outside the complete H25 one-braid census.

#### Proof

Formula (1.4) is exactly the definition of a segment braid, so it is
sufficient.  Conversely a segment braid acts by one orientation on each of
the four displayed original intervals and hence coalesces to (1.4). ∎

## 2. An explicit five-piece two-braid commutator

Take seven nonempty blocks in their old forward orientations.  First apply
the `FF` braid which swaps `P_1P_2` with `P_3`:

\[
 P_0\mid P_1P_2\mid P_3\mid P_4P_5P_6
 \longmapsto
 P_0P_3P_1P_2P_4P_5P_6.                              \tag{2.1}
\]

In the resulting path apply the `FF` braid which swaps the now adjacent
block `P_2P_4` with `P_5`:

\[
 P_0P_3P_1\mid P_2P_4\mid P_5\mid P_6
 \longmapsto
 P_0P_3P_1P_5P_2P_4P_6.                              \tag{2.2}
\]

### Theorem 2.1 (five-piece shuffle)

Both intermediate and final words are deck-exact Johnson paths precisely
when the following six new edges are Johnson edges:

\[
\begin{array}{lll}
 r(P_0)\sim\ell(P_3),&r(P_3)\sim\ell(P_1),
     &r(P_2)\sim\ell(P_4),\\
 r(P_1)\sim\ell(P_5),&r(P_5)\sim\ell(P_2),
     &r(P_4)\sim\ell(P_6).
\end{array}                                           \tag{2.3}
\]

The final substitution (0.1) is not a single segment braid.

#### Proof

The first row of (2.3) is exactly the endpoint test for (2.1); all other
connectors at that step are inherited.  The second row is exactly the test
for (2.2).  Theorem 1.1 proves deck exactness.

In the final interior order

\[
                         3,1,5,2,4
\]

no two successive labels are consecutive in the original order, in either
orientation.  Thus the complete final index map has seven monotone runs:
`P_0`, the five displayed interior blocks, and `P_6`.  Proposition 1.4
allows at most four. ∎

This is the smallest explicit pattern used here.  It is a construction
template, not an assertion that the six endpoint edges (2.3) have already
been located in H25.

## 3. Exact connector shadow algebra

Assume for the moment that every block has at least `H` states.  For an
oriented connector `P|Q` and `1<=q<=H`, define the upper and lower connector
vectors

\[
 \mathsf U_q(P,Q)=
   \sum_{j=1}^{q}
   e_{\,\bigcup(\operatorname{suf}_jP\,\cup\,
                    \operatorname{pre}_{q+1-j}Q)},               \tag{3.1}
\]

\[
 \mathsf L_q(P,Q)=
   \sum_{j=1}^{q}
   e_{\,\bigcap(\operatorname{suf}_jP\,\cup\,
                    \operatorname{pre}_{q+1-j}Q)}.               \tag{3.2}
\]

The union inside the subscript of (3.2) means the concatenated family of
states; the label is their intersection.  The basis vector records the
resulting target set.  Orientations are already built into `P,Q`.

Because block lengths are at least `H`, a window through depth `H` crosses
at most one connector.

### Theorem 3.1 (multi-braid shadow boundary formula)

Let `E_0` and `E_1` be the ordered connector multisets of the old and new
signed block paths.  For `star` equal to upper or lower,

\[
 \Delta_{q,\star}
 =\sum_{e\in E_1}\mathsf{\star}_q(e)
  -\sum_{e\in E_0}\mathsf{\star}_q(e).               \tag{3.3}
\]

The final upper layer is complete exactly when

\[
 m_{q,U}^{T}(S)+\Delta_{q,U}(S)\ge1
 \quad\text{for every target }S                       \tag{3.4}
\]

at that depth.  Exact multiset preservation is the stronger equality
`Delta_{q,U}=0`.

If some blocks are shorter than `H`, the same theorem remains true after
replacing the single-connector vectors by the exact multiset of all windows
crossing the old or new cut sets.  Such a window may then meet more than one
connector and must be counted once, not once per connector.

#### Proof

Every window internal to an oriented block is transported by translation or
reflection and has the same union and intersection label.  Cancel these
windows.  The uncancelled windows are precisely the boundary windows in
(3.3).  The support criterion is the definition of completeness. ∎

For the five-piece shuffle the two connector sets are

\[
\begin{aligned}
E_0={}&\{01,12,23,34,45,56\},\\
E_1={}&\{03,31,15,52,24,46\}.                         \tag{3.5}
\end{aligned}
\]

Thus (3.3)--(3.4) are six-connector equations, not an unstructured scan.

### Lemma 3.2 (cocycle/telescoping identity)

For consecutive braids `g` and `h`,

\[
 \Delta_{q,\star}(h\circ g;T)
 =\Delta_{q,\star}(g;T)
  +\Delta_{q,\star}(h;gT).                            \tag{3.6}
\]

Hence the intermediate path need not preserve a shadow support: a loss in
the first signed ledger may be restored by the second.  Only the final
inequality (3.4) is necessary for final support.

#### Proof

Insert and subtract the intermediate multiplicity vector. ∎

Residence is not a signed linear ledger.  Nevertheless it is equally local:
all coordinate runs internal to final oriented blocks are inherited, and
the final carrier is depth-`d` resident if and only if every internal run
meeting one of its new connectors has length at least `d+1`.  The
intermediate residence test is necessary only if one insists that both
braids separately be admissible carriers.

### Theorem 3.3 (additive Hall current for separated braid banks)

Let the old and final lower graphs, after transporting their common interior
cells, have the decompositions

\[
 G_0=H\sqcup B_1^-\sqcup B_2^-,
 \qquad
 G_1=H\sqcup B_1^+\sqcup B_2^+,                      \tag{3.7}
\]

where the two boundary banks are disjoint as physical right-cell sets.  For
a left target family \(X\), put

\[
 I_j(X)=
 \#\{c\in B_j^+:N(c)\cap X\ne\varnothing\}
 -
 \#\{c\in B_j^-:N(c)\cap X\ne\varnothing\}.           \tag{3.8}
\]

If \(h\) is the old Hall deficiency and

\[
 \sigma(X)=h-|X|+|N_{G_0}(X)|,
\]

then

\[
 \boxed{\displaystyle
 \delta(G_1)=
 h-\min_X\bigl(\sigma(X)+I_1(X)+I_2(X)\bigr).}         \tag{3.9}
\]

In particular the pair descends by at least one exactly when

\[
 I_1(X)+I_2(X)\ge1-\sigma(X)
 \qquad\text{for every }X.                            \tag{3.10}
\]

Thus two one-braid moves which are separately blocked by different
near-critical shores can be jointly descending.  This is a genuine
two-braid effect; checking only the canonical H25 shore is still
insufficient.

#### Proof

Disjointness gives

\[
 |N_{G_1}(X)|-|N_{G_0}(X)|=I_1(X)+I_2(X).
\]

Substitute this into
\(\delta(G_1)=\max_X(|X|-|N_{G_1}(X)|)\) and use the definition of
\(\sigma\). ∎

If the banks overlap, (3.8) must be replaced by the current of their union;
adding the separate currents would double-count shared cells.

## 4. Decorated `(H,3)` connector germs and the exact escape invariant

For a depth-three resident carrier `T'`, its maximal erosion controller is

\[
 P'_p=\bigcap_{i=\max(0,p-3)}^{\min(p,N-1)}T'_i,
 \qquad 0\le p<N+3.                                  \tag{4.1}
\]

At an interior connector placed between `T'_{c-1}` and `T'_c`, write the
last three left states as `L_{-3},L_{-2},L_{-1}` and the first three right
states as `R_0,R_1,R_2`.  The only controller columns crossing this
connector are

\[
\begin{aligned}
 P'_c&=L_{-3}\cap L_{-2}\cap L_{-1}\cap R_0,\\
 P'_{c+1}&=L_{-2}\cap L_{-1}\cap R_0\cap R_1,\\
 P'_{c+2}&=L_{-1}\cap R_0\cap R_1\cap R_2.             \tag{4.2}
\end{aligned}

Every lower compiler cell is an interval `I=[s,s+e]`, `e=0,1,2`.  Its
maximal native label is

\[
                         \tau_{P'}(I)=\bigcup_{p\in I}P'_p.       \tag{4.3}
\]

Equations (4.2)--(4.3) give the exact new native cells of every multi-braid
from its final connector collars.

### Lemma 4.1 (native cells are the three shallow lower rows)

For \(e\in\{0,1,2\}\) and

\[
                         3-e\le s\le N-1,
\]

depth-three residence gives the exact identity

\[
 \boxed{\displaystyle
 \bigcup_{p=s}^{s+e}P'_p
   =\bigcap_{i=s+e-3}^{s}T'_i.}                       \tag{4.4}
\]

Thus the interior native cells of lengths one, two, and three are exactly,
up to the displayed index shifts, the lower shadow rows of depths three,
two, and one.  The cells outside the indicated range are the
\(2(3-e)\) clipped endpoint bonus cells and must be handled separately.

#### Proof

Put \(R=[s+e-3,s]\).  For \(0\le j\le e\), the carrier-index interval
defining \(P'_{s+j}\) contains \(R\); hence every \(P'_{s+j}\) is contained
in the right side of (4.4).

Conversely fix a coordinate \(x\) present throughout \(R\).  Its maximal
presence run contains \(R\).  If the run is internal, residence says that it
has at least four states, so it contains one of the \(e+1\) four-state
extensions

\[
 [s-3,s],\ [s-2,s+1],\ldots,[s+e-3,s+e].
\]

The corresponding controller column \(P'_{s+j}\) contains \(x\).  If the
run meets a global endpoint, the same argument uses the clipped controller
interval there; the allowed range of \(s\) makes \(R\) a valid carrier
interval.  Therefore \(x\) lies in the union on the left. ∎

Consequently, exact preservation of the lower depth-one, -two, and -three
occurrence multisets preserves the multiset of all interior native-cell
labels.  It can still relocate those labels among physical right cells and
can still change exceptional compatibility.  But it cannot create a
previously absent interior native label.  Such support creation must change
one of those shallow lower ledgers or use a clipped endpoint cell.

For the fixed H25 critical shore \(D\), an interior cell
\(I=[s,s+e]\notin N_{H25}(D)\) becomes a certified **native DM portal** as
soon as

\[
 \bigcap_{i=s+e-3}^{s}T'_i\in D.                      \tag{4.5}
\]

Provided the final maximal controller is nonempty at every physical
position, (4.4) then makes that target the literal maximal-controller value
of \(I\).  This is a stronger and cheaper screen than recomputing every
one-target flexible edge.  It is not by itself an augmentation certificate:
the new right cell must also complete an alternating route, and its pin must
survive the simultaneous common-\(Q\) test.

Define the **decorated `(H,3)` germ** of a connector to consist of:

* the last `H` carrier states on the left and first `H` carrier states on
  the right, in their final orientations (and hence every shadow connector
  vector through depth `H`);
* its three controller columns (4.2), together with the unchanged controller
  columns needed by the short cells immediately outside them;
* every length-one, two, or three physical cell meeting that collar and its
  complete target-neighbourhood shore;
* every retained or proposed exact pin interval meeting the collar, with its
  target label and physical overlaps;
* the coordinate-run ports at both sides of the collar.

The shadow connector vectors (3.1)--(3.2) are projections of this decorated
germ: they forget cell incidence, pin overlap, and the order in which the
three controller columns occur.

When two connector collars overlap, their germs are understood as one
induced decorated seam structure with the shared positions identified.  If
the chosen full germ collars are disjoint (for example, after requiring each
intervening block to exceed twice the complete germ radius), the structure
is their ordinary disjoint union.

### Theorem 4.2 (full-germ cancellation is an obstruction)

Suppose a signed block substitution transports every interior decorated
cell and pin, and its old and new connector germs admit a label- and
incidence-preserving bijection.  Then:

1. the old and new lower target--cell graphs are isomorphic;
2. their Dulmage--Mendelsohn decompositions and Hall deficiencies agree;
3. a simultaneous pin family passes the common-`Q` test before the move if
   and only if the transported family passes it after the move.

Consequently such a macro cannot open a compiler cell outside the H25 DM
neighbourhood.  A viable commutator must satisfy

\[
 \Delta_{q,U}=0\ (1\le q\le7)
 \quad\text{or at least (3.4),}
 \qquad
 \Delta(\text{decorated controller germ})\ne0.         \tag{4.6}
\]

#### Proof

Interior transport and the assumed germ bijection together give a bijection
of all physical cells preserving their complete target neighbourhoods.
This is a bipartite-graph isomorphism, proving the first two assertions.
The same bijection preserves physical interval incidence, controller
columns, pin labels, and coordinate membership.  It therefore carries every
maximal allowed set `Q_x`, every positive-hit condition, and every nonempty
point-core condition to its counterpart.  This proves the third assertion.
∎

This theorem explains why merely asking for a seam ledger to “return” can
overconstrain the search.  The upper shadow ledger should return; the full
controller/pin germ must not.

## 5. Exact protected transport for one common word

Let `Phi` be an injective family of lower target pins `(I,S)` for a carrier
`T`, and put

\[
 K_p=P_p\cap\bigcap_{(I,S)\in\Phi:\ p\in I}S.          \tag{5.1}
\]

Equivalently, for each coordinate `x` define the forbidden-position union

\[
 F_x(\Phi)=\bigcup_{(I,S)\in\Phi:\ x\notin S}I,
 \qquad
 \{p:x\in K_p\}=\{p:x\in P_p\}\setminus F_x(\Phi).   \tag{5.1a}
\]

This is a union ledger, not an additive histogram.  Two pin families with
the same controller and the same unions `F_x` have exactly the same
common-`Q` feasibility.  Equality only of pin counts, target histograms, or
signed interval multiplicities is weaker because overlaps in `F_x` are
idempotent.  Thus a proposed seam commutator which returns all `F_x` and the
controller germ cannot improve the common-`Q` state; one which returns only
shadow/pin counts may still do so.

The exact common-word theorem says that `Phi` is literal if and only if:

\[
 K_p\ne\varnothing\quad\text{for every }p,             \tag{5.2}
\]

\[
 [i,i+3]\cap\{p:x\in K_p\}\ne\varnothing
 \quad(x\in T_i),                                      \tag{5.3}
\]

and

\[
 I\cap\{p:x\in K_p\}\ne\varnothing
 \quad((I,S)\in\Phi,\ x\in S).                        \tag{5.4}
\]

When these hold, the literal word is `A_p=K_p`.

Consider now any final signed-block substitution.  On positions lying far
enough inside a block that their central four-window and every pin interval
under consideration stay inside that block, there is a natural translation
or reflection `theta`.  Transport all such pins by `theta`.  Pins crossing
an old cut are not transported blindly; they enter the boundary package.

Let `Z` contain

1. the final images of the complete old- and new-seam closures (in
   particular every position belonging to a central four-window which is
   not wholly inside one transported block);
2. every position at which the maximal controller is not the transported
   old controller; and
3. every position belonging to a pin which was deleted, inserted, or
   reassigned.

Let `C(Z)` be the family of all central four-windows and all selected pin
intervals which meet `Z`.

### Theorem 5.1 (protected common-`Q` transport)

Assume the old pin family satisfies (5.2)--(5.4).  After transporting the
interior pins and choosing an arbitrary new boundary package, the final pin
family is literal if and only if the following boundary checks pass:

1. `K'_p` is nonempty at every `p in Z`;
2. every positive central requirement (5.3) whose window belongs to `C(Z)`
   is hit by `K'`;
3. every positive target-pin requirement (5.4) whose interval belongs to
   `C(Z)` is hit by `K'`.

All conditions outside `C(Z)` are inherited under `theta` and need not be
reproved.

#### Proof

At a position outside `Z`, the controller and the complete family of
negative pin labels containing that position are transported unchanged, so
`K'_p=K_{\theta^{-1}(p)}`.  A central or target-pin interval disjoint from
`Z` is wholly in one transported block and has exactly its old core and
positive-hit pattern.  Thus only the displayed constraints can change.
Checking them gives all of (5.2)--(5.4), and necessity is immediate. ∎

This is a genuinely simultaneous theorem.  Rechecking every new target--cell
edge separately is insufficient, because two individually legal pins may
delete each other's last coordinate witness.

### Corollary 5.2 (separated common-`Q` packages compose)

Suppose `Z=Z_1 disjoint-union Z_2` and no central four-window or selected pin
interval meets both `Z_1` and `Z_2` (distance at least four between the two
sets is sufficient).  Then the union of two boundary packages
passes the common-`Q` test if and only if each package passes the local tests
of Theorem 5.1 against the transported background.

#### Proof

Every condition (5.2)--(5.4) is pointwise or belongs to one central/pin
interval.  By hypothesis its data are either unchanged or meet exactly one
package.  Therefore no condition contains deletions from both packages, and
the two local audits partition the changed conditions. ∎

This is the exact circumstance in which the additive Hall macro of Theorem
3.3 also admits a packagewise common-`Q` audit.  Physical disjointness of the
right cells alone is weaker; the complete length-four/length-three interval
closures must be separated.

### Corollary 5.3 (native portal)

Let `I` be a new boundary cell and let

\[
                         S=\tau_{P'}(I).              \tag{5.5}
\]

Adding the pin `(I,S)` introduces no new negative deletion from the maximal
controller.  It is compatible with an existing exceptional pin family
exactly when

\[
                         I\cap\{p:x\in K'_p\}\ne\varnothing
                         \quad(x\in S).                \tag{5.6}
\]

In particular (5.6) is automatic if no exceptional pin interval meets `I`.

#### Proof

If `x` is absent from `S`, (5.5) says that it is already absent from every
`P'_p`, `p in I`; the pin therefore makes no further negative deletion.  Its
only new obligations are the positive hits (5.6). ∎

Thus a new maximal-controller trace is the cleanest possible literal DM
portal.  A merely projected Hall edge is not.

## 6. Exact H25 backtrack and second-neighbourhood reduction

Write the certified last descent as

\[
 H26=A\,B\,C\,D
 \longmapsto
 H25=A\,C\,\overleftarrow B\,D,                       \tag{6.1}
\]

where

\[
 |A|=3259,\qquad |B|=3823-3259=564,
 \qquad |C|=5264-3823+1=1442.                         \tag{6.2}
\]

In H25 the block boundaries are consequently

\[
                         3259,\quad4701,\quad5265.     \tag{6.3}
\]

Swapping `C` with `reverse(B)`, reversing the latter and retaining the former,
is precisely

\[
 \operatorname{RF}(3259,4701,5264),                  \tag{6.4}
\]

which proves (0.2) directly.

For a cut `t` strictly inside one of the four H26 blocks, its boundary
position pulled back to the H25 atom partition is

\[
 \lambda(t)=
 \begin{cases}
 t,&0<t<3259,\\
 8524-t,&3259<t<3823,\\
 t-564,&3823<t<5265,\\
 t,&5265<t<N.
 \end{cases}                                          \tag{6.5}
\]

Cuts at the three displayed block boundaries merely reuse an existing atom
boundary and require no new split.

### Corollary 6.1 (exact two-neighbourhood catalogue reduction)

Let `gamma` range over the complete resident/all-upper-safe H26 one-braid
catalogue.  Every composite

\[
 H25\xrightarrow{\beta^{-1}}H26\xrightarrow{\gamma}Y,
 \qquad \beta^{-1}=\operatorname{RF}(3259,4701,5264), \tag{6.6}
\]

has an overlay of at most seven H25 atoms, obtained from (6.3), (6.5), and
the three cuts of `gamma`.  If that overlay coarsens to (1.4), then `Y` is
already in the exhausted H25 one-braid catalogue.  Otherwise it is a
genuinely new multi-braid neighbour.

The conclusion is independent of the Hall score of the intermediate H26
carrier.  Common-`Q` feasibility is to be tested directly on `Y` by Theorem
5.1; it does not follow by multiplying two projected Hall certificates.

#### Proof

Lemma 1.2 and formula (6.5) give the atom bound and explicit overlay.
Proposition 1.4 gives the exact dichotomy. ∎

This is the smallest exact H25 search space not closed by the local-minimum
theorem: backtrack through the known H26 parent and take a different safe
outgoing braid.  A useful `gamma` need not itself improve H26 relative to
every score; only the final H25-relative carrier and common word matter.

## 7. The literal DM-escape certificate

Fix a maximum matching `M` in the H25 projected lower compiler graph.  Let
`D` be a left alternating-reachable DM shore and `N(D)` its old right
neighbourhood.  Under a multi-braid, first retain the part

\[
                         M_0=M\cap E(G')               \tag{7.1}
\]

and let `r=|M|-|M_0|`.

For the canonical matching reconstructed in
`scratch/k15_segment_braid_descent_audit.json`, the H25 shore has

\[
 |D|=1320,\qquad |N(D)|=1295,
 \qquad |D|-|N(D)|=25,                                \tag{7.2}
\]

and its sorted-target digest is

```text
89449e9fe9fb085c96ec911e3a9fad61f1e0409e4c6ef0133ed72677eb273e83
```

This identifies the old neighbourhood meant below; it does not make its
projected matching a common-`Q` pin system.

### Proposition 7.1 (an H24 descent must leave the old DM neighbourhood)

If a final projected graph `G'` has deficiency at most `24`, then

\[
 |N_{G'}(D)|\ge1296.                                  \tag{7.3}
\]

After pairing transported/common cells by their complete target-neighbourhood
signatures, let `g_D` old-outside boundary cells be gained and `ell_D` old
boundary neighbours be lost.  Then

\[
                         g_D-\ell_D\ge1.              \tag{7.4}
\]

In particular at least one of the at most `180` new two-braid boundary
cells must lie outside the old `N(D)` and acquire a neighbour in `D`.

#### Proof

Deficiency at most `24` applied to the fixed target family `D` gives

\[
 |D|-|N_{G'}(D)|\le24.
\]

Use `|D|=1320` for (7.3), then subtract the old value `1295` to obtain
(7.4).  The paired common cells cancel from the neighbourhood difference,
so the gain occurs in the contracted boundary bank. ∎

This proposition is necessary but projected.  It neither supplies an
augmenting path nor proves that a corresponding target pin is compatible
with all other pins.

### Theorem 7.2 (projected portal plus common-`Q` lift)

Assume first that the old matching `M` is equipped with a simultaneous
common-`Q`-feasible pin injection `Phi` on its matched target domain.  Suppose
a final multi-braid carrier `T'` satisfies all of the following.

1. It is a deck-exact Johnson path, depth-three resident, and preserves every
   required upper support layer by (3.4).
2. In its projected lower graph there are `r+1` vertex-disjoint
   `M_0`-augmenting paths.  Equivalently, its Hall matching is larger than
   the H25 matching.
3. Along those paths, replace precisely the alternating target pins, retain
   and transport every protected off-path pin from `Phi`, and let the
   resulting partial pin injection on `|M|+1` targets be `Phi'`.
4. The final cores `K'_p` of `Phi'` pass (5.2)--(5.4), equivalently the local
   audit of Theorem 5.1 passes together with the unchanged interior.

Then the maximal common word `A'_p=K'_p` is one literal word which realizes
all pins in `Phi'`, has `D^3A'=T'`, and installs one more lower target than
the old pinned matching.

#### Proof

The disjoint augmenting paths give a matching of size

\[
 |M_0|+(r+1)=|M|+1.
\]

This proves only an injective pin assignment.  Hypothesis 4 and the exact
common-word theorem then realize that entire assignment simultaneously by
`A'`.  The central equality and the upper transfer follow from hypotheses
1 and 4. ∎

A particularly transparent sufficient projected portal is a new edge from a
target reached from an unmatched left vertex to an `M`-free right cell
outside `N(D)`, while no edge of the alternating route is lost.  If that
cell is native, Corollary 5.3 reduces its literal audit to (5.6).  If the new
right cell is matched, being outside `N(D)` alone is not enough: the
alternating route still has to reach an unmatched right cell.

## 8. Sharp proved/conditional boundary

The following facts are unconditional.

* The H25 one-braid local minimum does not cover the five-piece shuffle
  (0.1), nor any noncoarsening overlay in (6.6).
* Endpoint legality, all-depth shadow balance, and residence of each such
  macro have the exact finite collar criteria above.
* Exact cancellation of decorated controller/pin germs is a no-go: it cannot
  alter the DM neighbourhood or common-`Q` feasibility.
* A final common-`Q` audit is local relative to transported interior pins,
  but it is simultaneous and cannot be replaced by Hall.
* The inverse move (6.4) gives a canonical nonlocal second-neighbourhood
  entrance from H25.

The macro (0.3) now gives the actual projected H25-to-H24 step and realizes
all `1297` cells on the old H25 DM-right shore in one common word.  What is
not yet proved is the stronger hypothesis and conclusion of Theorem 7.2: a
common-`Q`-feasible pin injection on the whole old maximum matching, followed
by a transported augmentation to `16359` simultaneous pins.  The original
H25 JSON artifact contains a carrier and a projected maximum matching, not
such a global injection.  Thus H24 is an exact outer Hall descent and a
literal fixed-shore descent, but not yet a literal complete lower compiler.

The exact next target is now narrow:

1. enumerate or characterize the noncoarsening composites (6.6), or realize
   the six endpoint equations (2.3) directly in H25;
2. impose the six-connector upper ledgers (3.3)--(3.4) and final residence;
3. require a full-germ change which creates an augmenting boundary cell,
   preferably a native trace (5.5), outside the old critical neighbourhood;
4. perform the alternating pin reassignment and the final simultaneous
   common-`Q` test (5.2)--(5.4).

That is the proof-safe Shadow--Braid commutator gate beyond H25.

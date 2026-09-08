# Octahedral phase-hole slides and the odd-to-even braid gate

Date: 2026-07-30  
Lane: K  
Status: **proved an exact mixed-\(C_6\) phase-hole slide and a protected
composition theorem; audited the 121-run top-bit trace of the current K16
three-hole word.  The trace has ample scalar donor mass, but its byte artifact
does not contain the owner/compiler provenance needed to certify a literal
octahedral repair.**

## 0. Result and boundary

There is a precise correspondence between a split-active octahedral
\(C_6\) and phase-hole transport in an odd-to-even two-shore braid.  A single
mixed atom can change two low-shore phase-run lengths by

\[
        \{t,L\}\longmapsto\{h,L-h+t\},                 \tag{0.1}
\]

where \(1\le t<h\) and \(L\ge2h-t\), while leaving the two high-shore
run lengths unchanged as a multiset.  It therefore removes exactly
\(h-t\) units of low-phase curvature.  The complementary orientation gives
the same statement with the two shores interchanged.

The move is literal and squarefree, preserves every middle-owner degree,
and preserves both \(q=1\) colour multisets exactly.  With a common protected
witness bank and residence-safe collars, compatible atoms compose.  This
gives a reusable odd-to-even braid theorem, conditional on an explicit
unsplittable packing of short phase runs into protected octahedral donor
sockets and on the stated witness/compiler bank.

For the frozen length-12,873 K16 three-hole word, the top-coordinate trace has

\[
121\text{ linear runs},\qquad
60\text{ zero runs},\qquad61\text{ one runs}.         \tag{0.2}
\]

Its zero-run histogram is exactly

\[
1^{57},\quad2^2,\quad6436^1.                           \tag{0.3}
\]

At threshold four the zero-phase deficit is

\[
57(4-1)+2(4-2)=175.                                   \tag{0.4}
\]

The long run has surplus \(6436-4=6432\), so there is no scalar phase-mass
obstruction.  The normal form would use 57 transfers of size three and two
transfers of size two, hence 59 mixed atoms, if the required owner-level
sockets and compiler-transparent collars exist.

They have not yet been identified.  The byte word has nine equally minimum
alignments to its canonical lift history, and arbitrary substitutions need
not be images of factor moves.  Thus (0.3) is a strong target atlas, not a
proof that the current three-hole word admits 59 literal \(C_6\) moves.

## 1. The two-shore phase graph

Let \(|S|=2r+1\), add a new coordinate \(z\), and work in

\[
J(S+z,r+1).
\]

Its middle owners split into

\[
\mathcal H=\{z+X:X\in\tbinom Sr\},\qquad
\mathcal L=\tbinom S{r+1}.                             \tag{1.1}
\]

Call \(\mathcal H\) the tagged or high shore and \(\mathcal L\) the
untagged or low shore.  A factor chronology has phase trace

\[
\epsilon_i=1[z\in T_i].                               \tag{1.2}
\]

On every cyclic factor component meeting both shores, its maximal one-runs
are exactly the path components of the internal \(HH\) graph, and its
maximal zero-runs are the path components of the internal \(LL\) graph.
Cross edges are their endpoints.  Thus the number of runs on either shore is
half the number of cross edges, while the total number of cyclic phase runs
is the number of cross edges.  A monochromatic factor cycle is instead one
constant whole-component run.  In a linear opened word, the number of runs is
the number of phase transitions plus one.

For a threshold \(h\), put

\[
\Psi_b^{(h)}(F)=
  \sum_{C\in\mathcal R_b(F)}(h-|C|)^+,qquad b\in\{0,1\},       \tag{1.3}
\]

where \(\mathcal R_b(F)\) is the multiset of finite phase-\(b\) runs.

The same definition applies to an emitted word only when every emitted cell
has a fixed additive assignment to a retained, phase-monochromatic carrier
fragment and the old/new seam-collar masses agree or are separately booked.
Then \(|C|\) is the number of assigned emitted cells, not necessarily the
number of middle owners.  Mere intactness of a block without this assignment
does not justify the weighted lift.

## 2. The split-active octahedral cell

Fix \(R\in\binom S{r-1}\) and distinct labels \(a,b,c\in S\setminus R\).
Put

\[
H_x=R+z+x,\qquad L_{xy}=R+x+y.                        \tag{2.1}
\]

The mixed octahedral exchange is

\[
\boxed{
\{H_bH_c,\ H_aL_{ac},\ L_{ab}L_{bc}\}
\longrightarrow
\{H_aH_c,\ H_bL_{bc},\ L_{ab}L_{ac}\}.}             \tag{2.2}
\]

### Lemma 2.1 (literal phase-cell exactness)

Exchange (2.2) preserves every middle-owner degree, the complete lower
\(q=1\) colour multiset, and the complete upper \(q=1\) colour multiset.
It replaces one \(HH\), one cross, and one \(LL\) edge by one edge of each
type.  Hence it preserves the total number of phase boundaries.

#### Proof

Each of the six displayed owners is incident with one old and one new edge.
The old lower colours are

\[
R+z,\qquad R+a,\qquad R+b,                            \tag{2.3}
\]

and the new lower colours are the same three.  The old upper colours are

\[
R+z+b+c,\qquad R+z+a+c,\qquad R+a+b+c,               \tag{2.4}
\]

again the same as the new upper colours.  The edge-type assertion is visible
in (2.2).  QED.

This is stronger than a trace switch: it preserves both physical turn
palettes.  It is also the support-minimal palette-exact move which changes a
pointwise cross assignment; a four-edge alternating rectangle cannot do so.

## 3. Exact weighted run action

Delete the old \(HH\) edge \(H_bH_c\) from a cross-bounded high path.  Let
its two high fragments have additive masses \(p,q\), with \(H_b\) on the
\(p\)-side and \(H_c\) on the \(q\)-side.  Let the distinct cross-bounded
high endpoint component through \(H_a\) have mass \(d\).  Then (2.2) changes
the high run masses by

\[
             \{d,p+q\}\longmapsto\{p,d+q\}.          \tag{3.1}
\]

Similarly, delete \(L_{ab}L_{bc}\) from a cross-bounded low path, give its
\(L_{ab}\)- and \(L_{bc}\)-side fragments masses \(\bar p,\bar q\), and let
the distinct cross-bounded low endpoint component through \(L_{ac}\) have
mass \(\bar d\).  Then

\[
 \{\bar d,\bar p+\bar q\}
   \longmapsto\{\bar d+\bar p,\bar q\}.               \tag{3.2}
\]

### Lemma 3.1 (weighted tail exchange)

Equations (3.1)--(3.2) hold for any nonnegative additive mass assigned to
the retained path fragments.  In particular they hold for owner count and,
under the fragment assignment specified after (1.3), for emitted word
length.

#### Proof

Deleting the two old internal edges exposes four shore fragments.  The new
\(HH\) edge joins the \(H_a\)-fragment to the \(H_c\)-fragment, while the
\(H_b\)-fragment becomes the new high cross endpoint.  This gives (3.1).
The low calculation is identical: the new \(LL\) edge joins the old
\(L_{ac}\)-component to the \(L_{ab}\)-fragment, and the
\(L_{bc}\)-fragment becomes the cross endpoint.  Additivity proves the
weighted statement.  QED.

## 4. The phase-hole slide

### Theorem 4.1 (one-hole octahedral repair)

Fix \(1\le t<h\) and \(L\ge2h-t\).  Suppose a literal cell (2.2) has the
following current run data.

1. On the low shore, the endpoint component through \(L_{ac}\) is the short
   run of mass \(t\), and the edge \(L_{ab}L_{bc}\) lies in a donor run of
   mass \(L\), split as

   \[
   \bar p=h-t,\qquad \bar q=L-h+t.                   \tag{4.1}
   \]

2. On the high shore, the endpoint component through \(H_a\) has mass
   \(d\ge h\), and \(H_bH_c\) lies in a distinct run split as

   \[
   p=d,\qquad q=\sigma\ge1.                          \tag{4.2}
   \]

3. The three new edges are absent.

Then (2.2) is a squarefree factor switch and its phase-run action is

\[
\begin{array}{c|c}
\text{high}&\{d,d+\sigma\}\longmapsto\{d,d+\sigma\},\\
\text{low}&\{t,L\}\longmapsto\{h,L-h+t\}.
\end{array}                                            \tag{4.3}
\]

Consequently

\[
\Delta\Psi_0^{(h)}=-(h-t),qquad
\Delta\Psi_1^{(h)}=0,                                 \tag{4.4}
\]

and none of the four modified output phase runs is shorter than \(h\).
Unrelated pre-existing short runs remain.  The complementary cell repairs a
high-shore hole with the analogous formula.

#### Proof

Substitute (4.1) into (3.2):

\[
\{t,L\}\mapsto\{t+h-t,L-h+t\}=\{h,L-h+t\}.
\]

The hypothesis \(L\ge2h-t\) gives \(L-h+t\ge h\).  Substitute (4.2) into
(3.1):

\[
\{d,d+\sigma\}\mapsto\{d,d+\sigma\}.
\]

Lemma 2.1 gives degree and palette exactness.  Absence of the new edges makes
the switch squarefree.  The curvature statement follows from (1.3).  QED.

Thus the atom literally slides \(h-t\) units of phase mass from a donor run
into a short hole while recharging the opposite shore exactly.

### Corollary 4.2 (threshold four)

At \(h=4\), the two elementary hole repairs are

\[
\{1,L\}\mapsto\{4,L-3\}\quad(L\ge7),                 \tag{4.5}
\]

and

\[
\{2,L\}\mapsto\{4,L-2\}\quad(L\ge6).                \tag{4.6}
\]

Each atom touches only one short run on the repaired shore.  Since two
distinct runs of lengths below four have total mass at most six, one such
two-component exchange cannot make both of them length at least four.

### Corollary 4.3 (paired two-shore repair)

One mixed cell can repair one short run on each shore simultaneously.  If
the high inputs are \(t_1,L_1\), take

\[
d=t_1,\qquad p=h,\qquad q=L_1-h,                      \tag{4.7}
\]

and use (4.1) on the low inputs \(t_0,L_0\).  Provided

\[
L_i\ge2h-t_i\qquad(i=0,1),                            \tag{4.8}
\]

the action is

\[
\{t_i,L_i\}\longmapsto\{h,L_i-h+t_i\}
\qquad(i=0,1).                                        \tag{4.9}
\]

Thus a low-hole conveyor may pay the smaller high-phase deficit during its
first few transfers and run high-neutral thereafter.

#### Proof

Substitution in (3.1) gives
\(\{t_1,h+L_1-h\}\mapsto\{h,t_1+L_1-h\}\); the low
formula is Theorem 4.1.  Inequalities (4.8) make both residual donors at
least \(h\).  QED.

## 5. Protected composition and the exact flow gate

The phase law alone is not enough.  A factor switch may create a short run in
an old coordinate or remove the last shadow witness of a target.  The
following formulation isolates all required resources.

Call a candidate (2.2) **\((h,d)\)-transparent** if:

1. it has the phase normal form of Theorem 4.1 or Corollary 4.3 at the
   current state, with every repaired-shore action declared;
2. after deleting the old edges and inserting the new ones, every resulting
   run on every affected fragment has length at least \(h\) in each residence
   sense required by the application;
3. for every required fixed lower and upper target through depth \(d\), an
   old occurrence avoids the three deleted seams or a declared new crossing
   occurrence supplies it;
4. every arbitrary-width upper/compiler target with no avoiding occurrence
   has a declared accepting accumulated-union path through the new seams;
5. its compiler blocks are attached to retained fragments, and any changed
   seam collar has an exact literal replacement ledger.

Under the convention that a depth-\(q\) occurrence is a cyclic window crossing
\(q\) seams, one deleted seam meets at most \(q\) fixed windows.  Hence an
atom has at most \(3q\) old occurrence starts to protect on either fixed
shadow side.  This makes item 3 a finite collar test; it does not bound the
nonlocal compiler/upper intervals in item 4.

### Theorem 5.1 (protected phase-braid composition)

Let \(F_0\) be a literal odd-to-even two-shore factor with a feasible compiler,
a complete required shadow tower, and threshold-\(h\) residence in every old
coordinate outside the declared phase holes, under a fixed cyclic or
endpoint-exempt convention.  Let \(g_1,\ldots,g_s\) be a sequential family
of transparent mixed octahedral atoms such that, at every prefix,

* all old edges of \(g_j\) are selected and all new edges absent;
* the selected owner/edge supports are compatible; and
* the declared witness and compiler resources remain present.

Then every prefix is a literal exact factor with the same two \(q=1\)
palettes, the same required shadow coverage, and a feasible literal compiler.
Moreover

\[
\Psi_0^{(h)}(F_s)=\Psi_0^{(h)}(F_0)
 -\sum_{j:\text{low repair}}(h-t_j),                  \tag{5.1}
\]

with the analogous identity for high repairs.  If both shore sums equal the
corresponding initial phase curvatures, and no pure-cycle or exempt-endpoint
defect remains under the chosen convention, the final braid is
phase-resident at threshold \(h\).

A paired atom is included once in each of the two shore sums.

#### Proof

Lemma 2.1 proves factor and \(q=1\) exactness at each switch.  The collar
condition proves residence.  An old fixed-window witness can disappear only
when it crosses a deleted seam, and item 3 replaces every such last witness.
The identical avoiding-witness/accepting-path dichotomy proves arbitrary
upper and compiler preservation.  Finally Theorem 4.1 gives the additive
curvature identity prefix by prefix.  QED.

When atom halos are disjoint and use a common avoiding-witness bank, ordinary
pairwise conflicts suffice.  Otherwise the correct compatibility object is a
witness-depletion hypergraph, and exact iterative replay is required.

For a constructive finite test, let \(\mathcal C_b\) be the short runs on
shore \(b\).  A current mixed-cell socket \(s\) carries an assigned set
\(A(s)\subseteq\mathcal C_0\cup\mathcal C_1\), with at most one run from
each shore, and one donor \(D_b(s)\) for every represented shore.  Retain the
socket only when it realizes Theorem 4.1 or Corollary 4.3 and passes every
transparency test.  With \(d(C)=h-|C|\), the exact static model has one binary
variable \(x_s\) per single or paired socket and rows

\[
\sum_{s:\,C\in A(s)}x_s=1,
\qquad
\sum_{s:\,D_b(s)=D}\ 
  \sum_{C\in A(s)\cap\mathcal C_b}d(C)x_s
   \le\operatorname{cap}(D).                          \tag{5.2}
\]

Add distinct-socket, owner-support, and witness-depletion rows.  This is an
unsplittable generalized assignment/packing problem: ordinary max-flow could
split one hole's demand among several donors and is not exact.  A network
model is justified only for unit demands or after an independently proved TU
formulation which preserves the indivisible socket choice.  Without disjoint
halos, use the explicit conflict/hyperedge rows or iterative re-census.

Call the atlas **hereditarily neutral-complete** on a shore if, at every
state reachable by its certified transfers, for every deficient run \(C\),
every donor run \(D\), and every integer

\[
1\le\delta\le\min\{h-|C|,|D|-h\},                   \tag{5.3}
\]

it contains a stage-legal transparent mixed cell with shore action

\[
\{|C|,|D|\}\longmapsto\{|C|+\delta,|D|-\delta\},     \tag{5.4}
\]

and with the opposite-shore run multiset unchanged.

### Theorem 5.2 (mass criterion for a protected neutral atlas)

Suppose the atlas is hereditarily neutral-complete on both phase shores and all its
applications retain one common protected witness/compiler bank.  Write
\(M_b\) for the total phase-\(b\) mass and \(n_b\) for its run count.  Then
octahedral packets make the factor phase-biresident at threshold \(h\) if
and only if

\[
M_b\ge h n_b\qquad(b=0,1).                            \tag{5.5}
\]

#### Proof

Necessity is mass conservation.  On one shore, total deficit and surplus are

\[
D=\sum_C(h-|C|)^+,qquad S=\sum_C(|C|-h)^+.
\]

Condition (5.5) is exactly \(D\le S\).  Repeatedly transfer the minimum of a
current deficit and a current donor surplus using (5.3)--(5.4).  Each step
exhausts a deficit or a donor, so the process terminates.  Apply the same
argument on the other shore.  Transparency and the common bank invoke
Theorem 5.1 at every prefix.  QED.

The strength of this theorem is also its scope: neutral completeness is the
physical Pascal/owner routing lemma still to be proved.  The theorem turns
that local atlas statement into a global all-run construction without any
additional averaging argument.

## 6. Exact K16 phase census

Let

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and tag a cell precisely when bit 15 is present.  A linear replay gives

\[
|w|=12873,\quad |w|_1=6376,\quad |w|_0=6497.          \tag{6.1}
\]

There are 61 tagged runs and 60 untagged runs.  Both word endpoints are
tagged; cyclic identification merges the first and last tagged runs.  Thus
the cyclic phase braid has 120 runs, 60 on each shore.  The complete
untagged histogram is (0.3).  The linear short tagged runs have histogram

\[
1^3,\qquad2^1.                                        \tag{6.2}
\]

One singleton tagged run is the left endpoint run.  Excluding linear
endpoints, tagged curvature at threshold four is eight; including both
endpoints it is eleven.  Untagged curvature is 175 either way.

Cyclically, the short tagged histogram is \(1^2,2^1\), so the two shore
deficits are exactly

\[
(\Psi_0^{(4)},\Psi_1^{(4)})=(175,8).                  \tag{6.3}
\]

### Corollary 6.1 (scalar 59-slide schedule)

Ignoring owner, shadow, and compiler eligibility, the untagged trace admits
the unique demand multiset

\[
57\cdot3+2\cdot2=175.                                 \tag{6.4}
\]

The long untagged run has 6432 units of surplus above four.  Thus 59
applications of (4.5)--(4.6) would clear every untagged phase hole and leave
the donor run of length

\[
6436-175=6261.                                         \tag{6.5}
\]

During three of these transfers, Corollary 4.3 can simultaneously repair the
two tagged singleton runs and the tagged length-two run, drawing eight units
from the tagged run of length 820 and leaving length 812.  Thus 59 is the
exact trace-level optimum for repairing both shores within the neutral-or-
paired octahedral tail-exchange normal form.  It does not prove that any of
the 59 required octahedral cells exists in the physical carrier.

The mass inequalities of Theorem 5.2 hold with enormous slack:

\[
6497\ge4\cdot60,\qquad6376\ge4\cdot60.                \tag{6.6}
\]

## 7. Why the trace is not yet a literal C6 atlas

The frozen word is a sequence of arbitrary nonzero masks, not a recorded
middle-owner chronology.  A top-bit boundary in this byte word therefore
does not determine:

* the two rank-eight owners incident with a carrier seam;
* the core \(R\) and labels \(a,b,c\) of (2.2);
* which compiler cells belong to which retained owner fragment; or
* the shadow witnesses consumed by rethreading that fragment.

This is visible even at the singleton holes.  The 57 isolated untagged cells
have popcount histogram

\[
1^3,\quad2^{15},\quad3^{24},\quad4^{10},\quad5^5,     \tag{7.1}
\]

so none is a rank-eight middle owner.  They are erosion/compiler letters.

The three pieces of (2.2) are also forced by degree balance.  The \(LL\)
replacement alone gives degree drift \(+1\) at \(L_{ac}\) and \(-1\) at
\(L_{bc}\).  The cross replacement cancels those low-shore drifts but creates
the corresponding high-shore drift, which is cancelled only by the \(HH\)
replacement.  A one-shore K15 atom is therefore not yet an odd-to-even phase
move: a Pascal/two-rail lift must supply its companion cross and opposite-
shore pieces.

This ambiguity is concrete.  The existing exact alignment audit finds nine
equally minimum alignments to the canonical lift history, each with 197
substitutions and different deletion positions.  Therefore the phase trace
alone cannot select a proof-safe carrier move.  A claimed C6 repair must
first authenticate one occurrence-level provenance map, or work directly at
the literal word level and replay every OR target.

This is the first exact missing interface, not a scalar capacity problem.

The authenticated canonical lift

```text
answers/k16_upper12876.word
SHA-256 9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8
```

has exactly two linear phase runs, of lengths 6438 and 6438.  A mixed
octahedral switch preserves the number of cross edges and hence the number of
cyclic phase boundaries.  It can therefore redistribute the already
interleaved 120-boundary incumbent, but it cannot explain how the canonical
two-run lift first became a 121-linear-run braid.  That initial interleaving
requires a boundary-creating compiler operation outside the C6 transfer
class.

## 8. Reusable odd-to-even braid theorem

Define \(\operatorname{OPR}(r,h,d)\) to be the following assertion.

> Every short phase run in the chosen odd-to-even two-shore lift has a
> transparent mixed-octahedral donor socket, and these sockets admit a
> sequential binary packing satisfying (5.2), with exact prefix
> freshness and a common protected compiler/witness bank.

### Theorem 8.1

If an all-depth-complete odd source factor has an odd-to-even two-shore lift
which itself has the complete protected shadow tower, a feasible literal
compiler, threshold-\(h\) old-coordinate residence, and
\(\operatorname{OPR}(r,h,d)\), then mixed octahedral switches produce a
phase-resident even factor which preserves both \(q=1\) palettes, every
protected shadow through depth \(d\), and the declared literal compiler.

#### Proof

Choose the saturating routing and apply its atoms in the certified order.
Theorem 5.1 gives every conclusion and clears the phase curvature.  QED.

This theorem is uniform in \(r\).  Its hypotheses are finite and physical:
they ask for an occurrence-labelled socket packing, not an asymptotic entropy or
orbit count.  The K16 121-run braid shows that the desired object need not be
a one-seam lift and that scalar donor mass is overwhelmingly sufficient.

The seven-orbit K15 descent proves that all-depth-safe octahedral cells can
regenerate after earlier packets and can be composed at positive density.
It does not prove \(\operatorname{OPR}\): those cells live in one Johnson
factor, whereas every phase portal requires the linked \(HH\), cross, and
\(LL\) pieces of (2.2) plus a compiler-fragment occurrence map.  The descent
is therefore a supply theorem for one layer of the desired atlas, not yet the
odd-to-even lift itself.

For the frozen K16 incumbent the exact next audit is therefore:

1. choose one of the nine byte alignments and additionally authenticate a
   carrier-owner/fragment-to-byte occurrence map, or construct such a map
   directly without using an edit alignment;
2. attach every one of the 59 short zero runs to its underlying low-shore
   owner component;
3. enumerate only mixed cells incident with those components and the long
   donor component;
4. test (4.1)--(4.2), all old-coordinate collars, the complete shadow witness
   ledger, and the exact OR-provider ledger; and
5. solve the resulting unsplittable conflict packing, re-censusing after every
   accepted orbit or packet.

## 9. Frozen artifacts and scope

The light trace auditor is

```text
scratch/audit_k16_12873_top_phase_braid_20260730.py
SHA-256 f91bbf282a09b0769e2c3edf4a56f95d06f0006d5bf458409ab9168500d7f2d3
```

and its compact census is

```text
scratch/k16_12873_top_phase_braid_20260730.audit.json
SHA-256 9c257a916350ce3fc6b44dc41523b5972dccfa7002cea049a737455040da6f6c
```

The ambiguous canonical-lift alignment and byte provenance are frozen in

```text
scratch/k16_12873_repaired_partial_exact_edit_ledger_20260730.audit.json
SHA-256 ae6b54352575bd6478291d6ef84dd8f0addf92e2a9f0e51af40fc2328a61e2fb
```

The mixed-cell algebra and authenticated finite cells are independently
recorded in

```text
MATH_THEOREM_K_PROTECTED_OCTAHEDRAL_RECHARGE_AND_PAIRED_SHELL_PACKET_20260730.md
SHA-256 eedb0ee47f52a1e174cde3d82d76ec033ee6b45d2fd31794d929d90b98e4c909
```

No heavy local search was used.  This report does not claim that the current
three-hole word is universal, that it has a unique lift history, that its
phase holes possess owner-level C6 sockets, or that K16 is solved.  It proves
the exact local transport law and the finite protected-routing theorem needed
to turn such sockets into a reusable odd-to-even braid.

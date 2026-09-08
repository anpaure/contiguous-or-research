# Closed complement circuits: exact closure, anchored Hall, and an LLL criterion

Date: 2026-07-31  
Lane: A, probabilistic/expansion  
Status: unconditional abstract theorems and a quantitative application to the
authenticated `K17` complement catalogue; no `K17` repair or all-dimension
RSB theorem is claimed

## 0. Result

The `10--45` providers attached to each current rank-ten hole are raw
one-colour edge-replacement columns.  They are not physical repair choices.
Every nonidentity raw column has nonzero owner-degree boundary.  A physical
choice first has to close with other columns into a degree-balanced
alternating-circuit packet, pass the Hamilton-path cut, and carry exact
residence and upper-shadow guards.

This note proves three statements.

1. Degree balance is exactly alternating-circuit closure.
2. In a private closed-packet face, simultaneous service is exactly Hall.
3. For a bounded-interaction closed-packet bank, an independent transversal
   exists whenever

   \[
        L_{\min}^2\ \ge\ 2eL_{\max}\Delta .                 \tag{0.1}
   \]

   Here `Delta` is the **candidate** conflict degree after all physical,
   residence, and provider-anchor conflicts have been inserted.  If
   `lambda=L_max/L_min`, (0.1) is

   \[
        L_{\min}\ \ge\ 2e\lambda\Delta .                   \tag{0.2}
   \]

Private provider anchors have an explicit cost.  If the non-anchor conflict
degree is `Delta_0`, a candidate exports at most `a_A` anchors and invalidates
at most `a_D` possible anchors, while an anchor is invalidated by at most
`kappa_D` candidates and exported by at most `kappa_A` candidates, then

\[
 \Delta\le
 \Delta_0+a_A\kappa_D+a_D\kappa_A.                         \tag{0.3}
\]

For the `K17` raw range `L_min=10,L_max=45`, (0.1) would require
`Delta=0`.  Even after truncating every list to ten, the criterion permits
only `Delta<=1`.  More importantly, the raw columns have not passed circuit
closure, so neither numerical substitution is currently legitimate.

## 1. The complete raw complement master

Freeze the authenticated `4108`-owner marked path and its two crossing
edges.  Let `C` be the `20202` complementary rank-nine owners and let
`Gamma` be the `20201` unused rank-eight lower colours.  For every
`c in Gamma`, let

\[
 e_c^0=\{u_c,v_c\}
\]

be the current complement edge of colour `c`.  Every alternative edge of
that colour has the form

\[
 e=\{u,v\},\qquad u,v\in C,\qquad u\cap v=c.                \tag{1.1}
\]

The raw column `(c,e)` means delete `e_c^0` and add `e`.  Its owner-degree
boundary is

\[
 b(c,e)={\bf1}_u+{\bf1}_v-{\bf1}_{u_c}-{\bf1}_{v_c}
       \in {\mathbb Z}^{C}.                                 \tag{1.2}
\]

The authenticated complete catalogue has `545721` off-source columns.  Its
rank-ten service ledger is

```text
current rank-ten holes                           1900
raw columns adding one                           66223
distinct lower colours used                      16471
raw support per hole                             10..45.
```

These are exact singleton-list degrees, not circuit-list degrees.

### Theorem 1.1 (degree balance equals alternating-circuit closure)

Let `S` be a set of raw columns using each colour at most once.  Replace the
corresponding old edges by the new edges.  The following are equivalent.

1. Every complementary owner retains its old degree.
2. `sum_{(c,e) in S} b(c,e)=0`.
3. After common edges are suppressed, the old edges and new edges decompose
   into edge-disjoint even circuits alternating old, new, old, new.

Every off-source singleton column has nonzero boundary and hence is not a
physical degree-preserving move.

#### Proof

The coefficient of owner `v` in the sum in item 2 is exactly its new degree
minus its old degree, proving `1 iff 2`.

Colour every deleted edge red and every added edge blue.  Under item 2,
every vertex has the same red and blue degree.  At each vertex, pair its red
incidences bijectively with its blue incidences.  Starting from an incidence,
traverse its edge and then the oppositely coloured incidence paired to the
arrival incidence.  This successor rule is a permutation of the finite set
of incidences, and every orbit projects to an even closed alternating trail.
Splitting a repeated-vertex trail at a repeated state gives edge-disjoint
alternating circuits.  This proves item 3.  Conversely every alternating
circuit contributes one red and one blue incidence at each of its vertices,
so a union of them has zero boundary.

Finally, an off-source edge with zero boundary would have the same unordered
endpoint pair as `e_c^0`, and hence would be `e_c^0` itself.  Thus every
nonidentity singleton has nonzero boundary.  \(\square\)

### Corollary 1.2 (the graphic row is additional)

Circuit closure preserves owner degrees and the complete lower-q1 colour
multiset, but it need not preserve the complement Hamilton path.  A balanced
toggle can split that path into one boundary-to-boundary path and disjoint
cycles.  Thus the usual proper-subset graphic cuts, or an equivalent literal
Hamilton-ear certificate, remain necessary.

#### Proof

The frozen crossing edges leave two complement boundary owners of internal
degree one and all other complement owners of internal degree two.  Any
balanced selection therefore has one path between the boundary owners and
zero or more cycles.  Degree balance alone does not exclude the cycles.
\(\square\)

## 2. Closed packets and exact anchors

A **closed exchange packet** `p` is a finite set of raw columns together
with all of the following certificates.

1. **Zero signatures.**  Its owner-degree boundary and signed lower-colour
   vector are zero, and it changes no edge of the marked path or its two
   prescribed crossings.
2. **Hamilton certificate.**  Its old/new symmetric difference is supplied
   with an alternating-circuit decomposition and the toggled complement is
   one boundary-to-boundary Hamilton path.
3. **Residence collar.**  Every coordinate run meeting the changed support
   is replayed through the full declared collar; the packet repairs its
   assigned run block and creates no undeclared bad run.
4. **Shadow signature.**  Every destroyed and created named interval witness
   at upper ranks ten, eleven and twelve is recorded with its literal
   occurrence span.

A particularly transparent sufficient Hamilton certificate is a **rooted
ear**: inside a complementary interval `I`, the old and new edges each form
a path through exactly the vertices of `I` with the same two boundary
owners, and all other incidences are unchanged.  Pairwise collar-disjoint
rooted ears compose to one Hamilton path.  This is stronger than individual
Hamilton safety; two arbitrary individually safe global circuits need not
compose safely.

Let `T_0` be the set of upper targets already covered by the base chronology.
Choose one named base witness `w_T^0` for every `T in T_0`.  A packet `p`
exports:

* a new named witness for every assigned hole it repairs; and
* a replacement named witness for every `T in T_0` whose base witness is
  invalidated by `p`.

Write `A(p)` for these exported anchor footprints and `D(p)` for every named
catalogue-witness footprint touched by `p`; a touched footprint is
conservatively treated as invalidated even when it happens to remain a
witness after `p` alone.  Declare `p,p'` to conflict whenever

\[
       A(p)\cap D(p')\ne\varnothing
       \quad\hbox{or}\quad
       A(p')\cap D(p)\ne\varnothing .                        \tag{2.1}
\]

Also declare a conflict for shared exchange resources, overlapping residence
collars, a noncomposable Hamilton transition, or any marked-path/lower-palette
collision.

### Lemma 2.1 (private anchors prevent rotating casualties)

Let `P` be a conflict-free family of closed packets.  Assume every old upper
target has its selected base witness or the replacement anchor of each packet
which destroys that base witness, and every initially missing target is
assigned to some packet in `P`.  Then every upper target at ranks ten through
twelve is covered after all packets in `P` are applied.

#### Proof

Fix an old target `T`.  If no selected packet destroys `w_T^0`, that witness
survives.  Otherwise choose a selected packet `p` which destroys it.  By
definition `p` exports a replacement anchor for `T`.  Equation (2.1) and
conflict-freeness say that no other selected packet destroys that anchor, so
it survives the composite toggle.

For an initially missing target, its assigned selected packet exports a new
anchor, and the same argument protects it from every other selected packet.
\(\square\)

This is why target multiplicities cannot be treated as independent random
deficits.  A repair is valid only together with a named witness which the
rest of the random choice is forbidden to erase.

## 3. Exact Hall in the private face

Partition the violated rows into repair blocks `D`; one block may contain
several residence and shadow rows which must be repaired together.  Let `R`
be a bank of closed packets.  Suppose distinct members of `R` have disjoint
protected collars, compatible rooted-ear transitions, and mutually private
anchors.  Let `N(d) subset R` be the packets certified to repair block `d`.

### Theorem 3.1 (private closed-packet Hall theorem)

There is a simultaneous physical repair using a distinct packet for every
block if and only if

\[
             \left|\bigcup_{d\in S}N(d)\right|\ge |S|
             \qquad(S\subseteq D).                           \tag{3.1}
\]

#### Proof

Under the private-bank hypotheses, any set of distinct packets composes:
zero signatures add, rooted ears preserve the Hamilton path, disjoint full
collars preserve residence, and Lemma 2.1 preserves all upper targets.  A
repair is therefore exactly a matching from `D` into `R`.  Hall's theorem
gives (3.1).  \(\square\)

The raw assertion `|N({d})|>=10` checks only singleton subsets of (3.1), and
does so before circuit closure.  It gives no information about a large set
of holes whose raw columns may share the same lower colours or whose degree
boundaries can close only together.

## 4. Bounded interaction and the local lemma

For every repair block `d`, let `L_d` be a list of closed packets.  Form the
candidate conflict graph `K` on the labelled candidates `(d,p)`, putting
edges only between different lists and using all conflicts from Section 2.
Assume that every independent transversal of `K` composes literally to the
declared physical chronology.  Put

\[
 L=\min_d|L_d|,\qquad U=\max_d|L_d|,
 \qquad \lambda=U/L,                                        \tag{4.1}
\]

and let `Delta` be the maximum degree of a candidate in `K`.

### Theorem 4.1 (anchored independent-transversal LLL)

If `Delta=0`, a simultaneous repair exists.  If `Delta>=1` and

\[
                         L^2\ge 2eU\Delta,                   \tag{4.2}
\]

then a simultaneous repair exists.  Equivalently, it suffices that

\[
                         L\ge 2e\lambda\Delta.               \tag{4.3}
\]

#### Proof

Choose one candidate independently and uniformly from every list.  For every
conflict edge between candidate `p in L_d` and candidate `p' in L_{d'}`,
let `B_{p,p'}` be the event that both are chosen.  Then

\[
                 \Pr(B_{p,p'})={1\over|L_d||L_{d'}|}
                              \le L^{-2}.                    \tag{4.4}
\]

This event is independent of every conflict event not involving random
variable `d` or `d'`.  The total number of conflict edges incident with all
candidates in one list is at most `U Delta`.  Hence a bad event depends on
at most

\[
                         2U\Delta-1                          \tag{4.5}
\]

other bad events.  The symmetric Lovasz local lemma applies because

\[
 eL^{-2}\bigl((2U\Delta-1)+1\bigr)\le1.                     \tag{4.6}
\]

It yields an outcome containing no conflict edge, hence an independent
transversal.  The composition hypothesis and Lemma 2.1 turn that transversal
into the claimed physical repair.  \(\square\)

### Corollary 4.2 (balanced truncation)

If every list has at least `L` candidates, one may retain any `L` from each
list.  The sufficient condition becomes

\[
                            L\ge2e\Delta.                    \tag{4.7}
\]

The candidate degree can only decrease under truncation.

### Proposition 4.3 (explicit anchor contribution)

Split conflicts into non-anchor conflicts, of maximum degree `Delta_0`, and
the two anchor conflicts in (2.1).  Suppose

\[
 |A(p)|\le a_A,\qquad |D(p)|\le a_D                         \tag{4.8}
\]

for every candidate.  Suppose every footprint is invalidated by at most
`kappa_D` candidates and is exported as an anchor by at most `kappa_A`
candidates.  Then

\[
             \Delta\le
             \Delta_0+a_A\kappa_D+a_D\kappa_A.              \tag{4.9}
\]

In the symmetric case `a_A,a_D<=a` and
`kappa_A,kappa_D<=kappa`,

\[
                         \Delta\le\Delta_0+2a\kappa.         \tag{4.10}
\]

#### Proof

At most `a_A kappa_D` candidates invalidate one of the anchors of `p`.
At most `a_D kappa_A` candidates export an anchor invalidated by `p`.
Adding the non-anchor neighbours proves (4.9), and (4.10) follows.  \(\square\)

Thus a genuinely private anchor bank is useful twice: it prevents rotating
casualties and keeps the LLL dependency degree small.

### Proposition 4.4 (partial nibble bound)

Activate every repair block independently with probability `theta`, and on
each active block choose one candidate uniformly.  Retain a chosen candidate
only if it has no conflict with another chosen candidate.  Then the expected
number of retained blocks is at least

\[
       |D|\,\theta\left(1-\frac{\theta\Delta}{L}\right).     \tag{4.11}
\]

Consequently, when the residual instance regenerates the same list and
conflict bounds after every nibble, a constant fraction can be frozen in
each round whenever `Delta/L=O(1)`.  Finishing all blocks still requires
either Theorem 4.1 on the residue or a separate absorber.

#### Proof

Condition on block `d` choosing candidate `p`.  Each of the at most `Delta`
conflicting candidates belongs to another block and is chosen with
probability at most `theta/L`.  The union bound gives conditional survival
probability at least `1-theta Delta/L`.  Multiply by the activation
probability `theta` and sum over blocks.  The retained choices are
conflict-free by construction.  \(\square\)

This is only a partial packing statement.  It cannot be iterated from
marginal counts alone: the packet catalogue and every private anchor must
survive conditioning on the earlier rounds.

### Corollary 4.5 (exchange-hypergraph load criterion)

Suppose every non-anchor incompatibility is witnessed by a shared physical
resource.  If a packet uses at most `r` resources and every resource belongs
to at most `mu` labelled candidates, then

\[
                       \Delta_0\le r(\mu-1).                 \tag{4.12}
\]

Consequently it suffices that

\[
 L^2\ge 2eU\bigl(r(\mu-1)+a_A\kappa_D+a_D\kappa_A\bigr).   \tag{4.13}
\]

#### Proof

For each of the at most `r` resources used by `p`, there are at most
`mu-1` other labelled candidates using it.  The union bound gives (4.12),
with multiple shared resources only overcounting.  Combine (4.12),
Proposition 4.3, and Theorem 4.1.  \(\square\)

Thus the useful expansion datum is not raw target degree.  It is large
closed-packet list size compared with the maximum load of the exact physical
resources and private anchors carried by those packets.

## 5. Quantitative `K17` consequence

The current exact data give

```text
middle owners and lower-q1 colours              exact, 24310 each
marked owner bank                                fixed, 4108 owners
upper holes at ranks 10/11/12                    1900 / 911 / 128
off-source raw complement columns                545721
rank-ten raw support per current hole             10..45.
```

The complete edge catalogue removes the *individual* rank-ten support
obstruction which was present in the fixed macro/packet skeleton.  It does
not remove the joint obstruction.  In particular:

1. every off-source raw column has nonzero owner boundary by Theorem 1.1;
2. no list of balanced Hamilton-safe packets has yet been extracted;
3. no corresponding list count is known for rank-eleven or rank-twelve
   holes or for the residence/replay blocks; and
4. no private anchor load or candidate conflict degree has been bounded.

Even if one incorrectly treated the raw rank-ten columns as candidates,
Theorem 4.1 would give

\[
  10^2\ge 2e\cdot45\cdot\Delta.                              \tag{5.1}
\]

Since `100/(90e)<1`, the full-list criterion allows only `Delta=0`.
After truncating every list to ten, (4.7) allows only `Delta<=1`, because

\[
                  {10\over2e}<2.                              \tag{5.2}
\]

Physical circuit packets will generally interact through degree closure,
Hamilton fragments, residence collars, and shared interval anchors.  The
raw support range therefore supplies no K17 LLL margin.

The first proof-safe finite object to enumerate is not another raw service
edge.  It is, for each service edge, a zero-boundary packet containing that
edge and satisfying:

```text
one edge per lower colour;
owner-degree zero;
one complement Hamilton path with the fixed boundary owners;
marked-path and crossing-edge preservation;
exact residence/replay collars;
named upper-rank 10--12 creation and destruction footprints.
```

Only after deduplicating those packets should one measure `L,U,Delta` and
the anchor loads in Proposition 4.3.  A positive Hall or LLL conclusion at
that packet level would be a theorem; the present `10--45` edge census is
not one.

## 6. Dimension-uniform hypothesis sufficient for RSB

The correct all-dimension hypothesis is the following joint statement.

### Anchored closed-packet expansion `ACPE(m)`

Starting from the recursively supplied physical owner/lower-palette state in
dimension `m`, there are:

1. a collection of **joint repair blocks** covering every residence,
   all-depth upper-shadow, erosion-envelope/compiler, port, and common-cap
   defect which is not already protected;
2. for every block, a list of physical zero-signature alternating-circuit
   packets with an accepting coherent orientation and Hamilton certificate;
3. a base witness/augmenting-path anchor bank for all already accepted RSB
   rows, and packet-specific replacement anchors for every spent member of
   that bank;
4. an exact composition conflict graph, including cross-depth, compiler,
   socket, and anchor conflicts; and
5. parameters `L_m,U_m,Delta_m` satisfying

\[
                  L_m^2\ge2eU_m\Delta_m.                     \tag{6.1}
\]

The word **joint** is essential: a residence row, an upper target and a
compiler match sharing one occurrence belong to the same signature system.
No independence of rankwise deficits is assumed.

### Theorem 6.1 (`ACPE(m)` gives one regenerative step)

If the incoming state is an accepted RSB state apart from the declared
repair blocks and `ACPE(m)` holds, then there is an accepted terminal RSB
state in dimension `m`.  If `ACPE(m)` is available at every recursive step
with the required exported port state, it supplies the regenerative
shadow--braid induction.

#### Proof

Apply Theorem 4.1 to choose one packet for every joint repair block.  Zero
signatures preserve physical middle degree two, exact lower ownership and
the fixed protected state.  The Hamilton composition certificates give one
coherently oriented carrier.  Full residence collars repair all declared
run blocks.  Lemma 2.1 and its identical named-path version for compiler
augmentations preserve old accepted rows and install every missing row.
The exported terminal port state is accepted by hypothesis, so the complete
RSB tuple is accepted.  Iterating this implication proves the second
sentence.  \(\square\)

This is a sufficient all-`m` theorem, not a proof that `ACPE(m)` holds.  It
also explains what must replace the false heuristic that many marginal
providers make the deficits independent.

## 7. Adversarial audit

* The LLL is applied only after exact circuit closure.  Substituting raw
  edge columns for packet candidates is invalid.
* Individual Hamilton safety is insufficient.  The theorem requires rooted
  ear composition or an independently verified all-independent-sets
  composition rule.
* Rank-eleven and rank-twelve witnesses are interval objects, so their
  signatures are not sums of edge-colour indicators.  Named occurrence
  anchors and their footprints are indispensable.
* Singleton support does not imply Hall expansion.  Shared lower colours or
  a common degree cut can collapse a large union of raw lists.
* The current K17 upper ranks thirteen through seventeen are complete, but
  any prospective packet theorem must also protect named witnesses there if
  it can touch them.
* Common-cap Hall is not a consequence of this K17 specialization.  It is
  covered by Theorem 6.1 only when its exact cell/matching state is included
  in the packet signatures and anchor conflict graph.

Accordingly, the strongest unconditional K17 conclusion is a precise
negative one: `10--45` raw service abundance is quantitatively and
structurally insufficient for the present LLL.  The minimal positive input
still missing is an anchored balanced-circuit catalogue with measured
`L,U,Delta`.

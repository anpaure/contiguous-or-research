# The exact `k=15` carrier as an odd-to-even source: collar transversals and the dense `BB` restoration gate

Date: 2026-07-29  
Lane: K  
Status: unconditional raw-certificate theorem and sharp architecture-specific
obstructions.  No `k=16` word and no complete complement braid are claimed.

## 0. Result

Let

\[
 T=D^3(\texttt{answers/k15.word})
\]

and restore the audited cyclic factor behind this opened path.  Its component
lengths are `6390,45`; it is positive-resident through depth three and covers
every lower and upper fixed-window shadow at every depth.  The pointwise
complement is not resident.  All cyclic dual defects lie on the large
component, with short-zero histogram

\[
 R_1=330,\qquad R_2=585,\qquad R_3=1095.       \tag{0.1}
\]

The raw opened path has six boundary zero fragments and exactly `2010`
internal defects,

\[
 1^{329}2^{586}3^{1095}.                         \tag{0.2}
\]

The main conclusions are as follows.

1. Every replacement factor on the same middle vertices whose complement is
   depth-three resident must remove at least

   \[
   \boxed{1230}
   \]

   old Johnson edges.  This is an exact interval-transversal number, with a
   matching `1230`-point transversal and `1230` pairwise disjoint dual
   collars.  If the replacement remains lower-q1 exact, it must also add at
   least `1230` colour-restoring edges, so its edge symmetric difference has
   size at least `2460`.

2. The obstruction respects all source symmetry.  Coordinate rotation shifts
   the large cycle by `1704=4*426`.  The `2010` physical collars quotient to
   `134` circular intervals on `Z_426`, of sizes

   \[
   2^{22}3^{39}4^{73},
   \]

   and their exact transversal number is `82`.  Its fifteen translates give
   the physical optimum `82*15=1230`.  Thus symmetry imposes no extra loss;
   it identifies an explicit dense `82`-orbit braid target.

3. A stronger q1 obstruction excludes every complement construction made
   from preserved old `BB` pieces and mixed `AB` seams alone.  There are `270`
   bad collars, or `18` quotient collars, all of whose possible cut edges
   carry globally unique upper-union colours.  Their exact transversal is
   `240` physical edges, or `16` quotient edge orbits.  In the complementary
   `B` rail these become distinct q1 colours containing the new coordinate
   `z`; an `AB` seam has z-free intersection and restores none of them.
   Therefore a cyclic repair needs at least `240` genuinely new `BB`
   colour-restoring adjacencies.  Even allowing the two global q1 boundary
   cells, a linear compiler still needs at least

   \[
   \boxed{238\text{ new }BB\text{ restorations}.}       \tag{0.3}
   \]

4. Exact load-neutral trades are also excluded.  The cyclic upper-window
   rank-deficit moments at depths `2,3,4` are

   \[
   (E_2,E_3,E_4)=(330,1245,3255).                \tag{0.4}
   \]

   These moments determine `(R_1,R_2,R_3)`.  Hence a trade preserving the
   exact upper-window multiset, or merely its rank-load vector through depth
   four, cannot repair dual residence.  A viable trade must preserve target
   **support** while being strongly load-nonneutral.

The remaining live architecture is consequently not a bounded seam braid.
It is a dense same-rail alternating-circuit packet, followed by a small number
of legal cross-rail ports and the exact compiler.

## 1. Frozen source and the two complement rails

The canonical word is

```text
answers/k15.word
SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
```

Its third derivative is a length-`6435` Johnson Hamilton path through every
rank-eight subset of `[15]`.  The hidden cyclic source is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.best.json
SHA-256 0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555
```

with components in

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151.
```

The opened chronology first traverses the `6390`-cycle and then the
`45`-cycle across the audited foreign seam.  Its endpoint wrap is not a
Johnson edge, so linear and restored-cyclic run counts must not be mixed.

For a cyclic source state `T_i`, define child middle states

\[
 A_i=T_i,\qquad
 B_i=\{z\}\cup([15]\setminus T_i).                \tag{1.1}
\]

For every old coordinate `x`, the `B` trace is the complement of the `A`
trace.  Thus `B` positive residence is exactly `T` zero residence.  A
pointwise common-order complement is biresident if and only if every
nonconstant one-run and every nonconstant zero-run of `T` has length at
least four.

### Theorem 1.1 (exact complement suspension)

Let `F_A` and `F_Q` be arbitrary oriented Johnson factors on
`binom([15],8)`.  Then

\[
 F_A\ \sqcup\ \bigl(\{z\}+([15]\setminus F_Q)\bigr)       \tag{1.2}
\]

is a spanning factor of the two shores of `binom([16],8)`.  The first shore
is depth-three resident exactly when `F_A` has minimum one-run four, and the
second is depth-three resident exactly when `F_Q` has minimum zero-run four.
For every `q`,

\[
 \bigcap_{h=0}^q\bigl(\{z\}\cup([15]\setminus Q_{i+h})\bigr)
 =\{z\}\cup\left([15]\setminus\bigcup_{h=0}^qQ_{i+h}\right), \tag{1.3}
\]

\[
 \bigcup_{h=0}^q\bigl(\{z\}\cup([15]\setminus Q_{i+h})\bigr)
 =\{z\}\cup\left([15]\setminus\bigcap_{h=0}^qQ_{i+h}\right). \tag{1.4}
\]

Consequently, bilateral all-depth completeness of `F_A,F_Q`, positive
residence of `F_A`, and dual residence of `F_Q` give a resident,
all-depth-complete even factor.  Opening, connecting the components, and
finding a literal compiler remain separate requirements.

An `A` state `P` and a `B` state `z+([15]\setminus Q)` form a Johnson edge
if and only if

\[
 |P\cap Q|=1.                                      \tag{1.5}
\]

If `P cap Q={u}`, the seam is literally the swap

\[
 P=(P\setminus\{u\})+u
 \quad\longleftrightarrow\quad
 (P\setminus\{u\})+z.                             \tag{1.6}
\]

The port graph on the two rank-eight decks, with adjacency (1.5), is
eight-regular bipartite: for fixed `P`, choose `u in P` and take
`Q=([15]\setminus P)+u`.  Hence it has a perfect matching.  Scalar cross-port
supply is therefore not the obstruction; the difficulty is simultaneous
collar, colour, tower and compiler compatibility.

### Proof

The two shores in (1.2) partition the middle layer according to whether `z`
is absent or present.  Equations (1.3)--(1.4) are De Morgan's laws.  They
exchange the lower and upper towers on the complemented shore and prove the
coverage assertion.  The residence assertion follows pointwise from
complementing every old-coordinate trace.  Finally, both child states have
rank eight and their intersection is `P\setminus Q`; it has rank seven
exactly when `|P cap Q|=1`.  In that case `P union Q=[15]`, proving (1.6).
Regular bipartite graphs have perfect matchings.  `square`

This complement rail is distinct from the Pascal facet rail

\[
 \{z\}\cup(T_i\cap T_{i+1}).                       \tag{1.7}
\]

The two constructions have different residence hazards.  The `2010` count
in this note belongs to (1.1), not to the facet rail (1.7).

## 2. Exact run structure

### Theorem 2.1 (linear and cyclic biresidence audit)

The opened path has short positive-run histogram

\[
 1^2 2^2 3^2.
\]

All six are boundary fragments.  There is no internal positive residence
defect.  Its short zero-run histogram is

\[
 1^{331}2^{588}3^{1097}=2016.                     \tag{2.1}
\]

Exactly six are boundary fragments, one at each length on each side.  The
internal histogram is (0.2).  Of these `2010` internal defects, `2009` lie
inside the large opened block and one length-two gap crosses the foreign
seam.  None lies inside the `45` block.

After restoring the two source cycles, the `6390` component has short-zero
histogram (0.1), uniformly

\[
 1^{22}2^{39}3^{73}                               \tag{2.2}
\]

per coordinate.  The `45` component is already biresident: for every
coordinate its one-run lengths are `7,7,10` and its zero-run lengths are
`6,6,9`.

The cyclic source remains lower-q1 exact and has upper-q1 load histogram

\[
 1^{3675}2^{1230}3^{100}.                         \tag{2.3}
\]

Every lower and upper fixed-window target is present at every depth
`1<=q<=7`.

### Proof

The audit forms `D^3` directly from the canonical word, checks the complete
rank-eight deck and every Johnson transition, and enumerates maximal binary
runs coordinate by coordinate.  It separately loads the two cyclic
components, checks their cycle closures, and repeats the enumeration with
cyclic indexing.  It then enumerates every fixed-window lower intersection
and upper union at every depth.  All assertions are literal counts; no
solver output or probabilistic inference is used.  The audit is recorded in
Section 8.  `square`

## 3. The collar-transversal theorem

Let

\[
 e_i=\{T_i,T_{i+1}\}
\]

denote an old Johnson edge, with cyclic or linear indexing as appropriate.
Suppose the trace of coordinate `x` contains an internal short zero gap

\[
 t_{a-1}(x),t_a(x),\ldots,t_{b-1}(x),t_b(x)
   =1,0,\ldots,0,1,                               \tag{3.1}
\]

where `s=b-a` lies in `{1,2,3}`.  Its **closed old-edge collar** is

\[
 I(a,b)=\{e_{a-1},e_a,\ldots,e_{b-1}\}.           \tag{3.2}
\]

It contains `s+1` edges.  Notice that both boundary edges and every internal
gap edge are legitimate ways to break the forced subpath.

### Lemma 3.1 (forced-collar lemma)

Let `F'` be any degree-two factor or path on the same middle vertices.  If
`F'` retains every old edge of `I(a,b)`, then the pointwise complement of
`F'` has a positive run of length `s<=3`.  Consequently the set of removed
old edges `E(F)\E(F')` hits every short-zero collar.

### Proof

Retaining all edges in (3.2) forces the old subpath

\[
 T_{a-1},T_a,\ldots,T_{b-1},T_b
\]

inside `F'`; the degree-two condition permits only its two orientations.
The coordinate trace on that forced subpath is (3.1), or its reversal.
After pointwise complementation it is

\[
 0,1^s,0.
\]

The two displayed zeros make the central positive run maximal independently
of the continuation beyond the subpath.  Thus dual residence fails unless
some collar edge is removed.  `square`

This proof does not assume that `F'` is obtained by permuting pre-cut
segments.  It applies to every new factor on the same vertex set.  It also
shows why a phase-varying local rail swap on an intact collar is insufficient:
the short run moves from one complementary rail to the other but does not
disappear.

### Theorem 3.2 (exact raw and cyclic transversals)

For the `2010` internal collars of the opened path,

\[
 \tau=1230.                                       \tag{3.3}
\]

For the cyclic two-component source the same physical optimum is attained by
a coordinate-equivariant cut set.  On the large component coordinate
rotation acts by

\[
 \rho(T_i)=T_{i+1704},\qquad1704=4\cdot426.       \tag{3.4}
\]

The `2010` collars reduce to `134` circular intervals on `Z_426` with size
histogram `2^22 3^39 4^73`, and

\[
 \tau_{\mathbb Z_{426}}=82.                       \tag{3.5}
\]

The fifteen translates of an optimum in (3.5) give (3.3).

### Proof

For line intervals, sorting by right endpoint and selecting the right
endpoint of the first unhit interval is an exact transversal algorithm.  The
interval that causes each selection is disjoint from every earlier causing
interval, giving a dual packing of the same size.  Applied to the raw collars
it gives `1230` on both sides.

For circular intervals, fix one collar `J`.  Every transversal contains some
`p in J`.  Conditional on `p`, remove all collars containing `p`, cut the
circle just after `p`, and apply the line greedy algorithm to the remaining
intervals.  Trying the at most four values of `p` is exhaustive.  The minimum
on all `2010` physical collars is `1230`.  Applying the same argument after
quotienting gives `82`.  The audit verifies (3.4), verifies that reduction
modulo `426` maps all translated collars to the `134` declared intervals,
and checks a literal `82`-residue optimum.  Lifting every residue through the
fifteen classes gives `1230` old edges and hits every physical collar.  Thus
the quotient construction attains the independently proved physical lower
bound.  `square`

One explicit quotient optimum is included in the audit artifact.  Thus a
symmetry-respecting repair is not ruled out, but it is necessarily
macroscopic:

\[
 {82\over429}={1230\over6435}>0.191.              \tag{3.6}
\]

### Corollary 3.3 (q1-exact symmetric-difference cost)

Let `F` be the restored cyclic source factor.  If a cyclic replacement factor
`F'` on the same vertices is also lower-q1 exact, then

\[
 |E(F)\setminus E(F')|\ge1230,
 \qquad
 |E(F')\setminus E(F)|\ge1230.                   \tag{3.7}
\]

Hence `|E(F) triangle E(F')|>=2460`.  If `F'` is required to be connected,
one further old edge must be removed from the defect-free `45` component.

### Proof

The source factor uses every rank-seven intersection colour exactly once.
The `t` removed old edges therefore have `t` distinct lower colours.  A new
lower-q1-exact factor must realize each of those colours on a newly added
edge, proving (3.7).  The collar family lies entirely on the large component;
connecting the untouched small cycle requires opening it at least once.
`square`

## 4. Boundary-only cuts are a different, stronger restriction

If a construction permits a short gap to be repaired only by cutting one of
its two boundary edges, associate to every gap the pair

\[
 \{e_{a-1},e_{b-1}\}.                             \tag{4.1}
\]

These pairs form the **return graph** on old transition positions.

### Proposition 4.1 (exact return-graph cover)

For the raw path, the return graph has `2010` edges and `3405` nonisolated
vertices.  It is the disjoint union

\[
 P_2^{1050}\sqcup P_3^{195}\sqcup P_4^{90}
 \sqcup P_5^{30}\sqcup P_7^{30}.                 \tag{4.2}
\]

Its minimum vertex cover is

\[
 1050+195+2(90)+2(30)+3(30)=1575.                \tag{4.3}
\]

### Proof

Orient a return edge from the transition deleting `x` to the later transition
reinserting `x`.  Every Johnson transition deletes one coordinate and
inserts one coordinate, so every return-graph vertex has outdegree at most
one and indegree at most one.  Time strictly increases, so no directed cycle
exists.  Every component is therefore a path.  Direct enumeration gives
(4.2), and a path with `e` edges has minimum vertex cover `ceil(e/2)`, giving
(4.3).  `square`

The number `1575` belongs only to this two-boundary subclass.  For a general
factor rethread the necessary clause is the OR of all `s+1` collar edges, and
the correct minimum is `1230`.

## 5. The unique-colour `BB` obstruction

For an old source edge `e_i`, put

\[
 U_i=T_i\cup T_{i+1}.                              \tag{5.1}
\]

On the complementary rail, the corresponding internal `BB` lower colour is

\[
 B_i\cap B_{i+1}
 =\{z\}\cup([15]\setminus U_i).                  \tag{5.2}
\]

Thus multiplicity of the z-containing child q1 colour (5.2) is exactly the
old upper-union multiplicity of `U_i`.

### Theorem 5.1 (unique-colour subtransversal)

Among the `2010` cyclic bad collars, `270` have the property that every edge
in the collar carries an upper colour of global multiplicity one.  They form
`18` coordinate-rotation orbits.  Their exact collar transversal number is

\[
 \tau_{\rm unique}=240=16\cdot15.                 \tag{5.3}
\]

Every dual-resident replacement therefore deletes at least `240` distinct
globally unique old upper colours.

### Proof

Use the load histogram (2.3) to mark each old edge whose union colour has
load one, retain only collars consisting entirely of marked edges, and apply
the circular conditioning-and-greedy proof of Theorem 3.2.  Directly on the
`270` physical collars the optimum is `240`.  There are `18` quotient
intervals and their optimum is `16`; a literal `16`-residue transversal and
all fifteen lifts attain the physical lower bound.  Since each selected edge
has globally unique colour, the `240` selected edges have `240` distinct
colours.  `square`

### Corollary 5.2 (pure mixed-seam braid no-go)

No depth-three resident complement braid obtained from old `BB` fragments
and `AB` seams alone can retain all but two child lower-q1 colours.  A cyclic
repair requires at least `240` new `BB` adjacencies carrying the prescribed
z-containing colours; after allowing two linear boundary absorbers, at least
`238` are still necessary.

### Proof

By Theorem 5.1, at least `240` unique colours (5.2) lose their only old `BB`
witness.  An `A` state omits `z`, so every legal `AB` edge has z-free
intersection.  It cannot realize any target in (5.2).  Therefore each lost
z-containing colour needs a genuinely new `BB` witness, except for at most
the two colours assigned to the global q1 boundary channels.  `square`

This is stronger than the scalar cut-capacity bound.  It permits internal
collar cuts and arbitrary fragment order; it excludes the architecture
because of colour type, not because there are too few total edges.

The sixteen colour orbits in the displayed optimum certificate are not a
fixed list forced on every repair.  Their identities depend on the chosen
collar transversal.  The exact cut-size interaction is as follows.

For a quotient cut set `C`, let

\[
 u(C)=\#\{e\in C:[U_e]\text{ has quotient-orbit load one}\},    \tag{5.4}
\]

and let `L(C)` be the number of upper-colour orbits all of whose old edge
witnesses lie in `C`.  Necessarily `L(C)>=u(C)`, and a q1-complete
reassembly needs at least `L(C)` new same-rail colour restorations.

### Proposition 5.3 (unique-loss frontier at the critical cut scale)

There are `245` large-component edge residues satisfying (5.4).  Among
quotient edge sets of exact size `b` hitting all `134` short-gap collars,
the minimum of `u(C)` is

\[
 u_{82}=19,
 \qquad u_{83}=18,
 \qquad u_{84}=17,
 \qquad u_b=16\quad(85\le b\le110).              \tag{5.5}
\]

In particular, a collar repair with exactly sixteen new BB restorations is
impossible at gross cut sizes `82,83,84`; from size `85` onward it is only an
optimistic lower-bound possibility, because multiplicity-two or
multiplicity-three colours can also lose their last witnesses.

### Proof

Every quotient collar is a cyclic interval of length at most four.  Fix the
first three cut bits.  Scan residues `3,...,425`, retaining the last three
bits and the number selected; reject a transition precisely when a
nonwrapping collar ending at the new residue is all zero, and charge the new
bit when its quotient colour orbit has load one.  At the end check the wrapping
collars.  The last-three-bit state contains the complete future-relevant
history, so this dynamic program exhausts every cut set of every cardinality.
Its exact minima are (5.5).  The audit stores attaining edge sets for
`b=82,83,84,85`, so both inequalities are independently replayable.
`square`

## 6. Exact shadow-moment rigidity

For a cyclic rank-`r` Johnson chronology define

\[
 E_q=\sum_i\left(r+q-
   \left|T_i\cup T_{i+1}\cup\cdots\cup T_{i+q}\right|\right).   \tag{6.1}
\]

Let `R_g` be the total number of coordinate zero-gaps of length `g`.

### Lemma 6.1 (zero-gap moment formula)

If no coordinate is constant on a component, then

\[
 E_q=\sum_{g\ge1}(q-g)^+R_g.                      \tag{6.2}
\]

### Proof

For one coordinate with a zero-gap of length `g`, exactly `(g-q)^+`
cyclic `(q+1)`-state windows lie wholly in that gap.  Summing over all
coordinates counts the total number of coordinate omissions from all upper
windows.  Across a strict cyclic Johnson chronology there is one new zero-gap
per transition, so the total number of zero-gaps is the component length,
while their total mass is `(k-r)` times the component length.  Subtracting
the actual total union rank from `(r+q)` times the number of windows and
using

\[
 (g-q)^+=g-q+(q-g)^+
\]

gives (6.2).  Summing components proves the statement.  `square`

For the source factor, (0.1) and (6.2) give (0.4).  Conversely,

\[
 R_1=E_2,
 \qquad R_2=E_3-2E_2,
 \qquad R_3=E_4-2E_3+E_2.                         \tag{6.3}
\]

The opened path has the independently audited linear vector

\[
 (E_2,E_3,E_4)=(329,1244,3254).                  \tag{6.4}
\]

### Corollary 6.2 (load-neutral no-go)

Any trade preserving the exact upper-window multiset, or only the aggregate
upper rank-load vector, through depths two, three and four preserves all
three short-zero counts.  It cannot make the complement depth-three
resident.

This does **not** obstruct a trade preserving only target support.  Indeed,
the audited all-depth Markov reduction changed the cyclic short-zero totals

\[
 2040\longrightarrow2025\longrightarrow2010\longrightarrow2010,  \tag{6.5}
\]

while keeping positive residence and complete bilateral target support.  Its
first two shadow-safe switches each removed one fifteen-copy orbit of
length-three zero gaps.  Thus dual defect is not an invariant of protected
factor-fibre switches; the required packet must simply carry nonzero window
load drift.

## 7. Exact surviving braid target

The smallest source-relative theorem still capable of succeeding is the
following.

> **Dense equivariant `BB` circuit gate.**  Starting from the audited
> `6390+45` factor, choose an alternating-circuit packet in the lower-middle
> incidence factor fibre such that:
>
> 1. its deleted old-edge set contains a transversal of every bad collar;
>    in a `Z_15`-equivariant construction this means at least `82` old edge
>    orbits;
> 2. it contains at least `16` new `BB` edge orbits restoring the
>    cut-set-dependent unique z-bearing q1 colours (or the exact
>    non-equivariant analogue with
>    at least `238` physical restorations after boundary absorption);
> 3. the new factor remains lower-q1 exact, every one-run and zero-run has
>    length at least four, and every lower and upper target remains in the
>    fixed-window support at every depth;
> 4. after the factor is opened and coupled to the other child rail, all new
>    seams pass their two-sided collars, component voltage/connectivity is
>    correct, arbitrary-width upper coverage survives, and `COMP_3` is
>    feasible.

Conditions 1 and 2 are now exact certified necessities.  Condition 3 is a
finite factor-fibre problem.  Condition 4 is the already separated
port/compiler consumer and is not implied by factor existence.

If a primitive quotient circuit deletes at most `s` old edge orbits, any
edge-disjoint packet satisfying condition 1 contains at least `ceil(82/s)`
primitives.  In particular, support-at-most-eight local circuits require at
least eleven circuit blocks.  This is a scale statement, not an
impossibility theorem for overlapping or larger circuits.

The positive evidence in (6.5) says that the factor fibre has the right kind
of load-changing directions.  What is missing is a theorem producing enough
of them simultaneously while protecting the all-depth support and the
positive-run queue.

## 8. Audit and scope corrections

The new solver-free auditor is

```text
scratch/audit_k15_complement_braid_obstruction_20260729.py
SHA-256 36bf1a8f807914e47789a5c61b0dbc3f910ad9d3c11e511d63784de328ac7094
```

and its output is

```text
scratch/k15_complement_braid_obstruction_20260729.audit.json
SHA-256 15719ccba1186e2c95e99d7acf1e891e449718b77333faaae3a49704d039bd85
```

It verifies the raw and cyclic run histograms, the complete fixed-window
tower, both q1 load histograms, the line and circular transversals, the
return-graph census, the unique-colour subtransversal, rotation shift, and
the rank-deficit moments.  It also proves the exact-cardinality unique-loss
frontier (5.5) by a complete width-three cyclic transfer DP and stores
attaining cut sets at sizes `82..85`; the three small-component edge-colour
orbit loads are independently replayed as `1,3,1`.

Two earlier statements require precise scope corrections.

1. Section 4 of
   `MATH_K16_TWO_RAIL_CUT_CAPACITY_REDUCTION_20260729.md` writes only the two
   boundary choices of a short run.  Its corresponding exact minimum is
   `1575`.  The value `1230` comes from the broader full-collar clauses, which
   also allow internal gap edges.
2. That note defines the facet rail `z+(T_i intersection T_(i+1))`, whereas
   the `2010` defects audited here belong to the pointwise complement rail
   `z+([15]\T_i)`.  The numerical `1230` must not be used as the facet-rail
   hazard count.

Finally, none of the obstructions in this note excludes an independently
chosen resident `B` factor, a new same-rail `BB` circulation, or a global
factor outside the source-relative fibre.  Nor does complete fixed-window
support alone solve the literal compiler.  The proved boundary is exactly:

\[
\boxed{
\begin{array}{c}
\text{bounded/sparse complement braid: impossible;}\\
\text{old }BB\text{ pieces plus only }AB\text{ seams: impossible;}\\
\text{exact load-neutral tower trade: impossible;}\\
\text{dense support-preserving, load-changing }BB\text{ circuit packet: open.}
\end{array}}
\]

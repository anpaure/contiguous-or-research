# Independent audit of the gap--Hall Pascal decoration recursion

Date: 2026-07-31  
Scope: symbolic audit of the new exact statements in
MATH_THEOREM_K_GAP_HALL_PASCAL_DECORATION_RECURSION_20260731.md.

## 1. Rectangular Pascal decomposition

Let \(|\Omega|=2m-1\). The four outer banks after adding \(z\) have sizes

\[
 \begin{array}{c|cc}
 &z\notin&z\in\\ \hline
 \text{lower}&A=\binom{2m-1}{m-1}&B=\binom{2m-1}{m-2}\\
 \text{upper}&B=\binom{2m-1}{m+1}&A=\binom{2m-1}{m}.
 \end{array}
\]

All \(B\) no-\(z\) upper colours force \(B\) internal no-\(z\) diamonds;
all \(B\) \(z\)-lower colours force \(B\) internal \(z\)-diamonds. The
remaining banks both have size

\[
                   A-B=\frac1{m+1}\binom{2m}m
                      =\operatorname {Cat}_m.
\]

A residual containment is necessarily \(L\subset z+S\) with \(S=L+c\).
Its middle pair is exactly \(\{S,z+L\}\), so the two signs and the four
missing-port tests in Theorem 1.1 are exhaustive. Two internal forests
have \(2A\) vertices and \(2B\) edges; adding \(K=A-B\) cross arcs gives
\(2A-K\) edges, hence \(K\) components if and only if no cycle is created.
With indegree and outdegree at most one, every undirected cycle is a
directed cycle, so contraction of the parent paths is exact.

Calibration at \(m=4\):

\[
                         A=35,\quad B=21,\quad K=14.
\]

Thus the theorem requires two 21-edge forests on 35 vertices and exactly
14 signed cross diamonds. The counts close.

## 2. Block gap composition

If a cyclic block contains \(t_i\ge1\) selected upper marks, it has
\(t_i-1\) internal gaps. Therefore

\[
                 \sum_i(t_i-1)=P-b,
\]

and there is one bridge gap per cyclic block. An injective internal
matching consumes \(P-b\) of the \(P\) lower colours. The residual problem
is literally a balanced \(b\)-by-\(b\) occurrence graph, so its perfect
matching is necessary and sufficient. No independence, regularity, or
topological assumption was inserted into this step.

The authenticated \(m=4\) obstruction is consistent with the theorem:
three consecutive forced upper marks make two one-position gaps; the two
gaps have the same unique lower colour, giving a two-versus-one Hall set.

The later authenticated \(m=4\) toggle is also consistent: it changes the
six local turn occurrences and hence changes the gap graph itself. The
resulting cycle has an explicit perfect gap matching and a zero-run of
length six. Thus the negative example is a cycle-specific Hall obstruction,
not an obstruction to semilength four.

## 3. Transparent hexagon transfer

An incidence-hexagon toggle changes neighbour pairs only at its six ports.
For one fixed selected vertex set, global palette bijectivity after the
toggle is therefore equivalent to equality of the selected local colour
multisets on each shore. Deleting the old three-edge matching leaves three
retained fragments. Alternation is already valid inside them and is
preserved by reversal, so checking the three new last/first shore-type
pairs is necessary and sufficient.

This independently verifies the local transfer theorem. It is a diagonal
condition on a decoration and a toggle together. The exact \(m=4\) census
shows why neither projection suffices alone:

\[
 31\text{ alternating hexagons},\quad
 16\text{ Hamilton outputs},\quad
 10\text{ decorable outputs},\quad
 6\text{ outputs with a common decoration}.
\]

Consequently a transparent gluing tree is rigorous, while an arbitrary
published gluing tree or an arbitrary frozen SDR is not.

The proof uses only that an alternating switch replaces one perfect
matching of an even local cycle by the other. It therefore extends without
change to any available alternating polygon: local palette equality handles
every changed turn, while the retained-fragment endpoint types handle every
new seam. A square gives a four-port state in larger cube-level factors,
but the strict middle-levels incidence graph has no \(4\)-cycle; its first
literal local state is the six-port hexagon.

Leaf-peelability is a separate graphic condition. If one matched leaf pair
is added to a forest, its nonleaf mate may meet several old components, but
at most one vertex in each; two neighbours in one old component close a
cycle through that component's unique path. This proves the matched-ear
criterion in both directions.

For a transparent toggle, the selected representatives already give a
perfect matching in the new gap graph. Deleting lost incidence edges from
the old forest and contracting the remaining components is therefore
exact: the new graph remains leaf-peelable precisely when the gained-edge
quotient is loopless and acyclic. Transparency alone does not imply this
test. The finite six-toggle census proves only that at least one common
decoration passes it in each audited row.

The graph here must be the simple support graph: one edge per
(gap, lower-colour) pair, regardless of occurrence multiplicity. In the
displayed repaired \(m=4\) decoration, four gaps contain repeated
occurrences of one colour; treating occurrences as parallel edges would
create four spurious two-cycles and reject the authenticated forest.
Distinct gained support edges that become parallel only after component
contraction are different: they do encode a genuine cycle and must be
retained as parallel quotient edges.

The common gap vertex is labelled by its preceding physical selected
\(A\)-vertex in the carried orientation. Endpoint-pair labels are not
stable under reconnection, and an unoriented block does not determine
“preceding.” Thus orientation is a literal part of the recursive state.

An independent replay over all 2,412 common decorations with an old
gap-forest across the 16 Hamilton hexagon outputs at \(m=4\) found zero
mismatches between the quotient loop/parallel/cycle test and direct
acyclicity of the new simple support graph.

The nontransparent finite-width bound is also exact. A \(2t\)-switch
deletes at most \(t\) edges in each of the physical-incidence, upper-turn,
and lower-turn augmented categories. Restricting an old matching of size
\(N-d\) to the common graph loses at most \(3t\) edges, so its maximum
matching deficiency is at most \(d+3t\). Symmetric difference with any new
perfect matching gives exactly that many or fewer vertex-disjoint
augmenting paths covering every exposed terminal; conversely such a
complete linkage augments to perfection.

The width is the common deficiency: it counts unpaired terminals on each
shore, not a prescribed pairing. Thus deficiency \(r\) means \(2r\)
terminal vertices, and a decorated parent gives at most \(3t\) per shore,
or \(6t\) total. The proof uses only that the alternating circuit is
factor-safe; Hamiltonicity of either endpoint is unnecessary.

This proves bounded terminal width, not bounded path support. The paths may
cross the whole augmented graph and can alter the trace, gap forest, or
physical socket far from the switch. The recursive definition therefore
names a maximum matching of the common graph and its two exposed terminal
sets. It also requires every protected occurrence to avoid both the
physical circuit collar and the matching symmetric-difference support, or
else requires literal output re-verification. Avoidance of the linkage
support alone would not protect geometry changed directly by the circuit.

Under a tree decomposition with bounded adhesion, recording every
realizable oriented disjoint path-fragment pattern on each boundary is
exact. Restriction of a global linkage gives compatible child patterns;
conversely, joining patterns while forbidding repeated boundary vertices,
directed cycles, and illegal terminal orientations reconstructs a global
linkage. With total boundary state size \(a\), the endpoint-pattern count
is \(2^{O(a\log a)}\). This finite gammoid/linkage coordinate must be
multiplied with, not substituted for, the gap-forest component partition
and trace/socket/voltage state.

The component assertion is likewise literal: every accepted recursive
step must satisfy \(\kappa(C_{i+1})=\kappa(C_i)-1\). A net edge-count or
“component reducing” label without ruling out simultaneous splitting is
insufficient.

## 4. Trace socket

The authoritative topology theorem says the only cyclic face has every
zero-run of length two and every one-run odd. Four consecutive protected
zeros force a zero-run of length at least four, so Lemma 3.1 is immediate
and remains valid under any orientation or reversal that preserves those
four positions consecutively and unmarked.

The boundary-state wording is also correctly scoped. Zero lengths must be
capped at \(4+\), not remembered only modulo two, because two boundary
zero-runs of length two may merge to make the decisive length-four witness.

## 5. Pascal shell census

Adding \(x,y\) to a \(2m-1\)-point ground set, rank-\((m-1)\) lower colours
split as

\[
 \binom{2m-1}{m-1}
 +2\binom{2m-1}{m-2}
 +\binom{2m-1}{m-3}=Q+2P+R.
\]

Rank-\((m+2)\) upper colours split dually as \(R+2P+Q\). Tagged parent
turns have exactly one new coordinate and hence lie only in the \(2P\)
mixed bank. The support lower bound \(Q+R\) counts selected turn positions,
not switches, so (4.5) remains true even when collars overlap; overlap can
only decrease the number of distinct changed positions. The theorem is
correctly restricted to an architecture without an auxiliary extreme-bank
path system.

Calibration for the step \(m=4\to5\):

\[
             Q=35,\qquad P=21,\qquad R=7,\qquad
             Q+2P+R=84=\binom93.
\]

Thus copied parents cover 42 mixed colours and leave 42 extreme colours on
each turn side.

In the clean copied-mark template, all \(2P\) mixed upper representatives
survive, the two parent mark circles are opened into \(b\) blocks, and
exactly the \(b\) distinct crossing parent gaps are destroyed. Deleting
each such gap and its forced matched colour leaves \(2P-b\) pairs, while
the child has \(Q+2P+R\) vertices per shore. The exact number of router
vertices on each shore in this template is

\[
                         Q+R+b.
\]

Its gap shore consists of \(Q+R\) extreme-upper-induced gaps and \(b\)
bridge gaps; its colour shore consists of \(Q+R\) extreme lower colours and
\(b\) released mixed colours. The reverse-ear criterion is sufficient and
necessary for routers required to peel completely before either parent
core. The induced retained core must remain a balanced forest with its
restricted matching; strict separation into the two opened parents is a
convenient sufficient special case. Ordinary Hall does not imply either
this core condition or the matched-ear condition.

For two parent blocks at \(m=4\to5\), the count is \(35+7+2=44\) vertices
per shore: 42 extreme-shell vertices plus two bridge gaps on one shore and
two released mixed colours on the other. Pairing the shores is an
additional exterior-router condition.

More generally, if \(c\) matched parent pairs literally survive, the router
size is \(P^+-c\). If \(d\) rather than \(b\) pairs are destroyed while all
mixed upper representatives survive, it is \(Q+R+d\). Thus \(Q+R+b\) is
not a chronology-free invariant of an arbitrary Pascal braid.

## 6. Complement-antipodal indexing

The important index is the physical position modulo the half-length:

\[
 A_i\text{ is at }2i,\qquad
 B_{i+s}\text{ is at }2(i+s)+1=2i+Q.
\]

Hence one selected upper occurrence contributes the antipodal pair
\(\{p,p+Q\}\) with \(p=2i\bmod Q\). This verifies the factor \(2\) in
\(S=2I\), which cannot be replaced by the ordinary cyclic order on \(I\).
Rail type is parity, so alternating rail types are exactly odd physical
gaps.

Lucas' theorem gives \(Q\) odd exactly for \(m\) a power of two. Then
\(m+1\) and \(Q\) are odd and

\[
             K=2Q/(m+1)\equiv2\pmod4,\qquad P=Q-K\text{ odd}.
\]

At \(m=4\), \(Q=35,P=21,K=14\), and the bad quotient trace

\[
                           (11100)^7
\]

has the required length and weight. At \(m=8\), the corresponding values
are \(Q=6435,P=5005,K=1430\), and \((1^7 00)^{715}\) again has length 6435
and weight 5005. Thus the trace exception is genuinely compatible with all
arithmetic constraints.

The reduction is intentionally scoped to the complement-coherent lower
choice \(J=I+s\). Complement supplies that lower SDR but does not make it
unique. At \(m=2\), \(I=\{0\}\) with paired \(J=\{1\}\) gives the bad trace
\(100100\), while the legitimate unpaired \(J=\{0\}\) gives a forest.
Likewise, the one-half switch state applies at intermediate stages only
when both the decoration and block indexing remain complement-paired.

## 7. Scope verdict

The following implications are proved:

* rectangular partial forests + residual inclusion matching + compatible
  signs + contraction acyclicity imply an ordered four-transversal;
* recursive internal gap matchings + boundary Hall imply alternating turn
  representatives;
* a component-distinct matched-ear pairing of \(Q+R+b\) router vertices on
  each shore preserves a balanced gap forest and its unique matching;
* a jointly chosen fixed decoration survives a tree of transparent,
  contraction-forest-safe switches which each join exactly two current
  components and split none;
* a nontransparent factor-safe \(2t\)-switch from a decorated parent has an
  exact augmenting-linkage state of common-deficiency width at most
  \(3t\), hence at most \(6t\) unpaired terminal vertices in total, with
  global routing
  still required in general and an exact finite tree DP under bounded
  adhesion;
* either a protected \(0^4\) socket or the exact trace test gives a linear
  forest;
* complement-antipodality at power-of-two \(m\) turns the two SDRs into one
  odd-gap coloured transversal inside the complement-coherent subclass.

The following are not proved and are not stated as consequences:

* existence of the residual signed matching for every \(m\);
* existence of \({\rm BPGR}(m)\) in the published GMM factor;
* existence of a leaf-transparent decorated gluing tree for every \(m\);
* closure of the power-of-two simplification under \(m\mapsto m+1\);
* middle-levels resolvability of an arbitrary ordered four-transversal;
* any Greene--Kleitman \(W/2\) edit bound.

The decisive remaining statement is therefore exactly the bulk
extreme-shell gap-router lemma, with the general rectangular signed-port
theorem as the matching-first alternative **for the central Catalan
matching gate**. Residence, deeper shadows, endpoint sockets, and the full
compiler remain separate downstream requirements for \(\nu(k)=B(k)\).

## 8. Private-path and \(m=5\) rank audit

The private-path composition lemma is a direct tree argument, but its
occurrence-closure clause is indispensable.  Private interval labels do not
prevent the same colour from occurring in an uncut retained-core gap.  The
proof therefore checks literal simple-support occurrence closure before it
suppresses a bundle to a pendant path.  It also requires pairwise-disjoint
off-anchor interiors and literal one-contact with the previously built
union; private colour labels alone do not prevent two bundles from sharing
a gap or one new gap from seeing a second old-core component.

For a symbolic standard label \(x=110u0v,y=101u0v\), direct application of
the local word map gives the lower triple
\(010u0v0,001u0v0,000u1v0\) and the identity-to-path support change.  The
three prefixes distinguish the roles; the first below-zero cut in \(u0v\)
and the last primitive component in \(u1v0\) recover \((u,v)\), proving
triple injectivity.  This verifies the lower-tube assertion for every
standard label.  The upper multiset statement is deliberately restricted
to the heavy-root labels: the third \(m=5\) label is a literal counterexample
to unrestricted two-sided transparency.

The canonical \(n=4\) extractor gives three plane-tree components of sizes
\(36,72,144\).  For the potential-decreasing two-edge component tree, the
two physical hexes have old/new matchings

\[
\begin{split}
 &(83,91),(85,87),(89,93)
   \longleftrightarrow (83,87),(85,93),(89,91),\\
 &(51,59),(53,55),(57,61)
   \longleftrightarrow (51,55),(53,61),(57,59).
\end{split}
\]

Direct replay gives the two lower triples \(\{82,84,88\}\) and
\(\{50,52,56\}\), the two upper triples
\(\{343,347,349\}\) and \(\{311,315,317\}\), and exactly the gap-support
matrices in (8.5)--(8.8).  All occurrences of the first triple lie at the
local A-index cluster \(54,55,72,73,74\); all occurrences of the second lie
at \(18,19,108,109,110\).  Hence no undeclared old gap touches one of the
four private colours.  The two gained bundles are literally disjoint
pendant paths and have distinct retained-core anchors.

The same replay checks the signed mark ledger: every atom fixes five
upper-side versus three lower-side marks.  The two atoms therefore leave
74 upper and 78 lower marks to the exterior sectors.  This four-unit debt
is separate from both the graphic path test and the missing-colour rank
deficit.

The complete standard-family replay has two Hamilton outputs and no others.
Both attain exactly \(81/84\) colours on both turn shores and miss the lower
orbit \(\{73,146,292\}\).  The locally private output misses upper
\(\{219,365,438\}\).  This proves a palette obstruction, not a gap-cycle
obstruction and not an obstruction to nonstandard \(m=5\) cycles.

The rank calculation is independent of the finite replay.  On the two
locally private labels, both active matroids are free of rank two, so every
Edmonds cut has value two and the label deficit is zero.  Adding six
mandatory missing-colour atoms as component-row coloops and linkage-row
loops makes every toggle contribute one to every rank partition and every
repair atom contribute zero when placed on the linkage side.  The minimum
is therefore two, witnessed by putting the two toggles on the component
side and all six repair atoms on the linkage side.  Against target eight,
the exact augmented deficit is six, or three on either shore separately.
This is the formal reason the two-matroid accepting theorem cannot be
invoked before palette preparation.  This is a rank deficit of six
atomized missing-colour obligations, not a six-switch lower bound: one
nonstandard physical switch may create several missing colours.

Authenticated inputs:

* `MATH_THEOREM_CATALAN_PRIVATE_TRIPLE_STANDARD_M5_REFUTATION_20260731.md`,
  SHA `39315e57c998c0733036ea804c3683a65188c579e07422d724410568f0782c3b`;
* `scratch/audit_catalan_private_triple_standard_m5_refutation_20260731.py`,
  SHA `3bd41be38af3ddbf7a96e20adc31934c591aad1c5790984b64eea8a58e81080d`;
* its frozen JSON, SHA
  `cb283fdfac243b1724f1eab9a7e7bddcc9fee24c450743b74b1855b7f7e1ad3c`;
* `MATH_THEOREM_CATALAN_JOINT_GRAPHIC_GAMMOID_GLUING_FACE_20260731.md`,
  SHA `b0595b2dd109f92ef17fbd5ee43d29554ea3bb09c542df8fdc689b3195e3e82e`.

## 9. Independent audit of the synchronized \(m=5\) repair

The new finite theorem passes, with one important recursion correction.
The three displayed \(C_{10}\) circuits are pairwise vertex-disjoint and
sequentially Hamilton-safe.  Direct reconstruction gives

\[
 (\delta_-,\delta_+,\nu)
   =(3,3,207)\to(2,2,208)\to(1,1,209)\to(0,0,210). \tag{9.1}
\]

Each circuit deletes and adds five physical-incidence, five lower-turn and
five upper-turn augmented edges.  Consecutive common augmented graphs have
matching orders \(204,205,205\), hence deficiencies \(6,5,5\).  The macro
common graph has order \(197/210\); symmetric difference with the forced-
port final matching gives exactly thirteen augmenting paths, of vertex
lengths

\[
          4,4,4,4,4,4,4,4,4,4,4,6,16,             \tag{9.2}
\]

and four alternating four-cycles.  All twelve private port edges can be
forced without lowering any of those common ranks.  Thus the common-core
linkage and pinned-port assertions are literal.

The packet is nevertheless not a sequence of decorated BPGR transitions:
the first three augmented graphs in (9.1) have no perfect matching.  The
eventual SDR pulled backwards is not alternating at the first two stages.
Therefore Theorem 9.4's atomic-macro formulation is necessary, not merely
convenient.

The complete private-tube supports are

\[
\begin{aligned}
T_0={}&\{83,85,86,87,89,90,91,92,93,94,340,342\},\\
T_1={}&\{51,53,54,55,57,58,59,60,61,62,308,310\}.
\end{aligned}                                      \tag{9.3}
\]

They are disjoint from one another and from every repair support.  The
packet changes none of the private lower labels
\(50,52,56,82,84,88\) or upper labels
\(311,315,317,343,347,349\).  Full occurrence replay gives multiplicities
\(1,2,2\) in each private triple, with every occurrence confined to the
two gained stars and the retained anchor star.  This verifies the two
private paths rather than inferring them from port disjointness.

The final simple gap graph has \(84+84\) vertices, 111 edges and 57
components, with profile

\[
 41(1,1,1)+10(2,2,3)+4(3,3,5)+(5,5,9)+(6,6,11).    \tag{9.4}
\]

It is a forest and its perfect matching is unique.  All 84 pairs peel.
All four standard-glue cube states independently pass the forest, unique-
matching and binary-trace tests.

The topology correction is exact.  Before the private glues the component
profiles are

\[
 (36,72,144)\to(36,216)\to(36,48,168)\to(120,132), \tag{9.5}
\]

and from the repaired endpoint either standard hex alone, or both, gives
one 252-cycle.  Thus the prepared component matroid is \(U_{1,2}\), not the
old rank-two tree.  One private hex is the component connector and the
other is a Hamilton-to-Hamilton transparent move.  Any recursive theorem
which silently retains the old two-edge component tree is false.

The final forced decoration and all four private-glue endpoints have a
valid binary trace, including explicit four-zero output runs.  No such
breaker is disjoint from the whole repair packet, and the 132-component
itself has no protected four-zero run.  Output revalidation is therefore
the proved packet-level statement.  The later 42-connector audit now proves
final endpoint topology and every lower/upper shadow depth: 46 cuts retain
all-depth support, 39 without breaking a path block.  It also finds the
sharp remaining negative: 31 internally bounded length-two one-runs survive
every whole-path permutation, reversal and endpoint choice, so depth-two
residence fails and an interior rethread is mandatory.

Authenticated source:

* theorem SHA
  `78c2079ad71641b96fc1e5002047f012f8f8fd787a73f4ae1d8bc6c916910881`;
* audit-script SHA
  `65a52cb19f2ef6e38e437fe251726bec28935509ca05e86b43557bf5ab72e07d`;
* frozen-JSON SHA
  `f43e39674c4a027fe46ed2f9918e8c3dcc218865816decad4a8e1f4b8052c7e1`;
* canonical payload
  `ca3c2ffe5bc7f7a93543f63be93a282f39c12eb08e8fdd9f2fefb4f132b0d1fe`;
* downstream all-depth/residence note SHA
  bd3cc11ac3682c5d7a244099e736f5a707884edac5d1554dde7ada0805f20c60;
* replay JSON SHA
  91201d7281bde581ef01a58778b6e8edbea8dcb7da37d185c76f1771b91b2a5e,
  payload
  19752a1d1ec5d02ad5ab18479228a85d6128caa8b1bc51cc0226e509c8f31549.

## 10. Audit of the orbit-bank capacity theorem

The orbit classification is exact.  A stabilizer order divides both the
ground-cycle size \(n=2m-1\) and the lower turn rank \(m-2\), while

\[
                     \gcd(n,m-2)=\gcd(3,m-2).
\]

Upper colours have the same classification by complement.  Hence only
free and order-three orbits occur.  When \(m=3a+2\), an order-three colour
is a union of \(a\) cosets of the unique order-three subgroup, giving
\(E_a=\binom{2a+1}a\) physical colours and
\(\operatorname {Cat}_a\) orbits of length \(n/3\).
At \(m=2\) the empty/full colour is the degenerate order-three orbit and
its stabilizer is the whole group \(\mathbb Z_3\); the later \(a\ge1\)
exceptional asymptotics start at \(m=5\).

A \(C_{10}\) uses five vertices on each middle-levels rail.  Therefore a
pairwise-disjoint one-pair-per-circuit bank for \(f\) free and \(e\)
shortened paired orbits uses exactly

\[
                         D=nf+(n/3)e
\]

circuits and exactly \(5D\) vertices on each rail.  The two typed
inequalities (10.5) are stronger than their scalar sum and are unavoidable.
The canonical \(7/5\) tube specialization is correctly conditional on
using that literal oriented tube footprint; it is not asserted for an
arbitrary glue collar.

The exceptional-bank estimate is also correct.  Counting only subsets
with \(a\) points in a fixed \((2a+1)\)-block gives

\[
 \binom{6a+3}{3a+1}
 \ge \binom{2a+1}a\binom{4a+2}{2a+1}>5\binom{2a+1}a
 \quad(a\ge1).
\]

Thus the complete stabilizer-three defect bank clears raw vertex capacity.
The free-orbit bound (10.13) is the exact remaining typed capacity after
that reservation.  Conversely
\(5P_m/N_m=5(m-1)/(m+1)>1\), so no disjoint \(C_{10}\) architecture can
repair an arbitrary turn map.  Sparse source defects are a necessary
hypothesis.

The stronger Pascal-shell calculation also passes.  With

\[
 S_m=\binom{2m-1}{m-1}+\binom{2m-1}{m-3},\qquad
 N_{m+1}=\binom{2m+1}m,
\]

factorial cancellation gives

\[
 \frac{S_m}{N_{m+1}}=\frac{m^2+2}{(2m+1)(m+2)}.
\]

The inequalities \(5S_m>N_{m+1}\) for all \(m\ge2\) and
\(3S_m>N_{m+1}\) for \(m\ge5\) reduce respectively to
\(3m^2-5m+8>0\) and \((m-1)(m-4)>0\).  Since strict middle levels has no
alternating four-cycle, even a minimal six-cycle one-pair router cannot
service the full copied-parent extreme shell beyond \(m=4\).  The report's
classification of \(C_{10}\) packets as sparse post-bulk repair is therefore
forced by capacity, not a design preference.

Capacity is not construction.  The subfamily union inequalities (10.17)
are necessary but not sufficient for a rainbow matching in ten-uniform
support families.  The report correctly leaves the rainbow support packing,
endpoint component topology and pinned final augmented matching as the
constructive gate.  The count \(f+e\) of mixed relays is explicitly an
orbit-router design choice--one last relay per bank--and is not claimed as
a palette lower bound.

The endpoint-transition lemma is exact.  Cutting the old 2-factor at every
removed edge and contracting the retained paths produces the alternating
2-regular multigraph \(S\cup A\); its cycles, plus untouched old cycles, are
exactly the endpoint components.  Thus a permutation-wrap “relay” is not
automatically a physical component relay.  The report now tests topology
through this graph.

The \(7/5\) private reserve is correctly restricted to the full
occurrence-isolation supports independently replayed at \(m=5\).  The
symbolic marked atom alone has only a \(5/3\) footprint and does not prove
an all-\(m\) halo.  General dimensions must use the literal \(r_0,r_1\)
of their supplied collars.

At the clean subgroup \(H=\mathbb Z_h\), the exact quotient-track demand is
\(B=sf+(s/3)e\) and the physical demand is \(D=hB\).  This distinction is
essential at higher three-primary valuation.  More generally the two shore
demands are

\[
 B_-=sf_-+(s/3)e_-,\qquad B_+=sf_++(s/3)e_+,
\]

so clean-track mixing needs exactly \(B_-=B_+\), not typewise equality.
Every middle vertex has a free \(H\)-orbit, and there are
\(N_m/h=s\operatorname {Cat}_{m-1}\) such orbits per rail.  If a translated
\(C_{10}\) seed uses five distinct rail orbits, the exact equivariant slot
cut is

\[
 5B+\rho_H(S_\epsilon)\le s\operatorname {Cat}_{m-1}.
\]

This verifies Proposition 10.1A.  It also shows why raw private-reserve
cardinality is insufficient uniformly: a reserve of size \(N_m/h\),
dispersed one vertex per \(H\)-orbit, saturates a rail, while it is
\(o(N_m)\) whenever \(h\to\infty\).  A symmetric construction needs
\(\rho_H(S_\epsilon)=o(N_m/h)\), or must break/reconfigure the clean
symmetry.

The quotient-pressure lemma is also exact.  Before job \(i\), the selected
seeds occupy at most \(5(i-1)\) slots on each rail.  A slot on rail
\(\epsilon\) excludes at most \(\Delta_{i,\epsilon}\) candidates for that
job.  The union bound therefore excludes at most

\[
 5(i-1)(\Delta_{i,0}+\Delta_{i,1})
\]

candidates, so the strict inequality (10.9h) leaves one choice.  This is a
proved sufficient condition, not a characterization of the quotient
rainbow-matching problem.

The extra ordinary partial
edge orbit forced when \(3\nmid\operatorname {Cat}_a\) is a global
mixed-orbit obligation, not an extra physical circuit per exceptional
orbit.  Finally, a growing \(D\)-bank is not a bounded-state macro merely
because every atom is bounded: it needs bounded accepting packets or one
common bounded-width decomposition (or exact bounded-interface block
transitions) for linkage, component, gap and socket states.

Finally, the transparent/debt distinction is correct.  A private glue must
preserve one fixed decoration by equality of both local turn-colour
multisets and alternating retained-fragment boundary types, followed by the
graphic contraction test.  A repair packet may violate those conditions at
its prefixes and is judged by its final linkage.  The authenticated
\(31/16/10/6\) \(m=4\) incidence-hex census calibrates the first class; the
three-\(C_{10}\) \(m=5\) packet calibrates the second.  Interchanging them
would invalidate the recursion.

## 11. Audit of repair--rethread capacity and streaming debt

The all-\(m\) run identity passes directly.  For each coordinate, the
induced subforest has

\[
 \binom{2m-1}{m-1}-\binom{2m-1}{m-2}
 =\operatorname {Cat}_m
\]

components.  A Johnson seam between distinct current components merges
exactly the \(m-1\) boundary runs belonging to its intersection.  Hence
(11.0) is exact.  Since total positive-coordinate mass is
\(m\binom{2m}{m}=m(m+1)\operatorname {Cat}_m\), subtracting the run floor
times the exact number of runs proves (11.0a)--(11.0b).  In particular,
the \(d+1=\Theta(\sqrt m)\) residence requirement has large aggregate
surplus; this is a capacity statement, not a balancing construction.

The separated resource theorem also passes after distinguishing its two
ledgers.  If \(d_Z\) is the number of source-old edges deleted by a
rethread and \(s_{Z,\epsilon}\) is its complete physical footprint on rail
\(\epsilon\), then

\[
 \sum_Zd_Z\ge\tau_S,\qquad
 5D+\sum_Zs_{Z,\epsilon}+r_\epsilon\le N_m.
\]

The first inequality is the closed-span transversal; the second is typed
resource disjointness.  They cannot in general be replaced by one abstract
cycle half-length.  The turn packet must be frozen before the potential and
spans are measured, or every interleaved turn move must be included in the
same ordered marginal ledger.  The gains then telescope exactly to \(R\).

Only in the additional rail-balanced, no-auxiliary-support subclass does
one have

\[
 d_Z=s_{Z,0}=s_{Z,1}=t_Z.
\]

The \(m=5\) scalar window \(29\le\Theta\le97\), and the derived
\(t=3\)/\(\sum(t_Z-3)\le4\) calibration, belong only to this subclass.
They do not cover a rail-imbalanced palette braid or a physical rethread
with collars.  The ordinary frozen-source run-span number \(\tau=29\) is
exact.

The strict frozen-reserve comparison was independently replayed rather
than inferred from that scalar bound.  The turn packet uses 30 vertices
and the two private tubes use 12 vertices each, with no overlap.  Exactly
10 of the 31 closed spans meet their 54-vertex union, and exactly two have
no old edge with both endpoints outside it:

\[
 (3,1,[19,21])\quad\hbox{and}\quad(7,1,[1,3]).
\]

Thus \(\tau_S=\infty\) and the strictly separated frozen-reserve face is
indeed impossible.  The previously listed path-3/coordinate-0 span is not
locked: all three of its old edges avoid the reserve.  The run-span note
and JSON have SHAs
20a632a046d2f8fdeb745ef366e1c93938ab858d1d107e6f35dc80b7be3d74e2 and
22fb3d9fc344ba0f1656319f304f26df4961853fd9b31bbb68dc893f98f9789d,
with payload
43b39a185d71991d3e40538defd1e325e0f7436f63a41113f0fc0a14ccc2340f.
The independent repair/private support source has SHA
e5f15f9775bc65c8e283a16ffc584c3d2c1cc29c73382fca58894ecfe1de3540.

Most importantly, the finite residence obstruction has now been bypassed.
The independently replayed matching changes 119 partners and its
symmetric difference has 30 colour-disjoint alternating circuits with
half-length histogram

\[
              2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1.
\]

The half-lengths sum to 119.  Its lift is again a 210-edge, 42-path forest
with both immediate palettes exact and no strictly internal run shorter
than three.  The circuit decomposition is a diamond-colour decomposition,
not a proof of disjoint Pascal-rail footprints or an accepted intermediate
physical-switch history.  The exact remaining debt
is 21 deep targets plus endpoint-run joining, so the central residence
problem is distributional and jointly chronological rather than intrinsic.

The later two-dead-socket theorem sharpens “endpoint joining.”  Only 69 of
304 formal endpoint pairs are depth-two pair-safe, 15 ports are dead, and
both ports of one path component are dead.  The two forced short-run
collars are disjoint in every connected choice; their unique overlap
isolates a two-component cycle.  Hence the fixed 42 path bodies admit no
resident endpoint-only Hamilton chronology even after one arbitrary
opening.  A further interior/socket actuator is necessary, while another
matching or a joint interior--connector rethread remains open.

The imported finite packages are authenticated separately in handoff
items 2187R, 2188 and 2190.  This audit checks the implications used here,
not a particular concurrent prose hash of those source notes.

The asymptotic calculation also passes:

\[
 N_m=(2m-1)\operatorname {Cat}_{m-1},\qquad
 \frac{E_a}{N_m}\le\binom{4a+2}{2a+1}^{-1}.
\]

Thus the full shortened bank and \(O(\operatorname {Cat}_{m-1})\)
constant-width private tubes cost \(o(N_m)\).  If the free physical defect
density is strictly below \(1/5\) and both typed residence footprints are
sublinear, the raw rail inequalities have positive linear slack.  This is
only capacity; support candidates, run redistribution, deep witnesses and
chronology remain constructive requirements.

The controlled-debt theorem is an exact bounded-treewidth composition.
Connected resource occurrence ensures every interaction with a processed
subtree crosses its boundary.  The state must carry the fixed or selected
common-core matching, exposed terminals, oriented factor fragments, the
gap perfect matching and connectivity partition, physical-use bits,
directed reachability, exact capped residence collars including the
all-one/same-boundary-run bit, and every still-
mutable named witness.  Directed contraction after selecting \(T\to H\)
is legal exactly when the residual is acyclic and has no
\(H\leadsto T\) path.  Delete-first normalization or literal reachability
recomputation is necessary.  All coordinates must come from the same local
circuit/representative choices; a Cartesian product of separately feasible
projections is unsound.

If the binary trace or quotient phase changes, it is an additional
finite-automaton coordinate, not a consequence of the residence collars:
the boundary state must carry zero-run length capped at \(4+\), one-run
parity, same-run/violation bits, and the live voltage or phase sum.  It may
be omitted only under a literal immutability/protection certificate.

The reachability relation gives \(2^{O(w^2)}\) possibilities, residence
collars give \((d+2)^{O(w)}2^{O(w)}\), and a local alphabet of size
\(A_m\) contributes \(A_m^{O(w)}\).  Bounded adhesion alone is vacuous because of the one-bag
decomposition.  It is sufficient only when each unbounded block comes with
an exact bounded-interface transition relation.

Consequently packet length can grow without growing live debt when the
*joint* physical/augmentation/gap/reachability/residence/deep-witness graph
has bounded width, or when bounded-interface blocks have supplied exact
transition relations.  Width two of the abstract defect-orbit cycle is not
enough: long augmenting paths, deep witnesses or private-tube interactions
may destroy physical bounded width.  The report correctly leaves existence
of one aligned decomposition as the exact all-\(m\) gate.

The serial-bank corollary is a valid concrete specialization.  Under its
nearest-neighbour resource hypothesis, the cell bags intersect only in the
declared \(S_i\)'s, the carried wrap interface and the at most \(p\) live
private pins.  Cutting the wrap exposes at most two live interfaces, while
bags have size at most \(\omega=b+3w+p\).  This gives the stated
\(2^{O(\omega^2)}(d+2)^{O(\omega)}\) state bound.  It proves bounded live debt for growing
free and shortened orbit packets; it does not prove that physical
augmenting paths and residence witnesses satisfy the nearest-neighbour
hypothesis.

This agrees with the Pascal determinant obstruction.  Two complete parent
rails plus forced cross edges already contain a cycle, and contraction of
one atom requires both residual acyclicity and no \(H\leadsto T\) path.
Hence boundary-deficient rails and live reachability are algebraically
necessary; scalar two-parent recursion cannot bypass the streaming state.

The proved boundary is therefore sharp.  Capacity and bounded-state
composition are available, and \(m=5\) supplies a genuine overlapping
residence-clean rethread.  What is not proved is an all-\(m\) construction
which simultaneously realizes the sparse free/shortened turn router, run
redistribution, deep-witness repair, endpoint chronology, and the ordered
fixed-decoration transparent glues in one bounded-width physical state.

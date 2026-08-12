# Independent audit of the K17 GMM endpoint-oriented residual factor

Date: 2026-07-31  
Status: `GO` for the balanced `A/X/Y` residual-factor theorem; `GO` for the
Johnson-port tight-enumeration subclass only with its explicit extra premise;
Sections 7--8 are exact for the unsigned/unoriented flow and are only a
relaxation when all macros must retain their prescribed `X -> Y` directions

## 0. Audited snapshot and verdict

This note audits the snapshot

```text
MATH_THEOREM_K17_GMM_ENDPOINT_ORIENTED_RESIDUAL_FACTOR_20260731.md
SHA 20d37788b9927df7fe6c4f2e41597bec9158c432917d270b4e43c5ac28e2d5bd
```

The theorem had no separately named finite audit artifact.  The independent
replay accompanying this note is therefore the first literal finite checker
for its authenticated parent and its two orientation distinctions.

The scoped verdict is:

1. Sections 1--5 are `GO`.  A two-level tight enumeration gives the required
   rank-lowered path forest; the endpoint contraction criterion is exact; and
   transitivity proves that some relabelling works for the `6390+45` parent.
2. Section 6 is `GO` because the current snapshot explicitly assumes
   
   \[
        |\ell(P)\mathbin\triangle h(P)|=2
   \]

   for every macro.  This Johnson-port premise is genuinely additional and
   cannot be dropped.
3. Sections 7--8 correctly characterize an **unsigned** incidence
   two-factor.  Their Hall system is exact for that relaxation.  It does not
   enforce one orientation traversing every macro from its declared input
   port to its declared output port.  The current theorem now says this
   explicitly through its macro-coherence clause.
4. No K17 word, physical owner chronology, residence theorem, upper-service
   theorem, or common-cap compiler follows from this result.

## 1. Tight-enumeration contraction

Let

\[
 \mathcal Z={\Omega\choose r-2},\qquad
 \mathcal C={\Omega\choose r-1},\qquad
 N=|\mathcal Z|,\quad M=|\mathcal C|,
\]

and put \(b=M-N=\operatorname{Cat}_r\).  In a tight cyclic enumeration of
the two levels, let \(x\) be the number of cross-level transitions.  Every
cross-level transition costs at least one flip, every same-level transition
costs at least two, and \(x\le 2N\).  Therefore

\[
  \operatorname{len}_{Hamming}\ge
  x+2(M+N-x)=2(M+N)-x\ge 2M.
\]

Tightness is equality.  Hence \(x=2N\), every cross-level transition is an
inclusion edge, and every same-level transition is a Johnson edge.  After
suppressing \(\mathcal Z\), one obtains a Hamilton cycle on \(\mathcal C\)
with exactly \(N\) mediated edges, one of each colour in \(\mathcal Z\), and
exactly \(b\) direct edges.  Deleting the direct edges leaves a spanning
linear forest with

\[
 |V|=M,\qquad |E|=N=M-b,\qquad c=b.
\]

This is exactly Lemma 1.1.  It uses only the published existence of a tight
enumeration; no compatibility with a second tight enumeration is inherited.

## 2. Endpoint coupling and contraction

For every oriented component of the forest, let \(\alpha\) mark its first
endpoint and \(\beta\) its last endpoint.  An isolated vertex carries both
marks.  Then

\[
             \deg_G(i)+\alpha_i+\beta_i=2.
\]

The theorem's `A/X/Y` edge prescription therefore gives degree two at every
`A` owner.  Cutting the `X` parent rail at the \(\alpha\)-indices and the
`Y` rail at the \(\beta\)-indices leaves a sealed rail cycle precisely when
the corresponding mark set misses a parent cycle.  Otherwise each forest
component receives one `X` arm and one `Y` arm and becomes one path.  Thus
the endpoint-hitting condition is necessary and sufficient.

After contracting every parent cycle, a forest component becomes one
multiedge joining the parent cycles containing its endpoint occurrences.  A
path orientation is exactly an orientation of that multiedge.  Every parent
cycle must receive both an incoming and an outgoing endpoint.  An undirected
multigraph admits such an orientation iff every vertex has degree at least
two, with loops counted twice: balance an Eulerian augmentation and delete
the auxiliary edges.  This proves Lemma 3.1, including loops and isolated
forest vertices.

For the authenticated K15 parent there are `2860=2*1430` endpoint
occurrences.  If `S` is the `45`-vertex small parent cycle, coordinate
transitivity on the `6435` rank-seven colours gives

\[
 \mathbb E|E(G)\cap S|={2860\cdot45\over6435}=20.
\]

Hence one relabelling puts at least 20 endpoint occurrences on the small
cycle.  At most two endpoint occurrences can lie at one vertex, so the small
cycle receives at most 90 and the large cycle at least `2860-90=2770`.
Both contracted degrees are at least two.  This is a solver-free existence
argument; it does not materialize one particular GMM enumeration,
permutation, or orientation.

## 3. Exact K17 interface

For K17, \(r=8\), \(|\Omega|=15\),

\[
 M={15\choose7}={15\choose8}=6435,
 \qquad N={15\choose6}={15\choose9}=5005,
 \qquad b=1430.
\]

The proved objects and palettes are:

| object | old projection | child rank | count | proved property |
|---|---:|---:|---:|---|
| parent owner `T_i` | rank 8 | -- | 6435 | lower-rainbow two-factor, cycles `6390+45` |
| parent colour `C_i` | rank 7 | -- | 6435 | every rank-seven set exactly once |
| GMM colour `Z` | rank 6 | -- | 5005 | every rank-six set exactly once on `G` edges |
| `A_i=C_i+xy` | rank 7 | 9 | 6435 | spanned by the residual factor |
| `X_i=T_i+x` | rank 8 | 9 | 6435 | spanned by the residual factor |
| `Y_i=T_i+y` | rank 8 | 9 | 6435 | spanned by the residual factor |
| pure `U` owner | rank 9 | 9 | 5005 | **not inserted by Sections 1--5** |

The residual edge ledger is:

| edge family | count | exact lower colour palette |
|---|---:|---|
| `AA` | 5005 | all `Z+xy`, once |
| `XX` | 5005 | together with `XA`, all `C+x`, once |
| `XA` | 1430 | together with `XX`, all `C+x`, once |
| `YY` | 5005 | together with `AY`, all `C+y`, once |
| `AY` | 1430 | together with `YY`, all `C+y`, once |

Thus the residual graph has `19305=3*6435` owners,
`17875=19305-1430` edges, and exactly `1430` vertex-disjoint paths.  Each
path has one free `X` endpoint and one free `Y` endpoint.  The input-port
bank and output-port bank are separately injective because they are subsets
of the two parent rails.  A macro may nevertheless have equal ports, or a
non-Johnson ordered port pair.

The missing owner/lower-`q1` row is the simultaneous insertion of all 5005
pure `U` owners while using every untagged rank-eight colour exactly once.
On a closed cyclic braid the exact slot identity is

\[
       (N-c)+2c+(b-c)=N+b=M,
\]

where `c` is the number of nonempty `U` paths.  Opening one retained direct
macro seam loses exactly one untagged colour and gives the required linear
`M-1` ledger.  Counts alone do not establish the occurrence-labelled
containments, colour bijection, or connectedness.

## 4. Why the Johnson-port premise is necessary

The audit script contains a complete project-parameter `r=3` fixture.
Its parent lower-rainbow rank-three cycle is

```text
07,0b,0d,15,1c,0e,1a,19,13,16.
```

Its contracted lower tight enumeration on rank two is

```text
03,05,09,11,12,06,0c,14,18,0a,
```

with mediated edge indices `{0,4,5,7,8}`.  Their intersection colours are
all five singleton sets.  Orienting the resulting five forest components as

```text
[05,03], [09], [11], [0c,06,12], [0a,18,14]
```

gives the exact residual macro ports

```text
0d->0b, 13->15, 1a->13, 15->07, 0e->19.
```

The last pair has Hamming distance four.  Nevertheless the directed atomic
cycle

```text
U0f,P4,U1b,P2,P1,P3,U17,U1e,U1d,P0
```

is externally legal and its ten seam colours are all ten rank-three sets.
It cannot expand `P4` to a direct same-level transition of a tight
enumeration.  Therefore Section 6 is correct precisely because the current
statement includes the Johnson-port premise; two independent applications
of the tight-enumeration theorem do not provide the required correlation.

## 5. Unsigned Hall versus fixed macro directions

Assume the input ports are pairwise distinct, the output ports are pairwise
distinct, and no macro has equal ports.  Put

\[
 m_T=|\{P:T\in\{\ell(P),h(P)\}\}|,
 \qquad d_T=2-m_T.
\]

Forgetting port orientation, choosing degree two at each `U` owner and
degree \(d_T\) at every colour is an ordinary integral bipartite flow.  Its
Hall inequalities are exactly

\[
 2|\mathcal S|\le
 \sum_T\min\bigl(d_T,|\{U\in\mathcal S:T\subset U\}|\bigr).
\]

The complementary full-star formula in Section 8 follows algebraically and
is exact for this unsigned flow.

It does not force a prescribed `X -> Y` orientation.  On the same `r=3`
fixture, choose the following two facets at each `U` owner:

```text
U0f:{0d,0e}, U17:{07,16}, U1b:{0b,1a},
U1d:{19,1c}, U1e:{16,1c}.
```

This is one connected degree-two factor and exhaustively satisfies every
small Hall cut; its minimum slack is zero.  Its suppressed cycle is

```text
P0,U0f,P4,U1d,U1e,U17,P3,P1,P2,U1b
```

with seam colours

```text
0d,0e,19,1c,16,07,15,13,1a,0b.
```

In the displayed direction `P0` is traversed backward while `P4` is
traversed forward.  Reversing the whole cycle reverses both, so neither
orientation respects all five declared macro directions.  This proves that
macro coherence is an independent row.  If individual residual paths may be
reversed and no downstream state distinguishes `X -> Y`, the unsigned
factor is still a valid undirected owner cycle; this is exactly the scope of
the corrected Section 7.

For a fixed-direction recurrence, the proof-safe exact formulation is:

* every macro is the fixed directed arc \(\ell(P)\to h(P)\);
* every pure `U` owner chooses one directed arc
  \(a_U\to b_U\) between two **distinct** rank-eight facets of `U`;
* every rank-eight colour has indegree one and outdegree one; and
* the resulting directed cycle cover has one component, or carries an
  explicitly certified directed splice to one component.

The distinctness \(a_U\ne b_U\) and the joint choice at one `U` owner are
correlation constraints; two separate marginal matchings do not suffice.

## 6. Composition with the facet/staircase recurrences

The three current results occupy consecutive but different rows.

| theorem | supplied row | row still missing |
|---|---|---|
| K16 shifted cap/facet bridge | a slot-preserving inclusion map `T(rank8)->C(rank7)`, with one rooted four-edge path plus the complete 45-cycle facetified | uniform ports, deep cut rays, and a compiler |
| all-k Pascal facet/staircase recurrence | perfect cap/facet traces, the exact facet-window shadow shift, one-jump residence/capacity criterion, and a conditional common-cap interface | a braid meeting all sockets and one integral common-cap assignment |
| K17 GMM residual theorem | a spanning forest on `C(rank7)` whose edge colours are all `Z(rank6)`, endpoint-oriented into 1430 balanced `A/X/Y` macros | correlated pure-`U` insertion and the untagged palette, then all physical rows |

Together they give a nested owner tower

\[
       T^{(8)}\supset C^{(7)}\supset Z^{(6)},
\]

but not yet one physical recurrence.  Complementing the lower GMM tight
enumeration does give an upper tight enumeration on ranks eight and nine.
Its `1430` direct rank-eight transitions are useful only if they equal the
`1430` ordered macro-port pairs.  The published existence theorem does not
provide that correlation.  The K16 partial facet substitution fixes 49
special cap/facet rows; it does not determine this Catalan-sized port bank.

After a correlated owner cycle is found, the facet-window identity can
transport internal marked shadows along intact trace pieces.  The following
remain independent and load-bearing:

1. literal Johnson seams and occurrence-labelled cut/terminal sockets;
2. all-width pure and tagged upper service;
3. a legal depth-three residence/deadline staircase;
4. one opening and its protected missing lower colour; and
5. one simultaneous maximal-common-cap compiler.

Consequently the residual theorem is composable with the Pascal recurrence
as an owner-level central factor, but it does not by itself yield
`B(17)+O(1)`, an exact K17 word, or a uniform all-k recurrence.

## 7. Independent replay and hashes

Run

```text
python3 scratch/audit_k17_gmm_endpoint_oriented_residual_factor_independent_20260731.py
```

The script:

* replays `D^3(answers/k15.word)` and its `6390+45` lower-rainbow cycles;
* verifies the complete `r=3` tight enumeration and residual graph;
* reconstructs the five macro ports from the literal `A/X/Y` graph;
* verifies the legal non-Johnson-port external cycle;
* checks the correct directed-arc degree law; and
* exhausts every Hall cut of the connected mixed-orientation unsigned
  counterexample.

It writes

```text
scratch/k17_gmm_endpoint_oriented_residual_factor_independent_20260731.audit.json
```

Referenced frozen dependencies at audit time:

```text
answers/k15.word
  f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b
MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md
  a0b90eccd3d3cfd311eee68bce7e2dbacfd08d378a6b5913df24c42b1210906e
MATH_THEOREM_ALLK_PASCAL_FACET_STAIRCASE_RECURRENCE_20260731.md
  b22b48a053fc94481885a4a3ec278953812ee34309e08a1ad80ec2668f0e31e7
scratch/audit_allk_pascal_facet_staircase_recurrence_20260731.py
  96e4e4936ff77853e9981220cac843946f804d9a75a46080e63cda2e4f000b00
scratch/allk_pascal_facet_staircase_recurrence_20260731.audit.json
  dcae02a7c7b25c0a36eb9ae113f66766f9165134a4f5e446663ced7e2c092e72
  payload 7c15b7af3d0b23af6ed0c8314d5cb0311d83f8b82e0e6a98eb93ca38953ae9a0
MATH_THEOREM_EVEN_K16_CAP_FACET_BRIDGE_COMPONENT_HALO_20260731.md
  eb37919a2542d9a5960f37ccef589a7c11ebe2eff079c0c60028032a4b75bc06
scratch/audit_even_k16_two_rank_facet_bridge_20260731.py
  d4a03db8af07c15c306370313e8a2a4a0411b5137071c6eb839cf41075a37e0a
scratch/even_k16_two_rank_facet_bridge_20260731.audit.json
  c3e1e252702906f4a18aa9ff8dbc3b94e1132bb3123ea9e159307cfa16d05c00
  payload a35c35c5dde0b8a9a06f5ba43d65ac6895c5be7bf647221e5e8284c8b9578272
MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md
  71a84f0209910b3f56d2305234a87d35f646c0727fb1e80209934653a9d2a1f7
scratch/audit_k16_shifted_chunk_facet_bridge_20260731.py
  f14dd6c016814565a90d5b2dc4ffde1b0974b3aa98eeb103e417a3e92d964134
scratch/k16_shifted_chunk_facet_bridge_20260731.audit.json
  51b8e1c925229d39662878de1e1e65f71dbc33fdaa208d66cf44b97b98bc9747
  payload 744d5696de7ae56c0e8a5dd9f4c0e93e73ba7fe64df49a6373a955fe230fe937
```

No solver result is used anywhere in this audit.

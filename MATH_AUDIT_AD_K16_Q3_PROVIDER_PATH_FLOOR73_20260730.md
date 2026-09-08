# K16 q<=3 provider-path obstruction: exact cut floor 73

Date: 2026-07-30  
Lane: AD  
Status: proved for the authenticated direction-coherent q<=3 / upper-width-four
seam ledger.  Equality 70 is eliminated before separation, reverse-edge, q1,
or survivor constraints.  No claim is made for the older combined `WIDTH45`
catalogue or for unrestricted compound rethreads.

## 1. Frozen objects and notation

The source factor has SHA-256

```text
6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

and the authenticated q<=3 physical seam ledger has SHA-256

```text
832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

It contains 12,870 source transition indices and 211,604 admissible directed
seams.  The original defect bank is

\[
 \mathcal H=\mathcal H^-_2\sqcup\mathcal H^+_3,
 \qquad |\mathcal H^-_2|=45,\quad |\mathcal H^+_3|=48.       \tag{1.1}
\]

For a seam \(a\), let \(H(a)\subseteq\mathcal H\) be the set of distinct
original defects supplied by its new crossing windows.  Call \(a\) a
*provider* if \(H(a)\ne\varnothing\), and a *zero-hit seam* otherwise.
There are exactly 5,425 providers in this ledger, and the audited census is

\[
                        1\le |H(a)|\le2                       \tag{1.2}
\]

for every provider.  “Defect membership” below always means membership in
the distinct set \(H(a)\), not repeated window-occurrence multiplicity.

For a selected endpoint-balanced seam set \(Y\), write

\[
 p=|\{a\in Y:H(a)\ne\varnothing\}|,
 \qquad z=|\{a\in Y:H(a)=\varnothing\}|,
\qquad c=|Y|=p+z.                                           \tag{1.3}
\]

The endpoint equations say that every used transition index has selected
indegree and outdegree one.  Hence the directed graph formed by \(Y\) is a
vertex-disjoint union of directed cycles.

Let \(\rho\) rotate coordinates \(0,\ldots,14\) and fix coordinate 15.  The
decisive target set is the three-block bank

\[
 T=\mathcal O_{15}(33609)\sqcup\mathcal O_{15}(34069)
     \sqcup\mathcal O_{3}(46811),
 \qquad |T|=15+15+3=33.                                     \tag{1.4}
\]

All 33 members of \(T\) are original defects in \(\mathcal H\).

## 2. Provider paths after deleting zero-hit seams

### Lemma 2.1 (path decomposition)

Delete the \(z\) zero-hit seams from an endpoint-balanced selected seam set.
The remaining provider graph is a disjoint union of provider-only directed
cycles and at most \(z\) nonempty directed provider paths.

#### Proof

Consider one selected directed cycle.  If it contains no zero-hit seam, it
remains a provider cycle.  If it contains \(t>0\) zero-hit seams, deleting
them leaves at most \(t\) nonempty provider runs; adjacent zero-hit seams can
only reduce this number.  A zero-only cycle contributes no provider path.
Summing over the selected cycles gives at most \(z\) paths.  QED.

Let \(D\) be the directed graph of all 5,425 provider seams on the 12,870
transition indices, and contract the strongly connected components of
\(D\).  Every provider-only directed cycle lies inside one contracted
component.  Every provider path maps to a path in the resulting condensation
DAG.

## 3. Exact union-mask capacity

### Lemma 3.1 (two-target path capacity)

No provider seam internal to a strongly connected component of \(D\) hits a
member of \(T\).  Moreover, every directed provider path hits at most two
distinct members of \(T\).

#### Exact certificate and proof

The independent auditor recomputes the SCCs from the authenticated binary
ledger.  For every ordered pair of distinct SCCs it retains every distinct
33-bit mask supplied by a parallel provider seam.  At every SCC it starts
with the empty mask and propagates exact unions along a topological order of
the condensation DAG.

This deliberately relaxes physical paths: arrival and departure points
inside one SCC are treated as freely connectable, different paths need not be
vertex-disjoint, and connector existence is ignored.  Therefore every actual
provider-path trace is contained in the propagated family.

The exact replay gives

```text
provider arcs                         5,425
strong components                   12,804
ordered condensation pairs           5,350
exact endpoint union states          14,300
internal T-hitting provider arcs          0
maximum distinct T-mask size              2
```

The last two lines prove the claim.  Notice that the recurrence unions masks;
it does not add per-arc hit counts.  Thus a target appearing on two arcs of
one path is counted only once.  QED.

Equivalently, assigning integer weight five to each member of \(T\) gives
total target weight 165 and path capacity 10.  The eager master row is

\[
              2\sum_{a:H(a)=\varnothing} y_a\ge33,           \tag{3.1}
\]

or, integrally, \(z\ge17\).

## 4. The floor-73 theorem

### Theorem 4.1 (endpoint-service floor)

Every endpoint-balanced selection in the authenticated q<=3 seam ledger
which supplies all 93 original defects in the additive sense

\[
             \sum_{a:t\in H(a)}y_a\ge1\qquad(t\in\mathcal H) \tag{4.1}
\]

satisfies

\[
                          z\ge17.                             \tag{4.2}
\]

The independent provider edge-cover theorem gives

\[
                          p\ge56.                             \tag{4.3}
\]

Consequently

\[
                          c=p+z\ge73.                         \tag{4.4}
\]

#### Proof

By Lemma 2.1, deleting the \(z\) zero-hit seams leaves at most \(z\)
provider paths, together with provider cycles.  Lemma 3.1 says that provider
cycles hit no member of \(T\), while each provider path hits at most two.
All 33 targets in \(T\) must nevertheless be supplied.  Hence

\[
                         33\le2z,
\]

which gives (4.2).  The provider bound (4.3) is the exact
\(93-\nu(G)=93-37=56\) defect-edge-cover theorem, independently certified by
the provider audit with file SHA-256

```text
7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27
```

Every selected seam is either a provider or zero-hit, so adding (4.2) and
(4.3) proves (4.4).  QED.

Without four-separation, this endpoint-service system is an additive
relaxation and need not itself materialize a literal splice.  It is a sound
relaxation of the encoded separated master, which is all the lower-bound
argument requires.

No four-separation inequality, physical reverse-edge inequality, q1 row,
nondefect q2/q3 survivor row, residence condition, or arbitrary-upper CEGAR
row occurs in this proof.  In particular, exact cut counts 70, 71, and 72
already fail in the endpoint-plus-service relaxation.

The complete 2,506-mask audit in
`MATH_THEOREM_K16_PROVIDER_PATH_DUAL_FLOOR73_20260730.md` also materializes a
17-mask cover of all 48 cycle-unserviceable defects.  Hence 17 is the exact
cover number of the deliberately permissive path-mask universe.  This does
not construct vertex-disjoint provider paths or connector seams; it shows
that any further lower bound must use provider/path coupling, endpoint
disjointness, connector existence, separation/reverse, q1, or survivor data.

## 5. The exact equality face at 73

### Proposition 5.1

If equality \(c=73\) holds in Theorem 4.1, then:

1. \(p=56\), \(z=17\), and deletion of the zero-hit seams leaves exactly 17
   provider paths which all hit \(T\);
2. zero-hit seams are isolated between nonempty provider runs—there is no
   adjacent zero-hit pair and no zero-only selected cycle;
3. if \(d\) is the number of selected two-defect providers, then
   \(d\in\{37,38\}\), so the 56 providers have respectively zero or one
   repeated defect membership; and
4. writing \(M_i\subseteq T\) for the *distinct target mask* of path \(i\),
   either sixteen masks have size two and one has size one, with the 17 masks
   pairwise disjoint, or all seventeen masks have size two with exactly one
   unit of inter-mask overlap.  The latter case forces \(d=38\) and consumes
   the unique global \(H(a)\)-membership surplus.

#### Proof

Equality in \(p+z\ge56+17\) forces \(p=56,z=17\).  The 33 targets require at
least 17 provider paths by Lemma 3.1, while Lemma 2.1 permits at most 17, so
there are exactly 17.  Any adjacent zero-hit seams or zero-only cycle would
make the path count strictly smaller, proving items 1 and 2.

Eighteen defects have double-provider degree zero.  Each requires its own
singleton provider, so among 56 providers at most 38 can be double.  On the
other hand, 56 providers cover 93 distinct targets only if at least 37 are
double.  Thus \(d\in\{37,38\}\), and the total available defect-membership
count \(56+d\) is 93 or 94.  This proves item 3.

Seventeen masks of size at most two have total mask cardinality at most 34.
A zero mask would leave capacity at most 32 on the other sixteen paths, so
every mask is nonempty.  Covering 33 distinct targets gives exactly the two
mask-overlap cases in item 4.  A target may still occur on two seams within
one path; mask union intentionally counts it once.  Inter-mask overlap adds
one distinct-set provider membership globally, so the 34-incidence case
requires the unique surplus \(d-37=1\).  QED.

This is the correct next equality face for any subsequent endpoint/q1 audit.
The present work does not prove that this face is feasible.

## 6. Computational staging and audit corrections

The previously persisted exact-count-70 full-proto result is `INFEASIBLE`:

```text
scratch/k16_separated_port_master_exact70_20260730.audit.json
SHA-256 79a96eaa583d934455c7ad7f2f230177fe9a02855024db4d1e41f4978ecf31c3
model SHA-256 a641c228b75c1a31818bc2582c6a43273d3d076f6a42ce4dd486f9b079eb1d45
```

Theorem 4.1 strictly subsumes that radius-70 exclusion and localizes it to a
weaker row family.  A staged endpoint-service CP run under a 4 GiB address
cap ended in `MemoryError` and is `UNKNOWN`; it is not evidence.  A separate
14-path DFS timed out and is also `UNKNOWN`.  Neither is used.

An early draft tried to add target hits along condensation arcs.  Independent
replay returned additive maximum three, because the same target can occur on
two arcs of one path.  That draft was rejected.  Lemma 3.1 uses exact bitwise
unions and independently returns maximum distinct cardinality two.

A floating LP was used only to discover the 33-target half-weight dual.  The
authoritative proof and v3 certificate invoke no LP or SAT solver: they replay
all exact union states and verify the integer capacity directly.

The full frozen proto at exact count 73 also has a trusted-CP-SAT transcript
reporting `INFEASIBLE`, but this is not a formal UNSAT certificate.  It uses
all q1 and q2/q3 rows and has not yet been localized beyond the equality face
of Proposition 5.1:

```text
scratch/k16_separated_port_master_exact73_20260730.audit.json
SHA-256 f7860f3237abf6df3d9ba7a0a27b098f16fe6a08f39bb7a7dd3c29fa42e7fd89
payload SHA-256 744b0332aa3ae2ddd6eaceead6f61b0bf7370a7f47a05b93d894938d4ce67e57
```

Thus no q1 incompatibility is needed to eliminate count 70.  Whether count
73 already fails at endpoint service, separation/reverse, or q1 is the next
unresolved localization question.

## 7. Authoritative certificate

```text
scratch/audit_ad_k16_provider_path_subset_floor73_20260730.py
SHA-256 fc7413559ee1de8653eccb49c86a2f41b7e3fb5f39d077d1cd7fa451221b13e5

scratch/ad_k16_provider_path_subset_floor73_v3_20260730.audit.json
SHA-256 00404a022a84cefc4249930726775ccb57a57cc75a2be0098a4499dca2fe24fd
payload SHA-256 225f9e86c8b156dabc519e7f24a5a61dffa5b34eb194a203faa53c6ab1d2b385

scratch/ad_k16_provider_path_subset_floor73_v3_20260730.resource.txt
SHA-256 5236edfa09361783a4ae6766599a3ace9a4b10d13895956f8e03f95c46638f13

scratch/ad_k16_provider_path_subset_floor73_v3_20260730.stdout.txt
SHA-256 fea723b3de9df6a31610427c20c26cc8e47f8910b29a64bd3fd7aeac9aa756b5
```

The H100-CPU replay used one process, a 2 GiB address-space cap, 3.02 wall
seconds, and 347,036 KiB maximum RSS.

The v3 auditor independently proves only the zero-hit/path bound \(z\ge17\).
It embeds the expected provider-audit SHA but does not open and rehash that
file.  The total floor 73 is therefore formally the composition of this v3
certificate with the separately authenticated provider-floor-56 certificate,
not one monolithic replay.

## 8. Exact scope boundary

The theorem applies to the authenticated direction-coherent q<=3 /
upper-width-four seam ledger with 5,425 providers.  It does **not** transfer
automatically to the older combined `WIDTH45` graph: that graph has 150
additional width-five-only singleton providers, and those arcs can change
the provider SCCs and path capacity.  It also says nothing about
non-separated interacting windows, compound seam gadgets, arbitrary
successor rethreads, connectivity, compiler completion, or `nu(16)`.

Within its stated ledger, however, the boundary is unconditional and
integral:

\[
 \boxed{\text{endpoint balance + 93 service rows}\Longrightarrow c\ge73.}
\]

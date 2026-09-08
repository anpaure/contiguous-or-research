# Audit of the k16 27-core beam: transition circuits, packet locks, and exact Hall rank

Date: 2026-07-29  
Lane: K  
Status: independently replayed, theorem-level finite audit  
Scope: the fixed `resume1` resident endpoint and the named q1 factors only

## 1. Verdict

There are two distinct censuses in the saved artifacts, and they must not be
conflated.

1. The saved beam
   `scratch/k16_resume1_portalq1_multicore_beam23_w8_d6_20260729.json`
   was run with the earlier **scalar saturation-core** score.  Its path is

   \[
   (3,29)\to(2,13)\to(1,6)\to(0,0).
   \]

   Its embedded census objects contain `saturation_core_count` and do not
   contain `unit_core_count`.  Its status `ZERO_SATURATION_CORES` is correct
   for that earlier statistic.

2. Replaying the identical three legal physical \(C_6\) moves with the current
   full interaction-core analyser gives

   \[
   (30,554)\to(29,548)\to(27,461)\to(27,501),
   \tag{1.1}
   \]

   where the entries are

   \[
   (\text{number of peeled unit cores},
     \text{union of their row tags}).
   \]

   Thus the last move clears the last scalar saturation core but leaves 27
   interaction cores and increases their row union from 461 to 501.

3. The materialized endpoint
   `scratch/k16_q1_endpoint_resume1_zero_saturation_cores_20260729.json`
   is exactly the replayed final factor.  Its physical-edge digest is

   ```text
   87f7a7ccb2d32b13f278dab4bb0b20c62000c2c394a52e0bcd364d3b9df64f5e
   ```

4. The later saved interaction report records score
   \((27,517,0,2250,3)\), whereas the current source replays the same frozen
   factor as \((27,501,0,2250,3)\).  The factor SHA is the same.  The analyser
   source was edited after both saved search artifacts and the saved report
   contains no analyser-source hash.  Therefore the old row-union value 517
   is not reproducible from the current source.  The core count 27 is stable
   in this comparison, but 517 must not be used as a frozen invariant.

5. Every one of the 27 current displayed cores has been reconstructed from
   its palette, endpoint, and motif row tags and independently unit-refuted.
   Their motif-row sets are pairwise disjoint.  Consequently the fixed final
   overlay has an exact, solver-free lower bound of **27 unavoidable motif
   holes**.  There is no matching 27-hole feasible assignment, so equality is
   not proved.

6. The number of cores is not monotone on the legal trade graph.  Legal
   alternating trades are reversible; concretely, the inverses of the first
   two beam moves raise the current count \(29\to30\) and \(27\to29\).
   The audited strict-token local chase additionally contains an exact
   two-cycle.

The correct canonical quantity is the circuit-hypergraph transversal number
defined below, not a particular greedy peeling count.

## 2. Fixed-overlay system

Fix a resident factor \(R\) and a q1 factor \(Q\).  Put

\[
B=Q\setminus R,\qquad A=R\setminus Q.
\]

For \(e\in B\), let \(b_e=1\) mean that \(e\) is deleted from \(Q\).  For
\(f\in A\), let \(a_f=1\) mean that \(f\) is added.  The base binary system
\(\mathcal B_R(Q)\) consists of:

- the two endpoint inequalities whose conjunction is

  \[
  \sum_{f\in A(v)}a_f=\sum_{e\in B(v)}b_e
  \tag{2.1}
  \]

  for every middle vertex \(v\);

- for every lower and upper q1 colour \(c\),

  \[
  \sum_{e\in B_c}b_e-\sum_{f\in A_c}a_f
  \le \mu_Q(c)-1;
  \tag{2.2}
  \]

- \(a_f,b_e\in\{0,1\}\).

The all-zero assignment belongs to \(\mathcal B_R(Q)\).  Hence any
infeasibility arises only after residence motif rows are imposed.

For a short-run occurrence \(M\), let \(C_M\) be its cut closure.  Its row is

\[
\sum_{e\in C_M\cap B}b_e\ge1.
\tag{2.3}
\]

This audit concerns exactly (2.1)--(2.3), with both q1 palettes.  It says
nothing by itself about newly created seam motifs, top residence, deeper
shadows, connectivity, or the compiler.

## 3. Exact circuit-transversal theorem

Let \(\mathcal M(Q)\) be the finite set of inherited motif rows.  Define the
**overlay circuit hypergraph** \(\mathscr C_R(Q)\) on vertex set
\(\mathcal M(Q)\) as follows: its hyperedges are the inclusion-minimal sets
\(C\subseteq\mathcal M(Q)\) for which

\[
\mathcal B_R(Q)\quad\text{together with all motif rows in }C
\]

is infeasible.

Define the exact motif-hole deficiency

\[
\Delta_R(Q)=min_{x\in\mathcal B_R(Q)}
 \bigl|\{M\in\mathcal M(Q):x\text{ violates row }M\}\bigr|.
\tag{3.1}
\]

### Theorem 3.1 (exact Hall-rank normal form)

\[
\boxed{\Delta_R(Q)=\tau(\mathscr C_R(Q))},
\tag{3.2}
\]

where \(\tau\) is hypergraph transversal number.  Consequently

\[
\rho_R(Q):=|\mathcal M(Q)|-\Delta_R(Q)
\tag{3.3}
\]

is the exact maximum number of inherited motif rows simultaneously
satisfiable inside the fixed overlay.

#### Proof

Let \(x\in\mathcal B_R(Q)\), and let \(H(x)\) be its set of violated motif
rows.  If some circuit \(C\) were disjoint from \(H(x)\), then \(x\) would
satisfy every row in the infeasible subsystem \(C\), a contradiction.  Thus
\(H(x)\) meets every circuit, and

\[
|H(x)|\ge\tau(\mathscr C_R(Q)).
\]

Minimizing over \(x\) proves \(\Delta_R(Q)\ge\tau\).

Conversely, let \(H\) be a minimum transversal.  If the base system together
with every motif row in \(\mathcal M(Q)\setminus H\) were infeasible, finiteness
would give an inclusion-minimal infeasible subset
\(C\subseteq\mathcal M(Q)\setminus H\).  Then \(C\) would be a circuit missed
by \(H\), contradiction.  Hence those remaining rows are simultaneously
feasible and all holes lie in \(H\).  Therefore
\(\Delta_R(Q)\le|H|=\tau\).  This proves (3.2), and (3.3) follows. \(\square\)

### Corollary 3.2 (packing lower bound)

Let \(\nu(\mathscr C_R(Q))\) be the maximum number of pairwise motif-disjoint
circuits.  Then

\[
\nu(\mathscr C_R(Q))\le
\tau(\mathscr C_R(Q))=Delta_R(Q).
\tag{3.4}
\]

More generally, any family of pairwise motif-disjoint infeasible packets
certifies the same lower bound: shrink each packet to a minimal circuit.

For the final factor, the independent replay reconstructs 27 pairwise
motif-disjoint unit-refutable packets.  Hence

\[
\boxed{27\le \nu(\mathscr C_R(Q))le
       \tau(\mathscr C_R(Q))=\Delta_R(Q)}.
\tag{3.5}
\]

This is the rigorous meaning of the present “27-core” statement.  It does
not prove \(\Delta_R(Q)=27\), because neither a 27-element transversal nor a
base-feasible assignment with exactly 27 motif holes has been supplied.

The peeling algorithm produces one certified packing.  It need not produce
a maximum packing and is not itself the definition of \(\nu\), \(\tau\), or
\(\Delta\).

## 4. AA/BB portal replay

The three quotient moves forming the five-orbit portal are, in order:

1. a BB alternating square;
2. a second BB alternating square, with the two BB squares telescoping to the
   recorded BB \(C_6\);
3. an AA alternating square.

All three preserve degree two and complete lower and upper q1 support.  Under
the current full interaction census the exact stage table is

| stage | unit cores | core-row union | static blockers | motifs | components |
|---:|---:|---:|---:|---:|---:|
| source | 31 | 541 | 2 | 2205 | 5 |
| first BB square | 31 | 539 | 2 | 2250 | 6 |
| second BB square | 31 | 556 | 1 | 2265 | 8 |
| AA square | 30 | 554 | 0 | 2250 | 5 |

The exact core-signature transitions are

| move | unchanged | removed | created |
|---|---:|---:|---:|
| first BB square | 29 | 2 | 2 |
| second BB square | 29 | 2 | 2 |
| AA square | 30 | 1 | 0 |

Thus the BB moves translate packets without reducing their number, and the AA
move removes one.  Reversing the AA move is a legal increase \(30\to31\).
Neither static-blocker count nor scalar saturation count controls the full
interaction rank.

## 5. Three-C6 beam replay

The current full-census table along the saved winning path is

| stage | unit cores | core-row union | scalar saturation cores | motifs | components |
|---:|---:|---:|---:|---:|---:|
| 0 | 30 | 554 | 3 | 2250 | 5 |
| 1 | 29 | 548 | 2 | 2250 | 5 |
| 2 | 27 | 461 | 1 | 2250 | 5 |
| 3 | 27 | 501 | 0 | 2250 | 3 |

The exact core-signature transitions are

| move | unchanged | removed | created |
|---|---:|---:|---:|
| first \(C_6\) | 29 | 1 | 0 |
| second \(C_6\) | 26 | 3 | 1 |
| third \(C_6\) | 26 | 1 | 1 |

The first two \(C_6\) moves preserve q1 support but not the physical q1 load
multisets term by term.  The third is strict-token on both shores:

\[
\lambda_-(D)=\lambda_-(A)=\{50467,50474,50530\},
\]

\[
\lambda_+(D)=\lambda_+(A)=\{50987,51043,51050\}.
\]

The third move destroys the familiar single-motif socket packet with closure

\[
\{(50531,51042),(50531,52547),(52547,56642)\}
\]

and rows

\[
U51043,U55747,U56643,U63811,V55619.
\]

It creates one four-motif interaction packet instead.  Hence scalar success
is achieved by translating and enlarging a packet, not by removing the full
obstruction.

## 6. Packet-lock geometry of the final 27 cores

The 27 independently refuted packets contain motif-row counts

\[
1^{19},\quad2^5,\quad3^2,\quad4^1.
\tag{6.1}
\]

They therefore use 39 pairwise distinct motif rows in total.

Join two packets when they share a nonmotif q1 or endpoint row.  The resulting
interaction graph has 40 edges and component sizes

\[
17,4,2,1,1,1,1.
\tag{6.2}
\]

In contrast, join packets only when their motif closures share a physical
edge.  That graph has just two edges and component sizes

\[
2,2,1^{23}.
\tag{6.3}
\]

Thus the main locks are nonlocal: physically disjoint motif closures are tied
through common palette-provider and endpoint-degree rows.  Treating each
motif as an independent “edge to cut” loses precisely this remote coupling.

The most reused nonmotif rows occur in five packets:

\[
L42627,\quad L59010,\quad U34367,\quad V59011.
\]

These high-incidence rows are natural packet sockets, but their incidence
alone is not an additive capacity: one exterior provider or endpoint
rethread can alter several packets simultaneously.

## 7. Exact strict-token transition cycle

The separately audited strict-token chain supplies a literal transition
cycle.  From \(F_1\), delete

\[
\{(41147,57499),(41627,41657),(57529,58009)\}
\]

and add

\[
\{(41147,41627),(41657,58009),(57499,57529)\}.
\]

The lower ledgers on both shores are

\[
\{41115,41625,57497\},
\]

and the upper ledgers are

\[
\{41659,57531,58041\}.
\]

This maps \(F_1\) to \(F_2\).  Complete radius-three strict-token censuses
through every saved core edge show that the unique corresponding move out of
the translated \(F_2\) core is the inverse move, returning to \(F_1\).
Both packet proofs use the same locked remote socket at vertex 49819.

Therefore the local rule “hit the current core by a strict-token \(C_6\)” is
trapped in

\[
F_1\longleftrightarrow F_2.
\tag{7.1}
\]

The scope is exact but narrow: radius-three, strict-token, through the saved
core edges, and in the fixed \(F/R_1\) overlay.  A \(C_8\), a non-strict
protected-token move, an exterior provider, or a simultaneous resident
rethread remains outside the no-go.

## 8. Monotonicity theorem and the usable potential

### Proposition 8.1 (reversible-move obstruction)

Let \(G\) be the graph whose vertices are q1 factors and whose edges are legal
alternating exchanges from a move class closed under inversion.  If an
integer statistic \(P\) is nonincreasing along every legal move, then \(P\)
is constant on every connected component of \(G\).

#### Proof

For every edge \(Q\leftrightarrow Q'\), monotonicity in both directions gives
\(P(Q')\le P(Q)\) and \(P(Q)\le P(Q')\).  Hence equality holds on each edge,
and therefore on each connected component. \(\square\)

The current core count is visibly nonconstant: the first beam move gives
\(30\to29\), and the second gives \(29\to27\).  Their inverses give legal
increases.  Thus neither peeled-core count, maximum circuit packing, nor exact
deficiency can be an **unoriented** move-monotone unless it happens to be
constant on the restricted component.

The useful exact Hall potential is instead

\[
\Delta_R(Q)=\tau(\mathscr C_R(Q)),
\]

with a certificate sandwich

\[
\underbrace{\widehat\nu(Q)}_{	ext{disjoint refuted packets}}
\le
\Delta_R(Q)
\le
\underbrace{\widehat h(Q)}_{	ext{holes of a base-feasible assignment}}.
\tag{8.1}
\]

A descent claim is proof-safe only when it does one of the following:

- exhibits a smaller feasible hole set \(\widehat h\);
- proves a smaller exact transversal number by matching lower and upper
  certificates;
- supplies an oriented exchange lemma ensuring \(\Delta_R(Q')<\Delta_R(Q)\);
- or works with the global legal-trade distance to the completion set.

The scalar saturation count and the greedy number of peeled packets can rank
heuristics, but neither is a Lyapunov function.  In particular, clearing all
scalar saturation cores is not a valid stopping condition.

## 9. Reproducible audit

The new audit performs no search.  It replays the frozen moves, recomputes the
current census, reconstructs all 27 core row systems independently, verifies
their unit contradictions and motif disjointness, builds the two packet
intersection graphs, and verifies the strict-token inverse cycle.

Audit script:

```text
scratch/audit_k16_27core_beam_hall_rank_20260729.py
SHA-256 2ccd1a103b872307021783bf19c1c246fa65a5a0f260d801c99bb99cd33c2bed
```

Output:

```text
scratch/k16_27core_beam_hall_rank_20260729.audit.json
SHA-256 c32261739d55c7be4022ad6cc10733d818d2200ee89082724ae5d6244dd1f9b4
```

The decisive boundary is:

> The fixed final overlay has at least 27 unavoidable inherited-motif holes,
> certified by 27 pairwise motif-disjoint unit-refutable packets.  The exact
> deficiency is the circuit-transversal number.  Its value, a legal trade
> decreasing it, and any full completion outside the fixed overlay remain
> open.

## 10. Addendum: corrected portal24 chain through the radius-{2,3} one-core trap

After the preceding audit was frozen, a linked sequence of corrected
`portal24` reports appeared.  A lightweight metadata audit verifies every
file-to-file SHA link, every saved initial/best score, degree balance of every
displayed alternating move, zero q1 holes in every saved endpoint, and
pairwise motif-disjointness of each endpoint's displayed peeled packets.

The full saved greedy sequence is

\[
27,21,18,16,14,12,11,9,8,7,6,5,4,3,2,1,1,
\tag{10.1}
\]

with row-union sequence

\[
501,390,301,249,226,213,166,150,110,86,64,49,42,18,12,7,3.
\tag{10.2}
\]

The accompanying motif/component coordinates of the lexicographic score vary
throughout; in particular the chain is not a monotone residence or topology
chain.  All endpoints remain q1-complete.

The rigorous rank interpretation of (10.1) is only

\[
c_i\le \nu(\mathscr C_R(Q_i))le
\tau(\mathscr C_R(Q_i))=\Delta_R(Q_i)
\tag{10.3}
\]

at each separate endpoint \(Q_i\).  A decrease \(c_i>c_{i+1}\) is a decrease
in the size of one certified disjoint circuit packing.  It does **not** imply

\[
\Delta_R(Q_{i+1})<\Delta_R(Q_i).
\]

No endpoint in the chain has a matching feasible-hole upper certificate.
Thus (10.1) is valuable proof-directed search evidence, but it is not an
exact Hall-rank descent theorem.

### The current last packet

From the state with score

\[
(2,12,0,2248,4),
\]

an alternating square reaches

\[
(1,7,0,2248,3).
\]

The subsequent complete restricted scan generates exactly two connected
q1-preserving trades of radii two or three through the current core support
and scores both.  Neither reaches zero peeled cores.  The lexicographically
best endpoint has score

\[
(1,3,1,2248,3).
\tag{10.4}
\]

Its sole displayed packet is motif 1839.  Its closure is

\[
\{(33715,41395),(34233,41401),(41395,41401)\},
\]

and its two removable blue candidates are

\[
(34233,41401),\qquad(41395,41401).
\]

The first is locked by upper row \(U42425\), the second by lower row
\(L41393\).  Therefore this endpoint has a literal static one-motif circuit,
and

\[
\Delta_R(Q)\ge1.
\]

It is not proved that \(\Delta_R(Q)=1\): other non-unit interaction circuits
may remain after deleting motif 1839.  Similarly, a future score with zero
peeled unit cores would not by itself prove \(\Delta=0\); it would only say
that this propagation procedure found no circuit.

The last-step no-go is complete only for connected q1-preserving alternating
\(C_4/C_6\) trades through the displayed core support.  It excludes neither
\(C_8\) or larger circuits, disconnected circuit unions, a neutral remote
router followed by a splitter, nor simultaneous motion of the resident
endpoint.

Metadata audit:

```text
scratch/audit_k16_portal24_chain_metadata_20260729.py
SHA-256 fa54c3b6ccfd82633d1bdabbb0c12a23c3134ae11e9b5bde8df1dc7516764e72
```

Output:

```text
scratch/k16_portal24_chain_metadata_20260729.audit.json
SHA-256 7870c58f79c8618e323a25ecb2e282f70e897ae4b599ffc96f68c5a9799cd2e2
```

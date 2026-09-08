# K17 occurrence296+C6: surviving guarded cut, first balanced packet bank, and exact projected cost-to-go arc

Date: 2026-07-31  
Lane: R, guarded Rado / signed cost-to-go  
Status: exact, source-relative theorems and independently replayed finite
certificate.  This does **not** produce an accepting K17 compiler, a K17
word, or an all-dimensional contraction theorem.

## 0. Executive theorem

Let \(b\) be the independently authenticated occurrence296+C6 checkpoint
whose owner-cycle SHA-256 is

```text
a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49.
```

The old rank-zero obstruction survives exactly in the following sense.

1. **Fixed residual-\(U\) fibre.**  The C6 history changes neither the
   occurrence base nor a macro interior.  Hence the 296 component-interior
   occurrence defects \(I_{296}\) and the 177 arbitrary-residual-\(U\)-zero
   rank-ten targets \(Z_{177}\) still have empty neighbourhood under every
   finite residual-\(U\) circuit compound:
   \[
      r_M\bigl(A(I_{296}\sqcup Z_{177})\bigr)=0<473                 \tag{0.1}
   \]
   for every guard matroid \(M\) on that pure fibre.

2. **Balanced complement exchanges.**  Once same-lower-colour complement
   exchanges are admitted, \(I_{296}\) is not an invariant and must be
   removed from the cut.  Arity one cannot balance owner degrees, and among
   all pairs from the complete 545,721-column primitive catalogue the
   arity-two bank is empty.  The first nonempty
   balanced bank is the support-two arity-three bank: its columns are
   directed endpoint triangles, equivalently alternating C6 packets.  The
   complete bank has 13,871 one-path packets.

3. **What remains rank zero.**  These P3 packets provide 1,462 of the 1,585
   current rank-ten holes, leaving a 123-target empty-neighbourhood cut
   \(Z_{123}\) in the atomic one-packet service projection.  On the
   distinguished old set \(Z_{177}\), they provide
   151 targets and leave the explicit 26-target set
   \[
   \begin{split}
   Z_{26}=\{&34775,34806,42739,48809,50551,53155,55189,60337,\\
            &61077,61240,63849,64810,69612,71579,75706,75725,\\
            &79407,80686,81266,82811,89816,93215,95154,97667,\\
            &97985,97992\}                                      \tag{0.2}
   \end{split}
   \]
   with payload SHA-256
   `1b41458e4841f1d96292b8fc70be0a93bc7050ef2fb899179c69f1b741cda327`.
   Thus \(Z_{26}\) is the exact zero-degree part of the old target cut in the
   **unguarded** union of the frozen residual-C6 and frozen support-two P3
   atomic candidate relations.  It remains a 26-row lower bound after any
   guard prunes columns, but the exact guarded zero set may be larger.  This
   statement is neither deletion-stable under regeneration after applying a
   packet nor a no-go for a synergistic mixed compound whose target effect
   is absent from every constituent atom.

4. **A literal signed projected-cost arc.**  Packet 584 is independently
   replayed.  It preserves owner degree, the single owner cycle, every
   lower-q1 colour, and the literal marked path.  The aggregate D2/D3,
   replay, and recorded envelope-proxy values are unchanged.  Its exact
   upper-shadow transport is
   \[
   \begin{array}{c|c|c}
   \text{rank}&\text{newly covered}&\text{newly missing}\\ \hline
   10&\{0xb73a,0x1173b,0x1333e\}&\varnothing\\
   11&\{0xb73b,0x1333f\}&\varnothing\\
   12&\varnothing&\{0xb73f\}.
   \end{array}                                                   \tag{0.3}
   \]
   Only \(0x1173b\), not all three rank-ten gains, belongs to the old
   \(Z_{177}\).  For rank weights \(w_{10},w_{11},w_{12}\), the exact
   one-step derivative is
   \[
                  \Delta\Phi=-3w_{10}-2w_{11}+w_{12}.             \tag{0.4}
   \]

The frozen P3 bank therefore gives a genuine nonempty provider actuator,
but not an accepting repair.  The exact common-cap object is undefined at
this upstream-invalid checkpoint; host redundancy and envelope volume are
only numerical proxies.

## 1. Authenticated checkpoint and obligations

The source-relative state is frozen by:

| object | SHA-256 |
|---|---|
| candidate JSON | `960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c` |
| residual JSON | `6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4` |
| owner cycle | `a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49` |
| H2 independent audit | `fc6716d285f774c246e22b7cbfd9a29f69391ace9f7d8089061d2fed57f38be7` |
| H4 independent audit | `0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4` |

Its exact relevant ledger is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{rank-nine owners / lower-q1 colours}&24310/24310\text{, exact}\\
\text{physical owner components}&1\\
\text{marked owners}&4108\\
\text{strict D2/D3 defects}&503/503\\
\text{replay rows / missing row bits}&748/776\\
\text{upper holes in ranks }10,11,12&1585,824,116\\
\text{upper holes in ranks }13,\ldots,17&0,0,0,0,0\\
\text{occurrence-interior defects}&296\text{ in }157\text{ components}.
\end{array}                                                       \tag{1.1}
\]

The maximal envelopes are all nonempty, with minimum size 6, host
redundancy 252,803 and envelope volume 150,224.  These values do not imply
literal inversion or common-cap feasibility: 776 row bits are still
missing, so the common guard family is empty at the compiler type boundary.

## 2. Action classes and owner boundary

Fix the accepted lower-q1 factor.  For each rank-eight lower colour \(L\),
its current complement edge is an unordered pair \(e_L=\{a,b\}\) of
rank-nine owners containing \(L\).  A primitive same-colour exchange is

\[
             p=(L;e_L\to f),\qquad f=\{u,v\}\ne e_L,             \tag{2.1}
\]

where both endpoints of \(f\) contain \(L\).  Its owner-degree boundary is

\[
             \partial p=\mathbf e_u+\mathbf e_v-\mathbf e_a-\mathbf e_b.
                                                                    \tag{2.2}
\]

A packet \(P\) is owner-balanced when
\(\sum_{p\in P}\partial p=0\).  It is a **one-path packet** when replacing
all old edges by all new edges leaves one owner cycle.  Lower-q1 exactness
then follows because every replacement keeps its labelled lower colour.

There are three distinct action families.

* A residual-\(U\) circuit changes only residual port routing and keeps the
  occurrence base and all macro interiors fixed.
* An occurrence move changes the macro base and needs a fresh residual
  lift; it cannot be treated as a residual-circuit column.
* A balanced complement packet changes complement chronology while
  preserving owner degree and the lower palette.  It may change interior
  run signatures and upper providers.

Consequently an invariant proved for the first family cannot be imported
into the third.

## 3. Exact survival of the old rank-zero cut

Let \(\mathscr C_U(b)\) be the set of all finite compounds of residual-\(U\)
circuits on the fixed occurrence base underlying \(b\).  Compound length
and circuit support are unrestricted.

Let \(I_{296}\) be the occurrence-labelled short runs wholly internal to
fixed macro components.  Let \(Z_{177}\) be the rank-ten set having no
provider even in the previously audited arbitrary locally admissible
residual-\(U\) pairing relaxation; its payload SHA-256 is

```text
b383958488c70ea67ecf5678f84677c68e666cbf5eb4a1f98b7ecd48bee3f778.
```

### Theorem 3.1 (fixed-fibre survival)

For every \(C\in\mathscr C_U(b)\):

1. every obligation in \(I_{296}\) remains; and
2. no target in \(Z_{177}\) is created.

Hence (0.1) holds for every serialization and every guard matroid on this
pure fibre.

#### Proof

The authenticated 1,160-C6 history and every further residual circuit keep
the occurrence base and each macro interior fixed.  A strict short run whose
entire defining three- or four-edge collar lies inside such an interior is
therefore unchanged, proving (1).  The exact profile is 114 length-two
collars and 182 length-three collars, with formal weight
\(114+2\cdot182=478\).

The relaxation defining \(Z_{177}\) contains every locally admissible
residual-\(U\) incidence available to a residual circuit and drops global
degree and connectivity restrictions.  A target with no provider in this
superset has no provider in any circuit compound, proving (2).  Candidate
sets for all 473 obligations are empty, and every matroid has rank zero on
the empty set. \(\square\)

### Scope boundary

A complement exchange changes physical owner adjacencies and upper unions.
It need not preserve a macro-interior run signature.  Thus \(I_{296}\) is
not a valid obligation bank for the broadened action class.  The P3 census
below also directly repairs 151 targets of \(Z_{177}\), so \(Z_{177}\)
itself is not invariant there.

## 4. Packet girth and the first nonempty balanced layer

### Lemma 4.1 (no balanced singleton)

Every nontrivial primitive column has nonzero boundary.  Therefore no
arity-one packet is owner-balanced.

#### Proof

Equality \(\partial p=0\) would make the old and new unordered endpoint
multisets equal, hence \(f=e_L\), contrary to (2.1). \(\square\)

### Lemma 4.2 (no balanced pair in a fixed lower-rainbow factor)

Two distinct primitive same-colour exchange columns relative to one fixed
lower-rainbow factor cannot have opposite nonzero boundaries.

#### Proof

Colour the two old edges red and the two new edges blue.  Opposite
boundaries say that red and blue degrees agree at every owner.  After
cancelling any common red-blue edge, a nonempty remainder is an alternating
C4; the empty/reverse case already forces the two lower colours equal.

Write a nondegenerate C4, after relabelling, as red edges \(AB,CD\) and
blue edges \(AC,BD\).  The first exchange gives
\(A\cap B=A\cap C=L_p\).  Hence the distinct owners \(B,C\) both contain
\(L_p\), so \(B\cap C=L_p\).  The second exchange gives
\(C\cap D=B\cap D=L_q\), whence the same two owners satisfy
\(B\cap C=L_q\).  Thus \(L_p=L_q=L\).  In the empty/reverse case, equality
of an old edge of one column with a new edge of the other gives the same
conclusion directly.

A fixed lower-rainbow factor has a unique old edge \(e_L\).  Both columns
therefore have old edge \(e_L\); balance forces the two new endpoint
multisets together to be two copies of \(e_L\), so both new edges equal
\(e_L\), contradicting nontriviality. \(\square\)

The complete checkpoint census independently gives 545,721 distinct
boundaries and zero opposite pairs.  Thus the full P2 bank, including
support-four primitives, is empty.

### Lemma 4.3 (support-two P3 normal form)

Suppose a primitive column retains one old endpoint and moves its other
endpoint from \(x\) to \(y\).  Write it as the directed arc \(x\to y\), so
its boundary is \(\mathbf e_y-\mathbf e_x\).  Three nontrivial support-two
columns balance if and only if their arcs form a directed triangle, up to
cyclic ordering.

#### Proof

Balance says that the three arcs form an Eulerian directed multigraph.
Loops are excluded.  A directed two-cycle would leave the third arc
unbalanced unless it were a loop.  The only remaining three-arc Eulerian
multigraph is a directed triangle.  Conversely, the three triangle
boundaries telescope to zero. \(\square\)

When the three columns have distinct lower colours and no physical
incidence cancels, the two endpoint matchings around this triangle form a
simple alternating C6.  P1/P2 emptiness rules out a proper balanced
subpacket, and the frozen catalogue checks simplicity explicitly for all
retained records.  After deleting the three old cycle edges, the one-path
condition is an exact four-fragment reconnection test.

### Theorem 4.4 (complete first bank at the checkpoint)

The complete support-two P3 census at \(b\) has

\[
\begin{array}{c|r}
\text{directed endpoint triangles}&28114\\
\text{disconnected reconnections}&14243\\
\text{one-path balanced packets}&13871.
\end{array}                                                       \tag{4.1}
\]

Their net rank-ten gain profile is

\[
-3:417,\ -2:1874,\ -1:4478,\ 0:5597,\
+1:1341,\ +2:156,\ +3:8.                                      \tag{4.2}
\]

In particular 1,505 packets have positive net rank-ten gain.  Since P1 and
P2 are empty, this is the first nonempty balanced provider bank by arity.

## 5. Frozen-bank Rado diagnostics

Let \(T_{10}\) be the 1,585 current rank-ten holes and \(\mathcal P_3\) the
13,871 one-path packets.  Join \(t\in T_{10}\) to \(P\in\mathcal P_3\) when
applying \(P\) to the frozen checkpoint newly covers \(t\).  This is a
**one-credit service graph**: a matching assigns at most one target credit
to a packet, even when the physical packet covers several targets.

### Theorem 5.1 (exact marginal service)

The graph has:

* 4,074 packets incident with at least one target;
* 4,599 service incidences;
* 1,462 nonempty target rows and 123 empty rows;
* free-packet Rado rank 1,459.

The canonical payload SHA-256 of the 123 empty rows is
`a1d3249958bb50c7c0ff4de91aa84ca58823881ab612c55ec93a8faa4a7e906f`.

A maximum-deficiency alternating Hall witness has 129 target rows and 3
packet vertices, hence one-credit deficiency 126.  Its nonempty core is

\[
\begin{split}
T_*&=\{48782,63344,63662,74463,94430,95608\},\\
P_*&=\{1065,4812,8663\}.                                      \tag{5.1}
\end{split}
\]

Each of the three packets in \(P_*\) can cover two of these six targets.
Thus (5.1) is a real obstruction to **unit-credit serialization**, but not
a physical impossibility certificate for simultaneous hyperpacket service.
The empty set \(Z_{123}\), in contrast, is a rank-zero cut for every guard
matroid on this frozen **atomic candidate relation**.  It does not exclude a
synergistic compound whose literal effect is not the union of its atomic
service rows.  The set of zero rows is exactly \(Z_{123}\) before guard
pruning; an actual guard may delete more columns and enlarge it.

#### Proof

The counts and matching rank come from the independent reconstruction of
every P3 packet and every rank-ten load change.  A target row with no
incident packet has empty candidate set under any further guard restriction
of this atomic relation, so the 123-row claim is unconditional inside the
declared Rado model.  Ordinary Hall/Rado with the free matroid gives the
matching statements.  The final caveat follows because the graph
deliberately caps a packet at one credit, whereas literal application
retains all of its gains. \(\square\)

If one additionally requires no loss of any currently covered rank-ten
target, 1,292 packets remain.  They give 1,457 incidences on 892 targets and
free-packet Rado rank 873.  This restriction says nothing about ranks 11+
or other guards.

### Corollary 5.2 (atomic survivor of the old target cut)

On \(Z_{177}\), the all-service P3 graph has 389 incidences, covers and
matches 151 targets, and has exactly the 26 empty rows (0.2).  Therefore the
empty-neighbourhood projection of the old target cut contracts from 177 to
26 when the frozen P3 atoms are added.  This neither supplies a compatible
151-target repair nor excludes multi-atom synergy on the remaining rows.

The hexadecimal form of \(Z_{26}\) is

```text
87d7 87f6 a6f3 bea9 c577 cfa3 d795 ebb1 ee95 ef38 f969 fd2a
10fec 1179b 127ba 127cd 1362f 13b2e 13d72 1437b 15ed8 16c1f
173b2 17d83 17ec1 17ec8
```

## 6. Exact signed projected cost at packet 584

For an upper target set at rank \(r\), let \(h_r\) be its literal hole
count.  For nonnegative weights \(w_r\), define the truncated append-cost
potential

\[
                         \Phi_w=\sum_{r=10}^{12}w_rh_r.            \tag{6.1}
\]

For a packet \(P\), let \(G_r(P)\) and \(L_r(P)\) be the newly covered and
newly missing rank-\(r\) targets.  Then the exact signed derivative is

\[
       \Delta_P\Phi_w=\sum_{r=10}^{12}w_r
                  \bigl(|L_r(P)|-|G_r(P)|\bigr).                  \tag{6.2}
\]

This is an identity, not an independence assumption or a physical action
cost.  Derivatives of sequential packets cannot be summed from the initial
catalogue without regenerating their literal effects.

### Theorem 6.1 (independently replayed provider arc)

Packet 584 uses cuts \((12635,18172,19557)\), removes

\[
\{38714,71482\},\quad\{13118,14138\},\quad\{70459,78650\},
\]

and adds

\[
\{14138,38714\},\quad\{13118,78650\},\quad\{70459,71482\}.
\]

The moved endpoints form the directed triangle

\[
             71482\longrightarrow14138\longrightarrow78650
                    \longrightarrow71482.                         \tag{6.3}
\]

Literal replay gives

\[
(h_{10},h_{11},h_{12})=(1585,824,116)\longmapsto(1582,822,117), \tag{6.4}
\]

with the exact target transport (0.3).  All quantities

\[
(\text{empty},\text{replay},\text{missing},D2,D3,
  \text{host},\text{envelope volume},\min\text{ envelope})
\]

remain

\[
                   (0,748,776,503,503,252803,150224,6).            \tag{6.5}
\]

Consequently (0.4) holds; with unit literal weights the truncated potential
drops by 4.

#### Proof

The independent checker reconstructs the packet from the binary catalogue,
replays both 24,310-owner cycles, checks the three removed and three added
edges, owner balance, one-cycle topology, exact lower-colour multiset, the
literal marked prefix, strict runs, envelopes, inverse replay, and all upper
interval unions in ranks 10--12.  It then differences the literal upper
sets and checks membership in \(Z_{177}\).  The resulting audit has SHA-256

```text
641cf08a1557e11f8a5792ace7362beefd1f11085f0f9ebb745180c8d3dbccb0
```

and payload SHA-256
`18956dd3879040a37a56ca9955dff3273dc99eed757f3e3344d8d682a318a7c8`.
Equation (6.2) now gives (0.4). \(\square\)

Across the full P3 bank, exact evaluation finds 2,067 packets which do not
worsen the recorded empty/replay/missing/D2/D3/minimum-envelope thresholds;
181 of them improve rank ten.  Requiring in addition host redundancy and
envelope volume not to decrease leaves 1,882 packets, of which 165 improve
rank ten.  These are exact finite census statements, but the two envelope
quantities are not a common-cap proof.

## 7. Exact guarded-Rado/cost-to-go interpretation

For a declared packet atlas \(\mathcal P\), a correct accepting-state graph
has vertices

\[
 s=(\text{owner/lower factor},\text{run monoid},
    \text{literal upper loads},\text{protected tickets},
    \text{topology},\text{common guard}),                          \tag{7.1}
\]

and a directed edge \(s\to s'\) only after literal replay of a compatible
closed compound.  If its physical action cost is \(a(s,s')\) and \(V\) is
physical cost-to-go, then

\[
             V(s)\le a(s,s')+V(s').                               \tag{7.2}
\]

Writing \(\widetilde V=V-\Phi_w\), the exact reduced action cost is

\[
  a_{\Phi}(s,s')=a(s,s')+\Phi_w(s')-\Phi_w(s)
                =a(s,s')+\Delta_P\Phi_w,                          \tag{7.3}
\]

and \(\widetilde V(s)\le a_{\Phi}(s,s')+\widetilde V(s')\).
Thus (6.2) is the signed projected-potential difference, not the
common-guard or future-provider part of the physical cost-to-go.  Packet
584 is a negative projected-potential arc; the present upstream-invalid
state does not make it an edge of a common-cap accepting graph.

The one-credit Rado graph in Section 5 is exact only for a serializable
subbank in which each selected packet is charged to one target and all
packet conflicts are represented by the guard matroid.  It cannot encode
the six-target/three-packet hyperservice in (5.1).  The physically faithful
next object is therefore either

1. a conflict-aware hyperpacket/flow formulation which retains every gain
   and loss of a selected packet; or
2. a proved serializable unit-service subbank with an exact gammoid or
   matroid guard.

For a dimension-uniform \(B(k)+O(1)\) theorem, these finite arcs must form a
regenerative family with bounded terminal literal charge and a uniform
contraction

\[
       \Phi_{k+2}\le \rho\Phi_k+C,\qquad \rho<1.                  \tag{7.4}
\]

This implication additionally requires a base physical construction of
length \(B(k)+O(1)\), zero hard replay/inversion debt, an exact terminal
common cap, protected deeper witnesses, and uniformly bounded literal
casualties and physical overhead.  Under those hypotheses (7.4) gives the
bounded terminal charge needed for \(B(k)+O(1)\).  The present P3 packet
proves nonzero provider mobility and one negative truncated-potential arc.
It proves neither a compatible covering bank nor (7.4).

## 8. Sharp remaining boundary

The following are proved:

* the full old 473-cut survives arbitrary-length pure residual-\(U\)
  circuits on the fixed occurrence base;
* P1 and P2 are empty, while support-two P3 is the first nonempty balanced
  packet layer;
* the unguarded frozen P3 atomic service projection has exact empty sets
  \(Z_{123}\) globally and \(Z_{26}\) on the old target bank, both of which
  remain lower bounds after guard pruning;
* packet 584 is a literal signed provider move preserving the recorded
  scalar carrier/shadow counts through rank 12, but it is **not** common-cap
  guarded and ranks 13+ protected witnesses were not audited; its derivative
  is (0.4).

The following remain unproved and are not implied:

* deletion-stable service after sequential packet regeneration;
* compatible simultaneous selection of enough P3 packets;
* exclusion of nonlinear service created only by a multi-packet compound;
* service of \(Z_{123}\) by support-four P3, P4, or longer packets;
* exact common-cap feasibility (currently fail-closed upstream);
* repair of the 503 D2/D3 and 776 replay-bit obligations;
* an accepting K17 word or an all-\(k\) regenerative contraction.

The next exact catalogue should price support-four P3 and balanced P4
columns against the 123 empty rows and the signed rank-11/rank-12 transport,
then regenerate effects after each compatible compound.  A matching rank on
the frozen one-credit projection is insufficient.

## 9. Frozen packet artifacts

| artifact | SHA-256 |
|---|---|
| P2 binary | `99f95d27849a324a4cbeb29d789f0cc6a776d830a763319211a72f1d4a22643b` |
| P2 metadata | `1d35eea0f8607c50020308841e4cb1e01d9811f117992af5a5c0c627733391d2` |
| P3 support-two binary | `adf7bf83cdcfea5ea308decf1ca1b0ec7eefa466736261dbff8ce974c1cf132e` |
| P3 metadata | `2a07e8d11aa9e9aadf5696e8173658ade4bc89d68f8c0fa3735ae6595dd3fcf9` |
| P2/P3 independent audit | `de1e812ce472954a9875b787ecec00dc6117af77a3dca02aeeb4804c2098ff2e` |
| exact packet evaluator result | `39cd6be297803a0ecfbbdcac4903413f952d8288f45531c4a3660f32e43ce7fc` |
| packet-584 owner cycle | `c522020c4f7cdee2719d654b6d6b9a0c9228fd80f27d877102997c0db0e3ab30` |
| packet-584 independent audit | `641cf08a1557e11f8a5792ace7362beefd1f11085f0f9ebb745180c8d3dbccb0` |

# Independent K17 hinge-balance and first-enrichment audit

**Date:** 2026-08-02  
**Status:** independently replayed exact finite obstruction, with two scoped
enrichment censuses.  This note does not assert chronology, residence, an
upper deck, a compiler, or a word.

## 1. Verdict

The reported `1/24310` **compatibility matching** is real for the fixed K17
depth-three chain table and the canonical payload-transparent hinge
convention.  It is not a
51-bit packing error, a head/tail reversal, or a duplicate-state artefact.
An independently written sort-join enumerator obtains

\[
  734904\text{ distinct head states},\qquad
  6223360\text{ raw tail options},
\]

but only one head--tail state equality.  Consequently only one head role and
one tail role have support, and the exact role-projection matching number is
one.

There are two producer-reporting defects, neither affecting the numeric
obstruction.

1. The frozen remote JSON says
   `PASS_K17_HINGE_RECTANGLE_BALANCE_MAXFLOW` even though `matched<W`.  The
   status is wrong; the numeric fields are the authority.  The corrected
   local source emits `NO_K17_HINGE_RECTANGLE_BALANCE_MAXFLOW` when
   deficient.
2. The field `maximum_balanced_roles=1` is misnamed.  Dinic finds one edge in
   the bipartite graph from head-role copies to tail-role copies.  That edge
   joins two different roles.  It is therefore one compatible pair, not a
   balanced one-role trace set.  The compatibility digraph has no directed
   cycle, so the largest nonempty balanced role subcollection is actually
   empty.  The value `selected_trace_rows=0` exposes this distinction; its
   writer is not a decoder for a general head-role--tail-role matching.

The maximum matching value one is nevertheless more than enough to refute
a full `24310`-role balance.

Neither of the following changes the obstruction:

1. allowing every singleton filler for every length-one chain; or
2. replacing the canonical hinge by the complete right-aligned unsaturated
   one-sided family, including every legal `(x,y,A)` choice.

Both still have exactly one compatible state and projection matching one.

A genuinely different enrichment does create new support.  Splitting the
old last layer as an ordered nonempty cover

\[
                         B_2\cup B_3=S_1
\]

while preserving the original marked suffix widths yields 2,454 compatible
states and projection matching 888.  Thus filler/guard freedom is inert on
this table; changing an actual overlap-state letter is the first tested
effective escape.  The number 888 is only a projection upper bound, because
the chosen `B_2` must be shared by the tail and head of the same physical
role arc.

## 2. Independently reconstructed equations

Let a role have rank-nine owner `T`, rank-eight root `U`, and nested chain

\[
  S_1\subsetneq\cdots\subsetneq S_\ell=U,
  \qquad 1\leq\ell\leq3.
\]

For the canonical literal hinge put

\[
 (P,Q)=
 \begin{cases}
 (\{\min S_1\},S_1),&\ell=1,\\
 (U\setminus S_1,S_1),&\ell=2,\\
 (U\setminus S_2,S_2\setminus S_1),&\ell=3.
 \end{cases}
\]

The complete head and tail menus are then

\[
 \begin{array}{c|c|c}
 &\text{head}&\text{tail}\\ \hline
 \ell\leq2&(P,Q,L),\quad\varnothing\ne L\subseteq S_1
     &((T\setminus U)\cup A,P,Q),\quad A\subseteq U,\\
 \ell=3&(P,Q,S_1)
     &((T\setminus U)\cup A,P,Q),\quad A\subseteq U.
 \end{array}                                             \tag{2.1}
\]

These are literal ordered triples, not their unions.  The independent audit
compares the three coordinates in (2.1) directly and builds the resulting
bipartite graph from head roles to tail roles.  It uses sorting, exact equal
ranges, and an independent Hopcroft--Karp implementation; it does not reuse
the producer's hash map or Dinic implementation.

For the right-aligned unsaturated class the audit separately reconstructs
the theorem's four letters.  For `ell<3`, it enumerates all

\[
 x\in T,\quad y\in S_1,\quad x\ne y,\quad
 S_\ell\cup\{x\}\ne T,quad A\subseteq S_1-\{y\},       \tag{2.2}
\]

uses `B_0=(T-S_ell) union A`, repeats `{x}` through positions
`1,...,3-ell`, and puts the chain differences in the rightmost positions.
For `ell=3`, it enumerates every `y in S_1` and every
`A subseteq S_1-{y}`.  Every generated word is replayed for nonempty letters,
owner `T`, and every declared suffix target before its endpoint states are
accepted.

The slot-preserving split class keeps the old target widths.  For
`ell<3`, it replaces the saturated last layer by every ordered pair of
nonempty sets `(B_2,B_3)` satisfying `B_2 union B_3=S_1`; the earlier spine
letter and `B_0` remain canonical.  Length-three roles retain their forced
chain-difference spine.

## 3. Exact census

| mode | distinct heads | tail options | compatible states | supported head/tail roles | maximum projection matching |
|---|---:|---:|---:|---:|---:|
| canonical least filler | 734,904 | 6,223,360 | 1 | 1 / 1 | 1 |
| all singleton fillers on length-one roles | 3,855,084 | 6,223,360 | 1 | 1 / 1 | 1 |
| right-aligned unsaturated, one canonical `(x,y)` | 24,310 | 791,073 | 1 | 1 / 1 | 1 |
| right-aligned unsaturated, all `(x,y,A)` | 63,839 | 6,534,183 | 1 | 1 / 1 | 1 |
| slot-preserving split last layer | 15,082,360 | 188,135,424 | 2,454 | 1,450 / 955 | 888 |

The exhaustive unsaturated run visits 21,004,849 raw `(x,y,A)` choices;
deduplication leaves 6,534,183 role-labelled physical arcs.  All 63,839
head states are distinct.  Thus its one-edge result cannot be explained by
accidental duplicate collapse.

The slot-split table has no nonfull role with singleton `S_1`.  Its 2,454
compatibilities are all distinct as `(head role,tail role,state)` triples.

## 4. Structural no-go and the exact unique edge

Every canonical head in (2.1) has union `U` and hence rank eight.  For
`ell=1,2`, every canonical tail contains `(T-U)`, while its two fixed spine
letters already union to `U`.  Thus every such tail has union `T` and rank
nine.  No short-role tail can equal any head, independently of the chosen
length-one filler or optional first-letter subset.

For full chains write

\[
 L\subset M\subset U,\qquad |M|=7, |U|=8,qquad
 T=U\cup\{z\}.
\]

The head and tail are

\[
 (U-M,M-L,L),\qquad (\{z\}\cup A,U-M,M-L).           \tag{4.1}
\]

If a head role `i` equals a tail role `j`, coordinate equality in (4.1)
forces `A_j=emptyset`, bottom rank six at the head, and bottom rank one at
the tail.  More explicitly, for a tail flag

\[
 \{x\}=L_j\subset M_j\subset U_j,qquad T_j=U_j\cup\{z_j\},
\]

the only possible head flag is

\[
 M_j-\{x\}\ \subset\ U_j-\{x\}\ \subset\
 (U_j-\{x\})\cup\{z_j\}.                              \tag{4.2}
\]

The frozen table has only 17 bottom-rank-one full chains.  Checking the 17
forced flags (4.2), rather than searching all 6,223,360 tails, leaves the
single compatibility below.

### 4.1 The unique canonical compatibility

The sole equality is

\[
 (512,8192,2405).
\]

It joins

* head role 1783, owner 27493, chain
  `(2405,10597,11109)`; and
* tail role 2623, owner 15205, chain
  `(4096,6501,14693)`.

Indeed

\[
 11109\mathbin\triangle10597=512,qquad
 10597\mathbin\triangle2405=8192,
\]

while for the tail role the empty optional set gives

\[
 15205\mathbin\triangle14693=512,quad
 14693\mathbin\triangle6501=8192,quad
 6501\mathbin\triangle4096=2405.
\]

There is no reverse or self edge.  The same equality is the sole survivor
in both unsaturated censuses.  This is a predecessor compatibility, not by
itself a selected physical trace: a complete circulation would still have
to choose correlated incoming and outgoing endpoints for every role.

### 4.2 The old hinge fails every K17 three-slot chainization

The preceding rank argument is not peculiar to the frozen Dilworth table.
For any partition of the `65,535` targets into `24,310` chains of lengths at
most three, let `n_j` count length-`j` chains.  Its empty-slot count is

\[
 2n_1+n_2=3(24310)-65535=7395.                         \tag{4.3}
\]

Consequently

\[
                         n_1+n_2\ge\lceil7395/2\rceil=3698. \tag{4.4}
\]

All these short-role tails are rank nine under the old hinge, while all
heads are rank eight.  Hence no old-hinge table on these compressed levels
can have a perfect state balance.  The least-bit filler convention is
irrelevant to this general no-go.

### 4.3 Positive-density lower bound for repairing the frozen table

Suppose arbitrary new head/tail menus are allowed on only `q` of the frozen
roles.  Every edge of a perfect matching except the one old compatibility
must touch either a modified head copy or a modified tail copy.  A matching
uses each of those `2q` shore vertices at most once, so

\[
                    24310\le 2q+1,qquad q\ge12155.     \tag{4.5}
\]

Thus no bounded correction bank repairs this fixed table.  Since there are
only 5,647 short roles, modifying all of them still leaves a requirement to
enrich at least 6,508 full-chain roles (or replace the table itself).

## 5. Scope and next state class

The exact numeric `1/24310` result is confined to the given table.  The
rank-eight/rank-nine short-role obstruction, however, applies to every K17
three-slot chainization using the old hinge.  Neither result is a no-go for
all payload-transparent gadgets.

The exhaustive comparisons prove a useful local distinction:

* changing only the filler singleton, missing guard, or first-letter subset
  cannot repair this table; but
* allowing an ordered cover of `S_1` across the two last letters changes the
  overlap state and produces a nontrivial predecessor graph.

Therefore any next candidate on this fixed table must at least alter an
internal overlap letter (or replace the chain allocation itself).  The
slot-preserving ordered-cover class is the smallest tested such enrichment,
not a claim of absolute minimality among every possible Boolean gadget.  Its
matching value 888 is far below 24,310 and ignores the same-role
head/tail-choice correlation, so it does not close chronology or state
balance.

The smallest proof-safe **global class capable of escaping all proved
cuts** must add a second operation on a positive-density set of full-chain
roles.  One literal choice is the split--reinsertion family.  With
`A subseteq U`, `B_0={z} union A`, and `x in U`, it uses

\[
\begin{array}{ll}
 \ell=1:&(B_0,\{x\},V_0,V_1),
          \quad V_0,V_1\ne\varnothing,quad V_0\cup V_1=U,\\
 \ell=2:&(B_0,U-S,V_0,V_1),
          \quad V_0,V_1\ne\varnothing,quad V_0\cup V_1=S,\\
 \ell=3:&(B_0,(U-M)\cup R,M-L,L),
          \quad R\subseteq M.
\end{array}                                             \tag{5.1}
\]

The first two rows preserve the original marked suffix widths while
splitting their last marked layer.  The third retains the full payload but
re-inserts already covered coordinates into the first head letter, breaking
the rigid rank rotation in (4.1).  For fixed `(V_0,V_1)` or `R`, variation
of `A` is a genuine Cartesian role rectangle.  The union over such
factorizations is **not** itself one Cartesian product: a correct selector
must first choose a rectangle and then choose its tail.  Projecting all
tails and heads independently would admit false cross-factorization arcs.

Equation (4.5) requires this enrichment on at least 12,155 roles of the
frozen table.  Existence of a perfect correlated selection in (5.1) is the
new exact predecessor-Hall/functional-flow gate; it is not proved here.
Unmarked lower outputs, chronology, residence, upper decks, common cap and
compiler remain separate filters.

## 6. Frozen artifacts

Input table:

* `scratch/k17_exact_depth3_owner_payload_table_20260802/k17_depth3_owner_payload.tsv`
* SHA-256 `029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1`

Independent bundle:

* `scratch/k17_hinge_rectangle_enrichment_independent_20260802/audit_k17_hinge_balance_independent_20260802.cpp`
  — `c2cc49104c5b38ab437044acc9e39c2643ef06eacb754a949270128807827bb4`
* `scratch/k17_hinge_rectangle_enrichment_independent_20260802/independent.audit.json`
  — `81ac2cec2107cb083163a02811860df1421c96e27bbcb96770c8b81c09f79a7d`
* `scratch/k17_hinge_rectangle_enrichment_independent_20260802/compatibility_witnesses.tsv`
  — `f7bf8f167841f3d95b64cb67ce3757910890ccd4e9a1651726562779704d9fef`
* `scratch/k17_hinge_rectangle_enrichment_independent_20260802/run.out`
  — `3e95c2113c0b54609499594cf7654c8ac666cdcdffb0b7d075258ec22f68a09d`
* `scratch/k17_hinge_rectangle_enrichment_independent_20260802/run.err`
  — `1bd6e7d474d79143a4f17b586f749ba4770ce8d73603c1c53b4bc8e477dac31a`

The O3 audit ran on one H100 CPU core.  Maximum resident memory was 242,476
KiB; wall time was 20.54 seconds.  The persistent remote root is
`/home/amodo/or15/work/k_hinge_balance_independent_20260802`.

Original producer artifacts:

* remote source SHA-256
  `f571c530d588cffa50437aa8185b99d75054be7ee237fb405bb98db41898cc1a`;
* remote binary SHA-256
  `c8c2d1cc31b09cbba18b43d11cade3006bed5d94554a5fd313b93480424a5b88`;
* frozen, incorrectly labelled remote audit JSON SHA-256
  `70a7af9cb89a6b513b20f068b0315db83b87cc7292bef5d50c5c3aa419932f42`;
* corrected local producer source
  `scratch/solve_k17_hinge_rectangle_balance_20260802.cpp`, SHA-256
  `c00bec5bbf2aa167b9282d91d06ad6a2bb177310af390b08cf29bc5b42c96180`.

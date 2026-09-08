# Independent Hall/DM audit of the detached-7 pass-1 K16 chronology

Date: 2026-07-30  
Lane: AD, fixed-chronology common-compiler obstruction  
Status: **proved finite theorem; no compiler or literal word claimed**

## 1. Frozen input and independent replay

The input is

`scratch/root_k16_a_bad2_detached_cycles_20260730/out7/pass_1.targets`

with SHA-256

`aea7a05a8837298205e9f35f39c7e6b99b8e7ef00fe46dcab9a8ab831e018e34`.

The independent standard-library replay is

`scratch/ad_k16_detached7_pass1_hall_dm_20260730/audit_pass1_hall_dm.py`

with SHA-256

`b23ae9b1fc9ab4e94d12af9c16b04ec5f8f6c78c395e248052e5a0b78ecf2842`.

It does not import the compiler or Hall-audit modules used to make the
original result.  It reconstructs their mathematics directly.  The exact run
used one H100 CPU for 2.03 seconds and 51,188 KiB peak RSS.  No CP, SAT, or
third-party library was used.

The independent replay agrees field-for-field on the incidences, maximum
matching, unmatched targets, canonical alternating left shore, and its full
right neighbourhood with the original `hall_1.json`, whose SHA-256 is

`d231de3e8ebc8073ee4e2a00ec71ff90084786cbe587a1f429c05f915ce69a2e`.

## 2. Exact graph semantics

Let (T_0,\ldots,T_{12872}) be the frozen rank-eight chronology.  Start with
depth (d_i=3); after each adjacent equality (T_i=T_{i+1}), decrease all
subsequent depths by one.  The three equality starts are

\[
6320,\qquad12869,\qquad12871.
\]

Thus the depth histogram is

\[
\#\{d_i=3\}=6321,\quad
\#\{d_i=2\}=6549,\quad
\#\{d_i=1\}=2,\quad
\#\{d_i=0\}=1.
\]

For each source position (p), define its maximal envelope

\[
P_p=\bigcap_{i:\ i\le p\le i+d_i}T_i.
\]

Every (P_p) is nonempty, and

\[
\bigcup_{p=i}^{i+d_i}P_p=T_i
\]

for every row (i).  A right vertex is a proper-prefix cell

\[
J=(s,\ell),\qquad1\le\ell\le d_s,
\]

representing the source interval ([s,s+\ell)).  Put

\[
E_J=\bigcup_{p\in J}P_p.
\]

For a row bit (b\in T_i), its carrier is

\[
C(i,b)=\{p\in[i,i+d_i]:b\in P_p\}.
\]

The forced set of a cell is

\[
M_J=\{b:\text{ for some }i, b\in T_i\text{ and }C(i,b)\subseteq J\}.
\]

The left vertices are all 26,332 nonempty masks (S\subseteq[16]) of ranks
one through seven.  The exact edge law is

\[
S\sim J
\quad\Longleftrightarrow\quad
S\subseteq E_J,\quad M_J\subseteq S,
\quad S\cap P_p\ne\varnothing\ \text{for every }p\in J.
\tag{2.1}
\]

### Lemma 2.1 (exact one-cell feasibility)

For a fixed cell (J), condition (2.1) holds if and only if there is a
nonempty source-letter assignment (A_p\subseteq P_p) satisfying every
middle-row equation

\[
\bigcup_{p=i}^{i+d_i}A_p=T_i
\]

and also satisfying

\[
\bigcup_{p\in J}A_p=S.
\]

#### Proof

Necessity is immediate.  The cell union is contained in (E_J); nonempty
letters force (S\cap P_p\ne\varnothing); and when an entire bit carrier
(C(i,b)) lies inside (J), row (i) can receive (b) only if (b\in S).

Conversely set

\[
A_p=P_p\cap S\quad(p\in J),qquad A_p=P_p\quad(p\notin J).
\]

All letters in (J) are nonempty by (2.1), and the other envelopes are
already nonempty.  Their union over (J) is exactly (S): containment follows
from intersection with (S), while each bit of (S\subseteq E_J) appears in
some (P_p\), (p\in J).  Fix a required row bit (b\in T_i).  If
(C(i,b)\not\subseteq J), a carrier position outside (J) keeps (b).  If
(C(i,b)\subseteq J), then (b\in M_J\subseteq S), so a carrier position in
(J) keeps it.  No row receives an extraneous bit because every active
envelope is contained in that row.  Hence all row equations hold.  ∎

This lemma is deliberately one-cell-at-a-time.  It does **not** say that
assignments for different matched cells coexist in one source word.

## 3. Exact Hall theorem

### Theorem 3.1

For the graph in Section 2:

* the number of right cells is 32,063;
* the number of incidences is 347,809;
* the maximum matching cardinality is exactly 26,298;
* therefore the Hall deficiency is exactly 34.

The deterministic Hopcroft--Karp matching leaves these 34 left vertices
unmatched:

```
05ce 1665 22cd 2665 27a4 28e9 29a9 4339 4371 4372 4378
4879 48e9 4e70 5439 5670 583c 5a1c 5a29 5c70 6989 6a29
6a38 6a70 6b21 6c70 6cb0 72e0 7c30 8000 8cd8 a1a9 d268 d342
```

Their rank histogram is one rank-one mask and 33 rank-seven masks.

#### Proof

The matching file

`scratch/ad_k16_detached7_pass1_hall_dm_20260730/pass1_hall_dm.matching.tsv`

contains 26,298 pairwise-disjoint incidences and has SHA-256

`5119eec8c704fdb8e0b20160e57d226422755ca75f52fa6bf1a917cfd5db4e5d`.

Starting from its unmatched left vertices, traverse nonmatching edges from
left to right and matching edges from right to left.  The resulting canonical
alternating shore has

\[
|X|=249,\qquad |N(X)|=215.
\]

The replay checks directly that the enumerated right set is the **full**
neighbourhood of (X).  Thus every matching misses at least
(249-215=34) left vertices.  The displayed matching misses exactly 34, so
both bounds are tight.  ∎

The left-shore rank histogram is

\[
1:1,\qquad5:7,\qquad6:50,\qquad7:191.
\]

All 249 masks, all 215 cell identifiers, and every neighbour cell's start,
length, allowed mask, and mandatory mask are recorded explicitly in

`scratch/ad_k16_detached7_pass1_hall_dm_20260730/pass1_hall_dm.audit.json`.

Its file SHA-256 is

`28f6d9ada312d8fe2e033003f2b0289f2663e4138a894239b885c23b7bbbffe3`,

and its internal stable payload SHA-256 is

`efffa1ee3349b107177c5ee8efbfc732ca833a30c1b9c86a4032a4132c38643a`.

## 4. Zero-degree targets and DM components

Exactly 19 targets have no candidate cell:

```
2665 28e9 29a9 4339 4378 4879 48e9 4e70 5439 5670
583c 5c70 6989 6a29 6a38 6a70 6b21 6c70 8000
```

Here `8000` has rank one; the other 18 have rank seven.  Each is a singleton
DM component of size (1/0).

The induced undirected incidence graph on (X\cup N(X)) has 33 components.
There are 19 singleton (1/0) components.  The 14 nontrivial components are:

| component | left/right | gap | unmatched root(s) |
|---:|---:|---:|---|
| 0 | 15/14 | 1 | `22cd` |
| 1 | 34/33 | 1 | `05ce` |
| 2 | 35/34 | 1 | `8cd8` |
| 3 | 18/17 | 1 | `27a4` |
| 4 | 7/6 | 1 | `1665` |
| 5 | 3/2 | 1 | `a1a9` |
| 9 | 44/43 | 1 | `72e0` |
| 10 | 21/20 | 1 | `d268` |
| 11 | 10/8 | 2 | `4371`, `4372` |
| 16 | 4/3 | 1 | `5a29` |
| 18 | 23/22 | 1 | `d342` |
| 21 | 7/6 | 1 | `5a1c` |
| 23 | 5/4 | 1 | `7c30` |
| 30 | 4/3 | 1 | `6cb0` |

Thus 32 components have gap one, and the unique gap-two component is the
(10/8) component rooted at `4371`, `4372`.

## 5. Consequence for the loss-robust collar catalogue

The three advertised Hall roles of a loss-robust collar all lie in this
explicit shore:

* `8000` is a zero-degree singleton (1/0) component;
* `2665` is a zero-degree singleton (1/0) component;
* `0665` lies in the (7/6) component

  ```
  {0665,066d,0675,06e5,0765,1665,8665}.
  ```

Therefore a globally legal, middle/upper-preserving collar embedding that
creates three **new** distinct right cells serving `8000`, `2665`, and `0665`
would enlarge the present neighbourhood (N(X)) by as many as three and
directly attack three units of the certified gap.

This is only a necessary screening result.  The local catalogue alone does
not prove that its cells survive global embedding, are new relative to the
215 recorded cells, or preserve all other neighbours.  No collar is accepted
without those three checks.

## 6. Scope boundary

The chronology itself has all 12,870 rank-eight owners, with exactly the
three repeated owners `4e71`, `cc63`, `ce61`, and its interval unions have no
upper-rank hole.  Those facts authenticate the intended exact-middle and
upper-complete fixed schedule.

Theorem 3.1 is nevertheless an obstruction theorem only.  It proves that the
frozen chronology cannot assign distinct proper-prefix occurrence cells to
all lower targets.  It does not construct source letters, does not settle a
modified chronology, and does not establish a literal length-12,873 OR word.

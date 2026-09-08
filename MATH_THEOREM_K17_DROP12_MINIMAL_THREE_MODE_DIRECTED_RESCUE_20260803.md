# K17 drop-12 minimal three-mode directed-rescue theorem

**Date:** 2026-08-03

**Status:** exact theorem and checker specification on the canonical consumer
face.  An authenticated lossless phasewise upper reduces the 94-anchored
three-mode domain to 70 rows, and a separate complete-menu verifier proves
that all 70 are occurrence-negative.  This closes the single-helper/94-
anchored three-mode branch, but not the irreducible bilateral-source branch.

## 1. Authoritative face and evidence

All notation and claims below are relative to the canonical consumer parent

```text
compressed  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
final       fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
catalogue   790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
```

and the following exact pair package:

```text
complete pair audit JSON       b23ba07aa0e4ff6e155ec0f3ccbe865d341937d6cb409fb5bb63b677d4010741
combined manifest              d30257cac313ea497cbc52979616118092b1e7ce41b3ebc9d37ea02ade23dfe0
recorded manifest check        259c42a25566dad53f448fa102751a50c513e5394ce524ea11eaa2cc3548b120
94-row directed upper ledger   3f61ed962dcdca21cb3a3412f89a9ec9de27c594e7358e7921bc7d2727ad31e5
94-row exact menu ledger       f33f6ed5a7102ee3cc63a260a0608685a6776586c8014015ad8df56c0c4421c5
exact-menu audit               1e9a44d5336ff436e8b08c3fe8d28c2a2426430f150a5c7a335c5d69b50c92b4
```

The exact package proves that the complete directed face consisting of one
of the 468 supplier-rank-16,878 source modes and one of the 112,621
fixed-bank-safe structural partners is occurrence-empty.  Its domain has
52,664,349 endpoint-disjoint directed incidences.  The upper leaves 94
ordered pairs, and the complete pair verifier finds zero compatible option
edges on all 94.

For every one of the 94 pairs, the source has exactly one native-phase-0
tuple, one transported-phase-1 tuple, and one cross-phase source anchor.  The
partner has zero phase-0 tuples.  Its phase-1 menu-size distribution is

```text
70 pairs: 0 tuples
17 pairs: 1 tuple
 7 pairs: 2 tuples.
```

The authoritative three-mode phasewise upper is:

```text
upper source    31947fe3f1934a9826156bbd7d17034d5aced8361fc85b0add192516a2fa51c4
upper ledger    762c65a41176dcea9517a52f4213f2faea3bcf69a879d90089ef89412f1cd0e3
upper audit     46ce798aa266b7d5653cacb55f1a401c6bc64fd5933d9a155d92bb7d6986e24d
```

It scans 10,536,324 six-endpoint-disjoint directed extensions of the 94
pairs and leaves 70 phasewise necessary survivors.  Those 70 form seven
source/partner requests crossed with ten third modes.  All seven use partner
edge 39089, all ten third modes have host row 3362, and every emitted partner
phase-0 tuple has declared key 70.  These observations are a census of the
upper ledger, not a complete occurrence certificate.

The separate exact 70-row replay is bound by

```text
exact checker source  b4e6af16dc5e5ad4452776bbaf623fb0563bc89cefb5fe10d1a8a0910f8780a2
exact checker binary  fc73d84a05e5aeda71d209ae083ef6aba23ebc5ada8f31fc08eb62dcf7ee839f
exact output ledger   281b32fd6d4acb8e0c78abadbc7d85fca1bb0f89b7092eb08c6ee2d8a8a21555
exact audit JSON      b99f8b509a58a5ebb3f8c9c0fae32ab3c6452a7480308e3e0b12770a14d2135c
menu histogram        a1d919f157da5c331bf09cd4d44388e5ac9d5756ab0a17970288ba5d6e11bca4
human handoff         a0504d1f278cf022c473a07b198327868408dc2aaefb6d9ca25964fac7c440c8
```

## 2. Three-transfer long-state delta

For a transfer (x), write (h_x) for its old LR host and (d_x) for its
old LMR donor.  Simultaneous materialization changes

```text
h_x : (u_x,q_x)       -> (l_x,u_x,q_x),
d_x : (l_x,m_x,r_x)   -> (m_x,r_x).
```

Let (H_x^\phi(c)) denote the flag-(c) long state created at (h_x) in
owner phase (\phi\), and let \({\cal L}_0^\phi\) be the exact fixed-final
long-state bank after the global private-row rule and phase-specific
incumbent reservations have been applied.  For three transfers (e,f,g)
with six distinct endpoints,

\[
 {\cal L}_{e,f,g}^\phi
 =
 \left({\cal L}_0^\phi\setminus\{d_e,d_f,d_g\}\right)
 \cup
 \{H_x^\phi(c):x\in\{e,f,g\},\ 0\le c<4\}.       \tag{2.1}
\]

Equation (2.1) is literal: there are exactly three long-row deletions and
three four-flag host insertions, and no other changed long state.

The eligibility rules in (2.1) are part of the theorem:

* all 7,213 private rows are unavailable in both phases;
* the twenty rows occupied by the ten incumbent tickets are reserved
  separately in each phase;
* their reservation union has 23 rows, with 17 shared by the phases;
* a row reserved only in the opposite phase may be used at the already fixed
  incumbent flag, but at no other flag; and
* a current incumbent LLR host remains an eligible long provider whenever it
  is not reserved in the phase at issue.  Endpoint immutability is not a
  global provider ban.

## 3. Exact tickets and options

For the new MR short of a transfer (x), a phase-(\phi) ticket is

\[
 w=(k;p,\alpha;s,\beta),\qquad k=(q,\alpha,\beta),       \tag{3.1}
\]

where the predecessor state \((p,\alpha)\) and successor state
\((s,\beta)\) belong to \({\cal L}_{e,f,g}^\phi\), and the exact incoming,
outgoing, and literal five-cell predicates all hold.  If (p=s), then
(\alpha=\beta).  Its physical phase footprint (F_\phi(w)) is the set
\(\{p,s\}\), with a repeated row counted once, and its flag map assigns
(p\mapsto\alpha) and (s\mapsto\beta).

A two-phase option is

\[
 o_x=(k,w_x^0,w_x^1),                                   \tag{3.2}
\]

with the same declared key in both phases and a single-valued union of the
two flag maps.  Let \({\cal O}_x(e,f,g)\) be the complete set of such options.
Every physical tuple for every declared key must be retained; a tuple count,
first witness, or frozen pair witness is not an exact substitute.

For an option (o), write (F_\phi(o)) for its phase footprint and
\(\gamma_o\) for its cross-phase row-to-flag map.

## 4. Exact three-option hypergraph theorem

Construct a three-partite compatibility hypergraph with parts

\[
 {\cal O}_e(e,f,g),\qquad {\cal O}_f(e,f,g),\qquad
 {\cal O}_g(e,f,g).
\]

Place a hyperedge on \((o_e,o_f,o_g)\) exactly when

\[
 \sum_{x\in\{e,f,g\}} \mathbf 1\{v\in F_\phi(o_x)\}\le1
 \quad\text{for every phase }\phi\text{ and row }v,      \tag{4.1}
\]

and

\[
 \left|\{\gamma_{o_x}(v):x\in\{e,f,g\},
                         v\in\operatorname{dom}\gamma_{o_x}\}\right|
 \le1
 \quad\text{for every row }v.                            \tag{4.2}
\]

### Theorem 4.1 (exact triple occurrence oracle)

The three transfers admit a simultaneous occurrence packing together with
the ten incumbent tickets if and only if this hypergraph has a hyperedge.

### Proof

A simultaneous packing restricts to one same-key two-phase option for each
new short.  Unit physical-row capacity in each phase gives (4.1), and the
single physical flag address across both phases and all roles gives (4.2).
The phase-specific incumbent rules were enforced when the option menus were
built.

Conversely, a hyperedge supplies six exact phase tickets.  Equation (4.1)
packs them with unit phase capacity; (4.2) makes every shared cross-phase row
have one flag; and the option definition supplies the exact local predicates
and phase-reservation compatibility.  Hence the six tickets and the ten
fixed incumbent tickets form a simultaneous packing.  \(\square\)

Pairwise compatibility is sufficient here because both global constraints
are pairwise: same-phase row intersection is forbidden and a shared
cross-phase row must have equal flags.  An implementation may therefore seek
a triangle in the three-partite pair-compatibility graph, but it must not
replace complete option vertices by marginal state counts.

## 5. Exact minimality of the open cardinality

The corrected unary replay proves that every one of the 468 supplier sources
is common-occurrence empty in its one-transfer child under the same
phase-specific provider rules.  The complete 52,664,349-incidence pair
package proves that every endpoint-disjoint two-transfer child containing
one of those sources is occurrence-empty.

Therefore any occurrence-valid fixed-presentation child containing an
authenticated supplier-improving source requires at least three new
transfers:

\[
 \boxed{|T|\ge3.}                                        \tag{5.1}
\]

This is a lower bound, not an existence statement.  Cardinality three is the
first open layer until Theorem 4.1 is evaluated on an exact triple domain.

## 6. Directed phase-0 rescue lemma

Fix one of the 94 ordered pairs \((e,f)\).  Its complete pair-child phase-0
menu for the partner short (f) is empty.  For a third transfer (g), let
\({\cal W}_{f,\phi}^{ef}(k)\) be the exact phase-(\phi) ticket menu in
the pair child and let
\({\cal W}_{f,\phi}^{efg}(k)\) be the exact phase-(\phi) ticket menu in the
triple child.  Split it as

\[
\begin{aligned}
 {\cal S}_{f,\phi}^{ef}(k;g)
   &=\{w\in {\cal W}_{f,\phi}^{ef}(k):d_g\notin F_\phi(w)\},\\
 {\cal G}_{f,\phi}^{g}(k)
   &=\{w\in {\cal W}_{f,\phi}^{efg}(k):h_g\in F_\phi(w)\}.
\end{aligned}                                             \tag{6.1}
\]

Then

\[
 {\cal W}_{f,\phi}^{efg}(k)
 = {\cal S}_{f,\phi}^{ef}(k;g)
   \mathbin{\dot\cup}{\cal G}_{f,\phi}^{g}(k).           \tag{6.2}
\]

Indeed, adding (g) to the pair child only deletes (d_g) and inserts
(h_g).  A triple ticket not using (h_g) is exactly a pair ticket that
survives the deletion.  Since the pair phase-0 menu is empty,

\[
 \boxed{{\cal W}_{f,0}^{efg}(k)={\cal G}_{f,0}^{g}(k).}   \tag{6.3}
\]

Thus every triple phase-0 ticket for (f) must use (h_g) as predecessor,
successor, or both.  For the 70 pairs whose partner phase-1 menu is also
empty, the same conclusion holds in phase 1.

This is the exact directed-rescue invariant.  Deleting a donor cannot create
a ticket; the third host is the only possible creator.

## 7. Preserving a pair source option

Let \(\bar o_e=(\bar k_e,\bar w_e^0,\bar w_e^1)\) be a pair source anchor.
It survives addition of (g) if and only if

\[
 d_g\notin F_0(\bar o_e)\cup F_1(\bar o_e).              \tag{7.1}
\]

No other row state used by the anchor changes.  Endpoint disjointness alone
does not imply (7.1), because a source ticket may use an unchanged base long
row that is the third donor.

For a surviving anchor, define the exact partner-repair set

\[
 {\cal R}_{ef}(g;\bar o_e)
 =\bigcup_k
 {\cal G}_{f,0}^{g}(k)
 \bowtie_{\bar o_e}
 \left({\cal S}_{f,1}^{ef}(k;g)
       \cup {\cal G}_{f,1}^{g}(k)\right),                \tag{7.2}
\]

where \(\bowtie_{\bar o_e}\) requires:

1. the same declared key in phases 0 and 1;
2. a single-valued partner cross-phase flag map;
3. disjoint partner/source footprints in each phase; and
4. equality of flags on every row shared across phases or roles.

Then

\[
 (7.1)\ \text{and}\ {\cal R}_{ef}(g;\bar o_e)\ne\varnothing             \tag{7.3}
\]

is necessary and sufficient for (e), using this fixed anchor, and (f) to
have compatible two-phase options in the triple child.  It says nothing yet
about occurrence of the third short (g).

The exact 94-row output freezes counts for the nonempty partner phase-1
menus, but not their ticket keys, rows, and flags: its partner witness fields
are `-1` because no pair has an overall positive option edge.  Therefore an
exact triple implementation must rebuild each complete partner phase-1 menu;
it cannot select a tuple from the reported counts 0, 1, or 2.

## 8. Lossless 94-extension upper

Let \({\cal A}_{94}\) be the ordered 94-pair ledger and let (U) be the
112,621-mode fixed-bank-safe partner bank.  The directed extension domain is

\[
 {\cal D}_{94}^{(3)}=
 \{(e,f,g):(e,f)\in {\cal A}_{94},\ g\in U,
            |\{h_e,d_e,h_f,d_f,h_g,d_g\}|=6\}.           \tag{8.1}
\]

Its exact directed incidence count is

\[
 94\cdot112621=10,586,374\quad\longrightarrow\quad
 \boxed{|{\cal D}_{94}^{(3)}|=10,536,324}                \tag{8.2}
\]

after six-endpoint disjointness.  This is a directed anchored count; the same
unordered triple may have more than one anchor and must not be silently
deduplicated without retaining every anchor label.

The SHA-bound phasewise upper applies the following necessary conditions to
every row of (8.1):

1. build the pair contexts with (d_e,d_f) deleted and (h_e,h_f)
   inserted;
2. for some partner key (k), create a phase-0 (f)-ticket using (h_g),
   after also deleting (d_g);
3. retain or create a phase-1 (f)-ticket for the same key (k);
4. for some source key (k_e), retain or create a source ticket in each
   phase at that same key after the three deletions and insertions.

Every exact triple hyperedge extending one of the 94 pairs satisfies these
conditions, by (6.3) and by restriction of its source and partner options.
Hence rejection by this phasewise screen is lossless on
\({\cal D}_{94}^{(3)}\).  The screen leaves exactly

\[
 \boxed{70}                                               \tag{8.3}
\]

rows.

The 70-row screen deliberately does **not** enforce:

* internal cross-phase flag consistency of the chosen source and partner
  phase tuples;
* source/partner phase-capacity compatibility;
* a complete two-phase option for the third short;
* three-role capacity and flag compatibility (4.1)--(4.2);
* simultaneous table materialization; or
* a fresh complete supplier replay.

Consequently 70 is a lossless upper-domain count, not an occurrence-positive
count and not a deficiency-20 child count.  It supersedes the earlier 5,853
one-sided-aperture execution frontier.

### 8.1 Exact closure of the 70-row upper

The independent exact checker constructs the three-deletion/three-host bank
(2.1), enumerates complete physical menus for all three shorts in both phases
and all 90 keys, and applies Theorem 4.1 without imposing a frozen source-
anchor filter.  Its exact menu census is

```text
source phase-0 tuples                  1 on all 70 rows
source phase-1 tuples                  1 on all 70 rows
source two-phase options               1 on all 70 rows
source anchored / unanchored options   70 / 0 in total
partner phase-0 tuples                 1 on all 70 rows
partner phase-1 tuples                 1 on 7 rows, 2 on 63 rows
third phase-0 tuples                   0 on all 70 rows
third phase-1 tuples                   1 on 7 rows, 0 on 63 rows
occurrence-positive triples            0
```

The seven nonempty third phase-1 menus are exactly the seven rows using third
edge 8240.  Every third phase-0 menu is empty.  Hence the third option part
\({\cal O}_g(e,f,g)\) of the hypergraph is empty before any three-role
capacity or flag edge can be formed:

\[
 \boxed{{\cal O}_g(e,f,g)=\varnothing
        \quad\text{for every one of the 70 upper rows}.} \tag{8.4}
\]

Therefore the exact replay proves

\[
 \boxed{\text{no occurrence-valid triple exists in }
        {\cal D}_{94}^{(3)}.}                            \tag{8.5}
\]

The obstruction is earlier than joint packing: the third transfer creates
the partner's missing phase-0 ticket but cannot authenticate its own native-
phase-0 short.  The supplier-replay queue is therefore empty.  Equation
(8.5) uses the losslessness of the 70-row upper plus the exact zero on all 70;
it is not inferred from the upper alone.

## 9. Structural no-go invariants

Several exact no-go tests follow before supplier replay.

### 9.1 Forced ownership of the third host

By (6.3), every partner phase-0 option uses (h_g).  Unit phase capacity then
forces

\[
 h_g\notin F_0(o_e)\cup F_0(o_g).                        \tag{9.1}
\]

Thus a third mode whose every phase-0 option uses its own new host cannot
complete the triple.  For a pair with an empty partner phase-1 menu, (f)
must also use (h_g) in phase 1, so (g) must avoid (h_g) in both phases.

### 9.2 Same-key/same-flag obstruction

If the pair partner menu is empty in both phases, the new host must occur in
both partner tickets at one declared key, with the same physical flag.  If no
such cross-phase join exists, the triple is impossible even when both
phasewise ticket menus are nonempty.

### 9.3 Source-capacity obstruction

If every exact (f)-phase-0 ticket using (h_g) also uses a row in
(F_0(o_e)), then no packing preserving (o_e) exists.  The analogous test
applies in phase 1.  Opposite-phase row sharing is allowed only at an equal
flag and therefore must not be confused with a same-phase capacity conflict.

### 9.4 Third-option obstruction

For a compatible pair \((o_e,o_f)\), let \({\cal O}_g^{\rm free}\) contain
the third options satisfying

\[
 F_\phi(o_g)\cap(F_\phi(o_e)\cup F_\phi(o_f))=\varnothing
 \quad(\phi=0,1)                                         \tag{9.2}
\]

and agreeing with \(\gamma_{o_e}\cup\gamma_{o_f}\) wherever a physical row
is shared across phases.  The triple is impossible if
\({\cal O}_g^{\rm free}=\varnothing\).  This is precisely the final shore of
the hypergraph oracle, not a marginal self-support count.

## 10. Two-branch completeness boundary

The 94-anchored search is not, by itself, the complete three-mode face.
This follows from an exact support decomposition.

Let (e) be a unary-common-zero source in a feasible triple
\((e,f,g)\), and choose its triple option (o_e).  Put

\[
 S_e(o_e)=\{x\in\{f,g\}:h_x\in F_0(o_e)\cup F_1(o_e)\}.  \tag{10.1}
\]

Deletion of (d_f,d_g) cannot create an option, so (S_e(o_e)\ne\varnothing).
There are two cases.

1. **Single-helper support.**  If (S_e(o_e)=\{f\}), then (o_e) remains
   valid in the pair child \((e,f)\): it does not use (h_g), and it cannot
   use (d_g), which is absent in the triple.  Hence \((e,f)\) is one of the
   complete source-rescue upper pairs, and this orientation belongs to the
   94-anchored branch.  The same holds with (f,g) exchanged.
2. **Bilateral support.**  If (S_e(o_e)=\{f,g\}), the source may need both
   new hosts in one option.  Removing either helper can destroy the option,
   so neither two-mode subchild need belong to the 94 ledger.

Therefore a lossless global three-mode search is the union of

\[
 \boxed{\text{94-anchored single-helper extensions}}
 \quad\cup\quad
 \boxed{\text{irreducible bilateral-source options using both helper hosts}}.
                                                               \tag{10.2}
\]

The 70-row upper is lossless for the first box only.  It is not a proof that
the bilateral box is empty.  The exact replay in Section 8.1 now proves that
the first box is empty.  Consequently every still-possible three-mode child
containing one of the 468 sources must lie in the second box: its chosen
source option must use both other new hosts.  In symbols, any surviving
triple witness must satisfy

\[
 \boxed{S_e(o_e)=\{f,g\}.}                               \tag{10.3}
\]

The same distinction explains why deleting candidates whose third donor
kills one frozen pair source witness is generally unsafe: (h_g) may create
an alternative source option.  An exact implementation must either rebuild
the source menu, as the 70-row upper does phasewise, or route the candidate to
the bilateral/re-anchoring branch.

## 11. Proof-safe exact-verifier specification

For every retained directed triple, a complete verifier must:

1. authenticate the canonical parent, catalogue, source bank, partner bank,
   phase owner tables, private rows, phase reservations, and triple request;
2. assert six distinct endpoints and the literal transfer payload on the
   fixed-final parent;
3. construct (2.1) independently in each phase;
4. enumerate every exact physical ticket for all three shorts and all 90
   declared keys;
5. form every internally flag-consistent same-key two-phase option;
6. test the exact hyperedge conditions (4.1)--(4.2);
7. emit complete witness tickets even on a positive found before the end of a
   menu, together with menu and option counts sufficient to audit the search;
8. only after an occurrence hyperedge is found, simultaneously materialize
   the three transfers and verify all protected rows; and
9. run a fresh complete supplier graph and maximum matching on that child.

An efficient exact implementation may index options with conflict bitsets.
For a role-option bank (B), precompute

\[
 U_{\phi,v}=\{j:v\in F_\phi(o_j)\},\qquad
 V_{v,c}=\{j:o_j\text{ assigns }v\text{ a flag other than }c\}. \tag{11.1}
\]

For a compatible partial choice \((o_e,o_f)\), subtract from the (g)-bank

\[
 \bigcup_{\phi,v\in F_\phi(o_e)\cup F_\phi(o_f)}U_{\phi,v}
 \ \cup\!
 \bigcup_{v\in\operatorname{dom}(\gamma_{o_e}\cup\gamma_{o_f})}
 V_{v,(\gamma_{o_e}\cup\gamma_{o_f})(v)}.                \tag{11.2}
\]

Nonemptiness after subtraction is exactly the remaining hyperedge test,
provided \(o_e,o_f\) are already mutually compatible.

## 12. Scope

This note proves the exact occurrence oracle, the three-transfer lower bound,
the directed third-host rescue invariant, the losslessness of the 70-row
phasewise upper on the 94-anchored domain, the exact occurrence no-go for all
70 survivors, and the resulting necessity of bilateral source support in any
still-open three-mode child.

It does not prove the bilateral branch empty and therefore does not close the
complete three-mode face.  It also makes no claim of supplier-rank
preservation, deficiency 20, residual presentation completion, chronology,
residence, arbitrary upper coverage, compilation, or a K17 word.  Phase 1
remains transported-owner evidence rather than an independently native
phase.

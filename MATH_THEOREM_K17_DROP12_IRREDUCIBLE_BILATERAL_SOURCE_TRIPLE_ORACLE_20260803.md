# K17 drop-12 irreducible bilateral-source triple oracle

**Date:** 2026-08-03

**Status:** exact lossless factorization and checker specification for the
remaining cardinality-three occurrence face on the canonical drop-12 parent.
It defines the smallest source-support domain that a complete search must
scan. It does not report that domain's data-dependent row count, an
occurrence positive, a supplier replay, or a K17 word.

## 1. Frozen scope and premises

The parent and structural catalogue are

```text
compressed  e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
final       fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
catalogue   790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
```

Let (S) be the 468 authenticated structural supplier-rank-16,878 source
modes (ledger SHA `21ab1c4f987c54d835306394c86a7aef0b96ead2caeaf31153b9513889a91050`),
and let (U) be the 112,621 fixed-bank-safe parent-local modes (ledger SHA
`f1d9ab4ad29d4806d1b3e6a7518dda17733cd415c24e34a5aa8865f236f067db`).
The source bank is a subset of (U).

Occurrence semantics are fixed as follows.

* All 7,213 private rows are unavailable in both phases.
* The ten incumbent tickets reserve 20 physical rows separately in each
  phase. The two reservation maps have intersection 17 and union 23.
* A row reserved only in the opposite phase may be used only at its incumbent
  flag.
* The ten materialized incumbent LLR hosts remain eligible long providers
  whenever the phase rule permits them. Structural endpoint immutability is
  not a global witness-row ban.
* Phase 0 is native. Phase 1 is the explicitly transported owner phase only.

The corrected phase-specific unary replay proves exact common-option zero on
all 468 sources. Its frozen manifest SHA is
`94101008273ed54928cd818daab8142bf03b007fba106477c71009b4d0ffcb03`.

The complete source/partner face has 52,664,349 endpoint-disjoint directed
incidences. A lossless source-rescue upper leaves 94, and the exact verifier
finds no pair packing on those 94:

```text
upper94 ledger  3f61ed962dcdca21cb3a3412f89a9ec9de27c594e7358e7921bc7d2727ad31e5
exact94 ledger  f33f6ed5a7102ee3cc63a260a0608685a6776586c8014015ad8df56c0c4421c5
exact94 audit   1e9a44d5336ff436e8b08c3fe8d28c2a2426430f150a5c7a335c5d69b50c92b4
```

Extending those 94 prefixes by every endpoint-disjoint third mode gives
10,536,324 directed triples. A lossless phasewise upper leaves 70; a complete
three-role verifier finds zero occurrence packings on all 70:

```text
triple upper ledger  762c65a41176dcea9517a52f4213f2faea3bcf69a879d90089ef89412f1cd0e3
triple upper audit   46ce798aa266b7d5653cacb55f1a401c6bc64fd5933d9a155d92bb7d6986e24d
exact70 ledger       281b32fd6d4acb8e0c78abadbc7d85fca1bb0f89b7092eb08c6ee2d8a8a21555
exact70 audit        b99f8b509a58a5ebb3f8c9c0fae32ab3c6452a7480308e3e0b12770a14d2135c
```

The 94-prefix and 70-row results are used below only through their proved
losslessness. No no-go is inferred from either upper screen alone.

## 2. Literal state bank and exact tickets

For a mode (x), write (h_x) for its old LR host and (d_x) for its old
LMR donor. Simultaneous installation performs

```text
h_x : (u_x,q_x)       -> (l_x,u_x,q_x),
d_x : (l_x,m_x,r_x)   -> (m_x,r_x).
```

Let (H_x^phi(c)) be the flag-(c) long state installed at (h_x) in
phase (phi), and let ({\cal L}_0^phi) be the fixed-final long-state
bank after the private-row and exact phase-reservation rules. For any
endpoint-disjoint installed set (T),

\[
 {\cal L}_T^\phi=
 \left({\cal L}_0^\phi\setminus\{d_x:x\in T\}\right)
 \cup\{H_x^\phi(c):x\in T,\ 0\le c<4\}.                \tag{2.1}
\]

There are no other long-state changes.

For the new MR short of role (x), a phase-(phi) ticket at declared key
(k=(q,\alpha,\beta)) is

\[
 w=(k;p,\alpha;s,\beta),                               \tag{2.2}
\]

where both long states occur in (2.1), the exact incoming, outgoing, and
literal five-cell predicates hold, and (p=s) implies
(\alpha=\beta). Its phase footprint is the physical set
(F_\phi(w)=\{p,s\}), with a repeated row counted once, and its flag map is
(p\mapsto\alpha, s\mapsto\beta).

A two-phase role option is a pair ((k,w^0,w^1)) at the same declared key
whose two flag maps have a single-valued union. Keys are common only between
the two phases of one role; different roles need not declare the same key.
Every physical tuple must be retained. A marginal state count or a first
witness is not an exact menu.

## 3. Exact support-two theorem

Fix an endpoint-disjoint triple (T=\{e,f,g\}) with (e\in S), and let
(o_e) be a source option in the triple child. Define its helper-host support

\[
 \operatorname{supp}_e(o_e)=
 \{x\in\{f,g\}:h_x\in F_0(o_e)\cup F_1(o_e)\}.          \tag{3.1}
\]

### Theorem 3.1 (irreducible bilateral support)

If (T) has a complete three-role occurrence packing, then the source option
used by that packing satisfies

\[
 \boxed{\operatorname{supp}_e(o_e)=\{f,g\}.}            \tag{3.2}
\]

### Proof

If the support is empty, neither phase ticket uses an inserted helper host.
The tickets also cannot use (d_f) or (d_g), since those rows are absent in
the triple bank. Adding those two old long rows back cannot invalidate either
ticket. Hence the same option exists in the unary (e)-child, contradicting
the exact 468/468 unary common-zero theorem.

Suppose the support is ({f}). Removing (g) deletes no state used by the
option: it does not use (h_g), and it could not use the absent (d_g).
Thus the same source option exists in the (e+f) child. The lossless
52,664,349-to-94 source-rescue screen must retain the directed prefix
((e,f)). Consequently (T) is in the complete 10,536,324 extension of the
94-prefix bank. Every occurrence-valid extension passes the lossless
phasewise upper, but the complete exact replay proves zero on all 70 upper
survivors, a contradiction. The case ({g}) is symmetric. Only support
({f,g}) remains. \(\square\)

This proof does not assume that the (e+f) pair itself packs. It uses only
the existence of its source option and the losslessness of the subsequent
third-mode upper and exact replay. If a triple contains two or three members
of (S), the argument applies separately to every source role in a chosen
packing.

## 4. The exact (B/G1/G2) phase factorization

Fix (e\in S), a phase (phi), and a key (k). Let
({\cal B}_{e,\phi}(k)) be the complete phase menu in the unary (e)-child,
where (d_e) is deleted and (h_e) is installed.

For an unordered endpoint-disjoint helper pair ({f,g}), define:

\[
\begin{aligned}
 B_{e,\phi}^{f,g}(k)
   &=\{w\in{\cal B}_{e,\phi}(k):
          d_f,d_g\notin F_\phi(w)\},\\
 G1_{e,\phi}^{f\mid g}(k)
   &=\{w\in{\cal W}_{e,\phi}^{e,f}(k):
          h_f\in F_\phi(w),\ d_g\notin F_\phi(w)\},\\
 G1_{e,\phi}^{g\mid f}(k)
   &=\{w\in{\cal W}_{e,\phi}^{e,g}(k):
          h_g\in F_\phi(w),\ d_f\notin F_\phi(w)\},\\
 G2_{e,\phi}^{f,g}(k)
   &=\{w\in{\cal W}_{e,\phi}^{e,f,g}(k):
          \{h_f,h_g\}\subseteq F_\phi(w)\}.
                                                               \tag{4.1}
\end{aligned}
\]

The pair-child definition makes each (G1) ticket use exactly the named
helper host: the other helper host is not long there. A (G2) ticket has the
two physical rows (h_f,h_g); both predecessor/successor orientations remain
distinct.

### Lemma 4.1 (exact phase partition)

\[
\boxed{
 {\cal W}_{e,\phi}^{e,f,g}(k)=
 B_{e,\phi}^{f,g}(k)
 \mathbin{\dot\cup}G1_{e,\phi}^{f\mid g}(k)
 \mathbin{\dot\cup}G1_{e,\phi}^{g\mid f}(k)
 \mathbin{\dot\cup}G2_{e,\phi}^{f,g}(k).}              \tag{4.2}
\]

### Proof

Classify a triple ticket by which of (h_f,h_g) occur in its footprint. The
four possibilities are neither, only (h_f), only (h_g), and both. By
(2.1), a ticket using neither is exactly a unary ticket surviving both donor
deletions. A ticket using only one helper host is exactly a ticket created in
the corresponding pair child and surviving the other donor deletion. A
ticket using both is in (G2). These classes are exhaustive and disjoint.
\(\square\)

The donor tests in (4.1) are essential. A host aperture without the literal
other provider row is not sufficient: that row may be (d_f) or (d_g) and
disappear in the triple child.

By Theorem 3.1, the complete source-option join uses exactly the following
nine ordered phase-class pairs, where phase 0 is listed first:

```text
(B,G2)       (G2,B)
(G1_f,G1_g)  (G1_g,G1_f)
(G1_f,G2)    (G2,G1_f)
(G1_g,G2)    (G2,G1_g)
(G2,G2)
```

Within each pair, retain only tickets with the same declared key and a
single-valued cross-phase flag map. This list includes one helper in each
phase, both helpers in one phase, and every mixed repetition. It excludes
exactly the support-zero and support-one cases already closed in Section 3.

## 5. Candidate-driven semantic-state join

For a helper mode (x), phase (phi), and flag (c), the activated state
record must contain at least

\[
 A_x^\phi(c)=
 (x,h_x,c,\operatorname{LongFamily}(l_x,u_x,q_x,c),
       q_x,\operatorname{owner}_\phi(h_x)).              \tag{5.1}
\]

The mode ID (x) cannot be replaced by the host row alone. Different modes
may share (h_x) while installing different lower payloads; even identical
installed host states can have different donors, new shorts, supplier
effects, and casualty tests.

For every fixed source, phase, key, short family, and ticket side, quotient
activated states only by the complete semantic arguments used by the exact
predicates, and retain a posting list of every originating mode/state record
in each quotient class. The exact physical flag is retained explicitly even
when it is fixed by the declared key. On the predecessor side,
`incoming_possible` depends on that flag and the left `Family`. On the
successor side, `outgoing_possible` and `common_five_cell` depend on the exact
flag, right `Family`, physical root, and phase owner. The exact
`common_five_cell` predicate is evaluated once per surviving left/right
semantic-class pair; compatible posting-list products are expanded only
afterward.

On the frozen 468-source bank, the source-short transition arguments collapse
to exactly 32 two-phase role classes keyed by

\[
 (m_e,r_e,\operatorname{owner}_0(d_e),
          \operatorname{owner}_1(d_e)).                \tag{5.2}
\]

Predicate tables may be cached by these 32 classes. This quotient does not
merge source records: each posting still retains the exact source edge,
source host state, deleted donor, physical rows, support derivation, and
supplier identity. Source-specific unary-bank membership and casualty tests
are expanded from the postings before ledger emission.

* Join one activated state to every compatible state in the complete unary
  (e)-child bank to emit a literal (G1) ticket. This bank explicitly includes
  the source's installed own-host states (H_e), every admissible incumbent
  LLR host, and all other long states surviving the exact 20/20 reservation
  and opposite-phase fixed-flag rules; “base” must not be implemented as
  parent-only. Before ledger emission, reject the record if its non-created
  provider footprint uses either named helper donor (d_f) or (d_g); the
  helper's own pair-child construction alone is not a substitute for this
  two-donor test. Also test the activated state against itself when
  (alpha=beta): the legal same-row ticket ((H_f,H_f)) has one physical
  helper-host footprint and belongs to (G1), not (G2).
* Join compatible activated states from two distinct helper modes to emit a
  literal (G2) ticket. Evaluate the exact common-five-cell predicate after
  the index join; a signature bucket is only an acceleration.
* Store the key, predecessor/successor orientation, physical rows, flags,
  support edge IDs, and full footprint. The footprint is the donor-casualty
  certificate.
* Never deduplicate on the literal ticket tuple alone. Distinct support
  modes/states can yield the same physical rows and flags (the host-3362
  family is a calibration hazard) while carrying different donor casualties,
  short payloads, and supplier effects. Canonicalize only identical complete
  derivation records, or store one literal tuple with the full provenance
  posting list. In particular, collapse duplicate discovery of a same-row
  ticket only within one complete support derivation.

This is a candidate-driven exact type-pair join. It avoids the blind outer
loop over all (112621^2) helper pairs for each source: a helper pair is formed
only by expanding an exact compatible semantic-class pair or by joining two
one-host postings. No subquadratic or output-sensitive worst-case bound is
claimed; compatible posting-list products may themselves be quadratic and
their measured workload must be reported honestly.

For a phase record (w), let (R(w)\subseteq U) be the helper modes whose
installed states occur in it. Join phase-0 and phase-1 records on source and
declared key, then require

\[
 |R(w^0)\cup R(w^1)|=2,                                 \tag{5.3}
\]

six distinct transfer endpoints, survival under both named donor deletions,
and a single-valued cross-phase flag union. The helper pair
({f,g}=R(w^0)\cup R(w^1)) is determined by the records; it is not guessed
from the quadratic structural bank.

Define the exact anchored source-support domain

\[
\begin{split}
 {\cal Q}=\{(e,\{f,g\}):{}&e\in S,\ f,g\in U,\ f<g,\\
 &|\{h_e,d_e,h_f,d_f,h_g,d_g\}|=6,\\
 &\text{the nine-class join contains a source option}\}.
                                                               \tag{5.4}
\end{split}
\]

### Theorem 5.1 (losslessness of the indexed domain)

Every occurrence-valid three-mode child containing a member of (S) appears
in ({\cal Q}) under at least one source label.

### Proof

Choose a source label (e) and its option from a valid packing. Theorem 3.1
says its helper support is exactly ({f,g}). Lemma 4.1 reconstructs each
phase ticket in one of the four exact classes, and the two records pass
(5.3), endpoint disjointness, donor survival, the same-key join, and
cross-phase flag consistency. Hence the indexed join emits
((e,\{f,g})). \(\square\)

The converse is deliberately not claimed: membership in ({\cal Q}) proves
only a complete source option, not options for the two helper shorts or a
three-role packing.

## 6. Exact finite host-incidence templates

There are two useful finite template counts before literal rows, flags, and
state predicates are expanded.

For the source role alone, its selected-host footprint in one phase is a
subset of ({h_e,h_f,h_g}) of size at most two, hence one of seven subsets.
Forbidding one specified helper leaves four subsets; forbidding both helpers
leaves two. Inclusion-exclusion across the two phases gives

\[
 7^2-2\cdot4^2+2^2=\boxed{21}                           \tag{6.1}
\]

source selected-host patterns in which both helper hosts occur at least once.

For the full three-role packing in one phase, assign each selected host row
(h_e,h_f,h_g) to one of

\[
 \{\text{unused},\text{source }e,\text{helper }f,
                         \text{helper }g\}.              \tag{6.2}
\]

Same-phase unit row capacity makes this assignment a function. Of the
(4^3=64) maps, exactly three are impossible because they assign all three
distinct hosts to one role, while one role ticket has at most two distinct
provider rows. Thus there are 61 phase maps.

If (h_f\) is forbidden from the source role, there are
(4\cdot3\cdot4=48) raw maps and two impossible all-to-one maps, hence 46.
If both (h_f) and (h_g) are forbidden from the source role, there are
(4\cdot3\cdot3=36) raw maps and again two impossible maps, hence 34.
Requiring both helpers to occur in the source role in at least one of the two
phases therefore gives

\[
 61^2-2\cdot46^2+34^2=\boxed{645}.                       \tag{6.3}
\]

These 645 matrices are a lossless host-incidence cover of the remaining
three-role face. They are not 645 physical triples or occurrence positives.
Ticket position, state family, declared key, flags, base-provider rows,
donor casualties, and cross-phase coalescing remain join fields.

## 7. Complete helper menus and the three-option oracle

For any role (x\in T=\{e,f,g\}), let (y,z) be the other two modes. The
same delta proof as Lemma 4.1 gives its complete phase menu

\[
 {\cal W}_{x,\phi}^{T}(k)=
 B_{x,\phi}^{y,z}(k)
 \mathbin{\dot\cup}G1_{x,\phi}^{y\mid z}(k)
 \mathbin{\dot\cup}G1_{x,\phi}^{z\mid y}(k)
 \mathbin{\dot\cup}G2_{x,\phi}^{y,z}(k).                \tag{7.1}
\]

For the two helper roles every class is retained. Parent-common status, one
selected tuple, or a forced mutual-rescue orientation is not a substitute:
a donor deletion may kill an old option, while either other host may create
an alternative.

Build all internally flag-consistent same-key two-phase options
({\cal O}_e(T),{\cal O}_f(T),{\cal O}_g(T)). A triple of options is
compatible exactly when

\[
 F_\phi(o_x)\cap F_\phi(o_y)=\varnothing
 \quad(\phi=0,1;\ x\ne y),                              \tag{7.2}
\]

and the union of all three cross-phase flag maps is single-valued. Same-phase
sharing is forbidden even at an equal flag; opposite-phase sharing is legal
only at an equal flag.

### Theorem 7.1 (exact three-role oracle)

The child (T) has a simultaneous occurrence packing with the ten incumbent
tickets if and only if the three option banks contain a compatible triple
under (7.2) and the global flag rule.

### Proof

Any packing restricts to one same-key two-phase option for each new short.
Unit phase capacity gives (7.2), and the physical one-flag address gives the
global flag rule. Conversely, three compatible options supply all six exact
new tickets; their menus already enforce the private-row and phase-specific
incumbent reservations. Thus they extend the ten incumbent tickets to the
required packing. \(\square\)

Pairwise incompatibility bitsets are exact here: phase conflicts and unequal
cross-phase flags are pairwise constraints. After choosing a compatible
source/helper pair, subtract their conflict bitsets from the third option
bank. Nonemptiness is exactly a hyperedge test.

## 8. Structural census and symmetry conventions

Let (P) be the endpoint multigraph of (U). For source
(e=\{a,b\}), write (m(a,b)) for endpoint-pair multiplicity. The number of
endpoint-disjoint individual helpers is

\[
 n_e=|U|-\deg_P(a)-\deg_P(b)+m(a,b).                    \tag{8.1}
\]

Let (P_e) be the subgraph induced by edges avoiding (a,b). The exact
number of unordered mutually endpoint-disjoint helper pairs is

\[
 Q_e={n_e\choose2}
 -\sum_v{\deg_{P_e}(v)\choose2}
 +\sum_{\{u,v\}}{m_{P_e}(u,v)\choose2}.                 \tag{8.2}
\]

The last term corrects parallel helper pairs, which the degree sum counts at
both endpoints. Thus the raw designated-source structural incidence count is
(A=\sum_{e\in S}Q_e); an ordered helper scan has exactly (2A) rows.
Neither number is the source-support domain size (|{\cal Q}|).

For unique physical child tables, let (T_i) count endpoint-disjoint triples
containing exactly (i) source modes. If

\[
\begin{aligned}
 B&=\sum_{\{s,t\}\subset S,\ s\perp t}
       |\{p\in U:p\perp s,t\}|=T_2+3T_3,\\
 C&=\sum_{\{s,t\}\subset S,\ s\perp t}
       |\{u\in S:u\perp s,t\}|=3T_3,
                                                               \tag{8.3}
\end{aligned}
\]

then

\[
 T_3=C/3,\qquad T_2=B-C,\qquad
 T_1=A-2T_2-3T_3,                                      \tag{8.4}
\]

and the unique structural child count is

\[
 T_1+T_2+T_3=A-B+T_3.                                  \tag{8.5}
\]

These formulas permit a light SHA-bound census without enumerating the raw
helper-pair product. No numeric value of (A), (T_i), or
(|{\cal Q}|) is asserted in this note before that census and the complete
created-ticket join are frozen.

For a distinguished source, helpers are unordered; use (f<g) by catalogue
ID. Swapping helpers does not change the child, but predecessor/successor
orientations in (G2) remain distinct. If a sorted edge triple contains
multiple source modes, preserve every viable source label through the source
join. Before the complete helper-menu replay, collapse to

\[
 (\{a,b,c\},A_{\rm bil}),                               \tag{8.6}
\]

where (A_{\rm bil}) is the set of source labels with a nonempty bilateral
option bank. One physical child replay then covers all retained labels.
Discarding the label set before this projection is not proof-safe.

## 9. Required frozen ledgers

A fail-closed implementation should hash-bind at least:

1. `structural_domain.summary.tsv` and a per-source ledger implementing
   (8.1)--(8.5), including ordered/unordered and one/two/three-source counts;
2. `INPUTS.sha256`, created and fully checked before any promoted run, binding
   the parent, catalogue, source bank, partner bank, reservations, incumbent
   tickets, occurrence union, owner phases, theorem, checker sources, and all
   executable build inputs;
3. `activated_state_classes.tsv`, asserting the 32 source-role classes,
   reporting left/right semantic-class and compatible class-pair counts, and
   mapping every class back to the complete provenance posting list of edge
   IDs, exact host-state payloads, and donor casualties;
4. `B.tsv`, `G1.tsv`, and `G2.tsv`, retaining every literal phase ticket and
   its complete support derivation/provenance set;
5. `support2_options.tsv`, with both phase tickets, common key, rows, flags,
   support IDs, and donor-survival fields;
6. `support2_roles.tsv`, the canonical (e,f,g) projection of
   ({\cal Q}), with (f<g);
7. `support2_children.tsv`, sorted physical triples plus the complete viable
   source-label set and its one/two/three-label histogram;
8. `exact_triple_occurrence.tsv`, complete menu/option counts and one literal
   six-ticket witness for every occurrence positive; and
9. `supplier_replay.tsv`, child-table hashes and a fresh complete supplier
   maximum matching for every occurrence positive.

The audit must also assert the 21 source patterns, 645 full host-incidence
matrices, 20/20 phase reservations, 17-row intersection, 23-row union,
7,213-row private bank, six distinct endpoints, and byte-identical protected
rows after simultaneous materialization.

## 10. Exactness hazards

The following reductions are not lossless.

* Scanning only the 94 pair prefixes: this omits (G2) source tickets whose
  two helpers are jointly necessary.
* Keeping only (G1_f^0G1_g^1) and its phase reverse: this omits all seven
  (G2+(B/G1/G2)) class pairs.
* Applying donor casualties in only one phase or only to base tickets.
* Merging modes by host row or installed family without retaining their edge
  IDs, donors, short payloads, and supplier effects.
* Using the global 23-row reservation union in both phases. The exact rule is
  20 rows per phase with opposite-only rows admitted at their fixed flag.
* Treating endpoint-forbidden rows as globally forbidden occurrence
  providers; incumbent LLR hosts remain eligible.
* Equating phasewise menu nonemptiness with a same-key two-phase option.
* Requiring different role keys to agree.
* Allowing two roles to share a same-phase row because their flags agree, or
  forbidding equal-flag reuse across opposite phases.
* Freezing one helper tuple instead of regenerating its complete triple-local
  menu.
* Deduplicating source labels or (G2) predecessor/successor orientations.
* Adding marginal Hall or supplier credits. The two extra modes can destroy
  the source's unary rank improvement.

## 11. Acceptance and scope

For every option-hypergraph positive, simultaneously install all three modes,
verify the literal child table and all protected rows, replay the six new
tickets with the ten incumbents, and run a fresh complete supplier matching.
The target-deficiency pass condition is final rank 16,878, not a marginal
Hall score.

This theorem proves the losslessness of the support-two factorization and the
645-template full host-incidence cover. It does not prove
({\cal Q}=\varnothing), does not report (|{\cal Q}|), and does not certify
supplier rank, residual outer matching, selected-parent projection,
endpoint/demand composability, literal cyclic replay, chronology, residence,
compilation, or a K17 word. Phase 1 remains transported-owner evidence only.

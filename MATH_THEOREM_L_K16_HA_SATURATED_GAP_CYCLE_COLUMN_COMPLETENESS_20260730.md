# K16 H/A portal component: saturated-gap cycle columns and exact pair MITM

Date: 2026-07-30

Status: unconditional weighted-column and positive-cut completeness theorem;
independently reconstructed finite catalogue; the primary finite search
disposition is recorded in Section 6

## 1. Frozen state and exact scope

The rooted word is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873
sole hole H = 0x2c6d = 11373.
```

The opposite recurring one-hole label is

```text
A = 0xa86d = 43117.
```

The archived portal-composition bundle contains twelve `H` backgrounds and
sixteen `A` backgrounds.  Every persistent-`H` one-cell minimum goes to `A`,
and every `A` one-cell minimum returns to `H`.  This is a literal atlas fact,
not a state-quotient theorem: two words with the same hole can have different
future columns.  Moreover, a chronological `A -> H` return may rewrite an
already used position.  Hamming support must therefore be normalized to the
four final distinct positions; an ordinary shortest path in the two-label
graph is unsound.

The finite move catalogue is

```text
scratch/k16_h1_radius4_mitm_catalogue_20260730.tsv
SHA-256 19a48659bdd50abf0a17d3baa3755b79fa88ab7c69a1361dd39a51eb9cd2d4a0
288 positions, 7099 genuine position/value moves.
```

It is exactly the union declared by its builder: retained provider-atlas
moves with at most eight holes, values occurring in the archived portal
circuits and depth-two children, positions in the twelve interacting nested
supports, and the 245-value closure alphabet on the named closure positions.
The incumbent at a position is not a move.

The theorem below concerns a final four-edit support partitioned into two
pairs `P,R` such that:

1. all four positions are distinct and every final value is in this finite
   catalogue;
2. one pair, called `P`, installs `H` when applied alone to the source;
3. both pair-alone states have at most eight holes; and
4. the pair supports are ordered and the fixed open gap between them has OR
   `0xffff` in the source.

This is the **separated saturated-gap class**.  It is not unrestricted
radius four.

## 2. Exact weighted transport and positive cuts

For a word `w`, let `m_w(t)` be the number of nonempty contiguous intervals
whose OR is `t`.  For an equal-length rewrite `w -> v`, define the signed
transport column

\[
                 \beta_{w,v}(t)=m_w(t)-m_v(t).          \tag{2.1}
\]

Every changed interval contributes one directed arc from its old label to its
new label.  Therefore (2.1) is the divergence of the exact weighted arc
multiset, and

\[
 v\text{ is universal}
 \quad\Longleftrightarrow\quad
 \beta_{w,v}(t)\le m_w(t)-1\quad(0<t<2^{16}).          \tag{2.2}
\]

For every set `Q` of nonzero targets, summing (2.2) gives the positive-cut
inequality

\[
 \beta_{w,v}(Q)\le
 \sum_{\substack{t\in Q\\m_w(t)>0}}(m_w(t)-1)
 -|Q\cap\mathcal H(w)|.                               \tag{2.3}
\]

Singleton `Q={t}` cuts are already equivalent to (2.2); larger down-ideal or
nested-annulus cuts are useful aggregated certificates.  This is an integral
capacity statement, not a fractional score.

Stateful columns always telescope along an exact path.  Static columns
computed against one common source do **not** generally add when their
supports interact.  The next lemma proves precisely why they add here.

## 3. Saturated-gap annihilation lemma

Let `P` lie strictly to the left of `R`, and let `G` be the fixed open interval
between the rightmost position of `P` and the leftmost position of `R`.
Assume

\[
                         \operatorname{OR}_w(G)=0xffff. \tag{3.1}
\]

### Lemma 3.1 (exact static-column additivity)

For arbitrary nonzero replacement values on the two disjoint pairs,

\[
             \boxed{\beta_{w,w^{P\cup R}}
                    =\beta_{w,w^P}+\beta_{w,w^R}}.     \tag{3.2}
\]

### Proof

Partition intervals by which pair supports they meet.  Intervals meeting no
edit contribute zero.  An interval meeting only `P` or only `R` contributes
exactly its corresponding pair-alone transport arc.  Every interval meeting
both pairs contains all of `G`; by (3.1), its old, pair-partial and final ORs
are all `0xffff`.  Its apparent transport arc is the loop
`0xffff -> 0xffff`, whose divergence is zero.  These four classes prove
(3.2) coordinatewise.  QED.

The same statement holds for the multiplicity delta
`delta=m_new-m_old=-beta`.  A deterministic regression compares 500 random
pair deltas and 500 random four-site deltas against fresh full multiplicities,
then compares 500 random saturated-gap four-site deltas with the sum of their
pair columns.  All 1,500 comparisons pass for all 65,536 labels.

## 4. Exact rarest-debt meet-in-the-middle theorem

Enumerate every unordered pair of distinct catalogue positions and values.
The implemented preliminary portal filter is necessary-complete: if a new
`H` witness meets only one edited site, the corresponding singleton installs
`H`; if it meets both, both replacements and the fixed bridge between them
are submasks of `H`.  No possible catalogue portal pair is discarded.
A **portal action** is a pair action which installs `H` and whose exact
pair-alone state has between one and eight holes.  For a portal action `P`,
write

\[
                 D(P)=\{t:m_{w^P}(t)=0\}.              \tag{4.1}
\]

A **repair action** is a pair action whose pair-alone state has at most eight
holes and whose exact source-relative delta is positive at some target in the
union of the sets (4.1).  Every distinct-position catalogue pair is evaluated
by its exact pair column.  In particular, no individual-provider or compatible-
corridor prefilter is used: two net-zero singleton columns may have a positive
joint delta through the both-site interval class.

The completed portal enumeration encountered no zero-debt installing pair.
Thus every in-scope installing pair either is one of these nonempty-debt portal
actions or violates the hole cap; the rarest-debt choice below is always
defined.

### Theorem 4.1 (MITM completeness in the separated class)

For every portal `P`, choose any member `t*` of `D(P)`, in particular one
with the shortest repair-provider list.  If a separated saturated-gap
four-edit completion `P union R` exists, `R` occurs in the provider list of
`t*`, passes the complementary-debt test for every member of `D(P)`, and
passes the exact four-site replay.  Hence exhaustive failure of those joins
is a no-completion theorem for the class in Section 1.

### Proof

For `t in D(P)`, `m_{w^P}(t)=0`.  Lemma 3.1 gives

\[
 m_{w^{P\cup R}}(t)=m_w(t)-\beta_P(t)-\beta_R(t)
                    =-\beta_R(t).                       \tag{4.2}
\]

Universality makes the left side at least one, so
`beta_R(t)<=-1`: the repair pair has strictly positive multiplicity delta at
every portal debt.  It is therefore in the provider list of `t*` and passes
the complete debt test.  The pair supports and fixed gap pass the declared
geometry test.  Finally, (2.2), evaluated by the exact four-site column, is
necessary and sufficient for universality.  Thus the enumerator cannot miss
a completion in the stated class.  QED.

Equivalently, every rejected join has a violated singleton positive cut
`Q={t}`.  The exhaustive result is a finite integral cut cover, not an LP
relaxation or a label-level cycle argument.

## 5. Independent catalogue and primitive audit

The independent checker

```text
scratch/audit_l_k16_h1_radius4_separated_cycle_columns_20260730.py
```

reconstructs the move domains and provenance from the three frozen atlases,
both portal tarballs, the interacting-12 TSV, and the 245-value closure map.
It does not import the catalogue builder and does not rerun the pair search.
It also replays all 128 archived word records: 56 have hole `H` and 72 have
hole `A`.  The records include the base backgrounds repeated for provenance
in both tarballs and the saved depth-two children; they are not claimed to be
128 inequivalent states.

The independent reconstruction gives exactly the declared 288 positions,
7,099 moves, closure-position list, and domain histogram.  The exact source
and saturated-gap delta regression is

```text
scratch/test_k16_h1_radius4_pair_mitm_delta_20260730.cpp
```

and reports

```text
PASS 500 exact pair-delta + 500 exact four-delta
     + 500 saturated-gap additivity comparisons.
```

## 6. Primary finite-search disposition

The primary run used `screened` mode, which contains the theorem-complete
separated class and additionally tests every disjoint portal/repair pair for
which the repair pair independently has positive delta on all portal debts.
It returned

```text
PASS_EXHAUSTED_SCOPED_NO_COMPLETION

distinct-position catalogue pairs        24,348,717
portal prefilter                           4,111,372
retained portal actions                      224,114
residual targets                               1,625
retained repair actions                      775,506
disjoint portal/repair joins              897,885,352
exact screened four-site replays           27,141,316

separated saturated-gap joins              94,353,810
separated exact four-site replays           2,515,178
universal words                                     0.
```

The negative screened verdict is not complete for arbitrary unshielded
cross-derivative repairs.  By Theorem 4.1, however, the separated subset is
complete for the scope in Section 1.  Therefore:

> **Scoped no-go.** No universal length-12,873 word is obtained from the
> authenticated H1 root by four catalogue-valued substitutions admitting a
> partition into an H-installing pair and a repair pair, with both pair-alone
> states having at most eight holes and the two pair supports separated by a
> fixed `0xffff` gap.

The run used one H100 CPU at core 28 in the unique directory

```text
/home/amodo/or15/work/root_k16_h1_radius4_pair_mitm_20260730_19a48659
```

for 17:08.47 wall time and 1,028.20 user seconds, with 115,468 KiB maximum
RSS and zero swaps.  Exit status one is the program's intentional exhausted-
without-solution status.  The exact sequential source used by the binary is
retained separately from a later threaded convenience revision.

Two independent audits pass.  The first rebuilds the catalogue byte-for-byte,
checks all dimensions and terminal counts, compiles the all-label regression
against the exact sequential run source, and replays the resource terminus.
The second independently reconstructs every move and provenance tag from the
underlying atlases/tarballs/TSV/closure map, replays all 128 archived word
records and their H/A transition minima, verifies the run manifest including
the textual C++ dependency and binary, and checks the separated-count
relations without rerunning the search.

Authenticated artifacts:

```text
exact sequential run source
scratch/search_k16_h1_radius4_pair_mitm_serialrun_20260730.cpp
SHA-256 ab7744951aa15e3b70c80c9e427f118b97aaf12f074d2224a506e5c70efc8f89

included exact multiplicity dependency
scratch/search_k16_exact_joint_two_edit_blocker_20260730.cpp
SHA-256 2b2ed3a3775ea440de1fcc8725102197c073282c388642d2c293ca47da5eaa9c

H100 binary
SHA-256 9d76aea1082f16e52a385ddc98309d29a2063bb72c9a35cfdd03715d78462990

primary audit
scratch/k16_h1_radius4_pair_mitm_20260730.audit.json
SHA-256 74c7578326175f9589befa3bde56a3c5f8c9813356496d7c318964699804b794

resource and proof-input manifest
scratch/k16_h1_radius4_pair_mitm_20260730.resource.txt
SHA-256 3f0dfa114573d8bbb0d95057ac39314f098cb4f8dcf78175ae0629469a8c7d6f
scratch/k16_h1_radius4_pair_mitm_20260730.hashes.txt
SHA-256 6539831197232fef202068c69a787cea2fae5dbb27b83e17077213a5ff89b0d5

primary independent verifier and audit
scratch/audit_k16_h1_radius4_pair_mitm_final_20260730.py
SHA-256 a1330b53e1e5214034c5d7f38dc7671b67244f9373f0d3749ad70000788e642b
scratch/k16_h1_radius4_pair_mitm_final_independent_20260730.audit.json
SHA-256 a3f4308da250bd9a664ae04259b3f8792592162acda2289e3bc45ba8e611de0e
payload ce046b2006cb4158031f53c1e0126ec47dfd735588a51a982b9d7a7ba4b65571

H/A catalogue/provenance verifier and audit
scratch/audit_l_k16_h1_radius4_separated_cycle_columns_20260730.py
SHA-256 75e14fe31c5288e9ac9a8726a7ada2bd25ef74fa1dad560f97b85cd1201278b5
scratch/l_k16_h1_radius4_separated_cycle_columns_20260730.audit.json
SHA-256 7c6f624742080c1abe85552211ce3165a0b5b75435c28dc9c523451125f190e1
payload fc039b033fc64bd9f98b3d0304a91b23e60e4ab8d81cf51a1069b5f1ef30d26d

all-label delta/additivity regression
scratch/test_k16_h1_radius4_pair_mitm_delta_20260730.cpp
SHA-256 aca19c2d66f64220a8321b8ab976bec7f6a80481458251229e789080c9686e3e
```

## 7. Relation to the exact depth-three results

The radius-three results around this same root must be kept logically
separate.

* The all-three-site `H`-witness class is solver-free impossible.
* The exact two-site-plus-one theorem exhausts 105,510,990 ordered two-site
  packet assignments and every exact third-cell value, with no completion.
* The one-site portal plus jointly witnessing repair-pair theorem exhausts
  144,191,783 exact assignments with no completion.  It strictly contains
  the earlier 1,341-support nested laminar no-go; that theorem remains a
  valuable independently DRAT-checked regression subface.

The sole open radius-three class is mixed: after a one-site portal, at least
one repair individually supplies a portal debt, while some debt has no final
joint two-repair witness.  No result in this note closes that class.

There is, however, an exact no-hole-cap positive-cut oracle for its last cell.
For a two-edit intermediate word `u` and prospective last position `s`, let

\[
 \mathcal K_u(s)=\{T:\text{no current }T\text{-witness avoids }s\}. \tag{7.1}
\]

For `T in K_u(s)`, let `c_s^u(T)` be the OR of the maximal fixed
`T`-compatible collar around `s` after removing its incumbent, and put

\[
 L_s=\bigvee_{T\in\mathcal K_u(s)}(T\setminus c_s^u(T)),\qquad
 U_s=\bigcap_{T\in\mathcal K_u(s)}T.                  \tag{7.2}
\]

A nonzero value `z` at `s` covers every target after the edit if and only if

\[
                         L_s\subseteq z\subseteq U_s,   \tag{7.3}
\]

with `z` different from the incumbent for a genuine third edit.  Targets
outside (7.1) retain a witness avoiding `s`; for targets inside (7.1), the
maximal collar proves (7.3) both necessary and sufficient.

If a bit `e` lies in `L_s\U_s`, choose a target which requires `e` at `s`
and an `s`-exclusive target omitting `e`.  Setting `z_e=0` loses the first;
setting `z_e=1` loses the second.  This is a two-target integral positive-cut
certificate.  If both bounds in (7.2) are zero, at most sixteen target masks
with zero intersection certify conflict with the nonzero-cell row.  These
small certificates give the correct next proof object for the mixed branch;
bounding its intermediate hole count would be unsound.

## 8. Exact frontier

A negative Section-6 result proves only that no catalogue-valued completion
exists in the separated saturated-gap pair/pair class.  It does not exclude:

1. the open mixed radius-three branch;
2. an arbitrary value outside the 7,099-move catalogue;
3. a pair-alone intermediate with more than eight holes;
4. interleaved or short-gap pairs with a favourable cross derivative;
5. a non-pair portal packet or edits outside the 288 positions;
6. the exact arbitrary-value joint13 fibre; or
7. an unrelated length-12,873 word.

For unshielded supports the correct object is the full compound first/last-
edited-site column.  Adding source-relative primitive columns without an
absorption proof is not valid.  The global bracket remains

```text
12873 <= nu(16) <= 12874.
```

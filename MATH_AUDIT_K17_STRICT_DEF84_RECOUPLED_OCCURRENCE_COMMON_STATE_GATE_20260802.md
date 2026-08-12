# K17 strict-def84 recoupling: occurrence/common-state audit and exact next gate

**Date:** 2026-08-02  
**Status:** proof-safe finite audit and reduction.  The frozen recoupled table is
an exact lower-target/root construction and its selected donor menus have been
enumerated in two owner phases.  The selected 438-transfer face is decisively
not a common occurrence state.  No chronology, residence, upper, compiler, or
K17 word is claimed.

## 1. Frozen parent and exact static claims

The recoupling inspected here starts from the authoritative strict-`def84`
parent

```text
c490cc49aef575caae9f72d478ff08320f24a3625593f2465f9b94fb7d8ce979
  def84.selected.tsv
3171bf380c3a139313f1304bb1d821810cb7402c20aa99f01ab8ccdc189854f1
  def84.table.tsv
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  private_h_outer_materialized.tsv
736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
  round047.s7.phase1.tsv
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  selected_tickets.tsv
```

Its root-recoupling outputs are

```text
e1393222343922f8d3e55452f1996b93901a4c387a62066430f128d50101099a
  audit.json
bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241
  compressed.tsv
9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3
  final.tsv
b4e3f66178efbcd4129bc8a83cb8725b613a8eb09b35bb58548a2ffd90f5dff5
  supplier.projection.audit.json
```

The producer audit proves, on these hashes:

* all `65,535` targets of ranks at most eight occur exactly once;
* the `24,310` roots and owners and the `7,395/16,915` length histogram are
  exact;
* all `7,213` protected physical rows are unchanged;
* the static residual augmented b-matching has value `28,018/28,018`;
* the compressed table changes `213` rows from the private parent;
* overlaying the selected `438` transfers changes their `876` endpoint rows;
* the complete row-pair supplier projection has rank `16,864/16,898`, hence
  deficiency `34`, with `20` zero heads and a maximum shore `51/17`.

These are static table/projection statements.  The producer audit explicitly
excludes occurrence state, outer state, chronology, residence, upper support,
the compiler, and a word.

A separate coordinate-DP replay independently validates the final table and
the complete marginal DNF sets for all `7,395` short rows:

```text
phase 0 / phase 1 / both / either = 3099 / 2260 / 1838 / 3521.
```

Its audit SHA is

```text
33df370ac42062ce8f037b36973f4b88b087bb3a9899a7250204ad24a283d086
  def84_release.recoupled.independent.audit.json
```

Marginal positivity is only an existential OR and is not a simultaneous
ticket selection.

The recoupled output is not claimed socket-Pareto acceptable: relative to
the strict parent its phase-0 and `both` marginal counts regress by `3` and
`6`.  That rejection is separate from the finite occurrence audit below.

## 2. Exact selected-donor occurrence census

For each of the 438 selected donor short rows, the all-witness enumerator
lists tuples

```text
(short_row,q,alpha,beta,pred_row,succ_row).
```

It uses the exact relaxed-nine/common-five-cell DP, requires `beta<=alpha`,
requires equal flags when predecessor and successor are the same row, and
excludes every one of the `7,213` protected physical rows from the dynamic
short and long shores.

The frozen ledgers are

```text
30d12d86ae7fcf6eb5d5692e3273715c9426a5cf6d328e70f05677409eaa7a2f
  phase0.occurrences.tsv
fbf29b7c14abee96cc8f72a654155b3999e5e057608af952ee6f889054c0d004
  phase1.occurrences.tsv
8e57c62ef6cc198715b71b30e05ef6cf6d5d88fa49f666f1b08d4c3fa9cc1b80
  common.occurrences.tsv
b6ff2745c4b3611812cd747609a7babb864420b668fed39753f381b5c5e16774
  common.audit.json
```

The exact census is

| object | roles | tuples |
|---|---:|---:|
| phase 0 | 244 | 301 |
| phase 1 | 216 | 260 |
| positive in both phases | 188 | — |
| positive in either phase | 272 | — |
| literally identical tuple in both phases | 116 | 129 |

Thus `250` selected roles lack even separate phasewise witnesses, `322` lack
an identical two-phase tuple, and `72` of the `188` marginal-both roles have
no identical tuple.  A clean lexical set intersection of the two phase files,
followed by canonical numeric sorting, reproduces `common.occurrences.tsv`
byte for byte.

This establishes two different fixed-table obstructions:

1. even when the two phases may choose different occurrences, all 438
   selected roles are impossible because only 188 have nonempty menus in both
   phases;
2. in the stronger exact-common-tuple subface, at most 116 roles can even be
   considered.

## 3. Exact common-tuple packing rank

An identical tuple consumes one predecessor port, one successor port, and a
single common flag on every used long row.  The frozen producer computed an
exact maximum row-disjoint packing:

```text
9f8860f9d342209fe97d0bb954bcfaa6940c6ddc529292c059b3baa38ef2e90a
  common.packing.tsv
c731ca82f49139e63f17ca471aa297e19a98797c3c03d97296021e6ee858fec2
  common.packing.audit.json
```

Its rank is `113/116`; it uses `226` physical long rows.  An independent
parser/branch-and-bound audit using the weaker exact contracted-port
semantics—one predecessor and one successor port per row, with a common flag
across both directions—reproduces the same optimum:

```text
PASS_K17_RECOUPLED_COMMON_PORT_PACKING
tuples=129 roles=116 rank=113 deficiency=3
pred_rows=113 succ_rows=113 physical_rows=226
shared_opposite_direction=0 nodes=8594 bound_prunes=4194
```

The independent source is

```text
1a82bf861d49134be3b4c38f52799470ea59873e69732c14471da6b13564c74d
  scratch/audit_k17_recoupled_common_port_packing_20260802.cpp
```

There is also a transparent optimum certificate.  Three disjoint pairs of
single-menu roles are mutually incompatible:

```text
roles 10193 and 4569:  both require predecessor row 10641;
roles 15807 and 13720: row 13973 is used with flags 0 and 1 respectively;
roles 24009 and 23928: both require predecessor row 24011.
```

Therefore at least one role from each pair must be omitted, proving rank at
most `116-3=113`; the frozen packing attains this bound.  Hence the exact
common-tuple subface authenticates at most `113/438` selected donors, a gap
of `325`, before direct-transition, outer, supplier, or topology constraints.

## 4. Exact paired-phase master: the common-tuple subface is stronger than needed

Literal equality of the phase-0 and phase-1 occurrence tuples is a useful
sufficient subface, but it is not the general common-state condition.  The
two phases may select different physical occurrences provided they use one
common table, common outer/address resources, and compatible shared long-row
flags.

Fix a materialized table and protected bank.  For each active short role
`w`, phase `p in {0,1}`, and complete occurrence record `g in G_w^p`, use
`lambda_(w,g)^p`.  For each long row `h` and flag `a`, use one shared bit
`z_(h,a)`.  For each exact direct long--long transition `c` in phase `p`, use
`e_c^p`.  The smallest transparent equations are

\[
 \sum_{g\in G_w^p}\lambda_{w,g}^p=a_w,
 \qquad \sum_a z_{h,a}=1,                              \tag{4.1}
\]

and, for every `(h,a,p)`,

\[
\begin{aligned}
 O^p_{h,a}+\sum_{w,g:\operatorname{pred}(g)=(h,a)}
       \lambda_{w,g}^p
 +\sum_{c:\operatorname{tail}(c)=(h,a)}e_c^p &=z_{h,a},\\
 I^p_{h,a}+\sum_{w,g:\operatorname{succ}(g)=(h,a)}
       \lambda_{w,g}^p
 +\sum_{c:\operatorname{head}(c)=(h,a)}e_c^p &=z_{h,a}.
                                                               \tag{4.2}
\end{aligned}
\]

Here `a_w` is the common active-short bit, and `O/I` are protected stub
uses.  Every selected ticket additionally implies its complete signed DNF:
table-row state, transfer column, common-basis/outer edges, bottom address,
flag, and every occurrence resource.  Shared resources have their literal
capacity rows.

Equations (4.1)--(4.2) are exact for two contracted cycle covers sharing the
declared physical state.  Once the ticket choices and flags are fixed, the
remaining `e^0` and `e^1` rows are two ordinary bipartite perfect-matching
flows and are separated exactly by Hall cuts.  Before those branches, the
ticket layer is a typed hypermatching and is not one TU flow.

An equivalent smaller branch language forms a paired column

\[
             c=(w,g_0,g_1),\qquad
             g_p\in G_w^p,                            \tag{4.3}
\]

only when the two records' complete shared literals are compatible.  Choose
one paired column per active role, impose the four directed-port capacity
families and shared-flag rows, and run the two residual direct-transition
flows.  On the frozen selected menus there are `188` roles and only `297`
raw Cartesian paired columns before complete shared-resource filtering.  The
identical-tuple audit is exactly the special case `g_0=g_1`.

For the current frozen selection, (4.1) is already infeasible on `250` roles
with an empty phase menu.  No flow or supplier completion can repair that.

## 5. Prospective screening before transfer selection

A scalar `common_positive` label computed on one incumbent table is not an
exact prospective screen.  Selecting one LLR transfer changes one donor into
a short row and one LR row into a long row.  A witness may use a long row
changed by another selected transfer; conversely a zero transfer can gain a
witness from a newly created long state.  Therefore incumbent positivity is
neither a necessary nor a sufficient condition for a simultaneous selected
state unless its witness hosts are certified invariant.

Three proof-safe screens are available:

1. **optimistic support:** enumerate occurrences over the union of every
   admissible row state.  Absence is a necessary no-go; presence is only a
   relaxation;
2. **private stable support:** retain a witness whose complete host/resource
   footprint cannot be touched by any other selected transfer.  Presence is
   sufficient, but this may discard feasible correlated states;
3. **exact compound support:** keep each ticket as a DNF over the transfer and
   row-state one-hot variables.  This is the exact master (4.1)--(4.2).

The existing exhaustive `114,813`-edge prospective catalogue belongs to the
older compressed parent
`bb5232e33dff6c9aeb367ce8810cba111cf6c30cd3146ad6120bb1f2c49d6bcf`.
It is not a catalogue for the stronger strict-def84 parent `bf5b946f...`.
This audit assumes no prospective catalogue on `bf5b946f...`.  Any such
catalogue used downstream must be freshly generated and hash-bound to that
literal parent; old edge indices and old scalar positivity labels are not
transportable.

## 6. Smallest proof-safe next lemma

**Prospective paired-ticket branch-flow lemma.**  On the strict-def84
compressed parent `bf5b946f...`, regenerate every legal protected transfer
column and every complete two-phase paired occurrence column (4.3), with its
full row-state DNF.  Then there exist 438 row-disjoint transfer columns and
one compatible paired ticket column for each selected donor such that:

1. the shared flag and directed-port rows (4.1)--(4.2) hold;
2. both residual direct-transition Hall flows are perfect; and
3. the protected 1,748-ticket/common-basis footprint remains fixed.

This lemma is necessary and sufficient to authenticate all 438 transferred
donor roles on one declared two-phase literal state within this transfer
grammar.  Supplier Hall, one-cycle topology, carrier transport, residence,
upper support, compiler feasibility, and the word remain later gates.

The immediate finite milestone is weaker: prove that the optimistic paired
support graph has a row-disjoint transfer matching of size 438.  Failure is a
genuine no-go for this strict parent; success only authorizes building the
exact compound-DNF branch-flow master.

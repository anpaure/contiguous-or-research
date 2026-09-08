# Independent audit of the K17 rank-seven P2--H--H C6 and its correlated-column interface

**Date:** 2026-08-02  
**Status:** PASS for the single literal three-row rethread and for the two
separately declared preservation certificates.  The exact multi-column
interface below is proof-complete conditional on an exhaustive
occurrence-labelled catalogue.  No packing, common selected state, topology,
residence, upper deck, compiler, or word is claimed.

## 1. Frozen inputs and independent replay

The replay used the following files.

```text
db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185  scratch/ad_k17_s7_carrier_adapter_20260802/input/origin.res1972.tsv
ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207  scratch/ad_k17_s7_carrier_adapter_20260802/out/round047.s7.phase0.tsv
736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058  scratch/ad_k17_s7_carrier_adapter_20260802/out/round047.s7.phase1.tsv
d39b58f679f4d9219b72209b06ea71387db64cdecac649a4f390c9f7ed13da25  scratch/k17_fixed_p2_role_moving_escape_20260802/out/c1_outer.edge_map.tsv
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735  scratch/k_rots_k17_joint_1s_20260802/warm47/seed4015.relay_cegar.round047.table.tsv
21046c1d33c274c20d8259cb9e7c49a567bd372f61615192afe27ddc40af55a1  scratch/k_rots_k17_joint_1s_20260802/warm47/seed4015.relay_cegar.round047.matching.tsv
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv
179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e  scratch/k17_phase0_retained_witness_private_basis_20260802/complete_outer_matching.tsv
```

The independently written literal checker has SHA-256

```text
f00230aca24fc80e11cdeb8ecbe1f893eed037444079737c8076d93fa10dbea1
```

and the independently written supplier/private-bank checker has SHA-256

```text
82e1c98f67fba9bc041fca45e61a36dc2df076e5094b72d8f9f2c8f46df081c1.
```

Both were rebuilt locally with `clang++ -std=c++20 -O3 -DNDEBUG` and replayed
from the files above.  They returned, respectively,

```text
PASS_INDEPENDENT_K17_RANK7_P2_HH_SUFFIX_C6
PASS_K17_RANK7_SUFFIX_C6_SUPPLIER_PRIVATE_PRESERVATION.
```

The frozen replay outputs have hashes

```text
fc65985e3a8f29fa62c2d1787cbff0ca41ffbb31a1d7d1998e0181c04ea59f32  rank7_p2_hh_suffix_c6.independent.audit.txt
698e9865bae2cde1c663d62dcee78e3759ccd2f8e54a1dab174ce556817d7829  rank7_suffix_c6_supplier_private.audit.tsv
```

## 2. Literal incidence identity

The affected physical rows are

```text
P2 = 16269,  H1 = 16267,  H2 = 16271.
```

Writing each row from lower target through root, the move is

```text
old: 81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new: 81409-81417 ; 73216-81412-81413 ; 81408-81416-81420.
```

Put

```text
s0=81416, r0=81417,
b1=73216, s1=81409, r1=81413,
b2=81408, s2=81412, r2=81420.
```

Their ranks are

```text
|s0|=|s1|=|s2|=7,  |r0|=|r1|=|r2|=8,
|b1|=5, |b2|=6.
```

Direct bit replay verifies

\[
s_1\subset r_0,\quad s_2\subset r_1,\quad s_0\subset r_2,
\quad b_1\subset s_2,\quad b_2\subset s_0,
\]

with every containment strict.  Thus the new rows are legal.  The three
rank-seven values are merely cyclically reassigned,

\[
(s_0,s_1,s_2)\longmapsto(s_1,s_2,s_0),
\]

while every lower target, rank-eight root, physical-row owner and row length
is fixed.  Sorting all chain targets before and after gives the same
65,535-entry deck.  The materialized phase tables have SHA-256 values

```text
3410767cec8933140bf86bf7d36c233e43aac3a411af996fe4dfd0b474291fff  phase0.rank7c6.tsv
66f4acc8233600da02a55fb5fd60e9fff14833f539e34057fb2f6fa470825df1  phase1.rank7c6.tsv.
```

This proves exact lower-target/root/owner preservation for this move.  It
does not prove that an arbitrary collection of overlapping C6s composes.

## 3. Phase sockets and protected bank

The same new P2 row admits a literal five-cell socket in each authenticated
owner phase:

```text
phase 0: (q,a,b)=(8,2,2), modes=(70822,1584370),
         cells=(16384,1544,14849,66560,6659), owner=97801;
phase 1: (q,a,b)=(7,0,0), modes=(86138,414573),
         cells=(65,73216,8193,72712,16), owner=81481.
```

The full menu counts are 3,899 and 3,584, respectively.  Both displayed mode
pairs avoid the changed H destinations.  The two witnesses are different;
therefore **common phase means that the same row rethread has one legal
witness in each phase, not that one occurrence is shared by the phases.**

The protected-bank replay proves:

1. none of rows 16267, 16269, 16271 is a protected short row, predecessor
   host, successor host, predecessor token, or successor token in the 1,748
   selected tickets;
2. all 1,748 tickets therefore remain rowwise unchanged;
3. the complete outer matching remains legal with 16,898 H and 1,748 F
   receivers; rows 16267 and 16271 occur only as non-ticket-forced H
   receivers and their assigned bottoms remain contained in the new
   middles; and
4. the frozen warm-47 supplier matching remains 16,898/16,898.  Its only
   three affected records change masks as

```text
16269->15428: 1073741892 -> 68
19298->16271:  536870963 -> 1073741892
22299->16267:  268435506 -> 68.
```

This last item is a phase-zero/raw-warm47 certificate.  It is not a
phase-common or selected-parent supplier theorem.  Likewise, the replay does
not assert that the five new cell masks are private relative to all other
physical sockets; such occurrence-level conflicts must be carried by the
multi-column master.

## 4. Exact correlated-column master

Let `T0` be the frozen table and let `G` be a **complete
occurrence-labelled** catalogue.  One column `g` contains:

* its three changed rows `R(g)={i(g),h1(g),h2(g)}`;
* its exact old and new row states;
* one fully labelled socket witness in each required phase;
* every endpoint-mode, token, address/history, fixed-soft and other physical
  resource used by those witnesses; and
* the truth values of every protected-ticket and protected-outer incidence
  under the new local rows.

Columns which fail target/root/owner preservation or literal protected-bank
replay are deleted.  Let `x_g` be the selection bit.

### 4.1 Row and occurrence compatibility

For each physical row `r` and occurrence resource `rho`, impose

\[
 \sum_{g:r\in R(g)}x_g\le1,
 \qquad
 \sum_{g:\rho\in F(g)}x_g\le 1-b_\rho,                 \tag{4.1}
\]

where `F(g)` is the complete labelled footprint and `b_rho` is the protected
bank's prior use of that resource.  If every rank-seven role in a declared
set `K` must be repaired, also impose

\[
                  \sum_{g:i(g)=i}x_g=1\quad(i\in K).     \tag{4.2}
\]

For an optional repair face replace equality by at most one.  Equation
(4.1), rather than row disjointness alone, is required because an endpoint
mode of one column can reference a row changed by another column.

Introduce row-state bits `s_(r,sigma)`.  On the row-disjoint face they are
defined exactly by

\[
s_{r,0}=1-\sum_{g:r\in R(g)}x_g,
\qquad s_{r,g}=x_g\quad(r\in R(g)).                    \tag{4.3}
\]

Thus `T(x)` is a literal final table, not an additive menu approximation.

### 4.2 Protected outer extension

For every possible token/receiver edge `e=(u,v)`, enumerate all local state
pairs for which its containment test is legal and set

\[
 \alpha_e\Longleftrightarrow
 \bigvee_{(\sigma,\tau):\,e\text{ legal}}
     (s_{u,\sigma}\wedge s_{v,\tau}).                  \tag{4.4}
\]

With outer-edge bits `m_e`, require `m_e<=alpha_e`, one edge at every
uncontracted left and right vertex, and `m_e=1` for every forced protected
edge in `E_B` and for the fixed soft endpoint.  These are the exact residual
outer-Hall rows after contracting the protected assignments.  A chosen
alternating-cycle fibre may replace the general `m_e` rows, but that is a
scoped restriction, not WLOG.

### 4.3 Regenerated ticket/direct DNFs

Every residual ticket or direct transition `q` must be cloned over its
complete final row-state, outer-edge and flag support.  Its activation is

\[
 \lambda_q\Longleftrightarrow
 \bigwedge_{\ell\in L(q)}\ell,                         \tag{4.5}
\]

with both directions of the standard conjunction linearization.  The
catalogue in (4.5) is regenerated after the C6 packet, or pre-enumerated over
all row-state tuples from (4.3).  Retaining a pre-C6 Boolean menu is not
equisatisfiable.

The protected tickets are fixed, one activated ticket is selected for each
residual short role, and the selected flags, tickets and direct arcs obey the
exact incoming/outgoing degree equations of the contracted cycle-factor
master.  If direct arcs are projected, the resulting Hall inequalities are
valid only for factor existence; the direct-edge bits must remain through
the supplier coupling below.

### 4.4 Selected-parent supplier Hall

Supplier records must be cloned by final source state, final head state and
the unique selected primitive which owns the supplier occurrence.  For a
record `r`, impose

\[
 \kappa_r\Longleftrightarrow
 \lambda_r\wedge\pi_{\operatorname{parent}(r)},        \tag{4.6}
\]

then form the exact source--head graph by OR-ing the active `kappa_r` and
impose all supplier Hall rows.  Equations (4.3)--(4.6) are essential: two
row-disjoint C6s can jointly change a source/head record even when neither
column's stale marginal price detects it.

### Theorem 4.1 (exact scope)

Assume `G` and all record clones in (4.4)--(4.6) are exhaustive.  Integral
feasibility of (4.1)--(4.6), the protected units, the residual ticket/direct
degree equations and supplier Hall is equivalent to a row/resource-disjoint
C6 packet whose literal final table extends the protected bank to the
declared outer matching and selected-state supplier cycle-factor face.

#### Proof

From a feasible solution, (4.1)--(4.3) materialize one unambiguous final row
state.  The biconditionals in (4.4)--(4.6) make the outer, ticket, direct and
supplier graphs exactly those of that table.  Their degree and Hall rows
then give the required matchings and factor.  Conversely, read the selected
columns, row states, literal occurrences and matchings from any such packet;
all displayed rows follow.  No integrality beyond the declared binary
variables is asserted.  In particular the C6 selection remains a
three-uniform packing problem.  \(\square\)

## 5. Proof-safe scope and corrections

The exact conclusions are:

* the displayed P2--H--H C6 is a genuine support-six target reassignment;
* it preserves the complete target deck, all row roots/owners, the protected
  H tickets, one complete outer matching, and one raw warm-47 supplier
  matching;
* it admits separate exact sockets in both owner phases.

The following stronger readings are unsupported:

* one socket occurrence common to both phases;
* global reduction of the fixed/free zero count (the frozen ledger labels
  the global net delta unaudited);
* additivity of per-column DNF or supplier masks;
* cell/resource privacy from row disjointness alone;
* a common selected-state supplier factor, one cycle, residence, upper/source
  closure, compiler feasibility, or a word.

Therefore this fixture is a valid seed column for the exact master in
Section 4, but not itself a global completion certificate.

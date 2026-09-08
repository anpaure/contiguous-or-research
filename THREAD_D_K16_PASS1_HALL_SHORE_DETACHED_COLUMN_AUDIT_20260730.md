# Exact Hall-shore columns for the first all-upper `j3959` carrier

Date: 2026-07-30

Status: proved fixed-shore reduction and solver-free audit.  This is a
necessary witness-directed filter for detached exchanges, not a Hall pass
and not a search result.

## 1. Frozen incumbent and witness

The chronology

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/out7/pass_1.targets
SHA aea7a05a8837298205e9f35f39c7e6b99b8e7ef00fe46dcab9a8ab831e018e34
```

has exact maximal-envelope reconstruction and no arbitrary-width upper
hole.  Its generalized-COMP3 Hall audit is

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/hall_1.json
SHA d231de3e8ebc8073ee4e2a00ec71ff90084786cbe587a1f429c05f915ce69a2e
```

and supplies an explicit alternating-reachability shore (U) with

\[
             |U|=249,\qquad |N(U)|=215,\qquad
             |U|-|N(U)|=34.                       \tag{1.1}
\]

The solver-free audit

```text
scratch/audit_threadD_k16_pass1_hall_shore_endpoint_columns_20260730.py
SHA 6d145d33362b0126777a7e861d4ea4ca03b3ab78dcd8cce5874e1c2ecdb75694

scratch/threadD_k16_pass1_hall_shore_endpoint_columns_20260730.audit.json
SHA 9ec31925392964c9a51975a9a02e17f896317d80ee9677488239ed6666119505
payload 6b1ea694c9653b5e2270fe2b0eb27e95007b605f614627247b37250504bcd1f8
```

reconstructs the geometry directly and recovers exactly the 215 cell IDs in
the frozen Hall audit.  The canonical shore and neighbour-key hashes are,
respectively,

```text
a3bac5b3f40f91890807c2eb0262e605d80ddb8e45306f7f454a5942b9d83feb
f857d2e94bb31846964a42aafcb977e00291ecf88d15ef9c2f1dd24b00c66b19
```

## 2. Exact signed-neighbour theorem

Use the canonical right-cell key

\[
                         c=(s,\ell),\qquad 1\leq\ell\leq d_s\leq3,       \tag{2.1}
\]

where (s) is the source start.  Let (E_p) be the maximal envelope at
source position (p), and let (M_c) be the exact mandatory mask imposed by
the middle-row carrier constraints.  Put

\[
 A_c=\bigvee_{p=s}^{s+\ell-1}E_p.                                  \tag{2.2}
\]

For a lower target (S), the generalized compiler incidence predicate is
exactly

\[
 S\sim c
 \iff
 M_c\subseteq S\subseteq A_c
 \quad\hbox{and}\quad
 S\cap E_p\ne\varnothing\ \text{for every }p\in[s,s+\ell-1].        \tag{2.3}
\]

Consequently the full cell profile

\[
             \pi(c)=\left(M_c,\ \set{E_s,\ldots,E_{s+\ell-1}}\right)       \tag{2.4}
\]

determines its incidence to every lower target.  Both order and duplicate
envelope masks are irrelevant to (2.3).  Their OR makes (A_c), so it need
not be stored separately.

For the fixed shore (U=(S_1,\ldots,S_{249})), define the lossless projected
column

\[
 B_U(c)=\{j:S_j\sim c\}.                                             \tag{2.5}
\]

Thus (c\in N(U)) precisely when (B_U(c)\ne\varnothing).  For an old and
new chronology define

\[
 G_U=N_{new}(U)\setminus N_{old}(U),\qquad
 L_U=N_{old}(U)\setminus N_{new}(U).                                \tag{2.6}
\]

Then the exact shore current is

\[
 |N_{new}(U)|-|N_{old}(U)|=|G_U|-|L_U|.                             \tag{2.7}
\]

In particular every compiler-feasible detached exchange from the frozen
incumbent must satisfy

\[
                         |G_U|-|L_U|\geq34.                          \tag{2.8}
\]

This is a necessary condition.  It is not sufficient: another shore can
become deficient.

## 3. Exact finite automaton

There is a radius-six streaming implementation of (2.4)--(2.5).  A cell
(c=[s,s+\ell)), (ell\leq3), has envelope letters depending only on target
rows from (s-3) through (s+\ell-1).  A bit is mandatory in (c) when the
complete carrier of some row (rin[s-3,s+\ell-1]) lies inside (c).
Testing that complete carrier needs envelopes through (r+d_r), hence at
most through (s+\ell+2); constructing those envelopes reaches back three
more rows.  Therefore

\[
               (T_i,d_i)_{i=s-6}^{s+\ell+2}                         \tag{3.1}

determines (pi(c)).  Uniformly over (ell\leq3), the window is contained
in ([s-6,s+5]), exactly twelve rows.

An implementable deterministic transducer retains the last eleven pairs
((T_i,d_i)).  After appending row (t), it has the twelve-row window
([t-11,t]), finalizes every allowed cell length at start (s=t-5), emits
the 249-bit set (B_U(c)), and drops the oldest row.  Four 64-bit words store
the projected column.  If only the fixed cut (2.8) is needed, the single bit
(1[B_U(c)\ne\varnothing]) is the minimal projection.

For concatenated detached intervals, an exact column contains:

1. the topological `Phi` state (signed side/near relations to every local
   port and forced endpoint, plus boundary separation truncated at three);
2. the first and last eleven `(target,depth)` rows, or equivalently the
   proved six-mask-per-side pending-row state;
3. the exact arbitrary-upper prefix/suffix/seen monoid;
4. the emitted internal (B_U(c)) columns, or only their nonempty count when
   merely testing (2.8); and
5. absolute cell keys only when the literal gain/loss sets in (2.6), rather
   than their signed cardinality, are requested.

The same-gap middle interval remains a joint state: OR and the carrier
transducer are noncancellative, so two endpoint states do not determine it.

## 4. Audited state sizes

For the frozen incumbent the exact counts are

| object | count |
|:--|--:|
| proper-prefix cells | 32,063 |
| distinct full profiles (2.4) | 30,977 |
| incidences from the 249-target shore | 535 |
| distinct projected bitsets (2.5), including empty | 216 |
| distinct nonempty projected bitsets | 215 |
| neighbour cells of lengths (1,2,3) | (7,80,128) |

Thus the full carrier atlas barely compresses by equality, whereas the
witness-directed Hall projection compresses to 216 semantic states.

As a calibration, applying the fixed *pass-1* shore to the two other exact,
all-upper chronologies from the same finite cycle run gives:

| chronology | gains | losses | signed current | residual fixed-shore gap |
|:--|--:|--:|--:|--:|
| `pass_0` SHA `a36eaeff...` | 16 | 0 | +16 | 18 |
| `pass_2` SHA `fdbcc3fb...` | 3 | 0 | +3 | 31 |

Their actual maximum-matching deficiencies are 35 and 35, respectively.
This is a concrete warning that optimizing one shore is a proof-safe filter,
not a substitute for rerunning exact Hall.

## 5. Audit of the blind two-external normal form

The following parts of
`scratch/threadD_k16_j3959_support7_two_external_normal_form_20260730.md`
(SHA `70db93ea...`) survive independent audit:

* the 114 five-edge covers and the unique
  `(Y,C,e_L,e_R)` representation;
* the exact total `9,421,558,172` and intact total `4,281,322,762`;
* the arbitrary-upper OR monoid and the interval-transversal reduction for
  targets with residual witness hitting number at most two; and
* the need for a joint same-gap sweep rather than cancellative endpoint
  subtraction.

One qualification is essential.  A six-gap index plus adjacency to cover
cuts is **not** a lossless topological contact pattern.  External cuts in the
same cover gap can lie on different sides of an uncut forced endpoint, and
separation two creates a forbidden cross-boundary base edge.  Every
implementation must use the stronger `Phi` state proved in
`scratch/threadD_k16_j3959_detached_endpoint_state_compression_20260730.md`:
signed/clipped side and near relations to all local ports and forced-edge
endpoints, together with `min(e_R-e_L,3)`.  Sections 4 and 6 of the blind
normal form are correct only when their phrase `gap/contact port type` is
read as this full `Phi`, not as the shorter prose list.

Likewise, “six masks per side” is exact only with the pending-row transition
state made explicit.  The twelve-row automaton above supplies that missing
implementation contract.

## 6. Scope and next use

The recommended detached search is now witness-directed:

1. enumerate only legal return trees using full `Phi`;
2. enforce exact flat/capacity/envelope reconstruction;
3. enforce arbitrary-width upper coverage;
4. compute (2.7) and reject unless it is at least 34;
5. materialize survivors and rerun the full generalized Hall audit.

No result in this note closes the detached family or proves existence of a
compiler-ready chronology.

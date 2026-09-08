# K16 nested debt: interval transport, endpoint fans, and exact cycle columns

Date: 2026-07-30

Status: unconditional transport/circulation theorem; exact solver-free
primitive-column census; no length-12,873 word in the scoped full-gap
one/two-column family

The global bracket remains

\[
                         12873\le \nu(16)\le12874.
\]

## 1. Two distinct authenticated basins

Two words are used below and must not be conflated.

The current Lane-D two-hole minimum is

```text
scratch/threadD_k16_deletep1_ledger_abridge_o3_20260730/
  threadD_k16_deletep1_ledger_abridge_o3_20260730.best.word
SHA-256 452055e47d7f7c331dfab6cbfef5a88ced2ed9bdfa6cb817a920640628d8b525.
```

Its holes are

\[
P=0x4879\subset Q=0x6879.                              \tag{1.1}
\]

The reorganized one-hole word is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a.
```

Its sole hole is `H=0x2c6d`.  It comes from the different two-hole word
`scratch/k16_ejection_lns_h2_p110_20260730.word` (SHA-256 `5234b771...`),
not from the current Lane-D minimum.  The two basins differ at 2,545 cells.
Only theorem-level geometry is compared between them.

## 2. Exact interval-transport theorem

For a word \(w=(w_0,\ldots,w_{n-1})\), put

\[
\lambda_w(I)=\bigvee_{i\in I}w_i,\qquad
m_w(x)=|\{I:\lambda_w(I)=x\}|,                         \tag{2.1}
\]

where \(I\) ranges over nonempty intervals.  For two equal-length words
\(w,v\), form a directed multigraph on the nonzero masks: every interval with
different old and new labels contributes one arc

\[
                       \lambda_w(I)\longrightarrow\lambda_v(I). \tag{2.2}
\]

Let

\[
\beta_{w,v}(x)=d^+(x)-d^-(x).
\]

### Theorem 2.1 (transport identity and exact feasibility)

For every nonzero \(x\),

\[
\boxed{\beta_{w,v}(x)=m_w(x)-m_v(x).}                 \tag{2.3}
\]

Consequently

\[
\boxed{v\text{ is universal}\iff
       \beta_{w,v}(x)\le m_w(x)-1\quad(0<x<2^k).}     \tag{2.4}
\]

#### Proof

Every interval labelled \(x\) before but not after supplies one outgoing arc;
every interval labelled \(x\) after but not before supplies one incoming arc.
Their difference is (2.3).  The inequality (2.4) is exactly
\(m_v(x)=m_w(x)-\beta_{w,v}(x)\ge1\).  This counts all simultaneous-edit
cross terms and requires no independence assumption.  \(\square\)

### Theorem 2.2 (integral reserve circulation)

Adjoin a hub `rho`.  Force all transport arcs (2.2), add an arc

\[
\rho\to x\quad\hbox{of capacity }m_w(x)-1
\]

for every initially covered \(x\), and an unlimited arc \(x\to\rho\).
Give \(x\to\rho\) lower bound one for every initial hole.  The augmented
digraph has an integral circulation if and only if \(v\) is universal.

Indeed, if \(v\) is universal, use hub flows

\[
a_x=m_w(x)-1,\quad b_x=m_v(x)-1
\]

at an initially covered vertex, and \(a_x=0,b_x=m_v(x)\) at a hole.
Conversely conservation gives

\[
m_v(x)=m_w(x)-a_x+b_x\ge1.
\]

Thus every initial hole consumes one unit of genuine old reserve.  Two
distinct holes require two reserve units even when their masks are nested.
Nestedness can share physical support; it cannot make one interval witness
two different labels.

For any target family \(\mathcal Q\), summing (2.4) gives the exact cut

\[
\beta(\mathcal Q)\le
\sum_{\substack{x\in\mathcal Q\\m_w(x)>0}}(m_w(x)-1)
-|\mathcal Q\cap\mathcal H(w)|.                       \tag{2.5}
\]

For \(P\subset Q\), the natural two positive-mask rows are

\[
\mathcal Q_0=(\downarrow P)\setminus\{0\},\qquad
\mathcal Q_1=(\downarrow Q)\setminus(\downarrow P).  \tag{2.6}
\]

They separate inner service from outer-annulus service.

## 3. Exact nested-fan theorem

Fix nonzero strict masks \(0<S\subset T\) and intervals
\(I\subsetneq J\).

### Theorem 3.1 (fan criterion)

A rewrite \(v\) realizes the nested fan

\[
\lambda_v(I)=S,\qquad\lambda_v(J)=T                 \tag{3.1}
\]

if and only if

\[
\bigvee_{i\in I}v_i=S,qquad
\bigvee_{i\in J\setminus I}v_i\subseteq T,qquad
S\vee\bigvee_{i\in J\setminus I}v_i=T.              \tag{3.2}
\]

Equivalently, the outer shell avoids every bit outside \(T\) and supplies
every bit in \(T\setminus S\).

There is a sharp support formula.  Define

\[
B_S=\{i\in I:w_i\nsubseteq S\},\quad
B_T=\{i\in J\setminus I:w_i\nsubseteq T\},           \tag{3.3}
\]

and let \(G_S,G_T\) be the ORs of the retained cells on the two respective
regions.  With arbitrary nonzero replacement masks, the minimum number of
edited cells which realizes this fixed fan is

\[
\boxed{|B_S|+1_{B_S=\varnothing,G_S\ne S}
       +|B_T|+1_{B_T=\varnothing,S\vee G_T\ne T}.}    \tag{3.4}
\]

All poison cells in \(B_S\cup B_T\) are forced edits.  If one side has no
poison but lacks required bits, one further cell on that side is necessary
and sufficient: assign one edited inner cell the whole of \(S\), and one
edited shell cell \(T\setminus S\).

A useful equivalent corridor form is this: a word contains a nested
\((S,T)\)-fan if and only if some \(S\)-witness lies in a maximal contiguous
\(T\)-submask run whose total OR is \(T\).

## 4. External reserve and ejection chains

For a future portal position \(p\) and a word \(u\), write

\[
m_{\neg p}^u(x)=|\{I:\lambda_u(I)=x, p\notin I\}|.  \tag{4.1}
\]

If the portal destroys every \(p\)-containing witness of \(S,T\), any
preparatory circuit \(w\mapsto w_{\rm prep}\) which leaves the portal fixed
must provide

\[
m_{\neg p}^{w_{\rm prep}}(S)\ge1,\qquad
m_{\neg p}^{w_{\rm prep}}(T)\ge1.                    \tag{4.2}
\]

Raw multiplicity is insufficient: several witnesses may all cross \(p\).
Condition (4.2) is necessary in general.  Under a zero-cross-derivative
shield—for example, when the open gap between the preparation and portal has
fixed OR `0xffff`—let \(\beta_{\rm prep}\) and \(\beta_{\rm portal}\) be
their signed columns against the common source word.  Then (4.2) is
sufficient for the two labels \(S,T\) only together with the exact remaining
reserve inequalities

\[
 \beta_{\rm prep}(x)+\beta_{\rm portal}(x)\le m_w(x)-1
 \qquad(x\ne S,T).                                  \tag{4.3}
\]

Thus even two individually safe shielded columns can fail jointly by
exhausting a third label of multiplicity two.  Without a shield, the union
support is one compound column and must be evaluated directly by (2.3).

More generally, for edited sites \(s_0<\cdots<s_{r-1}\), every affected
interval has a unique first and last edited site.  Grouping left suffix ORs
and right prefix ORs gives at most

\[
                     17^2\binom{r+1}{2}               \tag{4.4}
\]

weighted transport terms.  This is an exact solver-free compound-column
algorithm.  Static columns add exactly if every interval meeting two selected
supports contains a fixed absorbing segment; fixed full-OR gaps suffice.

An ejection chain is therefore a sequence of exact columns, recomputed
statefully unless shielded.  A directed label cycle alone proves nothing:
it may merely return the same debt.  A successful chain must terminate both
hole paths in genuine reserve capacity from Theorem 2.2.

## 5. The four reorganized-H1 portal fans

In the authenticated one-hole word, all displayed fibres are complete:

| portal | replacement family | inner debt and fibre | outer debt and fibre |
|---:|---|---|---|
| `0` | `0x0800 OR s`, `s subset 0x246d` (128) | `0x4879`: `[0,0]` | `0x6879`: `[0,1]` |
| `4489` | `0x0024 OR s`, `s subset 0x2041` (8) | `0x2669`: `[4487,4489]` | `0x2e69`: `[4486,4489]` |
| `6440` | `0x0440 OR s`, `s subset 0x002d` (16) | `0x806d`: `[6440,6440]` | `0xa86d`: `[6438,6440]` |
| `12872` | `0x2c6d` (1) | `0xce61`: `[12871,12872]` | `0xce63`: `[12869,12872]`, `[12870,12872]` |

Every portal installs `H=0x2c6d` and ejects precisely its displayed nested
pair.  The shell increments \(T\setminus S\) are respectively

\[
0x2000,\quad0x0800,\quad0x2800,\quad0x0002.        \tag{5.1}
\]

The last outer label has raw multiplicity two, but both witnesses contain
position `12872`, so its external reserve is zero.  This is the simplest
literal demonstration that occurrence multiplicity and usable reserve differ.

The 153 portal rows and the fact that no portal plus one arbitrary return edit
closes are independently frozen in
`scratch/k16_reorganized_h1_exact_provider_atlas_v2.audit.json` (SHA-256
`b216a9da...`) and
`scratch/k16_reorganized_h1_portal_depth2_to_h1_v2.audit.json` (SHA-256
`a7539f6c...`).

## 6. Current H2 geometry

In the current Lane-D minimum, positions `0,2,6440` contain

\[
0xa86d,\quad0x006d,\quad0x0440.                    \tag{6.1}
\]

Each contains a bit outside \(Q=0x6879\).  If they remain fixed, every
\(P\)- or \(Q\)-witness avoids all three, hence lies in one of

\[
[1,1],\qquad[3,6439],\qquad[6441,12872].              \tag{6.2}
\]

The singleton component cannot contain two distinct fan labels, leaving two
physical fan regions.

The complete arbitrary one-cell provider census has `42,457` columns:

```text
inner only  16,597
outer only  24,568
joint        1,292
```

Every joint column is a literal nested fan.  The minimum remaining-hole count
is one, attained by exactly one column:

```text
p0: 0xa86d -> 0x4879,
gain 0x4879 and 0x6879,
lose 0xa86d.
```

Its decisive transport coordinates are

\[
\beta(0x4879)=\beta(0x6879)=-1,\qquad
\beta(0xa86d)=3.                                     \tag{6.3}
\]

The source has (m(0xa86d)=3), hence reserve capacity only two.  The column
overdraws that capacity by exactly one, explaining the surviving hole without
any heuristic independence argument.

## 7. Exact primitive-column atlas

The new C++ enumerator emits the full signed beta vector for every one-cell
column with at most four exported holes.  It also counts the complete
untruncated primitive atlas, records portal-avoiding inner/outer gains, detects
nested fans, and marks the sufficient fixed-full-gap shield.

| case | all providers | joint | full-gap shielded | minimum exported holes |
|---|---:|---:|---:|---:|
| current H2 | 42,457 | 1,292 | n/a | 1 |
| H1 portal 0 | 44,405 | 1,348 | 14,518 | 2 |
| H1 portal 4489 | 45,955 | 1,013 | 14,654 | 2 |
| H1 portal 6440 | 43,291 | 202 | 42,839 | 0 |
| H1 portal 12872 | 80,234 | 2,240 | 79,322 | 2 |

The portal-6440 exception is exact: there are 25 zero-export columns, all of
which create only the inner reserve `0x806d`.  There is no zero-export outer
or joint column.  The two-level cut (2.6) therefore sees what scalar hole
count misses: the inner ledger can be fortified for free, while the outer
annulus still needs one unit.

For each portal, every retained column of exported-debt size at most four was
then combined with every portal value under a fixed full-gap shield.  Every
shield-compatible pair of distinct retained columns was also tested.  This is
an exact additive calculation, not SAT:

| portal | single tests; minimum | pair geometries/tests; minimum | zeroes |
|---:|---:|---:|---:|
| 0 | 1,280; 3 | 16 / 2,048; 6 | 0 |
| 4489 | 16; 3 | 0 / 0; -- | 0 |
| 6440 | 3,488; 1 | 18,964 / 303,424; 1 | 0 |
| 12872 | 100; 3 | 2,688 / 2,688; 4 | 0 |

The sharp portal-6440 pair still leaves exactly `0xa86d`:

```text
portal p6440 -> 0x0440,
p7984 -> 0x8004,
p9726 -> 0x806d.
```

Both reserve columns serve the inner row; neither pays the outer annulus.
This is a theorem-level explanation of the observed nested-debt shuttle.

## 8. Scope and surviving circuit gate

The census is complete for:

1. every arbitrary one-cell provider of either current-H2 hole;
2. every arbitrary one-cell, portal-avoiding provider of either member of
   each H1 nested pair which preserves the H1 hole;
3. all one- and two-column bundles drawn from the emitted debt-at-most-four
   bank when every interaction is protected by fixed full-OR gaps.

It does not exclude:

* a needed witness containing two or more edited sites (the **joint-only**
  class);
* an unshielded compound column with a favourable cross derivative;
* three or more reserve columns;
* primitive columns exporting five or more debts whose compound sum cancels;
* or an unrelated length-12,873 word.

The exact next mathematical object is therefore not another scalar portal
score.  It is a compound first/last-edited-site column using (4.4), with the
two ideal cuts (2.6) imposed before enumeration.  A positive construction must
either create a joint-only fan or pay the outer-annulus unit through a genuine
reserve sink.

## 9. Authenticated artifacts

```text
C++ source
  scratch/threadD_k16_nested_debt_cycle_columns_20260730.cpp
  SHA-256 cf16c0c434162f2ea19d17cc6a1c0afd5aec0f6d3cd2c8be164e8d2977031931

H100 binary
  scratch/threadD_k16_nested_debt_cycle_columns_20260730/
    threadD_k16_nested_debt_cycle_columns_20260730
  SHA-256 a24ee6c6e3a6919f62092970cde807d205dd53cff03ee543ec7db2050d565ebf

raw exact census
  scratch/threadD_k16_nested_debt_cycle_columns_20260730/
    threadD_k16_nested_debt_cycle_columns_20260730.raw.audit.json
  SHA-256 b2b6f333c4430ee3296bce5795beedfc679ea67e8edd9f0fc1d0e45ddd5ab87e

build/resource provenance
  scratch/threadD_k16_nested_debt_cycle_columns_20260730/
    threadD_k16_nested_debt_cycle_columns_20260730.build.txt
  SHA-256 e1a96e0cd43d6af3b3d024fd165ed49748b7023fb25dc06f44226b68742530fc

independent checker
  scratch/audit_threadD_k16_nested_debt_cycle_columns_20260730.py
  SHA-256 c1ed7e587d95e1a51371a522a3f7384ab20e4c0a8d49ab7f88d95adffd625538

independent audit
  scratch/threadD_k16_nested_debt_cycle_columns_20260730.audit.json
  SHA-256 31bece8b47b582c09b8c4378da9f97f8f948bb0f9b20e7d226e1dfd50730af09
  payload c4cd6a6e60c27d237e6f1ed3b513723cf85579b72d17611e17207b26c40ad0a9
```

The final run was executed in the unique directory
`/home/amodo/or15/work/threadD_k16_nested_debt_cycle_columns_20260730_final`,
not `/dev/shm`.  It used one H100 CPU, a 512 MiB address-space cap, 24,064 KiB
maximum RSS, no swap, and 0.95 seconds wall time.  It exited zero; no resource
or ENOSPC event occurred.

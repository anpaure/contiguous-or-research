# K16 private deficits, orthant MITM, and radius-four portal returns

Date: 2026-07-30

Status: unconditional transport/MITM theorem; exact stateful sharp-return
no-go; no length-12,873 word in the enumerated full-gap three-reserve
families

The finite bracket remains

\[
                         12873\le \nu(16)\le12874.
\]

## 1. Frozen source and scope

The rooted one-hole word is

    scratch/k16_h2_to_h1_p0.h1.word
    SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
    length 12873
    sole hole H=0x2c6d.

It is the reorganized H1 basin, not the current Lane-D H2 word.  Those two
basins differ at 2,545 cells.

A portal plus three reserve columns changes four source positions.  It is
therefore cardinality-disjoint from the completed all-three and
two-site-plus-one radius-three branches.  The one-site portal branch at
radius three is only partially closed: the nested-portal theorem eliminates
its minimum-debt laminar two-blocker family, not every mixed repair.

## 2. Exact absorber-additivity lemma

For a source word \(w\), let

\[
m_w(x)=|\{I:\bigvee_{i\in I}w_i=x\}|,\qquad
\kappa_w(x)=m_w(x)-1.                                  \tag{2.1}
\]

Thus \(\kappa_w(x)=-1\) at a source hole.  A cluster rewrite \(e\) has
signed interval column

\[
\beta_e(x)=m_w(x)-m_{w^e}(x).                           \tag{2.2}
\]

### Lemma 2.1 (partial-edit absorption)

Let \(e_1,\ldots,e_s\) have disjoint supports.  Suppose every interval meeting
at least two supports has the same OR under every partial application of
these edits.  Then

\[
\beta_{\{e_1,\ldots,e_s\}}=\sum_{j=1}^s\beta_{e_j}.     \tag{2.3}
\]

Consequently the combined word is universal if and only if

\[
\boxed{\ \sum_{j=1}^s\beta_{e_j}(x)\le\kappa_w(x)
       \quad\hbox{for every nonzero }x.\ }              \tag{2.4}
\]

#### Proof

Intervals meeting no support do not change.  An interval meeting one support
contributes exactly that cluster's signed column.  By hypothesis every
interval meeting two or more supports contributes zero under every partial
choice.  This proves (2.3); (2.4) is the exact reserve-capacity criterion
\(m_w-\sum_j\beta_{e_j}\ge1\).  \(\square\)

If the open gap between every pair of consecutive selected support clusters
has fixed OR \(0xffff\), the hypothesis holds.  Merely having the same final
OR is not enough: absorption must survive partial applications.

## 3. Private deficits and the orthant MITM

Fix a portal column \(g\).  For two reserve columns \(a,b\), put

\[
r_{ab}(x)=g(x)+a(x)+b(x)-\kappa_w(x),                  \tag{3.1}
\]

and retain its positive deficit signature

\[
D_{ab}=\{(x,r_{ab}(x)):r_{ab}(x)>0\}.                  \tag{3.2}
\]

### Theorem 3.1 (exact third-column orthant)

Under Lemma 2.1, a third reserve column \(c\) closes the pair \(a,b\) if and
only if

\[
\boxed{\ c(x)\le-r_{ab}(x)\quad\hbox{for every }x.\ }   \tag{3.3}
\]

Equivalently, with

\[
K_{ab}=\{\gamma:\gamma(x)\le-r_{ab}(x)\ \forall x\},
\]

the exact question is whether the physically compatible column bank meets
the down-orthant \(K_{ab}\).

If no portal bundle with at most two reserve columns is universal, then in
every successful minimal triple:

1. \(D_{ab}\ne\varnothing\) for each omitted column \(c\);
2. \(c(x)\le-r_{ab}(x)<0\) at some \(x\in D_{ab}\);
3. the analogous statement holds after omitting \(a\) or \(b\).

Thus every selected column carries a genuine private reserve unit needed by
the other pair.  The three labels may coincide, but the integral units do
not.  In particular, nesting does not turn three reserve obligations into
fewer units.

#### Proof

Equation (3.3) is (2.4) after moving \(g+a+b\) to the right.  If
\(D_{ab}\) were empty, \(g+a+b\) would already be feasible, contrary to the
minimality hypothesis.  Feasibility of \(g+a+b+c\) then forces \(c\) to pay
every positive coordinate of \(r_{ab}\).  Repeat for the other omissions.
\(\square\)

This gives a solver-free meet-in-the-middle algorithm:

1. enumerate compatible unordered pairs \((a,b)\);
2. store sparse signatures \(D_{ab}\);
3. intersect postings

   \[
   L(x,d)=\{c:c(x)\le-d\}
   \]

   over \((x,d)\in D_{ab}\);
4. check physical separator compatibility and all coordinates of (3.3).

The two nested-ideal rows

\[
(\downarrow P)\setminus\{0\},\qquad
(\downarrow Q)\setminus(\downarrow P)
\]

are safe dominance prescreens.  They never replace the coordinatewise
test.

### Corollary 3.2 (service localization)

Suppose \(P<Q<0xffff\) have no portal-avoiding source witnesses.  In a
full-gap-separated bundle, every final \(P\)- or \(Q\)-witness lies inside
one reserve cluster.  Hence service has exactly two forms:

* split: an individual inner provider and an individual outer provider,
  followed by an arbitrary compensator;
* joint: one individual joint provider followed by two compensators.

A fan whose \(P,Q\) witnesses genuinely need several clusters is an
unshielded compound-column phenomenon, not an additive one.

## 4. Exact relation to the radius-three theorems

The authoritative rooted-H1 radius-three theorem proves no completion when
the final \(H=0x2c6d\) witness uses all three edits, or exactly two edits plus
an arbitrary third.  It exhausts 105,510,990 ordered two-site assignments
and 9,667,813 exact third values in the latter branch.

The one-site-portal theorem now also closes every genuinely joint repair
pair: it rebuilds 28,805 exact portals, reduces 372,365,874 raw positional
supports to 49,390 structurally feasible supports, and exhausts 144,191,783
exact value pairs with no completion.  This strictly contains the earlier
1,341-support minimum-debt laminar two-blocker theorem.

The exact surviving radius-three class is mixed provider-repair: after the
one-site portal, at least one repair individually supplies a portal debt,
while some debt lacks a final witness containing both repair cells.  The
radius-four results below neither close nor infer anything about that class;
they begin with four distinct source edits.

## 5. Debt-at-most-four provider-only triple census

The first exact engine joins a pair and a third column from the audited
debt-at-most-four external \(P/Q\)-provider atlas.  It admits only
four-position full-gap chains and checks every portal value using (2.4).

| portal | retained rows | pair bank | triple geometries | capacity tests | minimum |
|---:|---:|---:|---:|---:|---:|
| 0 | 28 | 196 | 0 | 0 | -- |
| 4489 | 84 | 164 | 0 | 0 | -- |
| 6440 | 266 | 29,428 | 884,044 | 14,144,704 | 1 |
| 12872 | 132 | 5,888 | 25,600 | 25,600 | 7 |

There is no completion.  At portal 6440 there are 1,024 one-hole rows; the
recorded minimum leaves \(0xa86d\).  One recorded minimum is

    portal 6440 -> 0x0441
    6606 -> 0x0004
    7984 -> 0x8004
    9726 -> 0x806d.

This result is exact for the stated provider-only bank.  It does not include
an arbitrary non-\(P/Q\) compensator and is therefore not the complete
three-reserve problem.

The independent audit reconstructs every pair/triple geometry, checks the
test and histogram arithmetic, and literally replays both reported minima.
It does not repeat the native engine's 14,170,304 individual capacity joins.

The one-CPU H100 run used a 1 GiB address-space cap, 40,540 KiB maximum RSS,
no swap, and 29.95 seconds wall time.  It ran in

    /home/amodo/or15/work/threadD_k16_nested_debt_three_column_mitm_20260730

and did not use /dev/shm.

## 6. Sharp stateful fourth-edit theorem

Materialize the sharp three-edit state

    6440: 0x806d -> 0x0440
    7984: 0x80c4 -> 0x8004
    9726: 0x006d -> 0x806d.

It has sole hole

\[
                              A=0xa86d.                \tag{6.1}
\]

### Theorem 6.1 (complete sharp-state return census)

No arbitrary one-cell substitution completes this state.

#### Proof

Any completion must create an \(A\)-interval through its changed cell.  At a
position \(t\), let \(C_t(A)\) be the OR of the maximal consecutive
\(A\)-submask corridor on both sides of \(t\).  The exact candidate values are

\[
                  A\setminus C_t(A)\ \subseteq z\subseteq A,              \tag{6.2}
\]

excluding zero and the incumbent.  This enumerates every possible new
\(A\)-witness.  Fresh one-cell interval deltas test the complete fibre.

There are 29,029 candidates and zero completions.  Of these, 28,853 use a
genuinely fourth position.  Their minimum is two holes, attained by exactly
81 rows:

| position | values | residual pair |
|---:|---:|---|
| 0 | 64 | \(\{0x4879,0x6879\}\) |
| 10005 | 16 | \(\{0xa86e,0xaa6e\}\) |
| 12872 | 1 | \(\{0xce61,0xce63\}\) |

The remaining 176 candidates overwrite a sharp site.  Their 16 minima merely
change position 6440 into the reverse portal fibre and return to sole hole
\(H=0x2c6d\).  Thus the stateful one-cell escape is an exact three-way nested
debt shuttle, not a closure.  \(\square\)

The independent checker reconstructs the maximal-corridor fibre and every
one-cell delta; its histograms and digest match the native engine exactly.
The remote run used a 512 MiB cap, 21,504 KiB maximum RSS, no swap, and
0.06 seconds.

## 7. The minimal split fan: \(I_0+O_2+\) arbitrary return

At portal 6440 the smallest split service strata are:

* \(I_0\): a zero-export inner-only column;
* \(O_2\): an exactly-two-debt outer-only column.

There are 25 \(I_0\) columns and 81 \(O_2\) columns.  Every one of the
\(25\cdot81=2,025\) service pairs has the required three-position full-gap
geometry.  Across all 16 portal values this gives 32,400 partial states.

For a partial deficit family \(\mathcal D\) and a return position \(t\), put

\[
U(\mathcal D)=\bigcap_{T\in\mathcal D}T,\qquad
L_t(\mathcal D)=
  \bigvee_{T\in\mathcal D}\bigl(T\setminus C_t(T)\bigr),                 \tag{7.1}
\]

where \(C_t(T)\) is the OR of the maximal source \(T\)-submask corridor on
both sides of \(t\).

### Lemma 7.1 (exact common-provider interval)

A single value \(z\) creates a witness for every \(T\in\mathcal D\) if and
only if

\[
\boxed{\quad L_t(\mathcal D)\subseteq z\subseteq U(\mathcal D).\quad}     \tag{7.2}
\]

#### Proof

If a \(T\)-witness through \(t\) exists, extending it throughout the maximal
\(T\)-compatible corridor keeps its OR inside \(T\).  Therefore \(z\) must
contain every bit of \(T\setminus C_t(T)\) and no bit outside \(T\).
Intersect these conditions over \(T\).  Conversely, (7.2) makes the maximal
corridor together with \(z\) have OR exactly \(T\) for every target.
\(\square\)

All six deficit families in this census are non-FULL.  Under the admitted
full-gap geometry, none of their witnesses can cross another edit.  Hence the
unchanged source corridors in (7.1) are exact.

### Theorem 7.2 (minimal split-fan no-go)

No portal-6440 bundle consisting of one \(I_0\) column, one \(O_2\) column,
and one arbitrary common-provider return is universal when the four distinct
sites are separated by fixed full-OR gaps.

The exact ledgers are

    pair states                         32,400
    distinct deficit sets                   6
    common-provider return rows          7,414
    return rows considered          39,166,400
    full-gap compatible joins       12,191,824
    universal joins                          0
    minimum final holes                      3.

The sharp minimum is

    6440:  0x806d -> 0x0440
    7984:  0x80c4 -> 0x8004
    9968:  0xac60 -> 0xa868
    10005: 0xa80e -> 0x0801

and leaves the nested chain

\[
                       0xac60\subset0xac66\subset0xae66.                 \tag{7.3}
\]

The independent audit reconstructs all 106 selected service columns, all six
common-provider banks, all 12,191,824 compatible joins, and the literal best
word.  It checks the producer's minimum/no-zero histogram arithmetically but
does not independently repeat every final capacity test.

The one-CPU H100 run used a 512 MiB cap, 24,496 KiB maximum RSS, no swap, and
67.45 seconds wall time.  It ran in

    /home/amodo/or15/work/threadD_k16_p6440_i0_o2_return_mitm_20260730

and did not use /dev/shm.

## 8. Exact surviving gate

The earlier-cardinality mixed provider-repair radius-three class described
in Section 4 remains open.

The minimal split signature \((I_0,O_2)\) is now closed.  Any successful
shielded portal-6440 split triple must therefore leave this lowest stratum:

1. \(I_0+O_3\) or \(I_0+O_4\), followed by an arbitrary return;
2. \(I_{\ge1}+O_{\ge2}\), followed by an arbitrary return;
3. a higher-debt service column omitted from the retained bank.

The joint branch first appears outside the retained bank: portal 6440 has 202
joint primitive providers overall but none with at most four exported holes.
For a fixed joint column \(j\), define

\[
K_j=\{\gamma:\gamma(x)\le
       \kappa_w(x)-g(x)-j(x)\ \hbox{for every }x\}.                    \tag{8.1}
\]

It requires the geometry-compatible two-return Minkowski query

\[
                  (\mathcal C+\mathcal C)\cap K_j\ne\varnothing.       \tag{8.2}
\]

At portals 0 and 4489 the provider-only result is vacuous because the
retained bank has no admissible full-gap triple geometry.  At portal 12872
the minimum seven is only within that retained bank.  Arbitrary nonprovider
returns, higher-debt service columns, and unshielded forms remain open at
all three portals.

The unshielded \([1,1,1,1]\) class also remains a compound/open problem,
because its singleton columns need not add.  Beyond it, the first partitions
containing a multi-site atomic packet are

\[
                      [2,1,1],\quad[2,2],\quad[3,1],\quad[4].
\]

For four edited sites, first/last-site compression uses at most

\[
                    17^2\binom{5}{2}=2,890
\]

weighted transport terms per compound support.

In the distinct current-H2 basin, the unique joint bridge has the schematic
ledger

\[
             (0x4879,0x6879)\longrightarrow0xa86d
             \longrightarrow D\longrightarrow\hbox{hub}.               \tag{8.3}
\]

The sharp stateful census proves one literal realization shuttles into three
nested two-debt fibres.  It does not close every realization of (8.3).

No statement here excludes an unrelated length-12,873 word or changes the
global bracket.

## 9. Authenticated artifacts

Common H100 build/run provenance:

    scratch/threadD_k16_three_reserve_h100_build_provenance_20260730.txt
      SHA 795f19d7738bcb99ca1ae192608275808c0d874bacca31f14dcd9edfaec413e6

Radius-three scope anchors:

    MATH_THEOREM_K16_EJECTION_H1_NONLAMINAR_RADIUS3_TWO_BRANCHES_20260730.md
      SHA fe88bfb3cf8bc647966f19f0e0268d71dc28d166730d3738ff3acdef9873158d
    MATH_THEOREM_K16_NESTED_PORTAL_NORMAL_FORM_AND_INTERACTING12_NOGO_20260730.md
      SHA f432c830995601ef14f10d0d610e5751c708ac1a9c113474347934c8b7218abb

Provider-only triple engine:

    scratch/threadD_k16_nested_debt_three_column_mitm_20260730.cpp
      SHA d4d5950c4cf45daeb7211e874588efc9acb274ba8e611a65539bd61bc357403f
    scratch/threadD_k16_nested_debt_three_column_mitm_20260730/
      threadD_k16_nested_debt_three_column_mitm_20260730
      SHA d8df522d6ff4351911ffc1f3687fbc3172e1f486877be354fda41348f21c1854
      threadD_k16_nested_debt_three_column_mitm_20260730.raw.audit.json
      SHA 06430fc9c24ea03aed0cdf847cfba592236f1c3be58c76a9a9073cdbb72dd88c
      threadD_k16_nested_debt_three_column_mitm_20260730.resource.txt
      SHA d4aa9368fdbb63cd26227c795a17990afa228da3596bfbcfc7d0aa487150a69c
    scratch/audit_threadD_k16_nested_debt_three_column_mitm_geometry_20260730.py
      SHA 195e5d6b665189eb398dc7f2e36ea07de48ac69723c08014743139450095df62
    independent audit
      SHA 13e186ddf267c340fef9aa6361540ef56327c4cc778a3600bbe2ae0e4023e506
      payload 571630827d6ac6d27dc4feb0b80221b448faea29816dccb4569a95e9eef3b710

Sharp-state return:

    scratch/threadD_k16_sharp_h1_three_edit_state_return_census_20260730.cpp
      SHA e9a0d0127c7bf99e9bdd165f6425f9e59ecf350a3e4d303a57c53d5ef1d74574
    primary raw audit
      SHA 5c12b3cb8d4bac617cd7d9becacf15ccf94adc1aa02407ef960e6f094780cf7d
    scratch/audit_threadD_k16_sharp_h1_three_edit_state_return_census_20260730.py
      SHA e0e0c93cf9e393177673879fad15760daca93b18d5a8dc5733ae7443bd3c14b7
    independent audit
      SHA 335cb1f3e3052605003db79e7c3c5150fdbc211fc1ed69f77e78e68d12f5ef06
      payload 1175134bbf2c1234d254527cd091bd3fbb8b6fdbb878180732ee50497297cffa

Minimal split-fan MITM:

    scratch/threadD_k16_p6440_i0_o2_arbitrary_return_mitm_20260730.cpp
      SHA 3d3d6ae1396aa8fca135b15ca7e198d5a1a847768375292bff0f372aac5d9d84
    producer binary
      SHA 64e2c4789d1d8d1a734eb26cfd460c18b3abac8be7e84177b9bcf2b578e7724c
    producer raw audit
      SHA a408da8da473490c9a8c7b8f0e2c21e764898ea31415d0897042530447bafb88
    producer resource
      SHA 84388e089f0385a558ec76c3d332cfc4bee8c911d0cd2af71affd946d51a4a00
    scratch/audit_threadD_k16_p6440_i0_o2_return_mitm_independent_20260730.py
      SHA 30054da89283696f09e7b55d02bbfecae4a2e01b8e41fa3357ad92e52233730a
    independent audit
      SHA 4239a111b1e4df9030b4e28836d3f4b2d24f4f2e34b470a92d93d2c3b1f9daf1

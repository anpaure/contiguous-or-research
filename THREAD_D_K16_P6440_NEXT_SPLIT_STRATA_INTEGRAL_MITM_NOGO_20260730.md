# K16 p6440 next split strata: integral MITM no-go

Date: 2026-07-30

Status: exact solver-free no-go for the two next shielded
debt-at-most-four service strata, each followed by one arbitrary one-cell
return; no global radius-four or K16 no-go

The finite bracket remains

\[
                         12873\le \nu(16)\le12874.
\]

## 1. Frozen source and exact scope

The source is

    scratch/k16_h2_to_h1_p0.h1.word
    SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
    length 12873
    sole hole H=0x2c6d.

The portal is position 6440 with all 16 values in its exact fibre.  An
\(I_d\) column is a full-gap-shielded, inner-only, one-cell column in the
frozen external-reserve atlas which exports exactly \(d\) holes.  The
definition of \(O_e\) is analogous for outer-only columns.  Only atlas rows
with at most four exported holes are used.

This note exhausts exactly

\[
 \boxed{I_0+O_3+R,\quad I_0+O_4+R,\quad
        I_d+O_e+R\ (1\le d\le4,\ 2\le e\le4),}            \tag{1.1}
\]

where \(R\) is an arbitrary one-cell return generated from the complete
common-provider interval.  The four sites must be distinct, and every open
gap between consecutive sites in source order must have OR \(0xffff\).

The previously completed \(I_0+O_2+R\) stratum is not repeated.  The present
scope is disjoint from the mixed radius-three provider-repair branch and
from the joint13 CNF lane.

## 2. Integral column criterion

For a word \(w\), let

\[
 m_w(x)=|\{I:\bigvee_{i\in I}w_i=x\}|,
 \qquad \kappa_w(x)=m_w(x)-1.                            \tag{2.1}
\]

For a one-cell rewrite \(e\), use the signed interval column

\[
                 \beta_e(x)=m_w(x)-m_{w^e}(x).           \tag{2.2}
\]

The fixed-full-gap hypothesis makes every interval meeting two edited sites
have OR \(0xffff\) before and after every partial application.  Hence the
four source-relative columns add exactly.  If \(g,a,b\) are the portal and
two service columns, put

\[
 r_\sigma(x)=g(x)+a(x)+b(x)-\kappa_w(x),
 \qquad
 D_\sigma=\{(x,r_\sigma(x)):r_\sigma(x)>0\}.             \tag{2.3}
\]

An admissible return column \(c\) completes the state if and only if

\[
              \boxed{c(x)\le-r_\sigma(x)\quad\forall x.} \tag{2.4}
\]

The native engine tests (2.4) on the full 65,536-coordinate sparse union.
In particular, it explicitly restores the unit deficit at the source hole
when signed sparse entries cancel to zero.

## 3. Complete common-provider return bank

For a non-FULL target \(T\) and possible return position \(t\), let
\(C_t(T)\) be the OR of the maximal consecutive source \(T\)-submask
corridor on both sides of \(t\), excluding the incumbent at \(t\).  For the
positive-support projection

\[
                 \mathcal D_\sigma=\{x:r_\sigma(x)>0\},
\]

define

\[
 U(\mathcal D)=\bigcap_{T\in\mathcal D}T,
 \qquad
 L_t(\mathcal D)=
   \bigvee_{T\in\mathcal D}\bigl(T\setminus C_t(T)\bigr).              \tag{3.1}
\]

### Lemma 3.1 (exact return interval)

If a one-cell return at \(t\) pays every positive deficit, then its new value
\(z\) lies in

\[
                   L_t(\mathcal D)\subseteq z\subseteq U(\mathcal D).
                                                                        \tag{3.2}
\]

Conversely, every nonzero \(z\) in (3.2) creates a through-\(t\) witness of
every member of \(\mathcal D\).  It is a completing return exactly when its
full signed column also satisfies (2.4).

#### Proof

A deficit-paying return has negative signed incidence at every positive
deficit, so at least one gained occurrence uses \(t\).  Such an occurrence
contains no bit outside its target and must contribute every bit absent from
the unchanged maximal corridor.  Intersecting those upper conditions and
joining those lower conditions gives (3.2).  Conversely, the maximal
corridor together with \(z\) has OR exactly \(T\) for every target \(T\).
Net multiplicity loss elsewhere is not inferred from witness existence; it
is retained literally in (2.4).  \(\square\)

Equivalently, with left/right source group multiplicities \(\ell_t,\rho_t\),

\[
 N_{t,z}(x)=\sum_{u\vee z\vee v=x}\ell_t(u)\rho_t(v),
 \qquad
 \beta_{t,z}(x)=N_{t,w_t}(x)-N_{t,z}(x).                 \tag{3.3}
\]

Every observed positive demand in (1.1) is exactly one.  Thus the
private-reserve-unit filter is simply \(\beta_{t,z}(x)\le-1\) for every
\(x\in\mathcal D\), followed by the full test (2.4).  This is the integral
MITM posting criterion, not a fractional or Boolean-hole proxy.

## 4. Sharp dominance theorem

Let \(\Gamma_\sigma\) be the set of return positions making a four-site
full-gap chain with state \(\sigma\).

### Lemma 4.1 (profile/geometry dominance)

If

\[
        r_\tau\le r_\sigma\quad\hbox{coordinatewise},
        \qquad \Gamma_\tau\supseteq\Gamma_\sigma,        \tag{4.1}
\]

then every return completing \(\sigma\) also completes \(\tau\).

This dominance has a sharp degeneracy.  Every equal-length rewrite preserves
the total number of intervals, so

\[
                       \sum_x\beta_e(x)=0.               \tag{4.2}
\]

Therefore \(r_\tau-r_\sigma\) also has coordinate sum zero.  The first
inequality in (4.1) forces

\[
                         r_\tau=r_\sigma.                 \tag{4.3}
\]

Thus strict full-coordinate Pareto dominance is impossible.  The only safe
dominance quotient is exact signed-profile equality together with containment
of the complete physical return set.  Hole count, hole set, provider side,
or a projected nested-ideal inequality is not sufficient.

The independent pre-audit confirms that all 218 retained shielded primitive
columns have distinct exact signed profiles and that there are zero strict
coordinatewise dominance pairs.  Their 106 ordered service-position pairs
induce 104 spatial bases and 62 exact \(\Gamma\)-classes.  Class
multiplicities are

\[
               1^{37}2^{17}3^3 4^2 5^1 6^1 7^1,          \tag{4.4}
\]

with 6,345 through 12,793 allowed return positions.

Residual-support and base-position grouping below is only a complete
candidate-bank cache.  It never identifies two signed states: every raw
state which survives the private-unit and geometry filters receives its own
exact capacity test.

## 5. Complete service stratification

The shielded retained banks have

\[
 |I_0|=25,quad (|I_1|,|I_2|,|I_3|,|I_4|)=(1,11,19,25),
\]

and

\[
                         (|O_2|,|O_3|,|O_4|)=(81,32,24).
\]

After the three-site full-gap test, the exact service-pair table is

| stratum | \(O_2\) | \(O_3\) | \(O_4\) |
|---|---:|---:|---:|
| \(I_0\) | 2,025, previously closed | 800 | 584 |
| \(I_1\) | 81 | 32 | 24 |
| \(I_2\) | 826 | 352 | 256 |
| \(I_3\) | 1,539 | 608 | 456 |
| \(I_4\) | 1,513 | 768 | 344 |

Hence the new census has

\[
 1,384+6,799=8,183\text{ service geometries},
 \qquad 16\cdot8,183=130,928\text{ portal/service states}.             \tag{5.1}
\]

No retained shielded debt-at-most-four row is joint.  This matters: (1.1) is the
complete next *split* stratum, not a claim about high-debt joint providers.

## 6. Family A: \(I_0+O_{3,4}+R\)

There are 1,400 raw service pairs.  Exactly 1,384 pass the three-site
geometry, giving 22,144 portal/service states.  They have unit demands and
only eight distinct positive supports:

| positive support | states | raw return rows | unit-eligible | exact tests |
|---|---:|---:|---:|---:|
| \(\{346d,6879,766d\}\) | 2,176 | 46 | 8 | 0 |
| \(\{346d,6879,766d,846d\}\) | 1,024 | 0 | 0 | 0 |
| \(\{846d,aa69,ab69,eb69\}\) | 2,048 | 0 | 0 | 0 |
| \(\{846d,b06d,b07d,b27d\}\) | 2,048 | 0 | 0 | 0 |
| \(\{846d,c86c,c86d,c96d,d96d\}\) | 2,048 | 0 | 0 | 0 |
| \(\{aa69,ab69,eb69\}\) | 4,352 | 1,616 | 1,331 | 4,264,960 |
| \(\{b06d,b07d,b27d\}\) | 4,352 | 1,092 | 847 | 2,254,336 |
| \(\{c86c,c86d,c96d,d96d\}\) | 4,096 | 376 | 315 | 765,952 |

The 46-row bank has no full-gap-compatible return.  Four other supports have
empty banks; only the last three rows reach the capacity test.  Thus the
exact ledger is

    raw common-provider rows considered       13,425,408
    integral-unit eligible state/rows         10,786,304
    geometry-compatible exact tests            7,285,248
    universal joins                                    0
    eligible-return minimum holes                       8.

The complete final histogram is

\[
\begin{array}{c|rrrrrrrrrrrr}
h&8&9&10&11&12&13&14&15&16&17&18&19\\ \hline
N_h&1561856&78080&1013760&1137408&996352&918016&1035264&
479232&26112&21760&8704&8704.
\end{array}                                                     \tag{6.1}
\]

One sharp eligible-return minimizer is

    1407:  0x6540 -> 0xaa69
    6440:  0x806d -> 0x0440
    7984:  0x80c4 -> 0x8004
    9958:  0x2a01 -> 0x0804

and has the literal residual

\[
 \{6540,6748,6750,6758,6768,7550,7554,7750\}.             \tag{6.2}
\]

## 7. Family B: \(I_{\ge1}+O_{\ge2}+R\)

The 7,672 raw pairs reduce to 6,799 full-gap service geometries and 108,784
portal/service states.  Their exact pair table is the lower four rows of
Section 5.  They produce 111 unit-deficit supports.

Exactly 110 supports have an empty common-provider bank.  The sole live
support is

\[
                         \{802d,b06d,b07d,b27d\}.          \tag{7.1}
\]

It occurs in 256 states and has six raw return rows, all with value
\(0x802d\), at positions

\[
                 5931,5932,5934,12369,12370,12372.        \tag{7.2}
\]

Positions 12369 and 12370 fail the integral-unit test; 12372 pays the units
but fails the four-site geometry.  Thus exactly three rows per state remain:

    raw rows considered          1,536
    integral-unit eligible       1,024
    exact full-gap tests            768
    universal joins                  0
    eligible-return minimum         13.

The final histogram is \(13^{512}14^{256}\).  One literal minimum is

    5931:  0x2069 -> 0x802d
    6440:  0x806d -> 0x0440
    6769:  0x802d -> 0x806d
    12371: 0x9060 -> 0x0840

and leaves

\[
\{2079,207d,2279,227d,22f9,23f9,23fd,
  306d,307d,327d,386d,387d,3c6d\}.                       \tag{7.3}
\]

## 8. The exact no-go and remaining gate

### Theorem 8.1 (next shielded split-stratum no-go)

No word in the exact family (1.1) is universal.

#### Proof

Sections 2 and 3 give a necessary-and-sufficient integral return criterion.
The census includes every retained service pair in the declared strata,
every one of the 16 portal values, and every one-cell return value in the
complete Boolean interval (3.2).  The reserve-unit filter removes only rows
which cannot pay a positive deficit.  The full-gap filter is exactly the
declared physical scope.  Every surviving row is tested by (2.4), producing
the exhaustive histograms in Sections 6 and 7, neither of which contains
zero.  \(\square\)

The theorem does not exclude:

1. a service column exporting more than four holes;
2. a high-debt joint provider;
3. an unshielded four-site interaction whose signed columns do not add;
4. a multi-cell service packet or multi-cell return;
5. another portal, source basin, or unrelated length-12,873 word;
6. the still-open mixed provider-repair radius-three class.

Thus the next additive escape must leave the entire retained
debt-at-most-four split atlas, not merely the old \(I_0+O_2\) row.

## 9. Reproducibility and audit scope

The one-process H100 run used one CPU and only

    /home/amodo/or15/work/threadD_k16_p6440_next_split_strata_20260730

with a 512 MiB address-space cap.  Compilation used 284,956 KiB maximum RSS.
The exact run used 136,612 KiB maximum RSS, no swap, and 12.72 seconds wall
time.  Neither stage wrote to `/dev/shm`.

The independent precheck consumes, and hash-binds, the frozen retained
service atlas; it does not regenerate that atlas's provider enumeration.  It
independently rebuilds source interval multiplicities, portal columns, every
support/common-provider bank and geometry ledger, and all 768 Family-B
capacity tests.  The final checker checks histogram arithmetic and literally
replays both minima.  It deliberately does not repeat the 7,285,248 Family-A
final capacity outcomes; that no-zero ledger rests on the audited native loop
plus the independent structure/accounting and literal-minimum replay.

Authenticated artifacts:

    scratch/threadD_k16_p6440_next_split_strata_mitm_20260730.cpp
      SHA 5125dcddd5185f9799297227d79b77eb781e44815c1c91c93259dfb834893ba1
    scratch/threadD_k16_nested_debt_cycle_columns_20260730.cpp
      SHA cf16c0c434162f2ea19d17cc6a1c0afd5aec0f6d3cd2c8be164e8d2977031931
    frozen retained-column atlas
      scratch/threadD_k16_nested_debt_cycle_columns_20260730/
        threadD_k16_nested_debt_cycle_columns_20260730.raw.audit.json
      SHA b2b6f333c4430ee3296bce5795beedfc679ea67e8edd9f0fc1d0e45ddd5ab87e
    producer binary
      SHA 17bb343b72fe5f8c37b831ee1fb0b06d49ad59dd88fca4732f13c9c71ffc4151
    producer raw audit
      SHA 23bc772920d8974c3a0f298cea32b880c352c0af9cceffc13d7dd07c7b263b2c
    Family-A best word
      SHA eeeef8e209b611d6aa0ac6e78528dde41bb1a204046ee1dd05e65bb83334800b
    Family-B best word
      SHA 3fac278420d95d601da95538977f521d246f05632c48b47f0dffd23246d71931
    run resource
      SHA fccbb43b24aa095a4fb73a2e845d76b0a8148f4f52c9d7362be6eb9d5ed88ead
    compile resource
      SHA 8659266b423dd43187cc57954e82d0d1aa8ae21af6c628290419c47de8cca89f
    launch provenance
      scratch/threadD_k16_p6440_next_split_strata_mitm_20260730.provenance.txt
      SHA 28b362ae631a37815ccd31fc79e8a602a237cba9342735f03564f5092330a0c1
    scratch/audit_threadD_k16_p6440_next_stratum_precheck_20260730.py
      SHA 0f2142a59613b74ce11afcb858c27f2f40980da4ddb28c22becf778033bde84c
    pre-audit
      SHA 9fdc09c758a906d67fbdd2bf8da5c362a18e4d4a5edada49a0b419fbe85136e4
    scratch/audit_threadD_k16_p6440_next_split_strata_mitm_independent_20260730.py
      SHA c33feac9ae778963d2833c37c18adb81bf493cce60512ccc6655e9c28aa1c42e
    independent audit
      SHA 83ffdc5a6a7c41d9e0270c99335f5f42636fd455ba4e87bce623fe28d86104b0
      payload 980126a4cb5b9cf6ce27e47e3e18d35b42dccfeb59fb7d976e35e050cfdf2dd2

# Lane K: exact compressed pair-cover master and simultaneous immediate-shadow factor

Date: 2026-07-29

Status: unconditional quotient theorem and independently replayed finite
certificate for \(k=15\). The compressed master is exact, and it contains a
\(\mathbb Z_{15}\)-equivariant spanning \(2\)-factor with squarefree middle and
lower-\(q1\) palettes, complete lower \(q2\), and complete upper \(q1\).
The retained factor is disconnected, has residence minimum two, is not at the
collision floor, and fails deeper-shadow tests. The compiler was not run.
Thus this note discharges the static simultaneous pair-cover gate only; it
does not produce a contiguous-OR word or improve the rigorous bound on
\(\nu(15)\).

## 1. The voltage-labelled quotient

Let \(\Omega=\mathbb Z_{15}\), let \(\rho:x\mapsto x+1\), and put

\[
 \mathcal L={\binom{\Omega}{7}}/\langle\rho\rangle,
 \qquad
 \mathcal U={\binom{\Omega}{8}}/\langle\rho\rangle.
\]

No nonidentity power of \(\rho\) fixes a rank-seven or rank-eight set. Indeed,
the cycles of such a power all have a common length in \(\{3,5,15\}\), while
neither \(7\) nor \(8\) is divisible by that length. Therefore

\[
 |\mathcal L|=|\mathcal U|={1\over15}{15\choose7}=429.       \tag{1.1}
\]

Let \(Q\) be the quotient of the rank-seven/rank-eight inclusion graph. Its
edges retain their voltage: an edge record is

\[
 e=(L_e,a_e,U_e,\lambda_e),
 \qquad L_e\cup\{a_e\}=\rho^{\lambda_e}U_e.     \tag{1.2}
\]

At sheet \(s\), this edge joins \(\rho^sL_e\) to
\(\rho^{s+\lambda_e}U_e\). Parallel quotient endpoints with different
voltages are distinct edges. The incidence action is free, so \(Q\) is
eight-regular on both shores and

\[
 |E(Q)|=429\cdot8=3432.                         \tag{1.3}
\]

The complete catalogue has 3,418 unordered endpoint pairs: 3,404 have one
edge orbit and 14 have two voltage-distinct edge orbits. No endpoint pair
has larger multiplicity. Keeping the edge ID or voltage is therefore
essential.

## 2. Exact \(56\to8\to28\) local compression

Fix \(U\in\mathcal U\). Align an incident edge \(e\) to the canonical
\(U\)-frame by

\[
 X_U(e)=\rho^{-\lambda_e}L_e\subset U.          \tag{2.1}
\]

The eight incident edge IDs give exactly the eight lower neighbours
\(U\setminus\{a\}\). In the uncompressed choice-incidence representation,
each of these eight neighbours occurs in seven candidate turns, producing
\(8\cdot7=56\) incidences. Pairing those 56 incidences indiscriminately
would create

\[
 429{56\choose2}=660660                         \tag{2.2}
\]

raw syntactic witnesses before implementation-specific admissibility
filters, explaining the previously quoted roughly 658,000-witness scale.
That layer records the far endpoint choice redundantly at the middle vertex;
the shared incidence channel recovers it exactly at the rank-seven shore.
The correct local middle state is therefore only an unordered pair of
distinct aligned neighbours, hence only \({8\choose2}=28\) turns.

Introduce an edge bit \(e_a\) for the neighbour \(U\setminus\{a\}\) and a
turn bit \(y_{ab}=y_{ba}\) for each \(\{a,b\}\subset U\). The exact local
equations are

\[
 \sum_{\{a,b\}\subset U}y_{ab}=1,
 \qquad
 e_a=\sum_{b\ne a}y_{ab}.                       \tag{2.3}
\]

They imply \(\sum_a e_a=2\). Conversely, any binary vector \(e\) with
exactly two ones determines the unique turn \(y_{ab}=e_ae_b=1\). Thus
(2.3) is precisely the requested linearization of

\[
 e_a=\operatorname{OR}_{b\ne a}y_{ab},
 \qquad y_{ab}=e_a\mathbin{\mathrm{AND}}e_b,    \tag{2.4}
\]

with no relaxation and no loss of voltage information.

The selected turn has the literal lower-\(q2\) colour

\[
 \kappa_-(U,\{e,f\})
 =\operatorname{can}_\rho(X_U(e)\cap X_U(f))
 =\operatorname{can}_\rho(U\setminus\{a,b\}).  \tag{2.5}
\]

Dually, at \(L\in\mathcal L\), two incident upper neighbours in the common
\(L\)-frame have union

\[
 \kappa_+(L,\{e,f\})
 =\operatorname{can}_\rho(L\cup\{a_e,a_f\}),   \tag{2.6}
\]

the literal upper-\(q1\) colour.

## 3. The compressed global master is exact

For each quotient edge \(e\), introduce \(x_e\in\{0,1\}\). At each of the
858 quotient vertices introduce one binary variable for each of its 28
incident-edge pairs. Write these as \(y^U_{U,p}\) and \(y^L_{L,p}\). Impose

\[
 \sum_p y^U_{U,p}=1,
 \qquad
 \sum_p y^L_{L,p}=1,                            \tag{3.1}
\]

and, for every incidence edge \(e=LU\),

\[
 x_e=\sum_{p\ni e}y^U_{U,p}
     =\sum_{p\ni e}y^L_{L,p}.                  \tag{3.2}
\]

### Theorem 3.1 (factor bijection)

The binary solutions of (3.1)--(3.2) are in bijection with the
\(\rho\)-invariant spanning physical \(2\)-factors of the middle-levels
inclusion graph. Every such solution has exactly 858 selected edge orbits,
contains every physical rank-eight owner once, and contains every physical
rank-seven lower-\(q1\) colour once.

#### Proof

Equation (3.1) selects two distinct incidence edges at every quotient
vertex. Equation (3.2) forces the two endpoint descriptions of each edge to
agree, so the selected quotient graph is spanning and degree two. Its lift
is a spanning physical degree-two graph. Conversely, a rotation-invariant
spanning physical \(2\)-factor descends with voltage-labelled parallel edges
retained, and its two incidences at each vertex define the unique selected
pair. Contracting every physical rank-seven vertex gives the rank-eight
Johnson factor; each contracted vertex supplies its rank-seven intersection
colour exactly once. \(\square\)

The explicit master has

\[
 3432+2\cdot429{8\choose2}=27456                \tag{3.3}
\]

meaningful Boolean variables: 3,432 edge bits and 24,024 turn bits. The
edge bits may be eliminated by equating the two pair sums in (3.2), leaving
24,024 Booleans, 858 exactly-one rows, and 3,432 edge-channel rows. This is
an algebraic elimination, not a relaxation.

### Theorem 3.2 (ordinary pair-cover rows)

Complete lower \(q2\) and complete upper \(q1\) are exactly

\[
 \sum_{(U,p):\kappa_-(U,p)=C}y^U_{U,p}\ge1
 \quad(C\in{\binom{\Omega}{6}}/\rho),           \tag{3.4}
\]

\[
 \sum_{(L,p):\kappa_+(L,p)=D}y^L_{L,p}\ge1
 \quad(D\in{\binom{\Omega}{9}}/\rho).           \tag{3.5}
\]

#### Proof

If \(T_{i-1},T_i,T_{i+1}\) are consecutive rank-eight states and
\(X_{i-1}=T_{i-1}\cap T_i\), \(X_i=T_i\cap T_{i+1}\), then

\[
 T_{i-1}\cap T_i\cap T_{i+1}=X_{i-1}\cap X_i.
\]

This is (2.5). At the intervening rank-seven state,
\(T_i\cup T_{i+1}\) is (2.6). One quotient occurrence covers the entire
physical target orbit, so literal coverage is the OR row, not an equality or
a suffix-automaton constraint. \(\square\)

## 4. Composite-orbit and fibre audit

Burnside gives

\[
 \left|{\binom{\Omega}{6}}/\rho\right|
 ={\binom{15}{6}+2\binom52\over15}=335.          \tag{4.1}
\]

There are 333 target orbits of size 15 and two of size five; rank nine has
the complementary census. The short canonical representatives are

    rank 6: 3171, 5285
    rank 9: 7399, 11627

The exact local atlas has candidate-fibre histogram

\[
 36^{333}12^2                                    \tag{4.2}
\]

on each shore. A selected witness for a size-five orbit has 15 translates
and therefore visits each of its five physical targets three times. This
does not invalidate the OR cover; it does mean that quotient loads and
physical collision counts must not be conflated.

For one deck let \(n_C\) be its 335 quotient loads. Since
\(\sum_Cn_C=429\), complete coverage has collision floor

\[
 \sum_C{n_C\choose2}\ge94,                      \tag{4.3}
\]

with equality exactly for \(1^{241}2^{94}\), equivalently \(1\le n_C\le2\)
for every target. Hence the cap \(n_C\le2\) is the exact linear
collision-floor refinement. It is strictly stronger than coverage.

## 5. Complement-symmetric submaster

Complement induces a fixed-point-free involution on the 3,432
voltage-labelled edge orbits, giving 1,716 pairs. It sends an upper turn to
a lower turn and satisfies

\[
 \kappa_+(\bar U,\bar p)
 =\operatorname{can}_\rho(\Omega\setminus\kappa_-(U,p)).     \tag{5.1}
\]

Therefore, on the restricted face

\[
 x_e=x_{\bar e},                                 \tag{5.2}
\]

the lower-\(q2\) and upper-\(q1\) load vectors are complementary copies.
Either cover implies the other, and either cap at two implies the other.

This is a sufficient restricted submaster, not a without-loss-of-generality
symmetrization theorem. The successful solver run imposed lower-\(q2\)
coverage and (5.2), but omitted the formally redundant upper-\(q1\) rows.
The independent physical replay nevertheless checked all upper targets
directly.

## 6. Exact simultaneous pair-cover certificate

The complement-symmetric feasibility model returned OPTIMAL (a satisfaction
certificate, with no objective) after 39.367882828 seconds on four H100 CPU
workers, with 166,048 conflicts and 10,380,668 branches. The selected
assignment has:

    selected quotient edge orbits          858
    middle owners                         6435 / 6435, each once
    rank-7 lower-q1 colours               6435 / 6435, each once
    rank-6 lower-q2 targets               5005 / 5005
    rank-9 upper-q1 targets               5005 / 5005
    rank-6 quotient loads                 1^259 2^59 3^16 4^1
    rank-9 quotient loads                 1^259 2^59 3^16 4^1
    pair-collision sum, each deck          113
    collision-floor excess, each deck       19

The collision identity is exact:

\[
 59+16{3\choose2}+{4\choose2}=113=94+19.        \tag{6.1}
\]

The two short lower-\(q2\) orbits have loads one and two respectively; the
two short upper-\(q1\) orbits have the complementary loads. All 5,005
physical targets on both sides occur.

The independently reconstructed physical load histogram on either deck is

\[
 1^{3870}2^{870}3^{245}4^{15}6^5,
\]

with physical pair-collision sum 1,770.  The multiplicity-six entries are
exactly the physical manifestation of a load-two size-five quotient orbit.

One selected pair on each shore uses two voltage-distinguished edges with
the same quotient endpoints: pair IDs 11309 and 23463 select edge IDs
3229 and 3230.  These edges lift to the physical 15-cycle in the component
list below; they are not physical loops.  This is a concrete certificate
that deleting the 14 parallel-edge pair choices would make the compressed
model incomplete.

The quotient factor is not connected. Its seven components, listed as
\((\text{number of lower vertices},\text{voltage})\), are

\[
 (195,2),(195,2),(17,3),(17,3),(2,4),(2,4),(1,11). \tag{6.2}
\]

A quotient component of voltage \(\gamma\) lifts to
\(\gcd(15,\gamma)\) physical cycles. Thus (6.2) gives 11 physical cycles of
lengths

    2925, 2925,
    85, 85, 85, 85, 85, 85,
    30, 30,
    15.

The chronology has minimum residence two. Exactly 600 positive coordinate
runs have length two and 750 have length three, hence

\[
 \#\text{bad runs}=1350,
 \qquad
 \sum(4-\ell)_+=2\cdot600+750=1950.             \tag{6.3}
\]

The independent deeper replay finds 303 missing physical lower-\(q3\)
targets, 303 missing upper-\(q2\) targets, 75 missing upper-\(q3\) targets,
and no missing upper targets at depths \(4,5,6,7\). These later facts do
not repair the failures at depths two and three, and no lower-depth claim
beyond the explicitly audited lower \(q3\) statistic is inferred here.

### Theorem 6.1 (proved boundary)

The exact compressed master contains a strict-equivariant spanning physical
\(2\)-factor whose middle and lower-\(q1\) palettes are squarefree and whose
lower-\(q2\) and upper-\(q1\) palettes are complete.

It does not follow that this factor is a resident carrier, a Hamilton cycle,
collision-floor optimal, all-depth complete, safely openable, or compatible
with the literal common-\(Q\) compiler. The retained certificate explicitly
fails the first four of those stronger properties where tested.

## 7. Independent replay and frozen artifacts

The retained files and SHA-256 hashes are:

    scratch/k15_global_pair_cover_simultaneous_raw_20260729.json
    38690ae7288da3f27e772af08e3022edfc3956903f29d4e311d50b3fb60e1783

    scratch/k15_global_pair_cover_simultaneous_20260729.audit.json
    dedac1b8d3ea409a86f812e66dd82a4de8a32027892a2c5a91c657fe09938545

    scratch/k15_global_pair_cover_simultaneous_solver_20260729.stdout
    906ec60d0d2a425aee75dd91df826dd712754b4c9596878644b11fb2272da9e6

    scratch/search_k15_quotient_pair_cover_cpsat_20260729.py
    f89e880f8265bd6066672ec0ef39b1ae54503b4f1c362acd53e57313906e5bf1

    scratch/search_k15_global_pair_cover_cpsat_20260729.py
    3a4734614eedde1b9c33df14125bc62c4a18467e63f975b0af27f7c893d1cde0

The generator's selected-incidence semantic hash is

    6d848a1731c56e7a688f405d29e819124db259baa63f6e1c55d81fe5dd348f5a

The independent replayer uses a separately reconstructed quotient catalogue;
its compact sorted arc-ID serialization has hash

    68c7ab46cd2d0ab09b701acccf669147b05e00cca7b4fd137edb344c4fdd4b95.

The differing semantic hashes are serialization-dependent, not a catalogue
mismatch. Both implementations agree on all 858 selected incidence orbits,
all 6,435 physical degrees on each shore, both immediate-shadow load
vectors, complement symmetry, all seven quotient components and voltages,
all 11 lifted cycles, residence, and the stored deeper-shadow counts. The
independent audit status is PASS.  Its catalogue hashes are

    edge table     8b3d5054edd286c03092089c9e3e198b5f482f1d70d5539746c7ed608197899d
    lower pairs    09016236c04d556bd282f28fe6879aa9da5ee355f0617e6da913be561b695bcb
    upper pairs    5f5023d5daa13a856c36a26e223e8fe80c3621286f7def1cc7c9b6c159f57747
    combined pairs 62085d640098d15cddaea214e8a7a871520edf93a7108bac3e6e80cb94f16959

For comparison, the earlier lower-\(q2\)-only certificate remains frozen at

    scratch/k15_global_pair_cover_q2complete_raw_20260729.json
    SHA-256 59fb88bd84180d16348e0b86f234362d0df490cefa160977fe939e1f837f5dc1

    scratch/k15_global_pair_cover_q2complete_20260729.audit.json
    SHA-256 d49297b7f2af18d740186367eefd1f57f8bdcf732c07de23c46c89fa6e43e549

It is superseded for static pair coverage by Theorem 6.1, but remains a
useful nonsymmetric comparison point.

## 8. Sharp remaining gate

The static degree-two plus lower-\(q2\) plus upper-\(q1\) feasibility question
is now closed positively. The remaining intersection problem is to impose,
simultaneously:

1. one quotient component with unit voltage (or an exactly audited
   palette-preserving splice to one physical cycle);
2. residence at least four;
3. the cap-at-two collision floor if the application requires it;
4. lower \(q3\), the deeper upper tower, and safe opening;
5. the literal common-\(Q\)/compiler constraints.

An alternating circuit in the bipartite \(2\)-factor fibre preserves the
middle and lower-\(q1\) decks exactly, but it need not preserve either
pair-cover row, residence, or component voltage. Consequently the next
valid search/proof space is the intersection of those circuit moves with the
two local pair-cover atlases and the residence/deeper-shadow audits. Static
pair-cover feasibility by itself is no longer the obstruction.

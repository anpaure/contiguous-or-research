# K16 asymmetric repair: the peeling Farkas potential and a sharp C8 orbit descent

Date: 2026-07-30

Lane: H

Status: solver-free common-potential theorem plus an independently replayed
literal constructive descent. The canonical carrier deficit falls from 108
to 93. No compiler-ready K16 carrier or optimal K16 word is claimed.

## 0. Verdict

The new no-gos do not extend to a global obstruction.

* No gainful, q1-safe directed port cycle exists through length seven in the
  frozen positive-residence, four-separated catalogue.
* Among all 1,263 individually deep-safe, gainful cycles of lengths three
  through five, no nonempty subset is even q1-feasible.
* The two-round peeling proof compresses to one integral q1 potential

  \[
  \alpha=11\,1_{R_1}+1_{R_2}
  \tag{0.1}
  \]

  which is at most \(-1\) on every one of those 1,263 columns.
* Nevertheless, length eight is a sharp escape. Fifteen commuting rotated
  C8 head permutations are each q1-safe, deep-safe, and unit-gain. Their
  simultaneous literal replay preserves positive residence and both q1
  decks and gives

  \[
  \boxed{45+63=108\longrightarrow45+48=93}
  \tag{0.2}
  \]

  canonical holes.

Thus the short monotone cone is Farkas-separated, but the full move space is
not. Deep-unsafe or nongainful auxiliaries are necessary only if one insists
on using a cycle from the separated C3--C5 core; a longer C8 can bypass that
core on the zero face of \(\alpha\).

## 1. Frozen objects and exact scopes

The source is

    scratch/k16_asymmetric_triangle_orbit_repair_20260729.json
    SHA-256 6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc

It has 45 fixed lower-q2 holes and 63 authoritative arbitrary-upper
rank-eleven holes.

The complete signed C3--C5 core is

    scratch/k16_asymmetric_signed_compound_cycle_catalogue_20260730.json
    SHA-256 23984ea67f6d9275efa0de337c85a58bd23ff0bb6763af5de01a30f1d3305817

and its solver-free peeling certificate is

    scratch/k16_asymmetric_compound_q1_peeling_20260730.audit.json
    SHA-256 d0ff8ab28b4b64e1051f40de9421d18a62d772430f07444d769babf028628f0e

The catalogue contains

\[
\begin{array}{c|rrr|r}
\text{length}&3&4&5&\text{total}\\ \hline
\text{deep-safe gainful cycles}&95&180&988&1263.
\end{array}
\tag{1.1}
\]

Here deep-safe means fixed lower-q2 and fixed upper-q3 safe. It does not mean
all-depth or authoritative arbitrary-upper safe.

The length-seven certificate is

    scratch/k16_asymmetric_long_port_cycles_len7_20260730.audit.json
    SHA-256 f42ca26f8978dd4808db1253e6c9fcad3ab320a8e566566add5f79b877413429

It is complete for q1-safe gainful cycles in the frozen directed,
positive-residence, pairwise-four-separated catalogue. It is not a complete
classification of every C7: q1-prefix pruning leaves 101,663 completed
cycles, of which 947 are deep-safe, and none is q1-safe. The output is bound
to the correct factor hash, but its run manifest does not embed the source
or binary hash; this is a lineage caveat, not a reason to broaden its scope.

The constructive length-eight census and orbit factor are

    scratch/k16_asymmetric_long_port_cycles_len8_20260730.audit.json
    SHA-256 d1b5ffc53593b9aa312c67cb991cfd7ac7a5775752bce826c90b0fb2f9145213

    scratch/k16_asymmetric_len8_orbit_repair_20260730.json
    SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

    scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
    SHA-256 3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87

Existence of the materialized factor is independently replayed and does not
depend on completeness of the C8 census.

## 2. Two peeling rounds give one common Farkas potential

Let \(\mathcal G\) be the 1,263-column C3--C5 core and let \(D_P\) be the
full signed lower-plus-upper q1 column of \(P\).

The peeling certificate partitions

\[
 \mathcal G=\mathcal G_1\sqcup\mathcal G_2,\qquad
 |\mathcal G_1|=1235,\quad|\mathcal G_2|=28.
\tag{2.1}
\]

For \(i=1,2\), let \(R_i\) be the set of unit-load q1 rows chosen as
witnesses for candidates killed in round \(i\). After duplicate rows are
identified,

\[
 |R_1|=732,\qquad |R_2|=28.
\tag{2.2}
\]

### Theorem 2.1 (integral separator for the short gain cone)

With \(\alpha\) as in (0.1),

\[
 \boxed{\alpha^{\mathsf T}D_P\le-1
        \qquad(P\in\mathcal G).}
\tag{2.3}
\]

Consequently

\[
 x\ge0,\qquad D_{\mathcal G}x\ge0
 \quad\Longrightarrow\quad x=0.
\tag{2.4}
\]

This excludes the entire nonnegative fractional cone, not only subsets.

#### Proof

Every row in \(R_1\) has nonpositive coefficient on every catalogue column,
and every \(P\in\mathcal G_1\) is negative on at least one chosen \(R_1\)
row. Hence

\[
 1_{R_1}^{\mathsf T}D_P\le-1
 \qquad(P\in\mathcal G_1).
\tag{2.5}
\]

A length-\(\ell\le5\) head permutation adds \(\ell\) edges. Each added edge
contributes one lower and one upper q1 occurrence, so the total positive q1
mass of \(D_P\) is at most \(2\ell\le10\). Therefore

\[
 \alpha^{\mathsf T}D_P\le-11+10=-1
 \qquad(P\in\mathcal G_1).
\tag{2.6}
\]

A round-two survivor is zero on every \(R_1\) row: those rows have no
positive core coefficient, and a negative coefficient would have killed
the survivor in round one. Every \(R_2\) row is nonpositive on all
round-two survivors, and each survivor is negative on its chosen witness.
Thus (2.3) also holds on \(\mathcal G_2\).

If \(x\ne0\), then (2.3) gives

\[
 \alpha^{\mathsf T}D_{\mathcal G}x
 \le-\sum_{P\in\mathcal G}x_P<0,
\]

contradicting \(D_{\mathcal G}x\ge0\) on the unit rows supporting
\(\alpha\). \(\square\)

The lightweight replay finds the exact score range

\[
 -55\le\alpha^{\mathsf T}D_P\le-1
 \tag{2.7}
\]

over all 1,263 columns.

## 3. Exact auxiliary-generator escape inequality

Let \(\mathcal A\) be any additional additive generator family: longer
cycles, individually deep-unsafe cycles, nongainful cycles, or other
base-relative packets. Put

\[
 w_A=\alpha^{\mathsf T}D_A.
\tag{3.1}
\]

### Theorem 3.1 (positive-potential auxiliary is mandatory)

Every q1-feasible additive compound packet \((x,y)\) satisfies

\[
 \boxed{\sum_{P\in\mathcal G}x_P
 \le\sum_{A\in\mathcal A}w_Ay_A.}
\tag{3.2}
\]

In particular, a packet using any core cycle must use an auxiliary with
\(w_A>0\).

#### Proof

All rows supporting \(\alpha\) have source load one. Q1 feasibility gives

\[
 0\le
 \alpha^{\mathsf T}(D_{\mathcal G}x+D_{\mathcal A}y)
 \le-\sum_Px_P+\sum_Aw_Ay_A,
\]

which is (3.2). \(\square\)

Each core cycle hits at most five of the 108 source holes. For an integral
additive packet with \(x,y\in\mathbb Z_{\ge0}\), let \(h_A\) be the size of the positive support of
auxiliary \(A\) on those holes. Assume every final hole witness is represented
by the sum of the selected frozen columns. Then complete service of all 108
holes necessarily satisfies

\[
 \boxed{\sum_{A\in\mathcal A}(h_A+5w_A)y_A\ge108.}
\tag{3.3}
\]

Indeed, the support of the final positive hole vector is contained in the
union of the selected columns' positive supports. This is only a necessary
raw-service inequality for integral selections, not a fractional-cone
inequality. It ignores repeated hits, deep casualties, and
incompatibility. It does not apply to overlapping or sequential moves whose
new witnesses are not represented by the frozen additive columns. If all
admissible auxiliaries in this additive sense are nongainful, (3.3) forces
at least 22 integral units of positive \(\alpha\)-credit.

The C8 orbit below does not contradict Theorem 3.1: it uses no core column,
and every one of its fifteen C8 columns has \(\alpha\)-score zero.

## 4. Full repair and strict net descent with unsafe/helper generators

There are two different linear gates.

### Theorem 4.1 (complete-repair Farkas alternative)

For a finite additive catalogue, let

* \(Q\) be its q1 signed matrix, with source slack \(s\);
* \(H\) be its signed matrix on the 108 source holes;
* \(C\) be its signed matrix on previously covered required targets, with
  source slack \(r\).

The fractional complete-repair system is

\[
 Qy\ge-s,\qquad Hy\ge\mathbf1,\qquad Cy\ge-r,\qquad y\ge0.
\tag{4.1}
\]

It is infeasible if and only if there are
\(\alpha,\beta,\gamma\ge0\) such that

\[
 \alpha^{\mathsf T}Q_P+
 \beta^{\mathsf T}H_P+
 \gamma^{\mathsf T}C_P\le0
 \quad(P\text{ arbitrary}),
\tag{4.2}
\]

and

\[
 \beta^{\mathsf T}\mathbf1>
 \alpha^{\mathsf T}s+\gamma^{\mathsf T}r.
\tag{4.3}
\]

#### Proof

Apply Farkas to the three block inequalities in (4.1). Equivalently,
multiply a putative solution by \(\alpha,\beta,\gamma\); (4.2) makes the
result nonpositive, while (4.3) makes it positive. The converse is the
standard linear alternative. \(\square\)

This is the correct complete-repair dual after admitting deep-unsafe and
nongainful helpers.

### Theorem 4.2 (exact capped-coverage gate for a strict hole descent)

Let \(\mathcal T\) be a finite required target universe, let \(m_T\) be its
source load, and let \(S\) be an additive signed load matrix. Put

\[
 B=|\{T:m_T\ge1\}|.
\]

The relaxed strict-descent system is

\[
\begin{aligned}
 Qy&\ge-s,\\
 m+Sy&\ge z,\\
 0\le z&\le\mathbf1,\\
 \mathbf1^{\mathsf T}z&\ge B+1,\\
 y&\ge0.
\end{aligned}
\tag{4.4}
\]

Its infeasibility is equivalent to the existence of
\(\alpha,\eta,\theta\ge0\) and \(\rho>0\) such that

\[
 \alpha^{\mathsf T}Q_P+\eta^{\mathsf T}S_P\le0
 \quad(P\text{ arbitrary}),
\tag{4.5}
\]

\[
 \eta+\theta\ge\rho\mathbf1,
\tag{4.6}
\]

and

\[
 \alpha^{\mathsf T}s+\eta^{\mathsf T}m+
 \theta^{\mathsf T}\mathbf1
 <\rho(B+1).
\tag{4.7}
\]

#### Proof

Write (4.4) in upper-bound form:

\[
 -Qy\le s,\quad -Sy+z\le m,\quad z\le\mathbf1,\quad
 -\mathbf1^{\mathsf T}z\le-(B+1),
\]

with \(y,z\ge0\). Farkas multipliers
\(\alpha,\eta,\theta,\rho\) give respectively the column conditions
(4.5)--(4.6) and the strict right-hand inequality (4.7). \(\square\)

For integral compatible packets and literal load columns, \(z_T\) is the
coverage indicator and (4.4) is exactly a strict reduction in the number of
holes. For the fractional cone it is only a relaxation. For overlapping or
sequential moves, and for arbitrary-width upper witnesses, frozen local
columns may fail to add; the final successor chronology or accumulated-union
automaton must then be replayed.

## 5. Lower-q2 service must spend a unique token or cross slack

Let \(F_0\) be the repaired no-cross source, whose \(U_z\) upper-q1 bank has
one old provider per colour. Let \(F\) be any q1-complete spanning
two-factor with

\[
 |E_{AB}(F)|=2t.
\tag{5.1}
\]

Suppose \(g\) formerly missing lower-q2 targets are gained. Choose distinct
new \(BB\) edges supporting these new three-state witnesses. Their number
\(k\) satisfies

\[
 k\ge\left\lceil\frac g2\right\rceil,
\tag{5.2}
\]

because one factor edge lies in only two three-state windows.

Let \(R\) count upper colours among these new \(BB\) edges whose unique old
\(BB\) provider is absent from \(F\).

### Theorem 5.1 (unique-token/cross-slack dichotomy)

\[
 \boxed{R+t\ge k\ge\left\lceil\frac g2\right\rceil.}
\tag{5.3}
\]

#### Proof

For upper colour \(U\), let \(r_U\in\{0,1\}\) record retention of its old
unique provider, let \(n_U\) count chosen relevant new \(BB\) edges of colour
\(U\), and let \(m_U\) be its final \(U_z\)-load. Then

\[
 n_U\le(m_U-1)+(1-r_U).
\tag{5.4}
\]

Indeed, if \(r_U=1\), the incumbent plus the \(n_U\) new edges are all
present, while if \(r_U=0\), the \(n_U\) new edges themselves are present.
Summing (5.4) only over colours with \(n_U>0\), and using

\[
 \sum_{U\in U_z}(m_U-1)=t
\]

from the cross-shore surplus identity, gives \(k\le t+R\). \(\square\)

For all 45 lower holes this resource floor is 23. Cross slack is not free:
the same \(t\) removes \(t\) total occurrences from each of the
\(L_z\) and \(U_{\bar z}\) slack banks.

## 6. The sharp constructive C8

The length-eight q1-pruned census is complete for q1-safe gainful cycles in
the frozen directed catalogue. It proves the two complete counts

\[
\begin{array}{c|r}
\text{q1-safe class}&\text{count}\\ \hline
\text{deep-unsafe}&30\\
\text{deep-safe}&15.
\end{array}
\tag{6.1}
\]

The artifact also records 410,851 q1-unsafe/deep-unsafe and 2,438
q1-unsafe/deep-safe completed survivors, but those are not total C8 counts:
the file explicitly has
\(\texttt{complete\_all\_cycle\_classification=false}\).
All fifteen safe/deep-safe cycles have gain one and form one free
\(C_{15}\)-orbit.

One seed order of old transition indices is

\[
 (8641,10464,7052,5569,5060,3977,3298,4012).
\tag{6.2}
\]

It deletes

\[
\begin{aligned}
&(7829,15509),(15501,16005),(23687,24198),(23701,24197),\\
&(23702,24212),(40085,46229),(48261,48265),(56341,56468)
\end{aligned}
\tag{6.3}
\]

and adds

\[
\begin{aligned}
&(7829,23701),(15501,48265),(15509,16005),(23687,24197),\\
&(23702,24198),(24212,56468),(40085,56341),(46229,48261).
\end{aligned}
\tag{6.4}
\]

Its nonzero q1 delta is

\[
\begin{aligned}
\Delta L={}&
 e_{15497}+e_{39957}+e_{46213}
 -e_{38037}-e_{48257}-e_{56340},\\
\Delta U={}&e_{56980}-e_{16013}.
\end{aligned}
\tag{6.5}
\]

The three negative lower colours have source load two, and \(16013\) has
source upper load two. Thus the cycle is q1-safe. It uses two cross edges,
so \(t=1\), and (6.5) realizes exactly

\[
 (\Delta L_{\bar z},\Delta L_z,\Delta U_{\bar z},\Delta U_z)
 =(1,-1,-1,1).
\tag{6.6}
\]

It preserves the fixed lower-q2 and upper-q3 ledgers and fills precisely
the rank-eleven target \(48373\). Independent full replay gives one fewer
authoritative arbitrary-upper hole and no new arbitrary-upper target.

### Theorem 6.1 (commuting C8 orbit descent)

Apply all fifteen rotated cycles listed in the frozen factor artifact. Then:

1. their 120 old cuts are distinct and have minimum mutual source-cycle gap
   29, so the head permutations commute and all fixed q2/q3 ledgers add;
2. the final edge set has 12,870 distinct Johnson edges and 29 components;
3. positive residence remains four, with no violation;
4. both q1 decks remain complete, with exact shore histograms

   \[
   \begin{array}{c|c}
   L_{\bar z}&1^{6420}2^{15}\\
   L_z&1^{3690}2^{1215}3^{100}\\
   U_{\bar z}&1^{3690}2^{1215}3^{100}\\
   U_z&1^{6420}2^{15};
   \end{array}
   \tag{6.7}
   \]

5. the 45 lower-q2 holes are unchanged;
6. the upper rank-eleven holes fall from 63 to 48, filling exactly the
   \(C_{15}\)-orbit of \(48373\);
7. no new arbitrary-upper hole occurs, and rank twelve remains
   arbitrary-upper complete.

Therefore the canonical objective falls from 108 to 93.

#### Proof

The hash-pinned replay reconstructs all fifteen head permutations directly
from the source transition indices and obtains the saved successor map
exactly. It checks cut disjointness, gap 29, every Johnson edge, and the q1
histograms (6.7). The independent literal factor audit replays every fixed
lower/upper window and the accumulated-union automaton. Its set difference
between the old and new rank-eleven hole lists is exactly

\[
\begin{gathered}
40623,43983,44861,48373,48478,53079,54759,55198,\\
56954,59307,60147,62421,62841,63978,64188,
\end{gathered}
\]

the rotation orbit of \(48373\). \(\square\)

The fifteen fixed upper-q4 holes inherited from the triangle repair remain,
but every one has an interval witness of another width; they are not
arbitrary-upper holes. The factor is not compiler-ready because 93 canonical
holes remain.

## 7. The joint bounded-history model is the right local circulation space

The model in
MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md
absorbs phase into transition options and expands a quotient owner \(u\) to

\[
 (u,h_1,h_2,h_3),
\tag{7.1}
\]

where the three history labels are the last three inserted old coordinates
in the canonical frame of \(u\). Its arcs are precisely the transition
options satisfying the local history update. This gives the correct local
state space for q1 cancellation plus positive residence.

### Theorem 7.1 (signed q1 potentials become history-arc costs)

Let \(\widehat E\) be the expanded history arcs and let
\(\pi:\widehat E\to E_{\rm opt}\) forget history. Replicate each raw option's
exact lower-plus-upper q1 column, including the correct physical
multiplicities for short label orbits, on every arc in its fibre; call the
resulting common-index matrix \(\widehat A\). Let \(\widehat B\) be the
incidence matrix of the expanded history graph. Let \(x^0\) and \(x\) be two
feasible expanded-state cycle-cover selections, including one chosen history
state per owner cluster, and put \(z=x-x^0\). Then

\[
 \widehat Bz=0,\qquad \Delta_{\rm q1}=\widehat A z,
\tag{7.2}
\]

For every q1 potential
\(\lambda\),

\[
 \boxed{\lambda^{\mathsf T}\Delta_{\rm q1}
       =(\widehat A^{\mathsf T}\lambda)^{\mathsf T}z.}
\tag{7.3}
\]

Thus a signed q1 Farkas potential is exactly an additive cost on
history-compatible option arcs. The difference of two integral cycle-cover
selections is a balanced integral circulation, subject additionally to the
one-history-state-per-owner-cluster constraints.

#### Proof

Both selections are balanced on their chosen expanded history states, so
their difference has zero expanded incidence, giving \(\widehat Bz=0\).
Q1 load is the sum of the replicated local option labels, hence its signed
change is \(\widehat A z\).
Equation (7.3) is matrix transposition. The history expansion changes which
arcs are legal but not these identities. \(\square\)

The circulation identity does not remove feasibility bounds:
\(-x^0\le z\le1-x^0\), zero net change in every owner-cluster selection,
palette coverage, voltage, and connectivity must still be imposed.

The physical peeling potential also has a quotient-invariant
symmetrization

\[
 \widetilde\alpha=\sum_{g\in C_{15}}g\alpha
\tag{7.4}
\]

which is constant on q1 label orbits. The saved directed C3--C5 catalogue is
not itself closed under coordinate rotation, because its component
orientations are not equivariant; consequently closure cannot be used to
infer its score. Instead, the hash-pinned signed-column replay checks
directly that, for every one of its 1,263 core columns,

\[
 -825\le\widetilde\alpha^{\mathsf T}D_P\le-11.
\tag{7.5}
\]

Hence \(\widetilde\alpha\) is an honest quotient arc cost separating this
finite directed core, not a phase-dependent physical artifact. The direct
audit, rather than a false catalogue-closure argument, is essential.

The full C8 orbit lands naturally in the model's cross count: its 30
physical cross edges are one \(A\to B\) and one \(B\to A\) quotient option,
so \(t=15\). It creates exactly one duplicated free q1 orbit in each tight
sector. The duplicated lower-no-\(z\) orbit is represented by \(15497\);
the duplicated upper-with-\(z\) orbit is represented by \(56980\).
Every individual C8 has \(\alpha\)-score zero. Since all rows supporting
\(\alpha\) had source load one and each C8 is q1-safe, every such row has
individual delta zero; the complete peeling support therefore remains tight
after the orbit move. The two new reservoir orbits lie outside that support.
Each C8 also has \(\widetilde\alpha\)-score zero.
Therefore the post-C8 q1 constraints are

\[
 \widehat A z\ge-s^{(8)},
\tag{7.6}
\]

with one unit of quotient slack on each of those two tight label orbits,
not the zero-slack Eulerian equation of the original no-cross rails.
Any old core column which remains literally valid and disjoint from the C8
support retains its negative \(\alpha\)-score. This does not classify newly
created post-C8 cycles; their signed columns must be regenerated from the
new successor map.

Three qualifications are essential.

1. The joint theorem's connected, unit-voltage, one-\(A\)-block/
   one-\(B\)-block model is a sufficient equivariant class. The present C8
   factor has 29 physical components, so it is a cycle-cover seed, not
   already a feasible Hamilton point of that model.
2. The three insertion-history labels are sufficient for positive
   residence four of the old coordinates and q1 locality. In the connected
   theorem, the global one-\(A\)-block/one-\(B\)-block condition controls the
   top coordinate. A multicomponent cycle-cover relaxation must retain that
   condition or impose a separate top-coordinate short-run constraint.
   The three labels also do not encode fixed q2/q3 targets or
   arbitrary-width upper coverage. Fixed-depth work needs a bounded option
   trace, and authoritative upper coverage needs the accumulated-union
   automaton.
3. Flow balance alone is not enough. One state per owner cluster, palette
   coverage, voltage, and connectivity remain non-network constraints.

Subject to those qualifications, the right next algebraic object is a
coloured signed circulation in the expanded history graph, based at the C8
factor, with q1 reservoir \(s^{(8)}\) and a separate trace automaton for the
remaining 93 holes. One may work directly with final binary arc variables
\(x\), or write

\[
 z=z^+-z^-,\qquad x=x^0+z\in\{0,1\}^{\widehat E},
\]

with the displayed bounds, cluster rows, and degree rows. The nonnegative
generator system (4.4) applies only after a verified additive packet
catalogue is chosen; it must not be applied directly to the signed residual
\(z\). This expanded formulation admits deep-unsafe or nongainful helper
packets without discarding residence chronology.

For the source-relative, three-separated class, the newer global
port-permutation master eliminates the explicit history state: the three
incoming and outgoing histories are fixed by each source port, and collar
safety is compiled into arc legality. The exact assignment-circulation
identity, bounded-depth occurrence columns, cross-shore checksum, and the
assignment-priced Farkas alternatives are proved in

    MATH_THEOREM_H_K16_TOKEN_FARKAS_PORT_PERMUTATION_MAPPING_20260730.md.

In particular, the peeling potential becomes a literal reduced seam cost,
but a global dual also needs free tail/head prices and multipliers for
separation and physical reverse-edge conflicts. This is the precise finite
signed-circulation formulation of the post-C8 repair gate.

## 8. Audit and exact remaining boundary

The independent theorem replay is

    scratch/audit_k16_asymmetric_len8_orbit_token_descent_20260730.py
    scratch/k16_asymmetric_len8_orbit_token_descent_20260730.audit.json

It also verifies the common potential (0.1): its support sizes are 732 and
28, its score range on the core is \([-55,-1]\), the symmetrized
quotient-potential range is \([-825,-11]\), and every C8 orbit column has
score zero for both potentials.

The proved boundary is now:

* the separated deep-safe/gainful C3--C5 cone is strictly
  Farkas-decreasing;
* no single gainful q1-safe cycle exists through C7;
* C8 is a literal, sharp, q1-safe and deep-safe escape giving a
  15-hole orbit descent;
* the remaining exact carrier bank has 45 lower and 48 arbitrary-upper
  rank-eleven holes.

No statement here proves that the remaining 93 holes can be removed,
connects the 29 components, supplies the one-core compiler, or yields a word
of length 12,873. Any further overlapping or sequential packet must be
audited on its final chronology.

No new search, SAT, CP, LP solve, or heavy local computation was performed
in this lane. Existing remote certificates were copied and then replayed by
lightweight deterministic local audits.

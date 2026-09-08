# AD audit: exact radius-two `SSSSS` signed-lattice no-go

Date: 2026-07-30  
Status: proved and independently audited for the frozen source-relative
\(C=106\), `SSSSS` seam catalogue

## 1. Exact scope

Let \(E\) be the frozen 211,604-seam source-relative catalogue and let
\(S\subset E\) be the 662 positive columns of the exact capacity-one
fractional `SSSSS` basis.  For a binary selection \(x\), impose only

\[
\begin{aligned}
 \operatorname{out}_x(v)&=\operatorname{in}_x(v)\le1
     &&(v\text{ a port}),\\
 \sum_{e:t\in H(e)}x_e&=1
     &&(t\text{ one of the 93 frozen targets}),\\
 \sum_ex_e&=106,\\
 \sum_es_ex_e&=5.
\end{aligned}                                                     \tag{1.1}
\]

Every seam has nonnegative direct-dual slack, and under balance and exact
service

\[
 \sum_es_ex_e=2\sum_ex_e-207.                                    \tag{1.2}
\]

The support-only face is already excluded by an explicit 33-target parity
certificate and checked DRAT/LRAT.  The complete radius-one face over the 298
return-capable odd columns is also excluded by checked DRAT/LRAT, an exact
298-right-hand-side reconstruction, and a mod-457 separator.  Those proofs
are frozen in

```text
MATH_AUDIT_AD_K16_C106_SSSSS_SUPPORT662_CHECKED_UNSAT_20260730.md
SHA-256 f2f990efceb5bba6b633bd25ab196f0f2391846f0a5591dc8c52a66254aadc88

MATH_AUDIT_AD_K16_C106_SSSSS_RADIUS1_CHECKED_UNSAT_AND_CRT_ESCAPE_20260730.md
SHA-256 2df3308e79617cffb6e606fb3b8566b16d7e57b6f6b7caa7cac4d2c68a35a39b
```

The deterministic radius-one CNF has 7,344 variables and 22,390 clauses.
Kissat returned UNSAT; `drat-trim` verified the DRAT, retained 27 source
clauses and three lemmas, and emitted the LRAT checked against the full CNF.

The radius-one proof-producing bundle has CNF SHA-256
`8d853bd2532fac6d7662d6e67cc4aa3cfa284f57772f4f519dd8ae7307ab6c06`,
DRAT SHA-256
`5066dac60660a4a43da3c1902204b94e9915f0e546ee0fe55f3ac8f90764159f`,
and checked LRAT SHA-256
`324ed7f00ca2862a6a9511b2c1c90a7dceb5cde0727bf461bd40a9a6ff2b9687`.
Its independent raw-ledger/CNF replay is

```text
scratch/ad_k16_c106_sssss_radius1_unsat_bundle_20260730.audit.json
SHA-256 b1f9e87c8ebdcf3654dc95d7b4c4a5e50d5423dba766bd4e4359dca54618a154
payload 273c63ee481331fd5ea6115cdfa517c935c5047ea0f2f5074855abadf8e48242
status PASS_CHECKED_DRAT_LRAT_AND_FULL_PHYSICAL_RADIUS1_REPLAY
```

This note closes exactly the face with two selected columns in \(E\setminus
S\).  It does not claim that the full `SSSSS` branch is infeasible.

## 2. Exact structural universe at radius two

The support graph has 571 vertices, 662 edges, and three weak components.
Contract those components and leave every port outside the support vertex set
as a singleton quotient node.

Let \(F=\{a,b\}\subset E\setminus S\) be the two selected outside seams in a
physical solution of (1.1).  The following conditions are necessary.

1. Since all slacks are nonnegative, \(s_a+s_b\le5\).
2. The combined mod-two/mod-457 escape price satisfies
   \(q_a+q_b\equiv1\pmod {914}\).
3. Capacity one gives distinct raw tails and distinct raw heads.
4. Exact service gives \(H(a)\cap H(b)=\varnothing\).
5. The two quotient arcs have zero incidence.

With two quotient arcs, item 5 has exactly two forms: both arcs are quotient
loops, or they are opposite arcs between the same two distinct quotient
nodes.  This is both necessary and sufficient for a signed support chain to
cancel their endpoint divergence.

The frozen slack-at-most-five outside catalogue has 210,763 seams.  Exact
bucket enumeration gives

\[
 208=204+4                                                   \tag{2.1}
\]

unordered pairs: 204 loop-loop pairs and four reciprocal quotient two-cycles.
All 208 are target-disjoint.  Their sorted pair-set SHA-256 is

```text
55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7
```

The structural enumeration and two separately written replays are

```text
scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json
SHA-256 9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff
payload adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1

scratch/ad_k16_c106_sssss_crt914_radius2_pairs_replay_20260730.audit.json
SHA-256 bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c
payload 620a816024ed530e6d67a716a4559fa942566805b1661740b1adc769911c14b5

scratch/ad_k16_c106_sssss_crt914_radius2_service_disjoint_20260730.audit.json
SHA-256 d74a1cf145dcf6660772055931f80dff0ede34138e9fe185ff8822f0064c20e0
payload 42bc348d70fcdc4260ea43788d8edcb08718fcada615d1686398bc132910e8f4
```

Thus the 208 pairs are an exhaustive physical radius-two universe, not a
candidate sample.

## 3. Exact signed-support completion theorem

Let \(B\) be the port-edge incidence matrix.  For an integral edge vector
\(y\), define its 94-coordinate feature vector by

\[
 \Phi(y)=\left(\left(\sum_{e:t\in H(e)}y_e\right)_{t\in\mathcal T},
                  \sum_e y_e\right),                            \tag{3.1}
\]

where \(\mathcal T\) is the 93-target set.

Choose a spanning forest of the support graph.  Its signed fundamental cycles
\(z_1,\ldots,z_{94}\) form a \(\mathbb Z\)-basis of the integral support
circulation lattice, since

\[
 |S|-|V(S)|+c(S)=662-571+3=94.                                  \tag{3.2}
\]

Put

\[
 M=\bigl[\Phi(z_1)\ \cdots\ \Phi(z_{94})\bigr]\in
       \mathbb Z^{94\times94}.                                  \tag{3.3}
\]

For an outside set \(F\) with zero quotient incidence, choose any integral
signed support chain \(r_F\) satisfying

\[
 B(r_F+\mathbf1_F)=0,                                           \tag{3.4}
\]

and define

\[
 b_F=(\mathbf1_{93},106)-\Phi(r_F+\mathbf1_F).                  \tag{3.5}
\]

> **Theorem 3.1 (exact signed-recourse criterion).**  There exists
> \(y\in\mathbb Z^S\) such that \(y+\mathbf1_F\) is balanced, services each
> target exactly once, and has mass 106 if and only if
> \[
> b_F\in M\mathbb Z^{94}.                                      \tag{3.6}
> \]
> Membership is independent of the choice of \(r_F\).

**Proof.**  If \(y+\mathbf1_F\) and \(r_F+\mathbf1_F\) are balanced, then
\(y-r_F\) is an integral support circulation.  It therefore has a unique
expression \(\sum_j\lambda_jz_j\) with \(\lambda_j\in\mathbb Z\).  Applying
\(\Phi\) gives (3.6).  Conversely, an integral solution of
\(M\lambda=b_F\) gives the required signed completion
\(r_F+\sum_j\lambda_jz_j\).  Two return chains differ by an integral support
circulation, so they change \(b_F\) by an element of
\(M\mathbb Z^{94}\).  \(\square\)

This criterion is exact for signed support recourse.  It is a relaxation of
physical recourse because it omits support nonnegativity, binarity, and
port-capacity bounds.

## 4. Complete modular membership test

Bareiss elimination gives

\[
 \det M=-7452780650347681984140640,                              \tag{4.1}
\]

with independently checked factorization

\[
 |\det M|=2^5\cdot5\cdot457\cdot63079\cdot33852407\cdot47731799.\tag{4.2}
\]

All five displayed odd factors are prime.  For a full-rank integer matrix,
Smith normal form gives

\[
 b\in M\mathbb Z^{94}
 \Longleftrightarrow
 b\bmod p^{v_p(\det M)}\in\operatorname{im}M
 \quad\text{for every }p\mid\det M.                            \tag{4.3}
\]

Over \(\mathbb Z/p^a\mathbb Z\), the perfect pairing says that image
membership is equivalent to \(\lambda b=0\) for every left annihilator
\(\lambda M=0\).

For each odd factor, the checker finds a one-dimensional left nullspace, so
one generator suffices.  Modulo 32, it begins with the complete mod-two
nullspace and inductively enumerates every lift
\(\lambda+2^j\delta\) by solving

\[
 M^{\mathsf T}\delta=-\lambda M/2^j\pmod2.                     \tag{4.4}
\]

It obtains 32 distinct valid annihilators.  This is complete both by the lift
construction and because the two-primary cokernel has order
\(2^{v_2(\det M)}=32\).

## 5. Exact exclusion of all 208 pairs

For each structural pair, the raw-ledger checker constructs the return chain
in (3.4), computes (3.5), and applies the complete test (4.3).  Return signs
were independently audited:

- a support chord or quotient loop \(u\to v\) gets the tree return
  \(v\to u\);
- for reciprocal quotient arcs, the chain in each support component runs
  from the incoming endpoint to the outgoing endpoint;
- a singleton quotient class forces those two endpoints to coincide.

Every pair fails signed-lattice membership:

\[
\begin{array}{c|rrr}
\text{first failing modulus}&32&5&63079\\ \hline
\text{pairs}&198&8&2.
\end{array}                                                       \tag{5.1}
\]

There are no survivors.

```text
scratch/provider56_audit_k16_c106_sssss_crt914_radius2_lattice_20260730.py
SHA-256 e1de952e5094b3b54b2fee261b8d0a334652fc4c71cf811c9066cd5696b10fc4

scratch/provider56_k16_c106_sssss_crt914_radius2_lattice_20260730.audit.json
SHA-256 a84b4e07f8002d4f723c9ff476977f82ccd9568a575551e03b4f76a1584643f1
payload b36c2c0d658b2e0bc42ee515a085b3e5b927caa741de74fc25db643637b1787b
status PASS_ALL_208_PAIRS_EXCLUDED_BY_SIGNED_SUPPORT_LATTICE
```

The checker independently reparses the frozen physical ledger, rebuilds the
662-edge support graph, spanning forest, all 94 feature columns, determinant,
pair-set SHA, and every modular rejection.  Its H100 run took 3.93 seconds
wall time and 241,236 KiB maximum resident memory under a 2 GiB address-space
cap.  No local heavy process was run.

Combining the support-only, radius-one, and radius-two certificates proves:

> **Theorem 5.1 (checked expansion-radius lower bound).**  Every physical
> source-relative `SSSSS` solution of (1.1) uses
> \[
> \boxed{\sum_{e\notin S}x_e\ge3.}                              \tag{5.2}
> \]

The radius-two step is stronger than physical infeasibility: no pair admits
even an integral signed support completion of its service and count defect.

## 6. Semantic-core cross-audit

The 27-clause radius-one core also yields a global, auxiliary-free escape cut.
Without an outside seam from a particular 217-column bank, exact service
preserves two target ALOs and three target AMOs, while balance and capacity
preserve eight implication clauses inducing seven distinct directed locks at
six ports; these clauses contradict.
Because total slack is five and all seam slacks are nonnegative, the
full-ledger slack-at-most-five scan covers every selected outside seam.  The
semantic derivation then identifies the 217 seams capable of invalidating at
least one of those ALO or directed-lock premises, even when three or more
outside seams are selected.

The bank is necessary, but it is neither proved minimal nor sufficient.

```text
scratch/ad_k16_c106_sssss_radius1_core_escape_bank_20260730.tsv
SHA-256 a7b59f27b6b328b23337743083022dafbcb951997703998af78ef0f2a3c0ab00

scratch/ad_k16_c106_sssss_radius1_core_escape_bank_20260730.audit.json
SHA-256 10f1e495b0ae7b777cdc25dfaa8dc2d40f19c41a106e21d82c72f60b09a8f052
payload e685b3996b14fa621b840173bd968cfa7a6aaf0e92b029d02a327d4e2301e941
```

Intersecting this bank with the complete 208-pair structural interface leaves
exactly

\[
 (109877,208336),\qquad(207292,207669).                          \tag{6.1}
\]

Both fail the signed lattice modulo 32, at annihilator index 1 with residue
16.

```text
scratch/ad_k16_c106_sssss_radius2_pricing_bank_20260730.tsv
SHA-256 148be60290968c195d2a84b773018c8d7351d6a28ca4fd535accf28c14484b9e

scratch/ad_k16_c106_sssss_radius2_pricing_bank_20260730.audit.json
SHA-256 ef69110a0b7700d6ff0e03c3fe908a772aceec4239a6b57b2df98b8a10df7b74
payload 3ee6bb393d43d9a13d6bdf62eb1e8de77913bce2de18da92d2029cf013aaa794
```

## 7. Exact annealer condition after radius two

The smallest still-open support expansion has at least three outside seams.
For an annealer proposal with outside set \(F\), every exact physical
completion must satisfy all of the following.

1. \(|F|\ge3\).
2. \(\sum_{e\in F}q_e\equiv1\pmod {914}\).
3. \(\sum_{e\in F}s_e\le5\).
4. The outside quotient arcs have zero incidence.
5. Raw tails and raw heads each have multiplicity at most one.
6. Every target has outside multiplicity at most one.
7. \(F\) meets the 217-column semantic escape bank.
8. The exact signed-recourse condition \(b_F\in M\mathbb Z^{94}\) holds.

Condition 8 is a finite exact oracle, not another optimization proxy.  It can
be evaluated by the complete prime-power annihilators recomputed by the
checker; their coefficients are not yet serialized as a standalone bank.  On
a closed directed cycle, endpoint potentials cancel, so these residues are
additive cycle prices.  A direct implementation may retain the 31 nonzero
rows of the complete 32-element mod-32 annihilator group and one generator for
each of the five odd moduli.  The earlier CRT-914 price is the cheapest
projection of this full signature.  Condition 8 is exact for signed
balance/service/count recourse, not for physical recourse.

Passing these conditions proves only the existence of signed support recourse.
The annealer must still replay support nonnegativity and binarity, support-port
capacity, q1, residence, separation, connectivity, and every later physical
row before accepting a literal carrier.

## 8. Precise boundary

Proved:

1. The complete source-relative radius-zero, radius-one, and radius-two faces
   are infeasible.
2. Radius one has checked DRAT/LRAT and an independent full physical/CNF
   replay.
3. Radius two has an exhaustive 208-pair physical replay and a complete
   signed-lattice modular exclusion.
4. Every source-relative exact solution uses at least three seams outside
   \(S\).
5. The signed-recourse criterion (3.6) is exact for any finite outside set.
6. Every exact solution must meet the explicit 217-column semantic bank.

Not proved:

1. Feasibility or infeasibility with three or more outside seams.
2. Any full-branch `SSSSS` impossibility.
3. Satisfaction of q1, residence, separation, connectivity, or later physical
   rows by a signed-recourse survivor.
4. Existence of a literal carrier or compiler at \(C=106\).

Thus this is an exact source-relative expansion no-go and annealer cut, not a
claim that the full `SSSSS` branch is infeasible.

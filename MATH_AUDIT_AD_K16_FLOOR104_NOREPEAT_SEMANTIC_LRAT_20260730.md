# AD audit: K16 floor-104 no-repeat semantics and LRAT certificate

Date: 2026-07-30  
Lane: AD  
Verdict: **PASS, with physical port-capacity scope**

## 1. Audited claim

Fix the source-relative K16 seam catalogue

    scratch/k16_len8_source_seam_ledger_20260730.bin
    SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657.

Let \(D\) be its 93 zero-baseline targets and let the scale-two dual assign
weights \(b_t\in\{1,2,4\}\), with

\[
                         \sum_{t\in D}b_t=207.
\]

For a seam \(e:u\to v\), put

\[
 s_e=2+\phi_v-\phi_u-\sum_{t\in H(e)}b_t.
\]

The independently replayed dual proves \(s_e\in\mathbb Z_{\ge0}\) for all
211,604 seams.  The no-repeat equality face consists of Boolean seam
selections satisfying:

1. at most one selected incoming and at most one selected outgoing seam at
   each port;
2. equal selected indegree and outdegree at each port;
3. every target in \(D\) is serviced exactly once; and
4. \(\sum_e s_ex_e=1\).

The audited CNF is satisfiable if and only if this face is nonempty.  Its LRAT
certificate verifies, so this face is empty.

The port-capacity hypothesis is part of this particular CNF.  Consequently
this LRAT certificate alone does **not** refute the broader binary
endpoint-balance relaxation in which a port may carry several selected seams.
A separate no-capacity CNF/DRAT certificate closes that broader face; Section
7 records it.

## 2. Frozen construction and census

The current hardened builder is

    scratch/threadA_build_k16_floor104_exactonce_cnf_20260730.py
    SHA-256 59f5447c6687dfab76a4f579a780b45570b24ba626e765a17ea7d335d69ab411.

It pins both the binary above and the exact catalogue parser

    scratch/audit_k16_seam_ledger_permutation_20260730.py
    SHA-256 c88f13823c0c57a1934b5fcc541301fa13476bf2ca48b3fc614ed13087604ff2,

as well as the dual certificate

    scratch/k16_direct_cycle_dual_exact_20260730.audit.json
    SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d.

Exact reconstruction gives:

| object | count |
|---|---:|
| seams with \(s_e\le1\) | 74,879 |
| cycle-eligible seams after SCC pruning | 15,340 |
| cycle-eligible provider seams | 3,399 |
| cycle-eligible slack-one seams | 9,203 |
| active ports | 4,695 |
| CNF variables | 54,018 |
| CNF clauses | 135,771 |

The clause ledger is exact:

| block | clauses |
|---|---:|
| port activity | 40,070 |
| incoming at-most-one | 28,918 |
| outgoing at-most-one | 28,704 |
| target positive clauses | 93 |
| target at-most-one | 10,380 |
| slack-one positive clause | 1 |
| slack-one at-most-one | 27,605 |
| **total** | **135,771** |

## 3. SCC pruning is lossless

### Lemma 3.1

Every positive edge of a finite nonnegative integral endpoint-balanced
directed graph lies on a directed cycle.

### Proof

Let \(R\) be the vertices reachable from \(v\) through positive edges.  If
\(u\notin R\), then \(e\) is a positive edge entering \(R\), while no positive
edge leaves \(R\) by the definition of reachability.  Summing endpoint
balance over \(R\) says that its total positive inflow equals its total
positive outflow, a contradiction.  Hence \(u\in R\); a positive directed
path from \(v\) to \(u\), followed by \(e\), contains a directed cycle through
the chosen copy of \(e\). \(\square\)

Therefore any selected seam on the no-repeat face has both endpoints in the
same strongly connected component of the ambient \(s_e\le1\) graph.  Keeping
only the 15,340 cycle-eligible seams loses no feasible solution.  This
argument does not assume connectivity, unit voltage, or a single component.

## 4. Exact semantics of the port block

For each active port \(v\), the builder introduces an activity variable
\(a_v\).  For every outgoing or incoming seam variable \(x_e\), it adds
\(x_e\Rightarrow a_v\).  It also adds

\[
 a_v\Rightarrow\bigvee_{e\in\delta^+(v)}x_e,\qquad
 a_v\Rightarrow\bigvee_{e\in\delta^-(v)}x_e,
\]

and separate at-most-one constraints on the incoming and outgoing rows.

If \(a_v=0\), every incident selected-seam variable is zero.  If \(a_v=1\),
the two positive clauses and the two at-most-one blocks force exactly one
selected incoming and one selected outgoing seam.  Conversely, any
capacity-one balanced selection extends uniquely by taking \(a_v=1\) exactly
at its used ports.  Hence this block is equivalent to

\[
 \deg_x^-(v)=\deg_x^+(v)\in\{0,1\}.
\]

It is stronger than balance alone; this is precisely why the scope warning in
Section 1 is necessary.

## 5. Exact semantics of the cardinality blocks

The builder uses the Sinz sequential encoding for each at-most-one row
\(z_0,\ldots,z_{n-1}\).  Its state \(p_i\) may be extended as

\[
 p_i=\bigvee_{j\le i}z_j
\]

whenever at most one \(z_j\) is true, so every valid at-most-one assignment
has an extension.  Conversely, if \(z_i=z_j=1\) with \(i<j\), the clauses
propagate \(p_{j-1}=1\) from \(z_i\), while the clause for \(z_j\) forces
\(p_{j-1}=0\), a contradiction.  The encoding is therefore equisatisfiable
with at most one.  Adding the single positive row clause gives exact one.

The 93 target rows use Boolean seam incidence: \(H(e)\) is a set, so a target
appearing in two local slots of one seam contributes one literal, not two.
Thus the target blocks say exactly that each target is serviced once.  The
slack block says exactly one slack-one seam is selected.  Since all retained
seams have slack zero or one, this is equivalent to total slack one.

No explicit count-104 row is needed.  Summing the exact seam identities over
an endpoint-balanced exact-once selection cancels the potential:

\[
\begin{aligned}
\sum_e s_ex_e
 &=2\sum_ex_e-\sum_{t\in D}b_t\\
 &=2C-207.
\end{aligned}
\]

The slack exact-one row therefore gives \(1=2C-207\), hence \(C=104\).
This proves both directions of the claimed CNF/model equivalence.

## 6. LRAT replay

The frozen formula and proof are

    scratch/threadA_k16_floor104_exactonce_20260730.cnf
    SHA-256 4dbf00e3886f9f39419bf6e8e57ab90f3ef8838fb19d71f91ceca702e7dff2b4
    size 2,171,238 bytes;

    scratch/threadA_k16_floor104_exactonce_20260730.lrat
    SHA-256 955901bd496a9cc5f88b193eaad2fa5d637ba215cdc045a332db2bc12d97de6c
    size 9,792,776 bytes.

I independently reran

    /home/amodo/or15/drat-trim/lrat-check exactonce.cnf exactonce.lrat

on one H100 CPU.  The verifier itself has SHA-256

    e9e71c96b68dc9ed22db35d7581e613e6b161ffbc82c20cba5699f8320a065b8.

It parsed exactly 54,018 variables and 135,771 clauses, returned
“c VERIFIED”, exited zero, used 38,400 KiB maximum RSS, and took 0.12 seconds.
The independently rehashed remote CNF and LRAT exactly match the local hashes
above.

The earlier DRAT-to-LRAT lineage is also retained:

    DRAT SHA-256
    931ea827e6ccb37497a8cd09c984d35732d2ca4751cb125ae8735a67bd698fee;

    extracted core CNF SHA-256
    9d02ea5a9ecf240fa012655d841104004e58156162f0d17dab0af54672413465.

The LRAT check is the decisive UNSAT certificate; the solver's status is not
used as a premise.

## 7. Exact scope relative to the no-capacity theorem

This audited LRAT formula contains physical port capacity.  It proves:

> No capacity-one endpoint-balanced binary selection in the frozen catalogue
> services every target exactly once with total dual slack one.

For the broader binary balance/service relaxation with port capacity omitted,
the retained certificate is instead:

    full CNF SHA-256
    e1b89dd9da8a524baf1ed314eb6256d8cb0e9038e104043b94f68a9c4f7507d4;

    25,206-clause core CNF SHA-256
    c8be67536616d3bdd6fb9ed54e12e214b7abedc6c45860dfe52dd115a368d69c;

    core DRAT SHA-256
    80f00666ac026795fc1e1979b20efefee7ea1744ad55ce0f8180405579873da9;

    core-subset and DRAT audit SHA-256
    c60888ce8123d09ca5c07563e105bbd3aecdc87efc6395e5a15267862deb3119.

That separate proof, not this LRAT, supports any statement explicitly saying
that port capacity is omitted.

## 8. Provenance hardening

The original formula manifest has SHA-256

    29a1899e5e3959ca33ea21c173a09d01dd33ca7cfccf281bcdf811fb62fe9d0a

and records the earlier builder SHA \(7ebb92b2\ldots\).  The current builder
pins the parser as well as the binary and dual.  Its H100 rebuild produced the
same CNF byte hash and the hardened manifest

    scratch/threadA_k16_floor104_exactonce_hardened_20260730.manifest.json
    SHA-256 9efad108a2b8ec617b1360b6b12253b9ca9e70fac6466e05954c7bb6f380eefd.

Thus the current source-plus-parser lineage reproduces the exact certified
formula despite the historical builder-hash drift.

The structured audit record is

    scratch/ad_k16_floor104_norepeat_semantic_lrat_20260730.audit.json.

## 9. Final boundary

The no-repeat physical equality face is rigorously empty.  Combined with the
separate parity obstruction for the all-tight single-repeat face, this yields
the floor 105 for physical binary repairs inside the frozen catalogue.

No claim is made for repeated use of one seam, for a different carrier, for
noncatalogued or non-separated operations, or for attainability at 105.

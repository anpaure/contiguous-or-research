# AD audit: C106 fractional bases, five-lock faces, and the support-662 proof interface

Date: 2026-07-30  
Scope: frozen source-relative K16 seam ledger only.  No unrestricted K16 or word theorem is claimed.

## 1. Frozen provenance

The following inputs are used throughout.

- seam ledger: `scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256
  `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`;
- scale-two direct certificate:
  `scratch/k16_direct_cycle_dual_exact_20260730.audit.json`, SHA-256
  `29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d`;
- authenticated C106 lock normal form:
  `scratch/k16_c106_lock_normal_form_20260730.audit.json`, SHA-256
  `3c0121bdff5da978e048d88e46658223bc88afded3a9eb7cb0e3803834069f5f`;
- SSSSS floating basis JSON/TSV, SHA-256 respectively
  `e934799a0f881163e621236a530b4127253a4b032653eeb21876f40e81fad00a`
  and
  `e8cfd1c9f5ac8c68e49c8efeed9beae76334128b39a282a3cac126757deee494`;
- SSSSS exact rational audit/TSV, SHA-256 respectively
  `7f9780503ca106052044dc0b13604666509602e80f9bf7df6b091bbaa62c806e`
  and
  `bd12a626faa84fc0cef676bd2263d895ed5a63d34a59403a2ad111e27888268a`.

## 2. Exact 4^5 lock normal form

Let `b_t` be the frozen target prices, let `mu_t` be service multiplicity,
put

\[
 Q=\sum_t b_t(\mu_t-1),\qquad R=\sum_e s_e x_e.
\]

For every endpoint-balanced count-106 integral selection that covers all 93
targets, the exact direct identity gives

\[
 Q+R=2(106)-207=5. \tag{2.1}
\]

There are five disjoint lock triples, each consisting of three price-one
targets.  Let `q_j` be the total extra multiplicity in lock `j`, and let `A`
be the number of `j` for which `q_j` is odd.  The required lock syndrome has
Hamming weight `5-A`.  The authenticated automaton gives

\[
 5-A\le R.
\]

On the other hand

\[
 A\le\sum_jq_j\le Q=5-R.
\]

All inequalities are therefore equalities.  Consequently:

1. no target outside the five lock triples is repeated;
2. every repeated lock has exactly one extra occurrence;
3. the repeated locks are distinct;
4. every remaining lock contributes exactly one unit of slack syndrome.

Thus each lock independently chooses `S` or one of its three targets, giving
exactly

\[
 4^5=1024
\]

signatures.  The exact census by slack is

\[
(R=0,1,2,3,4,5): (243,405,270,90,15,1).
\]

This is a necessary normal form in the frozen balanced/service catalogue.  It
does not supply separation, q1, residence, survivor, or deeper-shadow rows.

## 3. Two LP domains that must not be conflated

For an arc `e=(u,v)` with service set `H(e)`, define its exact nonnegative
integer slack by

\[
 s_e=2+y_v-y_u-\sum_{t\in H(e)}b_t. \tag{3.1}
\]

There are two useful, but different, continuous models.

### 3.1 Unrestricted generic continuous model

Use every arc lying on a directed cycle of the full seam graph and impose

\[
0\le x_e\le1,
\quad Bx=0,
\quad \sum_{e\in\delta^+(v)}x_e\le1,
\quad \sum_ex_e=106,
\quad \sum_{e:t\in H(e)}x_e\ge1 \quad(t\in\mathcal T).
\tag{3.2}
\]

No threshold `s_e<=5` is valid for this unrestricted continuous LP: an arc
with `s_e>5` can occur with fractional mass below one.

### 3.2 Integer-WLOG fixed-signature model

For a lock signature with total slack `R`, an integral solution cannot select
an arc with `s_e>R`.  It is therefore WLOG for the integer face to fix all such
variables to zero before relaxing.  After SCC pruning, impose balance,
capacity, count 106, exact signature service multiplicities, and exact slack
`R`.

This is a valid integer presolve and a useful annealer seed LP.  It is a
strict strengthening of the unrestricted continuous model and must be labelled
as such.

The separate fail-closed exporter

`scratch/export_ad_k16_floor106_fractional_basis_v2_20260730.py`

implements both modes, pins the authenticated 1024-signature theorem, refuses
overwrites, runs only on the H100 CPU host, dumps the two-column annealer TSV,
all-variable basis/reduced-cost TSV, row activities and duals when exposed by
the backend, active capacity vertices, and a hashed annealer manifest.  A raw
`INFEASIBLE` status is deliberately labelled numerical until an exact Farkas
certificate is supplied.

## 4. The exact SSSSS fractional point

The all-slack signature has `R=5` and every target multiplicity exactly one.
Its exported positive support has 662 seams on three directed components with
`(vertices,edges)` pairs

\[
(2,2),\quad(4,4),\quad(565,656).
\]

Hence its circulation dimension is

\[
662-571+3=94.
\]

A deterministic decomposition gives 94 independent directed cycles.  The 93
service-once equations together with slack five have rank 94 over each of the
three checked primes.  Exact rational solution gives:

- edge-value denominator LCM
  `93159758129346024801758`;
- cycle-coefficient common denominator
  `14905561300695363968281280`;
- exact count 106;
- every target exactly once;
- exact slack 5;
- strict capacity, with maximum outgoing mass
  `37778099230409452138842 / 46579879064673012400879 < 1`.

Thus the LP point is genuine and nondegenerate with respect to its 94 cycle
coordinates.  It is not an integral solution.

## 5. Exact support no-go and global escape cut

The independent solver-free parity audit

`scratch/ad_k16_c106_sssss_support_parity_escape_20260730.audit.json`

has SHA-256
`d44c78780df5be82808d42f61ce1337f0f3cb18cde307f0222cf30a52c8705f5`.
On the 94 cycle variables its mod-two service system has rank 89, whereas the
augmented system has rank 90.  Equivalently, every support edge has a frozen
endpoint-coboundary parity, so every balanced support selection has even
service parity on a named set of 33 targets, while SSSSS requires odd parity.
Therefore the 662-column binary face is impossible.

The same audit evaluates the parity on the global column bank.  There are
9,311 slack-at-most-five seams with odd escape label, and every integral SSSSS
solution obeys

\[
 \sum_{e:\rho_e=1,\ s_e\le5}x_e\equiv1\pmod2. \tag{5.1}
\]

All 662 support seams have label zero.  Hence every global solution must leave
the support.

For an expansion using exactly one outside seam, balance after contracting
the support components forces its endpoints into the same support component.
Exactly 298 odd-labelled seams satisfy this necessary condition.  Their
deterministic bank is

`scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv`, SHA-256
`cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600`.

This is the smallest exact radius-one expansion bank.  Failure on those 298
columns would prove radius one impossible; it would not by itself exclude a
two-or-more-column expansion.

## 6. Proof-ready CNF interface

The new deterministic emitter is

`scratch/emit_ad_k16_c106_sssss_support662_cnf_20260730.py`.

It pins all six binary/certificate/JSON/TSV hashes above and maps primary
variables `1,...,662` to the floating/exact TSV seam order.  It encodes:

- incoming and outgoing port capacity one;
- exact endpoint balance through a common port-activity bit;
- exactly one provider for each of the 93 targets;
- weighted seam slack exactly five.

An explicit 106-cardinality counter is unnecessary.  From (3.1), balance
telescopes the potential, exact target service contributes 207, and slack
contributes five, so every assignment already satisfies

\[
2\sum_ex_e=207+5=212.
\]

Using the frozen support incidence census, the emitted formula has exactly

\[
2251\text{ variables},\qquad 5588\text{ clauses}.
\]

This removes 65,163 auxiliary variables and 259,885 clauses from the earlier
explicit-count formula without changing its satisfying primary assignments.

The independent checker

`scratch/verify_ad_k16_c106_sssss_support662_cnf_20260730.py`

authenticates the input hashes, full DIMACS syntax and hash, primary seam map,
and physical arc records.  Given a complete SAT assignment, it checks every
clause and independently replays count, balance, capacity, all 93 service rows,
and slack.  An UNSAT result must still be frozen as DRAT/LRAT and checked
against the exact emitted CNF hash; solver status alone is not promoted.

## 7. Exact boundary

Proved:

1. all C106 integral selections in the frozen balanced/service catalogue lie
   in one of exactly 1024 lock signatures;
2. the SSSSS LP has the stated exact positive 662-seam rational point;
3. no integral SSSSS selection is supported wholly on those 662 seams;
4. every global SSSSS selection crosses the explicit odd escape bank, and a
   radius-one escape must use one of 298 enumerated seams;
5. the support face has a deterministic small proof-producing CNF interface.

Not proved:

- infeasibility of the full SSSSS branch;
- infeasibility of any of the other 1023 lock signatures;
- separation, q1, residence, survivor, deeper-shadow, connectivity, or literal
  word feasibility for a C106 selection.


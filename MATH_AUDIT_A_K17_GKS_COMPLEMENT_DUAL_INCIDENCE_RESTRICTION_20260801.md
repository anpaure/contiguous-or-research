# `k=17`: complement-dual incidence restriction on the authenticated GKS age seeds

Date: 2026-08-01  
Lane: A, changing-owner chronology  
Status: exact quotient phase law and independently replayed negative census
for two fixed incidence matchings; the companion odd-graph zero-row theorem
now rules out every incidence matching on this fixed flag catalogue

## 1. Convention and exact phase law

Let `L` be the rank-eight necklace shore and `O` the rank-nine owner shore.
Bitwise complement is the shore-reversing involution

\[
 C:L\leftrightarrow O,
 \qquad C(\rho^u X)=\rho^uC(X).
\]

Fix one incidence perfect matching `D:L->O`.  For each stored rank-eight
representative `Q_p`, choose an attachment `alpha_p` and write

\[
 D(Q_p)=T_p=Q_p\cup\{\alpha_p\}.                  \tag{1.1}
\]

Define the complement-dual matching

\[
                         H=C D^{-1}C.              \tag{1.2}
\]

The quotient phase action in (1.2) is the following.  Let `r` be the unique
selected packet whose owner orbit is `[C(Q_p)]`, and let `u` be the unique
phase satisfying

\[
                         \rho^uT_r=C(Q_p).          \tag{1.3}
\]

Then

\[
 R=\rho^uQ_r,\qquad H(Q_p)=C(R).                   \tag{1.4}
\]

Let `q` be the unique selected packet whose owner orbit is `[H(Q_p)]`, and
let `v` be the unique phase such that

\[
                         \rho^vT_q=H(Q_p).          \tag{1.5}
\]

Thus the forced changing-owner successor of packet `p` is the phase-`v`
copy of packet `q`.  Equivalently, on unphased quotient packets its
successor is

\[
                         (D^{-1}C)^2(p).            \tag{1.6}
\]

### Lemma 1.1

Equations (1.3)--(1.5) always give a rank-eight/rank-nine incidence, and
the forced successor map is a permutation.

#### Proof

Since `Q_r subset T_r`, (1.3) gives
`R subset C(Q_p)`.  Complementing reverses containment, so
`Q_p subset C(R)=H(Q_p)`.  Hence (1.4) is an incidence edge.  Complement
and `D` are bijections, so `H` is a perfect matching; composing `H` with
`D^{-1}` gives the successor permutation.  Freeness of the `Z_17` action
on proper nonempty subsets makes both recorded phases unique. `square`

For the phase-`v` target flag put

\[
 D_i=\rho^vC^q_i\ (0\le i\le2),\qquad
 D_3=\{\rho^v\alpha_q\}.
\]

The forced incidence is a literal age turn exactly when its two owners are
distinct and

\[
 D_1\subseteq C^p_0,qquad D_2\subseteq C^p_1,qquad
 D_3\subseteq C^p_2,                               \tag{1.7}
\]

\[
 D_0=\{\beta\}\mathbin{\dot\cup}(C^p_0-D_1)
      \mathbin{\dot\cup}(C^p_1-D_2)
      \mathbin{\dot\cup}(C^p_2-D_3),              \tag{1.8}
\]

where `H(Q_p)=Q_p+beta`.  This is precisely the authenticated
changing-owner criterion, now applied to the single head forced by (1.2).

## 2. Primary seed, natural incidence matching

Take

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_20260801.tsv
SHA256 908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451
```

and choose the natural matching (1.1) from each row's stored `C3`
singleton.  The 1,430 selected owner orbits are distinct.  Literal replay
of (1.3)--(1.8) gives

```text
nonincidence or phase-alignment failures       0
forced literal age turns                     421
forced age-incompatible turns               1009
degenerate equal-owner incidences               0
survivor failures C1,C2,C3              901,588,391
refresh-identity failures                    1009
```

The survivor counts overlap.  In this census every incompatible row also
fails the refresh identity; this is an observed exact equality for the
frozen seed, not an asserted general equivalence.

The complete kind/type census is:

| packet kind/type | total | legal | incompatible | survivor failures `1,2,3` |
|---|---:|---:|---:|---:|
| broken pair / 1 | 107 | 17 | 90 | 90,6,4 |
| broken pair / 2 | 4 | 1 | 3 | 3,1,0 |
| broken pair / 4 | 9 | 3 | 6 | 6,1,0 |
| broken pair / 5 | 66 | 15 | 51 | 47,21,3 |
| broken pair / 7 | 100 | 20 | 80 | 68,45,2 |
| native pair / 1 | 190 | 34 | 156 | 155,79,71 |
| native pair / 2 | 4 | 0 | 4 | 4,3,1 |
| native pair / 4 | 11 | 1 | 10 | 9,7,3 |
| native pair / 5 | 74 | 16 | 58 | 49,47,23 |
| native pair / 7 | 137 | 24 | 113 | 84,95,47 |
| skip / 0 | 139 | 4 | 135 | 130,89,111 |
| skip / 3 | 20 | 2 | 18 | 17,16,15 |
| skip / 6 | 127 | 3 | 124 | 101,115,98 |
| triple / 8 | 442 | 281 | 161 | 138,63,13 |

Thus the complement-dual incidence factor is perfectly defined but is not
a changing-owner age factor for this fixed `D`.

Its quotient successor has 146 cycles, largest length 77.  Every quotient
cycle has nonzero voltage, so the physical lift also has exactly 146
components.  The failure is therefore neither incidence, phase alignment,
nor zero voltage; it occurs before any Hamilton joining, in the literal age
rows (1.7)--(1.8).

## 3. Checkpoint and selected-transversal calibrations

For the earlier seed2509 natural matching, the same incidence topology has

```text
legal / incompatible = 431 / 999,
quotient cycles = physical components = 146,
largest quotient cycle = 77.
```

Hence low-containment optimization from seed2509 to seed2512 improves the
unrestricted packet projection but slightly worsens this particular
complement-dual face.

The independently frozen state transversal

```text
scratch/selected_seed2511.tsv
SHA256 a349c8293f0e1e531e1c301f24a0532a55d49499a3811e2ce699e599d01560ab
```

is also an incidence perfect matching for seed2512.  Under (1.2) it gives

```text
nonincidence or phase-alignment failures        0
legal / incompatible                         297 / 1133
degenerate equal-owner incidences                  80
quotient cycles / largest                    102 / 579
zero-voltage quotient cycles                       80
physical lift components                         1382
```

The 80 degeneracies are doubled incidence edges rather than Johnson turns.
This transversal was optimized for the unrestricted dynamic graph, not for
the complement-dual relation, and does not supply a dual age factor.

## 4. Exact conclusion and resolved incidence-matching quantifier

For each of the two tested `D` matchings, a single violated row of
(1.7)--(1.8) is an exact obstruction to using `H=C D^{-1}C`; the displayed
censuses close those fixed faces.

A subsequent packet-support audit resolves the formerly open quantifier on
`D` for this fixed flag catalogue.  The complete turn TSV has 202 packet
roots with no nonloop successor.  Its sole packet-loop turn is based at
packet 559, which is outside that set.  Hence those same 202 roots have no
successor at all, after all nine attachments and all relative rotations are
allowed.  But every complement-dual matching forces the successor
`A^2(p)`, where `A=CD`, at every packet `p`.  Therefore no incidence
perfect matching `D` gives a literal age-compatible complement-dual
two-factor on these fixed flags.

Equivalently, the would-be global search would have had to choose `D` while
enforcing a three-state local constraint:

1. the state selected at `Q_p` supplies the source flag;
2. the state selected at owner orbit `[C(Q_p)]` determines `H(Q_p)`; and
3. the state selected at owner orbit `[H(Q_p)]` supplies the phase-rotated
   target flag.

The 202 empty source rows make that system infeasible before its
three-state correlation is considered.  This is not an obstruction to a
different static flag catalogue obtained by further GKS switches, nor to
the unrestricted two-matching incidence master.

The strengthened statement and the direct odd-graph replay are frozen in
`MATH_THEOREM_A_K17_GKS_COMPLEMENT_DUAL_ODD_GRAPH_OBSTRUCTION_20260801.md`.

## 5. Reproducibility

The O3 C++ census was run on the H100 CPU in

```text
/home/amodo/or15/work/threadA_k17_complement_dual_20260801
```

under a 2 GiB address-space and 120-second CPU cap.

```text
scratch/audit_threadA_k17_gks_complement_dual_incidence_20260801.cpp
  SHA256 797342d510880395821954b2f22aec73533ce5430fa24a81fcb3ac50b32b875a
H100 binary
  SHA256 26bc98b99f9bdd36bc0440f81960025e5fc2d7370ccbc6ef3f63f4c4dc6a6c83
scratch/verify_threadA_k17_gks_complement_dual_incidence_20260801.py
  SHA256 9d6c016581bb2353eb44f301bf124a57da54f65f74718a63d12b77054a759a4e
```

Primary natural-matching artifacts:

```text
scratch/threadA_k17_gks_complement_dual_seed2512_natural_20260801.forced.tsv
  SHA256 67a902e3c62fde065c027fafc3f43a725904dc3d25b71a0752227663086feedc
scratch/threadA_k17_gks_complement_dual_seed2512_natural_20260801.audit.json
  SHA256 df1b9ae7ad66d2867f1fa6bc857ec901944a564613160fa55695c55bb9593198
scratch/threadA_k17_gks_complement_dual_seed2512_natural_independent_20260801.audit.json
  SHA256 362d12e740cff3f372734bbc4031c99ad3b3d1ed6ace4631f3ec32bb39a29fe2
```

The independent Python replay reconstructs every complement phase, forced
head, successor, failure mask, cycle and voltage directly from the flags
and selected matching before comparing the C++ TSV and JSON.

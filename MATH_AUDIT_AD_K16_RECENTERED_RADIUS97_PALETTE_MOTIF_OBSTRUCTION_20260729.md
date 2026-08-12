# AD audit: exact recentered radius-97 palette/motif obstruction at \(k=16\)

Date: 2026-07-29  
Lane: AD  
Status: **proved solver-free no-go at deletion radius at most \(97\)**

## 1. Result

Let \(F_1\) be the \(C_{15}\)-equivariant quotient factor

~~~text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8
~~~

Its current residence-motif hypergraph has a checked \(97\)-motif
edge-disjoint packing and a checked \(97\)-edge transversal. Therefore

\[
\nu(\mathcal H(F_1))=\tau(\mathcal H(F_1))=97.
\]

### Theorem 1.1 (radius-97 palette/motif obstruction)

There is no \(C_{15}\)-equivariant quotient degree-two factor \(F'\), even if
quotient loops are admitted, satisfying all three conditions:

1. \(F'\) deletes at most \(97\) selected quotient edge orbits of \(F_1\) and
   inserts the same number of quotient edge orbits;
2. \(F'\) destroys every current positive short-run motif of \(F_1\);
3. \(F'\) covers every upper-\(q1\) colour orbit.

Consequently any such repair has deletion radius at least

\[
98.
\]

The proof uses degree-two restoration and upper-\(q1\). It does not use
lower-\(q1\), top residence, connectivity, voltage, or fresh-motif CEGAR.

## 2. Exact source and min--max census

The source selects \(858\) distinct loopless quotient edge orbits and is
quotient degree two. Its exact audit gives:

~~~text
lower-q1 orbit support       764
upper-q1 orbit support       764
quotient components            3
physical components             5
top/complement-top residence  PASS
physical positive short runs 2205
distinct positive motifs       147
complemented-top motifs          0
~~~

Each palette's \(764\) quotient colour orbits represent all \(11{,}440\)
literal colours: \(762\) orbits have size \(15\), and two have size \(5\).

The motif-size histogram is

~~~text
size 2 : 10
size 3 : 61
size 4 : 76
~~~

The motif overlap graph has \(85\) components, with size histogram

~~~text
1:49, 2:24, 3:6, 4:3, 5:1, 6:1, 9:1.
~~~

The frozen min--max certificate is

~~~text
scratch/k16_dynamic_cross_r147_round0_residence_tau97_20260729.certificate.json
SHA-256 6d6261267e9d2e9883b4afb2929b27ccbc8e005d4cd35fc068b628fefa414117
~~~

The explicit packing proves \(\nu\ge97\), the explicit transversal proves
\(\tau\le97\), and \(\nu\le\tau\) proves equality. Exhaustive-search
optimality is not needed after checking these two witnesses.

Let \(U\) be the union of the \(97\) packed motifs. The exact census is

~~~text
|U|                         322
AA / AB / BB in U     159 / 26 / 137
endpoint quotient nodes     407
off-source induced nonloops 5910
off-source induced loops      13
all induced additions        5923
~~~

### Lemma 2.1 (exposed minimum-radius face)

If a deletion set \(D\) meets every current motif and \(|D|\le97\), then

\[
|D|=97,\qquad D\subseteq U,
\]

and \(D\) contains exactly one edge from every packed motif.

#### Proof

The \(97\) packed motifs are edge-disjoint, so meeting all of them requires
at least \(97\) distinct deletions. The assumed upper bound forces equality.
Every deletion is already used on one packed motif, so no deletion lies
outside their union. Pairwise disjointness gives exactly one deletion in each.
\(\square\)

### Lemma 2.2 (complete addition universe)

Suppose \(F'=(F_1\setminus D)\cup A\) is quotient degree two and
\(D\subseteq U\). Every endpoint of every added edge lies among the \(407\)
nodes \(V(U)\). Thus \(A\) lies in the exact \(5923\)-edge off-source
catalogue induced on \(V(U)\): \(5910\) nonloops and \(13\) quotient loops.

#### Proof

At each quotient node, deleted incidence equals added incidence. A quotient
loop counts twice. A node outside \(V(U)\) has no deleted incidence, hence
cannot receive an added nonloop incidence or an added loop. Therefore every
addition is induced on \(V(U)\). The displayed census is an exact catalogue
scan. \(\square\)

## 3. The two-row contradiction

### 3.1 Forced deletion

Motif number \(66\) in the frozen ordering is

\[
M_{66}=\{22511,22692,25634\}.
\]

It has the literal witness

\[
34611\xrightarrow{22511}34643
\xrightarrow{22692}35667
\xrightarrow{25634}35635.
\]

In coordinate \(6\), the four vertex bits are \(0,1,1,0\), so the middle
vertices form a positive run of length \(2\). The same motif occurs in all
\(15\) rotations.

The exact packing-union ledger is

\[
M_{66}\cap U=\{22511\},\qquad
M_{66}\setminus U=\{22692,25634\}.
\]

Lemma 2.1 fixes the latter two edges. Destroying this run therefore forces

\[
22511\in D. \tag{3.1}
\]

### 3.2 Forced retention

Edge orbit \(22511\) has catalogue data

~~~text
u=34611, v=34643, node_u=611, node_v=617,
lower colour=(1,1811), upper colour=(1,1907).
~~~

The complete provider list for upper-\(q1\) orbit \(c=(1,1907)\) is

~~~text
4960 4961 4962 4963 4964 4965 4966 4967
18169 18170 18171 18172 18173 18174 18175
18660 18661 18662 18663 18664 18665
20334 20335 20336 20337 20338
21568 21569 21570 21571
22511 22512 22513 22688 22689 22777
~~~

Exact intersections give

\[
\begin{aligned}
P(c)\cap F_1&=\{22511\},\\
P(c)\cap(F_1\setminus U)&=\varnothing,\\
P(c)\cap E_{\rm add}^{\rm nonloop}&=\varnothing,\\
P(c)\cap E_{\rm add}^{\rm loop}&=\varnothing.
\end{aligned}
\]

This colour orbit has literal size \(15\). Lemma 2.2 proves that the two
addition families exhaust every degree-compatible addition at this radius.
Upper-\(q1\) completeness therefore forces

\[
22511\notin D. \tag{3.2}
\]

Equations (3.1) and (3.2) contradict, proving Theorem 1.1. \(\square\)

## 4. H100 model and transcript audit

The clean generic model, built from the same byte-exact source and
certificate, has:

~~~text
cut variables                 322
add variables                5910
top-boundary variables        858
top-reach variables         11872
total variables             18962
total constraints           14672
active lower-q1 rows          268
active upper-q1 rows          261
~~~

The CP model itself is loopless. It permits AA, AB, and BB changes, enforces
degree two and both \(q1\) palettes, and includes exact top boundary/reach
rows plus literal positive/complemented-top CEGAR. It deliberately omits
AddCircuit and unit voltage. The solver-free theorem above extends beyond
this model to the \(13\) candidate quotient loops by a separate exact census.

On H100 CPU with OR-Tools CP-SAT 9.15.6755 and exactly eight workers:

~~~text
status       INFEASIBLE
branches     0
conflicts    0
wall time    0.0279629 s
~~~

The model proto exposes the same proof:

~~~text
constraint 109:  +cut_22511 >= 1
constraint 956:  -cut_22511 >= 0
~~~

Variable \(266\) is cut_22511. Constraint \(109\) is motif \(66\) after its
two outside-\(U\) edges are fixed. Constraint \(956\) is upper orbit
\((1,1907)\) after unavailable providers are removed.

Thus the CP transcript is corroborating evidence only. The theorem is a
solver-free two-row certificate. No incumbent existed, so the atomic
per-incumbent checkpoint requirement was vacuous for this run. The hardened
driver still archives every future callback incumbent atomically, and resume
recomputes rather than trusts imported lazy rows.

## 5. Frozen artifacts

~~~text
source factor
  scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
  d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8

min--max certificate
  scratch/k16_dynamic_cross_r147_round0_residence_tau97_20260729.certificate.json
  6d6261267e9d2e9883b4afb2929b27ccbc8e005d4cd35fc068b628fefa414117

hardened generic driver
  scratch/threadD_generic_k16_tau_descent_cegar_20260729.py
  6ee671e56c99bab61f73d659f989295b4f07c000a3566f3ba85dc6768dcba0b6

runbook
  scratch/run_ad_k16_radius97_recentered_20260729.sh
  2391aad4bdf8dba35dbf7c8fcce5c8f1b772d1ae69bdf52def92cf74fb522148

H100 result
  scratch/ad_k16_radius97_recentered_20260729/ad_k16_tau97_recentered_s16901.json
  7fbc2f6d5189f92806ad7a9c129bcda8b569588cd160b3cfe229bffb1521380a

H100 log
  scratch/ad_k16_radius97_recentered_20260729/ad_k16_tau97_recentered_s16901.log
  4a1a7c08549d7605e9a12ad305860c7b42bef9d786ada00491a76f6e885ae764

H100 model proto
  scratch/ad_k16_radius97_recentered_20260729/ad_k16_tau97_recentered_s16901.model.pb
  ac5b511055d04954efa0889b144d8b60111333f55594c0b4b2bcb5b8a20f7bf6

solver-free auditor
  scratch/audit_ad_k16_radius97_palette_motif_obstruction_20260729.py
  11aab5e98df4797a0ac961ad93a63eab22312e8c006fbfa637eceb89fc320278

solver-free PASS output
  scratch/ad_k16_radius97_palette_motif_obstruction_20260729.audit.json
  bebde1c85517f51c8f31cad6f909d4898eebc675f30d88f5f7ee4a72d2ad84da
~~~

The source JSON's embedded payload digest is stale. Provenance uses its
whole-file SHA above, which the min--max certificate pins and the driver
independently replays.

## 6. Exact boundary and next gate

Proved:

- the current motif identity is exactly \(\tau=\nu=97\);
- the \(322\)-edge packing union and \(407\)-node addition portal are exact;
- any \(C_{15}\)-equivariant degree-two, upper-\(q1\)-complete repair
  destroying all current motifs has deletion radius at least \(98\), even
  with quotient loops;
- all catalogue edge orbits have physical size \(15\), so this means at least
  \(1470\) physical Johnson-edge deletions and physical symmetric difference
  at least \(2940\).

Not proved:

- feasibility or infeasibility at radius \(98\);
- a resident connected physical Hamilton cycle at \(k=16\);
- any non-equivariant radius bound;
- dual-zero residence in the other fifteen coordinates;
- a final contiguous-OR compiler.

At radius \(98\), one deletion may leave the \(322\)-edge packing union. The
next exact problem is a one-extra-cut portal: can one outside-\(U\) deletion
free an alternative provider of upper orbit \((1,1907)\), while the other
\(97\) deletions meet the packed motifs and degree two and both palettes stay
exact? This is the smallest neighborhood not closed by Theorem 1.1.

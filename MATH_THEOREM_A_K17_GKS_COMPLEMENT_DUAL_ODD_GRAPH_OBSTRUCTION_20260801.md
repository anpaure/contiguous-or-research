# `k=17`: complement-dual odd-graph test of the switched GKS seed

Date: 2026-08-01  
Lane: A / complement-dual chronology  
Status: exact obstruction for the authenticated 1,158-support flag seed; no unrestricted obstruction to another flag factor

## 0. Verdict

Let `D` be an incidence perfect matching from rank-nine owner orbits to
rank-eight facet orbits, and let `C` be set complementation between the two
shores.  The complement-dual restriction

\[
                         H=CD^{-1}C                  \tag{0.1}
\]

does **not** produce a state/owner-compatible two-factor from the
authenticated switched GKS seed of SHA

```text
908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451.
```

The obstruction is already visible before choosing `D`: the exact
loop-free changing-owner support has 202 packet rows with no successor.
There is only one packet-loop turn, at packet 559, and packet 559 is not
among those 202 rows.  Thus all 202 rows have no successor even after loops
are restored.  Any complement-dual two-factor forces one successor at every
packet, so none exists on this flag certificate.

The 202 universal zero-successor rows have the following exact kinds:

```text
pair_broken 45     pair_native 75     skip 81     triple 1.
```

By age type `0,...,8` their multiplicities are

```text
(10,60,1,1,0,13,70,46,1).
```

For the stored owner attachment matching `D_0`, the stronger literal
dual replay has only 421 supported forced turns and 1,009 failed forced
turns.  Thus the failure is not a topology-only defect.

## 1. Odd-graph normal form

Identify the complement of a rank-eight facet with a rank-nine owner.  Put

\[
                             A=CD.                   \tag{1.1}
\]

If `D(a)=Q subset a`, then

\[
                  A(a)=Q^c,qquad |a\cap A(a)|=1.    \tag{1.2}
\]

Hence `A` is a permutation using only odd-graph incidences.  Since
`H^{-1}=CDC`, the owner successor in the two-factor `D union H` is

\[
                         H^{-1}D=A^2.                \tag{1.3}
\]

Consequently `A` determines the complete complement-dual two-factor, and
its turn at `a` is fixed by the singleton labels on the two adjacent
odd-graph incidences.  In particular no independent choice of the second
matching or of its q1 colours remains.  This is the useful reduction behind
(0.1).  Requiring `A` itself to be one cycle is the connected odd-graph
subclass suggested in the question.

Because 1,430 is even, if `A` is one 1,430-cycle then `A^2` is exactly two
cycles of length 715.  Thus the direct `A`-cycle face targets an exact
two-factor with two quotient components; it does not by itself give a
one-cycle owner chronology.

For an `A`-cycle on 1,430 vertices, `A^2` has no fixed point, so every
forced chronology turn is nonloop.  For a general `A`, fixed points can
occur; the separate loop census above handles that possibility.

## 2. Exact zero-row obstruction

For a packet `p`, let `Gamma(p)` be the set of packets `q`, including
`q=p`, for which some attachment states and some recorded relative phase
give a literal changing-owner arc `p -> q`.

### Theorem 2.1

If a packet flag system admits a complement-dual two-factor, then

\[
                         \Gamma(p)\ne\varnothing
                         \quad\hbox{for every }p.    \tag{2.1}
\]

#### Proof

Choose the owner attachment used by `D` at packet `p`.  Equations
(1.1)--(1.3) force its successor to be the packet occupied by `A^2(a)`.
State/owner compatibility requires the corresponding literal age
transition, hence that successor lies in `Gamma(p)`.  `square`

The independent exact graph replay gives 202 packets with no nonloop
successor.  Its sole loop is based at packet 559, outside this set, so the
same 202 packets violate (2.1).
This proves the negative verdict without a SAT search and without choosing
an owner transversal.  The number 202 is the exact cardinality of the
unavoidable row obstruction for this certificate.  It is not asserted to
be the minimum number of failed forced turns over all imperfect
complement-dual transversals; it is a certified lower bound on every such
attempt.

## 3. Stored-matching replay

The static certificate itself supplies a distinguished incidence perfect
matching `D_0`: packet `p` uses the owner

\[
                     T_p=Q_p\mathbin{\dot\cup}C^p_3.
\]

For this matching, `A_0=CD_0` is a permutation with 146 cycles.  Its exact
cycle-length histogram is

```text
length  1  3  5  7  9  11 13 21 27 33 45 77
count   6 10 44 34 24   6  1 12  2  1  5  1.
```

Thus `D_0` fails the one-`A`-cycle topology condition.  Nevertheless its
odd-graph turns are already fully surjective on the complementary upper-q1
palette: the 1,430 turns cover all 1,144 rank-seven necklace colours, with
load histogram

```text
load 1: 866 colours;  load 2: 270 colours;  load 3: 8 colours.
```

Equivalently, the corresponding rank-ten union palette is complete.  This
confirms that q1 colour supply is not the failure of the stored dual
factor.  Testing every forced `A_0^2` successor against the literal age
equations gives

```text
supported forced turns  421
failed forced turns    1009.
```

The 1,009 failures by source packet kind are

```text
pair_broken 230     pair_native 341     skip 277     triple 161,
```

and by source age type `0,...,8` are

```text
(135,246,7,18,16,109,124,193,161).
```

Every failed row violates the refresh identity.  The three survivor
containments fail, with overlap, on respectively

```text
901, 588, 391
```

rows.  Hence merely changing the phase of the forced second matching cannot
repair this projection.

Every one of the 146 quotient `A_0` cycles has nonzero accumulated
`Z_17` voltage.  Its physical lift is therefore one component, rather than
17, and the stored geometric factor has exactly 146 physical components.
The component count and the age incompatibilities are separate defects.

For completeness, the source-type/target-type matrix of failed forced
turns is

```text
       target type 0  1  2  3  4  5  6  7  8 | row
source 0          28 29  0  2  1 21 22 19 13 | 135
source 1          33 57  3  7  3 25 20 61 37 | 246
source 2           1  2  0  0  0  0  1  3  0 |   7
source 3           5  5  1  1  0  1  2  2  1 |  18
source 4           1  2  0  0  2  4  0  2  5 |  16
source 5          10 37  2  0  3 12  7 17 21 | 109
source 6          34 21  0  8  1  9 25 20  6 | 124
source 7          17 48  0  1  3 30 19 29 46 | 193
source 8           8 78  2  1  4 14 14 19 21 | 161.
```

## 4. Scope

This is a decisive no-go for projecting the stated 1,158-support GKS flag
certificate into the complement-dual `A`-cycle face.  It does not rule out:

* another static flag factor obtained by further low or central GKS
  switches;
* a complement-dual factor with several `A` components if loop turns are
  admitted for a weaker target; or
* K's unrestricted two-matching incidence/deletion-spine master.

Indeed the exact central `2 x 2` switch theorem already changes the support
by one unit.  What is ruled out is the proposed shortcut on the frozen
1,158 certificate.

## 5. Independent replay artifacts

The odd-graph replay

```text
scratch/verify_threadA_k17_gks_complement_dual_oddgraph_face_20260801.py
  SHA256 ebbb209a40972913c4c19ef0a3feced3e9315d88d645b69cde829d7e7e9f302f
scratch/threadA_k17_gks_complement_dual_oddgraph_seed2512_20260801.audit.json
  SHA256 6f3bd75fc9b6d13ec901a7295e1e1c3b0ef48b026daba534d78586645bb72146
```

reconstructs `A`, its phases, all turn colours, all forced `A^2` age rows,
and the full zero-packet set directly from the switched flags and turn TSV.
It is independent of the H100 complement-dual census.

The latter supplies an occurrence-labelled forced-turn certificate and a
second independent replay:

```text
MATH_AUDIT_A_K17_GKS_COMPLEMENT_DUAL_INCIDENCE_RESTRICTION_20260801.md
  SHA256 e1fd757e7037012a5a672235514ab3ee336735c587295c1fe1371069ee7d9a58
scratch/threadA_k17_gks_complement_dual_seed2512_natural_20260801.forced.tsv
  SHA256 67a902e3c62fde065c027fafc3f43a725904dc3d25b71a0752227663086feedc
scratch/threadA_k17_gks_complement_dual_seed2512_natural_independent_20260801.audit.json
  SHA256 362d12e740cff3f372734bbc4031c99ad3b3d1ed6ace4631f3ec32bb39a29fe2
```

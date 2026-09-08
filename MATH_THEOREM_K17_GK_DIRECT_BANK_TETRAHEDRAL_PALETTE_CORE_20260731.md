# K17 adjacent-GK direct banks: a q9-free tetrahedral palette obstruction

Date: 2026-07-31  
Status: **proved finite direct-bank obstruction** for each of the explicit
`7abc` and `8afb` banks.  This is not an unrestricted `s=1` or K17 no-go.

## 1. Exact scope of the reported round-zero UNSAT

The reported artifact

```text
scratch/independent_k17_gk_shift1_stageB_fullturn_20260731.result.json
```

uses direct bank

```text
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d.
```

Its only solver round is round zero.  It ends `INFEASIBLE` with zero
branches, zero conflicts, and zero local-component cuts.  Consequently no
ear-shape, ear-length, cycle, or connectivity cut participated in that
result.  The status text `WITH_CUTS` is misleading for this particular run.

The round-zero master nevertheless contains the aggregate ledger

\[
 |F|=12698,\qquad \sum_{b\in B}d_F(b)=6134,\qquad
 |\{u\in U:d_F(u)=2\}|=9631.                         \tag{1.1}
\]

The displayed values `2637/430` occur only in audit metadata and in a
post-SAT component replay.  They are not model rows.  Thus the original
round-zero result is independent of the arrangement and individual lengths
of the proposed ears, but not, by itself, independent of the aggregate
totals (1.1).

The raw catalogue also deserves a scope correction.  It enumerates every
eligible residual EU/UU Johnson edge after old/direct lower, upper, and base
reservations; it is not restricted to the supported-provider relation.  For
`7abc` it has 413,268 edges, whereas the conditioned supported-provider
relation has 242,771 incidences.  No equivalence of these two catalogues is
proved or needed: infeasibility of the larger raw relaxation is stronger.

As written, catalogue construction also deletes an EU edge when its boundary
rank-nine label belongs to the fixed direct bank.  Hence merely deleting the
master's `AllDifferent` row does not by itself remove every q9 dependency.
Section 2 removes that catalogue filter as well.

## 2. The corrected four-family relaxation

Fix one of the two direct banks.  Remove its 572 lower-colour coverage
obligations (candidate edges carrying those lower colours remain allowed),
reserve its 572 fresh upper colours and 1,144 base endpoints, but do **not**
delete any candidate because of a fixed boundary-q9 collision.  Let
\(\mathcal E\) be every raw Johnson edge on the remaining base vertices and
all unused rank-seven vertices, subject only to:

1. no further base--base (`BB`) edge is allowed;
2. an upper colour used by the old seed or direct bank is unavailable.

For \(F\subseteq\mathcal E\), retain only these four constraint families:

\[
\begin{aligned}
&d_F(D)\ge1 &&\text{for every residual required rank-six colour }D,\\
&d_F(Q)\le1 &&\text{for every fresh rank-eight colour }Q,\\
&d_F(b)\le1 &&\text{for every residual base vertex }b,\\
&d_F(u)\in\{0,2\} &&\text{for every unused rank-seven vertex }u.
                                                               \tag{2.1}
\end{aligned}
\]

There is no selected-edge total, base-incidence total, active-\(U\) total,
rank-nine row, distinct-addition row, supported-provider row, component row,
or topology row in (2.1).

### Theorem 2.1 (direct-bank tetrahedral obstruction)

For each of the explicit `7abc` and `8afb` direct banks, system (2.1) is
infeasible.

The infeasibility has a 26-row certificate:

\[
4\text{ lower rows}+11\text{ upper caps}
 +2\text{ base caps}+9\text{ unused-vertex rows}.       \tag{2.2}
\]

### Proof

Write \(a,b,c,d=1,2,3,4\).  For `7abc` take

\[
 C=\{0,8,11,13,14\},                                   \tag{2.3}
\]

and for `8afb` take

\[
 C'=\{0,11,12,13,14\}.                                 \tag{2.4}
\]

The two instances below are identical, so write \(C\) for either set, use
\([17]=\{0,1,\ldots,16\}\), and put

\[
 Z=[17]\setminus(C\cup\{a,b,c,d\}).                    \tag{2.5}
\]

For concatenated subscripts, let \(Cac=C\cup\{a,c\}\),
and similarly for the other masks.  The four required lower rows are

\[
 Ca,\quad Cb,\quad Cc,\quad Cd.                         \tag{2.6}
\]

The eleven upper-capacity rows are

\[
 Cabc,\quad Cabd,\quad Cacd,\quad
 Cabz\ (z\in Z).                                       \tag{2.7}
\]

The two base-capacity rows are

\[
 Cbd,\quad Ccd,                                         \tag{2.8}
\]

and the nine unused-vertex rows are

\[
 X:=Cac,\quad Caz\ (z\in Z).                         \tag{2.9}
\]

The exact raw incidence menus have the following form.  Every one of the
six edges incident with \(Caz\) has upper colour \(Cabz\).  Upper capacity
one and the degree-zero-or-two row therefore force

\[
                       d_F(Caz)=0\qquad(z\in Z).         \tag{2.10}
\]

After (2.10), the four lower menus reduce to

\[
\begin{array}{c|c|c}
\text{lower}&\text{edge endpoints}&\text{upper}\\ \hline
Ca&(Cab,Cac)&Cabc\\
  &(Cab,Cad)&Cabd\\
  &(Cac,Cad)&Cacd\\ \hline
Cb&(Cab,Cbc)&Cabc\\
  &(Cab,Cbd)&Cabd\\
  &(Cbc,Cbd)&Cbcd\\ \hline
Cc&(Cac,Cbc)&Cabc\\
  &(Cac,Ccd)&Cacd\\
  &(Cbc,Ccd)&Cbcd\\ \hline
Cd&(Cad,Cbd)&Cabd\\
  &(Cad,Ccd)&Cacd.
\end{array}                                             \tag{2.11}
\]

The missing third edge in the last row would be the forbidden `BB` edge
\((Cbd,Ccd)\) of upper colour \(Cbcd\).  This is precisely where the
no-further-`BB` hypothesis enters.

Every raw edge incident with \(X=Cac\) has upper colour either \(Cabc\) or
\(Cacd\).  Now split on its allowed degree.

If \(d_F(X)=0\), row \(Ca\) is forced to use
\((Cab,Cad)\) of upper colour \(Cabd\).  Row \(Cc\) is forced to use
\((Cbc,Ccd)\), consuming base vertex \(Ccd\).  Row \(Cd\) then has no
choice: its first edge repeats \(Cabd\), while its second repeats base
vertex \(Ccd\).

If \(d_F(X)=2\), the two upper caps force one incident edge of colour
\(Cabc\) and one of colour \(Cacd\).  Row \(Cd\) is therefore forced to
use \((Cad,Cbd)\), consuming upper colour \(Cabd\) and base vertex
\(Cbd\).  Row \(Cb\) then has no choice: its first edge repeats \(Cabc\),
its second repeats \(Cabd\) and \(Cbd\), and its third repeats \(Cbd\).

Both allowed degrees of \(X\) are impossible, proving (2.1) infeasible.
\(\square\)

## 3. Literal masks and comparison of the two banks

The decimal core labels are:

| bank | lower q6 | base vertices |
|---|---|---|
| `7abc` | `26883,26885,26889,26897` | `26901,26905` |
| `8afb` | `30723,30725,30729,30737` | `30741,30745` |

For `7abc`, the eleven q8 labels are

```text
26895,26903,26907,26919,26951,27015,27399,27911,30983,59655,92423
```

and the nine U labels are

```text
26891,26915,26947,27011,27395,27907,30979,59651,92419.
```

For `8afb`, the eleven q8 labels are

```text
30735,30743,30747,30759,30791,30855,30983,31239,31751,63495,96263
```

and the nine U labels are

```text
30731,30755,30787,30851,30979,31235,31747,63491,96259.
```

The coordinate transposition \((8\ 12)\) maps every label of the `7abc`
core to the corresponding `8afb` label.  This proves an isomorphism of the
26-row cores only.  It does not assert that the two complete 572-ear banks
or their full conditioned catalogues are isomorphic.  In fact their enlarged
raw catalogues have different sizes:

\[
\begin{array}{c|ccc}
\text{bank}&\text{EU}&\text{UU}&\text{total}\\ \hline
7abc&131945&291177&423122\\
8afb&133411&291177&424588.
\end{array}                                             \tag{3.1}
\]

Thus the original full-turn artifact authenticates only `7abc`; the `8afb`
conclusion comes from its own independently replayed, isomorphic local core.

## 4. Consequences and exclusions

The strongest justified conclusion is:

> Neither explicit 572-direct bank can be completed by any residual EU/UU
> selection that covers every residual lower colour, is upper-rainbow, has
> residual-base degree at most one, and gives every unused vertex degree zero
> or two.

This conclusion is independent of:

* the `2637/430` length split and all aggregate counts derived from it;
* component sizes, cycles, connectivity, and the identity of final terminals;
* all boundary and central rank-nine constraints;
* the supported-provider relation.

It remains specific to the two fixed banks and the no-further-`BB`
architecture.  Rechoosing the 572 direct ears, allowing more direct `BB`
edges, changing the base seed, or changing the topology can evade the
certificate.  In particular this is not an `s=1` no-go.

## 5. Frozen replay

Dependency-free audit:

```text
scratch/audit_k17_gk_direct_bank_noh9_tetrahedral_core_20260731.py
SHA-256 88f33d73ebfd860416d78de76e05d2afc0e21f9c1b06c619ef387a0acebf7c7b
```

Frozen output:

```text
scratch/k17_gk_direct_bank_noh9_tetrahedral_core_20260731.audit.json
SHA-256 5f4cfbca522fd5fb5b62f7ea2de5107ee4c24432ea26e1720098ea65d0ab9b1a
canonical payload 53354643fdba00d531468b6811affd2346e338d0296aaeb105d053801ceccc7c
```

The replay reconstructs both 572-ear banks, enumerates the enlarged raw
catalogues with fixed-q9 filtering disabled, verifies every local menu and
resource status in (2.6)--(2.11), checks the two surviving finite palette
choices, and verifies the \((8\ 12)\) core isomorphism.

## 6. Provenance cautions for the older full-turn result

The older result remains useful as an independent solver observation, but it
is not itself the frozen small certificate above:

* it records residual-source SHA `355d877d...`, while the current local
  residual source has SHA `c5beed90...`;
* its embedded payload SHA `4b31c8af...` does not recompute from the current
  JSON by the master's canonical `payload_sha` rule (the recomputed value is
  `a9e48f5b...`);
* it does not record the master-script SHA or solver version.

The dependency-free 26-row replay removes these provenance and semantic
ambiguities for the theorem stated here.

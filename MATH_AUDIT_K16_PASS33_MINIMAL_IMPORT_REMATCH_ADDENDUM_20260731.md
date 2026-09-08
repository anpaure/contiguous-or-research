# K16 pass33 minimal-import rematch addendum

Date: 2026-07-31  
Status: **PASS; one rematch-aware local root.** This addendum does not modify
or invalidate the earlier paired-edge audit inside its stated stronger scope.

## Correction of the acceptance gate

The exact DM rematch-basis theorem proves that the old port mates

```text
ce40--J19536, ce30--J19538, 4a70--J31749
```

are noncore. They may disappear while a forced 26,309-edge matching survives.
The correct sufficient local gate is therefore:

1. exact middle replay;
2. the named `4e70` incidence at the selected port;
3. retained `8000--J31761`;
4. survival of the port's exact forced core, followed by a full forced
   rematch, or an equally explicit full forced rematch compensating any core
   loss.

The old mate itself is not required.

## Exact replay of the frozen minimal imports

The 17 individually exact A imports contain exactly one named-`4e70` root:

```text
source occurrence  4e72@280
destination        row6606
port               J19536=[6607,6609)
envelopes          4660,4e30
allowed/mandatory  4e70/4a50
```

It retains `8000--J31761` and every incidence in A's five-edge forced core:

```text
0a6e--J19546
866a--J19532
942b--J19528
b829--J19524
cc38--J19540
```

The complete candidate graph has 347,573 incidences and admits a forced
matching of size 26,309. Its basis SHA-256 is

```text
c401d053182d313cc20fee9f666dbc56b76b536b615d32d64a95a58960ea2012
```

The point import loses exactly five edges of the old frozen matching,

```text
8062--J19533, 8e20--J19537, c062--J19534,
c660--J19535, ce40--J19536,
```

all outside the forced core. This is the concrete reason the earlier paired-
mate rejection was too strong.

The point import is a local root, not yet an occurrence-integral or all-upper
word. It opens upper holes `{ce62,ce6a,ce6b}`. The direct two-cycle swapping
rows 280 and 6606 fails exactness at row280 by losing its `8000` carrier.
Under the same distance/protected-source rules there is also no exact
dependency-disjoint three-cycle with one intermediate source. Longer or
overlapping occurrence closure remains open.

For B, none of the 12 individually exact imports creates
`4e70--J19538`, even without requiring `ce30`.

For C, the earlier number 42 requires a terminology correction: it is the
number of safe ordered source pairs tested, not the number of locally exact
pairs. All 42 preserve the fixed flat pattern, but every pair fails middle
row12711 and loses that row's `0001` carrier. Hence

```text
C ordered pairs tested  42
C middle-exact pairs      0
C named-4e70 roots        0
```

## Corrected 19-template layer

The previously proposed 19 templates remain the complete one-local-
compensator layer:

\[
\begin{aligned}
K_A(t)&=\{6606,t\},&t&\in[6603,6610]\setminus\{6606\} &&(7),\\
K_B(t)&=\{6608,t\},&t&\in[6604,6611]\setminus\{6608\} &&(7),\\
K_C(t)&=\{12712,12713,t\},&t&\in[12710,12716]\setminus\{12712,12713\}
&&(5).
\end{aligned}
\]

Their acceptance predicate must not mention the old port mate. It is exact
middle replay, the named `4e70` incidence, retained `8000`, forced-core
survival or an explicit full forced rematch of at least 26,309, occurrence
closure, and literal upper replay.

This layer is no longer the absolute minimum A branch: the promoted
`4e72@280 -> 6606` singleton import should first be closed occurrence-
integrally. The seven A templates are its next interacting layer. B and C
still require compensation.

## Scope and authority

This is a pass33 finite addendum over exactly the frozen 17/12/42 catalogue.
It is not a complete occurrence-cycle search, does not decide the 19
templates, and makes no unrestricted Hall or K16 claim.

Inputs include the frozen paired audit
`b9fceeacd9fff8b36f837ddce4bf7cb3232b77836b28a820f82baa5d6c406ef0`
and the exact rematch-basis audit
`558b494a17f02682a5dc4cc131b880af437c5e680c8965235f00866bb42420c8`.

Reproducer:

```text
scratch/audit_k16_pass33_minimal_import_rematch_addendum_20260731.py
scratch/k16_pass33_minimal_import_rematch_addendum_20260731.audit.json
```

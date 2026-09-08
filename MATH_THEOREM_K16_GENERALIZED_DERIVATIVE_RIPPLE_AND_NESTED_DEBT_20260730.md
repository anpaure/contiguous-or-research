# K16 generalized derivative ripple and the exact nested-debt boundary

## 1. Construction

Let

\[
U=(U_0,\ldots,U_{N-1}),\qquad N=12874,
\]

be the authenticated universal word in
`answers/k16_upper12874.word`.  Its prefix is

\[
U_0=0x4879,quad U_1=0x2800,quad U_2=0x2069.
\]

Put

\[
A=0x4079,\qquad B=0x0800.
\]

The source satisfies the two exact split identities

\[
A\vee B=U_0,qquad B\vee U_2=U_1\vee U_2.
\tag{1.1}
\]

For integers \(2\le s\le t\le N-2\), define the length-\(N-1\)
word

\[
V^{s,t}=(A,B,U_2,\ldots,U_{s-1},
U_s\vee U_{s+1},\ldots,U_t\vee U_{t+1},
U_{t+2},\ldots,U_{N-1}).
\tag{1.2}
\]

Thus the original cell \(U_1\) is deleted, \(U_0\) is split, and an
adjacent-OR derivative compresses the segment \(U_s,\ldots,U_{t+1}\) by
one cell.

## 2. Exact interval map

Apart from the singleton intervals \([0,0]\) and \([1,1]\), every interval
of \(V^{s,t}\) has the OR of an interval of \(U\).  More precisely, for
indices at least two,

\[
\bigvee_{j=a}^{b}V^{s,t}_j=
\begin{cases}
\bigvee_{j=a}^{b}U_j,&b<s,\\
\bigvee_{j=a}^{b+1}U_j,&a\le t,\ b\ge s,\\
\bigvee_{j=a+1}^{b+1}U_j,&a\ge t+1.
\end{cases}
\tag{2.1}
\]

The same formulas extend to starts zero and one using (1.1), with the
special identities

\[
V_0\vee V_1=U_0,qquad
V_1\vee V_2\vee\cdots=U_1\vee U_2\vee\cdots.
\tag{2.2}
\]

Consequently the complete set of original intervals which have no image in
\(V^{s,t}\) is

\[
\mathcal D(s,t)=
\{[0,1],[1,1]\}
\cup\{[a,s]:0\le a\le s\}
\cup\{[j,j]:s<j<t+1\}
\cup\{[t+1,b]:t+1\le b<N\}.
\tag{2.3}
\]

This is an exact **nested-debt boundary**: two fixed prefix cells, one
horizontal endpoint row, an internal singleton diagonal, and one moving
vertical start column.

### Theorem 2.1 (nested-debt characterization)

Let \(\mathcal W_U(S)\) be the set of intervals of \(U\) whose OR is the
nonzero mask \(S\).  Then

\[
S\text{ is absent from }V^{s,t}
\quad\Longleftrightarrow\quad
S\notin\{A,B\}\ \text{ and }\
\mathcal W_U(S)\subseteq\mathcal D(s,t).
\tag{2.4}
\]

#### Proof

Equations (2.1)--(2.2) give an interval of \(V^{s,t}\) for every interval
of \(U\) outside (2.3).  Conversely, every interval of \(V^{s,t}\), except
the two split singletons \(A,B\), maps by those equations to an interval of
\(U\).  Therefore an old label disappears exactly when all of its old
witnesses lie on (2.3), unless one of the two new singletons reinstalls it.
\(\square\)

Advancing the endpoint from \(t\) to \(t+1\) converts the old right-column
cell into a derivative cell:

\[
V^{s,t}_{t+1}=U_{t+2}
\longmapsto
V^{s,t+1}_{t+1}=U_{t+1}\vee U_{t+2}.
\tag{2.5}
\]

Thus the old start column at \(t+1\) is released, its singleton remains on
the diagonal, and a new start column at \(t+2\) becomes debt.  This is the
literal carry law behind the ripple.

## 3. Exact census for starts through 64

The implementation

```
scratch/audit_k16_generalized_derivative_ripple_incremental_20260730.cpp
```

maintains exact interval-OR multiplicities.  For each fixed \(s\), advancing
\(t\) uses (2.5), so only intervals containing one position are updated from
grouped left-suffix and right-prefix OR banks.  The best word is independently
replayed from every start position.

The exhaustive range

\[
2\le s\le64,qquad s\le t\le12872
\]

contains **808,920** candidates.  It contains no universal word.  Its global
minimum is three holes, at \((s,t)=(2,2)\):

\[
\{0x146d,0x546d,0x6879\}.
\tag{3.1}
\]

Only starts \(s=2\) and \(s=3\) ever attain at most four holes.  The next
three-hole state is the fixed-start optimum \((s,t)=(3,5)\):

\[
\{0x1009,0x56a1,0x56b1\}.
\tag{3.2}
\]

Every start \(4\le s\le64\) has minimum at least five.  Hence this range
does not support broadening the same deterministic two-parameter family as a
likely finishing lane.

The witness fibres authenticate the geometry directly:

| state | hole | complete witness fibre in \(U\) | debt part |
|---|---:|---|---|
| \((2,2)\) | `0x146d` | `[3,5]` | right column |
| \((2,2)\) | `0x546d` | `[3,6]` | right column |
| \((2,2)\) | `0x6879` | `[0,1]`, `[0,2]` | fixed prefix + left row |
| \((3,5)\) | `0x1009` | `[5,5]` | internal diagonal |
| \((3,5)\) | `0x56a1` | `[6,8]` | right column |
| \((3,5)\) | `0x56b1` | `[6,9]` | right column |

## 4. Exact one-cell completion of the best basin

For the best state (3.1), a single replacement which creates all three
holes must be a nonzero submask of their intersection

\[
0x146d\wedge0x546d\wedge0x6879=0x0069.
\]

All 15 such values at all 12,873 positions were tested: **193,095 exact
assignments**.  None creates all three holes, even before collateral coverage
is considered.  Thus this basin has no one-cell installing assignment.

## 5. Authenticated artifacts

| artifact | SHA-256 |
|---|---|
| generalized source | `a741483cfe7abb07ec495416e6ae6c364935f97179b67a81cc39e8c5124f9ca6` |
| exact audit | `0ec9447a91a43b698dad1afed77de0aac1fcfd427f6c33530f8da52f6d192482` |
| best word | `7e850f8e7021983f9bdcc05bd3c5cc265d8e4600425871d96491c893bef2c275` |
| one-cell log | `18971b9b885bf35114a71098adb2e8dfcd3c372d718f320bdb903473ba2a61ec` |

The files are

```
scratch/k16_generalized_derivative_ripple_s2_64_20260730.audit.json
scratch/k16_generalized_derivative_ripple_s2_64_20260730.best.word
scratch/k16_generalized_derivative_ripple_s2_64_onecell_20260730.stderr
```

## 6. Smallest justified branch beyond deterministic ripple

The deterministic endpoint move (2.5) fixes how the released and newly
created columns exchange debt.  The smallest branch which can alter that
exchange without disturbing intervals spanning the frontier is a two-cell
OR-braid.  At a frontier pair \((x_0,y_0)\), replace it by nonzero \((x,y)\)
subject to

\[
x\vee y=x_0\vee y_0.
\tag{6.1}
\]

All intervals containing both cells retain their OR.  Only intervals ending
at the first cell or starting at the second can change.  Therefore (6.1)
provides exactly two exposed sides: one may serve the diagonal/left debt and
the other the moving right-column debt.  A braid is safe precisely when every
destroyed label not re-added across an exposed side has a witness outside the
two affected endpoint families.  This duplicate-reserve test is exact and is
the natural macro move for proof-aware annealing or an exhaustive frontier
census.

The exact frontier census was run on both three-hole minima:

| source | frontier | candidates | install every old hole | best residual |
|---|---:|---:|---:|---|
| \((s,t)=(2,2)\) | 2 | 432 | 36 | 2 holes, `0x146d,0x546d` |
| \((s,t)=(3,5)\) | 5 | 336 | 4 | 6 holes |

Neither frontier contains a universal braid.  The first line is especially
diagnostic: simultaneous installation of all three old holes is possible, but
every such split spends a last witness elsewhere.  The obstruction has moved
from service to duplicate reserve exactly as predicted by (6.1).

The source and audits are

```
scratch/search_k16_frontier_or_braid_completion_20260730.cpp
scratch/k16_generalized_derivative_frontier_s2t2_20260730.audit.json
scratch/k16_generalized_derivative_frontier_s3t5_20260730.audit.json
```

with SHA-256 values `3c97f7ec...`, `8b2bf2a8...`, and `79e0f308...`.

## 7. Cross-basin test on the annealed H background

The independently annealed length-12873 state

```
scratch/rex3_final_fwd_h11373.word
```

differs from the canonical basin in 1,620 cells.  It was tested with a
slightly different exact family: split its first cell into \((A,B)\), retain
all original cells, and pay for the insertion solely by derivative-compressing
the segment from \(s\) to \(t+1\).  This again has length 12873.

For

\[
1\le s\le64,qquad s\le t\le12871,
\]

the exact census contains **821,728** words.  It has no universal member.  Its
global optimum is again

\[
\{0x146d,0x546d,0x6879\},
\]

now at \((s,t)=(1,1)\); the second three-hole phase is again
\(\{0x1009,0x56a1,0x56b1\}\), now at \((2,4)\).  Starts at least three have
minimum at least five.

The best word again has no one-cell assignment which even installs all three
holes.  Its 432-candidate frontier-braid audit is byte-for-byte identical to
the canonical \((2,2)\) audit.  Hence the 1,620 remote annealing edits do not
change the duplicate reserve visible to this local ripple: this family depends
only on the same small prefix witness fibres.

Authenticated files:

```
scratch/audit_k16_split_only_derivative_ripple_incremental_20260730.cpp
scratch/k16_rex3_h11373_split_derivative_ripple_s1_64_20260730.audit.json
scratch/k16_rex3_h11373_split_derivative_ripple_s1_64_20260730.best.word
scratch/k16_rex3_h11373_split_derivative_frontier_s1t1_20260730.audit.json
```

Their SHA-256 values are respectively `e58b64d1...`, `ef87f122...`,
`9a2001a0...`, and `8b2bf2a8...`.

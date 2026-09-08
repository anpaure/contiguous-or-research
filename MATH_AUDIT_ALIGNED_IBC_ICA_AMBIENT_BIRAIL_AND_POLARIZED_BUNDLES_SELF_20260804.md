# Self-audit: aligned `Ibc/Ica` ambient birail and polarized bundles

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`  
**Status:** `PASS_SELF_AUDIT`, subject only to the explicit terminal-state,
background, global-host, and regeneration exclusions in the theorem.

## 1. Frozen inputs used

The audit uses the following exact files.

```text
7906b08d7d7953b2d8a22730fa6cd79f637f2f2e732890696155e3e1b0d3770e
  MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md
2d9fbf37ee6771013a28edd299b69ca5f4123c97d57f46339248e663fe6e2b83
  MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md
3035be5c0efee5fd9b72e7f201422bc182afc6c77c1c8fde4d1ae2543c6b89e0
  MATH_THEOREM_AD_COATOM_TRIANGLE_PHYSICAL_FLAG_CANCELLATION_20260801.md
c6ef1c254fffc65cb74d106a1f0beb5b7f2de6ea5cabcd3d772a4f970270ad83
  MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md
a6dba7ab6eab0e14e47552ab52ce00a2962969a6168f08972946720c6224fe53
  MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md
f2c3bb59ea841c16cf5ab9ad1b8f6d893e6126de3426ed059e573f3b0b22c6ae
  MATH_THEOREM_COATOM_FOUR_FAN_OCCURRENCE_SOCKET_REPLICATION_20260804.md
```

The superseded `Cd/Ic` draft is not used.

## 2. Correct physical pair and screen orientations

In the authenticated active words, positions `5,6` are

```text
P: Ibc, Ica,
Q: Ica, Ibc.
```

The screen before position `5` is lower, the screen between `5,6` is upper,
and the screen after position `6` is lower.  Their active parts are,
phasewise,

\[
 \{\infty,c\},\qquad \{\infty,a,b,c\},\qquad
 \{\infty,y_\epsilon\}.
\]

Therefore the first block has stable core

\[
 J=K\cup\{\infty,c\}
\]

and phase pivot `x_epsilon`, while the second has stable core
`K union {infinity,y_epsilon}` and pivot `c`.  The phase table

\[
 (x_0,y_0)=(b,a),\qquad (x_1,y_1)=(a,b)
\]

is exact.  This confirms that the theorem acts on the genuine aligned
birail pair, not on the old `Cd/Ic` surrogate.

## 3. Source convention and forced filler occurrences

For an owner trace equal to one on `[alpha,beta]`, a source occurrence at
`p` affects owners `[p-d,p]`.  Hence the legal source range is
`[alpha+d,beta]`.

For internal filler `f_i`, `1<=i<=d`, the unique zero owner `O_i` forbids

\[
                         [t+i,t+i+d].
\]

The immediately adjacent positive owner windows force the two occurrences

\[
                         t+i-1,\qquad t+i+d+1.
\]

This establishes Lemma 1.1 with the correct orientation.

The guard cases must be treated one-sidedly.

- First block (lower on the left, upper on the right): `f_0` has the bounded
  trace `1,0,1^(d+1),0`, hence unique block occurrence `s+d+1`;
  `f_(d+1)` has its forced terminal occurrence `s+d`, and its next run cannot
  contribute before `s+2d+3`.  A sparse completion of its preceding run can
  be kept before the used right-prefix range.  Thus neither guard occurs in
  `[s+d+2,s+2d]`.

- Second block (upper on the left, lower on the right): the upper screen and
  `O_0` are consecutive `f_0` zeros, so its first block-side occurrence is
  `s'+d+1`; the bounded `f_(d+1)` run `O_0,...,O_d` has unique occurrence
  `s'+d`.  Thus neither guard occurs in `[s'+1,s'+d-1]`.

These are exactly the ranges used by the first prefix rays and second suffix
rays.  No unused opposite-side assertion is needed.

## 4. Pin legality and a globally nonempty antecedent

For the first block, the stable pins `d-1,d,d+2` affect only its left lower
screen, its owners, and its right upper screen, all of which contain `J`.
The pivot pins `d,d+2` meet only owners containing `x_epsilon`.

For the second block, the stable pins `d-1,d,d+2` similarly meet only the
middle upper screen, block owners, and right lower screen, all containing
`K union {infinity,y_epsilon}`.  The pivot-`c` pins `d-1,d+1` are the two
endpoints of its permissible range: `c` is present from the middle upper
screen through the last block owner and absent at the right lower screen.

Across the middle screen, the last first-block stable pin and the first
second-block stable pin differ by exactly `d`.  The first-block post-zero
and second-block pre-zero occurrences of each internal filler differ by one.
Thus all prescribed occurrences respect the maximum source gap `d+1` and
extend independently to exact coordinate traces.

Because `K` is nonempty and lies in every owner and screen, putting all of
`K` in every source letter is legal and makes every source letter nonempty.
This removes the otherwise genuine global-empty-letter gap.

## 5. Literal ray identities

For

\[
 X_j=[s+d+2,s+d+j+1],\qquad
 Y_j=[s'+j,s'+d-1],\qquad 1\le j<d,
\]

the first-block forced post-zero occurrence of `f_i` belongs to `X_j`
exactly when `i<=j`; the second-block forced pre-zero occurrence belongs to
`Y_j` exactly when `i>j`.  The pin sets put the appropriate stable core and
pivot in every displayed interval, and Section 3 excludes guards and the
opposite active labels.  Therefore

\[
 \operatorname{OR}(X_j)=J\cup\{x_\epsilon\}\cup\{f_1,\ldots,f_j\},
\]

\[
 \operatorname{OR}(Y_j)=J\cup\{y_\epsilon\}\cup
                         \{f_{j+1},\ldots,f_d\}.
\]

Substituting the phase table gives precisely

\[
 (J+b+P_j,J+a+S_j)\longleftrightarrow
 (J+a+P_j,J+b+S_j).
\]

## 6. Native port intersections, including `d=2`

For port

\[
                         p_i=[t+i+1,t+i+d],
\]

the zero intervals of `f_i,f_(i+1)` cover the whole port.  If
`1<=h<=i-1`, the forced post-zero occurrence `t+h+d+1` lies in `p_i`; if
`i+2<=h<=d`, the forced pre-zero occurrence `t+h-1` lies in `p_i`.
The guard occurrences at relative `d,d+1` give the endpoint cases `i=0,d`.

Stable pins `d-1,d,d+2` meet every port: `d` handles `i<d`, and `d+2`
handles `i=d`.  The first pivot uses `d,d+2`.  The second pivot uses
`d-1,d+1`: `d-1` handles `i=0`, and `d+1` handles every `i>=1`.
Thus

\[
 \operatorname{OR}(p_i)=O_i\cap O_{i+1}
\]

for all `0<=i<=d`.

At the smallest case `d=2`, the only ray ticket is `j=1`:

\[
 X_1=[s+4,s+4],\qquad Y_1=[s'+1,s'+1].
\]

The first contains the stable/pivot pin at `4` and forced `f_1`; the second
contains the stable/`c` pin at `1` and forced `f_2`.  The three ports
`i=0,1,2` are met respectively by the stabilized active pins just listed,
so no endpoint exception is hidden at `d=2`.

## 7. Occurrence capacity and logical polarity

Across tickets, ray interval addresses are distinct.  Port, owner, and q1
addresses are separately injective in `j`; their lengths are respectively
`d,d+1,d+2`, while ray lengths are at most `d-1`.  Hence no two bundle
records use the same finite interval occurrence coordinate.  Overlap of
underlying source positions is irrelevant: capacity is charged to addressed
interval occurrences, not individual letters.

The prefix/suffix role is a genuine, phase-stable logical bit because the
literal ray occurrences and ticket label are retained.  It does not alter a
Boolean OR value and cannot force terminal acceptance.  Therefore the local
theorem correctly leaves all of the following as premises:

1. state-aware acceptance of the polarized owner--q1 code;
2. coexistence with the transported background matching;
3. whole-packet protected host planting and opening; and
4. regeneration after the same-parity lift.

No inference from logical role metadata to physical terminal type is used.

## 8. Verdict

The actual `Ibc/Ica` packet supplies, at zero added source positions,

- one exact nonempty antecedent in each phase;
- the full `d-1` aligned birail ray family;
- `d-1` pairwise occurrence-disjoint native owner--q1 socket records; and
- one pointwise common cap containing the two phase antecedents.

The proof does not close typed terminal acceptance or regeneration.  Within
that explicit scope, every address, endpoint, guard, and `d=2` boundary case
passes the audit.

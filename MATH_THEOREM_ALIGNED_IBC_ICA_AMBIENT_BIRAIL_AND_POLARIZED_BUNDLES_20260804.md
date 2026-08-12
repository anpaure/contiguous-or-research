# The aligned Ibc/Ica pair has an ambient birail antecedent and native sockets

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local-to-ambient theorem inside the complete
mixed-screen packet, for nonempty fixed core.  It materializes the exact
aligned birail rectangle in both phases, gives its canonical ray occurrences
and a capacity-disjoint native owner--q1 socket bank, and proves one common
source cap.  Terminal acceptance of the polarized code, transported
background coexistence, global host planting, and regeneration remain open.

## 0. The actual aligned birail pair

Let `d>=2`, put `n=d+2`, let the fixed packet core `K` be nonempty, and put

\[
                         F=\{f_0,\ldots,f_{d+1}\}.
\tag{0.1}
\]

Use the canonical active phases

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

The two blocks at zero-based positions `5,6` are `Ibc,Ica` in phase `P`
and `Ica,Ibc` in phase `Q`.  Let `s` be the owner start of position `5` and
put

\[
                         s'=s+d+3
\tag{0.2}
\]

for the start of position `6`.  Write

\[
 J=K\cup\{\infty,c\},
\qquad
 (x_0,y_0)=(b,a),
\qquad
 (x_1,y_1)=(a,b).
\tag{0.3}
\]

In phase `epsilon`, the first block has active set `J+{x_epsilon}`.  The
second has active set `J+{y_epsilon}`, viewed there as the stable core
`K+{infinity,y_epsilon}` plus pivot `c`.

The three surrounding screens have active parts

\[
 \{\infty,c\},
 \qquad \{\infty,a,b,c\},
 \qquad \{\infty,y_\epsilon\},
\tag{0.4}
\]

respectively.  The left and right screens are lower; the middle screen is
upper.  Every screen contains `K`.  Every internal filler `f_i`,
`1<=i<=d`, occurs in all screens, while an upper screen omits precisely the
guard fillers `f_0,f_(d+1)`.

For a block with active triple `V`, its owners are

\[
 O_i(V)=K\cup V\cup(F\setminus\{f_i\}),
                         \qquad0\le i\le d+1.
\tag{0.5}
\]

## 1. Coordinatewise source construction

For a binary owner trace with one finite positive run `[alpha,beta]` of
length at least `d+1`, the permissible source positions are

\[
                         [\alpha+d,\beta].
\tag{1.1}
\]

Any prescribed pins in (1.1) extend to an exact source trace: include the
two endpoints and insert further permissible positions until consecutive
gaps are at most `d+1`.  Apply this independently to every positive run of
every coordinate.

The following filler fact is forced, not chosen.

### Lemma 1.1 (coatom filler occurrences)

In a coatom block starting at `t`, for `1<=i<=d`, every exact antecedent
contains `f_i` at

\[
                         t+i-1,\qquad t+i+d+1,
\tag{1.2}
\]

and nowhere in `[t+i,t+i+d]`.

#### Proof

The owner `O_i` is the unique zero at the block and forbids the latter
source interval.  The preceding owner window has only `t+i-1` outside that
interval, and the following owner window has only `t+i+d+1`.  Both are
therefore forced.  \(\square\)

Choose sparse exact traces for the guards, but record only the sides used
below.  In the **first** block, whose left screen is lower and whose right
screen is upper, the block-side terminal occurrences are

\[
 f_{d+1}\in A_{s+d},\qquad f_0\in A_{s+d+1},
 \qquad
 f_0,f_{d+1}\notin A_p\quad(s+d+2\le p\le s+2d).
\tag{1.3a}
\]

In the **second** block, whose left screen is upper and whose right screen
is lower, the block-side initial occurrences are

\[
 f_{d+1}\in A_{s'+d},\qquad f_0\in A_{s'+d+1},
 \qquad
 f_0,f_{d+1}\notin A_p\quad(s'+1\le p\le s'+d-1).
\tag{1.3b}
\]

Indeed, at the first block the `f_0` owner trace is
`1,0,1^(d+1),0`, so its bounded positive run has the unique source
occurrence `s+d+1`.  The left positive run of `f_(d+1)` ends at owner
`s+d`, while the adjacent upper-screen zero postpones its next possible
source occurrence until `s+2d+3`; its earlier sparse completion can be
chosen before the displayed forbidden interval.  At the second block the
upper screen and `O_0` are consecutive zeros for `f_0`, so its next run
starts with source occurrence `s'+d+1`; the bounded `f_(d+1)` run through
`O_0,...,O_d` has the unique occurrence `s'+d`.  These are exactly the two
one-sided exclusions required by the ray intervals.

## 2. Simultaneous phase-specific pins

Fix a phase `epsilon`.

At the first block, pin every coordinate of `J` at relative source
positions

\[
                         d-1,\quad d,\quad d+2,
\tag{2.1}
\]

and pin its pivot `x_epsilon` at

\[
                         d,\quad d+2.
\tag{2.2}
\]

At the second block, pin every coordinate of

\[
                         K\cup\{\infty,y_\epsilon\}
\]

at relative positions

\[
                         d-1,\quad d,\quad d+2,
\tag{2.3}
\]

and pin its pivot `c` at

\[
                         d-1,\quad d+1.
\tag{2.4}
\]

### Lemma 2.1 (pin legality and simultaneous extension)

All pins (2.1)--(2.4) are permissible, and together with the filler traces
of Lemma 1.1 they extend to one exact nonempty depth-`d` antecedent
`A^epsilon` of the complete expanded packet chronology.

#### Proof

A source pin is permissible exactly when its entire affected owner window
contains the coordinate.  For (2.1), the three affected windows lie in,
respectively, left-screen plus first block, the first block, and first block
plus middle screen; all contain `J`.  The two windows in (2.2) lie in the
first block, with the latter also meeting the middle screen; both contain
`x_epsilon`.

The same argument on the second block proves (2.3).  Its pivot `c` is
present on the middle screen and throughout the second block but absent on
the right screen, so (2.4) is permissible and includes the forced final
source endpoint of that run.

Shared pins are compatible.  For `K union {infinity,c}`, consecutive
prescribed positions across the middle screen have gaps at most `d`.
For every internal filler, the right occurrence forced by its zero in the
first block and the left occurrence forced by its zero in the second block
are consecutive:

\[
 s+i+d+1,\qquad s'+i-1=s+i+d+2.
\]

The labels `x_epsilon,y_epsilon` are absent from the opposite block, so no
pin crosses a forbidden source interval.  The run-extension lemma completes
all affected coordinate traces; retain any exact endpoint/gap completion on
all other runs.

Finally put every coordinate of the nonempty fixed core `K` in every source
letter.  This is legal because every block and screen owner contains `K`,
and it makes the complete source word nonempty at every address.  Binary
dilation is coordinatewise, so the resulting word is one exact nonempty
antecedent of the full chronology.  \(\square\)

Applying the construction separately to `epsilon=0,1` and taking the
pointwise union

\[
                         \widehat A_p=A_p^0\cup A_p^1
\tag{2.5}
\]

gives one phase-common source cap containing both exact antecedents.  This
is a literal cap-containment statement; no terminal-type or transported-
background acceptance is inferred.

## 3. Exact aligned birail rays

For `1<=j<d`, put

\[
 P_j=\{f_1,\ldots,f_j\},
 \qquad
 S_j=\{f_{j+1},\ldots,f_d\}.
\tag{3.1}
\]

Use the physical intervals

\[
 X_j^\epsilon=[s+d+2,s+d+j+1],
 \qquad
 Y_j^\epsilon=[s'+j,s'+d-1].
\tag{3.2}
\]

Their addresses do not depend on `epsilon`; the superscript records the
phase word used to evaluate them.

### Theorem 3.1 (literal aligned rectangle)

For every `1<=j<d`,

\[
 \operatorname{OR}_{A^\epsilon}(X_j^\epsilon)
                         =J\cup\{x_\epsilon\}\cup P_j,
\tag{3.3}
\]

\[
 \operatorname{OR}_{A^\epsilon}(Y_j^\epsilon)
                         =J\cup\{y_\epsilon\}\cup S_j.
\tag{3.4}
\]

Consequently the two phase rows are exactly

\[
\begin{array}{c|cc}
 &\text{prefix}&\text{suffix}\\ \hline
 P&J\cup\{b\}\cup P_j&J\cup\{a\}\cup S_j\\
 Q&J\cup\{a\}\cup P_j&J\cup\{b\}\cup S_j.
\end{array}
\tag{3.5}
\]

This is the actual aligned birail action

\[
 (A\cup P_j,B\cup S_j)
 \longleftrightarrow
 (B\cup P_j,A\cup S_j),
 \qquad A=J\cup\{b\},\quad B=J\cup\{a\}.
\tag{3.6}
\]

#### Proof

The pin at first-block position `d+2` puts `J` and `x_epsilon` in every
prefix interval.  The pins at second-block position `d-1` put
`K union {infinity,y_epsilon,c}=J union {y_epsilon}` in every suffix
interval.

By Lemma 1.1, first-block right occurrence `s+i+d+1` lies in `X_j` exactly
when `i<=j`, while second-block left occurrence `s'+i-1` lies in `Y_j`
exactly when `i>j`.  If `i>j`, the first permissible post-zero occurrence
lies strictly to the right of `X_j`; if `i<=j`, the last permissible
pre-zero occurrence lies strictly to the left of `Y_j`.  Thus no optional
completion occurrence changes these membership tests.  The one-sided guard
exclusions (1.3a)--(1.3b) put both guards outside the ray family actually
used in each block.

Any active coordinate absent from the relevant block is absent throughout
the union of that block's owner windows, which contains its displayed ray
interval.  Therefore no opposite pivot or other active label enters.
Equations (3.3)--(3.4), and then (3.5)--(3.6), follow.  \(\square\)

The `2(d-1)` ray addresses in either phase are pairwise distinct: all
prefixes lie in the first block's right source range, all suffixes in the
second block's left source range, and each family has a different endpoint.

## 4. Native port and q1 occurrences

For either block start `t in {s,s'}` and `0<=i<=d`, define

\[
\begin{aligned}
 p_i(t)&=[t+i+1,t+i+d],&
 o_i(t)&=[t+i,t+i+d],\\
 o_{i+1}(t)&=[t+i+1,t+i+d+1],&
 q_i(t)&=[t+i,t+i+d+1].
\end{aligned}
\tag{4.1}
\]

### Theorem 4.1 (exact native diamonds)

In either phase and either block,

\[
 \operatorname{OR}(o_i)=O_i(V),
 \qquad
 \operatorname{OR}(o_{i+1})=O_{i+1}(V),
\tag{4.2}
\]

\[
 \operatorname{OR}(p_i)=O_i(V)\cap O_{i+1}(V),
 \qquad
 \operatorname{OR}(q_i)=O_i(V)\cup O_{i+1}(V).
\tag{4.3}
\]

#### Proof

Equation (4.2) is the defining exact dilation.  The q1 interval is the union
of the two owner intervals, proving its equality in (4.3).

For the port, Lemma 1.1 puts every internal filler except
`f_i,f_(i+1)` in `p_i` and excludes those two.  The block-side guard
occurrences in (1.3a)--(1.3b), at relative positions `d` and `d+1`, give
the same conclusion at `i=0,d`; the adjacent upper-screen zeros forbid any
contrary occurrence in those endpoint ports.  Every active block coordinate
occurs in `p_i`:
the stable-core pins at relative `d` meet `p_i` for `i<d`, and the pin at
`d+2` meets `p_d`; the first pivot has the same pair `d,d+2`, while the
second pivot's pair `d-1,d+1` meets every port.  Coordinates outside the
block are forbidden throughout these source intervals.  This proves the
intersection equality.  \(\square\)

## 5. Complete polarized bundle bank

For ticket `j`, `1<=j<d`, take the exact two ray occurrences in (3.2) and
the all-left native route in the first block at `i=j-1`:

\[
 \mathcal B_j^\epsilon=
 (X_j^\epsilon,Y_j^\epsilon;
  p_{j-1}(s),o_{j-1}(s),q_{j-1}(s)).
\tag{5.1}
\]

### Theorem 5.1 (ambient capacity-disjoint bundles)

For either phase, the `d-1` records (5.1) are pairwise disjoint **among
themselves** in every finite occurrence coordinate.  Their upstream values are the actual
aligned birail row (3.5), and each contains a literal native nested pair

\[
 O_{j-1}(V_L^\epsilon)
 \subset
 O_{j-1}(V_L^\epsilon)\cup O_j(V_L^\epsilon),
\tag{5.2}
\]

where `V_L^epsilon={infinity,c,x_epsilon}` is the first active triple.

Thus, in any fixed cap/phase/guard state which accepts the polarized native
code **and** admits these complete records alongside its transported
background, all `d-1` aligned birail tickets are simultaneously linked with
no additional source position.

#### Proof

The ray addresses are pairwise distinct and have lengths at most `d-1`.
The selected ports, owners, and q1 addresses are separately injective in
`j` and have lengths `d,d+1,d+2`.  Hence no two records share a finite
occurrence coordinate.  Theorem 3.1 gives the upstream identities and
Theorem 4.1 gives the native nested route.  Apply the deterministic
polarized-socket theorem under its explicit state-acceptance premise.
\(\square\)

The address templates are the same in `P,Q`, while `a,b` swap exactly as in
(3.5).  Hence (2.5) is one pointwise common **source-letter containment
cap** for the two phase-specific ray witnesses.  It is generally not itself
an exact antecedent for either phase and does not establish a common
terminal cap state.  The phase-specific matchings need not be the same edge
set.

## 6. Pivot-side polarity: exact scope

The packet geometry canonically distinguishes the prefix-pivot side from
the suffix-pivot side.  Retaining the ticket label `j`, phase, block side,
and ordered ray role therefore supplies an unambiguous binary logical field:

\[
                         1=\text{prefix-pivot role},
 \qquad 0=\text{suffix-pivot role}.
\tag{6.1}
\]

This field is stable under the phase swap: the physical roles and addresses
stay fixed while `a,b` exchange.  Because the exact upstream occurrences in
(3.5) remain in the complete record, adding (6.1) loses no literal target
identity and consumes no new physical cell.  It is therefore a legitimate
logical state augmentation and realizes the minimal polarity bookkeeping of
the polarized-chain coding theorem.

It is **not** by itself a physical terminal-type theorem.  A role bit cannot
change the OR value of `o_i` or `q_i`, cannot make an unavailable occurrence
active, and cannot force the transported common cap to accept the pair.
The statement

\[
 (\operatorname{val}(o_i),1),
 \quad(\operatorname{val}(q_i),0)
 \quad\text{is an accepted terminal code}
\tag{6.2}
\]

remains an explicit state-aware cap premise.  Treating (6.1) as metadata is
sound; treating it as proof of (6.2) would be an unauthorized identification
of different physical terminal types.

## 7. Exact remaining rows

The construction closes, on the actual aligned birail pair:

1. simultaneous ambient antecedent and nonempty source word;
2. exact prefix/suffix ray values in both phases;
3. exact port intersections and q1 unions, including `d=2`;
4. occurrence-disjoint native socket multiplicity; and
5. one pointwise common source cap for the two phase antecedents.

It does not prove:

1. state-aware terminal acceptance (6.2);
2. coexistence with one transported background compiler matching;
3. protected embedding of the whole packet in the global decorated carrier;
4. safe opening/global topology; or
5. regeneration of a fresh whole-packet atlas after the same-parity lift.

## 8. Dependencies

- `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`
- `MATH_THEOREM_AD_COATOM_TRIANGLE_PHYSICAL_FLAG_CANCELLATION_20260801.md`
- `MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
- `MATH_THEOREM_COATOM_FOUR_FAN_OCCURRENCE_SOCKET_REPLICATION_20260804.md`

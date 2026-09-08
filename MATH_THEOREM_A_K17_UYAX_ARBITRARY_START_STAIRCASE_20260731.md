# The K17 UYAX arbitrary-start staircase and a contiguous-U obstruction

Date: 2026-07-31  
Status: exact schedule theorem and independently audited scoped obstruction  
Scope: monotone depth-three P/Q schedules on a labelled linearization of the
four-sector skeleton; this is not a K17 construction

## 0. Verdict

For K17 the arbitrary-start staircase collapses to an exact six-integer
optimization.  Put

\[
 W={17\choose9}=24310,
 \qquad L=W+3=24313,
 \qquad \Delta_{17}=3W+{4\choose2}-65535=7401.
\]

If the omitted-start thresholds are written

\[
 \alpha_j=W-\delta_j,
 \qquad W\ge\delta_1\ge\delta_2\ge\delta_3\ge0,
\]

then every scalar-viable schedule automatically has all deadline thresholds
strictly before all start thresholds.  Consequently legality, chain
alignment, and the start/deadline cross term disappear.  The exact
row-replay and scalar criterion is

\[
 \boxed{
 \min_{\substack{W\ge\delta_1\ge\delta_2\ge\delta_3\ge0\\
                  \delta_1,\delta_2,\delta_3\in\mathbb Z}}
 \left(
  \delta_1+\delta_2+\delta_3+
  \rho_1^\delta+\rho_2^\delta+\rho_3^\delta
 \right)\le7401 .}
 \tag{0.1}
\]

The adjusted frontiers \(\rho_j^\delta\) are defined exactly in Section 3.
A passing vector gives the schedule explicitly; there is no residual
search over \(q_i,s_i\).

The unlabelled four-sector arithmetic itself is schedule-compatible.  One
can use 715 blocks of type

\[
 (|U_i|,|Y_i|,|A_i|,|X_i|)=(4,4,5,4)
\]

and 715 of type

\[
 (3,5,4,5).
\]

Every macroblock then has length 17, all sector totals are exact, and every
new-\(x\) and new-\(y\) run has length 9.  Thus only the old-coordinate run
geometry enters (0.1).

There are two rigorous outcomes.

1.  If every interior old-coordinate run has length at least four and every
    four consecutive carrier rows have nonempty intersection, then
    \(\alpha=(W,W,W)\), \(\tau=(0,0,0)\) is an explicit zero-loss physical
    schedule.
2.  The current 5005-row run-order artifact
    `scratch/k17_pbbs_u_remote_best_20260731/pbbs_u_best.word` cannot occur as
    one untouched non-wrapping contiguous \(U\)-block in any viable K17
    schedule, in either orientation or at any position.  Its four persistent
    singleton runs force loss at least \(10086>7401\).

The second conclusion is a sharp obstruction to contiguous placement, not
to a split, cyclically cut, interleaved, or rethreaded \(U\)-shore.  No
frozen labelled UYAX Hamilton chronology presently exists, so no K17 word is
claimed.

## 1. Exact four-sector arithmetic

For the semilength raise from K15 to K17, the old parameter is \(r=8\),

\[
 W_0={15\choose8}=6435,
 \qquad b=C_8=1430.
\]

The unlabelled sector skeleton is

\[
 U_1Y_1A_1X_1\ U_2Y_2A_2X_2\cdots
 U_bY_bA_bX_b.                                      \tag{1.1}
\]

Its required totals are

\[
 |U|=W_0-b=5005,
 \qquad |Y|=|A|=|X|=W_0=6435.                       \tag{1.2}
\]

Choose 715 indices with \(|A_i|=5\) and 715 with \(|A_i|=4\), and put

\[
 |X_i|=|Y_i|=9-|A_i|.
\]

Pair the former indices with \(|U_i|=4\) and the latter with
\(|U_i|=3\).  Then every macroblock has length 17 and

\[
 715(4+3)=5005,
 \qquad 715(5+4)=6435
\]

in the appropriate sector sums.  Moreover \(A_iX_i\) is an \(x\)-run and
\(Y_iA_i\) is a \(y\)-run, each of length exactly 9.

This is only a cardinality and run-length statement.  It does not label the
positions by rank-nine sets, make the seams Johnson, cover upper shadows, or
solve the lower compiler.

Fix from now on a labelled linearization

\[
 T=(T_0,T_1,\ldots,T_{W-1})                         \tag{1.3}
\]

of a proposed skeleton.  Runs touching row 0 or row \(W-1\) are boundary
runs; all other coordinate runs are interior.

## 2. Arbitrary starts and deadlines

Let the following be integer vectors:

\[
 0\le\alpha_1\le\alpha_2\le\alpha_3\le W,
 \qquad
 0\le\tau_1\le\tau_2\le\tau_3\le W.               \tag{2.1}
\]

The three omitted physical starts and deadlines are

\[
 x_j=\alpha_j+j-1,
 \qquad y_j=\tau_j+j-1.                             \tag{2.2}
\]

Define

\[
 g_i=\#\{j:\alpha_j\le i\},
 \qquad h_i=\#\{j:\tau_j\le i\}.                  \tag{2.3}
\]

The selected start and deadline of carrier row \(i\) are exactly

\[
 s_i=i+g_i,
 \qquad q_i=i+h_i.                                  \tag{2.4}
\]

Row intervals are nonempty exactly when

\[
 \tau_j\le\alpha_j\qquad(j=1,2,3),                 \tag{2.5}
\]

and the consecutive-row upper-transfer alignment is exactly

\[
 s_{i+1}\le q_i+1
 \quad\Longleftrightarrow\quad
 g_{i+1}\le h_i.                                    \tag{2.6}
\]

For an interior coordinate run \([a,b]\), of length
\(\ell=b-a+1\), the two adjacent absent rows leave the safe corridor

\[
 [q_{a-1}+1,s_{b+1}-1].
\]

Thus the run is recovered in every owner row if and only if

\[
 q_{a-1}+1<s_{b+1}
 \quad\Longleftrightarrow\quad
 h_{a-1}<\ell+g_{b+1}.                              \tag{2.7}
\]

Boundary runs are automatic because they have only one adjacent absent row.

The exact loss from the maximum depth-three catalogue is

\[
 \begin{aligned}
 \operatorname{Loss}(\alpha,\tau)
 &=\sum_{j=1}^3\tau_j+
   \sum_{\alpha_j<W}(L-q_{\alpha_j})\\
 &=\sum_j\tau_j+\sum_j(W-\alpha_j)
   +\#\{(j,t):\alpha_j<\tau_t\}.                   \tag{2.8}
 \end{aligned}
\]

Indeed, when \(\alpha_j<W\),

\[
 L-q_{\alpha_j}
 =W-\alpha_j+\#\{t:\alpha_j<\tau_t\};
\]

the same expression is zero when \(\alpha_j=W\).  Hence

\[
 |\mathcal C_{\rm full}|=3W+6-\operatorname{Loss},  \tag{2.9}
\]

and scalar feasibility is exactly

\[
 \operatorname{Loss}\le\Delta_{17}=7401.           \tag{2.10}
\]

## 3. The K17 two-ended collapse

Write

\[
 \alpha_j=W-\delta_j,
 \qquad W\ge\delta_1\ge\delta_2\ge\delta_3\ge0.  \tag{3.1}
\]

### Lemma 3.1 (forced separation)

Every schedule satisfying (2.10) obeys

\[
 \tau_3\le7401,
 \qquad
 \alpha_1\ge16909,
 \quad\alpha_2\ge20610,
 \quad\alpha_3\ge21843.                             \tag{3.2}
\]

In particular every deadline threshold is strictly earlier than every
start threshold.  The cross term in (2.8) is zero, (2.5) holds, (2.6) holds,
and

\[
 \operatorname{Loss}=\sum_j\delta_j+\sum_j\tau_j.  \tag{3.3}
\]

#### Proof

All terms in (2.8) are nonnegative, so

\[
 \sum_j\tau_j\le7401,
 \qquad \sum_j\delta_j\le7401.
\]

The first inequality gives \(\tau_3\le7401\).  Since the \(\delta_j\) are
nonincreasing,

\[
 \delta_1\le7401,
 \qquad 2\delta_2\le7401,
 \qquad 3\delta_3\le7401,
\]

which is (3.2).  Therefore \(\alpha_j>\tau_t\) for every \(j,t\), proving
(3.3) and legality.

For chain alignment, if \(i+1<\alpha_1\), then \(g_{i+1}=0\).  If
\(i+1\ge\alpha_1\), then \(i\ge16908>\tau_3\), so \(h_i=3\ge g_{i+1}\).
This proves (2.6). \(\square\)

For an interior run \([a,b]\), put

\[
 m_\delta(b)=g_{b+1}
 =\#\{j:\delta_j\ge W-b-1\}.                       \tag{3.4}
\]

If \(\ell+m_\delta(b)\ge4\), (2.7) is automatic.  If
\(\ell+m_\delta(b)=j\le3\), it is equivalent to

\[
 a\le\tau_j.                                        \tag{3.5}
\]

Define

\[
 \rho_j^\delta=
 \max\!\left(
 \{a:\ [a,b]\text{ is an interior coordinate run and }
       (b-a+1)+m_\delta(b)\le j\}\cup\{0\}
 \right)                                             \tag{3.6}
\]

for \(j=1,2,3\).  The vector \(\rho^\delta\) is nondecreasing.

### Theorem 3.2 (exact K17 arbitrary-start criterion)

For the fixed labelled linearization \(T\), there exists a monotone
depth-three schedule that is row-OR exact and has enough scalar lower cells
if and only if (0.1) holds.

For every passing \(\delta\), an explicit schedule is

\[
 \tau_j=\rho_j^\delta,
 \qquad
 x_j=W-\delta_j+j-1,
 \qquad
 y_j=\rho_j^\delta+j-1,                              \tag{3.7}
\]

with

\[
 s_i=i+\#\{j:\delta_j\ge W-i\},
 \qquad
 q_i=i+\#\{j:\rho_j^\delta\le i\}.                \tag{3.8}
\]

Its scalar surplus is

\[
 7401-\sum_j\delta_j-\sum_j\rho_j^\delta.          \tag{3.9}
\]

#### Proof

For fixed \(\delta\), (3.5) for all interior runs is equivalent to
\(\tau_j\ge\rho_j^\delta\) for all \(j\).  Lemma 3.1 shows that every
viable schedule has loss \(\sum\delta+\sum\tau\), so necessity of (0.1)
follows.

Conversely, suppose the objective in (0.1) is at most 7401 and put
\(\tau=\rho^\delta\).  Directly from the two nonnegative subsums,
\(\alpha_1\ge16909\) and \(\tau_3=\rho_3^\delta\le7401\).  Hence every
deadline precedes every start, the cross term vanishes, and the same
two-case proof as in Lemma 3.1 gives legality and chain alignment.
Equations (3.5)--(3.6) give exact coordinatewise row replay, while (2.8)
identifies the loss with the objective in (0.1). \(\square\)

For reference, every viable threshold vector also satisfies

\[
 \tau_1\le2467,
 \qquad
 \tau_2\le\left\lfloor{7401-\tau_1\over2}\right\rfloor,
 \qquad
 \tau_3\le7401-\tau_1-\tau_2.                      \tag{3.10}
\]

Theorem 3.2 is exact only for row-OR replay plus scalar capacity.  Physical
envelope nonemptiness, upper-shadow completeness, pins, lower Hall, and a
common-Q realization remain separate.

## 4. A sharp one-run obstruction

### Lemma 4.1

An interior run \([a,b]\) of length \(\ell\le3\) forces

\[
 \boxed{
 \operatorname{Loss}\ge
 (4-\ell)\min\{a,W-b-1\}.}                           \tag{4.1}
\]

The bound is sharp for the isolated run constraint.

#### Proof

Let \(r=g_{b+1}\).  The \(r\) start thresholds activated by \(b+1\) each
contribute at least \(W-b-1\) to \(\sum\delta_j\).  If
\(\ell+r\le3\), (2.7) forces at least \(4-\ell-r\) deadline thresholds to
be at least \(a\); if \(\ell+r\ge4\), no deadline cost is forced.  Ignoring
the nonnegative cross term gives

\[
 \operatorname{Loss}\ge
 r(W-b-1)+(4-\ell-r)_+a.
\]

Minimizing over integer \(0\le r\le3\) gives (4.1).  Equality in the
isolated constraint is attained either by putting the required
\(4-\ell\) deadlines at \(a\), or by activating \(4-\ell\) starts at
\(b+1\). \(\square\)

Consequently every viable K17 carrier must obey

\[
\begin{array}{c|c|c}
\ell&\text{necessary endpoint alternative}
    &\text{forbidden exact start band}\\ \hline
1&a\le2467\text{ or }b\ge21842 &[2468,21841]\\
2&a\le3700\text{ or }b\ge20609 &[3701,20607]\\
3&a\le7401\text{ or }b\ge16908 &[7402,16905].
\end{array}                                           \tag{4.2}
\]

Here the last column uses \(b=a+\ell-1\).  Any single violating run rejects
the chronology before upper replay or lower compilation.

## 5. Two explicit schedules

### 5.1 Zero-loss four-local schedule

Assume every interior old-coordinate run has length at least four.  The
new-coordinate runs of (1.1) already have length nine.  Take

\[
 \alpha=(W,W,W),
 \qquad \tau=(0,0,0).                                \tag{5.1}
\]

Then

\[
 X=\{24310,24311,24312\},
 \qquad Y=\{0,1,2\},
\]

and

\[
 s_i=i,
 \qquad q_i=i+3.                                    \tag{5.2}
\]

Every interior run is recovered, loss is zero, and the lower catalogue has

\[
 3W+6=72936=65535+7401                              \tag{5.3}
\]

cells.  If the local intersection condition of Section 6 also holds, this
is a literal nonempty schedule.

### 5.2 A schedule aligned with a 5005-row U prefix

For a linear architecture consisting of a 5005-row \(U\) prefix followed by
the YAX material, take

\[
 \alpha=(W,W,W),
 \qquad \tau=(0,0,5005).                             \tag{5.4}
\]

Then

\[
 X=\{24310,24311,24312\},
 \qquad Y=\{0,1,5007\},                             \tag{5.5}
\]

and

\[
 s_i=i,
 \qquad
 q_i=
 \begin{cases}
 i+2,&0\le i<5005,\\
 i+3,&5005\le i<W.
 \end{cases}                                         \tag{5.6}
\]

Its loss is 5005, so it retains scalar surplus

\[
 |\mathcal C_{\rm full}|=67931=65535+2396,
 \qquad 7401-5005=2396.                              \tag{5.7}
\]

The exact run condition for (5.4) is:

* there is no interior run of length one or two;
* every interior run of length three starts at or before row 5005.

Thus all short runs inside a run-safe U prefix can be discharged before the
YAX suffix.  Every interior run starting after row 5005 must have length at
least four; a length-three run starting exactly at row 5005 is still allowed.
Short-run verification at a seam uses the last four and first four rows: a
length-three run touching a seam also depends on its two bounding zero rows.

Section 7 shows that the current U artifact does not satisfy this condition
and, more strongly, cannot be repaired by translating or reversing it as one
contiguous block.

For this particular schedule the exact envelope test is also local.  Apart
from the truncated endpoint blocks, the active blocks through physical
position 5007 are consecutive triples, and those from position 5008 onward
are consecutive quadruples.  Equivalently, it is enough and necessary to
check

\[
 T_i\cap T_{i+1}\cap T_{i+2}\ne\varnothing
 \quad(0\le i\le5004)                               \tag{5.8}
\]

and

\[
 T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}
 \ne\varnothing
 \quad(5005\le i\le W-4).                           \tag{5.9}
\]

Condition (6.2) below is a simpler schedule-independent sufficient test.

## 6. Nonempty envelopes are a separate four-local gate

At physical position \(p\), let

\[
 E_p=\bigcap_{i:s_i\le p\le q_i}T_i.                \tag{6.1}
\]

Row replay is physically realizable only if \(E_p\ne\varnothing\) at every
used position.  Since \(s_i\ge i\) and \(q_i\le i+3\), the active rows form
a consecutive block of at most four rows.  Therefore the schedule-independent
condition

\[
 \boxed{
 T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}\ne\varnothing
 \quad(0\le i\le W-4)}                               \tag{6.2}
\]

is sufficient for every depth-three schedule.  Indeed, assign the physical
letter

\[
 Z_p:=E_p.
\]

Then \(Z_p\ne\varnothing\), every active owner contains \(Z_p\), and the
safe-corridor theorem gives

\[
 \bigcup_{p=s_i}^{q_i}Z_p=T_i
\]

for every row \(i\).  Thus the physical word literally replays the carrier.
In run language, (6.2) says
exactly that every four-row interval is contained in some coordinate
positive run.  This is not implied by the scalar short-run inequalities.

For rank-nine rows, put

\[
 d_i=|T_i\setminus T_{i+1}|.
\]

Then

\[
 |T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}|
 \ge9-d_i-d_{i+1}-d_{i+2}.                          \tag{6.3}
\]

Hence \(d_i+d_{i+1}+d_{i+2}\le8\) is a checkable sufficient condition.
In particular a rank-nine Johnson path has \(d_i=1\) and every fourfold
intersection has size at least six.

For the balanced blocks in Section 1, every sector block has length at least
three, so a four-row interval crosses at most one sector seam.  The YA
collars satisfy (6.2) automatically through coordinate \(y\), and AX collars
through coordinate \(x\).  It remains only to check:

1. four-row intervals internal to a U block;
2. the last-three/first-three row collars at each UY seam; and
3. the last-three/first-three row collars at each XU seam.

A sufficient stronger implementation is to make every U block internally
Johnson and to make the six-row collar around every UY and XU seam a
Johnson path.

There is also a schedule-independent central obstruction stronger than a
generic sufficiency test.

### Lemma 6.1 (forced four-row plateau)

In every K17 schedule of loss at most 7401, for

\[
 7401\le i\le16905,
 \qquad p=i+3,
\]

the active rows at \(p\) are exactly

\[
 T_i,T_{i+1},T_{i+2},T_{i+3}.                       \tag{6.4}
\]

Consequently an empty fourfold intersection anywhere in this index band is
an obstruction to every arbitrary-start schedule.

#### Proof

Lemma 3.1 gives \(\tau_3\le7401\) and \(\alpha_1\ge16909\).  Thus
\(h_j=3\) for every \(j\ge i\), while no start shift has activated by
\(p\le16908\).  Hence row \(i\) ends at \(p\), rows \(i+1,i+2,i+3\) start
by \(p\), every earlier row ends before \(p\), and every later row starts
after \(p\). \(\square\)

## 7. The current contiguous-U order is impossible

Consider

```text
scratch/k17_pbbs_u_remote_best_20260731/pbbs_u_best.word
SHA-256 085a6876191df16cdd8fc0ed09237f023aa5a4a570ea59463301d24339293915
```

It has 5005 distinct rank-nine rows.  A lightweight independent run replay
finds exactly four persistent interior singleton runs:

\[
 (\text{offset},\text{coordinate})
 =(1642,14),(2177,3),(4988,8),(5001,9).              \tag{7.1}
\]

There are no interior length-two runs; there are 916 interior length-three
runs, the last beginning at offset 4994.  Only the singleton data are needed
below.

Place the whole order, without wrapping or splitting it, at offset
\(0\le t\le W-5005=19305\).  Lemma 4.1 assigns a singleton at full row
\(p\) the lower bound

\[
 3\min\{p,W-p-1\}.                                  \tag{7.2}
\]

For the forward orientation the singleton offsets have minimum 1642,
maximum 5001, and span 3359.  Suppose all four endpoint distances were at
most 3361.  Then all singleton rows would lie in

\[
 [0,3361]\cup[20948,24309].                         \tag{7.3}
\]

Their span is too short to meet both intervals.  They cannot all lie in the
left interval because \(t+5001>3361\), and they cannot all lie in the right
interval because that would require
\(t+1642\ge20948\), hence \(t\ge19306\).  Therefore some singleton has
endpoint distance at least 3362.

This is attained at \(t=19305\), where the singleton rows are

\[
 20947,21482,24293,24306
\]

with maximum endpoint distance 3362.  Reversal changes the offsets to

\[
 3,16,2827,3362,
\]

again with span 3359.  If their endpoint distances were all at most 3361,
they could not meet both intervals in (7.3).  They cannot all lie in the
left interval because \(t+3362>3361\), and they cannot all lie in the right
interval because that would require \(t+3\ge20948\), hence
\(t\ge20945>19305\).  The lower bound 3362 therefore also holds after
reversal, and is attained at \(t=0\).  Thus, if \(S(t,o)\) denotes the four
translated singleton rows, then over every translation \(t\) and both
orientations \(o\),

\[
 \min_{t,o}\max_{p\in S(t,o)}3\min\{p,W-p-1\}
 =3\cdot3362=10086>7401.                             \tag{7.4}
\]

### Theorem 7.1 (contiguous-U no-go)

No monotone arbitrary-start/deadline depth-three K17 schedule can contain
this fixed U order as one untouched non-wrapping contiguous block, in either
orientation, regardless of the exterior YAX labels.

The obstruction precedes Johnson legality, envelope nonemptiness, upper
shadows, Hall, and common-Q.  It does not exclude cutting through U at the
global boundary, splitting U among the 1430 macroblocks, reordering its
fragments, or extending/deleting the four singleton occurrences.

## 8. Exact remaining boundary

The row-replay plus scalar schedule problem is now exact for every labelled
four-sector linearization: compute the old-coordinate run list and minimize
(0.1).  If the schedule-independent four-local condition (6.2) holds, no
further schedule search is needed.  Without (6.2), a nonminimal
\(\tau\ge\rho^\delta\) can change active intersections while remaining
inside the 7401 budget.  The remaining exact envelope search is then over
the admissible pairs

\[
 \tau\ge\rho^\delta,
 \qquad \sum_j\delta_j+\sum_j\tau_j\le7401,
\]

followed by the literal tests \(E_p\ne\varnothing\).

What remains is construction rather than accounting:

1. label the 1430 UYAX macroblocks by all 24310 rank-nine owners exactly;
2. remove or move every forbidden short old-coordinate run;
3. satisfy the U-interior and UY/XU four-local collar conditions;
4. retain the full arbitrary upper-shadow tower; and
5. solve the lower Hall/common-Q compiler on the same chronology.

The unlabelled sector theorem supplies none of these five statements.  The
current contiguous-U artifact fails item 2 by Theorem 7.1, so the next
viable four-sector construction must genuinely split or rethread U.

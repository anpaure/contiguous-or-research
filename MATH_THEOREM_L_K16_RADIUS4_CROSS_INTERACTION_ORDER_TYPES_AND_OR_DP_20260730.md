# K16 H1 radius four: cross-interaction order types and the exact OR-state DP

Date: 2026-07-30

Status: unrestricted four-site inclusion-exclusion identity; complete
classification of the six portal/repair endpoint words; sound exact reduction
of the cross-only pair/pair complement.  No broad candidate search is claimed
or launched.

## 1. Frozen source and the precise open complement

The rooted source remains

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873; sole hole H=0x2c6d.
```

Let `P` be a two-site action which installs `H`, let `R` be a disjoint
two-site repair action, and let `D(P)` be the exact nonempty hole set after
`P`.  The previous screened run exact-replayed every retained row satisfying

```text
source-relative multiplicity gain of R at t > 0
for every t in D(P).
```

Here `retained` includes catalogue membership, disjoint final positions and
the old portal- and repair-pair-alone hole cap eight.

That test is complete across a fixed `0xffff` separator, but not in general.
An `R` action can have zero or negative net source-relative gain because it
destroys source witnesses which `P` has already destroyed, while still
creating a witness after `P`.  A final witness can also use intervals meeting
both logical pairs.  The exact missing object is therefore the mixed second
difference below, not an independently positive repair column.

The algebra in Sections 2--6 allows arbitrary old and new nonzero values and
has no hole cap.  The finite algorithm in Sections 7--8 can be instantiated
on the current 7,099-move catalogue and the old cap-eight portal bank, but
that instantiation is still only a declared branch of radius four.

## 2. The exact mixed Möbius column

Write `M(v)` for the 65,536-coordinate contiguous-OR multiplicity vector of a
word `v`, and use the code-sign column

\[
                    \Delta_X=M(w^X)-M(w).                 \tag{2.1}
\]

For disjoint edit sets `P,R`, define

\[
 \mathcal C(P,R)
   =\Delta_{P\cup R}-\Delta_P-\Delta_R
   =M(w^{P\cup R})-M(w^P)-M(w^R)+M(w).                   \tag{2.2}
\]

Thus

\[
 M(w^{P\cup R})-M(w^P)=\Delta_R+\mathcal C(P,R).         \tag{2.3}
\]

For one interval `I`, put

```text
l00 = OR_w(I),       l10 = OR_{w^P}(I),
l01 = OR_{w^R}(I),   l11 = OR_{w^{P union R}}(I).
```

Its contribution to (2.2) is the exact signed rectangle

\[
                    e_{l_{11}}-e_{l_{10}}-e_{l_{01}}+e_{l_{00}}. \tag{2.4}
\]

If `I` misses `P` or misses `R`, (2.4) is zero.  Hence only intervals meeting
at least one site of each logical pair can contribute.  In the signed
transport convention of item 1975,

\[
 \beta_{w,w^{P\cup R}}
   =\beta_{w,w^P}+\beta_{w,w^R}-\mathcal C(P,R).          \tag{2.5}
\]

The signs and multiplicities in (2.2)--(2.5) are essential.  A nonfull gap
or the existence of one final cross interval does not by itself imply a
positive correction: distinct rectangle rows can cancel.

## 3. Consecutive-block rectangle normal form

Sort the four distinct edited sites as

\[
                         x_1<x_2<x_3<x_4.
\]

Every interval meeting an edit has a unique first and last edited index
`[i,j]`; it contains exactly the consecutive edited sites
`x_i,...,x_j`.  Let `x_0=-1,x_5=n`.  For this class define:

* `L_i`, the multiplicity-compressed multiset of ORs
  `OR_w(l,...,x_i-1)` for `x_{i-1}<l<=x_i`;
* `R_j`, the corresponding multiset of ORs
  `OR_w(x_j+1,...,r)` for `x_j<=r<x_{j+1}`; and
* `g_ij`, the OR of all unchanged cells strictly between the selected edited
  sites `x_i,...,x_j`.

Empty fringes have OR zero.  Each compressed chain has at most seventeen
distinct masks at K16.

For `a,b in {0,1}`, let `q_ij^{ab}` be `g_ij` OR the values at edited sites
`i,...,j`, choosing the new `P` values exactly when `a=1` and the new `R`
values exactly when `b=1`.  Put

\[
 \Phi_{ij}(q)=
   \sum_{\lambda\in L_i,\rho\in R_j}
       \mu(\lambda)\mu(\rho)e_{\lambda\mathbin\lor q\mathbin\lor\rho}. \tag{3.1}
\]

### Theorem 3.1 (exact cross-interaction normal form)

\[
 \boxed{
 \mathcal C(P,R)=
  \sum_{\substack{[i,j]\text{ contains P and R}}}
   \left(\Phi_{ij}(q^{11}_{ij})-\Phi_{ij}(q^{10}_{ij})
        -\Phi_{ij}(q^{01}_{ij})+\Phi_{ij}(q^{00}_{ij})\right).} \tag{3.2}
\]

#### Proof

Partition all intervals by their first and last edited indices.  Formula
(2.4), summed over the exact left/right endpoint product for one class, is
the displayed summand in (3.2).  A monochromatic class misses one logical
pair and cancels.  Every bichromatic class occurs once.  QED.

At most 289 endpoint products occur in one `Phi`.  Direct four-term emission
therefore costs at most 4,624, 5,780 and 6,936 signed rows in the separated,
nested and alternating shapes respectively.  These are fixed K16 constants,
not products of word length.

For a target-only query, first convolve the two endpoint chains by OR:

\[
 h_{ij}(s)=\sum_{\lambda\lor\rho=s}\mu(\lambda)\mu(\rho). \tag{3.3}
\]

Then

\[
 \Phi_{ij}(q)(t)=
 \begin{cases}
 \displaystyle\sum_{t\setminus q\subseteq s\subseteq t}h_{ij}(s),
       &q\subseteq t,\\
 0,    &q\not\subseteq t.
 \end{cases}                                               \tag{3.4}
\]

Thus every rectangle coordinate is an exact Boolean interval-zeta query; a
complete 65,536-entry interaction column need not be materialized merely to
test a small debt set.

## 4. Complete endpoint-order classification

Color `x_1,...,x_4` by their logical roles.  There are six oriented words.
The notation `ij` below means the full consecutive span `[i,j]`; for example,
`13` contains sites `1,2,3`.  The audit JSON spells that same class `123` by
listing every contained edited index.

| oriented word | geometry | mixed spans in (3.2) |
|---|---|---|
| `PPRR` | portal left, repair right | `23,13,24,14` |
| `RRPP` | repair left, portal right | `23,13,24,14` |
| `PRPR` | alternating | `12,23,34,13,24,14` |
| `RPRP` | alternating | `12,23,34,13,24,14` |
| `PRRP` | portal outer, repair inner | `12,34,13,24,14` |
| `RPPR` | repair outer, portal inner | `12,34,13,24,14` |

There are four reversal orbits:

```text
{PPRR,RRPP}, {PRPR,RPRP}, {PRRP}, {RPPR}.
```

If reversal and exchange of the logical pair names are both forgotten, only
three unlabelled chord shapes remain: separated, alternating and nested.
The rooted K16 word is not reversal-symmetric and `P,R` have different
semantics, so an implementation must retain all six oriented words.

The old saturated-gap theorem is the pair of separated rows with the fixed
`23` gap equal to `0xffff`.  Every mixed span contains that gap, and every
rectangle in (3.2) vanishes.  More generally, the following are sufficient
classwise annihilators:

```text
PPRR/RRPP: the central bichromatic gap is full;
PRPR/RPRP: all three adjacent gaps are full;
PRRP/RPPR: the two outer bichromatic gaps are full.
```

The latter alternating/nested additive subfamilies are not recognized by the
old spatial `separated_saturated` predicate.  They are nevertheless already
inside the screened negative in its declared catalogue/cap scope, because
additivity forces the repair pair to have positive independent delta on every
portal debt.

## 5. Exact stateful `A(x)+B(y)+C(x OR y)` decomposition

Fix the portal action and put `u=w^P`.  Let the remaining repair sites be
`r<s`, with incumbents `a=u_r,b=u_s` and proposed values `x,y`.  Partition
intervals changed by the repair into the three exact classes:

```text
r but not s,        s but not r,        both r and s.
```

Their multiplicity columns depend respectively only on `x`, only on `y`, and
only on `z=x OR y`.  Denote them by `A^P_r(x),B^P_s(y),C^P_rs(z)`.  Then,
coordinatewise on all labels,

\[
 \boxed{M(u^{r\leftarrow x,s\leftarrow y})-M(u)
   =A^P_r(x)+B^P_s(y)+C^P_{rs}(x\lor y).}                 \tag{5.1}
\]

This is just the exact three-class pair-delta identity evaluated on the
portal state.  It is also (2.3), with the rectangles of Section 3 supplying
the change from the source banks to the portal-state banks.

For reference, the full stateful interval classes in (5.1) are shown below;
a singleton digit denotes the span `[i,i]`.

| word | left-repair `A` spans | right-repair `B` spans | joint `C` spans |
|---|---|---|---|
| `PPRR` | `3,23,13` | `4` | `34,24,14` |
| `RRPP` | `1` | `2,23,24` | `12,13,14` |
| `PRPR` | `2,12,23,13` | `4,34` | `24,14` |
| `RPRP` | `1,12` | `3,23,34,24` | `13,14` |
| `PRRP` | `2,12` | `3,34` | `23,13,24,14` |
| `RPPR` | `1,12,13` | `4,34,24` | `14` |

The joint OR state in (5.1) is unavoidable without an absorption lemma: the
all-four span alone can distinguish different values of `x OR y`.

## 6. Nonnegative debt-cover form

Multiplicity columns are needed for a final all-label decision, but the
portal debts have an even smaller exact representation.  Fix a target `T` in
`D(P)`.  Since `T` has no witness in `u`, every final `T` witness meets `r`,
`s`, or both.

Remove the incumbent at `r` and take the maximal fixed `T`-submask collar
through `r`, truncated before `s`; call its OR `c_r(T)`.  Define `c_s(T)`
symmetrically.  If every fixed cell between `r,s` is a `T`-submask, extend
through both edited sites and call the maximal fixed collar OR `c_rs(T)`;
otherwise the both-site form is unavailable.  Then the three witness forms
are exactly

\[
\begin{aligned}
 A_T(x)&:\quad x\subseteq T,\quad c_r(T)\lor x=T,\\
 B_T(y)&:\quad y\subseteq T,\quad c_s(T)\lor y=T,\\
 C_T(z)&:\quad z\subseteq T,\quad c_{rs}(T)\lor z=T,
              \quad z=x\lor y.                           \tag{6.1}
\end{aligned}
\]

Maximality proves necessity and sufficiency: any smaller compatible witness
is contained in the maximal collar, and the full collar itself is a witness
when the displayed OR reaches `T`.

Let `A(x),B(y),C(z)` be the subsets of `D(P)` supplied by the three forms.
The exact portal-debt condition is

\[
                     \boxed{A(x)\cup B(y)\cup C(x\lor y)=D(P).} \tag{6.2}
\]

Unlike a clipped source-relative gain signature, (6.2) is safe: the targets
were absent before the repair, so only existence of a new stateful witness is
being tested.  Covered low-reserve targets are not protected by (6.2), which
is why exact final replay remains mandatory.

## 7. Sound OR-sliced MITM/DP

Fix `P,r,s` and the genuine replacement domains `X,Y`.  Enumerate only OR
states `z` attainable as `x OR y`.  For one such state put

\[
                    Q_z=D(P)\setminus C(z).               \tag{7.1}
\]

For a fixed `x subseteq z`, the condition `x OR y=z` is exactly

\[
                      z\setminus x\subseteq y\subseteq z. \tag{7.2}
\]

Hence the right-side query is

\[
 y\in Y,\qquad z\setminus x\subseteq y\subseteq z,
 \qquad B(y)\supseteq Q_z\setminus A(x).                 \tag{7.3}
\]

This is a finite two-dimensional dominance query: a Boolean interval in the
16 value bits and a superset query in the debt-cover bits.  Under the current
portal cap, the latter signature has at most eight bits.

One exact DP implementation stores, for every realized `z` and lower mask
`l subseteq z`, the inclusion-maximal family

\[
 F_z(l)=\operatorname{Max}_{\subseteq}
        \{B(y):y\in Y,\ l\subseteq y\subseteq z\}.        \tag{7.4}
\]

It is built by a 16-bit superset-zeta recurrence, unioning families and
discarding coverage profiles contained in another profile from the same value
interval.  This pruning is exact only as a debt-feasibility **emptiness
oracle**.  Query (7.3) is nonempty exactly when one member of
`F_z(z\setminus x)` contains `Q_z\setminus A(x)`.

On a positive query the implementation must recover and enumerate every
original `y` satisfying (7.3), either by scanning the raw interval posting or
by retaining backpointers to all literal values/actions.  A discarded profile
can have better collateral behavior than a debt-profile dominator, so
replaying only one maximal representative would be incomplete.  Equivalently,
with signed debt-count vectors one joins

\[
 B_D(y)\ \ge\ {\bf1}-C_D(z)-A_D(x)                       \tag{7.5}
\]

coordinatewise.  Profiles in (7.5) must remain exact signed integers; the
Boolean version (7.4) is justified only by the absent-debt witness theorem of
Section 6, and signed dominance pruning is likewise an emptiness test unless
all qualifying literal action IDs are expanded.

A fully dense `(z,l)` lattice has
`sum_z 2^popcount(z)=3^16=43,046,721` cells.  With at most eight debts a
Boolean-profile antichain has size at most `C(8,4)=70`; a catalogue
implementation can build the table sparsely and on demand for realized `z`.

Every survivor receives the existing exact ten-class `four_delta` check and
a literal full-word replay.  Conversely, every completion together with one
enumerated `P/R` partition has a unique oriented word, repair positions,
values and realized OR state.  The positive-query expansion above therefore
recovers its literal action, and (6.2)--(7.3) retain it.  Exhaustion of this DP
is a no-go for whatever domains and portal bank are explicitly supplied to it.

The existing catalogue contains 7,099 moves on 288 positions and 24,348,717
distinct-position move pairs.  The old 775,506 retained repair actions are
**not** a safe universe for (7.3): that list intentionally requires a
positive source-relative residual gain.  A complete catalogue complement
must admit all pair actions before applying only independently proved domain,
disjointness and optional pair-hole-cap restrictions.

## 8. Disjoint rescue buckets for the old screened complement

There is a second exact formulation which reuses the old static pair columns
without repeating its already checked rows.  Order the debts of each portal.
For an in-scope repair pair omitted by the screen, let `t_j` be the first debt
with

\[
                         \Delta_R(t_j)\le0.               \tag{8.1}
\]

Assign the pair to rescue bucket `j`, and evaluate the target-only rectangles
of (3.2).  It can survive only if

\[
             \Delta_R(t_j)+\mathcal C(P,R)(t_j)\ge1.      \tag{8.2}
\]

Then check the same inequality on every debt and perform exact final replay.
The first-failed-debt buckets are disjoint and cover every pair-cap-eight,
catalogue-valued completion omitted solely by the old independent-gain
screen.  Rows with positive static gain on every debt were already replayed;
separated saturated rows cannot survive a rescue bucket because their mixed
column is zero.

If the repair pair-alone cap is removed, pairs omitted only by that cap must
also be admitted even when they satisfy the old positive-gain test.  Thus
(8.1) partitions the old capped complement, while the stateful DP of Section
7 is the uniform reduction for a widened domain.

## 9. Light exact verification

The checker

```text
scratch/audit_k16_radius4_cross_order_type_normal_form_20260730.py
SHA-256 4a3bf627960cd158f76c82d6f3ec31e8ee9e72d67b71d212c0b0d72a66f6f6dd
```

independently enumerates the consecutive-block tables for all six oriented
words.  On 3,000 deterministic literal small-word trials it verifies, label
by label,

```text
four-edit delta = portal delta + repair delta + mixed rectangle column,
portal-state repair delta = left-only + right-only + joint-OR column.
```

It additionally checks the exact maximal-collar witness equivalence on
765,000 targets and (3.4) on 256,000 target queries.  It reports

```text
scratch/k16_radius4_cross_order_type_normal_form_20260730.audit.json
SHA-256 a8d055076f20253a083ac7f16b52f7fa199528922e070a9cfc55e798ef9f20a1
payload b2eb7c2da9963632e5257623a5877a14e14dd796807aedd1ca0cdc42295cb8ea
status PASS_ALL_SIX_ORDER_TYPES.
```

This is a proof-primitive regression, not a K16 candidate census.  No H100
job or duplicate broad search was used.

## 10. Exact frontier

The present theorem removes the logical gap in the pair/pair machinery: no
full separator and no independently positive repair column is needed for the
normal form or DP.  A finite exhaustion on the current catalogue with the same
cap-eight portal and repair banks would close the precise cross-only complement
of item 1973.  Admitting all catalogue repair pairs regardless of their
pair-alone hole count would close a strictly wider repair branch.

It would not yet prove unrestricted radius four.  Such a theorem must also
handle:

1. values outside the 7,099-move catalogue;
2. every H-installing pair without an intermediate-hole cap;
3. repair pairs outside the old pair-alone cap;
4. four-edit completions for which no two-site subset installs `H` alone,
   including genuine three-/four-site `H` witnesses; and
5. unrelated length-12,873 basins.

Repeated-site edit chronologies must first be collapsed to their final
distinct Hamming support.  The global bracket remains

```text
12873 <= nu(16) <= 12874.
```

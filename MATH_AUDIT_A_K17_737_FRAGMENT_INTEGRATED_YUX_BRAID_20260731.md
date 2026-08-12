# Audit of the K17 737-fragment integrated YUX braid

Date: 2026-07-31  
Status: exact palette and staircase audit; authenticated local forest; global
connector chronology remains open  
Scope: the frozen PBBS 737-fragment U bank and its occurrence-labelled
YUX/YX and balanced-A certificates

## 0. Verdict

Leaving the U shore as 737 protected paths is compatible with the exact
four-sector arithmetic.  It removes the need for a standalone 5005-state U
Hamilton path, but only by replacing it with one coupled connector problem
on 1430 protected local components.

There are two related ledgers, and they must not be conflated.

1.  In a **linear** order of 1430 Catalan macros, insert the 737 U paths into
    737 of the 1429 macro gaps.  The no-tag lower-q1 count is

    \[
      4268+2(737)+(1429-737)=6434,                  \tag{0.1}
    \]

    so the unique path hole is no-tag.
2.  The authenticated local certificate instead makes 1430 disconnected
    YUX/YX units: 737 YUX units and 693 direct YX units.  It has

    \[
      4268+2(737)+693=6435                         \tag{0.2}
    \]

    distinct no-tag colours, hence the entire no-tag palette.  After one
    distinct A owner is attached to every unit, the frozen forest has lower
    signature ledger

    \[
       (00,x,y,xy)=(6435,715,715,0).                \tag{0.3}
    \]

    Completing this forest to one spanning path needs 16,444 further edges,
    while its remaining tagged palette has 16,445 colours.  Therefore any
    residual tagged-colour-simple completion retaining every frozen edge has
    exact one-hole equation

    \[
       h_{00}=0,
       \qquad h_x+h_y+h_{xy}=1.                    \tag{0.4}
    \]

    Equivalently, if a colour-simple full cyclic completion exists, it uses
    every lower colour and opening one tagged connector creates the sole path
    hole.  Numerically, deleting a retained YX rung instead changes the
    no-tag count to (0.1); realizing that deletion as a single linear braid
    still requires the global connector chronology.

The staircase cost is not 737, 1474, or any other seam count.  For a final
lower-rainbow chronology, singleton positive runs are impossible, so the
canonical cost is exactly

\[
                    \rho_2+\rho_3.                 \tag{0.5}
\]

The authenticated balanced-A forest has no internal run of length one or
two.  It has exactly 175 internal length-three runs, all in old coordinates,
across 151 of its 1430 components.  Those components have total current span
1995.  If they form an initial segment and \(g\) connector vertices occur
before the last one, their certified contribution satisfies
\(\rho_3\le1991+g\).  Hence \(\Delta_{17}\) absorbs this complete local debt
whenever \(g\le5410\).  Under the component-contiguous balanced-packet
hypotheses stated in Corollary 7.1, \(g\le11(151)=1661\), giving the explicit
bound \(\rho_3\le3652\).

This is conditional, not a completed schedule.  The 1430 components retain
many short boundary arms, and the missing connector paths can close such an
arm into a late length-two or length-three run.  The exact remaining test is
the run-summary product on the actual global order.  Hence \(\Delta_{17}=7401\)
absorbs all presently certified fragment-interior defects under a
front-loading order, but it does **not** automatically absorb all future
connector boundaries.

No labelled global K17 carrier, all-upper theorem, or common-Q compiler is
claimed.

## 1. Frozen lineage

The U bank is

```text
scratch/k17_pbbs_u_upper_complete_20260731.fragments
SHA-256 f7ea82ae64a396da5db80836af55c16f3ebc8b96e8e354384423b4b96df944c8
```

with independent audit

```text
scratch/k17_pbbs_u_upper_complete_factor_independent_20260731.audit.json
SHA-256 c9913e87705b5f2001434340d48b7e523e168706708a1e5fbb843c0165b2557f
```

It partitions all 5005 U owners into 737 literal Johnson paths.  The paths
have 4268 distinct internal rank-eight intersection colours, cover every
old upper target of ranks 10 through 15 internally, and contain no
fragment-interior positive run of length one or two.

The first integrated certificate is

```text
scratch/k17_pbbs_u_yux_bridge_matching_20260731.tsv
SHA-256 e602f2f3abc91909bec42bdde02422001d9c78f354207c7fd69b0288d99c4148
```

with audit

```text
scratch/k17_pbbs_u_yux_bridge_matching_20260731.audit.json
SHA-256 ce666738203f9c5c45a180314507c0c85dcf504d1194caf90cb481412611dc74
```

The audit's corrected owner ledger is

\[
  \text{used }(U,A,X,Y)=(5005,0,1430,1430),
\]

\[
  \text{remaining }(A,X,Y)=(6435,5005,5005).        \tag{1.1}
\]

An earlier live JSON incorrectly wrote 5005 remaining A owners; the frozen
hash above contains the corrected value 6435.

The balanced A augmentation is

```text
scratch/k17_pbbs_u_yaux_balanced_bridge_20260731.fragments
SHA-256 23d889267915e45401cf72ca62aa5a789eb84213f6f132ea8352a05efc2e8d47
```

with ledger and audit

```text
scratch/k17_pbbs_u_yaux_balanced_bridge_20260731.tsv
SHA-256 669bd79b628f31bc1fb3eb2d2fcec7f50dc102e861a34944f13e2a8dae4c25b3

scratch/k17_pbbs_u_yaux_balanced_bridge_20260731.audit.json
SHA-256 1a54589de7cd1964abef7ae1d62f5b5724d5a117e1933c27ca16f3e93ead2047
payload 0a4aaf0d1da45b561edd0c5ab27e52b4d90595a4983aa672c5f9c5b7366f9662
```

All claims below were independently replayed from these literal files.  No
row order in a `.fragments` file is interpreted as a global chronology.

## 2. Rank-eight seam signatures

Let \(E=[15]\) and let \(x,y\) be the new coordinates.  Write the owner
types as

\[
 U=V,
 \quad X=T+x,
 \quad Y=T+y,
 \quad A=C+x+y,
\]

where \(|V|=9,|T|=8,|C|=7\).  A Johnson edge between rank-nine owners has
a rank-eight intersection.  Its new-coordinate signature is exactly

\[
\begin{array}{c|c}
\text{edge type}&\text{intersection signature}\\ \hline
AA&xy\\
AX,XX&x\\
AY,YY&y\\
UU,UX,UY,XY&00.
\end{array}                                         \tag{2.1}
\]

An AU edge is impossible: its intersection omits both new coordinates and
has old rank at most seven, whereas a Johnson intersection must have rank
eight.

The occurrence-labelled conditions for the no-tag external seams are

\[
\begin{array}{c|c|c}
\text{seam}&\text{Johnson condition}&\text{lower colour}\\ \hline
Y(T)-X(S)&T=S&T,\\
Y(T)-U(V)&T\subset V&T,\\
U(V)-X(S)&S\subset V&S,\\
U(V)-U(V')&|V\cap V'|=8&V\cap V'.
\end{array}                                         \tag{2.2}
\]

Thus a YUX insertion

\[
 Y(T_L)-Q(V^-,\ldots,V^+)-X(T_R)                   \tag{2.3}
\]

is legal precisely when \(T_L\subset V^-\) and \(T_R\subset V^+\), after
possibly reversing \(Q\).  Its two lower colours are \(T_L,T_R\), and its
two upper-q1 unions are respectively \(V^-+y,V^++x\).  A direct YX pair
has common projection \(T\), lower colour \(T\), and upper union \(T+x+y\).

## 3. Component neutrality and the linear one-hole theorem

Suppose the U deck is split into \(f\) nonempty paths.  Its internal no-tag
edge count is

\[
                       5005-f.                      \tag{3.1}
\]

The A, X, and Y decks are split into 1430 Catalan macros.  Their fixed
internal and socket counts are

\[
 AA=5005,
 \qquad XX+AX=5005+1430=6435,
 \qquad YY+YA=6435.                                 \tag{3.2}
\]

These already saturate the \(xy,x,y\) target families.  Therefore every
external seam of a lower-rainbow completion must have signature 00.

There are \(1430+f\) macro/U components, hence \(1429+f\) external seams in
one component-level path.  Combining with (3.1),

\[
 (5005-f)+(1429+f)=6434.                            \tag{3.3}
\]

The component count cancels.  For \(f=737\), inserting each U path into a
different internal macro gap gives

\[
 4268+1474+692=6434.                                \tag{3.4}
\]

If, as in the authenticated U bank, the 4268 internal U colours are
pairwise distinct, and \(\mathcal C_U\) denotes their palette, then

\[
 \mathcal P={E\choose8}\setminus\mathcal C_U,
 \qquad |\mathcal P|=2167.                          \tag{3.5}
\]

For a legal all-00 component path satisfying the targetwise-exact tagged
ledger (3.2), lower-colour simplicity is equivalent to its 2166 external
seam colours injecting into \(\mathcal P\).  In that case their unique unused
member \(h\in\mathcal P\) is exactly the no-tag boundary hole.  Equivalently,
if these 2166 seam colours are distinct, avoid the 4268 internal U colours,
and (3.2) is targetwise exact, the complete lower palette has exactly one
hole and it is no-tag.  Conversely, any repeated seam colour or collision
with the internal U palette produces at least one additional no-tag hole.

This proves that U Hamiltonization is not required by lower-q1 counting.
It does not produce the labelled sockets.

## 4. The authenticated 1430-unit local cover

The frozen YUX matching realizes a different, pre-opening object.  It uses

\[
 737\text{ YUX units},
 \qquad 693\text{ direct YX units}.                 \tag{4.1}
\]

Its 1474 bridge colours and 693 direct colours are distinct, avoid the 4268
internal U colours, and together with them enumerate all 6435 no-tag colours:

\[
 4268+1474+693=6435.                                \tag{4.2}
\]

The selected 1430 Y owners are distinct, as are the selected 1430 X owners.
Every local unit is Johnson and contains no interior `010` or `0110` in any
of the 17 coordinate traces.

This certificate is not a linear carrier: it has 1430 disconnected local
components.  Equation (4.2) is therefore not evidence for (3.4), whose
direct-pair count is 692.  Numerically, deleting one of the 693 direct YX
rungs changes the no-tag ledger from 6435 to 6434, the same count as (3.4),
but it also splits that local component.  Realizing this palette ledger as
the opening of one cyclic or linear braid still requires the global
connector chronology.

The balanced A certificate attaches 1430 distinct A owners, 715 on each
outer side.  The exact component forms are

\[
\begin{array}{c|r}
AYUX&369\\
YUXA&368\\
AYX&346\\
YXA&347.
\end{array}                                         \tag{4.3}
\]

It has 9295 distinct owners and 7865 pairwise-distinct internal lower
colours, and has lower signature histogram (0.3).  It leaves exactly

\[
 |A_{\rm rem}|=|X_{\rm rem}|=|Y_{\rm rem}|=5005.   \tag{4.4}
\]

All 4944 no-new upper targets of old ranks 10 through 15 retain an internal
witness in one protected U fragment.

## 5. Exact residual one-hole ledger

The remaining lower-colour demands after (0.3) are

\[
 x:5720,
 \qquad y:5720,
 \qquad xy:5005,                                    \tag{5.1}
\]

of total

\[
                       16445.                       \tag{5.2}
\]

There are 15,015 unused owners and 1430 current components.  Adding all
unused owners and joining the components into one spanning path needs

\[
                  15015+(1430-1)=16444             \tag{5.3}
\]

new edges.  Let \(e_x,e_y,e_{xy}\) be the numbers of distinct residual
colours of the indicated signatures realized by the new edges.  Therefore
any colour-simple completion that retains every frozen edge satisfies
exactly

\[
 h_{00}=0,
 \qquad
 (5720-e_x)+(5720-e_y)+(5005-e_{xy})=1.             \tag{5.4}
\]

Under these hypotheses every new edge must have tagged signature.  In
particular, adding a new 00 edge repeats an already complete palette and
forces an extra hole unless a frozen 00 edge is first deleted.

More generally, let \(m_c\) be the multiplicity of lower colour \(c\) in a
completed 24,309-edge path and put

\[
                 e=\sum_c(m_c-1)_+.
\]

Then the number of lower-q1 holes is exactly

\[
                         1+e,                        \tag{5.4a}
\]

because the number of distinct colours is \(24309-e\) out of 24,310.
Thus one-hole completion is equivalent to literal colour injectivity.

Any colour-simple single spanning-cycle completion retaining the frozen
forest would use all 16,445 remaining colours.  Opening one of its new
connector edges gives (5.4), and its signature identifies the sole hole.
Opening one of the 693 frozen direct YX rungs has the subtype count (3.4),
but no common cyclic chronology realizing either opening is presently
authenticated.

For such a colour-simple spanning-cycle completion, the residual palette
equations together with the owner-degree equations uniquely force

\[
 AA=5005,
 \quad XX=5005,
 \quad AX=715,
 \quad YY=5005,
 \quad AY=715.                                      \tag{5.5}
\]

These numbers meet every residual owner degree and every colour count.  They
are not a matching or connectivity theorem.

## 6. Exact staircase charge of the insertions

Consider first a *hypothetical regrouped completion* in coherent cyclic
packet notation

\[
                   A_i\,Y_i\,P_i\,X_i,              \tag{6.0}
\]

where \(P_i\) is a U fragment or is empty.  Choose this order, or its
simultaneous reversal, and choose the block lengths so that

\[
 |A_i|+|Y_i|=9,
 \qquad |X_i|+|A_{i+1}|=9.                          \tag{6.0a}
\]

This is not the literal order
of the frozen balanced-A forest, whose components have the mixed forms
AYUX, YUXA, AYX, and YXA.  Because every row of \(P_i\) omits both new
coordinates, inserting it
between Y and X only lengthens a zero-gap.  It neither splits nor shortens a
positive x- or y-run.  Thus every new-coordinate positive run has length
nine and the U insertions have exactly zero new-coordinate staircase cost.
All remaining cost below concerns the fifteen old coordinates.

For a complete linear chronology \(P\), let \(\rho_j(P)\) be the latest
start of an interior positive coordinate run of length at most \(j\), with
zero when none exists.  If all lower-q1 edge colours of \(P\) are distinct,
then

\[
                         \rho_1(P)=0.                \tag{6.1}
\]

Indeed, an isolated positive state has both adjacent intersection colours
equal to that state with the isolated coordinate deleted.

Hence, for the canonical tail-start schedule, the K17 staircase cost is
exactly

\[
                    \operatorname{Cost}(P)
                       =\rho_2(P)+\rho_3(P),          \tag{6.2}
\]

and that schedule absorbs the chronology exactly when

\[
                         \rho_2(P)+\rho_3(P)\le7401. \tag{6.3}
\]

Equivalently, \(\rho_2\) is the latest start of a `0110` trace and
\(\rho_3\) is the latest start of a `0110` or `01110` trace; `010` is
excluded by (6.1).

This is a maximum-position charge, not a sum over boundaries.  One late
`0110` contributes its start to both frontiers, while arbitrarily many
seams contribute zero when their composed traces have no short run.

For exact arbitrary starts, let \(\delta\) and \(\rho_j^\delta\) be the
adjusted quantities from
`MATH_THEOREM_A_K17_UYAX_ARBITRARY_START_STAIRCASE_20260731.md`.  Since no
singleton run exists, \(\rho_1^\delta=0\), and the exact row/scalar criterion
is

\[
 \min_{24310\ge\delta_1\ge\delta_2\ge\delta_3\ge0}
 \left(
   \delta_1+\delta_2+\delta_3+
   \rho_2^\delta+\rho_3^\delta
 \right)\le7401.                                    \tag{6.4}
\]

All variables are integral.  A full Johnson chronology automatically has
nonempty depth-three envelopes, since four consecutive rank-nine owners
intersect in at least six coordinates.

### Theorem 6.1 (exact insertion-summary law)

For each oriented component \(Q\) and coordinate \(z\), record:

1. its length \(|Q|\);
2. whether every row contains \(z\);
3. its positive prefix and suffix lengths, capped at four; and
4. the latest local starts of its interior runs of lengths at most two and
   at most three, using an explicit absent value \(-\infty\), not the
   numerical start zero.

These records have an associative concatenation product.  For a proposed
component order with absolute component starts \(p_i\), the global
\(\rho_2,\rho_3\) are exactly the maxima of:

* shifted component-internal starts \(p_i+r_{i,j}\);
* joined suffix--prefix runs when both seam endpoint bits are one; and
* one-sided boundary runs that become interior when a positive suffix is
  followed by zero, or when a positive right prefix is preceded by zero and
  later closes.

Consequently no scalar charge depending only on the number of fragments or
seams can replace (6.3).

#### Proof

Internal runs persist, with starts shifted by the preceding stored length.
At one seam there are four endpoint cases.  If both endpoint bits are one,
the left suffix and right prefix join.  If the left endpoint is one and the
right is zero, the left suffix closes and becomes an interior run.  If the
left endpoint is zero and the right is one, the right prefix ceases to be a
left-boundary run if it later closes; if the whole remaining word is one it
stays boundary-exempt.  If both are zero, no positive seam run occurs.  The
all-one flags propagate a boundary run through a whole component, and the
capped lengths decide exactly whether every resulting run has length one,
two, three, or at least four.  The absent sentinel prevents a nonexistent
local frontier from becoming a spurious start after shifting.  Taking the
relevant maxima gives the stated record.  Both parenthesizations compute the
literal run data of the same concatenated word, proving associativity.
\(\square\)

## 7. Quantitative audit of the authenticated forest

Direct replay of the YUX certificate gives:

\[
 \rho_1^{\rm local}=\rho_2^{\rm local}=0,
\]

with exactly 102 internal length-three runs across 90 YUX units.  Those 90
units have total span 1406, including their Y and X endpoints.

After balanced A attachment, the exact figures are:

\[
\begin{array}{c|c}
\text{interior length-one runs}&0\\
\text{interior length-two runs}&0\\
\text{interior length-three runs}&175\\
\text{components containing them}&151\\
\text{total current span of those components}&1995\\
\text{largest local length-three start in the stored orientations}&88.
\end{array}                                         \tag{7.1}
\]

All 175 runs use old coordinates; the two new coordinates contribute none.

The fragments are nevertheless not globally residence-safe.  Across all
1430 components and 17 coordinates, the prefix-run census, capped at four,
is

\[
 0^{11440}1^{1430}2^{1430}3^{5588}(\ge4)^{4422},    \tag{7.2}
\]

and the suffix census is identical.  There are 7680 coordinate/component
pairs which are positive through the whole component.  Thus a connector can
close a length-one or length-two arm unless the exact summary transition is
guarded.

### Corollary 7.1 (conditional front-loading bound)

Suppose the 151 components in (7.1) form the initial dangerous segment of a
global order.  Let \(g\) be the number of connector vertices interleaved
before the last of those components.  Suppose also that connector interiors
and all new seams create no additional run of length at most three.

The 151 current components have total length 1995.  An internal length-three
run begins at least four positions before the end of its component.  Hence

\[
                 (\rho_1,\rho_2,\rho_3)
                    =(0,0,R),
 \qquad R\le1991+g.                                  \tag{7.3}
\]

The explicit tail-start schedule

\[
 \alpha=(24310,24310,24310),
 \qquad \tau=(0,0,R)                                \tag{7.4}
\]

therefore passes whenever

\[
                         g\le5410.                   \tag{7.5}
\]

At \(g=0\) it retains at least 5410 units of scalar surplus.  For the
following stronger numerical specialization, suppose a component-contiguous
balanced packet completion exists, the 151 dangerous components occupy its
initial 151 packets, and no connector vertices from any other packet are
interleaved before them.  Choose exactly 715 cyclic indices with \(a_i=4\)
and the other 715 with \(a_i=5\), and put

\[
 a_i\in\{4,5\},\qquad y_i=9-a_i,\qquad
 x_i=9-a_{i+1}.                                    \tag{7.5a}
\]

Then a full packet has \(18-a_{i+1}\in\{13,14\}\) non-U owners.  Each
dangerous component already contains three non-U owners, so at most eleven
additional owners precede the end of its packet.  Consequently

\[
 g\le11(151)=1661,
 \qquad R\le3652,
 \qquad 7401-R\ge3749.                              \tag{7.6}
\]

The corollary proves that the authenticated fragment-interior defects are
quantitatively absorbable.  Its ordering and clean-connector hypotheses are
not supplied by the current artifacts.

## 8. Exact remaining theorem

The standalone U-path gate has been removed from the construction target.
The exact successor is now:

> On the remaining 5005 A, 5005 X, and 5005 Y owners, choose a
> colour-simple tagged connector system which joins the 1430 frozen local
> components into one path, omits exactly one colour from (5.1), preserves
> every required new-tag upper target, and whose global run-summary product
> satisfies (6.3) or (6.4).

The local forest already supplies:

* every U owner exactly once;
* the complete no-tag lower-q1 palette;
* every no-new upper target internally;
* exact owner balance after A attachment; and
* no internal run of length one or two.

What remains unproved is the common tagged connector chronology, including
connectivity, the one tagged hole, boundary-arm compatibility, new-tag upper
shadows, and the lower common-Q compiler.  The number 737 creates neither a
palette deficit nor an additive staircase deficit; all surviving difficulty
is occurrence-labelled and order-sensitive.

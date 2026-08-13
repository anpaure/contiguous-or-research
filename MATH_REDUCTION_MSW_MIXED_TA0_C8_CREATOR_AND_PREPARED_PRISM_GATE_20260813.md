# A native `C8` creates the first long low-renewal MSW hole, but it is not the prepared-prism carry

**Date:** 2026-08-13  
**Method:** exact MSW touching-step rule, exact `Gamma` multiplicities, and
the Boolean incidence context-transport identity; exhaustive work only on
`h100`  
**Status:** unconditional local theorem and exact all-parameter reduction.
The first long low-renewal target has an explicit native alternating `C8`
creator, and a mixed `C8+4C6` packet closes it.  The mixed packet is proved
not to be a literal realization of the previously proposed prepared prism.
An all-renewal theorem is reduced to one finite, recursively substitutable
owner-changing prism module.  The frozen base relay is proved internally
support-monotone at every linear upper width.  The module, its resident
collar, and exterior/lifted-closure protection are not proved here.

## 1. The low-renewal slice

Write

\[
 T_a=(1100)^a1111,
 \qquad a\ge2,                                      \tag{1.1}
\]

so `T_a` has length `4a+4` and semilength

\[
                         r=2a+2.                    \tag{1.2}
\]

The chamber theorem gives canonical multiplicity zero for every `a>=3`.
The frozen two-hex relay is `T_2`; `T_3,T_4` have native closed four-`C6`
repairs.  Starting at `T_5`, no native canonical `C6` creates the target.
The next native atom is a `C8`.

## 2. An explicit `C8` creator for `T_5`

Put

```text
S = 110011001111,
xi = its first coordinate,
zeta = its penultimate coordinate,

A0 = 110001000100,
A1 = 110001001100,
A2 = 110001101100,
A3 = 110001100100.
```

Define four rank-`r` owners

\[
\begin{aligned}
 O_0&=A_0S,\\
 O_1&=A_1(S-\zeta),\\
 O_2&=A_2(S-\xi-\zeta),\\
 O_3&=A_3(S-\xi),                                  \tag{2.1}
\end{aligned}
\]

and four rank-`r+1` colours

\[
\begin{aligned}
 Q_0&=A_1S,\\
 Q_1&=A_2(S-\zeta),\\
 Q_2&=A_2(S-\xi),\\
 Q_3&=A_3S.                                         \tag{2.2}
\end{aligned}
\]

The exact touching-step rule says that `Q_i` is unselected at `O_i` and
selected at `O_(i+1)` (indices modulo four).  Thus

\[
 O_0Q_0O_1Q_1O_2Q_2O_3Q_3O_0                     \tag{2.3}
\]

is a literal alternating incidence `C8` in the canonical semilength-12
MSW path factor.

The untouched selected mates are

\[
 E_0=O_0+5,
 \quad E_1=O_1+19,
 \quad E_2=O_2+15,
 \quad E_3=O_3+8.                                  \tag{2.4}
\]

Put

\[
 N_i=E_i\cup Q_{i-1},
 \qquad P_i=E_i\cup Q_i.                           \tag{2.5}
\]

The complete q2 current is

\[
             \partial_2 C_8=\sum_{i=0}^3[P_i]-\sum_{i=0}^3[N_i]. \tag{2.6}
\]

Its exact word and multiplicity ledger is

```text
positive target                                      base load
P0 = 110011001100110011001111 = T5                       0
P1 = 110001101100110011101101                            0
P2 = 110001101100011011001111                            0
P3 = 110001110100110011001111                            0

negative target                                      base load
N0 = 110011100100110011001111                            1
N1 = 110001001100110011101111                            1
N2 = 110001101100111011001101                            1
N3 = 110001111100010011001111                            2
```

Hence the `C8` creates `T_5` and three companion holes, transports three
unit-load debts, and spends only one of the two providers of `N3`.

### Proof

For `(2.3)`, the selected addition pairs at `O_0,...,O_3` are respectively

```text
{5,7}, {19,23}, {13,15}, {8,9}.
```

The incoming additions are `7,23,13,9`, giving `(2.4)` as the other
selected additions; the outgoing additions are `9,7,23,13`.  This checks
alternation and `(2.6)` directly.  Applying the exact height/corridor/
ordinal `Gamma` inverse criterion to the eight displayed targets gives
the listed loads. `square`

## 3. The aligned creator persists briefly, then changes phase

The same display works with

\[
 S=(1100)^{a-3}1111                                \tag{3.1}
\]

for `a=5,6,7,8`, if `xi` is chosen at the following one-based position
inside `S`:

\[
\begin{array}{c|cccc}
a&5&6&7&8\\ \hline
\operatorname{pos}_S(\xi)&1&2&5&6.
\end{array}                                        \tag{3.2}
\]

The other selected addition at `O_2` is at suffix position `3,3,7,7`,
respectively.  The other selected addition at `O_3` is the global
coordinate `8,8,11,11`, respectively.

This is not an all-`a` fixed-prefix formula.  Already at `a=7,8`, the
fourth negative term has canonical load one rather than two, and at `a=9`
the fixed prefixes in `(2.1)` no longer give an alternating cycle.  Native
`C8` creators still exist, but their touching-step phase has moved.  Thus
the finite data do not support the claim that one fixed `C8` packet simply
tensors through arbitrary `1100` renewals.

The target-local touching-step enumeration gives the following exact first
atom data:

\[
\begin{array}{c|c|c}
a&r&\text{shortest native creator found}\\ \hline
3&8&C6\\
4&10&C6\\
5&12&C8\\
6&14&C8\\
7&16&C8\\
8&18&C8\\
9&20&C8\\
10&22&C8\\
11&24&C8.
\end{array}                                        \tag{3.3}
\]

For `a=5,...,11`, the exact number of target-local `C6` creators is zero.
For `a=5`, enumeration of all `5,696,076` endpoint-inclusive native
alternating `C6`s independently gives the same zero.  There are eleven
native `C8` creators at `a=5`; none is support-safe by itself.

One of those `C8`s followed by four owner-disjoint native `C6`s has exact
final q2 support containing the entire canonical support together with
`T_5`.  It uses five owner-disjoint trades and therefore is a literal
simultaneous switch packet in the canonical factor.  This proves a positive
mixed repair at the first phase change.  It does not prove a recurrence.

## 4. The mixed packet is not the Boolean prepared prism

Let `Z_0` be the signed incidence circulation of the frozen `T_2` relay.
It consists of two edge-disjoint `C6`s, hence

\[
                         |\operatorname{supp} Z_0|=12.          \tag{4.1}
\]

For the two-step context path

```text
                         1100 -> 1001 -> 0011,
```

the context-transport theorem gives

\[
 (Z_0)_{1100}-(Z_0)_{0011}
       =-\sum_{e\in Z_0}\epsilon_e
          (H_e^{1100\to1001}+H_e^{1001\to0011}).   \tag{4.2}
\]

After toggling the source copy and sweeping a prepared annulus satisfying
the alternating incidence hypotheses, every interior rail returns to its
original phase.  At the **incidence-chain** level the final signed
difference is exactly `(Z_0)_(1100)`, and therefore has twelve supported
incidences.  This statement does not by itself determine ordered q3+
windows.

By contrast, the closed `T_5` mixed packet has one `C8` and four `C6`s on
pairwise disjoint owner supports.  Its signed incidence difference has

\[
                         8+4\cdot6=32              \tag{4.3}
\]

distinct supported incidences.  There is no cancellation because the
owner sets are disjoint.

### Theorem 4.1 (exact non-identification)

The native `C8+4C6` repair of `T_5` is not a literal prepared-prism
realization of the Boolean context transport `(4.2)`.  In particular it is
not obtained by toggling a source `T_2` relay and restoring every internal
annulus rail.

### Proof

The two final signed incidence chains have support sizes twelve and
thirty-two by `(4.1)` and `(4.3)`, so they are unequal. `square`

Their difference is another nonzero incidence circulation.  Equality of
their q2 target names, or the fact that both repair a low-renewal hole,
would not erase this occurrence-level distinction.

## 5. Exact all-renewal finite-module reduction

The algebraic all-renewal identity is already unconditional.  A literal
all-`a` owner-changing theorem needs one finite **prepared low-renewal
module** on the base relay plus one `1100` context block.  Its data are:

1. the two contextual boundary copies of the twelve incidences of `Z_0`;
2. the twenty-four transport `C6`s in `(4.2)` and complementary initial
   rail phases;
3. the untouched second selected colour at every boundary owner;
4. literal spare-provider occurrences for every negative terminal turn;
5. an ordered exterior socket map making the annulus chronology-faithful;
6. a protected owner-changing factor completion containing all selected
   incidences and excluding all unselected incidences; and
7. a recursive terminal signature identical to the source signature, so
   another copy of the module may be substituted at the next renewal.

For the all-width consequence, item 5 means the stronger ordered all-q
chronology condition of Corollary 6.2, not only equality of external socket
names.

Call these seven conditions `PP_1100`.  The reflected module `PP_high`
has the analogous data for a high renewal.

### Theorem 5.1 (finite recursive module suffices)

If `PP_1100` and `PP_high` exist and their recursive substitutions can be
chosen occurrence-disjoint in distinct suffix/chamber fibres, then the two
frozen base relays `T_2` and `B8` transport through every word of the exact
one-counter renewal grammar.  Every transported operation is a literal
owner-changing factor rethread, not a source-only common-history splice.

The final q2 current in each fibre is the contextual copy of the relevant
base current, the component permutation is conjugate to the base
permutation, and the reverse suffix stem is untouched.

### Proof

For one context edge, the alternating-annulus lemma turns the signed
identity into a literal sweep under conditions 1--6.  All internal rails
are restored, while the source boundary is replaced by the destination
copy.  Condition 7 permits induction on the number of renewals.  The
context-transport endpoint-coboundary theorem gives the q2 and component
claims.  Suffix projection gives disjointness and leaves the suffix-side
stem unchanged. `square`

This is a finite-module reduction, not an existence proof for `PP_1100`.
The unchanged canonical MSW factor fails the complementary rail phase at
five of the six owners of `Z_0`, so a genuine owner-changing host is
necessary.

## 6. The base relay is internally all-width support-monotone

Let `D_q(F)` be the support of unions of `q` consecutive q1 colours on the
linear z-free paths of an even MSW incidence factor.  This convention gives
the usual q2 turns at `q=2`; it also retains lower-rank coincidences created
by a rethread, rather than silently grading them away.

### Theorem 6.1 (complete finite base audit)

Let `F_6` be the canonical semilength-six path factor and let `F'_6` be its
image after the two literal `T_2` hexagons.  Then

\[
                         \boxed{D_q(F_6)\subseteq D_q(F'_6)
                                \quad(1\le q\le6).}              \tag{6.1}
\]

The exact support counts are

\[
\begin{array}{c|rrrrrr}
q&1&2&3&4&5&6\\ \hline
|D_q(F_6)|&792&407&184&62&12&1\\
|D_q(F'_6)|&792&408&186&67&17&6\\
\text{old casualties}&0&0&0&0&0&0.
\end{array}                                                     \tag{6.2}
\]

The old path-length histogram is `{6:132}` and the new one is
`{4:2,6:128,8:2}`.  In particular the audit does not assume that the
rethreaded paths retain their old lengths.

### Proof

The finite exact audit reconstructs all 132 canonical paths from the `g,h`
touching-step maps, verifies the twelve deleted and inserted incidences in
the two frozen hexagons, traverses every resulting path, and enumerates
every consecutive colour window.  Direct counter comparison gives `(6.2)`.
The script is listed in Section 8. `square`

### Corollary 6.2 (conditional internal all-width transport)

Assume each prepared prism satisfies the **ordered all-q chronology**
hypothesis of Theorem 4.1 in
`MATH_THEOREM_MNW_FULL_01_TO_10_ANNULUS_CURRENT_TOPOLOGY_AND_ALL_WIDTH_REDUCTION_20260807.md`:
after restoring every rail, the complete changed destination colour paths,
with their order and external half-edges, are the context-labelled copies
of the complete changed base paths.  Then every old internal linear upper
value survives after transport through any number of low renewals.

### Proof

Under the ordered all-q chronology hypothesis, the cited theorem gives the
all-width endpoint-coboundary identity for complete ordered paths, not
merely for their incidence chains.  It transports the complete base current
by the context injection.  Context union is injective on the base values,
and Theorem 6.1 has no base support casualty.  Induct over renewal modules.
`square`

This statement is conditional because Boolean incidence context transport
alone proves only the incidence identity and its turn-faithful q2 image;
it does not determine q3+ path-window order.  It also deliberately excludes
a source interval entering an arbitrary exterior body or crossing the fixed
lifted closure.  Those are not linear windows wholly internal to the
transported module.

## 7. Residence and exterior all-width scope

The mixed native packet and the prepared prism both alter owner
incidences, so they evade any obstruction applying only to same-owner
common-history splicing.  This is exactly why they remain relevant after
the absolute common-history hole for

\[
                         T_2(10)^{m-6}              \tag{7.1}
\]

is imposed.  That suffix family is already repaired by the owner-changing
two-`C6` tensor relay.

However, q2 closure does not imply a resident all-width collar.

* The doubled-history GK `C10` theorem uses pointwise screen identities
  `X_(i-1) union Y_i=X_i union Y_i` and
  `X_i intersection Y_(i+1)=X_i intersection Y_i`.
  The `C8` in Section 2 has a nonzero eight-term q2 current and does not
  satisfy those identities in that direct form.
* Adding a common history embeds every distinct base turn injectively.  It
  cannot by itself replace a lost base value.  The three singleton losses
  in Section 2 must still be supplied by the four closing `C6`s or by named
  exterior providers.
* For a prepared annulus satisfying the separate ordered all-q chronology
  hypothesis, the exact all-width law is

  \[
   \partial_q A_{S,S'}(Z_0)
     =\iota_{S'}\delta_q^{Z_0}-\iota_S\delta_q^{Z_0}. \tag{7.2}
  \]

  Hence the annulus transports the base wider-deck current; it does not
  make it vanish.  All-width support monotonicity reduces to a finite base
  audit plus literal backup providers for every base negative.

Accordingly, a resident all-width version of Theorem 5.1 additionally
requires:

1. a closed common-history collar on every boundary and transport rail,
   giving the requested positive/negative run lengths;
2. protected witnesses for every interval crossing the module/exterior or
   lifted-closure boundary; and
3. a proof that recursive collar copies remain occurrence-disjoint and
   retain their ordered socket signature.

Theorem 6.1 closes the formerly missing finite **internal linear** base
audit.  It does not close any of these three exterior/residence rows.

No theorem currently shows that the native `C8+4C6` packet admits such a
collar.  Nor is there a proved obstruction to a different collared
realization.  The exact remaining statement is therefore the finite
`PP_1100` module with these three resident/all-width rows, not another
finite census of `T_a` packets.

## 8. Reproducibility and exact scope

The H100 scripts are

```text
scratch/search_msw_q2_counter_carry.cpp
scratch/search_msw_target_local_cycles.cpp
scratch/audit_msw_t0_relay_linear_allwidth.py
```

The first enumerates the complete native factor, endpoint-inclusive `C6`
and target-directed `C8` trades, and checks exact loads and owner
disjointness.  The second uses only the exact touching-step rule to search
target-local alternating cycles without materializing the Catalan factor.

Proved here:

* the explicit literal `T_5` creator and its complete q2 ledger;
* the exact mixed closed repair at `T_5`;
* the failure of a fixed-prefix `C8` tensor recurrence;
* occurrence-level non-equivalence with the prepared prism; and
* the precise finite recursive module sufficient for all renewals; and
* complete internal linear all-width support monotonicity of the base
  two-hex relay.

Not proved here:

* existence of `PP_1100` or its high-renewal mirror in one global factor;
* simultaneous recursive planting across all chamber fibres;
* a resident collar for the mixed packet;
* support protection for intervals crossing a module/exterior or fixed
  lifted-closure boundary; or
* compatibility with the final lower compiler and linear opening.

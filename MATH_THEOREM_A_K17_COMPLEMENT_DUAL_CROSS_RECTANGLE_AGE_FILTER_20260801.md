# K17 complement-dual cross rectangles: exact palette, age, and residence filter

Date: 2026-08-01  
Lane: A  
Status: proved local theorem and proof-safe search specification.  No
rectangle existence claim is made.

## 1. Scope and outcome

Let `D,H` be perfect incidence matchings between the 1,430 quotient
rank-nine owners and rank-eight facets, and assume

\[
                 H=CD^{-1}C .                                      \tag{1.1}
\]

The selected factor `D union H` is assumed to have exactly two quotient
components and to cover every rank-seven and rank-ten immediate colour.
This is the interface supplied by the authenticated factor

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/best.tsv.
```

The copy inspected for this theorem has SHA-256
`a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3`.

This note proves the exact test for the smallest possible non-dual
component join.  It separates four logically different rows:

1. the incidence rectangle and quotient topology;
2. the two immediate-palette accounts;
3. fixed occurrence-age compatibility; and
4. physical residence in the 17-fold lift.

In particular, a quotient rectangle changes two successor **orbits**, but
it changes 34 physical seams.  A two-seam run calculation on quotient
representatives is not a sound residence audit.

## 2. The minimal cross rectangle

Choose one old `H` edge from each quotient component,

\[
                  e_i=p_iF_i \qquad (i=0,1).                       \tag{2.1}
\]

Let `r_i=D^{-1}(F_i)`.  Thus the two old oriented owner-successor darts
(following `D` and then `H^{-1}`) are

\[
                         r_i\longrightarrow p_i.                  \tag{2.2}
\]

Assume that the crossed physical incidence orbits

\[
                  e'_0=p_0F_1,\qquad e'_1=p_1F_0                 \tag{2.3}

\]

exist, are distinct, and neither belongs to `D`.  Replace (2.1) by (2.3).
Then the new successor darts are

\[
                         r_0\longrightarrow p_1,qquad
                         r_1\longrightarrow p_0.                  \tag{2.4}
\]

### Theorem 2.1 (minimal topology and voltage test)

The exchange (2.1)--(2.3) preserves every incidence degree and joins the
two quotient components into one.  No one-edge modification can preserve
all degrees, so this support-two `H` exchange, equivalently an alternating
incidence rectangle, is minimal.

Let `V_0,V_1` be the old component voltages.  Write `s(e)` for the
canonical physical incidence shift of an edge orbit.  The joined quotient
cycle has voltage

\[
 V'=V_0+V_1+s(e_0)+s(e_1)-s(e'_0)-s(e'_1)\pmod {17}.              \tag{2.5}
\]

Its physical lift is one cycle if and only if `V'` is nonzero.

#### Proof

Deleting one matching edge from each alternating component leaves two
alternating paths.  The crossed reconnection is the unique nontrivial
degree-preserving pairing of their four exposed endpoints and joins the
paths.  Voltage is additive around the two old cycles; removing the old
`H` shifts and inserting the crossed `H` shifts gives (2.5).  A quotient
cycle in a prime cyclic cover lifts to `gcd(17,V')` cycles.  A single edge
change leaves one owner and one facet with wrong degree, proving
minimality.  \(\square\)

### Corollary 2.2 (authenticated fixed-`D` rectangle no-go)

For the authenticated `best.tsv` factor, the two quotient components have
lengths `1429,1` and voltages `4,9`.  The exact fixed-`D` catalogue checks
all

\[
                  1429\cdot1=1429                                \tag{2.6}
\]

choices of one old `H` edge from each component and finds

\[
  \#\{\hbox{geometric crossed-incidence pairs}\}=0.              \tag{2.7}
\]

Hence this fixed factor has no support-two non-dual `H` rectangle at all;
the palette, voltage, and age filters are vacuous on that shell.  The
parity theorem in Section 6 further shows that a `C6` cannot join the
`1429+1` components.  Thus a pure-`H` connector must use at least four old
edges (a `C8`), or it must change `D` as well.

This is certified by

```text
scratch/threadA_k17_complement_dual_age_local_replay_20260801/
  twofactor_splice_catalogue.audit.json
```

with SHA-256
`17f1852bedb86abc176a4013d2c5823e97c120a5019e064ff0e2fda582ee7815`.
Its scope is the fixed `D` and literal two-edge `H` endpoint swaps; it does
not exclude a `D`-switch, `C6`, or mixed circuit.

## 3. The exact four-ticket palette ledger

All labels below are evaluated in the physical gauges specified by their
incidences.  At the two facets put

\[
\begin{array}{lll}
 U_0=r_0\cup p_0, &\quad& U'_0=r_0\cup p_1,\\
 U_1=r_1\cup p_1, && U'_1=r_1\cup p_0,
\end{array}                                                       \tag{3.1}

\]

and at the two `H`-owners put

\[
\begin{array}{lll}
 L_0=D(p_0)\cap F_0, && L'_0=D(p_0)\cap F_1,\\
 L_1=D(p_1)\cap F_1, && L'_1=D(p_1)\cap F_0.
\end{array}                                                       \tag{3.2}

\]

These are respectively the only changed rank-ten and rank-seven turn
occurrences.

Let `mu(T)` be the old rank-ten load.  Old complement duality gives the
same load for the complementary rank-seven target.  Define, on the common
rank-ten target set,

\[
\begin{aligned}
 d^U_T&=\#\{i:U_i=T\},       &a^U_T&=\#\{i:U'_i=T\},\\
 d^L_T&=\#\{i:C(L_i)=T\},   &a^L_T&=\#\{i:C(L'_i)=T\}.
\end{aligned}                                                       \tag{3.3}

\]

### Theorem 3.1 (two-account four-ticket criterion)

Both immediate palettes survive the rectangle if and only if, for every
rank-ten target orbit `T`,

\[
                 \mu(T)-d^U_T+a^U_T\ge1,qquad
                 \mu(T)-d^L_T+a^L_T\ge1.                         \tag{3.4}

\]

The four deleted tickets are `U_0,U_1,C(L_0),C(L_1)`, but the upper and
lower copies are separate accounts.  It is generally incorrect to sum
their deletions into one inequality.  The gain-blind sufficient screen is

\[
                 d^U_T\le\mu(T)-1,qquad
                 d^L_T\le\mu(T)-1                                \tag{3.5}

\]

for every `T`.  The exact test (3.4) is strictly stronger because it may
delete a unique occurrence when a crossed edge recreates its target.

#### Proof

At every other facet the two incident selected edges are unchanged, and
at every other owner they are unchanged.  Hence (3.1) and (3.2) are the
complete changed-occurrence lists.  Subtracting old and adding new
multiplicities proves (3.4).  Complementation only identifies the two old
load vectors; after the non-dual exchange it does not identify their
deltas.  This proves the two-account warning and (3.5).  \(\square\)

## 4. Exact fixed-state age compatibility

An occurrence-age state at owner `x` is

\[
             S_x=(T_x;C_{x,0},C_{x,1},C_{x,2},C_{x,3}),
             \qquad C_{x,3}=\{\alpha_x\}.                         \tag{4.1}

\]

For Johnson-adjacent physical owners `x,y`, define `R(S_x,S_y)=1` when,
with `T_y-T_x={beta}`, one has

\[
\begin{aligned}
 T_x-T_y&=C_{x,3},\\
 C_{y,j+1}&\subseteq C_{x,j}\quad(0\le j\le2),\\
 C_{y,0}&=\{\beta\}\mathbin{\dot\cup}
          \bigcup_{j=0}^2(C_{x,j}-C_{y,j+1}).                     \tag{4.2}
\end{aligned}

\]

This is the literal survivor/refresh relation, not merely a run-length
test.

### Theorem 4.1 (two-arc locality)

Fix a cyclic-equivariant occurrence-age state at every quotient owner.
Under the rectangle, every old
age transition except (2.2) remains unchanged.  Therefore the new joined
factor is literal-age compatible with these same states if and only if

\[
                         R(S_{r_0},S_{p_1})=1,qquad
                         R(S_{r_1},S_{p_0})=1.                    \tag{4.3}

\]

More generally the exact change in the number of compatible quotient
transition orbits is

\[
 \Delta_{\rm age}=
 R(S_{r_0},S_{p_1})+R(S_{r_1},S_{p_0})
 -R(S_{r_0},S_{p_0})-R(S_{r_1},S_{p_1}).                         \tag{4.4}

\]

Thus a support-two rectangle repairs at most two fixed-state age defects.
It improves the fixed-state score exactly when (4.4) is positive.  If all
old transitions were compatible, (4.3) is both necessary and sufficient
for zero-loss joining.

#### Proof

The matching exchange changes `H^{-1}D` only at facets `F_0,F_1`, giving
exactly (2.2) and (2.4).  Relation (4.2) is the necessary-and-sufficient
literal update on one arc.  Rotation commutes with (4.2), so checking each
of the two quotient arcs checks all 17 physical copies.  Summing their two
indicator changes gives (4.4).  \(\square\)

For a non-equivariant physical state bank, (4.3) must instead be imposed
on all 34 crossed physical arc copies; the quotient shortcut is then
invalid.

This theorem is deliberately fixed-state.  Allowing nearby states to be
redecorated is a different finite collar problem and may propagate beyond
the two changed arcs; it must not be credited to (4.4).

## 5. Exact phase-expanded residence filter

The physical residence row can be tested without replaying unaffected
interiors, but it cannot be tested on only two quotient seams.

For old component `i`, let

\[
                   v_i=s(D(r_i))-s(e_i)                            \tag{5.1}

\]

be the old successor-dart voltage, and let

\[
                   v'_i=s(D(r_i))-s(e'_{1-i})                     \tag{5.2}

\]

be its crossed successor-dart voltage at facet `F_i`.  For each phase
`g in Z_17`, delete the physical copy of `r_i->p_i` and let `P_(i,g)` be
the resulting directed path segment beginning at `rho^g p_i` and ending
immediately before the next copy of that cut.  Its final owner has phase

\[
                         g+V_i-v_i.                               \tag{5.3}

\]

The old closing seam sends it to `P_(i,g+V_i)`.  The crossed seam sends it
to

\[
               P_(1-i,\,g+V_i-v_i+v'_i).                         \tag{5.4}

\]

For a binary word `w` and threshold `h=4`, let `Sigma_h(w)` be its
**truncated boundary-run summary**:

* its first and last bits;
* its initial and final run lengths, truncated at `h`;
* whether the whole word is constant; and
* the number of its internal signed runs of length below `h`.

These summaries form an associative concatenation monoid: `Sigma_h(uv)`
is determined by `Sigma_h(u),Sigma_h(v)`.  Equal touching bits merge their
boundary lengths; unequal bits close both boundary runs.  The constant-word
flag records when a boundary propagates through the whole factor.  Thus a
cyclic concatenation's exact short-run count is determined by the summaries.

For a permutation `pi` of the 34 path pieces and a coordinate `z`, let
`kappa_z(pi)` be the number of signed runs of length below four in the
cyclic words obtained by concatenating the `z`-traces around every cycle
of `pi`.  Define

\[
\begin{aligned}
 \pi_{\rm old}(i,g)&=(i,g+V_i),\\
 \pi_{\rm new}(i,g)&=(1-i,g+V_i-v_i+v'_i).                         \tag{5.5}
\end{aligned}

\]

If no path piece is constant in coordinate `z`, this has the simpler
pairwise form.  Let `pre_(i,g)(z)` and `suf_(i,g)(z)` be the initial and
final constant-run lengths and, for two pieces `P,Q`, put

\[
 \Phi_z(P,Q)=
 \begin{cases}
  1_{\,\mathrm{suf}_P(z)+\mathrm{pre}_Q(z)<4},
      &\text{if their endpoint bits agree},\\
  1_{\,\mathrm{suf}_P(z)<4}+1_{\,\mathrm{pre}_Q(z)<4},
      &\text{if their endpoint bits differ}.
 \end{cases}                                                       \tag{5.6}

\]

### Theorem 5.1 (boundary-coboundary identity)

Let `B_old` and `B_new` be the numbers of signed runs of length below four
before and after the rectangle.  Then

\[
 B_{\rm new}-B_{\rm old}
       =\sum_z\big(\kappa_z(\pi_{\rm new})
                         -\kappa_z(\pi_{\rm old})\big).           \tag{5.7}
\]

If no `P_(i,g)` is constant in coordinate `z`, its summand in (5.7)
equals

\[
\sum_{g\in\mathbb Z_{17}}\sum_{i=0}^1
 \left[\Phi_z(P_{i,g},P_{1-i,g+V_i-v_i+v'_i})
       -\Phi_z(P_{i,g},P_{i,g+V_i})\right].                       \tag{5.8}
\]

Restricting the summary charge to bit-one runs gives the identical formula
for the positive-residence short-run count.  Vanishing of that count is
equivalent to validity of the four-deletion spine; equality of the two
different *numbers of violations* is not asserted.

Consequently:

* the rectangle improves residence exactly when the right side of (5.7)
  is negative;
* if every old cut-pair boundary score is zero, the rectangle cannot
  improve the score and is residence-preserving exactly when every new
  boundary score is zero; and
* a strictly improving rectangle must cut the boundary collar of at least
  one old short run.  Any bad run lying in an unaffected path interior is
  immutable under this rectangle.

#### Proof

Deleting all 17 physical copies of each of the two selected edge orbits
cuts the old lift into the 34 path pieces `P_(i,g)`.  Every run internal to
one piece is unchanged.  Equation (5.3) follows by traversing one quotient
component, which adds `V_i`, after removing the old dart voltage `v_i`.
Adding the new dart voltage `v'_i` gives (5.4).  The old and new factors
use the same 34 path words and differ only by the permutations (5.5).
The truncated-summary monoid computes the exact cyclic short-run count of
either permutation, proving (5.7), including constant path pieces.  When
no piece is constant, every boundary run touches one seam, and the direct
equal-bit/unequal-bit calculation gives (5.8).  Restricting to bit one
proves the positive-only statement.  \(\square\)

The 17-phase expansion is essential.  The two quotient edge orbits have
34 physical copies, and their phase pairing changes with `V_i-v_i+v'_i`.

## 6. Proof-safe catalogue and the first larger shell

A complete support-two age-local catalogue needs only the following rows
for each geometric cross rectangle:

1. incidence existence, `H`-matching degrees, and disjointness from `D`;
2. different old quotient components;
3. nonzero voltage (2.5);
4. the two palette accounts (3.4);
5. either the two fixed-state tests (4.3), or the exact score (4.4); and
6. the phase-expanded residence delta (5.7).

The existing remote source

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/
  twofactor_splice_catalogue_20260801/
  catalogue_k17_complement_dual_twofactor_splices_20260801.cpp
```

already implements rows 1--4 and a full joined-factor run replay.  Its
inspected SHA-256 is
`00af1d3ac01f43034286cd63af0490fb0d939ff95ff37b5daced3142c8fa18e9`.
Its
declared scope correctly says that residence is diagnostic and it contains
no occurrence-age state input.  Therefore it must not be cited as an audit
of (4.3).  Adding (4.3) as a filter is disjoint from rerunning or replacing
that whole-splice enumeration.

For a general alternating `H` circuit, choose `t` old edges `p_iF_i` and
cyclically rematch their owner endpoints.  The exact generalization of the
local ledgers is obtained by:

* replacing the two old/new labels in (3.3) by `t`;
* replacing (4.4) by the sum over the `t` changed successor arcs; and
* replacing the cross pairing in (5.7) by the induced permutation of the
  `17t` phase-expanded path pieces.

### Theorem 6.1 (`C6` parity obstruction and first connector shell)

On the authenticated component profile `[1429,1]`, a single alternating
`H` circuit on `t` selected old edges can join the components only if `t`
is even.  Consequently a `C6` (`t=3`) cannot connect them.  Since the
`C4` shell is empty by Corollary 2.2, the first topology-capable pure-`H`
shell is `C8` (`t=4`).

#### Proof

Any circuit meeting both components selects the unique loop edge and
`t-1` edges of the long cycle.  Cutting them gives `t` path fragments.  In
the old factor their head-to-next-head fragment permutation `kappa` has
cycle type `(1)(t-1)`, hence sign `(-1)^(t-2)`.  The new cyclic endpoint
rematching is a `t`-cycle `tau`, of sign `(-1)^(t-1)`.  The new component
permutation is `tau kappa` (up to reversing the composition convention),
so its sign is `-1`.  If it were one `t`-cycle its sign would be
`(-1)^(t-1)`, forcing `t` even.  Thus `t=3` is impossible and, after the
empty `t=2` shell, `t=4` is first.  \(\square\)

A `C6` may still change the residence score while leaving two components;
it is not a connector.  The `C8` catalogue remains local and
occurrence-labelled, and is distinct from K's unrestricted whole-splice
enumerator.

There is already a useful state-free calibration on the `D`-switch side.
The independently replayed three-owner switch

```text
75: 681 -> 678,   265: 2385 -> 2391,   219: 1975 -> 1971
```

preserves both complete immediate palettes and the component profile, while
reducing positive short runs from `4318` to `4301`, positive residence
deficit from `5508` to `5457`, and four-deletion-spine bad positions from
`5474` to `5440`.  The audit is

```text
scratch/threadA_k17_complement_dual_age_local_replay_20260801/
  switch75_265_219.audit.json
```

with SHA-256
`cbd5f32a6ba5293a90da516c57b77ffb7f0a629cfcab49256adf39a04404f525`.
This proves that local complement-dual switching can improve raw residence.
It does **not** prove fixed-state literal-age compatibility, signed
residence, or minimality of support three.

## 7. Precise remaining boundary

This note proves a necessary-and-sufficient connector test for a fixed
rectangle and fixed occurrence-age states, and an exact state-free
residence-delta identity.  It does **not** prove that the authenticated
factor has a passing rectangle, that a local state redecorating exists,
or that ranks eleven and above and the common compiler survive.  A negative
census using rows 1--6 would close only support-two non-dual rectangles on
this fixed factor; it would not exclude a complement-dual `D` switch, a
nonconnecting `C6` residence move, a `C8` connector, or an unrestricted
carrier.

The current `best.tsv` header is exactly

```text
owner  pick_edge  dual_edge  facet
```

and contains no `C_0,C_1,C_2,C_3` occurrence states.  Therefore (4.3)
cannot be instantiated from that file alone.  This is an input boundary,
not an obstruction to the factor: the state-free residence filter (5.7)
is evaluable from the factor geometry, while literal-age improvement needs
either a certified state bank or a separately solved local redecorating
collar.

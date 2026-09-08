# Necklace selector audit and exact rolling-reset coexistence at `k=17`

Date: 2026-08-01

Status: proof-safe audit, a general orbit-balanced substitution lemma, an
exact quotient-matching criterion at depth three, and an authenticated
`k=17` coexistence certificate.  The certificate gives an exact high-target
selector with uniform rails containing 17 disjoint translates of the
two-queue reset ring.  It does **not** complete the residual statewise Hall,
owner-rainbow, connectedness, upper-deck, or lower-compiler rows.

## 0. Outcome

The necklace-SCD selector is sound at its stated static scope.

* Coherent representatives really can be lifted down a quotient chain.
* Middle roots and rank-`m+1` owners have free rotation action when the
  ground size is `2m+1`.
* A lower target with stabilizer `h` is offered exactly `h` times at the
  relevant depth, so marking one occurrence is exact.
* At depth three, a rainbow perfect matching in one state graph is exactly
  equivalent to a **rotation-equivariant** owner-exact cycle cover.  It is
  not an equivalence for arbitrary non-equivariant covers.
* The old direct-necklace obstruction is respected: the new state edges
  join different root necklaces; it never asks a generic root to be
  Johnson-adjacent to a nontrivial translate of itself.

The rolling reset can coexist with all static selector rows.  For `k=17`,
one explicit eight-root reset template has distinct root, two lower-suffix,
and upper-owner necklace orbits.  Its forced quotient edges extend to both
required containment matchings.  Lifting gives:

\[
 \boxed{\text{exact ranks 7 and 6 marking}
       +\text{exact depth-3 rail balance}
       +17\text{ protected reset }8\text{-cycles}.}
\]

Thus the reset does not conflict with necklace target selection or rail
balance.  The surviving obstruction is the correlated legal-turn/owner
completion outside the protected bank.

## 1. Audit of the necklace selector

Let `p=2m+1`, let `tau` rotate `Z_p`, and put

\[
                       W=\binom p m.
\]

### Lemma 1.1 (coherent representative lift)

Let

\[
 [S_a]<[S_{a+1}]<\cdots<[S_m]
\]

be a saturated chain in the quotient Boolean poset, and fix an arbitrary
representative `Q_m` of `[S_m]`.  There are representatives

\[
                 Q_a\subset Q_{a+1}\subset\cdots\subset Q_m.
\]

Indeed, if `[S_(i-1)]<[S_i]`, choose one literal incidence `A subset B` in
those two orbits.  Rotate the pair so that `B` is the already chosen `Q_i`.
The rotated `A` is the required `Q_(i-1)`.  Iteration is legitimate because
only the current upper representative is frozen.

### Lemma 1.2 (middle and owner freeness)

Rotation is free on ranks `m` and `m+1`.

If a subgroup of order `h>1` fixes a set of rank `s`, then `h` divides both
`s` and `p`.  But

\[
             \gcd(m,2m+1)=\gcd(m+1,2m+1)=1.
\]

Hence every root and owner necklace has size `p`, and each shore has
`W/p` necklaces.

### Lemma 1.3 (exact stabilizer marking)

Suppose a quotient chain contains a lower target orbit `[S]`, and let

\[
                   h=|\operatorname {Stab}(S)|.
\]

The `p` translates of one coherent flag visit every named member of `[S]`
exactly `h` times.  Mark one of those `h` occurrences for each named target
and leave the rest unmarked.  This gives literal load one at every target.

The marking need not be equivariant.  That does not change the flag table
or its rail inventory.  It does mean that any later compiler theorem which
needs equivariant **marked occurrences** requires an additional choice;
the selector theorem itself makes no such claim.

### Proposition 1.4 (precise depth-three quotient equivalence)

For a fixed equivariant depth-three flag table, let `G_0` join flags with
outgoing state zero to flags with incoming state zero, and colour a legal
turn by its rank-`m+1` owner necklace.  Then

\[
 \begin{split}
 &G_0\text{ has a perfect matching with all }W/p
   \text{ colours distinct}\\
 &\quad\Longleftrightarrow\quad
 \text{the table has a rotation-equivariant owner-exact cycle cover}.
 \end{split}                                                   \tag{1.1}
\]

One implication translates the matching through all `p` rotations.  A
chosen edge has free owner orbit, so its translates use every physical owner
in that orbit exactly once.  Distinct quotient colours therefore give every
owner once.  Conversely, quotient a rotation-invariant owner-exact cover.

The word *rotation-equivariant* is essential in the converse.  Equation
(1.1) is a complete reduction inside the equivariant class, not a claim
that every possible owner-exact cover is equivariant.

### Proposition 1.5 (compatibility with the old direct-lift obstruction)

The direct necklace audit forbids, for almost every root `Q`, a Johnson edge
from `Q` to `tau^t Q`, `t != 0`.  In (1.1), a state edge is allowed to join
two different root necklaces.  Translating it produces parallel edges
between those two orbits.  No within-necklace Johnson edge is asserted.
Thus the two statements are logically disjoint and consistent.

## 2. Whole-orbit substitutions preserve positional flux

### Theorem 2.1 (orbit-balanced flag substitution)

Fix a free rank-`m` root necklace `[Q]`.  Choose any literal deletion flag

\[
                   f=(Q;z_1,\ldots,z_{d-1})
\]

and place all `p` translates of `f` on the roots in `[Q]`.  For every
position `j` and coordinate `x`, this one flag orbit contributes exactly
one occurrence to

\[
                   H_j(x)=|\{f:z_j(f)=x\}|.          \tag{2.1}
\]

Therefore replacing the flags on any collection of complete root necklaces
by arbitrary equivariant flag orbits leaves every positional histogram
`H_j` unchanged.

#### Proof

For fixed `j`, the labels `tau^t z_j`, `0<=t<p`, visit every coordinate
once.  This is independent of the root and of every other deletion
position.  Sum over the replaced root orbits. \(\square\)

At `d=3`, positional equality `H_1=H_2` is the complete rail-balance
equation.  Hence **every whole-root-orbit substitution is rail-neutral**.
For `d>3`, this proves only one-coordinate flux; complete ordered rail-word
balance still needs a separate orbit inventory.

The two-queue reset bank is especially well behaved: its own prefix and
suffix rail-word multisets agree at every depth because its protected turns
already form cycles.  The only possible higher-depth damage comes from the
flag orbits removed to make room for it.

## 3. Exact quotient criterion for a protected depth-three bank

Assume now that rotation is free on ranks `m-2,m-1,m`; in particular this
holds for prime `p`.  Let `N_s` be the set of rank-`s` necklaces and let
`Q_(s,s+1)` be the simple quotient containment graph: `[A]` is adjacent to
`[B]` when some representatives satisfy `A subset B`.

Suppose a protected bank prescribes vertex-disjoint quotient chains

\[
                     [B_i]<[A_i]<[T_i],             \tag{3.1}
\]

at ranks `m-2,m-1,m`.  Write `E_67` and `E_78` for the prescribed edge
sets in the two quotient graphs.

### Theorem 3.1 (quotient chain-extension criterion)

There is a rotation-equivariant exact marked depth-three selector containing
all chains (3.1) if and only if:

1. `E_67` and `E_78` are matchings; and
2. after deleting their endpoints, `Q_(m-2,m-1)` has a matching saturating
   every remaining rank-`m-2` necklace and `Q_(m-1,m)` has a matching
   saturating every remaining rank-`m-1` necklace.

#### Proof

Necessity is ordinary matching necessity.

For sufficiency, add the residual matchings to the prescribed edges.  Every
rank-`m-1` necklace now has one upper root necklace, and every rank-`m-2`
necklace has one upper rank-`m-1` necklace.  Starting at each selected root
representative, align representatives successively downward as in Lemma
1.1.  If a root chain has no marked rank-`m-2` child, complete its deletion
word arbitrarily and leave that suffix unmarked.  Do the same at root
necklaces unused by the rank-`m-1` matching.

Lift every resulting flag through all rotations.  Freeness makes every
selected quotient incidence orbit a literal perfect matching between its
two physical necklaces.  Hence every named target at ranks `m-1` and
`m-2` is marked exactly once, and every named root is used once.  Theorem
2.1 gives exact rail balance. \(\square\)

Equivalently, the two residual Hall systems are the exact and only static
coexistence obstruction.

## 4. The explicit `k=17` reset bank

Put `p=17`, `m=8`, `d=3`.  Let

\[
 K=\{0,1,2,3\},\qquad
 (X_0,\ldots,X_7)=(4,5,6,7,8,9,10,11),             \tag{4.1}
\]

with the `X` indices read modulo eight.  Define

\[
\begin{aligned}
 T_a&=K\cup\{X_a,X_{a+1},X_{a+2},X_{a+3}\},\\
 A_a&=K\cup\{X_{a+1},X_{a+2},X_{a+3}\},\\
 B_a&=K\cup\{X_{a+2},X_{a+3}\},\\
 U_a&=K\cup\{X_a,X_{a+1},X_{a+2},X_{a+3},X_{a+4}\}.
                                                               \tag{4.2}
\end{aligned}
\]

The flag at `T_a` is

\[
                         (T_a;X_a,X_{a+1}).          \tag{4.3}
\]

It has suffixes `A_a,B_a`, and its protected successor is the flag at
`T_(a+1)`.  The immediate upper owner of this turn is `U_a`.

### Theorem 4.1 (exact `k=17` static coexistence)

There is a rotation-equivariant exact depth-three marked selector on all
rank-eight roots which contains every translate of (4.3) and all protected
turns

\[
                         T_a\longrightarrow T_{a+1}. \tag{4.4}
\]

It has the following exact properties.

1. Every rank-seven and rank-six target is marked exactly once.
2. `H_1(x)=H_2(x)=1430` for every coordinate `x`.
3. The protected bank consists of 17 vertex-disjoint eight-cycles, hence
   136 distinct root flags.
4. Its 136 immediate lower colours and 136 immediate upper owners are all
   distinct.
5. Every private reset coordinate has protected owner-run length four,
   exactly the `d+1` residence threshold.

#### Proof

The necklace orbits `[B_a]`, `[A_a]`, `[T_a]`, and `[U_a]` are separately
distinct for `0<=a<8`; the literal orbit unions therefore have size 136 in
each family.  Thus the prescribed edges `B_a A_a` and `A_a T_a` are
matchings in the two quotient containment graphs.

The quotient layer sizes are

\[
 |N_6|=728,\qquad |N_7|=1144,\qquad |N_8|=1430.     \tag{4.5}
\]

After deleting the eight prescribed edges and their endpoints, exact
Hopcroft--Karp replay gives matchings of sizes

\[
             720=728-8,qquad 1136=1144-8.           \tag{4.6}
\]

Theorem 3.1 supplies the exact selector and Theorem 2.1 supplies its rail
balance.  Equations (4.2)--(4.4) are the two-queue rolling reset with
`d+1=4`; its direct identities give the remaining protected-bank claims.
\(\square\)

This is a finite exact theorem authenticated by a complete quotient replay,
not a randomized search claim.

## 5. The chronology row remains correlated

The quotient containment matchings in Theorem 4.1 were chosen independently
of the legal-turn state graphs.  To measure the scope, the audit reconstructs
one coherent literal flag representative from those matchings, uses the
first available phase for every unforced incidence, fixes either the opened
seven-turn reset path or the closed eight-turn reset cycle in `G_0`, and
computes the maximum residual state matching.  It finds

\[
                 850/1423\quad\text{(opened)},
                 \qquad849/1422\quad\text{(closed)},
                 \qquad406\quad\text{zero-out tails}.          \tag{5.1}
\]

This is **not** a no-go for another correlated quotient completion.  It is
an exact counterexample to the shortcut

\[
 \text{two quotient containment matchings + rail balance}
 \Longrightarrow \text{statewise Hall}.                       \tag{5.2}
\]

The surviving construction theorem must choose the two containment
matchings, their physical phases, and the residual rainbow state matching
jointly.  The protected reset bank itself is no longer an obstruction to
that theorem.

## 6. Audit artifacts

The standalone C++20 replay is

`scratch/audit_k17_necklace_selector_reset_bank_20260801.cpp`.

It was compiled with `-O3` and run on the H100 CPU.  The frozen output is

`scratch/audit_k17_necklace_selector_reset_bank_20260801.txt`.

It independently enumerates all rank-six, rank-seven, and rank-eight
necklaces, constructs both quotient containment graphs, forces the reset
bank, runs both residual matchings, replays all 136 literal orbit resources,
and audits one residual statewise completion.

The SHA-256 hashes are

* source: `7b974c89c0c87a3e34182080c02c2c7aae66b8b5318bda3d30fed0188b35ad24`;
* output: `012f211a76ebeacacca19089a8d8e5d4c03754b51f7818e5c04beebe2b2c2ab8`.

## 7. Exact frontier

| row | status |
|---|---|
| coherent quotient-chain representatives | proved |
| stabilizer-aware exact target marking | proved |
| whole-orbit positional flux preservation | proved |
| complete depth-three rail balance | proved |
| `k=17` exact target selector with reset bank | proved/audited |
| protected reset root/lower/upper resources | proved/audited |
| residual statewise Hall with the bank fixed | open |
| quotient owner-rainbow matching | open |
| one component/nonzero voltage | open |
| arbitrary-width upper deck and compiler | open |

The correct next finite object is therefore one correlated quotient
three-resource matching conditioned on the opened seven-edge reset path.
There is no remaining rail-balance or high-target incompatibility caused by
the rolling reset.

# The all-width `C8` host has an internal residence obstruction, and the joint interface has one exact replacement criterion

**Date:** 2026-08-13  
**Method:** literal run census, variable-aperture counting, socket-permutation
calculus, protected-Ore localization, and a typed gammoid cut  
**Status:** unconditional obstruction and conditional coinstantiation
theorem.  The proved all-width phased collar cannot itself be depth-`d`
resident for any `d>=2`.  A redesigned resident collar with subexponential
size and sublinear exposure would automatically retain a spanning phased
host; its inherited socket labels and private common-cap bank are governed
by the exact finite conditions below.

## 1. The protected two-slot rail

Use the all-width collar and its closed spanning host from

* `MATH_THEOREM_COMMON_MATE_C8_ONE_STEP_COLLAR_Q2_Q3_ZERO_ODD_SOCKET_20260812.md`; and
* `MATH_THEOREM_COMMON_MATE_C8_ALLWIDTH_COLLAR_SPANNING_PHASED_HOST_20260812.md`.

On path `i`, the neutral owners are

\[
 W_{i,j}=C\cup\{q_{i+1},z_{j-1},z_j\},
 \qquad 1\le j\le H,                               \tag{1.1}
\]

where `z_0=c` and, in the all-width construction, `H=m-3`.  The owner
immediately before `W_(i,1)` is

\[
 U_i=C\cup\{c,q_i,q_{i+1}\},                       \tag{1.2}
\]

and the owner after `W_(i,2)` is `W_(i,3)`.

Recall that depth-`d` factor residence requires every maximal internal
positive coordinate run to have at least `d+1` consecutive owners.

### Theorem 1.1 (immutable run-two obstruction)

Assume `H>=3`.  On every one of the four old paths, the coordinate `z_1`
has the maximal positive run

\[
                         W_{i,1},W_{i,2},            \tag{1.3}
\]

of length exactly two.  This run remains maximal after the two-transition
closure, after any spanning-factor completion containing the protected
bank, and after the odd `C8` switch.

Consequently neither the open all-width collar nor its proved spanning
phased host is depth-`d` resident for any `d>=2`.

#### Proof

The owners `W_(i,1)` and `W_(i,2)` both contain `z_1`.  Equation (1.2)
does not, and

\[
 W_{i,3}=C\cup\{q_{i+1},z_2,z_3\}                  \tag{1.4}
\]

does not.  Thus (1.3) is a maximal run already in the interior of the open
path.  If a later bridge uses `d_i=z_1`, that produces a second run after a
nonempty gap and cannot merge with (1.3).

The closure and every containing factor retain both protected adjacencies
around (1.3); in the closed host all of these vertices are saturated.
Exterior terminal paths and private prefixes can change only the endpoint
environment, not the two bracketing owners.  Finally the `C8` switch merely
transports complete output rail `i` to incoming socket `i-1`; it does not
change the internal order (1.1).  Hence the length-two run persists in both
phases.  For `d>=2`, residence requires length at least three, giving the
contradiction. `square`

This is stronger than failure of one chosen factor completion.  It is a
literal obstruction inside the protected bank itself.  No Ore--Ryser,
terminal, or common-cap choice can repair it.

## 2. The aperture lower bound behind the obstruction

The short run is not an accident of `z_1`; it is forced by the two-slot
architecture.

### Lemma 2.1 (variable-aperture residence bound)

Let

\[
                         V_0,V_1,\ldots,V_{L-1}     \tag{2.1}
\]

be a cyclic rank-`m` Johnson walk.  Suppose a fixed set `F` is contained in
every owner and every transition exchanges labels outside `F`.  Put

\[
                         a=m-|F|.                   \tag{2.2}
\]

Then some positive run of a coordinate outside `F` has length at most `a`.
In particular, depth-`d` residence forces

\[
                         \boxed{a\ge d+1.}          \tag{2.3}
\]

#### Proof

Every Johnson transition inserts exactly one coordinate outside `F`, and
therefore starts exactly one nonconstant cyclic positive run.  There are
`L` such run starts, counted with multiplicity over coordinates.  On the
other hand, the sum of the nonconstant positive-run lengths is at most

\[
 \sum_{t=0}^{L-1}|V_t-F|=aL.                       \tag{2.4}
\]

Thus their average run length is at most `a`; hence the minimum is at most
`a`.  (Coordinates constant outside `F` only contribute additional
full-cycle runs and do not weaken the inequality.)  If every
run has length at least `d+1`, (2.3) follows. `square`

Along (1.1), the fixed set is `C union {q_(i+1)}` of rank `m-2`, so the
aperture is exactly two.  Thus any resident replacement at growing depth
must shed at least `d-1` further fixed-core coordinates and operate with at
least `d+1` simultaneously variable slots.  Merely lengthening the same
two-slot rail or adding endpoint collars cannot work.

## 3. Exact inherited-socket equation

The two-transition closure in the spanning-host theorem is a proof device;
it is not automatically the inherited MNW terminal interface.  The exact
label condition is elementary.

In the proved closed bank, every `F_i` and `R_i` already has protected
degree two.  Therefore no additional factor-visible terminal incidence can
be appended at any of those owners.  Coinstantiation must **replace** the
closure incidences by the inherited exterior terminal paths (or cut and
rejoin them in one simultaneous bank); it cannot take the union of the
closed host and a separately constructed terminal bank.

Let

\[
                         s(i)=i+1\pmod4             \tag{3.1}
\]

be the local output shift made by the `C8`.  Suppose the exterior recursive
interface, including any fixed terminal paths, sends the outgoing socket
`F_i` to the next incoming socket `R_(kappa(i))`, for a labelled bijection
`kappa in S_4`.  Assume no further marked socket lies inside those exterior
paths.

### Lemma 3.1 (recursive terminal compatibility)

The old and switched first-return permutations on the four incoming
sockets are respectively

\[
                         \boxed{theta_0=kappa,
                         \qquad theta_1=kappa\circ s.}          \tag{3.2}
\]

Hence a prescribed inherited pair `(theta_0,theta_1)` can be realized by
this local actuator if and only if

\[
                         \boxed{theta_1=theta_0\circ s}         \tag{3.3}
\]

after the one allowed common relabelling of the four terminal indices.

#### Proof

Before the switch, incoming socket `R_i` traverses output path `i`, reaches
`F_i`, and then follows the exterior to `R_(kappa(i))`.  After the switch it
traverses output path `s(i)`, reaches `F_(s(i))`, and follows the same
exterior to `R_(kappa(s(i)))`.  These are exactly (3.2). `square`

For the artificial closure, `kappa=id`, so the old return is the identity
and the new return is the odd four-cycle `s`.  An inherited MNW terminal
bank need not have `kappa=id`; what is invariant is (3.3), not the names of
the private closure sockets.

Every exterior path from `F_i` to `R_(kappa(i))` must also start with phase
zero and end with phase one, because the protected path enters `F_i` in
phase one and leaves `R_i` in phase zero.  Since both endpoints are on the
upper shore, any alternating incidence path between them has even length;
this is exactly the required phase parity.

## 4. A robust phased-host theorem for the redesigned joint bank

The residence obstruction forces a different local rail, but it does not
reopen a difficult generic factor-Hall problem.

Let `P_m subseteq ML_m` be a union of pairwise vertex-disjoint, properly
two-coloured incidence cycles.  In particular, the selected lower vertices
all have protected degree two and every protected upper owner has degree at
most two.  Write

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},\qquad
 W=|\mathcal L|=|\mathcal U|,
 \tag{4.0}
\]

put `mathcal Z(P_m)={x in mathcal L:d_(P_m)(x)=2}`, and put

\[
\begin{aligned}
 e_m&=|E(P_m)|,\\
 \alpha_m&=\max_{x:d_{P_m}(x)=0}
   |\{U:x\subset U,\ d_{P_m}(U)>0\}|,\\
 \beta_m&=\max_U|N(U)\cap\{x:d_{P_m}(x)=2\}|.
\end{aligned}                                       \tag{4.1}
\]

### Theorem 4.1 (subexponential low-exposure coinstantiation)

If

\[
                         e_m=2^{o(m)},
 \qquad \alpha_m=o(m),
 \qquad \beta_m=o(m),                              \tag{4.2}
\]

then, for all sufficiently large `m`, `P_m` is contained in a spanning
two-factor of `ML_m`.  The alternating phases of every protected cycle are
retained, so the containing factor gives one ordered two-SDR containing
the entire phase bank.

#### Proof

The protected-Ore small/co-small localization theorem in
`MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` says that every
failed residual shore `A` obeys

\[
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}e_m=2^{o(m)}.                   \tag{4.3}
\]

The degree-only threshold argument in
`MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`
gives

\[
 |A|\ge K(m-\alpha_m-1),                            \tag{4.4}
\]

and, for the positive optional complement

\[
 B=(\mathcal L\setminus\mathcal Z(P_m))\setminus A,
 \qquad |B|\ge K(m-\beta_m-1)+1,                  \tag{4.5}
\]

where

\[
                         K(D)={2D-1\choose D}.       \tag{4.6}
\]

Because `alpha_m,beta_m=o(m)`, both right sides in (4.4)--(4.5) are

\[
                         2^{2m-o(m)}.              \tag{4.7}
\]

The small alternative in (4.3) contradicts (4.4).  In the co-small
alternative,

\[
                         |B|<W-|A|=2^{o(m)},         \tag{4.8}
\]

contradicting (4.5).  Hence no failed shore exists, and Ore--Ryser supplies
the spanning two-factor.  Each protected cycle is already saturated and
therefore remains one complete factor component, whose alternating phase
may be fixed independently. `square`

The same proof applies when a finite or deadline-scale collection of
resident terminal paths and factor-visible private-prefix paths is first
closed according to the inherited permutation `kappa`, provided the whole
closed bank satisfies (4.2).  Thus **factor coinstantiation is automatic**
after constructing one literal low-exposure joint bank.  Separate marginal
factor completions are neither needed nor sufficient.

## 5. The private common-cap cut remains occurrence-level

Theorem 4.1 concerns the Middle-Levels factor only.  A common-cap prefix is
not certified merely because its endpoint owner occurs in that factor.

Fix one complete cap/guard/phase/occurrence state.  After deleting the
fixed compensation linkage and every capacity used by the selected factor
bank and the literal prefix interiors, let `mathcal P` be the active
occurrence-labelled port set, let `T` be the unused correctly typed sink
bank, and let `Gamma_suf^type` be the strict gammoid of the residual typed
suffix network.

### Proposition 5.1 (exact full-port router gate)

The complete selected port bank has simultaneous pairwise-disjoint typed
suffixes if and only if

\[
 \boxed{r_{\Gamma_{\rm suf}^{\rm type}}(\mathcal P)=|\mathcal P|.} \tag{5.1}
\]

Equivalently, for every `S subseteq mathcal P`,

\[
 \boxed{
 \kappa_{\mathcal D_{\rm suf}^{\rm type}}(S,T)\ge|S|,}         \tag{5.2}
\]

where `kappa` is minimum node-split cut capacity.

#### Proof

Linkable port sets are exactly the independent sets of the strict gammoid.
Equation (5.1) says the full port set is independent.  Menger's theorem
turns this into the all-subset cut condition (5.2). `square`

Together with pairwise-private claim-to-port prefixes, (5.1) invokes the
regular-incidence-factor private-router theorem in
`MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`.
Neither the spanning
two-factor nor the socket equation (3.3) implies (5.1): a single common
unit suffix bottleneck is a counterexample.  The cap state must be fixed
before the graph and its structural zeros are formed.

## 6. Exact joint frontier

The current all-width collar cannot be promoted to the desired joint
interface by adding guards.  It must be replaced.  A sufficient and now
sharply separated replacement theorem is:

> **Resident MNW-cap collar theorem.**  Construct a properly phased closed
> incidence bank which
>
> 1. replaces the two-slot neutral rail by a variable aperture at least
>    `d+1` and has no internal positive run shorter than `d+1`;
> 2. retains the all-width prefix identity and full-union shield;
> 3. closes its labelled exterior terminals by a bijection `kappa`
>    satisfying `theta_1=theta_0 circ s`;
> 4. includes pairwise-private literal claim-to-port prefixes in one fixed
>    cap state;
> 5. has `e=2^{o(m)}` and `alpha,beta=o(m)`; and
> 6. satisfies the typed suffix cut (5.2).

Items 1--3 are the redesigned local/recursive module.  Item 5 then gives
the spanning phased host automatically by Theorem 4.1.  Items 4 and 6 give
the common-cap router in that **same** occurrence state.

The obstruction proved here is exact: item 1 fails in the existing collar
on the protected run (1.3).  The surviving construction problem is no
longer ordinary factor extension or local all-width current; it is a
resident aperture-`d+1` replacement carrying the inherited terminal labels
and the private-prefix/cut certificate.

## 7. Subsequent closure of the resident phased-host row

The aperture target isolated in Sections 1--4 is now met by

`MATH_THEOREM_COMMON_MATE_C8_COMPLEMENTARY_SQUARE_RESIDENT_ALLWIDTH_HOST_20260813.md`.

That construction replaces each two-slot neutral rail by a complementary
square Johnson cycle.  Its outward half introduces all missing coordinates
in one synchronized order, while its independently ordered return ends at
the literal inherited `R_i` socket.  It proves, on one protected bank,

\[
 \text{all-width current zero}
 +\text{ two-sided depth residence}
 +\text{ an ordered two-SDR host}
 +\text{ the odd crossed socket action}.             \tag{7.1}
\]

The bank has `e_m=16m-16` and constant exposure, so Theorem 4.1 applies
automatically.  Thus the internal residence obstruction in Theorem 1.1 is
an obstruction to the old two-slot rail, not to all all-width actuators.

The remaining joint interface is correspondingly narrower: identify the
two marked returns with the inherited recursive MNW terminal labels, plant
literal private claim-to-port prefixes at those same occurrences, and
verify the full typed cut (5.2).  No residence, phase-host, or all-width
upper-current redesign remains in that local row.

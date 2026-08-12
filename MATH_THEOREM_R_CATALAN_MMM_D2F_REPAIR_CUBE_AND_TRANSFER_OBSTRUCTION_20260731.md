# Raw canonical MMM turn-support obstruction and the exact `m=5` D2F repair cube

Date: 2026-07-31  
Status: exact finite target-coefficient theorem; exact circuit-transfer
obstruction; exact boundary-state transfer theorem; no all-dimension D2F
positivity theorem

## 0. Verdict

The canonical unmodified MMM factor has an exact turn-support deficit in
every nondegenerate paper parameter `n=m-1>=2`.  It attains

\[
 (2n+1)(\operatorname {Cat}_n-\operatorname {Cat}_{n-1})
\]

colours on each turn shore.  Its deficit is

\[
 D_n=(2n+1)\frac{(n-2)(n-3)}{(n+1)(n+2)}
                 \operatorname {Cat}_{n-1},
 \qquad \frac{D_n}{\binom{2n+1}{n-1}}\longrightarrow\frac14.
\]

Thus its D2F coefficient is zero for every `n>=4`, not just at the first
obstructed dimension `m=5`.  Any alternating-circuit repair with circuit
half-lengths `t_i` must satisfy `sum t_i>=D_n`.  No bounded-total-support
packet can repair this raw family.

The degenerate `n=1` base is separate: its single turn colour is attained,
so `A_1=P_1=1` and `D_1=0`.  Formula (2.10) is not asserted there because
the all-empty three-forest pair is not a two-element duplicated class.

At `m=5` the deficit is three on each shore.  This is not merely a failure
of one Hamilton gluing tree: every endpoint in the complete raw minimal ECO
family misses the same three lower and three upper turn colours, so its
configuration polynomial omits six required variables.

The authenticated three-`C10` packet is an exact polynomial exchange on a
larger state.  In its frozen three-cube every proper subset has target
coefficient zero, while the full packet has positive target coefficient
already on the repaired **preglue two-factor** with component lengths
`120,132`.  Hamiltonicity is unnecessary for this conclusion.

The repair cannot be expressed as multiplication of the scalar component
polynomials by three colour monomials.  A circuit changes cyclic gaps,
component partitions, unmarked phases and the binary trace.  In the exact
`ML(7)` calibration, 1,728 decorations project to the same target monomial,
but one fixed hex preserves only 144 of them, and only 72 preserve the gap
forest.  Hence the colour-set projection is not a congruence for circuit
transfer.

The correct inductive object is an occurrence-, phase-, fragment- and
trace-labelled boundary polynomial vector.  Alternating circuits act on this
vector by monomial-weighted `0-1` transfer matrices; the scalar configuration
polynomial is only its terminal projection.  This gives an exact repair-
packet recurrence, but not its all-`m` nonemptiness.  The remaining theorem is
uniform supply of an accepting orbit-router packet in this refined state.

## 1. The missing-variable ideal

Fix a spanning two-factor `F` of `ML(2m-1)`.  Let

\[
 S^-(F)=\{\ell:\ell\text{ occurs as a lower turn of }F\},\qquad
 S^+(F)=\{u:u\text{ occurs as an upper turn of }F\}.       \tag{1.1}
\]

Let `P_F(x,y)` be the corrected D2F configuration polynomial from
`MATH_THEOREM_R_CATALAN_D2F_CONFIGURATION_POLYNOMIAL_AND_ACCEPTING_ROOT_20260731.md`.

### Lemma 1.1 (missing-variable obstruction)

Every monomial of `P_F` uses only variables

\[
 \{x_u:u\in S^+(F)\}\cup\{y_\ell:\ell\in S^-(F)\}.       \tag{1.2}
\]

Consequently, if either turn map is not surjective, then

\[
                         [\mathfrak m_*]P_F=0.          \tag{1.3}
\]

#### Proof

A local configuration can select only literal turn occurrences of `F`.
Its colour monomial therefore uses only variables in (1.2).  The target
monomial contains every upper and every lower variable, so absence of one
variable forces (1.3).  \(\square\)

This elementary obstruction is useful because it precedes gap Hall and the
binary-face test.  It is a polynomial **subring** obstruction, not a claim
that a missing-variable product divides a later polynomial.

## 2. The complete raw canonical `m=5` family is coefficient-zero

At `m=5`, identify lower turn colours with rank-three masks on `[9]` and
upper turn colours with rank-six masks.  Put

\[
 \mathcal L_0=\{73,146,292\},\qquad
 \mathcal U_0=\{219,365,438\}.                       \tag{2.1}
\]

These are complementary period-three rotation orbits.

### Theorem 2.1 (finite obstruction to raw canonical MMM/ECO induction)

For the canonical `m=5` MMM factor:

1. every standard incidence-hex gluing sequence still misses the lower
   orbit `\mathcal L_0`; and
2. every one of the `648` legal ordered minimal raw ECO Hamiltonizations
   (the `324` distinct endpoints) misses exactly `\mathcal L_0` and
   `\mathcal U_0`.

Therefore every factor in the raw standard gluing family and every terminal
factor in the complete minimal raw ECO family satisfies

\[
                         [\mathfrak m_*]P_F=0.         \tag{2.2}
\]

#### Proof

The literal turn census and the local standard-label calculation prove that
the standard glues only permute their attained lower owner triples and do
not create an occurrence of any colour in `\mathcal L_0`.  The independent
raw-ECO census reconstructs all 45 physical atoms and every legal ordered
two-atom Hamiltonization; every endpoint has the exact missing lists (2.1).
Lemma 1.1 gives (2.2).  \(\square\)

Thus the explicit unmodified recursively described family has a genuine
finite obstruction at `m=5`.  Component merging, a different standard tree,
and collision-free coherent ports do not remove it.  A nonstandard
preparation packet or a different factor is necessary.

## 2A. Exact all-dimension turn support of the raw canonical factor

Use the paper parameter `n=m-1>=2`, put `q=2n+1`, and let `F_n` be the raw
canonical MMM factor on `ML(q)`, whose shores have ranks `n,n+1`.

### Lemma 2.2 (turn normal forms)

Up to cyclic coordinate rotation, the upper turns of `F_n` are exactly

\[
                            1u1v1,                    \tag{2.3}
\]

and the lower turns are exactly

\[
                            0u0v0,                    \tag{2.4}
\]

where `u,v` are Dyck words with total semilength `n-1`.

#### Proof

Every coordinate-rotation orbit of rank-`n` words has a unique representative
`D0`, where `D` is a Dyck word of semilength `n`.  Write its first-return
decomposition as `D=1u0v`.  By
the defining MMM map,

\[
 f(D0)=1u1v0.                                         \tag{2.5}
\]

Its other factor neighbour is `D1=1u0v1`: rotate `D1` to `1D`, use the
upper-to-lower half of the MMM matching, `f(1D)=0D`, and rotate back to
`D0`.  Thus `f(D1)=D0`, and the union of the two upper neighbours is (2.3).

Similarly every rank-`n+1` word has unique cyclic form `1D`.  Write the
last-return decomposition `D=u1v0`.  Its two lower neighbours are
`0u1v0` and `1u0v0`, whose intersection is (2.4).  Every ordered Dyck pair
of total semilength `n-1` occurs in the appropriate first- or last-return
decomposition.  \(\square\)

### Lemma 2.3 (cyclic three-forest quotient)

The cyclic words (2.3) form exactly

\[
                    \operatorname {Cat}_n-
                    \operatorname {Cat}_{n-1}         \tag{2.6}
\]

rotation classes, and every class is free under `Z_q`.  The same holds for
(2.4).

#### Proof

A cyclic binary word of excess three has a unique cyclic triple of Dyck
words `(a,b,c)`, up to cyclic permutation, in the form

\[
                             1a1b1c.                  \tag{2.7}
\]

Indeed, take one of the three positive starting positions supplied by the
cycle lemma (counted with multiplicity if the binary word is periodic) and
cut after the last visits to heights one and two.  The other two positive
cuts cyclically permute the three Dyck blocks.

The triple belonging to (2.3) is `(u,v,empty)`.  If both `u,v` are nonempty,
the unique empty component fixes the cyclic cut, so no two ordered pairs are
identified.  If exactly one is empty, precisely

\[
                         (u,\varnothing)\sim
                         (\varnothing,u)              \tag{2.8}
\]

are identified.  Catalan convolution gives `Cat_n` ordered pairs, and the
one-empty pairs give exactly `Cat_{n-1}` duplicated classes.  This proves
(2.6).

A nonfree upper turn would have repetition number dividing

\[
                  \gcd(2n+1,n+2)=\gcd(3,n+2),        \tag{2.9}
\]

so the only possibility is a threefold repetition `R^3`.  After rotation,
an excess-one word `R` is `1w` for one Dyck word `w`; the cyclic three-
forest triple of `R^3` is `(w,w,w)`.  It cannot equal `(u,v,empty)` unless
all three words are empty, which would give `n=1`.  Thus every upper class
is free for `n>=2`.  Reverse-complementation takes the lower normal form to
the same positive three-forest situation, so the lower classes are free as
well.  \(\square\)

### Theorem 2.4 (closed raw-MMM palette deficit)

The raw canonical factor attains exactly

\[
 A_n=(2n+1)(\operatorname {Cat}_n-
                   \operatorname {Cat}_{n-1})        \tag{2.10}
\]

distinct colours on each turn shore.  The total palette size and deficit
are

\[
 P_n=\binom{2n+1}{n-1},                              \tag{2.11}
\]

\[
 D_n=P_n-A_n
   =(2n+1)\frac{(n-2)(n-3)}{(n+1)(n+2)}
                  \operatorname {Cat}_{n-1}.         \tag{2.12}
\]

Consequently

\[
 \frac{D_n}{P_n}=\frac{(n-2)(n-3)}{2n(2n-1)}
                         \longrightarrow\frac14.     \tag{2.13}
\]

In particular, `[\mathfrak m_*]P_{F_n}=0` for every `n>=4`.

#### Proof

Rotation-equivariance supplies every one of the `q` rotations of every
class in Lemma 2.3, and freeness makes these rotations distinct.  This gives
(2.10) on each shore.  Complementation gives the common palette size
(2.11).  Use

\[
 \operatorname {Cat}_n=\frac{2(2n-1)}{n+1}
                        \operatorname {Cat}_{n-1}
\]

and

\[
 \binom{2n+1}{n-1}
 =\frac{2n(2n-1)(2n+1)}{(n+1)(n+2)}
                       \operatorname {Cat}_{n-1}
\]

to subtract (2.10), obtaining (2.12).  Division gives (2.13).  For
`n>=4`, the deficit is positive, so Lemma 1.1 forces the target coefficient
to vanish.  \(\square\)

The first values are

\[
\begin{array}{c|rrrrrr}
n&2&3&4&5&6&7\\ \hline
D_n&0&0&3&22&117&550.
\end{array}                                           \tag{2.14}
\]

At `n=5` the ground size is prime `11`, so the 22 missing colours are two
free rotation orbits.  The raw obstruction is therefore not exclusively a
period-three phenomenon.

### Theorem 2.5 (circuit-support lower bound)

Let an ordered alternating-circuit packet transform `F_n` into `F'`.  If
its circuits have lengths `2t_1,...,2t_s`, then on either turn shore

\[
 |S^\pm(F')\setminus S^\pm(F_n)|
                         \le\sum_{i=1}^s t_i.         \tag{2.15}
\]

Hence palette completeness, and therefore D2F positivity, requires

\[
                              \sum_i t_i\ge D_n.      \tag{2.16}
\]

#### Proof

An alternating `2t_i`-circuit meets at most `t_i` vertices on either shore.
Only the turn at a met vertex can change.  It therefore introduces at most
`t_i` colours absent immediately before the switch and, a fortiori, the
union of all colours new relative to the initial factor is bounded by the
sum in (2.15).  If that sum is below `D_n`, at least one initially absent
palette variable is still absent at the endpoint.  Lemma 1.1 proves zero
target coefficient.  \(\square\)

Thus a repair of the raw canonical factor needs macroscopic total circuit
support: asymptotically at least one quarter of a turn palette.  This does
not obstruct a growing global repair family, but it rules out any induction
which attaches only `O(1)` bounded circuits to the raw factor at each
dimension.  It does not rule out `O(1)` additional circuits applied to an
already repaired factor supplied by a stronger recursive lift.

## 3. The exact three-`C10` target-coefficient exchange

Let `C_1,C_2,C_3` be the frozen support-disjoint switches in
`MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`.
Index the periodic lower orbit by

\[
 L_0=73,\qquad L_1=146,\qquad L_2=292.                \tag{3.1}
\]

Their upper defect orbit is the complementary orbit, and the switch packet
uses the cyclic relay

\[
 C_1:L_0\mapsto\overline{L_1}=365,qquad
 C_2:L_1\mapsto\overline{L_2}=219,qquad
 C_3:L_2\mapsto\overline{L_0}=438.                   \tag{3.2}
\]

Define the missing-variable bookkeeping monomial

\[
 D=x_{219}x_{365}x_{438}y_{73}y_{146}y_{292}          \tag{3.3}
\]

and the three service monomials

\[
 r_1=y_{73}x_{365},\qquad
 r_2=y_{146}x_{219},\qquad
 r_3=y_{292}x_{438}.                                 \tag{3.4}
\]

Then

\[
                              r_1r_2r_3=D.            \tag{3.5}
\]

Equation (3.5) records only defect service.  It is not a factorization of
configuration polynomials.

For a subset `S\subseteq\{1,2,3\}`, let

\[
                  H_S=H_0\mathbin\triangle
                       \mathop{\triangle}_{i\in S}C_i.            \tag{3.6}
\]

Here `H_0` is the transparent standard Hamilton output.  Separately, write
`G_{111}` for the factor obtained by applying the complete packet to the
canonical preglue factor.  The frozen audits treat both literal contexts;
the proper-subset cube below is asserted only for `H_S`.

### Theorem 3.1 (unique positive vertex of the frozen repair cube)

In the frozen three-switch cube,

\[
 [\mathfrak m_*]P_{H_S}=0\quad(S\subsetneq\{1,2,3\}),
 \qquad
 [\mathfrak m_*]P_{H_{\{1,2,3\}}}>0,
 \qquad [\mathfrak m_*]P_{G_{111}}>0.                \tag{3.7}
\]

The positive endpoint already occurs on the repaired preglue factor, whose
two components have lengths `120` and `132`.

#### Proof

The complete signed-bank audit gives the missing-palette table

\[
\begin{array}{c|c|c}
S&\operatorname {miss}_-&\operatorname {miss}_+\\ \hline
000&73,146,292&219,365,438\\
001&146,292&219,438\\
010&73,292&365,438\\
011&292&438\\
100&73,146&219,365\\
101&146&219\\
110&73&365\\
111&\varnothing&\varnothing.
\end{array}                                           \tag{3.8}
\]

Every proper subset is zero by Lemma 1.1.  At `111`, the independently
replayed augmented occurrence graph has a perfect matching of order
`210`; its selected occurrences give a forest gap graph and an off-face
binary trace.  The same forced-port decoration is valid at the `(0,0)`
preglue point of the standard-glue cube, where the factor has component
lengths `120,132`.  The corrected D2F coefficient theorem therefore makes
both final coefficients positive.  \(\square\)

The Hamilton-output subset topology is correlated.  Its component counts in
selector order `000,...,111` are

\[
                         1,1,1,1,2,3,2,1,             \tag{3.9}
\]

and the Hamilton-safe installation routes are exactly

\[
 000\to001\to011\to111,qquad
 000\to010\to011\to111.                              \tag{3.10}
\]

Thus `C_3` is a contextual final relay.  Static palette multiplication does
not encode (3.9)--(3.10).

### Exact minimality scope

The proved minimality statements are only these:

* no single `C6`, `C8`, or `C10` repairs the standard endpoint;
* no sequence of at most three incidence-hex toggles repairs it;
* all three switches are necessary inside the frozen support-monotone
  three-cube; and
* the recorded 281-candidate common-exterior two-switch pool contains no
  complete pair.

There is no exhaustive exclusion of two adaptive overlapping circuits or
two longer circuits.  Hence “three `C10`s are globally minimal” is not a
proved statement.  They are the smallest authenticated positive packet in
the audited bounded catalogue.

## 4. Why `P_C` is not a circuit-transfer state

Let `Sigma(F)` be the literal occurrence-labelled accepting decorations of
`F`, including the residual phase on every unmarked component, and let

\[
 \pi:\Sigma(F)\longrightarrow\operatorname {Mon}(P_F),qquad
 \pi(\sigma)=\mathbf x^{U(\sigma)}\mathbf y^{L(\sigma)}.         \tag{4.1}
\]

For a fixed alternating circuit `Z`, let `s_Z(sigma)=1` when the same
literal selected occurrences and residual choices survive as an accepting
decoration of `F\triangle Z`, and `0` otherwise.

### Proposition 4.1 (descent criterion)

A termwise switch operator on the scalar monomials of `P_F` can represent
fixed-decoration transfer through `Z` only if `s_Z` is constant on every
fibre of `pi`.

#### Proof

A scalar monomial identifies all elements of one fibre.  Any operator
defined on that monomial must give the same survival verdict to every
element represented by it.  \(\square\)

### Theorem 4.2 (exact ML(7) noncongruence)

For the repaired `ML(7)` source and the fixed transparent hex
`H=66,(a,b,c)=(0,3,4)`, the target-monomial fibre has `1,728` literal
decorations.  Exactly `144` survive on both factors, while `1,584` do not.
Among the `144` common decorations, exactly `72` remain leaf-peelable on
both sides and `72` acquire the audited gap `C4`.

Consequently neither fixed-decoration survival nor forest survival descends
to the scalar configuration monomial.  In particular, there is no
coefficientwise/fibre-blind transfer identity of the form

\[
                         P_{F\triangle Z}=T_Z(P_F)     \tag{4.2}
\]

in which `T_Z` transports every decoration represented by one unlabelled
colour-set monomial uniformly.

#### Proof

All 1,728 decorations use every upper and lower colour exactly once, hence
all project to the single target monomial.  The literal transparent-hex
audit gives the `144/1,584` split and the forest audit gives the `72/72`
split.  Proposition 4.1 applies.  \(\square\)

This does not exclude an arbitrary nonlinear rule which recomputes the
entire output factor and all of its decorations from scratch.  Such a rule
is not a local circuit transfer on `P_F`; it uses information absent from the
polynomial.

There is an even smaller phase obstruction: the two unmarked residual
phases both contribute the same constant monomial `1`, but a fixed factor
edge belongs to exactly one of them.  Any switch rule touching that edge
must retain a phase bit.

The theorem does not weaken terminal exactness of `P_F`.  One may recompute
all representatives on the output factor.  That recomputation is a new
global occurrence-labelled gap-Hall problem, not a local operation on the
old scalar coefficient.

### Proposition 4.3 (the `m=5` cube forbids independent polynomial multipliers)

For every factor `F`,

\[
                              [1]P_F=2^{c(F)},         \tag{4.3}
\]

where `c(F)` is its number of components.  Therefore no three
context-independent scalar polynomials `R_1,R_2,R_3` satisfy

\[
                         P_{H_S}=P_{H_0}
                                      \prod_{i\in S}R_i           \tag{4.4}
\]

for all eight vertices of the frozen repair cube.

#### Proof

Each unmarked component contributes exactly its two residual phases, so
(4.3) follows from the definition of the local configuration polynomial.
The component counts (3.9) give constant coefficients

\[
                         2,2,2,2,4,8,4,2              \tag{4.5}
\]

in selector order.  The singleton states force
`[1]R_1=[1]R_2=1` and `[1]R_3=2`.  Equation (4.4) would then give constant
coefficient `4` at selector `101`, whereas the actual coefficient is `8`.
\(\square\)

This obstruction uses only component pairing.  The richer ML(7)
noncongruence additionally shows that even after component count is retained,
occurrence and gap-forest state cannot be projected away.

## 5. The exact boundary-state polynomial transfer

Fix a finite alternating-circuit packet and cut every old packet edge before
performing any reconnection.  The unchanged factor edges form oriented path
fragments together with untouched cycles.  A **complete packet boundary
state** records:

1. every selected packet-port occurrence and its old and possible new turn
   labels;
2. for every retained fragment, whether its selected subsequence is empty
   and, if nonempty, the shore types of its first and last selected marks;
3. the cyclic occurrence/gap identities exposed at the packet boundary;
4. the `Z_2` residual phase of every unmarked component touched by the
   packet;
5. a binary-trace automaton state distinguishing all-zero, all-one, the
   exceptional mixed face, and a certified breaker; and
6. when representatives may change, the occurrence-labelled exposed
   matching/linkage relation and the current component pairing.

Let `\mathcal B` be the finite set of such states.  Define a vector

\[
 \mathbf Q_{F,Z}=(Q_b)_{b\in\mathcal B},              \tag{5.1}
\]

where `Q_b` is the generating polynomial of partial decorations inducing
boundary state `b`.  Internal colours already consumed contribute their
usual `x,y` variables.

Every old or new packet port pairing `rho` defines a monomial-weighted
`0-1` contraction matrix `T_rho`: it joins the retained fragments, inserts
the newly determined turn-colour variables, rejects repeated colours or
invalid matching degrees, updates the trace automaton, and rejects every
sealed component on the all-one or exceptional mixed face.  Let `epsilon`
sum the accepting empty-boundary entries.

### Theorem 5.1 (exact circuit-transfer identity)

For every literal packet reconnection `rho`,

\[
                         P_{F_\rho}
                     =\epsilon T_\rho\mathbf Q_{F,Z}.             \tag{5.2}
\]

For an ordered packet `rho_1,...,rho_s`, after retaining the full exposed
state at intermediate steps,

\[
 P_{F_s}=\epsilon T_{\rho_s}\cdots T_{\rho_1}\mathbf Q_{F_0,Z}.  \tag{5.3}
\]

#### Proof

Restrict a literal accepting decoration of `F_rho` to the retained
fragments.  This gives one and only one partial decoration and boundary
state in (5.1).  Its seams pass exactly the degree, colour, alternation,
phase, matching and trace tests encoded by `T_rho`.  Conversely every
accepted contraction joins the retained literal occurrences into a unique
componentwise decoration of `F_rho`; the inserted monomial records precisely
the new seam turns.  These maps are inverse and preserve monomial weights,
proving (5.2).  Repeating the same restriction/gluing bijection at every
packet step proves (5.3).  \(\square\)

The state list is not claimed minimal, but Theorem 4.2 and the unmarked-phase
example prove that occurrence and phase data cannot both be dropped.  If
leaf peelability rather than only the D2F face is required, the boundary
state must additionally retain the delete-contract-insert gap-forest
relation.

## 6. A reusable repair-packet coefficient theorem

Let `F_0` have missing lower set `L` and missing upper set `U`, with
`|L|=|U|=d`.  Suppose a supplied macro catalogue is occurrence-level
support-monotone: every selected macro services one pair
`(\ell(e),u(e))\in L\times U`, every negative turn occurrence is surplus at
the prefix where it is removed, and no serviced or initially covered colour
is subsequently lost.

### Theorem 6.1 (router product plus accepting transfer)

For a selected macro set `M`, the palette defect monomial is repaired
exactly once on both shores if and only if

\[
 \prod_{e\in M}y_{\ell(e)}x_{u(e)}
       =\prod_{\ell\in L}y_\ell\prod_{u\in U}x_u.     \tag{6.1}
\]

Equivalently, the service edges form a perfect matching between the two
defect banks after retaining the supplied occurrence-capacity rows.

If, in addition, the packet has a legal path in its exact boundary-state
automaton and

\[
 [\mathfrak m_*]\,
   \epsilon T_{\rho_s}\cdots T_{\rho_1}\mathbf Q_{F_0,Z}>0,      \tag{6.2}
\]

then its endpoint is an accepting D2F and induces a `Cat_m`-path forest.

#### Proof

Squarefreeness in (6.1) says that every defect on each shore is serviced
once and no defect is repeated.  Support monotonicity preserves all other
palette variables.  The legal automaton path makes every circuit a literal
factor transition.  Equation (6.2), Theorem 5.1 and the target-coefficient
equivalence give the D2F endpoint and its physical forest.  \(\square\)

The nontrivial part of (6.2) is not palette coverage.  It is the terminal
occurrence matching/linkage and the component trace.  At `m=5`, the full
packet satisfies (6.1), while its source/final common augmented graph has
deficiency `13`; thirteen augmenting paths discharge that global debt.

## 7. What an all-`m` MMM induction must now prove

The exact surviving statement is the following supply lemma.

> **MMM refined repair-packet positivity lemma.**  For every `m`, choose a
> factor in an explicitly recursive MMM/ECO family and a bounded-port
> alternating-circuit packet whose service edges cover all missing turn
> variables as in (6.1), whose exact port/occurrence state has a legal
> ordered path, and whose terminal transfer has positive target coefficient
> as in (6.2).  The packet cardinality may grow, but the live boundary state
> exposed to the next recursive level must have uniformly controlled
> adhesion.

This lemma is not proved.  The `m=5` cube proves it once, with a three-cycle
defect router and one atomic terminal linkage.  The raw canonical family is
finitely false by Theorem 2.1.

The exact raw-family lower bound (2.16) is stronger than the earlier
period-three-only warning.  Already at project `m=6` (`n=5`) it requires
total half-length at least `22`, although every missing orbit is free.  The
correct prospective induction is therefore a macroscopic orbit router with
bounded **live interface**, not a packet with bounded cardinality or total
support.

An unconditional all-`m` target-coefficient positivity theorem remains
open.  The precise advance is that its recursive state and the first finite
failure are now exact: scalar `P_C` induction is invalid, raw canonical ECO
induction dies at `m=5`, and the first live replacement is a refined
occurrence-labelled orbit-router transfer.

## 8. Audit boundary

The finite claims use the independently frozen literal audits behind:

* `MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`;
* `MATH_THEOREM_CATALAN_M5_REPAIRED_PRIVATE_GRAPHIC_GAMMOID_FACE_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.

The new deductions are Lemma 1.1, the turn-normal-form and three-forest
count, the exact raw-family deficit and circuit lower bound, the coefficient
interpretation of the frozen cube, the noncongruence theorem, and the exact
boundary-state transfer identity.  They use no finite search beyond those
already authenticated source theorems.

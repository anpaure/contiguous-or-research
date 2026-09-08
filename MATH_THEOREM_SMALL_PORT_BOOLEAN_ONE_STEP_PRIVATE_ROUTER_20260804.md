# Small Boolean port banks have exact one-step private routers

**Date:** 2026-08-04  
**Status:** unconditional Hall theorem, with a conditional application to the
terminal common-cap interface.  No finite computation is used.

## 0. Result and scope

Let `P` be a bank of distinct rank-`s` Boolean states.  Suppose every port
has at least `L` legal typed one-coordinate extensions to rank `s+1`.  Let
`F` be the set of extension sinks already occupied by the fixed
compensation linkage, the literal prefix interiors, or another protected
bank.

If

\[
 |P|\le L,
 \qquad |F|\le L-1,                                  \tag{0.1}
\]

then all ports have pairwise distinct legal one-step sinks outside `F`.
Thus the entire active port bank, not merely every port separately, has a
simultaneous private suffix linkage.

The useful asymptotic regime is

\[
 |P|=O(d(k))=O(\sqrt{k}),
 \qquad |F|=O(d(k)),
 \qquad L=\Theta(k).                                 \tag{0.2}
\]

In that regime (0.1) is automatic for all sufficiently large `k`.

This theorem closes only the **suffix-router** row of the regular
factor-plus-router argument when its hypotheses are literally present.  It
does not create the gain-to-port prefixes, the active Boolean port bank, or
the typed sink occurrences, and it does not prove that these objects coexist
with the upper selector and lower compiler in one cap state.

## 1. Boolean one-step neighbourhoods

Let

\[
 P\subseteq { [k]\choose s}
\]

be a family of distinct sets.  For every `p in P`, let

\[
 A(p)\subseteq [k]\setminus p
\]

be its legal extension labels and put

\[
 N(p)=\{p\cup\{a\}:a\in A(p)\}
       \subseteq {[k]\choose s+1}.                  \tag{1.1}
\]

The allowed labels may depend on `p`; they can encode terminal type, phase,
flags, and a fixed complete cap state.  Assume only

\[
 |N(p)|=|A(p)|\ge L                                  \tag{1.2}
\]

for every port.

### Lemma 1.1 (pair overlap)

If `p` and `p'` are distinct rank-`s` sets, then

\[
 |N(p)\cap N(p')|\le1.                               \tag{1.3}
\]

#### Proof

Any common member is an `(s+1)`-set containing both `p` and `p'`.  Such a
set exists only when `|p union p'|=s+1`, and then it is forced to be
`p union p'`.  Restricting the full upper shadows to the typed subfamilies
`N(p),N(p')` cannot increase the intersection.  \(\square\)

### Lemma 1.2 (small-bank expansion)

For every nonempty `X subseteq P`, writing `x=|X|`,

\[
 \left|\bigcup_{p\in X}N(p)\right|
 \ge xL-{x\choose2}.                                \tag{1.4}
\]

#### Proof

The first two terms of inclusion-exclusion give

\[
 \left|\bigcup_{p\in X}N(p)\right|
 \ge \sum_{p\in X}|N(p)|
    -\sum_{\{p,p'\}\in{X\choose2}}|N(p)\cap N(p')|.
\]

Apply (1.2) and Lemma 1.1.  \(\square\)

## 2. Exact private-router theorem

### Theorem 2.1 (one-step Boolean private router)

Let `F subseteq binom([k],s+1)` be any forbidden sink bank.  If

\[
 p:=|P|\le L,
 \qquad f:=|F|\le L-1,                               \tag{2.1}
\]

then there is an injection

\[
 \phi:P\longrightarrow {[k]\choose s+1}\setminus F
\]

such that `phi(p) in N(p)` for every `p in P`.

#### Proof

For `X subseteq P`, `x=|X|`, Lemma 1.2 gives

\[
 |N(X)\setminus F|
 \ge xL-{x\choose2}-f.                              \tag{2.2}
\]

It remains to show that the right side is at least `x`.  Equivalently,

\[
 g(x):=x(L-1)-{x\choose2}-f\ge0.                    \tag{2.3}
\]

As a real function on `[1,p]`, `g` is concave, so its minimum is attained
at an endpoint.  At the first endpoint,

\[
 g(1)=L-1-f\ge0.                                    \tag{2.4}
\]

At the other endpoint, using `p<=L`,

\[
 \begin{aligned}
 g(p)
 &\ge p(L-1)-{p\choose2}-(L-1)\\
 &=(p-1)\left(L-1-{p\over2}\right)\ge0,             \tag{2.5}
 \end{aligned}
\]

with the cases `p=1` and `L=1` already covered by (2.4).  Hence

`|N(X)\setminus F|>=|X|` for every `X subseteq P`.  Hall's theorem gives
the required injection.  \(\square\)

### Sharpness remarks

1. Distinct Boolean values are essential to the proof.  Two physical ports
   carrying the same mask can have identical sink menus, so occurrence
   multiplicity alone does not imply (1.3).
2. The bound `f<L` is necessary in this level of generality: one port can
   have exactly `L` legal sinks and all of them can be forbidden.
3. A linear lower bound on every typed degree is substantive.  If typing
   leaves one common unit sink for every port, all individual menus are
   nonempty but the simultaneous deficiency is `|P|-1`.

## 3. Literal occurrence lift

Fix one complete cap/guard/phase/occurrence state.  Put

\[
                     \mathcal Y=\bigcup_{p\in P}N(p).
\]

Before applying Theorem 2.1, fix one physical sink occurrence `r(Y)` for
every value `Y in mathcal Y` that is to remain eligible.  Equivalently,
enlarge the forbidden **value** set `F` by every `Y` for which no such
occurrence is available.  Assume that:

1. the active physical ports have pairwise distinct Boolean values in
   `P`;
2. every value `Y in mathcal Y-F` has the reserved physical sink occurrence
   `r(Y)` in that same state, of a terminal type accepted by every gain
   whose displayed prefix may end at `p` whenever `Y in N(p)`;
3. different reserved values use different unit-capacity sink vertices;
4. `F` contains every Boolean value `Y` whose reserved occurrence `r(Y)`
   is used by the fixed compensation linkage, by a prefix interior, or by
   any protected bank; and
5. the one-step inclusion arc from `p` to `r(Y)`, for `Y in N(p)-F`, uses no
   additional shared unit-capacity interior.

Under these hypotheses, Theorem 2.1 gives pairwise vertex-disjoint literal
suffixes

\[
 R_p:p\longrightarrow r(\phi(p)).                  \tag{3.1}
\]

Because these suffixes have no internal vertices, their only possible
intersection with a gain-to-port prefix is the terminal port itself; the
forbidden bank removes every possible sink collision.

### Corollary 3.1 (completion of a private incidence factor)

Let `B=(G,P;E)` satisfy

\[
 \deg_B(g)=h,
 \qquad \deg_B(p)\le h.                             \tag{3.2}
\]

Suppose the incidence prefixes `Q_gp:s_g -> p` satisfy all prefix-privacy
hypotheses of the regular incidence factor theorem, and suppose each
`N(p)` is a common type-legal neighbourhood for every gain adjacent to
`p` in `B`.
If the literal occurrence hypotheses above and (2.1) hold, then every gain
in `G` links to a distinct legal sink, simultaneously with the fixed
compensation linkage.

#### Proof

Theorem 2.1 and Section 3 provide the full simultaneous private suffix
router.  Concatenate every incidence prefix with the suffix of its terminal
port.  Weight each concatenation by `1/h`.  Every gain emits one unit and a
port/suffix receives load `deg_B(p)/h<=1`.  Integral max flow gives one
pairwise disjoint gain-to-sink path per gain.  \(\square\)

### Corollary 3.2 (middle-level specialization)

Let the port values be distinct `m`-sets of a `(2m+1)`-element ground set.
Suppose terminal typing forbids at most `c` of the `m+1` possible extension
coordinates at every port, so that

\[
                         L=m+1-c.                   \tag{3.3}
\]

If

\[
 |P|\le m+1-c,
 \qquad |F|\le m-c,                                 \tag{3.4}
\]

then the active port bank has a simultaneous one-step typed suffix router.
In particular, for a left-2-regular/right-at-most-2 incidence factor,

\[
 |G|\le {m+1-c\over2}                               \tag{3.5}
\]

implies `|P|<=m+1-c`; hence Corollary 3.1 applies whenever the literal
prefix and occurrence hypotheses hold.

For fixed `c` and `|G|=O(sqrt(m))`, (3.4)--(3.5) hold eventually even after
an `O(sqrt(m))` forbidden sink bank.  Thus the small protected-factor
theorem needs no additional long suffix network on this face: it needs the
factor's right shore to be injected into distinct middle-level values and
the corresponding one-step sink occurrences to be retained.

## 4. Consequence for bounded packet banks

Assume that a protected packet construction exposes

\[
 |P|\le C_1d(k),
 \qquad |F|\le C_2d(k),                              \tag{4.1}
\]

and that every active distinct Boolean port retains at least

\[
 L\ge \eta k                                        \tag{4.2}
\]

legal typed one-step extensions, for fixed positive constants
`C_1,C_2,eta`.  Since `d(k)=Theta(sqrt(k))`, for all sufficiently large `k`,

\[
 |P|\le L,
 \qquad |F|\le L-1.                                 \tag{4.3}
\]

Thus the suffix-router rank condition

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|             \tag{4.4}
\]

is automatic on this one-step Boolean face.

This turns the former full-port all-cut premise into two concrete local
construction requirements:

* inject the physical active ports into distinct Boolean states; and
* retain `Theta(k)` legal typed one-step terminal extensions per state
  after the common cap and fixed prefixes have been materialized.

Neither requirement follows from the abstract `h`-factor alone.  In
particular, (4.4) is not proved for an arbitrary parent-derived port bank,
for duplicate-valued occurrence ports, or for a terminal system whose
legal suffixes are genuinely multi-step and share internal capacities.

## 5. Updated frontier

The regular-factor synthesis no longer needs a separate global
strict-gammoid theorem **if** the port interface can be placed on the
one-step Boolean face above.  The exact remaining correlation is then:

\[
 \boxed{
 \begin{gathered}
 \text{one cap state with private gain-to-port prefixes, distinct Boolean}\\
 \text{port values, linearly many typed extensions per port, and the}\\
 \text{transported background/upper selector on disjoint occurrences.}
 \end{gathered}}
\]

This is strictly weaker than constructing an arbitrary private suffix
network and strictly stronger than a factor-plus-matching statement.

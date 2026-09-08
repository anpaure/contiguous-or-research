# The weakest Middle Levels trace target is a decorated 2-factor

Date: 2026-07-31  
Status: corrected exact all-dimension implication theorem; exact all-marked
boundary counterexample; no all-dimension decorated 2-factor is claimed

## 0. Verdict

The terminal Hamilton requirement in the current post-glue synthesis is
stronger than Catalan Linear Matching needs.  A spanning Middle Levels
**2-factor**, decorated componentwise, already gives the required perfect
diamond matching and Catalan path forest.

Consequently the weakest currently known trace target is:

> **Decorated Middle Levels 2-Factor Theorem.**  For every `m>=2`,
> `ML(2m-1)` has a spanning 2-factor with globally bijective upper and lower
> turn representatives, alternating selected shore types on every factor
> component, such that every marked component contains at least one
> unmarked occurrence and is off the binary cycle face.

A Hamilton cycle is one special 2-factor, so the Decorated Middle Levels
Theorem implies this statement.  The converse is not proved and is not
needed for Catalan Linear Matching.

The 2-factor difference theorem also applies unchanged: from any starting
Hamilton cycle or 2-factor, an alternating-circuit packet to an accepting
decorated 2-factor exists if and only if such a terminal 2-factor exists.
Thus component merging is not part of the minimal central existential gate.

## 1. Componentwise decorations

Fix `m>=2`, put `Omega=[2m-1]`, and let `F` be a spanning 2-factor of
`ML(2m-1)`.  On one component write

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.
\tag{1.1}
\]

The two turn colours are

\[
 \ell_i=A_i\cap A_{i+1}\in\binom\Omega{m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in\binom\Omega{m+1}.
\tag{1.2}
\]

A **componentwise Catalan decoration** of `F` consists of selected `A`- and
`B`-occurrences such that:

1. over all components, the selected `A`-turn colours enumerate
   `binom(Omega,m+1)` exactly once;
2. over all components, the selected `B`-turn colours enumerate
   `binom(Omega,m-2)` exactly once; and
3. on every component containing a selected occurrence, consecutive
   selected occurrences in cyclic order have opposite shore types.

A component with no selected occurrence is called unmarked.  On a marked
component, deleting the selected positions leaves even paths and therefore
a unique residual perfect matching.  On an unmarked even cycle choose either
of its two alternating perfect-matching phases.

For a marked component, encode selected positions by a cyclic binary word.
Condition 3 makes every positive zero-run even.  If the word contains at
least one zero, call the component **linear** when its trace is not on the
unique cycle face

\[
 \text{every positive zero-run has length }2,
 \qquad\text{every one-run has odd length}.
\tag{1.3}
\]

Equivalently, such a marked component is linear when some positive zero-run
has length at least four or some maximal one-run has even length.

A **wholly marked** component is not linear.  Its two turn families lift to
the two disjoint rail cycles, so applying (1.3) vacuously to its absent
zero-runs is unsound.  An unmarked component is linear by convention: its
residual phase lifts to disjoint cross edges.

More precisely, if \(\beta(w)\) is the cycle rank contributed by one factor
component with trace \(w\), then

\[
\beta(w)=
\begin{cases}
0,&w=0^{2q},\\
2,&w=1^{2q},\\
1,&0<|w|_1<2q,\ \text{every zero-run has length }2
                  \text{ and every one-run is odd},\\
0,&\text{otherwise}.
\end{cases}
\tag{1.4}
\]

Thus the global physical lift is a forest exactly when every component has
cycle rank zero.  Without this restriction its number of physical connected
components is

\[
                  \operatorname{Cat}_m+\sum_C\beta(w_C).
\tag{1.5}
\]

## 2. Exact factor-to-diamond theorem

### Theorem 2.1

Every componentwise Catalan decoration of `F` determines a perfect matching
of the Boolean diamond graph between ranks `m-1` and `m+1` on
`Omega union {infinity}`.  If every factor component is linear, its Johnson
lift is a spanning linear forest with exactly `Cat_m` path components.

#### Proof

Apply the decorated-cycle construction on every marked component.  A
selected `A_i` supplies the diamond from lower colour `A_i` to upper turn
colour `u_i`; a selected `B_j` supplies the diamond from
`infinity+ell_j` to `infinity+B_j`; and every residual factor edge supplies
its cross diamond.  On an unmarked component use the chosen residual phase,
so every occurrence there is used by exactly one cross diamond.

The selected turn colours are globally bijective by Conditions 1--2.
Every unselected lower and upper occurrence is used exactly once by the
componentwise residual matching.  Hence every vertex on both diamond shores
is matched exactly once.

The physical lift is the disjoint union of the lifts contributed by the
factor components.  On a partially marked component, the binary-trace
calculation is local to that cycle: it has a physical cycle exactly in the
case (1.3), and otherwise every physical component is a path.  A wholly
marked component would instead give the two rail cycles and is excluded by
the definition of linearity.  On an unmarked component the chosen cross
phase is a matching, hence also a linear forest.  Therefore the global lift
is acyclic and has maximum degree at most two.

The diamond matching has

\[
 \binom{2m}{m-1}
 =\binom{2m}{m}-\operatorname{Cat}_m
\]

edges on `binom(2m,m)` physical vertices.  Euler's identity therefore gives
exactly `Cat_m` path components.  ∎

### Corollary 2.2

The Decorated Middle Levels 2-Factor Theorem implies the Catalan Linear
Matching Theorem.

This implication uses no component merging, Hamilton voltage, gluing tree,
owner alignment, or occurrence router.

### Proposition 2.3 (the all-marked exception is necessary)

At `m=3`, delete from `ML(5)` the perfect matching

```text
(3,7) (5,13) (6,22) (9,25) (10,11)
(12,14) (17,19) (18,26) (20,21) (24,28).
```

The remaining 2-factor has two components of order ten.  Mark every
occurrence of the component

```text
A: 3,9,12,20,18
B: 11,13,28,22,19
```

and leave the other component unmarked.  The selected lower colours are
`1,2,4,8,16`, and the selected upper colours are `15,23,27,29,30`, so both
global palettes are exact and the selected shore types alternate.  The
all-one trace `1111111111` fails (1.3) only because its sole one-run is even,
and hence the old wording called it linear.  Its lift nevertheless contains
two 5-cycles, one on each physical rail; the unmarked component contributes
five disjoint cross edges.  Thus the perfect-diamond conclusion survives,
but the forest conclusion requires the explicit wholly-marked exclusion.

## 3. Exact post-glue/rethread quantifier

### Theorem 3.1

Let `F_0` be any spanning 2-factor of `ML(2m-1)`.  The following are
equivalent.

1. Some spanning 2-factor `F_*` has a componentwise Catalan decoration with
   every component linear.
2. A finite packet of alternating circuits transforms `F_0`, through
   spanning 2-factors, into such an `F_*`.

#### Proof

For `1 -> 2`, colour `F_0 minus F_*` red and `F_* minus F_0` blue.  At every
vertex the red and blue degrees agree.  Pair unlike half-edges and follow
the pairings to decompose the symmetric difference into edge-disjoint closed
alternating circuits.  Toggling them successively preserves degree two and
ends at `F_*`.  The reverse implication reads the terminal state.  ∎

Ordinary Middle Levels Hamiltonicity supplies a permissible `F_0`, but its
connectivity is irrelevant after this point.

## 4. Revised hierarchy of central targets

The exact logical order is now

\[
\begin{array}{c}
\text{transparent leaf-peelable decorated Hamilton recursion}
\\ \Downarrow\\
\text{decorated Hamilton cycle with linear trace}
\\ \Downarrow\\
\text{componentwise decorated 2-factor with linear traces}
\\ \Downarrow\\
\text{Catalan Linear Matching}.
\end{array}
\tag{4.1}
\]

The last implication is Theorem 2.1.  None of the reverse implications is
asserted.

This correction changes the central research target within the
middle-levels trace architecture: the canonical MMM factor or another
recursively supplied 2-factor may be decorated directly, possibly after
alternating-circuit rethreading, without ever being merged to one Hamilton
cycle.  The raw project-`m=5` factor still shows that a fixed canonical
factor need not be decorable; terminal 2-factor existence remains open in
general.

## 5. Scope for the full word theorem

Even a proof of the Decorated Middle Levels 2-Factor Theorem would settle
only Catalan Linear Matching.  The equality `nu(k)=B(k)` additionally needs
one chronology satisfying strict residence, every deeper upper shadow,
protected seams/voltage where used, and the integral lower compiler.  Those
are the downstream RSB rows and are not consequences of Theorem 2.1.

## 6. Audit

The literal counterexample and its complete diamond lift are replayed by

```text
python3 scratch/audit_catalan_decorated_two_factor_all_marked_boundary_20260731.py
```

The replay verifies the spanning 2-factor, both global palettes, the
15-edge perfect diamond matching, five unmarked cross edges, and the two
physical 5-cycles.  It also checks the exact local cycle-rank formula on all
24,457 componentwise-alternating traces of lengths 6,8,...,20.  Its payload
SHA-256 is

```text
1dddf4bfc31ef055a7a30c3733b598149fc9b4a392f468d1a8d44c25294d645d
```

# Protected coloured rotors: fusion curvature and the saturated-hinge one-copy obstruction

**Date:** 2026-08-02  
**Lane:** A, integral coloured-rotor fusion  
**Status:** exact protected-switch calculus, smallest abstract protected
component obstruction, sharp four-port residence obstruction, and an exact
one-copy obstruction for the currently used literal hinge rectangles.  No
all-`k` rounding, protected Hamilton cycle, or `B(k)+O(1)` claim is made.

## 1. Scope and corrected fractional input

The only stationary-clock input admitted here is
`MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`, whose ratio
directions are

\[
 \frac{A_\delta}{A_{\delta+1}}\ge \rho,
 \qquad
 \frac{\Delta_{j+1}}{\Delta_j}\le \rho,
 \qquad \theta=\rho^{-1}.
\]

That theorem proves fractional clockability.  Nothing below rounds an
average over several owner/chain tables.  We instead start with one integral
owner/target/state-exact selector and ask when its Euler components may be
fused while residence and upper interfaces are protected.

## 2. Exact protected `q`-switch criterion

Let `F` be a rainbow directed cycle cover on a tail bank `J`, head bank `I`,
and owner colours `Omega`.  An arc `j->i` has owner colour `kappa(j,i)`.
In addition let `P` be a finite bank of **arc-local or occurrence-localized**
protected resource rows.  Write `m_F(p)` for the current load of `p` and
`b_p` for its required load.  A context-dependent interval witness is not
arc-local until it has been assigned a named occurrence/macro or its complete
old/new chronology is replayed.

Choose selected arcs

\[
                    e_t=j_t\longrightarrow i_t
                    \qquad(1\le t\le q)                 \tag{2.1}
\]

and a `q`-cycle `sigma`.  Replace them by

\[
                    e_t^+=j_t\longrightarrow i_{\sigma(t)}. \tag{2.2}
\]

For each protected row put

\[
 r_Q(p)=\#\{t:e_t\hbox{ supplies }p\},\qquad
 a_Q(p)=\#\{t:e_t^+\hbox{ supplies }p\}.               \tag{2.3}
\]

Any nonadditive residence/history requirement is evaluated on the complete
old and new port matchings, using the retained fragments as fixed data.

### Theorem 2.1 (protected rainbow fusion)

The switch (2.2) is an exact protected fusion if and only if

1. every new arc exists;
2. its owner-colour multiset is unchanged,

   \[
   \{\!\{\kappa(j_t,i_{\sigma(t)}):t\}\!\}
    =\{\!\{\kappa(j_t,i_t):t\}\!\};                   \tag{2.4}
   \]

3. every protected load satisfies its declared row after the literal update

   \[
                    m'_F(p)=m_F(p)-r_Q(p)+a_Q(p);       \tag{2.5}
   \]

   in particular, a lower-bound coverage row requires `m'_F(p)>=b_p`, an
   exact-load row requires equality, and a capacity row requires its declared
   upper inequality;
4. the new finite port/history state is accepting, including complete
   chronology replay for every context-dependent upper witness not already
   localized in item 3.

When the cut arcs lie on `q` distinct cycles, these conditions fuse the
`q` cycles into one while retaining exact tail, head, owner and protected
rows.

#### Proof

The new arcs permute the old heads, so every tail and head row is unchanged.
Equation (2.4) is exactly the owner row.  Equation (2.5) is the literal load
identity for every arc-local or occurrence-localized resource, and its
declared acceptance relation gives item 3.  All remaining changed
residence/history and context-dependent witness information meets the
replayed port chronology, so item 4 is necessary and sufficient for those
rows.  Cutting one arc on each input cycle and reconnecting their paths by a
`q`-cycle yields one output cycle.
\(\square\)

In particular, a tight localized lower-bound row `m_F(p)=b_p` with
`r_Q(p)>a_Q(p)` is an exact obstruction.  This includes a unique upper
witness only after its occurrence has been localized or after the complete
chronology replay certifies that no replacement witness is created.

## 3. Protected curvature and the exact coboundary criterion

Suppose a Cartesian arc menu `A x H` carries an additive protected signature

\[
                         s:A\times H\longrightarrow G,  \tag{3.1}
\]

where `G` is an abelian group.  For a rectangle define its mixed curvature

\[
 \partial s(a,a';h,h')=
 s(a,h)+s(a',h')-s(a,h')-s(a',h).                       \tag{3.2}
\]

### Theorem 3.1 (zero curvature iff every head permutation is transparent)

The following are equivalent.

1. Every finite permutation of heads among distinct tails preserves the
   total signature.
2. Every `2x2` rectangle has `partial s=0`.
3. There are functions `alpha:A->G` and `beta:H->G` such that

   \[
                              s(a,h)=\alpha(a)+\beta(h). \tag{3.3}
   \]

#### Proof

Item 1 implies item 2 by applying one transposition.  Item 3 makes every
head permutation telescope.  For `2=>3`, fix `a_0,h_0` and put

\[
 \alpha(a)=s(a,h_0),\qquad
 \beta(h)=s(a_0,h)-s(a_0,h_0).
\]

Equation (3.2) with `(a,a_0;h,h_0)` gives (3.3). \(\square\)

Thus a common additive upper/compiler interface may be ignored under every
head permutation only after a literal coboundary proof.  For role-indexed
signatures `s_i`, rolewise zero curvature is not enough: universal
cross-role head permutation requires, on each connected compatibility
class,

\[
                         s_i(a,h)=\alpha_i(a)+\beta(h)  \tag{3.4}
\]

with one common head potential `beta`.  The exact graph-theoretic criterion
is zero alternating signature sum around **every** cycle of the
role-tail/head compatibility graph.  Compatible cross-role `2x2` mixed
curvatures suffice only when those cycles are generated by rectangles (for
example on one full common Cartesian menu).  A chordless alternating
six-cycle shows that bare `2x2` tests may otherwise be vacuous while global
holonomy is nonzero.  Nonzero cycle holonomy obstructs **universal
signature-transparent permutation**; a particular switch may still have
zero net change or survive by resource slack.  Coverage rows with slack are
governed by the declared version of (2.5), not by equality of the complete
signature vector.

## 4. Smallest protected component obstruction

Take tails, heads and states all equal to `{0,1}` and allow every arc.  Give
arc `j->i` owner colour `T_j`, so every tail--head perfect matching uses each
owner exactly once.  Require one protected resource `p`, supplied only by
the arc `0->0`.

The identity cover

\[
                         0\to0,\qquad1\to1              \tag{4.1}
\]

is an exact one-copy selector with two Euler components and covers `p`.
The only connected selector is

\[
                         0\to1,\qquad1\to0,              \tag{4.2}
\]

which remains tail/head/owner exact but has load zero on `p`.

### Theorem 4.1 (minimality)

The system (4.1)--(4.2) is a global protected-connectivity obstruction,
not merely a failure of one chosen switch basis.  It is minimal in common
shore cardinality and in the number of protected rows.

#### Proof

There are only two permutations on two states.  The disconnected one is
(4.1) and the connected one is (4.2), so no protected connected selector
exists.  With one state the unique selector already has one component.
With no protected row, (4.2) is feasible. \(\square\)

This example is deliberately abstract: it proves that one-copy rounding and
protected fusion are logically distinct.  It is not asserted to be a
central-slice Boolean interval-OR instance.

## 5. A sharp literal residence-port obstruction

The obstruction above has a literal binary-history analogue.  Fix a minimum
positive-run length `L>=3`.  At four cut ports let the positive terminal
fragment lengths for one coordinate be

\[
                         (1,L-1,L-1,1).                  \tag{5.1}
\]

Let the old matching pair the first with the second and the third with the
fourth.  Its two affected run lengths are `(L,L)`.  Let the component-fusing
crossed matching pair first with fourth and second with third.  Its affected
run lengths are

\[
                              (2,2L-2).                  \tag{5.2}
\]

The first is short.  All other coordinates and all internal fragment runs
may be held fixed.

### Proposition 5.1 (sharpness at `L=3`)

For threshold three, `(1,2,2,1)` is the minimum-total-positive-mass
four-port certificate in which both old joined runs are safe and one crossed
run is short.

#### Proof

A crossed sum below three has two positive integer summands, hence is
`1+1`.  Each of those two unit fragments is paired safely in the old
matching, forcing both opposite fragments to have weight at least two.
The total is therefore at least six, attained by `(1,2,2,1)`. \(\square\)

This is a literal binary retained-fragment/residence obstruction.  It is
not, by itself, a rank-uniform Boolean owner-table counterexample: the
Johnson owner and palette rows must still be supplied by the ambient atlas.

## 6. The saturated-state one-copy obstruction

There is a separate obstruction before component fusion.

Let a flat rank-`r` depth-`d` chronology be a word of nonempty letters
`(...,B_0,...,B_d,...)` in which every consecutive `(d+1)`-letter union is
a rank-`r` owner and every owner is used at most once.

### Lemma 6.1 (saturated `d`-state forces an owner repeat)

If

\[
                         \bigcup_{i=0}^{d-1}B_i=T,
                         \qquad |T|=r,                   \tag{6.1}
\]

then the owner ending at `B_(d-1)` and the owner ending at `B_d` are both
`T`.  Consequently such a state cannot occur internally in a flat one-copy
chronology.

#### Proof

The later owner is `T union B_d`.  Rank `r=|T|` forces `B_d subseteq T`, so
the **later owner** equals `T`; the letter `B_d` need not equal `T`.  The
earlier owner contains the same saturated `d`-state union `T` and is also
constrained to rank `r`, hence it too equals `T`.
Equivalently, applying the argument to the predecessor letter gives the
same two consecutive occurrences. \(\square\)

Now apply this to the literal rectangles in
`MATH_THEOREM_K_HINGE_RECTANGLE_COLOURED_ROTOR_FLOW_AND_ROOTED_EULER_FUSION_20260802.md`.
For an empty chain, `B_0=T`, so the tail state is saturated.  For
`1<=ell<=d-1`, the fixed middle spine has union `S_ell`, while

\[
                         B_0=(T\setminus S_\ell)\cup A,
                         \qquad A\subseteq S_\ell,
\]

and the middle already contains all of `S_ell`; hence the tail union is
exactly `T` for every rectangle choice.

For `ell=d`, the tail union is instead

\[
                   (T\setminus S_1)\cup A,              \tag{6.2}
\]

so it is saturated exactly when `S_1 subseteq A`.  Thus precisely

\[
                         2^{|S_d|-|S_1|}                 \tag{6.3}

of the `2^{|S_d|}` advertised tail choices are saturated and forbidden
internally by Lemma 6.1; the other full-depth choices escape this particular
obstruction.

### Corollary 6.2 (scope of hinge-TU rounding)

The empty/proper-depth literal hinge rectangles are valid network-flow
menus but cannot be inserted internally, unchanged, into a flat rank-`r`
one-copy chronology.  They may still be used

1. once at an open initial boundary;
2. next to a deliberately non-flat/nonowner sidecar cell; or
3. after replacement by an unsaturated-tail construction.

Therefore TU rounding inside those rectangles does not by itself solve the
one-copy owner problem.  This is an owner-repeat obstruction, independent
of Euler-component fusion or protected curvature.

## 7. Exact separation of the remaining gates

The results give three different failure modes.

1. **One-copy failure:** a saturated internal `d`-state repeats an owner
   before any Euler selection question arises (Section 6).
2. **Protected component failure:** an exact one-copy cover exists, but a
   tight curved interface forbids every connected cover (Section 4), or a
   residence port state rejects the fusing matching (Section 5).
3. **Move-basis failure only:** a particular `2x2` catalogue has no safe
   fusion even though a larger protected `q`-switch or a different exact
   connected cover may exist.  Only Theorem 2.1 applied to the larger move,
   or a global enumeration/min--max theorem, can distinguish this from item
   2.

A positive integral rotor-fusion theorem must therefore supply, on one
common table:

* unsaturated one-copy-compatible tail/head states;
* a rainbow cycle cover;
* a protected fusion hypergraph crossing every nontrivial component
  partition, with (2.5) and the exact residence automaton checked at every
  regenerated prefix; and
* either one final Euler component or a separately proved `O(1)` total
  de Bruijn reset distance.  Merely `O(1)` components still permits
  `Theta(d)` sidecar.

The corrected stationary pull clock proves none of these correlations; it
remains a valid fractional marginal input.

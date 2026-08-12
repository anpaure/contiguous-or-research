# Middle-Levels pull ears: exact gap monoid, prepared-tree descent, and the canonical boundary

**Date:** 2026-08-02  
**Lane:** A, structured positive supply after the closed-packet/Farkas theorem  
**Status:** exact local calculus and an exact conditional two-pull descent
theorem.  The unqualified MMM gluing-tree supply claim is refuted by the
complete `ML(11)` family.  No unconditional growing-depth Middle-Levels
construction is claimed.

## 0. Result

Put

\[
                     k=2r-1,\qquad g=2d+1.
\]

There are four conclusions.

1. A phase-coherent incidence `C6` or `C8` has an exact ear calculus.  Its
   component change is a permutation calculation, and its residence effect
   is the composition of finite capped-age transducers on the retained ears.
   Auxiliary-tree connectivity by itself is not a residence theorem.
2. On a **prepared**, collar-separated pull system, residence debt is a
   graphic edge weight.  A nonminimum gluing tree then has a literal
   two-pull negative accepting path, with peak component debt one.  If a
   zero-debt tree exists, minimum-spanning-tree exchange reaches one.
3. A bounded *total physical* pull packet cannot clean an unbounded incoming
   event-bearing debt.  Put `s_d=min(d,r)`.  If `t6,t8` physical pulls are
   used, then

   \[
      N_d(F')\ge N_d(F)-s_d(3t_6+4t_8),               \tag{0.1}
   \]

   before counting newly born defects.
4. The complete labelled MMM gluing-tree family at `ML(11),d=3` is an exact
   counterexample to the unqualified positive claim.  Its upper-`q1`-exact
   face is nonempty, but its minimum residence debt is `154>0`.  Hence an
   upper-exact minimizer has no negative accepting path whose endpoint stays
   in that full family, regardless of the intermediate path length.

The honest live theorem is therefore **bounded per ear**, not bounded total
support: construct a prepared guarded-ear bank with a zero-weight spanning
tree, or leave the canonical MMM endpoint family by a genuinely noncanonical
rethread.  Deeper upper shadows, literal source factorization, and the common
compiler are not part of this note.

## 1. Oriented factors and the residence potential

Let `F` be a spanning two-factor of the Middle Levels graph on ranks `r-1`
and `r`.  Orient every component and write its flip word with a minus sign
for an upper-to-lower deletion and a plus sign for a lower-to-upper
insertion.  On a projected rank-`r` owner component this is

\[
 T_i\xrightarrow{-p_i}X_{i+1}\xrightarrow{+q_i}T_{i+1}.
                                                               \tag{1.1}
\]

For an insertion `+x`, let the next occurrence of `x` be its necessarily
negative deletion `-x`.  By the exact flip-gap theorem, the corresponding
positive owner run has length at least `d+1` if and only if the forward flip
distance is at least

\[
                              g=2d+1.               \tag{1.2}
\]

Let `N_d(F)` be the number of occurrence-labelled insertion-to-next-deletion
pairs of distance `<g`, over all components.  More generally, let
`Phi_g(F)` be any fixed nonnegative weighting of these event-bearing bad
occurrences.  Let `widehat_Phi_g(F)` additionally include fixed nonnegative
weights for short constant-present whole-component tokens.  The two
potentials agree on a Middle-Levels Hamilton cycle, because no coordinate is
constant on its spanning owner component.

Every lower rank-`(r-1)` vertex of a spanning factor occurs once and lies
between its two selected upper neighbours.  Consequently the projected
immediate-lower palette is automatic, independently of the number of factor
components.  This does not make the rank-`(r+1)` union palette automatic.

## 2. Exact `C_(2s)` ear calculus

Let `s` be `3` or `4`.  Consider a phase-coherent alternating incidence
cycle with lower ports `L_i`, upper ports `U_i`, and indices in `Z_s`.  The
old and new factor matchings on the cycle are

\[
 e_i=L_iU_i,\qquad f_i=L_iU_{i-1}.                  \tag{2.1}
\]

All `e_i` belong to one matching phase of `F`.  Orient each touched factor
component so that its `e_i` edges are traversed from lower to upper.  Delete
the `e_i`.  Starting at `U_i`, the retained oriented path ends at a unique
`L_{rho(i)}`; call it `P_i` and call its signed flip word `w_i`.  Thus `rho`
is a permutation of `Z_s`.  Put

\[
 \pi(i)=i-1,\quad
 \lambda_j=U_j\setminus L_j,\quad
 \mu_j=U_{\pi(j)}\setminus L_j.                    \tag{2.2}
\]

### Theorem 2.1 (literal component and word formula)

The touched old components are the cycles of `rho`.  Their exact words are

\[
 w_i,+\lambda_{\rho(i)},w_{\rho(i)},
 +\lambda_{\rho^2(i)},\ldots .                     \tag{2.3}
\]

After the pull, the touched components are the cycles of

\[
                              \theta=\pi\rho,       \tag{2.4}
\]

and their exact words are

\[
 w_i,+\mu_{\rho(i)},w_{\theta(i)},
 +\mu_{\rho(\theta(i))},\ldots .                   \tag{2.5}
\]

In particular,

\[
             c_{\rm old}=c(\rho),\qquad
             c_{\rm new}=c(\pi\rho).               \tag{2.6}
\]

If the output orientation traverses a retained path backwards, replace

\[
              w=(\epsilon_1x_1,\ldots,\epsilon_tx_t)
\]

by

\[
              w^\dagger=(-\epsilon_tx_t,\ldots,-\epsilon_1x_1). \tag{2.7}
\]

Every internal positive-run gap has the same length in `w` and
`w^dagger`.  Hence a pre-existing short run can change only when its closed
flip interval meets a removed old edge.

#### Proof

After traversing `P_i`, the old edge at `L_{rho(i)}` enters `U_{rho(i)}`;
the next retained path is therefore `P_{rho(i)}`.  The new edge instead
enters `U_{pi(rho(i))}`, so the next retained path is
`P_{pi(rho(i))}`.  This proves (2.3)--(2.6).  Reversing a path reverses the
event order and exchanges insertion with deletion.  A constant-coordinate
owner block is therefore read backwards with the same length, proving the
last assertion.  \(\square\)

For a non-phase-coherent toggle one must not use the parity consequences of
(2.6).  If `alpha,beta` are the old and new port matchings and `gamma` is
the retained-fragment endpoint involution, the general component formula is

\[
 c_{\rm old}=\frac{c(\alpha\gamma)}2,\qquad
 c_{\rm new}=\frac{c(\beta\gamma)}2.                \tag{2.8}
\]

### Lemma 2.2 (insertion counts are invariant)

Write

\[
 \alpha_i=U_i\setminus L_i,\qquad
 \beta_i=U_i\setminus L_{i+1}.
\]

Then

\[
                         \{\!\{\alpha_i\}\!\}
                       = \{\!\{\beta_i\}\!\}.     \tag{2.9}
\]

Thus a phase-coherent pull preserves every coordinate's number of insertion
events; it redistributes run lengths rather than changing the run-count
vector.

#### Proof

Since `U_i` contains both adjacent lower ports,

\[
                  L_{i+1}=L_i-\beta_i+\alpha_i.
\]

Summing these incidence-vector identities around the cycle gives (2.9).
Thus the changed upward phase has the same coordinate-label multiset.  The
retained phase is untouched, and on every cyclic factor component the number
of insertions of a coordinate equals its number of deletions.  Hence the full
insertion-count vector is preserved.
\(\square\)

## 3. The exact capped-age monoid

For positive depth `d`, a boundary state records, for every coordinate `x`,

1. whether `x` is currently present;
2. if present, the flip distance since its last insertion, capped at `g`;
3. one violation bit.

There is also a whole-component token: if `x` is present on an entire factor
component and hence has no signed event there, record that fact and the
component's owner length, capped at `d+1`.

Use the following scan order.  Before processing each later flip, increment
every live age once (capped at `g`), and then process that flip.  An insertion
sets the inserted coordinate's age to zero.  A deletion is legal exactly
when that coordinate's incremented age is at least `g`; it then makes the
coordinate absent.  Illegal signs or a too-early deletion set the violation
bit.  A constant-present whole-component token is legal exactly when its
owner length is at least `d+1`.

Let `tau_g(w)` be the induced map on this finite state space.  This state
decides residence feasibility.  To recover `N_d`, a distance histogram, or
the event-bearing part `Phi_g`, augment the violation bit by the corresponding
counter or occurrence ledger; its update composes by the same scan rule.  The
separate whole-component token then supplies the remaining term of
`widehat_Phi_g`.

### Theorem 3.1 (collar composition)

For literal signed words `u,v`,

\[
                         \tau_g(uv)=\tau_g(v)\circ\tau_g(u).       \tag{3.1}
\]

The cyclic word is positively depth-`d` resident if and only if its actual
cyclic boundary state is fixed by this map with violation bit zero and every
whole-positive component token is legal.
Equivalently, first and last collars of radius `g-1`, together with the
capped open ages, are Markov-sufficient.  No coordinate-free component or
cap summary is sufficient in general.

#### Proof

The age state is exactly the information needed to process the next signed
flip, so induction over the symbols proves (3.1).  If a coordinate has an
event, the cyclic assertion follows by starting in its literal
membership/age state at the cut and scanning once around the component.  If
it has no event, its trace is constant and is decided by the separate
whole-component token.  \(\square\)

For simultaneous positive and negative residence, add the absent-run age,
capped at `2d+3`, use the dual deletion-to-insertion threshold, and add the
constant-absent whole-component token.  Nothing else in the calculus
changes.

### Corollary 3.2 (common-core gap matrix)

Here a **pure merge** means that the `s` old edges lie in `s` distinct
components, so `rho=id`.  Let `x` be present throughout the relevant port
core.  If
`w_i` has length `m` and its last `+x` event is at zero-based position `p`,
put `a_(x,i)=m-p`, the distance from that event to the connector position.
If the first `-x` event of `w_j` is at zero-based position `q`, put
`b_(x,j)=q`.  When those events exist, the old and new crossing gaps are

\[
 g^-_{x,i}=a_{x,i}+1+b_{x,i},\qquad
 g^+_{x,i}=a_{x,i}+1+b_{x,\pi(i)}.                  \tag{3.2}
\]

The exact condition on the new arc `i->j` is

\[
                         a_{x,i}+b_{x,j}\ge 2d       \tag{3.3}
\]

for every persistent core coordinate, plus the direct transducer check for
active seam labels.  A sufficient robust-socket condition, valid for every
re-pairing, is

\[
              \min_i a_{x,i}+\min_j b_{x,j}\ge2d
              \quad\hbox{for every such }x.         \tag{3.4}
\]

Fragments with no `x` event are handled by Theorem 3.1; they cannot be
silently discarded from (3.2).

### Example 3.3 (tree connectivity is not enough)

At `d=6`, take three abstract resident ears and two persistent core
coordinates with boundary arrays

\[
\begin{array}{c|cc}
 &a&b\\ \hline
x&(1,7,11)&(11,5,1)\\
y&(11,5,1)&(1,7,11).
\end{array}                                           \tag{3.5}
\]

The threshold in (3.3) is `12`.  For `x`, the allowed row sets are
`{0},{0,1},{0,1,2}`; for `y`, they are
`{0,1,2},{1,2},{2}`.  Their intersection contains only the three diagonal
arcs.  The three old diagonal closures are resident, but neither nontrivial
three-cycle pairing is resident.

This is an exact occurrence-labelled collar-state counterexample.  Within
each ear the displayed `a`-values are pairwise distinct, as are the
`b`-values; a sufficiently long odd ear realizes the corresponding
insertion and deletion positions with the required parities and without an
occurrence collision.  It is not asserted to be a separately embedded
simple Middle-Levels factor.  Its role is precise: an ordinary connected
gluing graph cannot replace the common-core compatibility row (3.3).

## 4. Exact immediate-palette transport

At lower port `L_i`, let `A_i` be its retained upper factor neighbour.  The
projected rank-`(r+1)` turn colour changes as

\[
                         A_i\cup U_i
                    \longmapsto A_i\cup U_{i-1}.    \tag{4.1}
\]

Therefore the pull is upper-`q1` transparent exactly when

\[
 \boxed{
   \{\!\{A_i\cup U_i:i\in\mathbb Z_s\}\!\}
   =
   \{\!\{A_i\cup U_{i-1}:i\in\mathbb Z_s\}\!\}.}
                                                               \tag{4.2}
\]

This is literal multiset equality, not a degree or support relaxation.  If a
second turn shore is decorated, and `B_i` is the retained lower neighbour of
`U_i`, its separate exact row is

\[
 \{\!\{B_i\cap L_i\}\!\}_{i}
 =\{\!\{B_i\cap L_{i+1}\}\!\}_{i}.                 \tag{4.3}
\]

For the standard incidence hex with

\[
 L_a=H+a,\ L_b=H+b,\ L_c=H+c,
\quad U_{ab}=H+a+b,\ U_{bc}=H+b+c,\ U_{ca}=H+c+a,
\]

write the external neighbours as `A_x=L_x+d_x`.  Because these are
nonhexagon neighbours, legality gives

\[
                         d_x\notin H\cup\{a,b,c\}.   \tag{4.4}
\]

Then (4.2) holds if and only if

\[
                              d_a=d_b=d_c.           \tag{4.5}
\]

This is the exact lower-port union-turn, or projected upper-`q1`, condition.
The complete all-six coherent-hex condition additionally requires the
intersection row (4.3).  For `C8`, (4.2) itself is the required cyclic test.
At shared turns, palette deltas are not additive: the final pair of
neighbours must be replayed.

## 5. Fixed-ear accepting paths

Fix the retained fragment table, the protected incidence bank, and any
exposed ambient collar states.  A pull packet is a closed accepting path for
the present rows if and only if all of the following hold:

1. its final port matching is a legal factor and avoids the protected bank;
2. (2.6), or (2.8), has the required final component count; quotient voltage
   is also returned if the calculation is performed in a quotient;
3. every claimed immediate palette satisfies its literal multiset identity
   (4.2), and (4.3) if applicable;
4. the composed maps from Theorem 3.1 have no violation and return every
   required exposed ambient state, and every whole-component token is legal;
5. the exact killed/born residence ledger has negative total weight.

These conditions are necessary and sufficient on the fixed fragment table:
the component permutation gives topology, the local neighbour pairs give
the immediate palettes, and the signed words give every residence gap.
This is the pull/ear specialization of the lifted-return alternative in the
closed-packet/Farkas theorem.

Replacing exact state equality in item 4 by a separately proved dominance
relation gives a sufficient accepting test, but not the necessary-and-
sufficient characterization just stated.

## 6. Prepared pull-tree descent

Let `H` be a connected auxiliary multigraph whose vertices index the
components of an initial spanning two-factor `F_0`.  Each edge `e` carries a
factor-alternating `C6` or `C8` pull `Z_e`.  For a graphic forest `S`, put

\[
                     F_S=F_0\mathbin\triangle
                         \bigtriangleup_{e\in S}Z_e. \tag{6.1}
\]

Assume:

- **P1 (exact forest semantics).** For every forest `S`, `F_S` is a spanning
  two-factor and

  \[
                          c(F_S)=c(F_0)-|S|.          \tag{6.2}
  \]

- **P2 (protected/exterior return).** Every pull avoids the literal
  protected bank and induces the identity on each designated exterior
  collar state.
- **P3 (optional hereditary upper transparency).** Whenever `S+e` is a
  forest, the exact multiset (4.2) is the same in `F_S` and `F_(S+e)`.
  Moreover, other selected pulls do not alter the external incidences used
  by that equality.  When completeness is claimed, `F_0` has the required
  complete/exact upper-`q1` multiset.
- **P4 (prepared additivity).** There are integers `w_e` such that

  \[
       \widehat\Phi_g(F_S)=\widehat\Phi_g(F_0)+\sum_{e\in S}w_e
                  \quad\hbox{for every forest }S.    \tag{6.3}
  \]

A concrete proof-sufficient form of P4 is: the radius-`(g-1)` oriented pull
collars are mutually context-independent; no other pull changes their
literal collar words; in every forest state `F_S`, no old or born bad
insertion-to-next-deletion interval meets two pull collars; and every
whole-component token is assigned to one context-independent pull collar.
Then every bad token has one pull owner, and (6.3) follows by partitioning
the exact ledger.

### Theorem 6.1 (two-pull negative accepting path)

Every spanning tree `T` of `H` gives a Hamilton cycle `F_T`.  If `T` is not
a minimum-weight spanning tree for the weights `w`, then there are
`f notin T` and an edge `e` on the fundamental `T`-cycle of `f` such that
`w_f<w_e`.  The literal sequence

\[
       F_T\xrightarrow{\ -Z_e\ }F_{T-e}
          \xrightarrow{\ +Z_f\ }F_{T-e+f}           \tag{6.4}
\]

is a two-pull negative accepting path.  Its endpoints are Hamilton cycles;
its intermediate factor has exactly two components.  It preserves the
protected/exterior state, and under P3 it preserves the complete upper-`q1`
multiset at both steps.

If some spanning tree has `widehat_Phi_g=0`, every minimum-weight spanning
tree has `widehat_Phi_g=0`, and repeated fundamental exchanges from any
nonminimum tree reach a `g`-long-run Hamilton cycle.

#### Proof

Equation (6.2) gives one component at every spanning tree and two at
`T-e`.  The standard minimum-spanning-tree cycle criterion gives an
improving fundamental exchange whenever `T` is nonminimum.  By (6.3), its
residence change is `w_f-w_e<0`.  P2 and P3 give the remaining returned
resources.  Finally `widehat_Phi_g` is nonnegative, so the existence of a
zero tree forces the minimum possible value to be zero.  Repeated strict
integral weight decreases terminate at a minimum tree.  \(\square\)

This is the requested structured positive supply theorem.  It is conditional
on the literal forest/protection hypotheses and, crucially, on prepared
additivity plus existence of a zero-weight tree.  Neither ordinary
pull-graph connectivity nor the terminal leaf-shuttle theorem supplies those
last two facts.  In a quotient, unit voltage must additionally be part of the
accepting state or repaired by an exact parallel label; it is not implied by
the graphic exchange.

The graphic theorem is not a disguised phase-coherent `C6` theorem.  By
(2.6), a phase-coherent `C6` changes the component count by an even number,
whereas one graphic-tree edge in P1 changes it by one.  Canonical
two-component MMM glues use the general port-involution case (2.8).  A
phase-coherent ternary `C6` system instead needs a rank-two hypergraphic
analogue of Theorem 6.1.

## 7. Why bounded total support cannot be the all-dimension theorem

### Theorem 7.1 (event-bearing short-gap hitting bound)

Suppose a sequence uses `t6` physical incidence `C6` pulls and `t8` physical
incidence `C8` pulls.  For event-bearing defects, (0.1) holds.  In
particular, eliminating every old event-bearing defect requires

\[
                 3t_6+4t_8\ge
        \left\lceil\frac{N_d(F)}{\min(d,r)}\right\rceil.          \tag{7.1}
\]

#### Proof

A bad run of owner length `ell<=d` has the closed flip-edge interval from its
insertion through its next deletion.  Its `2ell` positions begin at an
insertion-parity position.  A fixed flip position lies in at most `d` such
intervals: their insertion endpoints are among the `d` insertion-parity
positions in the preceding `2d` positions.

Consider an original bad interval and the first pull in the sequence that
changes it.  Until that pull, all its original edges remain consecutive,
possibly with the entire containing fragment reversed.  Theorem 2.1 says
that such reversal preserves its length.  Therefore the first changing pull
must delete an original edge of the interval.  A `C6` deletes three old
factor edges and a `C8` deletes four.  Charging each destroyed original
interval to its first deleted edge proves that at most
`d(3t6+4t8)` old intervals are destroyed.  A flip edge `X\subset T` also
lies in positive collars only for coordinates of its rank-`r` upper endpoint
`T`, giving the alternative coefficient `r`.  Taking the smaller coefficient
proves (0.1).  Newly born bad intervals can only increase `N_d(F')`.
\(\square\)

The theorem deliberately counts signed-event intervals.  If a factor state
has a short component on which a coordinate is constant-present, that
whole-component token must be charged separately; the per-edge load `d`
need not bound such tokens.  The Hamilton-cycle application below has no
constant-coordinate component, so this qualification does not change its
numbers.

For the authenticated canonical `ML(17)` cycle,

\[
                       r=9,\quad d=3,\quad N_3=7293.
\]

Thus any physical `C6/C8`-only cleaning sequence satisfies

\[
                         3t_6+4t_8\ge2431.           \tag{7.2}
\]

Pure `C6` needs at least `811` pulls and pure `C8` at least `608`.  A fully
`Z_17`-developed quotient operation contains up to `17` physical copies, so
the corresponding safe lower bounds are `48` developed `C6` operations or
`36` developed `C8` operations.  The statement is a support lower bound,
not a proof that those many pulls suffice.

Consequently no dimension-uniform bounded **total physical** packet repairs
every high-debt input.  The viable recurrence in Theorem 6.1 uses bounded
support per gluing-tree exchange while allowing the number of ears or
exchanges to grow.

## 8. Exact canonical-family counterexample

The exhaustive `ML(11)` audit uses all `13` labelled MMM gluing pairs on the
six plane-tree components, every labelled spanning tree whose simultaneous
symmetric difference is quotient-Hamilton, every parallel-edge label, and
every unit-voltage lift.  Its exact counts are

\[
 74\text{ quotient-Hamilton tree occurrences},\quad
 1496\text{ parallel-labelled variants},\quad
 1360\text{ unit-voltage lifts}.                    \tag{8.1}
\]

The global residence minimum is `143`.  The six upper-`q1`-exact endpoints
have the complete profile

\[
 (154,\operatorname{lo2miss}=11)^2,\qquad
 (165,0)^2,\qquad
 (165,11)^2.                                        \tag{8.2}
\]

### Corollary 8.1 (no accepting descent inside the full MMM face)

Choose an upper-`q1`-exact endpoint of residence debt `154`.  There is no
negative path, of any length and with arbitrary temporary component or
palette debt, whose endpoint is another unit-voltage member of the complete
labelled MMM gluing-tree/parallel-label family with upper `q1` restored.
If lower `q2` is also protected, the analogous minimum is `165`.

#### Proof

Equation (8.2) is an exhaustive list of the accepting endpoint face.  Its
minimum residence debts are `154` and `165`, respectively.  No endpoint in
the face has smaller debt.  \(\square\)

This is stronger than failure of one greedy pull: it closes every return
path whose endpoint remains in the canonical family.  It does **not** close
arbitrary incidence `C8` rethreads or composite circuits leaving that
family; the known exact `k=11` carrier lies outside it.

There is also an all-dimension upper-palette boundary.  To avoid conflict
with this note's rank parameter, write `n` for the lexical paper parameter,
whose ground size is `2n+1`, and put

\[
 M_n={2n-1\choose n-3}-{2\over n-1}{2n-2\choose n-3}.             \tag{8.3}
\]

For `n>=11`, at most `Cat_n-1` canonical pulls leave at least

\[
 M_n-3(\operatorname{Cat}_n-1)>0                    \tag{8.4}
\]

projected upper colours missing.  Therefore a prepared recurrence carrying
upper `q1` exactly must start from a different upper-complete factor or use
noncanonical edits satisfying (4.2); the canonical lexical pull tree cannot
instantiate P3 for all dimensions.

## 9. The exact surviving target

One unconditional infinite family survives only at fixed depth one.  Every
Middle Levels Hamilton cycle has insertion-to-next-deletion distance at
least `3`: a length-one positive run would put the same lower vertex
`T\setminus{x}` on both sides of its unique upper owner `T`, contradicting
Hamiltonicity.  This does not scale to `d=d(k)`.

For growing depth, the weakest exact missing theorem is now:

> Construct, for every required dimension, a protected pull-ear system
> satisfying P1--P4 and containing a zero-weight spanning tree; or construct
> a rank-weighted hypergraphic guarded-ear recurrence whose capped-age and
> whole-component transducers have an accepting root.

The terminal leaf-shuttle theorem proves only connectivity of the component
pull graph.  Example 3.3 proves why that is insufficient.  Upper `q1` may be
carried only through the literal local identity (4.2).  Deeper upper decks,
source words, erosion, and the common compiler remain separate accepting
coordinates and are not inferred here.

## 10. Frozen provenance

The exact inputs used here are:

- `MATH_THEOREM_LONG_RUN_MIDDLE_LEVELS_RESIDENCE_REDUCTION_20260802.md`,
  SHA-256
  `96adc61fe19bb1eed12c503baa7facdbbbf0d51331573822112cace97104e2de`;
- `MATH_AUDIT_MMM_GLUING_SWITCH_PARAMETRIZATION_20260729.md`, SHA-256
  `2c544f7fa5b14fb63b1d2428cc14a5bb88976491b653c6ada61e22394aae3c66`;
- `scratch/extract_mmm_gluing_family.py`, SHA-256
  `f54d3840221857e02be4c82574704ee3e4a4884ae213c0728c30ba8010fafe67`;
- `scratch/threadA_ml11_mmm_upper_exact_endpoint_profile_20260802.audit.json`,
  SHA-256
  `06ad984d9aff6c4d5fdcfe9f49e36b351c1ca1f424c28924fc0367e56216e0c1`;
- `MATH_THEOREM_CATALAN_COHERENT_ALLSIX_TRANSPARENT_HEX_20260731.md`,
  SHA-256
  `3c4a3254f12acd8cf44cad8a9b4086f4e7e34d00bd325c26deaa5794f51228b1`;
- `MATH_THEOREM_CATALAN_TERMINAL_LEAF_SHUTTLE_CONNECTIVITY_20260731.md`,
  SHA-256
  `1577eecdcd3a388fa8a9f4a9cde5ddbc83f386f24ad8203984794b3c247caeee`;
- `MATH_AUDIT_K17_CANONICAL_MIDDLE_LEVELS_LONG_RUN_NOGO_20260802.md`,
  SHA-256
  `928904a6b92b7037ea37e389d6a275a074533a03caa741c69117d6bf4cf7b73d`;
- `MATH_AUDIT_K_R_LEXICAL_GMN_UPPER_OBSTRUCTION_20260801.md`, SHA-256
  `2059d3626fe2716b2bc246d58fa9482177c41bceab09decd7b88c4d195895bfb`;
- `MATH_THEOREM_A_BOOLEAN_RESIDENCE_CLOSED_PACKET_EXPANSION_AND_LIFTED_RETURN_DUALITY_20260802.md`,
  SHA-256
  `4276732389249fafa169cc01137c4be9702f947ee7679f2dbafaa8486cffe9cd`.

No claim in this note uses arbitrary circuit degree, average cap abundance,
or an unproved independence approximation.

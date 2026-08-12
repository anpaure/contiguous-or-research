# Named fragmentation: the collar-start Rado gate and a small freed-socket lift

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact named-containment formulation, an exact
co-selected collar-start matroid theorem, and an unconditional lift for a
small exceptional freed-socket bank.  Complete-layer bulk batches lift by
the existing joint-start orbit theorem.  A general anonymous interval
fragmentation still requires one correlated choice of its named interval
lift and its collar-start Rado transversal.

## 0. Outcome

Work in `B_(2r)`.  Let the new depth be

\[
                         D^+=D+1,
 \qquad
                         b=r-D^+.
\tag{0.1}
\]

Thus `b=t-1` in the one-depth-shift theorem.  A collar chain starting at
rank `u`, `b<=u<=r`, has marked collar load `r-u` and residual capacity

\[
 \mathcal B_s=\binom{[2r]}s,
 \qquad
 C_s=|\mathcal B_s|,
 \qquad
 H_s=C_s-C_{s-1}.
\tag{0.1a}
\]

\[
                         c^+(u)=D^+-(r-u)=u-b.
\tag{0.2}
\]

The note proves four facts.

1. Once a named residual interval fragmentation and a named collar bank
   are fixed, the lift is exactly the obvious bipartite Hall graph:
   chunk top contained in socket bottom, with the load bound.

2. If the collar is co-chosen, its legal start sets at rank `u` are the
   bases of the dual of one Boolean inclusion-transversal matroid.  Across
   all collar ranks, named attachment is exactly a Rado transversal with
   cuts

   \[
                         r_{\mathsf K}(N(X))\ge |X|.
   \tag{0.3}
   \]

3. Every set of at most `r` prescribed starts at one collar rank is
   independent in this start matroid.  Consequently any exceptional bank
   with at most `r` chunks assigned to each allowed start rank has an exact
   named lift.  In particular an `O(D)` exceptional bank is harmless for
   `D=Theta(sqrt(r))`.

4. The same small-bank construction can be made genuinely
   **freed-socket faithful** across the depth shift.  One co-chooses old
   singleton residual jobs and short-collar occurrences so that the old
   singleton occupies the socket and the new exceptional chunk occupies
   the same occurrence after its capacity rises by one.

This separates the easy exceptional bank from the bulk.  The interval
Boolean lift names any fixed interval schedule, and the complete-layer
joint-start theorem closes every Rado cut on its symmetric face.  For a
general configuration-rounded interval schedule, however, choosing the
named interval chains and the start transversal simultaneously is still a
variable-bank correlation problem; normalized matching alone does not
round it.

## 1. The exact fixed-bank Hall graph

Let `mathcal R` be a family of pairwise target-disjoint named residual
chunks below rank `b`.  Every `F in mathcal R` is a strict inclusion chain;
write

\[
                         S_F=\operatorname{top}(F),
 \qquad
                         \ell_F=|F|.
\tag{1.1}
\]

Let `mathcal C` be a fixed named collar chainization from ranks `b` through
`r`.  A **socket occurrence** is a collar chain `D` starting at rank
`u_D>b`; write

\[
                         T_D=\operatorname{bot}(D),
 \qquad
                         c(D)=u_D-b.
\tag{1.2}
\]

Make the bipartite graph

\[
                         \Gamma=(\mathcal R,\mathcal C;E)
\tag{1.3}
\]

with

\[
 F\sim D
 \quad\Longleftrightarrow\quad
 S_F\subset T_D
 \quad\text{and}\quad
 \ell_F\le c(D).
\tag{1.4}
\]

### Theorem 1.1 (fixed-bank named fragmentation Hall theorem)

Every residual chunk can be attached to a different fixed socket
occurrence if and only if

\[
                         |N_\Gamma(X)|\ge |X|
                         \qquad(X\subseteq\mathcal R).
\tag{1.5}
\]

#### Proof

This is Hall's theorem.  For a matched edge, every member of `F` is below
`S_F`, which is below `T_D`, and every member of `D` is above `T_D`.
Therefore `F union D` is one named inclusion flag.  Its marked load is

\[
                         \ell_F+(r-u_D)\le D^+
\]

exactly when `ell_F<=u_D-b=c(D)`.  Different chunks use different socket
occurrences and hence distinct collar chains and owners.  Conversely every
such attachment is a matching in (1.3).  \(\square\)

Theorem 1.1 is the exact graph requested after the two named banks are
fixed.  The real freedom in the one-depth argument is that the collar SCD
and hence the socket bottoms need not be frozen first.

## 2. Co-choosing the collar: the start matroid

For `b<u<=r`, let `G_u` be the Boolean inclusion graph

\[
                         \mathcal B_{u-1}\longleftrightarrow
                         \mathcal B_u.
\tag{2.1}
\]

Let `mathsf M_u` be the transversal matroid on ground `mathcal B_u`
represented by the left shore `mathcal B_(u-1)`.  It has rank
`C_(u-1)`.  Define the **start matroid**

\[
                         \mathsf K_u=\mathsf M_u^*.
\tag{2.2}
\]

Its rank is

\[
                         h_u=C_u-C_{u-1}.
\tag{2.3}
\]

A set `Z_u subseteq mathcal B_u` is a base of `mathsf K_u` exactly when
`mathcal B_u setminus Z_u` is the image of a matching saturating
`mathcal B_(u-1)`.  In that case the members of `Z_u` are precisely the new
collar-chain starts at rank `u`.

At the bottom rank `u=b`, put `mathsf K_b` equal to the free matroid on
`mathcal B_b`; every bottom set starts a chain.  Let

\[
                         \mathsf K=\bigoplus_{u=b}^r\mathsf K_u
\tag{2.4}
\]

on the disjoint rank-tagged union of the collar layers.

For `F in mathcal R`, define its candidate start set

\[
 N(F)={(u,T): b+\ell_F\le u\le r,
                     S_F\subset T\in\mathcal B_u}.
\tag{2.5}
\]

The inequality on `u` is exactly the load condition.

### Theorem 2.1 (collar-start Rado theorem)

There is a collar-saturated named chainization which attaches every
residual chunk in `mathcal R` if and only if

\[
 \boxed{
                         r_{\mathsf K}(N(X))\ge |X|
                         \qquad(X\subseteq\mathcal R),}
\tag{2.6}
\]

where `N(X)=union_(F in X)N(F)`.

#### Proof

Rado's theorem says that (2.6) is equivalent to an injection

\[
                         \mu:\mathcal R\longrightarrow
                         \mathop{\dot\bigcup}_{u=b}^r\mathcal B_u
\tag{2.7}
\]

with `mu(F) in N(F)` and image independent in `mathsf K`.

Assume such an injection.  At each rank `u`, extend the selected independent
set `Q_u` to a base `Z_u` of `mathsf K_u`.  For `u>b`, the complement
`mathcal B_u setminus Z_u` is a base of `mathsf M_u`, so choose a matching
from every rank-`u-1` set to that complement.  Start a new collar chain at
every member of `Z_u`.  Beginning with all rank-`b` sets and proceeding
upward, this gives exactly one chain ending at every set of every collar
rank and at every owner in rank `r`.

If `mu(F)=(u,T)`, attach `F` below the collar chain starting at `T`.
Containment and the depth bound follow from (2.5).  Injectivity gives
distinct starts and owners.

Conversely, in any collar-saturated chainization the complete start family
`Z_u` is a base of `mathsf K_u`.  The starts occupied by residual chunks
form an independent subset, and the attachment edges give the Rado
injection (2.7).  \(\square\)

For later use, the exact rank formula is

\[
 r_{\mathsf K_u}(A)
 =|A|+r_{\mathsf M_u}(\mathcal B_u\setminus A)-C_{u-1}.
\tag{2.8}
\]

Thus (2.6) is a finite, literal all-cut theorem.  It is stronger than
ordinary Hall because the chosen socket bottoms must simultaneously be
extendable to one collar chain forest.

## 3. Where normalized orbit lifting does close the gate

When the residual bank is a disjoint union of occurrence-labelled copies
of complete Boolean layers, with one declared load per type, the
joint-start orbit theorem constructs a uniform fractional matching whose
right loads are exactly the type-table loads.  Bipartite integrality then
chooses the continuations and residual starts jointly.  In the language of
Theorem 2.1, the feasible surplus table proves every Rado cut (2.6).

Likewise, once a rank-interval schedule below `b` has been fixed, the
interval-histogram Boolean lift names it as target-disjoint literal chains.
For such a named lift, Theorem 2.1 is the exact remaining containment
test.

The order of quantifiers matters:

\[
\begin{array}{c}
 \text{complete-layer batches + feasible surplus table}
 \Longrightarrow \text{named lift},\\[1mm]
 \text{arbitrary anonymous interval fragmentation}
 \Longrightarrow
 \exists\text{ named interval lift satisfying (2.6)}
 \quad\text{is not proved.}
\end{array}
\tag{3.1}
\]

The second line simultaneously chooses which literal set occupies each
interval row and which collar start it uses.  The target-once rows across
those choices are exactly the variable-bank correlation which produces the
determinant-two minors in the variable-slot audit.  Those minors do not
disprove the dense Boolean instance, but they rule out a generic appeal to
network or bipartite total unimodularity.

## 4. Protected-top independence of small start banks

The start matroids have a large exact local girth.

### Proposition 4.1 (every `r` prescribed starts are legal)

For every `u<=r`, every family

\[
                         Q\subseteq\mathcal B_u,
 \qquad
                         |Q|\le r,
\tag{4.1}
\]

is independent in `mathsf K_u`.

#### Proof

For `u>b`, apply the protected-top reserve theorem to the inclusion graph
from rank `s=u-1` to rank `u` on `k=2r` points.  Its parameters are

\[
                         a=2r-u+1,
 \qquad
                         b'=u.
\]

The reserve is

\[
 \eta_{u-1}=\left\lfloor\min\left\{
 2r-u,
 {(2r-2u+1)(2r-u)^2\over u}
 \right\}\right\rfloor.
\tag{4.2}
\]

The first term is at least `r`.  For the second,

\[
 2r-2u+1\ge1,
 \qquad 2r-u\ge r,
 \qquad u\le r,
\]

so it too is at least `r`.  Hence `eta_(u-1)>=r`.  Deleting `Q` leaves a
matching saturating `mathcal B_(u-1)`, which is exactly independence of `Q`
in the dual start matroid.  At `u=b`, the statement follows from freeness.
\(\square\)

### Theorem 4.2 (small exceptional bank lifts automatically)

Let `mathcal E` be a named exceptional chunk bank.  Assign each
`F in mathcal E` one compatible start rank `u(F)` satisfying

\[
                         b+\ell_F\le u(F)\le r.
\tag{4.3}
\]

If

\[
                         |\{F:u(F)=u\}|\le r
                         \qquad(b<u\le r),
\tag{4.4}
\]

then `mathcal E` has a collar-saturated named attachment.

#### Proof

Fix `u` and a chunk top of rank `s<u`.  It has

\[
                         \binom{2r-s}{u-s}
\tag{4.5}
\]

rank-`u` supersets.  Since `1<=u-s<2r-s`, every nontrivial binomial
coefficient in (4.5) is at least `2r-s>=r+1`.

There are at most `r` chunks assigned to `u`.  For every nonempty subfamily,
the union of its candidate sets contains the candidate set of one member
and hence has size at least `r+1`, at least the subfamily size.  Hall gives
distinct containing rank-`u` starts.  Proposition 4.1 says their set is
independent in `mathsf K_u`.  Perform this independently in every tagged
rank and apply Theorem 2.1.  \(\square\)

In particular, any total bank of `O(D)` exceptional chunks satisfies
(4.4) for all sufficiently large `r`, because `D=Theta(sqrt(r))`.

## 5. Making the small bank genuinely freed-socket faithful

Return to the shift from old bottom `t=b+1` to new bottom `b`.  Suppose
the anonymous one-depth packing has reserved `h<=r` distinct vanished
old-singleton/socket pairs for new exceptional chunks `F_i`.  Let the old
positive socket type in pair `i` be `c_i>=1`, and suppose

\[
                         \ell_{F_i}\le c_i+1.
\tag{5.1}
\]

Put

\[
                         u_i=t+c_i=b+1+c_i.
\tag{5.2}
\]

Thus a collar occurrence starting at rank `u_i` has old capacity `c_i`
and new capacity `c_i+1`.

### Theorem 5.1 (small physical freed-socket lift)

Assume

\[
                         b\ge1,
 \qquad
                         h\le H_b,
 \qquad
                         \binom{b+2}2\ge h.
\tag{5.3}
\]

One may co-choose the named data on these reserved pairs:

1. distinct rank-`u_i` collar starts `T_i` containing the exceptional tops
   `S_(F_i)`;
2. distinct rank-`b` old singleton-job values `A_i subset T_i`;
3. an old named residual interval lift in which the `A_i` are beginnings
   carrying `h` of the canonical length-one jobs;
4. one collar chainization, used at both depths, in which every `T_i` is a
   start;

so that old singleton job `A_i` occupies occurrence `T_i`, disappears under
the shift, and new exceptional chunk `F_i` occupies that same occurrence.

#### Proof

Apply the fixed-rank Hall construction in Theorem 4.2 at the prescribed
ranks `u_i`.  Since the total bank has size at most `r`, it gives distinct
`T_i` containing the corresponding `S_(F_i)`, and Proposition 4.1 makes
them compatible collar starts.

Each `T_i` has rank at least `b+2` and hence contains at least

\[
                         \binom{b+2}{b}=\binom{b+2}2
\]

rank-`b` subsets.  The displayed hypothesis and Hall's theorem choose
distinct `A_i subset T_i`.

At the last old residual interface, from rank `b-1` to rank `b`, reserve
the family `{A_i}` as new starts.  The protected-top calculation in the
proof of Proposition 4.1, now applied to this residual interface, shows
that the complete previous layer matches into
`mathcal B_b setminus {A_i}`.
Restrict that matching to the interval rows which actually continue to
rank `b`, and assign every unused rank-`b` set to a row beginning there.
In particular each `A_i` begins a row.  The canonical colour-passing theorem
assigns `h` of the `H_b` newly born length-one job colours to these singleton
rows.  All earlier ranks are named by the interval-histogram Boolean lift.

Construct the collar upward from rank `b`, reserving every `T_i` as a start
as in Theorem 2.1.  Restricting this same collar forest to old ranks
`t,...,r` leaves every `T_i` as the same old socket occurrence.  Attach
`A_i` below it at old depth; `A_i subset T_i` and old capacity `c_i>=1`
make this legal.  At new depth the residual singleton job is gone, while
the occurrence remains and has capacity `c_i+1`.  Equation (5.1) and
`S_(F_i) subset T_i` make the new attachment legal.  Distinctness prevents
all occurrence collisions.  \(\square\)

The theorem is an overlay statement: the transported bulk must use the
complementary starts, exactly as in the anonymous one-depth proof.  It proves
that a small exceptional bank introduces no additional named-containment
obstruction once its old singleton/socket type pairs have been reserved.

## 6. Exact surviving bulk gate

Let an integral anonymous interval fragmentation at depth `D+1` be fixed.
The interval-histogram theorem supplies at least one named residual lift
`mathcal R`.  The bulk names lift to a co-chosen collar if and only if one
can choose such a named interval lift satisfying the Rado cuts

\[
                         r_{\mathsf K}(N(X))\ge|X|
                         \qquad(X\subseteq\mathcal R).
\tag{6.1}
\]

This is the exact named-containment frontier.

* On complete-layer residual batches, the joint-start surplus orbit lift
  proves (6.1) from the finite type table.
* On an `O(D)` exceptional bank, Theorems 4.2 and 5.1 prove (6.1) and the
  stronger cross-depth occurrence statement.
* For a general configuration-rounded bulk, the chunks of one type occupy
  only partial named layers and the same literal target cannot be selected
  independently in several interval roles.  Neither normalized shadow nor
  independent random SCD marginals prove all cuts (6.1).

The determinant-two variable-slot minor is a sharp methodological no-go:
the simultaneous target-once and path-flow matrix is not generally totally
unimodular.  It is not a counterexample to (6.1) for the dense Boolean
histogram.  A positive proof still needs either

1. a decomposition of the bulk into complete-layer batches satisfying the
   joint-start type inequalities; or
2. a new uniform-spread theorem showing that some interval Boolean lift has
   enough rank in every start-matroid neighbourhood.

Thus the one-depth absorber's named exceptional part is locally solved,
while bulk naming remains the single correlated Rado/interval-lift gate.

## 7. Scope

Nothing here proves the depth-`D` fractional configuration inequalities or
the existence of a suitable integral anonymous bulk.  The result also does
not supply source-word serialization, residence, arbitrary-width upper
coverage, topology, or a safe opening.  The freed-socket theorem applies
unconditionally only to a small bank satisfying its displayed hypotheses;
the length-two breakup in the current anonymous absorber can create more
than `O(D)` chunks, so naming that entire bank still requires additional
distribution or batching.

## 8. Dependencies

1. `MATH_THEOREM_ONE_DEPTH_SHIFT_FREED_SINGLETON_ABSORBER_20260805.md`;
2. `MATH_THEOREM_JOINT_START_SURPLUS_ORBIT_LIFT_AND_NAMED_COLLAR_CHAINIZATION_20260804.md`;
3. `MATH_THEOREM_CAPACITATED_CHAIN_MAJORISATION_NOGO_AND_EXACT_HALL_LADDER_20260804.md`, Theorem 2.2;
4. `MATH_THEOREM_MONOTONE_INTERVAL_CANONICAL_FRAGMENTATION_EQUIVALENCE_20260804.md`;
5. `MATH_THEOREM_NESTED_INTERSECTION_BANK_SUPPORTED_CHAIN_EQUIVALENCE_PASCAL_RECURSION_AND_UCYCLE_NOGO_20260804.md`, Proposition 1.2A;
6. `MATH_AUDIT_VARIABLE_SLOT_LAYERED_FLOW_NONTU_20260803.md`;
7. Hall's theorem and Rado's matroid-transversal theorem.

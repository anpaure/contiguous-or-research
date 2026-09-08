# A Boolean hexagon is a ternary four-resource absorber

Date: 2026-08-01  
Status: exact local absorber and exact graphic switch theorem.  The packet
either gains one ordered diamond or removes one physical cycle while
preserving all four named resources.  It does not prove that the required
old pair is planted in a Delcourt--Postle near-forest, nor that a growing
family of such packets is simultaneously available.

## 0. Outcome

The ordered Boolean-diamond host has a support-minimal gain-one packet.
It is the alternating `C6` on three lower and three upper colours.

For one oriented target atom `e`, the displayed Cartesian fan supplies
exactly

\[
                              (m-1)^2
\tag{0.1}
\]

labelled packets.  (There may be other hexagons through the same target;
no classification of all of them is asserted.)  Every displayed packet has
three states:

* `O^-`, two old atoms, omitting exactly the four resources of `e`;
* `O=O^-+e`, three old atoms; and
* `N`, three new atoms.

Coordinatewise in the lower, upper, tail and head resource classes,

\[
                    \operatorname{res}(N)
       =\operatorname{res}(O)
       =\operatorname{res}(O^-)\mathbin{\dot\cup}\operatorname{res}(e).
\tag{0.2}
\]

Consequently the same packet has two exact uses.

1. **Gain mode.**  If `O^-` is present and the four resources of `e` are
   free, replace `O^-` by `N`.  Matching size rises by one and all four
   resource classes remain injective.
2. **Cycle mode.**  If all of `O` is present, replace `O` by `N`.  Matching
   size and all four resource palettes are unchanged.  If `e` lies on a
   physical cycle and the two other old edges lie in two distinct physical
   path components, the switch replaces those three components by two
   paths.  It therefore destroys one cycle without consuming a path
   component.

The union of the old and new physical phases is one alternating physical
`C6`; deleting `e` turns it into one alternating five-edge gain ear.  A
nontrivial `1 -> 2` packet cannot have (0.2).  Thus `2 -> 3` is the smallest
nontrivial exact four-resource gain.

This closes the *local* algebra requested by a cover-down/cycle absorber.
The remaining global statement is precisely a planting theorem: expose
enough old pairs in the near-forest, with the contracted graphic condition
below, to route its leave and its later physical cycles.  High girth and
the size `N-o(N)` alone do not imply that planting statement.

## 1. The six atoms

Let `Omega` have size `2m`, with `m>=3`.  Fix an `(m-2)`-set `S` and four
distinct coordinates

\[
                         a,b,c,d\notin S.
\]

Put

\[
\begin{array}{lll}
 L_a=S+a,&L_b=S+b,&L_c=S+c,\\
 U_a=S+b+c+d,&U_b=S+a+c+d,&U_c=S+a+b+d.
\end{array}
\tag{1.1}
\]

The containment graph induced by these six outer colours is `C6`:
`L_x subset U_y` exactly when `x!=y`.  Define the six middle vertices

\[
\begin{array}{lll}
 A=S+a+d,&B=S+a+c,&C=S+c+d,\\
 D=S+b+c,&E=S+b+d,&F=S+a+b.
\end{array}
\tag{1.2}
\]

An ordered atom is written `(L,U,T,H)`, with tail `T` and head `H`.
Set

\[
\begin{array}{lll}
 o_1=(L_a,U_b,A,B),&o_2=(L_c,U_a,C,D),
     &e=(L_b,U_c,E,F),\\
 n_1=(L_a,U_c,A,F),&n_2=(L_c,U_b,C,B),
     &n_3=(L_b,U_a,E,D).
\end{array}
\tag{1.3}
\]

Finally put

\[
        O^-={o_1,o_2},\qquad O=O^-\cup\{e\},\qquad
        N={n_1,n_2,n_3}.
\tag{1.4}
\]

### Theorem 1.1 (ternary hexagon resource identity)

Every entry of (1.3) is a legal ordered Boolean diamond.  Each of `O^-`,
`O`, and `N` is a four-partite matching, and (0.2) holds literally.

Their physical projections are

\[
 \partial O^-=\{AB,CD\},\qquad
 \partial O=\{AB,CD,EF\},\qquad
 \partial N=\{AF,CB,ED\}.
\tag{1.5}
\]

In particular `partial O union partial N` is the alternating cycle

\[
                       A-B-C-D-E-F-A,
\tag{1.6}
\]

and `partial O^- union partial N` is the alternating path obtained by
deleting `EF`.

#### Proof

Intersections and unions in (1.3) give, for example,

\[
 A\cap B=S+a=L_a,\qquad A\cup B=S+a+c+d=U_b,
\]

and the other five identities follow cyclically.  Thus every atom is
legal.  The four typed resource sets are

\[
\begin{array}{c|c|c|c|c}
 &\text{lower}&\text{upper}&\text{tail}&\text{head}\\ \hline
 O^-&L_a,L_c&U_b,U_a&A,C&B,D\\
 O&L_a,L_c,L_b&U_b,U_a,U_c&A,C,E&B,D,F\\
 N&L_a,L_c,L_b&U_c,U_b,U_a&A,C,E&F,B,D.
\end{array}
\tag{1.7}
\]

Every row is repetition-free, and the last two rows have identical typed
sets.  The difference between the first and last rows is exactly
`(L_b,U_c,E,F)=res(e)`.  This proves (0.2).  Formula (1.5) is read directly
from the tail/head pairs, and (1.6) follows.  \(\square\)

### Corollary 1.2 (automatic matching augmentation)

Let `M` be any matching in the ordered-diamond four-graph.  If `O^- subset
M` and no atom of `M` uses any of `L_b,U_c,E,F`, then

\[
                         M'=(M-O^-)\cup N
\tag{1.8}
\]

is a matching of order `|M|+1`.

No further collision check is needed: every resource of `N` is either a
resource formerly used by `O^-` or one of the four declared free resources.

## 2. Every target has a quadratic Cartesian fan

Let

\[
               e=(L,U,E,F),\qquad
               E=L+d,\quad F=L+a,quad U=L+a+d
\tag{2.1}
\]

be an arbitrary oriented atom.  Here `a,d` are the two coordinates of
`U-L`, assigned according to the desired head and tail roles.  For every

\[
                          b\in L,qquad c\notin U,
\tag{2.2}
\]

take `S=L-b` in Section 1.  This produces a packet whose missing old atom
is exactly (2.1).

### Theorem 2.1 (exact Cartesian-fan count and menu load)

The packets (2.2) are pairwise distinct.  Hence this construction gives
`e` exactly `(m-1)^2` indexed options.

The eight non-target typed resources of option `(b,c)` are

\[
\begin{array}{c|cc}
\text{lower}&L-b+a&L-b+c\\
\text{upper}&U-b+c&U-a+c\\
\text{tail}&U-b&L-b+c+d\\
\text{head}&L-b+a+c&L+c.
\end{array}
\tag{2.3}
\]

Within the menu of one fixed target, any fixed non-target typed resource
occurs in at most `m-1` options.

#### Proof

Within the displayed family, the target lower set is fixed as `S+b=L`;
the non-target entries recover `b` and then `c`.  This proves injectivity
of `(b,c)`, and the count follows from `|L|=|Omega-U|=m-1`.

In (2.3), the first lower, first tail entries determine `b` and leave `c`
free; the second upper, second head entries determine `c` and leave `b`
free.  Each of the other four entries determines both `b` and `c`.  The
row-type and mixed-type alternatives cannot coincide: the former use the
fixed coordinate `a` or remain inside `U`, while the latter use
`c notin U`.  Thus the maximum multiplicity is `m-1`.  \(\square\)

### Corollary 2.2 (bounded prospective banks pack)

Fix `H` pairwise resource-disjoint target atoms.  Before selecting options,
delete from each menu every option meeting a different target tuple.  Then
select options greedily, requiring their complete twelve-resource supports
to be disjoint.  A sufficient numerical condition is

\[
                            m-1>16(H-1).
\tag{2.4}
\]

Under (2.4), a disjoint option exists for every target.

#### Proof

Each of the four typed resources of another target deletes at most `m-1`
options by Theorem 2.1.  Hence the predeletion costs at most
`4(H-1)(m-1)` entries.  A selected complete hex support has three resources
in each of four types.  Against a later menu it deletes at most
`12(m-1)` entries.  Before the last choice the total excluded count is less
than

\[
          4(H-1)(m-1)+12(H-1)(m-1)
             <(m-1)^2.
\]

At least one option remains.  This is a prospective bounded-bank theorem;
it is not a packing theorem for `H` growing with `m`.  \(\square\)

## 3. Exact graphic uses

Resource feasibility does not imply physical acyclicity.  The packet has a
particularly small exact graphic test.

### Theorem 3.1 (gain-ear graphic criterion)

Let the physical projection `G` of `M` in Corollary 1.2 be a forest, and
put

\[
                         G_0=G-AB-CD.
\tag{3.1}
\]

Then the augmented projection

\[
                     G'=G_0+AF+BC+DE
\tag{3.2}
\]

is a forest if and only if the three displayed new edges form a forest
after every connected component of `G_0` is contracted.  In particular it
is sufficient that `A,B,C,D,E,F` lie in six distinct components of `G_0`.

If (3.2) is a forest, it has one fewer component than `G`, exactly as a
gain-one cover-down ear must.

#### Proof

Every edge of a forest is a bridge, so deleting `AB,CD` raises the component
count by two.  Adding the three new edges is acyclic exactly when their
component contraction has neither a loop nor a cycle; in that case it
lowers the component count by three.  The net change is minus one.  This is
the standard graphic-matroid contraction test, stated here on the literal
five-edge ear.  \(\square\)

There are two possible full phases after the resources of `e` become free:
the direct phase `O=O^-+e` and the rerouted phase `N`.  The direct phase is
forest-safe exactly when `E` and `F` lie in different components of `G`.
The rerouted phase obeys Theorem 3.1.  These two tests are not exhaustive
alternatives: both can fail, so the quadratic fan is a real physical
selection problem rather than a formal redundancy.

### Theorem 3.2 (one-cycle elimination)

Let `G` be the physical projection of an exact ordered four-transversal, so
its components are directed paths and directed cycles.  Suppose one packet
has all of `O` present and

1. `EF` lies on a cycle component;
2. `AB` and `CD` lie on two distinct path components; and
3. those three components are pairwise distinct.

Then toggling `O` to `N` preserves every lower, upper, tail and head
resource, preserves maximum physical degree two, and replaces the one cycle
and two paths by two paths.  In particular the physical cycle count drops
by one while the number of path components is unchanged.

#### Proof

After deleting `EF`, its cycle becomes one path joining `E` to `F`.
Deleting `AB` and `CD` splits each of the two old paths into two fragments.
Thus there are five path fragments.  The edges `AF` and `ED` join the
cycle fragment to one fragment from each old path, producing one path.
The edge `BC` joins the two remaining fragments, producing the second path.
No cycle is created.  The four-resource and degree statements are Theorem
1.1.  \(\square\)

### Corollary 3.3 (serial regenerative cycle bank)

If at every nonterminal state with more than `h` physical cycles there is
an applicable packet satisfying Theorem 3.2, repeated toggling leaves at
most `h` cycles and does not consume the `K` physical path components.
Deleting one atom from each remaining cycle gives a central defect at most
`h`.

Thus the needed cycle theorem is an **applicable-hex supply theorem**, not
an abstract cycle-count estimate.  The partner path bank is regenerative.

## 4. Support minimality and the star-centred square obstruction

The preceding `C6` is the first possible nontrivial packet.

### Lemma 4.1 (every outer alternating square is star-centred)

Suppose distinct lower colours `L_0,L_1` and distinct upper colours
`U_0,U_1` satisfy all four containments

\[
                  L_i\subset U_j\qquad(i,j\in\{0,1\}).
\tag{4.1}
\]

Then

\[
                    X=L_0\cup L_1=U_0\cap U_1
\tag{4.2}
\]

has rank `m`, and all four corresponding diamonds have `X` as a physical
middle endpoint.

#### Proof

Distinct rank-`m-1` sets have union of rank at least `m`; distinct
rank-`m+1` sets have intersection of rank at most `m`.  The containments
give

\[
                 L_0\cup L_1\subseteq U_0\cap U_1.
\]

Equality and rank `m` follow.  Since `L_i subset X subset U_j`, `X` is one
of the two intermediate middle sets of every diamond.  \(\square\)

### Theorem 4.2 (no nontrivial `1 -> 2` exact absorber)

There do not exist one off atom `o`, one target atom `e`, and two on atoms
`n_0,n_1` such that

\[
       \operatorname{res}\{n_0,n_1\}
       =\operatorname{res}\{o,e\}
\tag{4.3}
\]

in every one of the four typed resource classes, unless the two phases are
the same atoms.

#### Proof

The lower and upper identities in (4.3) leave two pairings.  If the pairing
is unchanged, each on atom has the same two physical middle endpoints as
its old counterpart.  Reversing exactly one orientation changes one typed
tail and one typed head; reversing both could preserve the typed multisets
only if the two old diamonds had the same unordered endpoint pair.  That
would give the same intersection and union, contradicting distinct lower
and upper resources.  Hence the unchanged pairing gives the same atoms.

In the remaining, nonidentity case the on atoms are the cross pairing of
the off and target outer colours.  All four containments then hold, so
Lemma 4.1 applies.  Write

\[
 X=C+a+b,quad L_0=C+a,quad L_1=C+b,quad
 U_0=X+c,quad U_1=X+d
\]

with `a,b,c,d` distinct.  Besides the common endpoint `X`, the two old
physical endpoints are

\[
                        C+a+c,\qquad C+b+d,
\]

whereas the two crossed endpoints are

\[
                        C+a+d,\qquad C+b+c.
\]

The two unordered pairs cannot agree: direct equality forces `c=d`, and
crossed equality forces `a=b`.  Therefore even the untyped physical middle
resource multisets differ, contradicting the tail/head rows of (4.3).
\(\square\)

So a two-atom alternating square can transport middle load, but it cannot
gain one atom while preserving the four named resource sets.  The ternary
hexagon is support-minimal.

## 5. Consequence for the asymptotic route and the one-cell seam

The Delcourt--Postle matching/high-girth forest supplies a large `O^-`-type
body only statistically; it does not assert that the two specific old atoms
of a desired hexagon are present.  Nor does high girth imply the applicable
placement in Theorem 3.2.  The exact remaining central theorem can now be
stated without ambiguity:

> **Prepared ternary-hex cover-down.**  Choose the near-forest colour and a
> family of quadratic hex menus jointly so that its outer/tail/head leave
> is partitioned into target atom tuples, every target has a planted old
> pair, the gain choices pass Theorem 3.1, and the neutral choices pass
> Theorem 3.2 until only `O(1)` physical cycles remain.

The local list size is `(m-1)^2`, and a fixed typed resource has menu load
at most `m-1`; these are the desired quadratic-versus-linear local scales.
What is not proved is the growing-family independent transversal or the
correlation of the bulk leave with the target tuples.

If a gain is subsequently realized as one added source position in the OR
word, the separate star-hidden fan theorem applies.  Its exact identity

\[
                    Z\cup C_i=L_{i+1}\cup R_{d-i+1}
\]

shows that fan targets and destroyed crossing targets are coupled.  The
present `C6` theorem concerns the central four-resource matching only; it
does not make those compiler traces independently programmable.  A literal
one-cell lift must additionally satisfy the interval-zero compatibility
criterion of
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`.

## 6. Replay

Run

```text
python3 scratch/audit_boolean_hex_ternary_four_resource_absorber_20260801.py
```

The audit checks the six literal atoms, every resource identity, the
alternating physical `C6`, all `(m-1)^2` options for one canonical target
at `3<=m<=10`, the menu-load bound, the graphic gain criterion on every
partition of the six named physical vertices, and the `1 -> 2` no-go on
the canonical outer square.

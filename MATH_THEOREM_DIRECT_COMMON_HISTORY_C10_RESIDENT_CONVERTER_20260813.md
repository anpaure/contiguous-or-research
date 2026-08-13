# A direct common-history resident lift of the rigid odd-GK `C10`

**Date:** 2026-08-13  
**Status:** unconditional literal local source rethread.  It realizes the
five-diamond `C10` in one operation, without the cancelling chord used by
the serial two-`C6` factorization.  It preserves the complete strict-lower
occurrence deck, the complete internal fragment deck, and positive
residence.  It does **not** by itself plant the five literal fragments in a
single global source carrier, certify the exterior zero-gap guard, or
preserve arbitrary upper witnesses crossing the protected collar.

## 0. Statement

Let `m>=5`, let the ten rank-`m+1` owners `A_i,B_i` (`i in Z_5`) be those
of the rigid palette-neutral `C10`, and let

\[
 E_i=A_iB_i,
 \qquad
 E_i'=B_iA_{i-1}.
\tag{0.1}
\]

Fix `1<=d<=m-2`.  There are nonempty source letters

\[
 X_i,C_1,\ldots,C_d,Y_i
\tag{0.2}
\]

such that the old literal fragments

\[
 W_i=(X_i,C_1,\ldots,C_d,Y_i)
\tag{0.3}
\]

have owner hinges `A_iB_i`, while the single cyclic head rethread

\[
 \widehat W_i=(X_i,C_1,\ldots,C_d,Y_{i+1})
\tag{0.4}
\]

has owner hinges `A_iB_{i+1}=E'_{i+1}`.  Hence `(0.4)` is exactly the net
`C10`, not a serial realization through an intermediate chord.

For arbitrary tagged exterior contexts transported with the right heads,
this rethread has all of the following properties.

1. It gives an occurrence-preserving bijection on every interval-OR whose
   rank is strictly below `m+1`.
2. It preserves the complete interval-OR multiset through width `d+2`.
   In particular, it preserves the complete internal deck of the five
   fragments at every possible width.
3. Every source occurrence has positive owner residence at least `d+1`;
   the two locally repeated hinge coordinates have one merged run of
   length `2d+2`.
4. On any protected global realization of the five old hinges, the induced
   owner switch is the rigid `C10`, so it replaces the four affected old
   owner cycles by exactly two.

Thus the shared-chord incompatibility of the two separate resident `C6`
lifts is not intrinsic: a five-hinge common-history packet bypasses that
chord completely.

## 1. The common core and the ten screens

Read binary words on coordinates `0,1,...,2m` and put

\[
 H=\{m,m+1,\ldots,2m-3\},
 \qquad |H|=m-2.
\tag{1.1}
\]

For compactness write

\[
 p=m-1,
 \qquad q=2m-2,
 \qquad s=2m-1,
 \qquad t=2m.
\tag{1.2}
\]

Directly subtracting `H` from the owners gives

\[
\begin{array}{c|c|c}
i&X_i=A_i\setminus H&Y_i=B_i\setminus H\\ \hline
0&\{p,q,s\}&\{q,s,t\}\\
1&\{0,p,q\}&\{0,q,s\}\\
2&\{0,1,p\}&\{0,1,q\}\\
3&\{0,p,s\}&\{0,1,s\}\\
4&\{p,s,t\}&\{0,s,t\}.
\end{array}
\tag{1.3}
\]

Consequently

\[
 A_i=H\mathbin{\dot\cup}X_i,
 \qquad
 B_i=H\mathbin{\dot\cup}Y_i.
\tag{1.4}
\]

All ten screen letters are nonempty triples.  Partition the common core
into nonempty pieces

\[
 H=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_d,
\tag{1.5}
\]

which is possible exactly in the asserted range `d<=m-2`, and write
`mathcal C=(C_1,...,C_d)`.

The two length-`d+1` windows of `W_i=(X_i,mathcal C,Y_i)` are now literally

\[
 H\cup X_i=A_i,
 \qquad
 H\cup Y_i=B_i.
\tag{1.6}
\]

After the cyclic head shift they are

\[
 H\cup X_i=A_i,
 \qquad
 H\cup Y_{i+1}=B_{i+1}.
\tag{1.7}
\]

The new hinge is therefore `A_iB_{i+1}`.  Since the rigid `C10` uses
`E'_j=B_jA_{j-1}`, setting `j=i+1` proves that the five new hinges in
`(1.7)` are exactly the five edges `(E'_j)_j`.

The known palette identities can also be read in the new indexing as

\[
 A_i\cap B_{i+1}=L_i,
 \qquad
 A_i\cup B_{i+1}=A_{i+1}\cup B_{i+1}=:U_{i+1}.
\tag{1.8}
\]

Thus lower colours rotate as prescribed and every old immediate-upper
colour is rematerialized on a new hinge.

## 2. One source rethread, with no intermediate chord

Cut each protected source carrier immediately before its tagged occurrence
of `Y_i`.  Let `P_i` denote the complete tagged left path ending in
`X_i mathcal C`, and let `Y_iQ_i` denote the complete tagged right path
beginning at that cut.  Reattach by the five-cycle

\[
 P_i\,(Y_iQ_i)
 \quad\longmapsto\quad
 P_i\,(Y_{i+1}Q_{i+1}).
\tag{2.1}
\]

Because the entire right path, rather than only its first source letter, is
moved, every old adjacency internal to a tagged left or right path remains
literal.  The only new depth-`d` seam is

\[
 X_i,C_1,\ldots,C_d,Y_{i+1},
\tag{2.2}
\]

and `(1.7)` proves that both new owner windows at that seam are legal.
There is no occurrence required to have two incompatible successors, and
the chord `A_3B_1` of the two-hexagon factorization never appears.

At owner level `(2.1)` removes `A_iB_i` and inserts `A_iB_{i+1}`.  Hence it
has exactly the successor permutation of the net rigid `C10`.  In
particular, when the five old occurrences have the audited return
involution `(0)(1\ 4)(2)(3)`, composition with this five-cycle has two
orbits.  The source rethread therefore induces the same four-to-two
topology change as the owner-level `C10`.

## 3. Exact strict-lower occurrence transport

### Theorem 3.1

Under `(2.1)`, every old occurrence of every interval-OR value of rank
strictly below `m+1` has a canonical new occurrence with the same value,
and this correspondence is a bijection preserving width and multiplicity.

#### Proof

An interval which crosses a displayed hinge from its left screen to its
right screen contains `X_i`, every `C_j`, and `Y_i`.  In particular it
contains

\[
 H\cup X_i=A_i,
\tag{3.1}
\]

which already has rank `m+1`.  The same is true after the rethread, with
`Y_{i+1}` in place of `Y_i`.  Therefore a strict-lower interval can meet
at most one of the two screen occurrences at every changed hinge.

If it lies on a left path or meets `X_i` and only a prefix of the common
history, keep it at the identical tagged positions.  If it lies on a right
path or meets only a suffix of the common history followed by `Y_iQ_i`,
move it with the complete tagged path `Y_iQ_i`.  Intervals contained in the
common history stay fixed.  All context-body intervals are literal.  These
operations partition all strict-lower occurrences and are inverted by the
opposite head shift, so they give the claimed bijection.  \(\square\)

Every strict-lower compiler matching, including all designated q2 and
deeper lower occurrences carried by this source packet, transports along
this bijection with deletion number zero.  No separate phasewise q2
calculation is needed for the compound lift.

## 4. The complete internal deck and the width-`d+2` collar

### Theorem 4.1

Across the five tagged context families, the interval-OR multiset is exact
at every width `1<=ell<=d+2`.  In particular, the multiset of every
internal interval of the five fragments is exact at all its possible
widths.

#### Proof

For `ell<=d+1`, an interval cannot meet both screens, since `d` common
letters lie strictly between them.  It therefore belongs to one of the
literal/permuted banks used in Theorem 3.1, whether or not its rank is
strictly lower.

At width `d+2`, an interval meeting both screens is exactly the full
fragment.  Its old value is

\[
 \operatorname{OR}(W_i)
 =H\cup X_i\cup Y_i
 =A_i\cup B_i
 =U_i,
\tag{4.1}
\]

whereas its new value is

\[
 \operatorname{OR}(\widehat W_i)
 =H\cup X_i\cup Y_{i+1}
 =A_i\cup B_{i+1}
 =U_{i+1}.
\tag{4.2}
\]

Thus the five full-fragment values are cyclically permuted.  Every other
width-`d+2` interval meets at most one screen and is handled by the same
literal/permuted bank bijection.  \(\square\)

This gives a particularly useful rematerialization rule: any designated
upper witness lying wholly inside one protected fragment survives at every
width, not only at the immediate-upper width.

## 5. Positive residence

Every coordinate occurrence at a source position belongs to `d+1`
consecutive length-`d+1` owner windows.  Hence it creates a positive owner
run of length at least `d+1`; another nearby occurrence can only merge or
extend such runs.

More explicitly, `(1.8)` has

\[
 |X_i\cap Y_{i+1}|=2.
\tag{5.1}
\]

Each of these two coordinates occurs at both endpoints of the new fragment,
at source distance `d+1`.  Its two blocks of `d+1` owner windows are
consecutive, so they merge into a positive run of length `2d+2`.  The one
remaining coordinate in each screen has its ordinary run of length
`d+1`.  Thus the new seam creates no short positive run.

This is only the positive-residence assertion.  A minimum zero-run between
distinct positive runs is a condition on the transported exterior
contexts and is not implied by the local packet.

## 6. The exact remaining caveats

The construction closes the **local occurrence converter**, but two global
assertions remain genuinely separate.

### 6.1 Global source planting

The owner identities `(1.4)` do not prove that a given global source
carrier contains these five owner edges with the **same literal ordered**
partition `(C_1,...,C_d)` of `H`, nor that its five complete right paths can
be reattached while every frozen socket, phase, history, and cap ticket
remains legal.  What is still needed is a protected completion/lift theorem
which plants the five fragments `(0.3)` in the required four GK/PBBS
components and supplies compatible exterior contexts.  The owner-level
small protected-factor theorem alone does not give that source lift.

The cross-seam zero-gap or q-safe residence guard belongs to this same
global planting problem: positive residence is local and automatic, but
spacing between separate runs depends on the exterior contexts brought
together by `(2.1)`.

### 6.2 Exterior upper witnesses

Width `d+3` is the first width at which an interval can contain both
screens and an exterior source letter.  For example, with a private left
context letter `z_i`, the old value

\[
 z_i\cup H\cup X_i\cup Y_i=z_i\cup U_i
\tag{6.1}
\]

is replaced locally by

\[
 z_i\cup H\cup X_i\cup Y_{i+1}=z_i\cup U_{i+1}.
\tag{6.2}
\]

Since the `U_i` are distinct sets of the same rank, no formal local deck
identity restores `(6.1)`.  If `(6.1)` had no other occurrence, its witness
is lost.  More generally, every possibly lost old exterior value contains
one of the five immediate-upper bases `U_i`, so the damage is confined to

\[
 \bigcup_{i=0}^4\{Z:U_i\subseteq Z\subseteq[2m+1]\}.
\tag{6.3}
\]

Therefore arbitrary all-width upper coverage still needs either a
protected alternative-witness reservoir in this cone or a global source
planting theorem that chooses the designated witnesses inside the exact
fragment bank.  The latter witnesses are already handled by Theorem 4.1.

## 7. Consequence for the repair architecture

The earlier serial resident lift failed because the intermediate chord
occurrence had to close the first `C6` and simultaneously open the second.
The direct packet shows that this is an artifact of the factorization, not
an obstruction to the net `C10`.  Conditional only on protected global
source planting and exterior upper/q-safe guards, it supplies one literal
five-hinge move with:

\[
\boxed{
\begin{gathered}
\text{net palette-neutral `C10`,}\quad
\text{four owner cycles to two,}\\
\text{zero strict-lower occurrence loss,}\quad
\text{exact internal all-width deck,}\quad
\text{positive residence.}
\end{gathered}}
\]

This is the smallest natural compound replacement for the incompatible
serial two-`C6` source lifts.

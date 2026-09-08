# The canonical restitution residual is a split-center triangular ear

**Date:** 2026-08-01  
**Lane:** A, ambient duplication / one-oriented reversal quotient  
**Status:** exact local theorem and exact scope audit; retained as the
smaller single-triangle gadget, not as the main reset-duplication theorem.
The stronger frozen theorem
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`
classifies the complete `d`-overlap leave as two Ferrers triangles and
supplies both with protected `5d`-owner banks.  The proposed
split-center path supplies every member of the forced
`binom(d,2)` residual family, with simple owners and simple immediate
palettes, using only `2d-2` roots.  It is only boundary-resident.  The
small protected-factor theorem plants its owner/lower-q1 path without
owner excess in sufficiently large dimension, but the local formula does
not prove exterior joins, a compatible global source, or coverage of the
additional long losses.

Throughout `d>=2`.  Only one orientation is constructed.  The opposite
source/witness/compiler certificate is obtained by global reversal; no
phase-common physical matching is asserted or needed.

## 1. The actual forced family after the canonical tail

Use the source normal form of
`MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md`.
Allow a permanent common core `H`, and write

\[
 X=\{x_1,\ldots,x_d\},\qquad C=\{c_1,\ldots,c_d\},
 \qquad B=H\cup X\cup C\cup\{\delta\}.
 \tag{1.1}
\]

Then `|B|=r`, where `r` is the owner rank.  Put

\[
 U_p=\{u_1,\ldots,u_p\}\quad(0\le p\le d-2),
 \tag{1.2}
\]

and, in reverse order along the terminal singleton block,

\[
 v_j=y_{d-j+1},\qquad
 V_q=\{v_1,\ldots,v_q\}\quad(1\le q\le d-1).
 \tag{1.3}
\]

The banks `B,U_(d-2),V_(d-1)` are pairwise disjoint except for the
displayed nesting within each bank.

Linearize immediately before `A_0` and append the canonical restitution
tail `A_0,...,A_(d-1)`.  For

\[
 p\ge0,\qquad q\ge1,\qquad p+q\le d-1,
 \tag{1.4}
\]

consider the cyclic interval consisting of the last `q` source cells and
the first `d+1+p` source cells.  Its value is

\[
 \boxed{T_{p,q}=B\cup U_p\cup V_q.}
 \tag{1.5}
\]

It is absent after the `d`-cell tail, because its required prefix has
length `d+1+p>d`.  Conversely every member of the forced short residual
after that tail occurs uniquely in (1.5).  At rank `r+u` there are exactly
`u` members, indexed by `p+q=u`, and hence

\[
 \bigl|\{T_{p,q}\}\bigr|
   =\sum_{u=1}^{d-1}u=\binom d2.
 \tag{1.6}
\]

### Proof

The first `d+1` cells `A_0,...,A_d` have union `B`; the next `p`
singleton-bank cells add exactly `U_p`.  The last `q` source cells are
`C+v_q,...,C+v_1` and add exactly `V_q`.  This proves (1.5).  The interval
has width `d+1+p+q<=2d`, so short-interval injectivity makes all these
values distinct and excludes an alternate-width cyclic witness.  The
tail criterion from the frozen linearization theorem says precisely that
the un-restored short intervals have after-cut prefix length greater than
`d`; writing that length as `d+1+p` gives (1.4), and proves exhaustion.
\(\square\)

## 2. The split-center owner ear

Choose distinct `a,b in C`.  Choose ordered lists

\[
 e_1,\ldots,e_{d-2}, f_1,\ldots,f_{d-2}
 \tag{2.1}
\]

which are pairwise distinct elements of
`B\setminus\{a,b,delta\}`.  This is possible in the reset range
`r>=2d+1`, and in particular under the stronger packet host hypotheses.
Let

\[
 E_p=\{e_1,\ldots,e_p\},\qquad
 F_t=\{f_1,\ldots,f_t\}.
 \tag{2.2}
\]

Define rank-`r` roots

\[
 L_p=(B\setminus(\{a\}\cup E_p))\cup\{v_1\}\cup U_p,
       \qquad 0\le p\le d-2,
 \tag{2.3}
\]

\[
 R_q=(B\setminus(\{b\}\cup F_{q-1}))\cup V_q,
       \qquad 1\le q\le d-1,
 \tag{2.4}
\]

and order them as

\[
 \mathcal E=(L_{d-2},L_{d-3},\ldots,L_0,
              R_1,R_2,\ldots,R_{d-1}).
 \tag{2.5}
\]

### Theorem 2.1 (literal triangular ear)

The list (2.5) is a simple rank-`r` Johnson path on `2d-2` roots.  Its
immediate lower and upper colours are all simple.  For every pair (1.4),
the interval

\[
             L_p,L_{p-1},\ldots,L_0,R_1,\ldots,R_q
 \tag{2.6}
\]

has union exactly `T_(p,q)`.  Consequently the path supplies the complete
forced triangular residual (1.5), once each as a selected witness.

### Proof

The ranks follow from

\[
 |L_p|=r-(p+1)+(p+1)=r,\qquad
 |R_q|=r-q+q=r.
 \tag{2.7}
\]

For `p>=1`, traversing from `L_p` to `L_(p-1)` exchanges `u_p` for `e_p`.
The center transition exchanges `b` for `a`, and traversing from `R_q` to
`R_(q+1)` exchanges `f_q` for `v_(q+1)`.  Thus every edge is Johnson.

The `L` roots are separated by their `U` profiles, and the `R` roots by
their `V` profiles.  A root `L_p` with `p>=1` contains a `u` label absent
from every `R_q`; `L_0` and `R_1` differ by `a,b`; while `R_q`, `q>=2`,
contains `v_2` absent from `L_0`.  Hence all roots are distinct.

The complete q1 ledger is

\[
\begin{aligned}
 L_p\cap L_{p-1}
   &=(B\setminus(\{a\}\cup E_p))\cup\{v_1\}\cup U_{p-1},\\
 L_p\cup L_{p-1}
   &=(B\setminus(\{a\}\cup E_{p-1}))\cup\{v_1\}\cup U_p,
                 &&1\le p\le d-2,\\
 L_0\cap R_1&=(B\setminus\{a,b\})\cup\{v_1\},\\
 L_0\cup R_1&=B\cup\{v_1\},\\
 R_q\cap R_{q+1}
   &=(B\setminus(\{b\}\cup F_q))\cup V_q,\\
 R_q\cup R_{q+1}
   &=(B\setminus(\{b\}\cup F_{q-1}))\cup V_{q+1},
                 &&1\le q\le d-2.
\end{aligned}                                               \tag{2.8}
\]

Strict `U` and `V` profiles separate colours on each side.  The two sides
are separated by the presence of a `u` label or of `v_2`; in the only
profile-zero cases, pairwise distinctness of `a,b,e_1,f_1` separates the
sets.  Thus both palettes are simple.

Finally the union of the `L` part of (2.6) is
`(B-a)+v_1+U_p`, while the `R` part has union
`(B-b)+V_q`.  Since `a!=b`, their combined union is
`B+U_p+V_q=T_(p,q)`.  \(\square\)

## 3. Exact relation with the opened reset packet

Take `v_1=y_d` as in (1.3), and open the reset-return packet at its natural
edge `Q_(d-1)E`, where `E=B` and

\[
                         Q_{d-1}=B-x_d+v_1.              \tag{3.1}
\]

Under the choices in Section 2:

1. every ear root is distinct from every packet root;
2. every ear lower colour is distinct from every surviving packet lower
   colour;
3. every ear upper colour except the center colour is distinct from every
   packet upper colour; and
4. the center upper colour is

\[
                         B+v_1=E\cup Q_{d-1},             \tag{3.2}
\]

   namely the unique upper colour deleted at the natural packet opening.

Thus the ear recycles the omitted seam upper colour exactly once.  It does
**not** recycle the omitted seam lower colour `B-x_d`; its center lower
colour is `(B-a-b)+v_1`.

### Proof

Reset roots and colours contain no fresh `y` label.  The `P` half of the
return rail contains `alpha` and omits `delta`, whereas every ear root and
colour contains `delta` and omits `alpha`.  The `Q` half retains every
coordinate of `C`, whereas every `L` object misses `a` and every `R`
object misses `b`.  The sole exception is the center upper set `B+v_1`,
and (3.1) gives (3.2).  The same signatures prove root disjointness and the
lower assertions.  \(\square\)

This is a palette calculation for the opened packet plus ear.  It does not
claim that the remaining global lower and upper palettes already admit a
spanning completion.

## 4. Erosion and the exact boundary residence state

Every positive coordinate run in (2.5) is either long enough or clipped at
one path endpoint.  The traces and their positive-run lengths are:

\[
\begin{array}{c|c|c}
\text{coordinate}&\text{location of positive run}&\text{length}\ \\ \hline
u_i&\text{prefix}&d-1-i\\
v_j\ (j\ge2)&\text{suffix}&d-j\\
a&\text{suffix}&d-1\\
b&\text{prefix}&d-1\\
e_i&\text{suffix}&d-1+i\\
f_i&\text{prefix}&d-1+i\\
v_1,\ B\setminus(\{a,b\}\cup E_{d-2}\cup F_{d-2})
 &\text{whole ear}&2d-2.
\end{array}                                                \tag{4.1}
\]

In particular, no positive run shorter than `d+1` is bracketed at both
ends inside the ear.  Relative to coordinates occurring in the ear, exact
depth-`d` residence after concatenation is equivalent to the following
boundary-age lower bounds:

\[
\begin{array}{c|c}
\text{left exterior suffix}&\text{required consecutive ones}\ \hline
u_i&i+2\quad(1\le i\le d-2)\\
b&2\\
f_1&1
\end{array}
\qquad
\begin{array}{c|c}
\text{right exterior prefix}&\text{required consecutive ones}\ \hline
v_j&j+1\quad(2\le j\le d-1)\\
a&2\\
e_1&1.
\end{array}                                                \tag{4.2}
\]

For `d=2`, every coordinate in the whole-ear row of (4.1), including
`v_1`, has run length two and additionally needs one adjacent exterior
occurrence on either side.  For `d>=3`, every whole-ear run already has
length at least `d+1`.  Coordinates belonging only to the exterior remain
subject to the ordinary join test and are not covered by (4.2).

There are exactly `d-2` length-`d+1` root windows wholly inside the ear.
For `1<=p<=d-2`, the window

\[
                         L_p,\ldots,L_0,R_1,\ldots,R_{d-p}
 \tag{4.3}
\]

has intersection

\[
 C_p=(B\setminus(\{a,b\}\cup E_p\cup F_{d-p-1}))
                      \cup\{v_1\},                       \tag{4.4}
\]

of rank exactly `r-d`.  Consecutive `C_p` differ by one exchange.  These
are the complete internal cells of the maximal depth-`d` antecedent.
Boundary antecedent cells depend on the exterior continuation.

### Proof

The traces follow directly from the nesting in (2.3)--(2.4).  Subtracting
each displayed ear-run length from `d+1` gives (4.2).  In (4.3), every
left root omits `a`, the deepest left root also omits `E_p`, every right
root omits `b`, and the deepest right root omits `F_(d-p-1)`; only `v_1`
is common from the external banks.  Therefore (4.4) holds, and

\[
 |C_p|=r-(2+p+d-p-1)+1=r-d.
\]

Changing `p` by one exchanges the newly omitted `e` coordinate with the
newly restored `f` coordinate.  \(\square\)

Consequently the ear admits an exact flat maximal antecedent once it is
placed in a globally Johnson, boundary-age-compatible owner chronology
whose boundary intersections are nonempty.  The local formulas do not
construct that chronology.

## 5. The zero-owner-count scope and the remaining residual

The ear has `2d-2` distinct rank-`r` owners and `2d-3` Johnson edges.
Together with the opened reset path it specifies

\[
 (8d+2)+2(2d-3)=12d-4                              \tag{5.1}
\]

incidence edges in the middle-levels graph.  In the central specialization
`r=m`, after relabelling the combined support inside `[2m-1]`, Sections 2--3
prove that this
protected subgraph has maximum degree two and has no repeated owner or
lower-q1 vertex.  Hence the small protected-factor theorem embeds it in a
spanning owner/lower-q1 two-factor whenever

\[
                         m\ge12d-2.                       \tag{5.2}
\]

This is an unconditional zero-net-owner and lower-q1 placement theorem.
It does not prescribe which factor components contain the two paths, their
joining order, or a source chronology satisfying (4.2).

At the word level:

* appending it to an owner-exact chronology adds `2d-2` owner occurrences
  and is **not** an `O(1)`-length operation;
* it is owner-neutral only when used through a spanning factor placement
  such as (5.2), rather than appended after a completed owner factor; and
* owner neutrality does not by itself ensure global upper-q1 uniqueness,
  residence at the two joins, or a common-cap/compiler matching.

The local result is nevertheless sharp for the proved post-restitution
short family: it supplies all `binom(d,2)` forced targets using only
`2d-2` owner roots and one center-crossing interval per target.  Since
`d=Theta(sqrt(k))`, this is an allowed `O(d)` root rethread and
`O(d^2)=O(k)` interval modification inside a prospective `B+O(1)` proof,
provided the missing global chronology/source rethread exists.

The frozen finite census shows that additional long-interval losses may
remain after a packet opening.  Nothing in (2.3)--(2.6) proves that those
losses are supplied.  Thus the exact implication established here is

\[
 \boxed{\text{owner-neutral compatible ear placement}
        \Longrightarrow
        \text{zero residual on the forced triangular short family},}
 \tag{5.3}
\]

not a complete ambient-duplication theorem.

## 6. Exact remaining gate

To promote (5.3) to a global construction it is enough to prove, in one
chosen orientation, a protected owner-factor rethread with all of the
following properties:

1. it places the roots (2.3)--(2.4) consecutively without adding owner
   occurrences;
2. its two exterior joins satisfy Johnson adjacency and the boundary-age
   ledger (4.2), including exterior-only coordinates;
3. the ear q1 colours (2.8) are unused except for the deliberate seam-upper
   recycling (3.2);
4. the vacated roots and colours are reconnected without loss;
5. every additional long opening casualty receives an ambient witness; and
6. the resulting maximal antecedent has a terminal compiler matching.

Global reversal then transports the completed source, witness, and compiler
certificate.  No phase-common intersection is part of this gate.

## 7. Comparison with the frozen twin-bank theorem

The split-center ear is **not false**, but it is strictly weaker than the
new frozen local closure.

* This note uses the older end-tail presentation and repairs exactly the
  forced short triangle of size `binom(d,2)`.
* The frozen `d`-overlap theorem gives an exact leave, not merely a forced
  subfamily: two triangles of total size `d(d+1)`, including all long
  losses.
* Its two protected paths use `5d` owners (at most `7d` with collars), have
  marker-certified palette separation, and possess an unconditional
  protected q1 host for `m>=22d`.
* Therefore the twin-bank theorem is the correct primary route for the
  reset packet.  The present ear should be retained only as an economical
  conditional gadget when a construction has already reduced its leave to
  the single family (1.5), or when its split-center boundary signature is
  useful for another rethread.

No statement here should be cited as covering the complete reset opening
leave.

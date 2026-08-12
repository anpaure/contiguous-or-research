# The merged PBBS gate is an exact interval-cover Benders system; SCD and endpoint slack alone do not round it

**Date:** 2026-08-06  
**Method:** pure mathematics; elimination of coordinate supports, minimal
interval covers, and coloured-cycle minors  
**Status:** unconditional exact integral formulation and sharp quantifier
correction.  The merged-region target-placement problem is characterized by
explicit cover inequalities.  SCD slab labels and the \(0.044W\) endpoint
margin do not imply those inequalities or integral coloured Euler rounding:
arbitrarily small closed bad minors survive arbitrary disjoint slack.  The
result does **not** refute the actual merged PBBS construction; it identifies
the missing expansion/absorption premise and changes the credible proof order
from target-first to support-first.

## 1. Candidate target intervals

Fix a PBBS owner chronology \(T=(T_i)\), its maximal depth-\(d\) envelope

\[
                       P_p=\bigcap_{i=p-d}^{p}T_i,             \tag{1.1}
\]

and one or several long free regions.  Let \(\mathcal I\) be their cyclic
or linear intervals of lengths at most \(d\).  For every strict-lower target
\(S\), let \(\mathcal I_S\subseteq\mathcal I\) be its candidate intervals
after the mandatory aperture and every fixed remote-placement restriction
have been imposed.

Use binary variables

\[
                         y_{S,I}\in\{0,1\},qquad I\in\mathcal I_S.          \tag{1.2}
\]

The ordinary target/address rows are

\[
 \sum_{I\in\mathcal I_S}y_{S,I}=1,qquad
 \sum_{S:I\in\mathcal I_S}y_{S,I}\le1.                       \tag{1.3}
\]

For a coordinate \(x\), put

\[
                         B_x=\{p:x\in P_p\}.                  \tag{1.4}
\]

An \(x\)-positive target candidate \((S,I)\), with \(x\in S\), demands a
support point in

\[
                              J_x(S,I)=I\cap B_x.              \tag{1.5}
\]

An \(x\)-positive owner window \(O_i=[i,i+d]\), with \(x\in T_i\), demands
a support point in

\[
                              J_x(i)=O_i\cap B_x.              \tag{1.6}
\]

Every selected \(x\)-negative target candidate forbids support on its whole
interval.

## 2. Exact cover inequalities

For a physical set \(J\), let \(\mathfrak C_x(J)\) be the families
\(C\) of distinct negative candidates \((R,H)\), with \(x\notin R\), such
that

\[
                              J\subseteq\bigcup_{(R,H)\in C}H.               \tag{2.1}
\]

### Theorem 2.1 (exact merged cover polytope on binary assignments)

A binary assignment \(y\) satisfying (1.3) is realizable by one nonempty
PBBS antecedent if and only if it satisfies the following inequalities.

For every \(x\)-positive owner window and every
\(C\in\mathfrak C_x(J_x(i))\),

\[
                 \boxed{\sum_{(R,H)\in C}y_{R,H}\le |C|-1.}                 \tag{2.2}
\]

For every \(x\)-positive target candidate \((S,I)\) and every
\(C\in\mathfrak C_x(J_x(S,I))\),

\[
                 \boxed{y_{S,I}+sum_{(R,H)\in C}y_{R,H}\le |C|.}          \tag{2.3}
\]

It is enough to retain inclusion-minimal interval covers \(C\).  After a
cyclic cut, every such cover is a negative-percolation chain with increasing
left and right endpoints.

#### Proof

For a selected assignment define

\[
 R_x(y)=\bigcup_{(R,H):,x\notin R,,y_{R,H}=1}H,qquad
 Q_x=B_x\setminus R_x(y).                                  \tag{2.4}
\]

If all members of a cover \(C\) in (2.2) were selected, then
\(J_x(i)\subseteq R_x(y)\), killing the positive owner window.  This proves
necessity of (2.2).  If the positive target candidate and all members of a
cover in (2.3) were selected, its whole owner-compatible part would be
killed, proving necessity of (2.3).

Conversely, suppose an owner or selected positive target is killed.  The
finite family of selected negative intervals covers its set \(J\).  Take an
inclusion-minimal subcover \(C\).  The corresponding inequality (2.2) or
(2.3) is violated.  Thus every positive owner and target interval meets
\(Q_x\).  The PBBS-relative coordinate criterion then realizes the table by

\[
                   A_p^*=P_p\cap
                       \bigcap_{S:\,y_{S,I}=1,,p\in I}S.                    \tag{2.5}
\]

The mandatory-core owner argument makes every letter nonempty.  Finally,
minimal interval covers have the standard increasing-endpoint chain form.
\(\square\)

Theorem 2.1 is an exact Benders description: (1.3) is the master assignment,
and (2.2)--(2.3) are the complete family of coordinate separation cuts.
Their arity grows up to \(d+1\); no bounded-order conflict graph is exact.

## 3. SCD piece variables and the coloured Euler lift

Let \(\Gamma\) be the exact SCD pieces supplied by the merged-region SCD
theorem.  A placement atom \(a\) chooses

1. one piece \(\gamma\in\Gamma\);
2. one endpoint chain and its nested interval addresses;
3. one literal tail/head transition carrying those marked targets; and
4. its owner colour; and
5. its PBBS occurrence/successor ticket.

Let \(z_a\in\{0,1\}\).  The piece, address, target, and owner rows are
ordinary exact-cover rows.  The target-level variables in Theorem 2.1 are
the linear projection

\[
                         y_{S,I}=\sum_{a:\,(S,I)\in a}z_a.                  \tag{3.1}
\]

The occurrence/successor tickets are required to reconstruct the prescribed
PBBS owner cycle, not merely an arbitrary permutation of the owner colours.
Let \(\partial a\) be the head-minus-tail state boundary of an atom.
One-copy state balance is

\[
                              \sum_a z_a\partial a=0.                       \tag{3.2}
\]

Connected balance additionally requires the selected directed support to
have one component, equivalently a rooted Euler tour.

### Theorem 3.1 (exact SCD-coloured-cover Euler formulation)

On a fixed PBBS owner chronology, a merged-region one-copy serialization of
the SCD pieces exists exactly when the atom system has an integral selector
which

1. satisfies every piece, target, address, owner, and PBBS-successor row;
2. satisfies state balance (3.2) and connectedness; and
3. whose projection (3.1) satisfies every cover inequality
   (2.2)--(2.3).

#### Proof

A literal serialization selects one atom for every placed SCD piece.  Its
source intervals give (3.1), its trace overlaps give (3.2), and its Euler
chronology is connected.  Theorem 2.1 gives all coordinate cuts.

Conversely an integral connected balanced selector has one Euler ordering of
its literal transitions; the successor tickets identify this ordering with
the prescribed PBBS chronology rather than only with an owner-colour
permutation.  Its target/address projection passes Theorem 2.1,
which supplies the maximal PBBS antecedent with exactly the selected target
values.  Exact resource rows give one use of every named target and owner.
\(\square\)

This theorem is not a new existence proof.  Its point is that the stationary
pull clock, the SCD chain table, the owner projection, and Euler balance are
four projections of one selector.  They cannot be rounded sequentially unless
the cover cuts survive the conditioning.

## 4. Arbitrary endpoint slack does not imply the cover cuts

### Theorem 4.1 (slack-blind laminar-star minor)

For every \(2\le q\le d\) and every integer \(R\ge0\), there is a
chain-consistent long-region candidate table with

* one inclusion-minimal infeasible subsystem of \(q+1\) target assignments;
* every proper subsystem literally feasible;
* every target in the deep range \(d<|S|<t\); and
* at least \(R\) completely unused endpoint chains elsewhere.

The infeasibility is one inequality (2.3), and is unchanged when arbitrary
disjoint feasible SCD pieces or Euler components are adjoined.

#### Proof

Inside a short subinterval \(G\) of the long region, partition

\[
                         G=J_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}J_q.                          \tag{4.1}
\]

Choose the deep laminar-star targets

\[
 Z_G=K\cup F(G)\cup\{x\},qquad
 Z_j=K\cup F(J_j),                                         \tag{4.2}
\]

with \(|K|=d+1\) and \(3d+2<t\).  The parent is \(x\)-positive, all
children are \(x\)-negative, and the children cover the parent interval.
Thus

\[
             y_{Z_G,G}+\sum_{j=1}^q y_{Z_j,J_j}\le q                       \tag{4.3}
\]

is an instance of (2.3), while the displayed assignment sets its left side
to \(q+1\).  Removing any assignment gives the literal fillings from the
laminar-star theorem, so the subsystem is minimal.

The target containments agree with the physical containments, so the table
is chain-consistent.  Add \(R\) unused endpoint chains and any number of
shield-separated feasible atoms outside \(G\).  They do not alter (4.3).
\(\square\)

Consequently the \(\sim0.044W\) spare endpoints in the SCD census are not,
by themselves, an absorber for coordinate-cover defects.  A proof must show
that every bad minor has an available rerouting edge into that reservoir.

## 5. Arbitrary slack also does not imply coloured Euler rounding

The abstract three-shore parity hole has tails, heads, and colours
\(\{0,1\}\), all four arcs, and colour

\[
                              \kappa(p,h)=p\oplus h.                          \tag{5.1}
\]

Weighting every arc by \(1/2\) is exact on all three shores, but neither
tail--head perfect matching uses both colours.

### Proposition 5.1 (closed coloured minors survive arbitrary slack)

For every \(R\), the disjoint union of the parity hole with \(R\) forced
one-state, one-colour loops has

1. an exact fractional owner/payload/state circulation;
2. an integral selector on every proper projection obtained by forgetting
   one of the three shores;
3. arbitrarily many already integral roles and components; but
4. no integral rainbow cycle cover.

#### Proof

Use weight \(1/2\) on the four parity arcs and weight one on every added
loop.  Every resource row is exact.  Any integral selector would restrict on
the closed two-state component to a forbidden rainbow matching, since no
added loop shares one of its tails, heads, or colours.  \(\square\)

Boolean union colouring excludes this particular \(2\times2\) XOR minor.
The proposition is therefore a quantifier warning, not a Boolean PBBS
counterexample.  To use endpoint slack for fusion one must prove that the
actual Boolean atom system has no closed coloured minor, or that every such
minor has a protected colour-neutral circuit into the slack reservoir.

## 6. Why independent random placement is the wrong proof order

For one coordinate \(x\), roughly half of the named deep targets omit
\(x\).  If their intervals were placed independently and approximately
uniformly, a fixed point would be covered with probability tending rapidly
to one: a length-\(\ell\) random cyclic interval covers it with probability
\(\ell/g\), while the number of negative intervals is of order \(dg\).
When their mean length is \(\Theta(d)\), the survival probability is at most

\[
                         \exp(-\Theta(d^2)).                         \tag{6.1}
\]

and a union bound leaves no support point with overwhelming probability.

This is only a probabilistic warning, but it explains the exact cut
structure: negative intervals must be highly correlated around a deliberately
chosen support set.  Randomly assigning the SCD pieces first and trying to
repair coordinates afterward is not a credible route.

The proof-safe order is **support first**.

### Proposition 6.1 (support-first signature factor)

Choose sets \(E_x\subseteq B_x\) which meet every \(x\)-positive owner
window, and put

\[
                              A_p=\{x:p\in E_x\}.              \tag{6.2}
\]

For an interval \(I\), define its signature

\[
                              \sigma_E(I)=\{x:I\cap E_x\ne\varnothing\}.    \tag{6.3}
\]

Then \(A\) has owner row \(T\), and it carries every named target exactly
once if and only if the bipartite graph

\[
                    S\sim I\quad\Longleftrightarrow\quad
                    \sigma_E(I)=S                                      \tag{6.4}
\]

has a matching saturating the target bank.

#### Proof

The owner statement is the maximal-envelope coordinate criterion.  Equation
(6.3) is exactly the union of the letters on \(I\).  Distinct interval
addresses may therefore be assigned to targets precisely by the matching in
(6.4).  \(\square\)

The stationary pull clock should be viewed as a fractional law for the
supports and their interval signatures.  SCD pieces may organize the target
matching only **after** one integral support system has been selected.

## 7. The sharp remaining lemma and credible route

The shortest remaining positive statement is now:

> **Merged support-first coloured Euler theorem.**  Select one integral
> PBBS-compatible support family \((E_x)\), one exact matching of all deep
> targets to interval signatures, and one exact owner-coloured connected
> Euler selector, so that all but \(O(1)\) of the available endpoint chains
> are internal and every cover inequality (2.2)--(2.3) holds.

The corrected stationary pull clock supplies a rational point only before
these three choices are conditioned.  A valid rounding proof needs two new
uniform properties of the actual Boolean candidate system:

1. **cover expansion:** every negative-percolation minor has many
   target-preserving reroutes into the spare endpoint reservoir; and
2. **colour-neutral fusion expansion:** every nontrivial Euler-component
   cut has many owner-neutral alternating circuits crossing it.

Under those two expansion statements, reserve a bounded rooted skeleton,
apply the fixed-table Hoffman selector on the residual rectangle faces, and
use the reroute/fusion circuits as an absorber.  That is a credible route
because the merged SCD census leaves \(\Omega(W)\) unused endpoints.  Neither
expansion statement currently follows from the stationary rank marginals or
from the slabwise antichain-top theorem.

Thus the attempted direct implication

\[
 \text{fractional pull clock}+\text{SCD slabs}+0.044W\text{ slack}
 \Longrightarrow\text{integral connected cover-free clock}                 \tag{7.1}
\]

is not a theorem.  The exact new content required is expansion of the
**joint occurrence-labelled** atom system, not another scalar count.

## 8. Scope

This note proves an exact endpoint/cover constraint system and two
slack-blind obstruction principles.  It does not show that the real merged
PBBS atom system contains either bad minor, and therefore does not refute the
merged architecture.  It does show that the remaining theorem cannot be
obtained by postprocessing an arbitrary SCD endpoint assignment or by citing
the stationary pull-clock marginals alone.

No computation, search, random construction claim, or SSH is used.

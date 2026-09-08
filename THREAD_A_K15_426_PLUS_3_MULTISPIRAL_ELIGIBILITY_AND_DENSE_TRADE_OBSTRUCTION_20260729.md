# The k15 426+3 multi-spiral: eligibility and the dense-trade obstruction

Date: 2026-07-29

Status: theorem and frozen exact certificate.  The saved two-component
factor cannot be converted to a biresident Hamilton parent by any bounded
packet whose total quotient deletion support is below 83.  In particular,
at least 28 equivariant alternating C6 trades, or at least 11
support-at-most-eight trades, are required even before final chronology and
upper-support feasibility are checked.  A single connected quotient circuit,
if it succeeds, has even support and therefore support at least 84.  Such a
macroscopic circuit or a dense overlapping packet is not excluded.

## 1. Frozen factor

Let F_0 be the factor in

    scratch/k15_fixed_matching_pbbs_resident_20260729/
        from3_markov_s7_merge.best.json

with physical components in

    scratch/k15_fixed_matching_pbbs_resident_20260729/
        from3_markov_s7_merge.components.json.

Their SHA-256 digests are, respectively,

    0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555
    f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151

It is invariant under coordinate rotation on Z_15.  Its quotient consists
of two cycles

\[
(L_0,v_0)=(426,11),\qquad (L_1,v_1)=(3,4),               \tag{1.1}
\]

where L is quotient length and v is voltage modulo 15.  Both voltages are
units, so the physical component lengths are 15L:

\[
6390,\qquad45.                                           \tag{1.2}
\]

The factor is lower-q1 exact, upper-q1 complete, complete in every audited
fixed lower and upper shadow depth, and cyclically positive-resident with
minimum run four.  It is not zero-resident.

## 2. Multi-spiral eligibility normal form

The following is the componentwise extension of the strict-spiral
run-transversal normal form.

### Theorem 2.1 (multi-spiral normal form)

Let F be a C_k-invariant rank-r Johnson factor on k=2r-1 coordinates.
Suppose its quotient cycles are Gamma_nu of lengths L_nu and voltages
v_nu.  On a component whose voltage is a unit, multiply coordinates by
v_nu^{-1} and index its physical lift so that

\[
T_{i+L_\nu}=\rho T_i.                                    \tag{2.1}
\]

There is a scalar cyclic word c_nu of length kL_nu such that

\[
T_i=\{x\in\mathbb Z_k:c_{\nu,i-xL_\nu}=1\}.              \tag{2.2}
\]

Before normalizing the unit voltage, write alpha_j,beta_j for the coordinate
deleted and inserted at quotient transition j.  The coordinate-zero start
and end seams are exactly

\[
s_j=j-L_\nu v_\nu^{-1}\beta_j,\qquad
e_j=j-L_\nu v_\nu^{-1}\alpha_j
\pmod {kL_\nu}.                                          \tag{2.2a}
\]

Their cyclic alternation forces the lifetime matching: each start is paired
with the next end, not with a separately chosen matching.

It has exactly L_nu one-runs.  If their chronological starts and ends are
S_{\nu,t},E_{\nu,t}, put

\[
\ell_{\nu,t}=E_{\nu,t}-S_{\nu,t}+1,\qquad
g_{\nu,t}=S_{\nu,t+1}-E_{\nu,t}-1.                       \tag{2.3}
\]

Then:

1. the start residues and end residues modulo L_nu are each permutations
   of Z_(L_nu);
2. the exact mass equations are

   \[
   \sum_t\ell_{\nu,t}=rL_\nu,\qquad
   \sum_tg_{\nu,t}=(r-1)L_\nu;                           \tag{2.4}
   \]

3. positive D-residence on this component is equivalent to
   min_t ell_(nu,t)>=D;
4. zero D-residence is equivalent to min_t g_(nu,t)>=D.

The whole physical factor is one Hamilton cycle if and only if its quotient
has one cycle of total length

\[
N=\binom{k}{r}/k
\]

and that cycle has unit voltage.  Exact lower q1 additionally requires the
N adjacent-intersection representatives to be pairwise rotation-inequivalent.
Upper q1 completeness is the literal orbit-union condition on all adjacent
unions.

#### Proof

On every quotient transition orbit, exactly one of its k physical lifts
inserts coordinate zero and exactly one deletes it.  Hence the start and
end seam sets contain one point in each residue class modulo L_nu.
Filling the arcs from each start to the next end gives c_nu and (2.2);
the converse reconstructs the component and every Johnson transition.
Coordinate homogeneity gives rL_nu occupied states and (r-1)L_nu omitted
states for coordinate zero, proving (2.4).  The maximal one- and zero-arcs
are exactly the positive and zero coordinate runs, proving the residence
statements.

A quotient cycle of voltage v lifts to gcd(k,v) physical cycles.  Thus one
physical Hamilton cycle is equivalent to one quotient cycle of length N and
unit voltage.  Rotation is free on the middle and lower-q1 ranks, so physical
middle and lower ownership are exactly the two quotient orbit-injectivity
tests.  Upper support must use its actual orbit union because k may be
composite.  \(\square\)

### Corollary 2.2 (exact k15 eligible target)

A C_15-equivariant eligible parent at k15 is exactly a quotient Hamilton
cycle of length 429 and unit voltage whose normalized run schedule satisfies

\[
\ell_t\ge4,\qquad g_t\ge4,                               \tag{2.5}
\]

\[
\sum_{t=0}^{428}\ell_t=3432,\qquad
\sum_{t=0}^{428}g_t=3003,                               \tag{2.6}
\]

with both start and end residues permutations of Z_429, middle and lower-q1
orbit injectivity, and complete upper-q1 orbit support.

Equivalently, in the deletion/insertion stream of the unique quotient
cycle, the two residence conditions are the six exact inequalities

\[
\beta_i\notin\{\alpha_{i+1},\alpha_{i+2},\alpha_{i+3}\},
\qquad
\alpha_i\notin\{\beta_{i+1},\beta_{i+2},\beta_{i+3}\}
\tag{2.6a}
\]

for every cyclic index (i).  At upper depth (q), the literal flag is

\[
U_i^{(q)}=T_i\cup\{\beta_i,\ldots,\beta_{i+q-1}\}.       \tag{2.6b}
\]

Thus all-depth upper completeness, when required, is the actual orbit-union
condition on the flags (2.6b); it is not a consequence of (2.6a).  The
two-parent one-rung theorem needs only the (q=1) instance, while the saved
factor initially supplies the complete audited tower.

The scalar composition equations themselves have ample surplus:

\[
\sum(\ell_t-4)=1716,\qquad \sum(g_t-4)=1287.             \tag{2.7}
\]

Thus there is no scalar mass obstruction; the obstruction is transport from
the frozen factor while retaining ownership and upper providers.

## 3. The exact schedule of F_0

For the large quotient component, the positive lifetimes all satisfy

\[
\ell_t\ge4,\qquad \sum_t\ell_t=8\cdot426=3408.           \tag{3.1}
\]

Its short zero gaps are

\[
g=1^{22}2^{39}3^{73},                                   \tag{3.2}
\]

so exactly 134 of its 426 quotient gaps violate (2.5).  The other gaps have
length at least four and the total gap mass is

\[
\sum_tg_t=7\cdot426=2982.                               \tag{3.3}
\]

The three-cycle is already biresident:

\[
\ell=(7,7,10),\qquad g=(6,6,9).                          \tag{3.4}
\]

All dual defects therefore lie on the 426-cycle.  In the physical lift,
(3.2) becomes

\[
1^{330}2^{585}3^{1095}=2010                             \tag{3.5}
\]

short zero-runs.

## 4. Closed collars and the exact support certificate

A short gap of length s in {1,2,3} has local trace

\[
1\,0^s\,1.
\]

Its closed old-edge collar consists of the s+1 transitions from the
left boundary edge through the right boundary edge.

### Lemma 4.1 (forced collar)

Let F' be any degree-two factor on the same middle vertices.  If F' retains
every old edge of one closed collar, then the old subpath is forced in F',
up to reversal, and the same zero-run of length s remains.  Hence every
zero-resident replacement deletes at least one old edge from every closed
collar.

#### Proof

Every internal vertex of the retained collar already has both incident
factor edges fixed.  Degree two therefore forces the entire old subpath,
in one of its two orientations.  Its coordinate trace is 1 0^s 1 or its
reversal, so the short maximal zero-run persists.  \(\square\)

The 134 quotient collars are circular intervals on Z_426 with size
histogram

\[
2^{22}3^{39}4^{73}.                                     \tag{4.1}
\]

The frozen circular-interval certificate gives

\[
\boxed{\tau=82.}                                         \tag{4.2}
\]

One attaining quotient transversal is

\[
\begin{split}
\{&0,16,20,22,26,30,35,42,47,63,66,69,77,83,86,89,95,98,\\
&104,110,119,128,135,139,141,147,154,158,161,167,171,173,\\
&176,180,183,191,195,201,210,213,216,219,228,232,237,242,\\
&247,252,257,261,268,275,279,283,286,290,296,301,306,309,\\
&313,319,326,330,334,338,346,352,364,368,371,375,379,383,\\
&389,392,400,404,408,412,421,424\}.
\end{split}                                              \tag{4.3}
\]

The lower bound has the following compact exact certificate.  Take the
collar

\[
J=\{97,98,99,100\}.
\]

Every transversal contains some (p\in J).  Condition on (p), discard
the collars containing (p), cut the circle immediately after (p), and
apply the right-end greedy algorithm to the resulting line intervals.  For
(p=97,98,99,100), respectively, the greedy algorithm returns

\[
81,quad81,quad82,quad82
\]

pairwise disjoint remaining collars.  These disjoint families are dual
certificates for line-interval covering.  Adding the conditioned point
gives conditional lower bounds (82,82,83,83).  Hence every circular
transversal has size at least 82, while (4.3) proves equality.

Lifting (4.3) through all fifteen rotations deletes 1230 physical edges and
hits all 2010 physical collars.  An independent physical interval dual also
has size 1230.  Therefore this support bound is sharp as a collar
transversal, although the displayed set is not asserted to extend to a new
factor.

## 5. Hamilton connectivity adds one more orbit

All collars in Section 4 lie on the large component.  A connected
replacement must also delete an old edge of the defect-free 45-cycle.

### Theorem 5.1 (dense eligible-repair lower bound)

Let F' be a lower-q1-exact, zero-resident Hamilton factor on the same
physical middle vertices as F_0.

Then

\[
|E(F_0)\setminus E(F')|\ge1231,                          \tag{5.1}
\]

\[
|E(F')\setminus E(F_0)|\ge1231,\qquad
|E(F_0)\triangle E(F')|\ge2462.                          \tag{5.2}
\]

If F' is C_15-equivariant, these sharpen to

\[
\boxed{|E_Q(F_0)\setminus E_Q(F')|\ge83,}                \tag{5.3}
\]

\[
|E(F_0)\setminus E(F')|\ge1245,\qquad
|E(F_0)\triangle E(F')|\ge2490.                          \tag{5.4}
\]

Here E_Q denotes quotient edge orbits.

#### Proof

Lemma 4.1 and (4.2) force 1230 physical old-edge deletions, or 82 quotient
orbits, on the large component.  If every edge of the small cycle were
retained, its vertices would remain a closed degree-two component, so
Hamilton connectivity forces at least one further old-edge deletion there.
Equivariance deletes its whole fifteen-edge orbit.

Every old factor edge has a distinct lower-q1 colour.  A lower-q1-exact
replacement must restore each deleted colour on a new edge, so the number
of additions is at least the number of deletions.  This proves all four
bounds.  \(\square\)

Thus any eligible equivariant parent differs from the solved factor on more
than 19 percent of all quotient owners.  This is not a bounded seam repair.

## 6. Consequences for alternating trades

Represent a lower-q1-exact Johnson factor as a degree-two spanning subgraph
of the inclusion graph between ranks seven and eight.  Every exact
degree-preserving trade is an alternating-circuit packet in this graph.

Consider a sequence of exact quotient trades

\[
F_0,F_1,\ldots,F_t=F'.
\]

Let d_j be the number of old quotient factor edges deleted at step j,
counting every deletion even if an edge is later reinserted.

### Corollary 6.1 (bounded-trade obstruction)

Every sequence ending at an equivariant eligible parent satisfies

\[
\sum_{j=1}^t d_j\ge83.                                  \tag{6.1}
\]

If each trade deletes at most b quotient edges, then

\[
\boxed{t\ge\left\lceil\frac{83}{b}\right\rceil.}         \tag{6.2}
\]

In particular:

* alternating C6 trades, with b=3, require at least 28 trades;
* support-at-most-eight trades require at least 11 trades;
* a packet of at most ten support-eight trades cannot succeed.

For non-equivariant physical C6 trades, (5.1) gives at least 411 trades.

#### Proof

Every old edge absent from F' must be deleted at some step, so the final
old-edge deletion set is contained in the union of the stepwise deletion
sets.  Sum multiplicity only increases its size.  Apply (5.3), or (5.1) in
the physical case.  \(\square\)

This is sharp in total collar-hitting support, not in the number of
circuits.  A single alternating circuit can be macroscopic.  The theorem
therefore rules out bounded-local packets and leaves one dense circuit or a
dense overlapping packet open.

### Theorem 6.2 (single-circuit parity)

In the fixed-M0 quotient matching model, any one connected alternating
circuit that changes the 426+3 factor into one quotient component has even
support.  Consequently a one-circuit eligible repair has quotient support
at least 84 and must have unit final voltage.

#### Proof

Write the old quotient factor permutation as

\[
\sigma=M_0^{-1}P;
\]

it has cycles C_426 and C_3.  A connected alternating circuit is one
s-cycle pi on its support S, and the new factor permutation is sigma pi.
To merge the two old cycles, S meets both.  The next-S return permutation
rho on the old cycles therefore has t=2 cycles.  A Hamilton quotient output
has h=1 new return cycle.

The circuit/old-component ribbon has one black circuit, two white old
components, one connected orbit and one new boundary.  Euler's identity is

\[
1+2+1=s+2-2g
\]

for a nonnegative integer genus g.  Hence

\[
s=2+2g
\]

is even.  The support bound (5.3) gives s>=83, so parity gives s>=84.
A one-cycle quotient lifts to one physical Hamilton cycle only when its
voltage is coprime to 15.  \(\square\)

The parity conclusion also survives a phase-valued lift.  If a quotient
primitive of row support (s) lifts to
(k_0=\gcd(15,\delta)) physical alternating circuits, then (k_0) is odd.
On the physical ribbon, the old return permutation has two cycles, the
output has one, and the incidence is connected, so Euler's identity is

\[
k_0+2+1=15s+2-2g.
\]

Hence (15s=k_0+1+2g), and (s) is again even.  In particular, a
successful one-primitive repair has at least 84 deleted quotient rows, at
least 1260 deleted physical edges, and physical symmetric difference at
least 2520.

## 7. Upper-palette and load-drift obligations

The old upper-q1 load histogram is

\[
1^{3675}2^{1230}3^{100}.                                \tag{7.1}
\]

There is a subfamily of 18 quotient bad collars all of whose possible cut
edges carry globally unique upper colours.  Its exact transversal number is
16.  Therefore every equivariant zero-residence repair that remains
upper-q1 complete must add providers for at least 16 lost unique upper
colour orbits.

The exact-cardinality frontier is sharper at minimum support: every
82-edge quotient transversal of all large-component collars loses at least
19 upper-colour orbits having exactly one old quotient-edge-orbit provider.
Consequently an eligible repair attaining the lower bound 83 in (5.3)
needs at least 19 new upper-colour provider orbits, even if the
small-component cut uses its load-three edge.  This is a quotient-provider
statement: a short-period colour orbit can have physical multiplicity
greater than one even though it has only one old quotient provider orbit.

The complete projected frontier near the minimum is exact.  Let b be the
number of selected large-component rows.  The minimum singleton losses are

\[
u_{82}=19,\quad u_{83}=18,\quad u_{84}=17,\quad
u_b=16\quad(85\le b\le110).                              \tag{7.1a}
\]

The three small-component quotient rows are 152,315,318; row 318 has
upper-provider-orbit load three and the other two have load one.  Selecting
a of them has minimum extra singleton loss a-1.
Thus at total support s the projected minimum is

\[
\min_{\substack{1\le a\le3\\b=s-a\ge82}}(u_b+a-1),
\tag{7.1b}
\]

which equals

\[
\begin{array}{c|cccc}
s&83&84&85&86,\ldots,111\\ \hline
\text{minimum singleton losses}&19&18&17&16.
\end{array}                                              \tag{7.1c}
\]

In particular the minimum one-circuit support 84 from Theorem 6.2 forces at
least 18 new singleton-colour providers.  These numbers are sharp for the
cut-set projection; extension of an attaining cut set to one legal
alternating circuit is not asserted.

There is also a qualitative no-go.  Let

\[
E_q=\sum_i\bigl((8+q)-|\bigcup_{a=0}^{q}T_{i+a}|\bigr).
\]

For a strict or multi-spiral schedule,

\[
E_q=15\sum_t(q-g_t)^+.                                  \tag{7.2}
\]

On F_0,

\[
(E_2,E_3,E_4)=(330,1245,3255).                          \tag{7.3}
\]

The short-gap counts are the second differences

\[
R_s=E_{s+1}-2E_s+E_{s-1}\quad(s=1,2,3),                 \tag{7.4}
\]

with E_0=E_1=0.  Thus (7.3) recovers exactly

\[
(R_1,R_2,R_3)=(330,585,1095).                           \tag{7.5}
\]

### Corollary 7.1 (load-neutral no-go)

A trade sequence preserving the upper-window rank-load vector through
depth four cannot repair zero residence.  Every successful
upper-support-preserving packet must be load-nonneutral.

This separates upper support, which may remain complete, from upper
multiplicity data, which must change.

## 8. Exact remaining finite gate

The minimum surviving equivariant construction must simultaneously:

1. delete at least 82 old quotient edges hitting every large-component
   collar and at least one old edge of the three-cycle;
2. add the same number of lower-colour-restoring edges;
3. restore at least 16 unique upper-colour orbits, or at least 19 at total
   deletion support 83;
4. produce one quotient cycle of length 429 and unit voltage;
5. produce a run-transversal schedule satisfying (2.5)-(2.6);
6. retain complete upper-q1 support.

If it is one connected alternating circuit, condition 1 strengthens to even
support at least 84 and condition 3 strengthens to at least 18 singleton
upper-colour restorations.

The first three conditions are exact certified necessities.  They are not
sufficient: new edges can create new short runs, the alternating circulation
can have the wrong topology or voltage, and rankwise palette restoration
does not imply a common chronology.

The already frozen protected-switch atlas gives a compatible local warning:
no connected alternating cycle of quotient support at most eight preserves
the two immutable short decks and joins the 426+3 factor, and no row-disjoint
pair of support-at-most-six primitives succeeds.  The new support theorem is
stronger for biresidence: no final eligible repair can have total old-edge
deletion support below 83, regardless of how its circuits are grouped.

The exact open object is therefore a dense, upper-support-preserving but
load-changing alternating circulation.  No packet of total quotient support
below 83 can produce it.

## 9. Frozen certificate and scope

The interval and palette claims are independently replayed in

    scratch/audit_k15_complement_braid_obstruction_20260729.py

with SHA-256

    36bf1a8f807914e47789a5c61b0dbc3f910ad9d3c11e511d63784de328ac7094

and

    scratch/k15_complement_braid_obstruction_20260729.audit.json

with SHA-256

    15719ccba1186e2c95e99d7acf1e891e449718b77333faaae3a49704d039bd85

The output records the quotient collar histogram, the 82-set (4.3), the
physical optimum 1230, the unique-colour quotient transversal of size 16,
the minimum unique-loss frontier 19,18,17,16 at exact full-transversal
sizes 82,83,84,85, and the moment vector (7.3).

No new exhaustive search or SAT computation is used here.  The theorem
does not exclude:

* one macroscopic alternating circuit;
* a dense overlapping packet whose individual trades are few but large;
* leaving C_15 equivariance;
* constructing an eligible parent from another starting factor;
* using distinct two-parent rails, one only positive-resident and the other
  only zero-resident, rather than manufacturing one biresident parent.

It proves that the saved 426+3 factor has no bounded-local path to
eligibility and identifies the exact minimum support and palette obligations
of every surviving repair.

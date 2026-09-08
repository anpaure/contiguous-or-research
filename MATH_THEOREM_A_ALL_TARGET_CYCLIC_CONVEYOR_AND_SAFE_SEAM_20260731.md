# All-target PBBS protection by a cyclic colour-back/key-forward conveyor

Date: 2026-07-31  
Lane: A, pure mathematics  
Status: unconditional implication and exact obstruction for the one-cut,
full-fragment conveyor architecture.  The port-cycle and safe-seam hypotheses
are not proved for every PBBS factor, so this note does **not** prove
\(\nu(k)=B(k)\).

## 1. Setup

Let

\[
                    F=C_1\sqcup\cdots\sqcup C_b
\]

be an owner-disjoint directed cycle factor in \(J(k,r)\).  Assume its lower
edge colours are exact: every required rank-\((r-1)\) colour occurs on exactly
one factor edge.  Let \({\cal U}_F\) be the upper targets covered by \(F\)
and let \({\cal H}_F\) be its source holes in the required upper universe.
For every \(Y\in{\cal U}_F\), fix one old directed fixed-width geodesic
occurrence \(I_Y\) on one of the components.  This is an assignment of one
witness to **every previously covered target**, not merely to a provisional
casualty list.

Assume \(b\ge2\).  Conveyor arcs below join different owner components;
re-installing a component's own deleted edge as a loop is not counted as a
conveyor seam.

On component \(C_i\), select a directed cut edge

\[
                         e_i=t_i s_i
\tag{1.1}
\]

and let \(Q_i=(s_i,\ldots,t_i)\) be the resulting full fragment.  Put

\[
        c_i=t_i\cap s_i,\qquad \kappa_i=t_i\setminus s_i.
\tag{1.2}
\]

Thus \(c_i\) is the deleted lower colour and \(\kappa_i\) is the departure
key.  Assume that \(e_i\) is a protected wedge flank in the following exact
sense:

> if the assigned occurrence \(I_Y\) on \(C_i\) uses \(e_i\), then it is the
> outward ray
> \[
>                 (t_i,s_i,u_{i,2},\ldots,u_{i,q}),
> \tag{1.3}
> \]
> and its running union grows by one at every edge.

The corrected wedge-ray theorem gives precisely this conclusion for a
fixed-width PBBS witness which is killed by a selected wedge flank.

Renumber the selected states in a proposed cyclic component order.  Indices
below are modulo \(b\).

## 2. The cyclic conveyor theorem

### Theorem 2.1 (all-target cyclic conveyor)

Suppose that, for every \(i\),

\[
 \boxed{
 t_i\cap s_{i+1}=c_i,
 \qquad
 \kappa_{i+1}\in t_i.}
\tag{2.1}
\]

Then replacing the cut edges by the cyclic seams

\[
                         a_i=t_i s_{i+1}
\tag{2.2}
\]

has all of the following properties.

1. The new chronology \(\widehat C=Q_1|\cdots|Q_b|\) is one owner cycle:
   every old middle owner occurs exactly once.
2. Its lower \(q=1\) colour multiset is exactly the old one.
3. Every previously covered upper target \(Y\) still has a literal interval
   witness on \(\widehat C\).

Thus (2.1) is an exact **colour-back/key-forward** rule: seam \(a_i\)
recycles the source cut colour \(c_i\), while its source endpoint carries the
departure key needed by component \(i+1\).

#### Proof

The first equality in (2.1) has rank \(r-1\), so \(a_i\) is a Johnson edge
of lower colour \(c_i\).  The components have disjoint owner sets, hence its
endpoints are distinct.  Cutting each component once and cyclically joining
the resulting paths therefore gives one cycle containing every owner once.

The old cut colours \(c_1,\ldots,c_b\) are distinct, because the old factor
is lower-rainbow.  We delete exactly those occurrences and add seam \(a_i\)
with colour \(c_i\).  The lower palette is consequently unchanged, including
multiplicity.

Now fix an arbitrary previously covered upper target
\(Y\in{\cal U}_F\), and consider its assigned old occurrence.  If its span
avoids the selected cut, it remains internal to
the corresponding fragment.  Otherwise (1.3) applies on, say, component
\(i\).  The incoming seam is \(t_{i-1}s_i\).  By (2.1),
\(t_{i-1}\sim s_i\) and \(\kappa_i\in t_{i-1}\).  Since
\(\kappa_i\notin s_i\), it is the unique element of
\(t_{i-1}\setminus s_i\), and hence

\[
 t_{i-1}\cup s_i=s_i\cup\{\kappa_i\}=t_i\cup s_i.
\tag{2.3}
\]

Replacing the first vertex \(t_i\) of (1.3) by \(t_{i-1}\) therefore leaves
the union of the entire ray unchanged.  The literal interval

\[
                (t_{i-1},s_i,u_{i,2},\ldots,u_{i,q})
\tag{2.4}
\]

on \(\widehat C\) witnesses \(Y\).  This argument applies to the assigned
witness of every target in \({\cal U}_F\).  \(\square\)

The theorem is stronger than a post hoc service theorem for a displayed
hole list: its quantifier ranges over the complete old upper tower.

### Corollary 2.1A (zero-net-hole cyclic completion)

If, in addition, every source hole \(Y\in{\cal H}_F\) has a selected literal
suffix/full-fragment/prefix interval on \(\widehat C\), then
\(\widehat C\) covers the entire required upper universe.  Thus source-hole
service and preservation of all old targets are simultaneous, not two
separate audits.

#### Proof

Theorem 2.1 retains every target of \({\cal U}_F\), while the additional
interval bank supplies every member of its complement \({\cal H}_F\).
\(\square\)

The two clauses in (2.1) have a strong algebraic consequence which is easy
to miss.

### Theorem 2.2 (common-key/Johnson-colour normal form)

Assume \(b\ge2\).  Every cyclic conveyor satisfying (2.1) has one common departure coordinate
\(\kappa\):

\[
                        \kappa_1=\cdots=\kappa_b=\kappa.
\tag{2.5}
\]

Moreover its cut colours are distinct and cyclically consecutive in
\(J([k]\setminus\{\kappa\},r-1)\) (a simple cycle when \(b\ge3\)), and the endpoints have the
exact form

\[
 \boxed{
       t_i=c_i\cup\{\kappa\},
       \qquad s_i=c_{i-1}\cup c_i.}
\tag{2.6}
\]

Conversely, a cyclic sequence of distinct adjacent colours \(c_i\) avoiding
\(\kappa\), together with protected component cuts having endpoints (2.6),
satisfies (2.1).

#### Proof

From \(t_i\cap s_{i+1}=c_i\), write

\[
        t_i=c_i\cup\{\kappa_i\},\qquad
        s_{i+1}=c_i\cup\{z_i\},
\tag{2.7}
\]

where \(z_i\ne\kappa_i\).  The destination key \(\kappa_{i+1}\) is absent
from \(s_{i+1}\).  Since it lies in \(t_i\) by (2.1), it cannot lie in
\(c_i\subset s_{i+1}\), and (2.7) forces
\(\kappa_{i+1}=\kappa_i\).  Going around the cycle proves (2.5).

The destination cut colour \(c_{i+1}=t_{i+1}\cap s_{i+1}\) is an
\((r-1)\)-subset of \(s_{i+1}\), as is \(c_i\).  They are distinct because
the old lower palette is exact.  Hence they are the two distinct facets of
the rank-\(r\) set \(s_{i+1}\):

\[
 |c_i\cap c_{i+1}|=r-2,
 \qquad s_{i+1}=c_i\cup c_{i+1}.
\tag{2.8}
\]

Both omit \(\kappa\), while \(t_i=c_i\cup\{\kappa\}\), proving (2.6).
The converse follows by taking intersections in (2.6); the predecessor
endpoint contains the common destination key. \(\square\)

When \(b=2\), (2.6) gives \(s_1=s_2=c_1\cup c_2\), contradicting
owner-disjointness.  Hence no strict two-component cyclic conveyor exists;
the first realizable strict cyclic case has \(b\ge3\).

Thus the conveyor is not a collection of independently chosen departure
keys.  It is a common-key lift of a cut-colour Johnson cycle.  In
particular, the architecture is impossible if no coordinate \(\kappa\) has
a protected port on every component, or if the corresponding component-
transversal colour states contain no required cyclic Johnson colour walk.
This is an unconditional algebraic obstruction, before any target or
residence test.
Explicitly, if

\[
 K_i=\{x\in[k]:C_i\text{ has an admissible protected cut with departure
 key }x\},
\tag{2.9}
\]

then

\[
                         \bigcap_{i=1}^b K_i\ne\varnothing
\tag{2.10}
\]

is necessary.  It is not asserted sufficient: the colour-cycle, residence,
and safe-seam constraints remain.

The equality propagation in the proof uses only connectedness, not cyclic
closure.  Hence every connected linear strict colour-back/key-forward
conveyor also has one common key, and its consecutive cut colours form the
corresponding simple Johnson path.

## 3. Exact extraction of a linear braid

Assume throughout this section that the cyclic conveyor satisfies the
source-hole hypothesis of Corollary 2.1A, so that \(\widehat C\) covers the
full required upper universe.  Without this assumption, every statement in
this section remains exact only relative to the targets already covered by
\(\widehat C\).

For a target \(Y\), let \({\cal I}_{\widehat C}(Y)\) be all its
occurrence-labelled cyclic interval witnesses on the conveyor cycle, and put

\[
 K_{\widehat C}(Y)=
       \bigcap_{I\in{\cal I}_{\widehat C}(Y)}\operatorname{span}(I).
\tag{3.1}
\]

### Theorem 3.1 (safe-seam extraction)

Delete one conveyor seam \(a_h\), producing a linear owner chronology
\(T_h\).  Then:

* every upper target remains covered if and only if
  \[
                  a_h\notin K_{\widehat C}(Y)
                  \quad\hbox{for every required }Y;
  \tag{3.2}
  \]
* the lower \(q=1\) ledger of \(T_h\) is exactly
  \[
                         H=1,\qquad E=0,
  \tag{3.3}
  \]
  with sole missing colour \(c_h\);
* every middle owner still occurs exactly once.

#### Proof

A cyclic interval becomes a linear interval after deleting \(a_h\) exactly
when its span avoids \(a_h\).  This proves the necessary and sufficient
condition (3.2).  The cyclic conveyor has the exact old lower palette by
Theorem 2.1.  Deleting \(a_h\), whose colour is \(c_h\), deletes its unique
occurrence and changes no other adjacency; this proves (3.3).  Deleting an
edge changes no vertex. \(\square\)

For canonical one-cut PBBS fragments, site homomesy gives

\[
                         V(Q_i)=[k],\qquad I(Q_i)=\varnothing.
\tag{3.4}
\]

Consequently a proper upper target cannot have a witness crossing two
conveyor seams: such an interval would contain a complete intervening
fragment and would have union \([k]\).

Let \(P(Y)\) be the set of seams crossed by witnesses for \(Y\), and let
\(\iota(Y)=1\) if \(Y\) has an internal-fragment witness.  Define a forced
seam only when

\[
                  \iota(Y)=0,\qquad P(Y)=\{a\};
\tag{3.5}
\]

in that case write \(\sigma(Y)=a\), and put

\[
                  \Sigma_* = \{\sigma(Y):\sigma(Y)
                                      \hbox{ is defined}\}.
\tag{3.6}
\]

### Corollary 3.2 (exact forced-seam obstruction)

For a full-fragment conveyor,

\[
 \boxed{a_h\hbox{ is safely removable }iff a_h\notin\Sigma_*.}
\tag{3.7}
\]

In particular, a zero-upper-loss linear opening exists if and only if

\[
                             \Sigma_*\ne\{a_1,\ldots,a_b\}.
\tag{3.8}
\]

This is the minimal obstruction inside the one-cut conveyor architecture:
every seam is the sole surviving provider of at least one target.  It is
sharp in both directions, not merely a counting bound.  Two useful
sufficient conditions are:

* every target has an internal witness or witnesses at two distinct seams;
  then every seam is removable;
* fewer than \(b\) targets have a unique seam provider; then at least one
  seam is removable.

#### Proof

By (3.4), a proper target witness is internal or crosses one uniquely
determined seam.  Thus every witness for \(Y\) crosses \(a_h\) precisely
when \(Y\) has no internal witness and its set of seam positions is the
singleton \(\{a_h\}\).  Combine this observation with Theorem 3.1.  The
full target \([k]\) has a witness inside every full fragment and creates no
exception. \(\square\)

The assigned PBBS witness system makes this obstruction destination-local.
Let \({\cal B}_i\) be the complete bundle of targets whose assigned old
witness uses cut \(e_i\); these are exactly the assigned witnesses replayed
through incoming seam \(a_{i-1}\).  For \(Y\in{\cal B}_i\), let
\({\cal A}_i(Y)\) be the set of all literal witnesses for \(Y\) on the
conveyor which avoid \(a_{i-1}\).

### Corollary 3.3 (exact old-tower guarded-bundle test)

\[
 \boxed{
 a_{i-1}\text{ is removable without losing any target of }{\cal U}_F
 \iff
 {\cal A}_i(Y)\ne\varnothing\quad(Y\in{\cal B}_i).}
\tag{3.9}
\]

#### Proof

Every target outside \({\cal B}_i\) has its selected witness either internal
to a fragment or replayed at an incoming seam different from
\(a_{i-1}\), so it already has a witness avoiding \(a_{i-1}\).  The targets
in \({\cal B}_i\) have exactly the alternatives listed in
\({\cal A}_i(Y)\).  Apply the witness-avoidance part of Theorem 3.1 to
\({\cal U}_F\). \(\square\)

Source holes are deliberately absent from \({\cal B}_i\), because they
have no old assigned witness.  Therefore (3.9) is an exact test only for
the previously covered tower.  To test removal against the full required
universe, one must additionally require every \(Y\in{\cal H}_F\) to have
a literal witness avoiding \(a_{i-1}\); equivalently, use the forced-seam
set \(\Sigma_*\) of Corollary 3.2 over the full universe.

Thus the candidate opening seam must be checked against more than a post hoc
hole list, but it need not be checked against unrelated targets one by one:
the exact guard universe is its complete assigned destination bundle, over
every depth.

Notice that a target-to-seam Hall condition is neither necessary nor the
right invariant: one seam can simultaneously restore an arbitrarily long
nested outward-ray tower.  The exact obstruction is sole-provider support,
not unit-capacity matching.

## 4. Residence is also an endpoint condition

For a fragment \(Q\) and coordinate \(x\), let \(s_x(Q)\) and \(p_x(Q)\)
be its terminal and initial positive-run lengths, with value zero when the
corresponding endpoint omits \(x\).

### Lemma 4.1 (local cyclic residence)

Fix \(d\ge1\).  Suppose:

1. every internal positive coordinate run in every \(Q_i\) has length at
   least \(d+1\);
2. every coordinate is present and absent somewhere in every \(Q_i\); and
3. for every conveyor seam,
   \[
       s_x(Q_i)+p_x(Q_{i+1})\in\{0\}\cup[d+1,\infty)
       \qquad(x\in[k]).
   \tag{4.1}
   \]

Then \(\widehat C\) is cyclically \(d\)-resident.  Deleting any seam gives a
linear chronology with no internal positive run of length at most \(d\).

#### Proof

Condition 2 prevents a positive run from crossing two seams.  Every cyclic
run is therefore internal to one fragment or is exactly the suffix-prefix
run measured in (4.1).  Conditions 1 and 3 prove cyclic residence.  Deleting
a seam can only turn a cyclic run crossing that seam into boundary pieces;
it creates no new internal run. \(\square\)

For one-cut PBBS fragments, condition 2 follows from site homomesy.  The
other two conditions are substantive and must not be inferred from
all-depth support.  If the construction uses the non-flat deadline
staircase rather than strict \(d\)-residence, replace (4.1) by the exact
associative run-summary transducer and the exact threshold inequalities;
Theorems 2.1 and 3.1 are unchanged.

### Lemma 4.2 (short-run pair locality under colour-back)

Suppose the strict colour-back equations hold and every fragment has at
least \(d\) owners.  Then every positive coordinate run of length at most
\(d\) meets at most one seam.  Consequently strict \(d\)-residence is
decided exactly by the internal fragment runs and the one-seam
suffix--prefix runs.

#### Proof

If an \(x\)-run crosses two seams, the intervening fragment \(Q_i\) is
\(x\)-full.  Hence \(x\in s_i\cap t_i=c_i\).  The outgoing colour-back seam
has intersection \(c_i\), so the first owner of the following fragment also
contains \(x\).  The run therefore contains every owner of \(Q_i\) and at
least one further owner, and has length at least \(|Q_i|+1\ge d+1\).
\(\square\)

In particular, for strict depth three, one-cut components of length at
least three have a genuinely pair-local residence test.  A non-flat
deadline staircase still needs its position-aware final transducer replay;
the lemma controls run length, not absolute deadline charge.

## 5. Constructive port-state criterion

Let \({\cal O}_i\) be a finite bank of admissible protected cut/orientation
states on component \(C_i\).  For a fixed cyclic component order, define a
Boolean relation

\[
 R_i\subseteq{\cal O}_i\times{\cal O}_{i+1}
\tag{5.1}
\]

by declaring \((p,q)\in R_i\) exactly when the corresponding endpoints
satisfy both equations (2.1) and, when strict residence is requested, the
collar inequalities (4.1).  Let \(M_i\) be its Boolean incidence matrix.

For a literal all-target construction, additionally fix an assignment

\[
                         \psi_H:{\cal H}_F\longrightarrow[b]
\tag{5.A}
\]

of every source hole to a destination component.  A relation edge into a
state \(q\) on component \(j\) is called **fully guarded** only when its
suffix--prefix service set contains the complete fibre
\(\psi_H^{-1}(j)\), in addition to replaying every assigned old casualty
of \(q\).  In the rest of this section, “legal” means fully guarded whenever
zero net holes are claimed; the matrices \(M_i\) are thinned accordingly.

There is a useful Hall stage before one asks for connectivity.  Fix one
common-key port state \(p_i\) on every component, and make a bipartite graph
on left and right copies of the components, joining left \(i\) to right
\(j\) when \(p_i\to p_j\) is a legal conveyor arc.  If

\[
                       |N(X)|\ge |X|
             \qquad(X\subseteq\{1,\ldots,b\}),
\tag{5.0}
\]

then Hall's theorem gives a perfect matching.  Interpreted as one outgoing
and one incoming arc at each component, it is a directed conveyor cycle
cover.  The proof of Theorem 2.1 applies componentwise to this cover: every
assigned old upper target is retained or replayed, every source-hole fibre
is installed by its destination's incoming seam, the lower palette is
exact, and all selected collar guards hold.  Hall alone does not make the
cover connected; Proposition 5.2 below is the needed fusion stage.

### Proposition 5.1 (exact fixed-order construction test)

A protected cyclic conveyor in that component order exists if and only if

\[
               \operatorname{tr}_{\mathbb B}
                    (M_1M_2\cdots M_b)>0,
\tag{5.2}
\]

where multiplication and addition are over the Boolean semiring.  A
positive diagonal term explicitly reconstructs the selected opening on
every component.  After reconstruction, (3.6) is the exact test for whether
one of its seams can be opened with zero upper loss.

#### Proof

Expanding a diagonal entry of the Boolean product gives states
\(p_i\in{\cal O}_i\) with
\((p_i,p_{i+1})\in R_i\) for every cyclic index.  These are exactly the
conveyor conditions.  The converse is the same expansion read backwards.
\(\square\)

This condition is an induction/transfer construction, rather than an
uncheckable appeal to marginal abundance.

There is a second constructive route which starts from a cycle cover and
fuses its cycles.  Let \(\Gamma_\kappa\) be the directed port graph whose
vertices are admissible protected openings with common key \(\kappa\),
parted by their owner component.  Put \(p\to q\) when the seam from the end
of \(p\) to the start of \(q\), on a different component, satisfies (2.1),
together with the requested residence collar and the fully guarded
destination service condition following (5.A).  By Theorem 2.2 this is
equivalently the physical lift of
an allowed transition between the two cut colours in
\(J([k]\setminus\{\kappa\},r-1)\).

### Proposition 5.2 (protected alternating-rectangle fusion)

Suppose a component-transversal selection of port states in
\(\Gamma_\kappa\) has a directed cycle cover.  Let

\[
                 p\to q,\qquad u\to v
\tag{5.3}
\]

be seams on two different cycles.  If the cross arcs

\[
                         p\to v,\qquad u\to q
\tag{5.4}
\]

also belong to \(\Gamma_\kappa\), then replacing (5.3) by (5.4):

1. merges the two owner cycles into one;
2. preserves the exact lower \(q=1\) palette;
3. preserves a literal witness for every assigned old upper target at every
   depth;
4. preserves every assigned source-hole fibre; and
5. preserves the imposed local residence collars.

#### Proof

The usual directed two-switch on arcs from two different cycles merges
them into one.  The switch changes no selected port state and no owner.
Both the old and new outgoing seam from \(p\) have colour \(c(p)\), and
the same holds for \(u\); hence the lower multiset is unchanged.  Every
component still has one incoming legal key-carrying seam.  The proof of
Theorem 2.1, applied at each destination, therefore replays every assigned
ray casualty, while old internal witnesses are untouched.  Membership of
the cross arcs in \(\Gamma_\kappa\) includes both the collar tests and the
fixed source-hole fibre of the destination, so the hole bank is preserved.
\(\square\)

This gives a genuine augmenting-circuit construction.  It also has a clean
Aharoni--Haxell sufficient condition.  Let
\({\cal D}_1,\ldots,{\cal D}_m\) be the cycles of the initial cover, fix a
tree \({\cal T}\) on these cycles, and for each tree edge \(e=ij\) let
\({\cal R}_e\) be the occurrence-labelled multigraph whose vertices are the
original seam occurrences of the cover and whose edges are the two-seam
supports, with their legal cross-arc certificates, of all rectangles joining
\({\cal D}_i\) to \({\cal D}_j\).  If, for every nonempty
\(J\subseteq E({\cal T})\),

\[
       \nu\!\left(\bigcup_{e\in J}{\cal R}_e\right)>2(|J|-1),
\tag{5.5}
\]

then the graph case of the Aharoni--Haxell rainbow-matching theorem selects
one rectangle from every \({\cal R}_e\), with all selected seam supports
pairwise disjoint.  Applying them in a leaf-to-root order of \({\cal T}\)
merges the cover into one protected conveyor cycle.  Disjointness ensures
that a later switch never deletes a seam reserved for another tree edge.
Proposition 5.2 proves all-target, lower-palette, and residence preservation
throughout.

Condition (5.5) is only sufficient, but it is a genuine all-target
Aharoni--Haxell condition: its objects are compound two-seam rectangles,
not individual target-to-seam assignments.  This distinction is essential
because one keyed seam services a whole nested tower.

### Corollary 5.3 (Hall--rectangle all-target braid)

Suppose, for one common key \(\kappa\), that:

1. a source-hole assignment (5.A) and component-transversal port choice
   satisfy the fully guarded Hall inequalities (5.0);
2. one resulting conveyor cycle cover has a contact tree satisfying (5.5);
3. the fused cycle has at least one seam outside \(\Sigma_*\); and
4. all selected ports and rectangle arcs carry the residence guards of
   Lemma 4.1.  For a non-flat deadline transducer, require instead that the
   complete state-labelled switched cycle and the finally opened path pass
   its exact replay; pairwise collars alone are not asserted sufficient.

Then deleting such a seam gives one linear owner chronology which covers
the full required upper universe, has exact lower ledger \(H=1,E=0\), and
satisfies the declared residence condition.

#### Proof

Hall gives the protected cycle cover.  The rainbow family of disjoint
rectangles supplied by (5.5) fuses it to one cycle by Proposition 5.2.
Theorems 2.1 and 3.1 and Lemma 4.1 then give the four asserted conclusions
in the strict-residence case; the stipulated final transducer replay gives
the corresponding non-flat conclusion.
\(\square\)

Pairwise Hall conditions do not replace (5.2).  Indeed, take three state
banks \({\cal O}_i=\{0,1\}\), let \(R_1,R_2\) be equality and \(R_3\) be
inequality.  Every \(R_i\) is a perfect matching and satisfies all
bipartite Hall inequalities, but a cyclic choice would require
\(p_1=p_2=p_3\ne p_1\).  Equivalently, the Boolean product has zero trace.
This is an abstract option-state obstruction; it is not asserted here to be
a realized PBBS obstruction.

There is also a useful jointly admissible SPILL criterion.  Let \(\mu\) be
any probability measure on tentative state tuples for a fixed order, let
\(A_i\) be failure of relation \(R_i\), fix a candidate opening seam \(a_h\),
and let \(B_Y^h\) be the event that every literal cyclic witness for \(Y\)
uses \(a_h\).  Then

\[
       \sum_i\mu(A_i)+\sum_Y\mu(B_Y^h)<1
\tag{5.6}
\]

implies a protected, resident conveyor for which \(a_h\) is safely
removable.  This follows immediately from the union bound.  Unlike a
product of marginal cut banks, (5.6) lives on complete state tuples and
therefore preserves the colour/key chronology coupling.

## 6. Exact boundary of the result

Canonical PBBS supplies:

* owner-disjoint lower-rainbow components;
* a fixed-width directed witness for every upper target at every depth;
* the wedge outward-ray classification; and
* full union and empty intersection of every one-cut component fragment.

It does not currently supply, in every dimension:

1. one coordinate \(\kappa\) carrying a protected opening on every component,
   and a component-transversal Hall/rectangle construction satisfying the
   common-key normal form (2.6);
2. the internal and seam-collar residence conditions (or the exact
   non-flat deadline substitute); or
3. a conveyor cycle with \(\Sigma_*\ne\{a_1,\ldots,a_b\}\); and
4. one source-hole assignment whose fibres survive the initial cycle cover,
   every fusion rectangle, and the final opening.

These four clauses are now the precise one-cut all-target gate.  If they
hold, Theorems 2.1 and 3.1 give literal owner chronology, complete upper
support, and the exact lower profile \(H=1,E=0\).  The remaining common-cap
compiler condition is separate and must still be checked on the same
chronology.

Conversely, if a realized conveyor has \(\Sigma_*\) equal to its entire seam
set, then **no choice of its linear opening seam** preserves the whole upper
tower.  This does not obstruct multiple cuts or a noncanonical
suffix/full/prefix repair, so it is sharply scoped rather than a purported
counterexample to exact equality.

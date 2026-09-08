# A 24-owner marked-C6 box is the minimal closed q2-resident three-state reset

**Date:** 2026-08-14  
**Status:** exact closed local theorem.  An 18-owner resident C6 router has
full first-return action `(b u c)` and marked quotient `(b c)`; adjoining one
six-owner identity cycle supplies a fixed tail spectator.  Both states use
the same simple owner/lower/upper bank and have zero lower and upper q2
current.  The canonical terminal cuts have phase-common depth-two stubs and
an explicit clock-disjointness collar criterion.  Both individual D5
terminal Venn types occur in a resource-simple rank-seven tapped box.
Simultaneous occurrence-level planting of the 212 reset rows is not claimed.

## 0. Outcome

The clean full-port parity obstruction does not apply after an auxiliary
port is hidden.  There is a literal closed bank with old and new return maps

\[
                 1_{\{a,b,u,c\}}
       \quad\hbox{and}\quad
                 1_a\times(b\ u\ c).                 \tag{0.1}
\]

Mark `a,b,c` and suppress the auxiliary socket `u`.  The marked
first-return maps are

\[
                 1_{\{a,b,c\}}
       \quad\hbox{and}\quad
                 1_a\times(b\ c).                    \tag{0.2}
\]

The router uses three six-owner cycles, and the fixed spectator uses a
fourth.  Thus the complete closed bank has 24 owners.  This is smallest in
the simple cyclic-owner model: every nonconstant q2-biresident component has
at least six owners, the identity phase needs three router components, and a
physical fixed spectator needs one more.

Unlike the earlier two-stage common-core carrier, this box does not cancel
its C6 action.  It uses one clean C6 seam and closes each of its three ports
by a resident six-owner return rail.

## 1. The 18-owner router

Fix a middle-owner rank `r>=5`.  Let `K` have size `r-2`, choose distinct

\[
       x_1,x_2,h\in K,
       \qquad y_1,y_2,z,a_0,a_1,a_2\notin K,          \tag{1.1}
\]

and read the `a` subscripts modulo three.  Put

\[
\begin{aligned}
 A_i&=K+z+a_i,\\
 B_i&=K+a_i+a_{i+1},\\
 P_{i,1}&=(K-x_1)+y_1+a_i+a_{i+1},\\
 P_{i,2}&=(K-x_1-x_2)+y_1+y_2+a_i+a_{i+1},\\
 Q_{i,0}&=(K-x_1-x_2)+y_1+y_2+z+a_i,\\
 Q_{i,1}&=(K-x_2)+y_2+z+a_i.
\end{aligned}                                           \tag{1.2}
\]

The old port cycle is

\[
 \mathcal C_i=(A_i,B_i,P_{i,1},P_{i,2},Q_{i,0},Q_{i,1}).
                                                               \tag{1.3}
\]

Every consecutive pair in `(1.3)` is a Johnson edge.  Replace the three
closing incidences

\[
                         A_iB_i
       \quad\longmapsto\quad A_iB_{i-1}.              \tag{1.4}
\]

The lower and upper resources of the direct seam are, respectively,

\[
 K+a_i,qquad K+z+a_i+a_{i+1},                       \tag{1.5}
\]

in the old state.  In the new state they are the same two indexed families
after cyclic reindexing.  Thus `(1.4)` is a literal alternating Boolean C6.

### Theorem 1.1 (full and marked return actions)

Before `(1.4)`, the three cycles have identity first-return map on the
distinguished ports.  Afterwards they form one 18-owner cycle and the
return map on the `A`-ports is

\[
                              i\longmapsto i-1.       \tag{1.6}
\]

Label `A_0=b`, `A_2=u`, and `A_1=c`.  Then `(1.6)` is `(b u c)`.
After marking only `b,c`, its first marked return is `(b c)`.

#### Proof

From `A_i`, the new seam enters `B_(i-1)` and follows the unchanged rail
through `P_(i-1,1),P_(i-1,2),Q_(i-1,0),Q_(i-1,1)` to `A_(i-1)`.
This proves `(1.6)`.  Starting at `b`, the first full return is `u` and the
next is `c`; starting at `c`, the first return is `b`.  Suppressing `u`
therefore gives the transposition. `square`

## 2. A physical fixed tail

On the same `(2r-1)`-point ground set choose a second core `K'` of size
`r-2` which omits `h`, two clock labels (x'_1,x'_2\in K'), and five
distinct labels (y'_1,y'_2,z',s_0,s_1) outside `K'`, all still omitting
`h`.  This is possible for `r>=5`: after deleting `h`, a core of size
`r-2` and five exterior labels use exactly `r+3<=2r-2` places.

Apply `(1.2)` with the primed data and the single active pair `s_0,s_1`.
Its six owners form one unchanged cycle \(\mathcal S\).  Mark one occurrence
on \(\mathcal S\) as the tail socket `a`.

Every router owner and each of its immediate lower and upper resources
contains `h`; every spectator resource omits `h`.  Hence the spectator is
resource-disjoint from the router on all three typed banks.  Its return map
is the identity in both phases.  Equations `(0.1)--(0.2)` follow.

If the ambient construction already supplies a protected fixed tail wire,
only the 18 router owners are new.  The count 24 is for a self-contained
physical four-port box.

## 3. Exact simplicity and q2 current

For a cyclic owner trace `V`, write

\[
\begin{aligned}
 L_1(V)&=\{V_j\cap V_{j+1}\}_j,&
 U_1(V)&=\{V_j\cup V_{j+1}\}_j,\\
 L_2(V)&=\{V_j\cap V_{j+1}\cap V_{j+2}\}_j,&
 U_2(V)&=\{V_j\cup V_{j+1}\cup V_{j+2}\}_j.
\end{aligned}                                           \tag{3.1}
\]

### Theorem 3.1 (one fixed simple bank and zero q2 current)

In both phases the complete 24-owner box has:

1. 24 distinct owners;
2. 24 distinct immediate-lower resources;
3. 24 distinct immediate-upper resources; and
4. 24 distinct lower-q2 and 24 distinct upper-q2 values.

The old and new occurrence multisets in every row of `(3.1)` are equal.
In particular both signed q2 currents are exactly zero, not merely
support-monotone.

#### Proof

Along one rail the prefix/suffix profile in `{x_1,x_2,y_1,y_2}` determines
the position.  The active profile then determines the port index.  At the
direct seam, `(1.5)` gives the same lower and upper indexed families in
both phases.  This proves owner/lower/upper simplicity and phase equality.
The marker `h` separates all router resources from the spectator resources.

Only two triple windows at each switched seam can change.  Directly from
`(1.2)`, their lower intersections are

\[
\begin{aligned}
 Q_{i,1}\cap A_i\cap B_i
   &=Q_{i,1}\cap A_i\cap B_{i-1}=(K-x_2)+a_i,\\
 A_i\cap B_i\cap P_{i,1}
   &=A_i\cap B_{i-1}\cap P_{i-1,1}=(K-x_1)+a_i.
\end{aligned}                                           \tag{3.2}
\]

Thus the lower occurrence current vanishes pointwise at every port.  The
complete six-value lower-q2 list on port `i` is

\[
\begin{array}{lll}
 (K-x_1)+a_i,&
 (K-x_1-x_2)+a_i+a_{i+1},&
 (K-x_1-x_2)+y_1+a_i,\\
 (K-x_1-x_2)+y_2+a_i,&
 (K-x_1-x_2)+z+a_i,&
 (K-x_2)+a_i.
\end{array}                                           \tag{3.3}
\]

The missing-clock and active-label signatures separate these values across
all positions and ports.

The old upper values at the two changed windows are

\[
 K+z+y_2+a_i+a_{i+1},qquad
 K+z+y_1+a_i+a_{i+1},                                \tag{3.4}
\]

while the new values are

\[
 K+z+y_2+a_{i-1}+a_i,qquad
 K+z+y_1+a_{i-1}+a_i.                                \tag{3.5}
\]

The complete six-value upper-q2 list before the switch is

\[
\begin{array}{lll}
 K+z+y_1+a_i+a_{i+1},&
 K+y_1+y_2+a_i+a_{i+1},&
 (K-x_1)+z+y_1+y_2+a_i+a_{i+1},\\
 (K-x_2)+z+y_1+y_2+a_i+a_{i+1},&
 K+z+y_1+y_2+a_i,&
 K+z+y_2+a_i+a_{i+1}.
\end{array}                                           \tag{3.6}
\]

Again the clock profile followed by the active singleton/pair separates all
18 router values.  Equations `(3.4)--(3.5)` are equal as occurrence
multisets by reindexing, and every other triple window is copied.  The
spectator is unchanged and `h`-disjoint, so its six distinct values on each
shore cannot collide with a router value.  This proves all claims. `square`

## 4. Internal residence and canonical terminal collars

On every old six-owner cycle, each nonconstant coordinate has cyclic run
pair `(3,3)`.  On the switched 18-owner cycle the four clock coordinates
and `z` still have repeated `(3,3)` runs, while each active `a_i` has run
pair `(9,9)`.  Therefore the exact minima on the owner trace are

\[
                       (\text{one run},\text{zero run})=(3,3). \tag{4.1}
\]

Passing to immediate-upper unions expands a positive run by one at each
boundary and shortens a zero run by one.  The exact upper minima are

\[
                                      (4,2).          \tag{4.2}
\]

The same `(3,3)` and `(4,2)` values hold on the spectator.  Hence both
closed phases are q2-biresident on the lower-owner and immediate-upper
traces.

There is a canonical place to open each router port: cut the unchanged
central rail edge

\[
                         P_{i,2}Q_{i,0}.              \tag{4.3}
\]

The changed seam `A_iB_j` is three edges away.  Thus no three-owner window
can meet both `(4.3)` and a changed seam.  The two local terminal stubs are

\[
       B_i,P_{i,1},P_{i,2}
       \qquad\hbox{and}\qquad
       Q_{i,0},Q_{i,1},A_i,                           \tag{4.4}
\]

and are literally identical in both phases.  Consequently every q2
intersection or union window crossing a fixed graft boundary is copied
exactly; the only changed q2 windows remain the internal zero-current
windows `(3.2)--(3.5)`.

For residence across an actual graft, orient the exterior path from the
`P_(i,2)` end to the `Q_(i,0)` end.  Let `S_1,S_2` be the supports of its
first two Johnson moves and `T_2,T_1` the supports of its last two moves,
with `T_1` adjacent to `Q_(i,0)`.  The two internal support pools adjacent
to either cut are

\[
                         \{x_1,y_1\},\qquad\{x_2,y_2\}. \tag{4.5}
\]

Hence the explicit sufficient terminal-collar guard is

\[
 (S_1\cup S_2\cup T_1\cup T_2)
       \cap\{x_1,x_2,y_1,y_2\}=\varnothing.           \tag{4.6}
\]

If the exterior is itself q2-biresident and `(4.6)` holds, then every triple
of consecutive support pools crossing either cut is pairwise disjoint: the
wholly exterior triples are controlled by exterior residence, and `(4.6)`
controls the one- and two-move mixed triples.  The lower-owner and
immediate-upper collar calculations giving `(4.1)--(4.2)` therefore
continue through the graft.

This is an exact interface criterion, not a proof that all 212 prescribed
D5 occurrences admit simultaneous clock-disjoint grafts.  Without `(4.6)`,
terminal residence must be checked on the actual connector.  At widths
beyond q2, independently fixed two-sided contexts are obstructed by the
resident-C6 private-marker theorem; no all-width exterior transparency is
claimed here.

## 5. Minimality

### Theorem 5.1 (18 plus 6 is sharp)

In a simple cyclic-owner box whose old phase has identity return on three
distinct C6 ports and whose owner traces are q2-biresident, the router uses
at least 18 owners.  If a fixed tail is supplied as a separate physical
q2-biresident orbit, the complete box uses at least 24 owners.

#### Proof

Adjacent owners in a simple Johnson cycle are distinct.  If every coordinate
were constant on a component, all of its owners would be the same set; hence
every component has a nonconstant coordinate.  Q2 biresidence gives that
coordinate a positive cyclic run of length at least three and a zero cyclic
run of length at least three.  The component therefore has length at least
six.

On a directed cycle containing two marked ports, first marked return sends
one to the other, so it is not the identity.  Identity first return on three
distinct ports therefore places them in three distinct old components,
contributing at least \(3\mathbin\times6=18\) owners.  A fixed physical
spectator is a fourth distinct marked-return component and contributes at
least six more.  Sections 1--4 attain both bounds. `square`

The 24-owner bound is architecture-relative: it allows no borrowed or formal
spectator and no repeated owner occurrence.  The 18-owner router bound itself
applies to every simple three-component q2-biresident first-return
realization, not just to the formulas in `(1.2)`.

## 6. What this changes in the D5 reset gate

The row-private D5 reset no longer lacks an abstract C6 switchbox.  The box
above satisfies, internally and under the collar guard `(4.6)`:

* one phase-independent simple owner/lower/upper bank;
* the exact action \(1_a\times(b\ c)\) after marked first return;
* q2 biresidence; and
* zero lower and upper q2 current.

### 6.1 Both D5 terminal types occur without a serial cable

At rank seven take

\[
 K=\{h,x_1,x_2,k_0,k_1\}                              \tag{6.1}
\]

and retain the router coordinates in `(1.2)`, together with two spare
labels `f_0,f_1`.  Put

\[
                 B=A_0,qquad U=A_2.                  \tag{6.2}
\]

For the adjacent-head type, choose

\[
                 C=A_1,qquad T=K+z+f_0.              \tag{6.3}
\]

Then

\[
 (d_J(T,B),d_J(T,C),d_J(B,C),|T\cap B\cap C|,
   |T\cup B\cup C|)=(1,1,1,6,9).                    \tag{6.4}
\]

For the distance-two-head type, tap a different phase of port one:

\[
 C=Q_{1,1}=(K-x_2)+y_2+z+a_1,qquad
 T=(K-x_2)+z+a_0+a_1.                                \tag{6.5}
\]

Now the tuple in `(6.4)` is `(1,1,2,5,9)`.  In either case the three marked
router sockets `B,U,C` lie one on each old port cycle.  Their old
first-return map is identity.  On the fused cycle their cyclic order is

\[
                             B\longmapsto U\longmapsto C\longmapsto B,
                                                               \tag{6.6}
\]

even though `C` in `(6.5)` is not at the same phase as `B,U`.  Suppressing
`U` gives `(B C)`.

There are also literal spectator cycles rooted at the displayed tails.  For
`(6.3)` use

\[
\begin{aligned}
 K'_1&=(K-h)+z,&(x'_1,x'_2)&=(k_0,k_1),\\
 (y'_1,y'_2,z',s_0,s_1)&=(a_0,a_1,f_0,h,f_1),        \tag{6.7}
\end{aligned}
\]

and for `(6.5)` use

\[
\begin{aligned}
 K'_2&=(K-\{h,x_2\})+z+a_1,&(x'_1,x'_2)&=(a_1,k_0),\\
 (y'_1,y'_2,z',s_0,s_1)&=(f_0,f_1,h,a_0,a_2).        \tag{6.8}
\end{aligned}
\]

Substitution in the six-owner formula makes the first spectator owner
exactly `T` in each case.  Comparing the explicit owner and the four lists
in `(3.1)` shows that all spectator q1 and q2 resources are simple and
disjoint from the router resources.  The replay checks this literal finite
comparison.

Adding `r-7` common core labels to every displayed owner and `r-7` unused
labels extends the construction from rank seven to every `r>=7`.  Conversely,
the two D5 signatures determine the Venn cells of an individual terminal
triple, so a coordinate relabelling maps every one such triple to `(6.3)` or
`(6.5)` at its ambient rank.

This proves individual **typed** terminal compatibility and removes the
separate serial-cable requirement.  It does not identify 212 occurrence
tickets in one factor: each relabelling chooses private clocks and spare
labels, and its exposed darts still require actual grafts satisfying
`(4.6)`.

### 6.2 Remaining coinstantiation rows

The sharp remaining rows are occurrence-level grafting and coinstantiation:

1. link the prescribed D5 tail and two head occurrences to `a,b,c` while
   hiding `u`;
2. realize `(4.6)` at every external seam, including the three roles of
   multiplicity four; and
3. plant all 212 boxes in one resource-simple protected bank.

The two local geometries in `(6.3)--(6.8)` prove that metric terminal type is
no longer an obstruction.  The unproved statement is their simultaneous
occurrence-level realization inside the frozen factor.

## 7. H100 replay

The independent verifier constructs the combined router and spectator for
every rank `5<=r<=40`.  It checks Johnson incidence, component counts, full
and marked return maps, simplicity and equality of all three q1 banks,
distinctness and equality of both q2 decks, seam formulas, and the exact
run/gap minima.

```text
verifier
  scratch/verify_d5_marked_c6_minimal_resident_reset_20260814.py
  SHA-256 bfc51de922d507ae86de1f88cafb919c3f34a0addc0f5b2e2adf518626f06336

H100 output
  scratch/verify_d5_marked_c6_minimal_resident_reset_20260814.h100.out
  SHA-256 24cd3b64a40f3c942a1961c00633c18adfc5ee104b87d58a5dc3c21cbcbef994
```

All execution and hashing occurred on H100.  The construction and
minimality proof are symbolic; the replay is an independent finite audit.

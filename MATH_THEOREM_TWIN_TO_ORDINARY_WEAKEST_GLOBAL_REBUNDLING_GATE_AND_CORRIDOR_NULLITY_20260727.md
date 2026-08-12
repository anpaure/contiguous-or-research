# The weakest twin-to-ordinary global re-bundling gate, and why paired corridors are presently interface-null

Date: 2026-07-27

Method: pure mathematics only.  No computation, finite search, solver,
probabilistic black box, or web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad
 r=m-q_0,\qquad
 D=H-q_0,
\tag{0.1}
\]

\[
 V_d=\binom{[n]}{r-d},\qquad
 N_d=|V_d|,\qquad
 W=\binom{2m}{m},
\tag{0.2}
\]

where

\[
                         q_0,H=\Theta(\sqrt m),
 \qquad q_0<H.
\tag{0.3}
\]

Let \(\mathcal A\subseteq V_0\) be the entrance family covered by a
domino-twin matching, with

\[
                         |\mathcal A|=N_0-L.
\tag{0.4}
\]

The literal split of every selected twin into its two ordinary component
cycles has floor-correct first-shadow excess

\[
 \widetilde E_1
 \ge\frac{N_0-L}{4}-O(W/\sqrt m).
\tag{0.5}
\]

Thus the twin split cannot feed the coefficient-one compiler.

This note gives the exact weakest remaining use of \(\mathcal A\).

### Gate GR (weak global re-bundling)

Discard or replace only a scalar-harmless entrance set, and cover the
retained entrance roots by a forest of ordinary cyclic-history paths
\(\mathscr P\).  If

\[
                         G'=|\operatorname{ent}\mathscr P|,
 \qquad
                         p=|\mathscr P|,
\tag{0.6}
\]

then require only

\[
 B(N_0-G')=o(W),
\tag{0.7}
\]

\[
 \boxed{
 \sum_{d=0}^{D}
 \left(
 \min\{G',N_d\}
 -|S_d(\mathscr P)|
 \right)=o(W),}
\tag{0.8}
\]

\[
                         Hp=o(W),
\tag{0.9}
\]

and \(o(W)\) expanded incidence cost for any literal exceptional
collars or discarded histories.

No exact factor at every depth, no rankwise independent matching, no
full-cycle decomposition, and no preservation of the old twin pairing
is required.  Conditions (0.7)--(0.9) are exactly the scalar,
correlated-support, and reset terms in the final length ledger.

### Theorem A (positive-density history reassignment is necessary)

Suppose the twin matching has \(T\) selected superpackets, so

\[
                         2nT=N_0-L=:G.
\tag{0.10}
\]

Compare any proposed ordinary rebundling with the two original component
history maps of those twins.  Let \(Q_1\) be the number of entrance
occurrences which are discarded or whose depth-one target is changed.
Then its floor-correct first-shadow excess satisfies

\[
 \boxed{
 \widetilde E_1
 \ge mT-Q_1-(G'-N_1)_+.}
\tag{0.11}
\]

Consequently every rebundling satisfying (0.8) must have

\[
 \boxed{
 Q_1\ge mT-o(W)
      =\frac G4-o(W).}
\tag{0.12}
\]

Thus at least a positive fraction of all entrance occurrences must
receive genuinely new ordinary histories.  A sparse retagging,
orientation change, or bounded number of local packet replacements
cannot suffice.

### Theorem B (paired-corridor nullity)

Any operation whose output is still a matching of intact domino-twin
superpackets remains subject to (0.5), regardless of how many critical
paired-corridor replacements or cluster choices were used to obtain it.
In particular:

1. replacing a twin by a close paired-corridor neighbour is
   interface-null;
2. quotienting all close neighbours of one twin into a cluster is
   interface-null if the chosen cluster representative is still a twin;
3. the exponent-\(1/2\) corridor census supplies alternative **twin
   columns**, not cross-parent ordinary splice columns.

Paired corridors become relevant only if one proves a new literal
cross-parent splice theorem which takes roots from several disjoint
selected twins and outputs non-twin ordinary histories satisfying
(0.8).  Such a theorem is already a concrete instance of Gate GR.

Therefore the present corridor technology does not weaken the ordinary
annulus problem.  After the twin decomposition is discarded, Gate GR
depends only on the entrance set \(\mathcal A\), not on how
\(\mathcal A\) was originally partitioned into twins.  The twin
matching supplies a large entrance set; it presently supplies no
usable history bundling.

## 1. Ordinary cyclic-history paths

Let

\[
                         \pi=(z_i)_{i\in\mathbb Z_n}
\tag{1.1}
\]

be a directed cyclic order of \([n]\), and write

\[
 I_\pi(i,k)
 =\{z_i,z_{i+1},\ldots,z_{i+k-1}\}.
\tag{1.2}
\]

An ordinary annular occurrence at phase \(i\) has entrance root

\[
                         X_0(\pi,i)=I_\pi(i,r)
\tag{1.3}
\]

and lower trace

\[
                         X_d(\pi,i)
 =I_\pi(i+d,r-d),
 \qquad 0\le d\le D.
\tag{1.4}
\]

Its upper trace is the complement image of (1.4).  Hence it is enough
to control the lower traces.

An **ordinary cyclic-history path** is a cyclic interval \(J\) of
phases in one order \(\pi\), together with all histories

\[
                         \{(X_d(\pi,i))_{d=0}^D:i\in J\}.
\tag{1.5}
\]

Full cyclic packets are the special case \(J=\mathbb Z_n\).  Allowing
proper \(J\)'s is strictly weaker and is legitimate for the compiler:
one pays one reset at each path boundary.

Let \(\mathscr P\) be a family of such paths whose entrance roots are
all distinct.  Put

\[
 \operatorname{ent}\mathscr P
 =\{X_0(\pi,i):(\pi,J)\in\mathscr P,\ i\in J\},
\tag{1.6}
\]

\[
 S_d(\mathscr P)
 =\{X_d(\pi,i):(\pi,J)\in\mathscr P,\ i\in J\}.
\tag{1.7}
\]

Every retained entrance occurrence produces exactly one target at every
depth.  Therefore all depth loads have the same total mass

\[
                         G'=|\operatorname{ent}\mathscr P|.
\tag{1.8}
\]

## 2. Why Gate GR is the weakest deterministic compiler statement

For every depth define the multiplicity

\[
 \mu_d(T)
 =|\{(\pi,J,i):i\in J,\ X_d(\pi,i)=T\}|.
\tag{2.1}
\]

Then

\[
                         \sum_{T\in V_d}\mu_d(T)=G'.
\tag{2.2}
\]

Let

\[
 E_d=\sum_{T\in V_d}(\mu_d(T)-1)_+,
\qquad
 H_d=N_d-|S_d(\mathscr P)|.
\tag{2.3}
\]

Since every positive load contributes one unit to the support,

\[
                         E_d=G'-|S_d(\mathscr P)|.
\tag{2.4}
\]

After removing the unavoidable scalar floor,

\[
\begin{aligned}
 \widetilde E_d
 &=E_d-(G'-N_d)_+\\
 &=\min\{G',N_d\}-|S_d(\mathscr P)|.
\end{aligned}
\tag{2.5}
\]

Consequently

\[
 \sum_{d=0}^{D}H_d
 =
 \underbrace{\sum_{d=0}^{D}(N_d-G')_+}_{B(N_0-G')}
 +
 \underbrace{\sum_{d=0}^{D}\widetilde E_d}_{\mathfrak C(\mathscr P)}.
\tag{2.6}
\]

This is an identity.  Complementation gives the identical upper bill.
Thus (0.7) and (0.8) are precisely the two nonnegative terms which must
be \(o(W)\).

The paths in \(\mathscr P\) can be concatenated after paying at most
\(2H\) boundary symbols per path.  Hence (0.9) is exactly the weakest
reset-scale condition in this path model.  Requiring full ordinary
cycles would imply

\[
                         p=G'/n=O(W/m)
\tag{2.7}
\]

and therefore (0.9), but full cycles are not logically needed.

This proves the following formulation.

### Proposition 2.1 (weakest sufficient rebundling theorem)

If the twin entrance set \(\mathcal A\) admits an ordinary history
forest satisfying (0.7)--(0.9), and all additional literal exceptional
incidences have expanded mass \(o(W)\), then the common-arrival
annulus compiler adds only \(o(W)\) length.

Conversely, within this ordinary-history/common-arrival architecture,
the exact hole ledger is (2.6).  Thus no weaker support statement than
(0.8) can imply an \(o(W)\) hole bill without using additional
support-redundancy information.

## 3. An exact packing formulation

Let \(\mathcal C\) be the catalogue of all allowed ordinary
cyclic-history paths.  For \(C\in\mathcal C\), write

\[
 E_0(C)\subseteq V_0
\tag{3.1}
\]

for its entrance roots and

\[
 E_d(C)\subseteq V_d
\tag{3.2}
\]

for its depth-\(d\) support.

The root-preserving version of Gate GR is the following integral
packing problem.  Choose

\[
                         z_C\in\{0,1\},
\qquad
                         y_{d,T}\in\{0,1\},
\tag{3.3}
\]

subject to

\[
 \sum_{C:X\in E_0(C)}z_C\le1
 \qquad(X\in\mathcal A),
\tag{3.4}
\]

\[
                         z_C=0
 \quad\text{if }E_0(C)\not\subseteq\mathcal A,
\tag{3.5}
\]

\[
 y_{d,T}
 \le
 \sum_{C:T\in E_d(C)}z_C
 \qquad(0\le d\le D,\ T\in V_d).
\tag{3.6}
\]

Put

\[
 G'=\sum_C|E_0(C)|z_C,
\qquad
 p=\sum_Cz_C.
\tag{3.7}
\]

The objective is to make

\[
 B(N_0-G')
 +
 \sum_{d=0}^{D}
 \left(
 \min\{G',N_d\}
 -\sum_{T\in V_d}y_{d,T}
 \right)
 +Hp
\tag{3.8}
\]

equal to \(o(W)\).  For fixed \(z\), maximizing the \(y\)'s makes
(3.6) exact at the support level.  Allowing a scalar-harmless symmetric
difference between \(\mathcal A\) and the selected entrance set merely
adds the corresponding entrance-change variables and their expanded
literal cost.

This is the precise global re-bundling problem.  It is not a matching
problem in the twin-packet hypergraph: its columns are ordinary history
paths, and its nonlinear difficulty is the common support union across
all depths.

## 4. Positive-density reassignment theorem

Let the selected twin superpackets be

\[
                         F_1,\ldots,F_T.
\tag{4.1}
\]

Choose any internal orientations and split \(F_j\) into complementary
ordinary component cycles

\[
                         P_j,\qquad P_j^\tau.
\tag{4.2}
\]

At odd entrance length \(r\), their entrance decks are disjoint.  At
depth one, the interval length \(r-1\) is even, and the two components
have exactly \(m\) common targets: the unions of consecutive whole
dominoes.

Thus there are exactly

\[
                         mT
\tag{4.3}
\]

labelled collision witnesses \((j,X)\), where \(X\) is a common
depth-one target of \(P_j,P_j^\tau\).

Compare a proposed rebundling history assignment with the original
assignment (4.2).  Call one original entrance occurrence **changed** if
it is discarded or its assigned depth-one target is not the one supplied
by (4.2).  Let \(Q_1\) be the number of changed occurrences.

### Lemma 4.1 (one changed occurrence kills at most one witness)

At most \(Q_1\) of the \(mT\) witnesses in (4.3) fail because of a
changed occurrence.

#### Proof

Inside one component cycle, the fixed-length cyclic intervals at
different phases are distinct.  Hence one entrance occurrence supplies
at most one of the \(m\) common depth-one targets of its twin.
Changing or discarding that occurrence can therefore kill at most one
labelled witness.  Entrance decks of different selected twins are
disjoint, so the same occurrence cannot belong to two witnesses from
different \(j\)'s. \(\square\)

At least \(mT-Q_1\) witnesses survive.  For a target \(X\), let \(k_X\)
be the number of surviving witnesses labelled by \(X\).  The new load
obeys

\[
                         \mu_1(X)\ge2k_X.
\tag{4.4}
\]

Therefore

\[
                         (\mu_1(X)-1)_+\ge k_X.
\tag{4.5}
\]

Summing gives

\[
                         E_1\ge mT-Q_1.
\tag{4.6}
\]

Subtracting the scalar floor proves

\[
 \widetilde E_1
 \ge mT-Q_1-(G'-N_1)_+,
\tag{4.7}
\]

which is (0.11).

In the Gaussian annulus,

\[
                         (G'-N_1)_+
 =O(W/\sqrt m)+o(W)
 =o(W)
\tag{4.8}
\]

whenever the new entrance leave is scalar-harmless.  Since (0.8)
forces \(\widetilde E_1=o(W)\), (4.7) yields

\[
                         Q_1\ge mT-o(W)=G/4-o(W).
\tag{4.9}
\]

This proves Theorem A.  It is stronger than saying that most twin
labels must be retagged: a positive density of literal entrance
occurrences must acquire a different first successor/deletion history.

## 5. Paired corridors remain inside the forbidden category

A critical paired-corridor operation starts with a domino necklace,
repartitions labels in \(I\) and \(I+r\), and ends with another domino
necklace.  Therefore it replaces one twin superpacket column by another
twin superpacket column.

The proof of the first-shadow bound uses only the following property of
one output column:

* it is a domino necklace split into its two complementary component
  cycles.

It does not use how that necklace was obtained.  Hence every corridor
neighbour, every iterated corridor neighbour, and every selected
representative of a corridor cluster again contributes \(m\) labelled
depth-one collision witnesses.

### Proposition 5.1 (closure of the obstruction)

Let \(\mathcal M'\) be any matching of \(T'\) twin superpackets,
possibly obtained after arbitrary corridor replacements, alternating
switches, or cluster choices.  Split every selected output twin into
its two components.  Then

\[
 \widetilde E_1
 \ge mT'-(2nT'-N_1)_+
 =\frac{2nT'}4-O(W/\sqrt m).
\tag{5.1}
\]

In particular a near-spanning output has \(\Omega(W)\) floor-correct
first-shadow excess.

#### Proof

Apply the \(m\)-common-target calculation independently to every
selected output twin and sum the collision witnesses exactly as in
Section 4. \(\square\)

There is a second, combinatorial mismatch.  The selected members of the
entrance matching have disjoint supports.  A critical corridor neighbour
of one selected twin overlaps that parent in all but \(o(m)\) roots, so
it is a conflicting alternative column; it is not another disjoint
selected parent and does not supply a splice between two selected
parents.

Thus close-neighbour entropy and corridor cluster quotients address
which twin column is selected.  Gate GR asks how roots belonging to
many disjoint selected columns are reassigned to non-twin ordinary
history columns.  These are different incidence problems.

## 6. The only form of direct corridor leverage

For paired corridors to help, one needs a theorem of the following
literal form.

### Cross-parent corridor splice theorem (missing)

Given a family \(\mathcal K\) of disjoint selected twins, construct
ordinary cyclic-history paths \(\mathscr P_{\mathcal K}\) such that

\[
 \operatorname{ent}\mathscr P_{\mathcal K}
 =
 \bigcup_{F\in\mathcal K}F
\tag{6.1}
\]

up to scalar-harmless quarantine,

\[
 H|\mathscr P_{\mathcal K}|=o(|\mathcal K|\,2n),
\tag{6.2}
\]

and the aggregate contribution of the cluster to

\[
 \sum_{d=0}^{D}
 \left(
 \min\{G',N_d\}-|S_d|
 \right)
\tag{6.3}
\]

is summable to \(o(W)\) over all clusters.

The output paths in (6.1) must use entrance roots from at least two
different selected parents and must not re-form intact twin pairs on
all but \(o(W)\) mass.  Theorem A forces at least \(G/4-o(W)\) changed
depth-one assignments globally.

No current paired-corridor theorem has these conclusions.  The
half-exponent construction gives many alternative necklaces close to
one parent.  It gives neither equality (6.1) for disjoint parents nor
one ordinary path crossing a parent boundary.

If (6.1)--(6.3) were proved and the clusters covered almost all selected
twins, their union would itself prove Gate GR.  Thus the missing
cross-parent lemma is not a cheaper bookkeeping corollary of corridor
stability; it is a localized version of the global ordinary annulus
re-bundling problem.

## 7. Exact implication boundary

### Proved

1. Gate GR, equations (0.7)--(0.9), is the weakest ordinary-history
   statement entering the deterministic common-arrival compiler.
2. Full cyclic packets are unnecessary; a path forest with
   \(Hp=o(W)\) suffices.
3. The exact integral selection problem is (3.3)--(3.8).
4. Any successful rebundling must change the depth-one history of at
   least \(G/4-o(W)\) entrance occurrences.
5. The class of intact twin outputs is closed under paired-corridor
   replacements and retains linear first-shadow excess.
6. Critical corridor neighbours are conflicting alternatives to one
   selected parent, not splice relations between disjoint selected
   parents.

### Not proved

1. Gate GR for the entrance set supplied by a twin matching.
2. A cross-parent ordinary splice preserving the union of selected
   entrance roots.
3. A small-component path cover after cross-parent rebundling.
4. Aggregate all-depth support control for any proposed splice library.

The answer to the interface question is therefore negative with the
present inputs: paired corridors merely restate the ordinary annulus
problem unless they are upgraded to literal cross-parent rebundling
columns.  The twin matching supplies entrance ownership, but coefficient
one still requires a new positive-density ordinary-history construction.

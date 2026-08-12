# Lane W: PBBS balanced flags and the nonlocal crossing-flow Hall gate

Date: 2026-07-25

Method: pure mathematics only.  No generic Johnson compiler, computation,
solver, or probabilistic rounding theorem is used.

## 0. Outcome

The weakest direct rotor gate is the covering-prefix condition
\((\mathrm{CP}_A)\): choose one full radius-\(H\) flag above every middle
owner and cover the selected useful states by \(o(W/H)\) directed
bridge-one paths.  This note pushes the PBBS route to an exact integral
flow--Hall statement.

There is no unconditional proof of \((\mathrm{CP}_A)\) here.  The advance is
the following.

1.  A bridge-one arc has an exact queue recurrence.  On the owner level it
    deletes the first lower flag coordinate, while the remaining lower
    queue shifts left.  This gives an if-and-only-if positive-residence
    criterion for lifting any prescribed Johnson path.
2.  Cut the PBBS owner cycles at a two-sided radius-\(H\) residence
    transversal.  On every owner more than \(H\) steps from a cut, the full
    lower and upper flags are forced by PBBS chronology.  Leave all other
    owners free.
3.  After subtracting the forced PBBS flag loads, completion to balanced
    full flags is exactly a pair of integral lower-bounded inclusion-flow
    problems.  Feasibility is characterized by Hoffman's cut inequalities;
    there is no hidden fractional step.
4.  Every integral pair of residual flows selects one full useful state at
    every owner.  Contract the already bridge-compatible PBBS interiors to
    atoms.  For a total order of the atoms, the exact minimum number of
    nonlocal bridge-one paths is the Hall deficiency of the split endpoint
    graph.  Minimizing this deficiency over the two residual flows and the
    order gives a single explicit number
    \(\Delta_H^{\rm PBBS}(D)\).
5.  Therefore the precise PBBS crossing-braid lemma still needed is
    \[
       \boxed{
       \text{for some critical PBBS cut set }D,\quad
       \mathfrak F_H(D)\ne\varnothing,
       \qquad
       \Delta_H^{\rm PBBS}(D)=o_A(W/H).}
       \tag{0.1}
    \]
    Here \(\mathfrak F_H(D)\) is the explicitly defined set of integral
    residual lower/upper flows.  This statement directly selects balanced
    full flags and directly constructs the few bridge-one paths.  It is
    strictly nonlocal: the matching may join different PBBS quotient times,
    components, and spatial phases.

Two rigidity facts show why (0.1) cannot be replaced by a local seam rule.

* If a changed seam preserves both its old first lower intersection and
  its old first upper union, its successor did not change at all.
* At a fixed quotient cut, joining one spatial phase to a different phase
  by a Johnson edge forces the source owner to be within symmetric
  difference four of a nontrivial rotation.  Only
  \(2^{N/3+o(N)}\) owners have this property.  Thus an all-phase diagonal
  phase permutation is exponentially too small; a successful braid must
  mix different quotient times.

Finally, the corrected literal ledger is exact.  If (0.1) holds with
deficiency \(p\), the flag paths cost

\[
  \boxed{W+2Hp.}
  \tag{0.2}
\]

The \((4H-1)\) QCF chart is charged only at the two outer borders of long
all-phase blocks, for total \(o(W)\).  It is not charged at the internal
PBBS residence cuts.  Likewise, the balanced flag word substitutes for the
internal sandwich charts; their openings are not appended a second time.
Thus (0.1) would give a baseline-relative block compiler with total excess
\(o(W)\).

The rest of the note proves these assertions and states all quantifiers.

## 1. Full flags and the exact bridge queue

It is convenient to allow both the even rotor model and the odd PBBS
model.  Let the ground set have size \(n\), fix rank \(k\), and assume

\[
  1\le H<\min(k,n-k).
  \tag{1.1}
\]

Put

\[
  \mathcal O=\binom{[n]}k,
  \qquad W=|\mathcal O|.
  \tag{1.2}
\]

The new rotor gate uses \(n=2m,k=m\).  The PBBS specialization uses
\(n=2m+1\) and \(k=m\) or \(m+1\).  All local statements below are the
same in the three cases.

A full useful state is an ordered partition

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=k-H,quad |R|=n-k-H,
 \tag{1.3}
\]

and its owner is

\[
 X=L\cup\{z_1,\ldots,z_H\}.
 \tag{1.4}
\]

Write its lower deletion queue and upper addition queue as

\[
 \alpha(\omega)=(\alpha_1,\ldots,\alpha_H)
 =(z_H,z_{H-1},\ldots,z_1),
 \tag{1.5}
\]

\[
 \beta(\omega)=(\beta_1,\ldots,\beta_H)
 =(z_{H+1},\ldots,z_{2H}).
 \tag{1.6}
\]

Thus

\[
 L_q(\omega)=X-\{\alpha_1,\ldots,\alpha_q\},
 \qquad
 U_q(\omega)=X+\{\beta_1,\ldots,\beta_q\}.
 \tag{1.7}
\]

### Lemma 1.1 (exact queue recurrence)

Let \(\omega\) have owner \(X\), and let a bridge-one successor
\(\omega'\) have a distinct owner

\[
 Y=X-a+b.
 \tag{1.8}
\]

Then necessarily

\[
 a=\alpha_1.
 \tag{1.9}
\]

There is an element

\[
 x\in L=X-\{\alpha_1,\ldots,\alpha_H\}
 \tag{1.10}
\]

such that

\[
 \boxed{
 \alpha(\omega')=(\alpha_2,\ldots,\alpha_H,x).}
 \tag{1.11}
\]

For the upper queue there are exactly two cases.

1. If \(b\notin\{\beta_1,\ldots,\beta_H\}\), then \(b\in R\) and
   \[
    \boxed{
    \beta(\omega')=(a,\beta_1,\ldots,\beta_{H-1}).}
    \tag{1.12}
   \]
2. If \(b=\beta_j\), then
   \[
    \boxed{
    \beta(\omega')=
    (a,\beta_1,\ldots,\beta_{j-1},
       \beta_{j+1},\ldots,\beta_H).}
    \tag{1.13}
   \]

Conversely, for every choice in (1.10), the update (1.11) together with
(1.12) or (1.13) is a bridge-one successor with owner (1.8).

#### Proof

In the rotor case of the bridge-one classification,

\[
 L'=L-x+b,
 \qquad
 z'=(x,z_1,\ldots,z_{2H-1}),
 \tag{1.14}
\]

with \(b\in R\).  Reversing the first \(H\) singleton positions gives
(1.11), and reading the last \(H\) gives (1.12).  The owner loses
\(z_H=\alpha_1\) and gains \(b\), proving (1.8)--(1.9).

In the promotion case,

\[
 L'=L-x+z_{H+j},
 \qquad
 z'=(x,z_1,\ldots,\widehat {z_{H+j}},\ldots,z_{2H}),
 \tag{1.15}
\]

for some \(1\le j\le H\).  This gives (1.11) and (1.13), and the owner
gains \(z_{H+j}=\beta_j\).  These are all distinct-owner bridge-one cases,
and direct substitution proves the converse. \(\square\)

The recurrence gives the exact first-band identities

\[
 \boxed{
 L_1(\omega)=X\cap Y,
 \qquad
 U_1(\omega')=X\cup Y.}
 \tag{1.16}
\]

### Theorem 1.2 (exact positive-residence lift)

Let

\[
 X_0,X_1,\ldots,X_s
 \tag{1.17}
\]

be a nonlazy Johnson path, with

\[
 X_{t+1}=X_t-r_t+a_t.
 \tag{1.18}
\]

Whenever a coordinate is inserted at edge \(u\) and next removed at edge
\(v\), call \(v-u\) its positive residence on the path.  Then (1.17)
admits one full useful state above every owner, with every displayed owner
edge bridge one, if and only if

\[
 \boxed{v-u>H}
 \tag{1.19}
\]

for every insertion--next-removal pair whose two edges both lie in the
path.

#### Proof

For necessity, an entering coordinate is placed in the target lower base.
It can enter the deletion queue only at its last position, and then needs
\(H\) queue shifts before it becomes the first deletion.  Therefore it
cannot be removed in the next \(H\) path edges.

For sufficiency, initialize the lower queue at \(X_0\) with

\[
 r_0,r_1,\ldots,r_{H-1}
 \tag{1.20}
\]

as far as those edges exist, and fill the unused tail with arbitrary
distinct elements of \(X_0\).  Condition (1.19) says precisely that every
displayed \(r_j\) is still in \(X_0\), and that they are distinct.  At edge
\(t\), use

\[
 x=r_{t+H}
 \tag{1.21}
\]

when that future edge exists; (1.19) puts it in the current lower base.
Near the terminal endpoint, fill with an arbitrary current base element.
This realizes (1.11) throughout.

Choose any initial upper queue.  At edge \(t\), the incoming coordinate
\(a_t\) is either in that queue or in the residual block.  Use promotion
in the first case and a rotor shift in the second.  Equations
(1.12)--(1.13) then propagate a valid upper queue.  Thus every owner edge
is bridge one. \(\square\)

If, in addition, every coordinate removed on the path is not reinserted
during the next \(H\) edges, then all updates in an \(H\)-deep interior
are rotor updates and

\[
 L_q(X_i)=\bigcap_{j=0}^qX_{i+j},
 \qquad
 U_q(X_i)=\bigcup_{j=0}^qX_{i-j}
 \tag{1.22}
\]

for every available \(q\le H\).  This is the two-sided clean regime in
which PBBS crossing windows literally equal the selected flags.

## 2. PBBS residence cuts and frozen full flags

Let \(g\) be the step-two PBBS permutation on the owner layer.  On one
oriented owner cycle write

\[
 X_{i+1}=X_i-r_i+a_i,
 \tag{2.1}
\]

with cyclic indices.  Let \(D\) be a set of PBBS transition edges which
contains at least one edge of every owner cycle.  Removing \(D\) gives a
family \(\mathcal P_D\) of linear PBBS pieces.

For a coordinate membership run, include the insertion edge, all internal
edges, and the next removal edge.  Let \(\mathcal I_H^+\) be the circular
intervals of this form having positive residence at most \(H\).  Define
\(\mathcal I_H^-\) in the complement owner path; equivalently these are
the absence runs of length at most \(H\) in the original path.

Call \(D\) a **two-sided radius-\(H\) residence transversal** if

\[
 D\cap I\ne\varnothing
 \quad
 (I\in\mathcal I_H^+\cup\mathcal I_H^-).
 \tag{2.2}
\]

The exact circular-interval packing/transversal theorem and the proved
PBBS height-gap estimate provide such transversals at the critical scale

\[
 |D|=O_A(W/H)
 \tag{2.3}
\]

after taking the union of the two signs and adding one cut on every
otherwise uncut PBBS cycle.  The missing gain is not (2.3): coefficient
one requires the final number of opened paths to be \(o_A(W/H)\).

An owner \(X_i\) is **\(H\)-deep relative to \(D\)** if none of the
transition edges with indices

\[
 i-H,\ldots,i+H-1
 \tag{2.4}
\]

lies in \(D\).  For such an owner, (2.2) gives two-sided cleanliness and
the natural full queues

\[
 \alpha_i=(r_i,r_{i+1},\ldots,r_{i+H-1}),
 \tag{2.5}
\]

\[
 \beta_i=(r_{i-1},r_{i-2},\ldots,r_{i-H}).
 \tag{2.6}
\]

All entries of (2.5) are distinct members of \(X_i\), and all entries of
(2.6) are distinct nonmembers.  They define a full useful state
\(\omega_i^{\rm PBBS}\).  Consecutive \(H\)-deep states are joined by a
bridge-one rotor edge.

Let

\[
 \mathcal I(D)=\{X_i:X_i\text{ is }H\text{-deep relative to }D\}.
 \tag{2.7}
\]

For every \(X_i\in\mathcal I(D)\) and \(q\le H\), its fixed flags are

\[
 L_{i,q}^{\rm PBBS}
 =X_i-\{r_i,\ldots,r_{i+q-1}\},
 \tag{2.8}
\]

\[
 U_{i,q}^{\rm PBBS}
 =X_i+\{r_{i-1},\ldots,r_{i-q}\}.
 \tag{2.9}
\]

These are exactly the consecutive PBBS intersection and union windows.
The owners outside \(\mathcal I(D)\) are not assigned flags yet.

## 3. Exact residual balanced-flag flows

For \(0\le q\le H\), put

\[
 N_q^- =\binom n{k-q},
 \qquad
 N_q^+ =\binom n{k+q}.
 \tag{3.1}
\]

A flag selection is **balanced** if every lower target at depth \(q\)
has load either

\[
 \left\lfloor {W\over N_q^-}\right\rfloor
 \quad\text{or}\quad
 \left\lceil {W\over N_q^-}\right\rceil,
 \tag{3.2}
\]

and every upper target has the analogous load with \(N_q^+\).  In
particular every target is covered.

For a lower target \(T\in\binom{[n]}{k-q}\), let

\[
 c^-_{q,T}(D)
 =\#\{X_i\in\mathcal I(D):L_{i,q}^{\rm PBBS}=T\}.
 \tag{3.3}
\]

Define \(c^+_{q,U}(D)\) from (2.9).  The first exact obstruction is the
pointwise ceiling condition

\[
 c^-_{q,T}(D)
 \le\left\lceil {W\over N_q^-}\right\rceil,
 \qquad
 c^+_{q,U}(D)
 \le\left\lceil {W\over N_q^+}\right\rceil.
 \tag{3.4}
\]

If (3.4) fails, no balanced full-flag selection can retain all the frozen
PBBS interiors.  Normalized-port degree balance does not imply (3.4).

Assume (3.4).  For every lower target put

\[
 \ell^-_{q,T}
 =\max\!\left\{0,
 \left\lfloor {W\over N_q^-}\right\rfloor-c^-_{q,T}(D)
 \right\},
 \tag{3.5}
\]

\[
 u^-_{q,T}
 =\left\lceil {W\over N_q^-}\right\rceil-c^-_{q,T}(D).
 \tag{3.6}
\]

Construct the residual lower inclusion network
\(\mathcal N_H^-(D)\) as follows.

* It has the set layers
  \[
    \binom{[n]}k,\binom{[n]}{k-1},\ldots,
    \binom{[n]}{k-H}.
  \]
* Only owners in \(\mathcal O\setminus\mathcal I(D)\) receive one unit of
  supply at depth zero.
* Consecutive layers are joined by all facet inclusions.
* Split every depth-\(q\) target node into an in-node and out-node.  Its
  internal gate has capacity interval
  \([ell^-_{q,T},u^-_{q,T}]\).
* All inclusion arcs have capacity interval \([0,W]\), and the bottom
  sends the total residual flow to one sink.

Define \(\mathcal N_H^+(D)\) by complementing and using the upper residual
intervals

\[
 \ell^+_{q,U}
 =\max\!\left\{0,
 \left\lfloor {W\over N_q^+}\right\rfloor-c^+_{q,U}(D)
 \right\},
 \tag{3.7}
\]

\[
 u^+_{q,U}
 =\left\lceil {W\over N_q^+}\right\rceil-c^+_{q,U}(D).
 \tag{3.8}
\]

### Theorem 3.1 (exact preloaded flag completion)

The frozen PBBS lower flags extend to a balanced lower full flag at every
owner if and only if \(\mathcal N_H^-(D)\) has a feasible flow.  The upper
analogue holds independently.  Whenever feasible, both networks have
integral feasible flows.

Equivalently, after the standard source--sink return arc is added, each
network is feasible if and only if for every vertex set \(S\),

\[
 \boxed{
 \sum_{e\in\delta^-(S)}u_e
 \ge
 \sum_{e\in\delta^+(S)}\ell_e.}
 \tag{3.9}
\]

These are Hoffman's circulation inequalities for the explicit residual
capacities (3.5)--(3.8).

#### Proof

A lower flag is a unit path in the layered inclusion network.  Remove the
already fixed unit paths (2.8).  The remaining target throughput needed for
a final floor/ceiling load is exactly the interval
(3.5)--(3.6).  Hence a completion is the same thing as a feasible residual
flow.

All supplies and all capacity endpoints are integral.  The lower-bounded
flow reduction has a directed incidence matrix, which is totally
unimodular.  Thus every nonempty residual flow polytope has an integral
point, and that point decomposes into one unit path from each residual
owner.  Hoffman's theorem gives (3.9).  The upper proof is the complemented
copy. \(\square\)

Let

\[
 \mathfrak F_H(D)
 \tag{3.10}
\]

be the set of pairs \(f=(f^-,f^+)\) of integral feasible flows in the two
networks.  Each \(f\in\mathfrak F_H(D)\), together with the frozen PBBS
flags, selects one full useful state \(\omega_f(X)\) at every owner.  The
lower and upper choices combine because one deletes elements of \(X\) and
the other adds elements of its complement.

Theorem 3.1 settles the balanced selection problem after a cut set is
fixed.  It does not settle chronology: the two flow choices must be made so
that the resulting common full states admit many bridge-one arcs.

## 4. The exact ordered Hall number of the PBBS braid

For \(f\in\mathfrak F_H(D)\), form atoms as follows.

* Every maximal consecutive run of frozen PBBS states
  \(\omega_i^{\rm PBBS}\) is one atom, in its PBBS order.
* Every remaining owner is a singleton atom carrying \(\omega_f(X)\).

Call the atom family \(\mathcal A(D,f)\).  The states inside every
nonsingleton atom already form one bridge-one path, and the atoms partition
all \(W\) owners.

Fix a total order \(\prec\) on the atoms.  Form the split bipartite graph

\[
 \mathcal B(D,f,\prec)
 \tag{4.1}
\]

with a left and a right copy of every atom.  Put an edge
\(P_{\rm L}Q_{\rm R}\) exactly when

1. \(P\prec Q\); and
2. the terminal useful state of \(P\) has a bridge-one arc to the initial
   useful state of \(Q\).

Define its Hall deficiency by

\[
 \delta(D,f,\prec)
 =\max_{\mathcal S\subseteq\mathcal A(D,f)}
 \left(
   |\mathcal S|-|N_{\mathcal B(D,f,\prec)}(\mathcal S)|
 \right).
 \tag{4.2}
\]

Finally put

\[
 \boxed{
 \Delta_H^{\rm PBBS}(D)
 =\min_{f\in\mathfrak F_H(D)}
   \min_{\prec}\delta(D,f,\prec),}
 \tag{4.3}
\]

with value \(+\infty\) when \(\mathfrak F_H(D)=\varnothing\).

### Theorem 4.1 (exact PBBS crossing-braid formula)

Among balanced full-flag selections obtained from the frozen-PBBS/residual-
flow construction above, the exact minimum number of directed bridge-one
paths is

\[
 \boxed{p_H^{\rm braid}(D)=\Delta_H^{\rm PBBS}(D).}
 \tag{4.4}
\]

#### Proof

Fix \(f\) and \(\prec\).  A matching in (4.1) selects at most one outgoing
join and at most one incoming join for every atom.  Because every selected
join points forward in \(\prec\), no directed cycle occurs.  A matching of
size \(M\) therefore joins the atom paths into exactly

\[
 |\mathcal A(D,f)|-M
 \tag{4.5}
\]

directed paths.

Conversely, any directed path cover of the atoms can be topologically
ordered.  Its interatom joins give a matching in the corresponding split
graph.  The deficiency form of Hall's theorem says

\[
 |\mathcal A(D,f)|-\nu(\mathcal B(D,f,\prec))
 =\delta(D,f,\prec).
 \tag{4.6}
\]

Minimize over the integral residual flows and over the order. \(\square\)

This theorem identifies the exact correlation absent from all marginal
arguments.  The same residual full state controls both the incoming and
outgoing bridge tests, while its entire nested lower and upper flags consume
the capacities in (3.5)--(3.8).  Independent lower flow, upper flow, and
endpoint matchings cannot be rounded separately.

### Corollary 4.2 (the precise PBBS flag-braid lemma)

Fix \(A>0\) and take \(H=\lceil A\sqrt m\rceil\).  Suppose that for all
sufficiently large \(m\) there is a two-sided PBBS residence transversal
\(D=D_m\) satisfying

\[
 |D|=O_A(W/H),
 \tag{4.7}
\]

\[
 \mathfrak F_H(D)\ne\varnothing,
 \tag{4.8}
\]

and

\[
 \boxed{
 \Delta_H^{\rm PBBS}(D)=o_A(W/H).}
 \tag{4.9}
\]

Then there is one balanced full radius-\(H\) flag at every owner whose
selected useful states have a bridge-one path cover with
\(p=o_A(W/H)\).  Hence \((\mathrm{CP}_A)\) holds.

#### Proof

Theorem 3.1 and (4.8) give balanced full flags.  Theorem 4.1 and (4.9)
give the path cover.  This is exactly the definition of the balanced
strengthening of \((\mathrm{CP}_A)\). \(\square\)

Thus (4.8)--(4.9), with the explicit networks and graph above, are the
remaining PBBS-specific flow--Hall lemma.  They are not proved here.

## 5. Two exact local obstructions

### Lemma 5.1 (two-sided first-band pointwise rigidity)

Let \(X\to Y\) be one old PBBS Johnson edge.  Suppose a proposed new seam
from the same source owner \(X\) to a Johnson neighbour \(Z\) preserves
both old first-band colors:

\[
 X\cap Z=X\cap Y,
 \qquad
 X\cup Z=X\cup Y.
 \tag{5.1}
\]

Then

\[
 \boxed{Z=Y.}
 \tag{5.2}
\]

#### Proof

Write \(X\setminus Y=\{a\}\) and \(Y\setminus X=\{b\}\).  The first
identity in (5.1) forces \(X\setminus Z=\{a\}\), and the second forces
\(Z\setminus X=\{b\}\).  Hence \(Z=X-a+b=Y\). \(\square\)

By (1.16), these are exactly the lower color of the source flag and the
upper color of the target flag.  Therefore every genuinely changed seam
changes at least one first-band target.  A successful crossing braid must
trade target loads among many seams; it cannot preserve the old two-sided
windows seam by seam.

Already at depth one, a potential interatom join is a bundled object

\[
 (P_{\rm out},Q_{\rm in},X\cap Y,X\cup Y).
 \tag{5.3}
\]

Selecting joins with endpoint degree at most one and balanced lower and
upper color capacities is a four-partite hypergraph matching.  Ordinary
Hall expansion of the uncolored endpoint graph is insufficient.  The
residual flow selector in Sections 3--4 retains this bundle rather than
discarding it.

### Lemma 5.2 (fixed-time cross-phase seams are exceptional)

Let \(N\) be odd, let \(\rho\) be cyclic coordinate rotation, and let
\(X\to Y\) be one PBBS Johnson edge.  Suppose for phases \(u\ne v\) that

\[
 \rho^uX\longrightarrow\rho^vY
 \tag{5.4}
\]

is also a Johnson edge.  Then, with \(c=v-u\not\equiv0\pmod N\),

\[
 \boxed{|X\mathbin\triangle\rho^cX|\le4.}
 \tag{5.5}
\]

Consequently the number of possible source owners for any nontrivial
same-time phase splice is at most

\[
 \boxed{
 (N-1)2^{N/3}\sum_{j=0}^{4}\binom Nj
 =2^{N/3+o(N)}.}
 \tag{5.6}
\]

#### Proof

Rotate (5.4) back by \(u\).  Since both the old and new arrows are Johnson
edges,

\[
 |X\triangle Y|=2,
 \qquad
 |X\triangle\rho^cY|=2.
 \tag{5.7}
\]

Therefore

\[
 |X\triangle\rho^cX|
 \le |X\triangle\rho^cY|
     +|\rho^cY\triangle\rho^cX|
 =4.
 \tag{5.8}
\]

For fixed \(c\ne0\), the permutation \(\rho^c\) has at most \(N/3\)
cycles because all its cycles have odd length at least three.  A set is
determined by its transition positions under \(\rho^c\) and one bit on
each rotation cycle.  With at most four transitions this gives

\[
 2^{N/3}\sum_{j=0}^4\binom Nj
\]

sets.  Sum over the \(N-1\) nonzero phase offsets. \(\square\)

Since a central owner layer has size \(2^{N-o(N)}\), (5.6) is
exponentially negligible.  Hence a braid which merely permutes the
\(N\) spatial lifts at each fixed quotient cut cannot prove (4.9).  The
ordered Hall matching must join different quotient times or different
PBBS components on almost all of its nonlocal edges.

## 6. Correct sandwich/QCF ledger after the braid

Suppose (4.7)--(4.9) hold and write

\[
 p=\Delta_H^{\rm PBBS}(D).
 \tag{6.1}
\]

A bridge-one path containing \(s\) owners has exact useful-prefix length

\[
 s+2H.
 \tag{6.2}
\]

Summing over the \(p\) paths gives

\[
 \boxed{L_{\rm flags}=W+2Hp=W+o_A(W).}
 \tag{6.3}
\]

Every selected full flag is balanced, so all lower and upper targets
through depth \(H\) are already covered.  There is no distinct crossing
support appendage.

For comparison, one proper depth-\(q\) PBBS extension run with \(r\)
extension edges has \(r+q+1\) charged owner positions and an exact sandwich
chart of length

\[
 r+2q+1=(r+q+1)+q.
 \tag{6.4}
\]

The corrected normalized-port trail ledger leaves

\[
 N\bar R_q+(q-1)c_q
 \tag{6.5}
\]

internal excess, while chronology-bearing spines retain
\((q-1)N\bar R_q\).  Equation (6.3) does not add those charts to the flag
word.  It **substitutes** the balanced full-state paths for them: every
middle owner is the one baseline letter of exactly one path, and every
internal nonlocal join is a bridge-one update costing that next baseline
letter.  Charging (6.4) or (6.5) again would double-count the same owners.

Outer block borders are different.  Partition quotient chronology into
blocks with

\[
 H\ll b,
 \qquad b\log N=o(m).
 \tag{6.6}
\]

The exact QCF one-border chart costs \(4H-1\), and the complete all-phase
outer-border cost is

\[
 \boxed{
 N(4H-1)\left\lceil{B\over b}\right\rceil
 =O\!\left({WH\over b}\right)+\exp(o(m))
 =o_A(W).}
 \tag{6.7}
\]

For example one may take \(b=m^{3/4}\) in the Gaussian window.  The QCF
chart is used only at these outer borders.  Applying it at each of the
\(O(W/H)\) residence cuts would return a linear term and is expressly not
part of the braid.

Thus, including the already audited bounded-depth and short-cycle terms,
the baseline-relative ledger is

\[
 \boxed{
 L\le
 W+2H\Delta_H^{\rm PBBS}(D)
 +N(4H-1)\left\lceil{B\over b}\right\rceil
 +o_A(W).}
 \tag{6.8}
\]

Under (4.9), every term after \(W\) is \(o_A(W)\).

## 7. Exact proved/remaining boundary

### Proved here

1. The full lower/upper queue recurrence (1.11)--(1.13).
2. The if-and-only-if positive-residence lift for a prescribed Johnson
   path.
3. The natural two-sided full PBBS flags on every \(H\)-deep owner after a
   residence transversal.
4. The exact residual balanced-flag networks, their integral completion,
   and their Hoffman cut characterization.
5. The exact ordered-Hall formula
   \(p_H^{\rm braid}(D)=\Delta_H^{\rm PBBS}(D)\).
6. Pointwise two-sided target preservation forces the original successor.
7. Same-time cross-phase Johnson splices are confined to an exponentially
   negligible rotational exceptional family.
8. The corrected baseline-relative ledger (6.8), with no internal QCF or
   sandwich double charge.

### Still unproved

For \(H=\lceil A\sqrt m\rceil\), one must choose a critical two-sided PBBS
cut set \(D\) so that

\[
 \boxed{
 \begin{aligned}
 &c^-_{q,T}(D)
   \le\left\lceil W/N_q^-\right\rceil,
 &&c^+_{q,U}(D)
   \le\left\lceil W/N_q^+\right\rceil;\\
 &\text{all Hoffman inequalities (3.9) hold for both signs};\\
 &\min_{f\in\mathfrak F_H(D)}\min_{\prec}
   \max_{\mathcal S}
   \bigl(|\mathcal S|-|N_{\mathcal B(D,f,\prec)}(\mathcal S)|\bigr)
   =o_A(W/H).
 \end{aligned}}
 \tag{7.1}
\]

This is the exact PBBS-specific nonlocal crossing-flow Hall lemma.  A
violation of a ceiling in the first line, a Hoffman cut in the second, or
an ordered Hall set in the third is an exact obstruction to this braid
architecture.  Conversely, absence of all three obstructions proves the
balanced strengthening of \((\mathrm{CP}_A)\) and, by (6.8), the desired
baseline-relative compiler with \(o(W)\) total excess.

The normalized-port obstruction is therefore not the endpoint of the
analysis.  It identifies why carrier-forgetting local joins fail; (7.1)
identifies the next, genuinely nonlocal integral theorem which would
finish the PBBS route.

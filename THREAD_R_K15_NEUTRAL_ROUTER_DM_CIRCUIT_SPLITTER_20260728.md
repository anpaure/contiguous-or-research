# Neutral legality routers, DM-circuit splitters, and the Hall-22 routing gate

Date: 2026-07-28

Status: exact audit of the Hall-\(23\to23\to22\) compound braid; exact
occurrence-split and turn-colour holonomy theorems; and a necessary-and-
sufficient orbit formulation of the proposed routing theorem.  Universal
routing over the remaining circuits is **not proved**.  The stored Hall
artifacts do not certify one simultaneous common-\(Q\) owner selection or a
literal length-\(6438\) word.

## 0. Verdict

The third neutral/improving pair is

\[
 H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}
 H23^{\rm portal}
 \xrightarrow{\operatorname{FR}(740,4051,6137)}H22.
\tag{0.1}
\]

It is an exact integral path reassembly.  Its matching ranks and Hall
deficiencies are

\[
 16360\longrightarrow16360\longrightarrow16361,
 \qquad
 23\longrightarrow23\longrightarrow22.
\tag{0.2}
\]

The two stages are genuinely remote from one another.

* The neutral braid changes compiler profiles only in the `161/160`
  component rooted at `24610`.  It rotates a Boolean packet and leaves that
  component's neighbourhood size and rank equal to `160`.
* The improving braid makes no profile-multiset change in that component.
  It acts instead on the `2/1` component with targets
  \(\{4877,4909\}\), replacing their one shared occurrence by two distinct
  occurrences.  Restricted to the component, the change is

  \[
                   \{4877,4909\}\longmapsto
                   \{4877\},\{4909\}.
  \tag{0.3}
  \]

Thus the correct architecture is

\[
\boxed{\text{neutral legality router}
       \quad+\quad
       \text{remote local DM-circuit splitter}.}
\tag{0.4}
\]

The algebraic generalization is positive: every nontrivial transversal
circuit admits an abstract binary split of one right occurrence which
perfects it.  The remaining difficulty is physical realization.  Legal
neutral segment braids form a state-dependent **groupoid**, not one group
acting freely on target roots.  A seed splitter routes exactly through its
connected component in a decorated rooted-ear lift graph whose vertices
record collars, matchings, shadow ledgers, residence, and common-\(Q\)
data.

There is also a sharp holonomy obstruction.  Colour a Johnson edge by its
two toggled coordinates.  Every fixed-endpoint braid has Eulerian signed
turn-colour current modulo two.  Hence a local splitter port with odd
coordinate boundary needs a remote return port.  In (0.1), the axis-\(6\)
split is closed by a second axis-\(6\) seam.  It cannot be installed as an
isolated one-port operation.

Consequently the theorem still needed is not bare transitivity on DM roots.
It is connectedness, or component coverage by a finite template library, of
the **decorated rooted-ear lift graph** subject to turn-colour holonomy and
the exact common-\(Q\) inequalities.

## 1. Exact finite audit

Let `T`, `T^p`, and `T^{22}` denote the three middle paths in (0.1).
Independent reconstruction gives

\[
\begin{array}{c|ccc}
&T&T^p&T^{22}\\ \hline
\nu(G)&16360&16360&16361\\
h(G)&23&23&22\\
|D_L|/|D_R|&1007/984&1007/984&1005/983\\
\text{unmatched ranks }(6,7)&(5,18)&(5,18)&(5,17)\\
\text{zero-degree targets}&7&7&7.
\end{array}
\tag{1.1}
\]

The seven zero targets remain

\[
2575,5801,13616,13620,17738,21641,29776.
\tag{1.2}
\]

The canonical DM target shore is literally unchanged by the first braid.
The second removes exactly

\[
                         \boxed{\{4877,4909\}}
\tag{1.3}
\]

and adds no target.  The exact old/portal/final cross-gap matrix is

\[
\begin{pmatrix}
23&23&22\\
23&23&22\\
22&22&22
\end{pmatrix}.
\tag{1.4}
\]

For the neutral braid, the common cell-profile multiset has `19293`
occurrences and matching rank `16350`; the changed bank has `18` old and
`18` new occurrences and contracted rank

\[
                             10\longrightarrow10.
\tag{1.5}
\]

For the improving braid the corresponding figures are `19270`, `16343`,
`41/41`, and

\[
                             17\longrightarrow18.
\tag{1.6}
\]

All three paths satisfy the following physical carrier facts.

1. They enumerate all
   \[
                           \binom{15}{8}=6435
   \]
   middle masks exactly once.
2. Every consecutive pair is Johnson adjacent.
3. The endpoints remain `9901` and `7779`.
4. Every coordinate's shortest internal residence run has length four, so
   depth-three residence has no defect.
5. Maximal erosion has length `6438`, rank histogram
   \[
                         5^{6432},6^2,7^2,8^2,
   \]
   and exactly satisfies
   \[
                         T_i=\bigcup_{p=i}^{i+3}P_p.
   \]
6. Every upper support at depths `q=1,...,7` is complete.
7. The lower-hole vectors are
   \[
   (4,19,6,1,0,0,0)
   \longrightarrow(4,19,6,1,0,0,0)
   \longrightarrow(4,18,6,1,0,0,0).
   \tag{1.7}
   \]
   The only lower-support gain is target `4877` at depth two; there is no
   lower-support loss.
8. The four immediate-lower holes remain
   \[
                         5801,7267,8877,13620.
   \tag{1.8}
   \]

“Shadow preserving” in this result means preservation of the required
support sets, not preservation of every multiplicity.  The exact
multiplicity \(L^1\) changes are

\[
\begin{array}{c|c|c}
&\text{lower }q=1,\ldots,7&\text{upper }q=1,\ldots,7\\ \hline
\text{router}&(0,0,4,4,5,1,0)&(0,0,0,0,3,3,0)\\
\text{splitter}&(2,6,10,16,18,7,3)&(6,7,9,9,7,1,0).
\end{array}
\tag{1.9}
\]

In particular, no theorem placing (0.1) in a fixed all-depth multiplicity
stratum is correct.

## 2. Exact block and seam normal form

Split the Hall-23 path at

\[
0,740,3799,4497,5788,6040,6138,6435
\tag{2.1}
\]

into forward blocks \(X_0,\ldots,X_6\), whose lengths are

\[
                         740,3059,698,1291,252,98,297.
\tag{2.2}
\]

Then the two intermediate paths are exactly

\[
 T^p=X_0X_1X_4^RX_3^RX_2X_5X_6,
\tag{2.3}
\]

\[
 \boxed{T^{22}=X_0X_3^RX_2X_5X_4X_1^RX_6.}
\tag{2.4}
\]

Equations (2.3)--(2.4) directly materialize the two named moves in (0.1).
The symmetric difference of the old and final seam sets is the union of two
alternating \(C_6\)'s.  In middle-mask notation they are

\[
5037-6573-22925-14733-13197-5007-5037,
\tag{2.5}
\]

\[
24811-24687-8431-12399-12523-28779-24811.
\tag{2.6}
\]

Their successive turn-colour pairs are respectively

\[
(10,12),(6,15),(14,15),(10,12),(2,14),(2,6)
\tag{2.7}
\]

and

\[
(3,8),(8,15),(8,13),(3,8),(8,15),(8,13).
\tag{2.8}
\]

One corresponding clean rank-seven/rank-nine flag \(C_6\) is

\[
\begin{array}{c|ccc}
&1&2&3\\ \hline
\text{old}&(24683,24815)&(8303,12527)&(12395,28907)\\
\text{new}&(24683,28907)&(8303,24815)&(12395,12527).
\end{array}
\tag{2.9}
\]

The splitter's adjacent flag data are

\[
\begin{array}{c|ccc}
\text{old}&(4525,7085)&(5005,13199)&(6541,31117)\\
\text{new}&(5005,5039)&(12685,15245)&(6541,22957).
\end{array}
\tag{2.10}
\]

They preserve support but are not a multiplicity-clean flag switch, in
agreement with (1.9).

Applying the nominal second move directly to `T`, without the router,
creates two Hamming-distance-eight seams and five depth-three residence
defects.  Its upper support happens to remain complete, but it is not a
Johnson path and is not a legal carrier.  The first braid is therefore a
genuine legality router, not a dispensable rank-neutral detour.

## 3. The two remote compiler changes

### 3.1 The neutral root-24610 packet rotation

Put

\[
 K=24610,\qquad Q=K+\mathcal P(\{1,64\}).
\tag{3.1}
\]

Inside the root-\(K\) component, the first braid performs exactly

\[
 (4+Q),\qquad Q\cup(4096+Q)
 \quad\longmapsto\quad
 (4096+Q),\qquad Q\cup(4+Q).
\tag{3.2}
\]

In decimal target profiles, the two old occurrences

\[
\begin{aligned}
&(24614,24615,24678,24679),\\
&(24610,24611,24674,24675,28706,28707,28770,28771)
\end{aligned}
\tag{3.3}
\]

become

\[
\begin{aligned}
&(28706,28707,28770,28771),\\
&(24610,24611,24614,24615,24674,24675,24678,24679).
\end{aligned}
\tag{3.4}
\]

This transfers the square `Q` between two cells.  The root-\(24610\)
neighbourhood has size `160` and matching rank `160` before and after.
The second braid preserves its cell-profile multiset exactly, although the
physical positions realizing those profiles move.

### 3.2 The remote 2/1 splitter

Before the second braid, targets `4877` and `4909` each have degree one in
their DM component and share the depth-two cell at start `739`.  Its full
compiler profile is

\[
                 \Gamma(c)=(4876,4877,4908,4909),
\tag{3.5}
\]

with envelope `4909` and mandatory mask `4876`.

After the braid, the relevant full profiles are

\[
\begin{aligned}
\Gamma(c_0)
  &=(4612,4613,4620,4621,4868,4869,4876,4877),\\
\Gamma(c_1)
  &=(4652,4653,4908,4909).
\end{aligned}
\tag{3.6}
\]

Here `c_0` has depth one and start `740`; `c_1` has depth two and start
`739`.  Restricted to the old DM target set,

\[
\Gamma(c)\cap X=\{4877,4909\},\quad
\Gamma(c_0)\cap X=\{4877\},\quad
\Gamma(c_1)\cap X=\{4909\}.
\tag{3.7}
\]

Thus (0.3) is a statement about component-restricted shores.  The full
compiler profiles are not singleton sets.  Local rank rises exactly

\[
                              1\longrightarrow2.
\tag{3.8}
\]

This split leaves both target supports and both target degrees unchanged.
The rank gain is caused solely by changing occurrence co-incidence.
Therefore support-only, degree-only, and marginal-only routing theories
cannot detect the decisive move.

## 4. Exact occurrence-split theorems

Let \(D=(X,Y)\) be a bipartite excess-one component:

\[
                         |X|=|Y|+1,\qquad\nu(D)=|Y|.
\tag{4.1}
\]

For a physical right occurrence \(y\), write

\[
                         \Gamma_D(y)=\Gamma(y)\cap X.
\]

### Theorem 4.1 (binary occurrence-split criterion)

Replace one occurrence \(y\in Y\) by two distinct occurrences \(y_0,y_1\),
leaving \(Y\setminus\{y\}\) unchanged.  The refined component has a
matching saturating \(X\) if and only if there exist distinct targets

\[
 x_0\in\Gamma_D(y_0),\qquad x_1\in\Gamma_D(y_1)
\tag{4.2}
\]

such that \(X\setminus\{x_0,x_1\}\) is matchable into
\(Y\setminus\{y\}\).

#### Proof

The refined right side has

\[
                  |Y|-1+2=|Y|+1=|X|
\]

occurrences.  A matching saturating \(X\) therefore uses both \(y_0\) and
\(y_1\).  Delete their two matching edges to obtain the residual matching
in the stated graph.

Conversely, adjoin the two distinct edges \(x_0y_0,x_1y_1\) to such a
residual matching.  The result has size \(|X|\) and saturates \(X\).
\(\square\)

### Corollary 4.2 (refinement monotonicity and strictness)

Assume additionally that

\[
             \Gamma_D(y)\subseteq
             \Gamma_D(y_0)\cup\Gamma_D(y_1).
\tag{4.3}
\]

Then every old matching survives: replace its edge at \(y\), if used, by
an edge from the same target to a child containing it.  Hence matching rank
does not decrease.  It rises by at most one, because the right side gained
only one occurrence, and it rises exactly one if and only if Theorem 4.1
holds.

If the two child profiles partition \(\Gamma_D(y)\), every target retains
the same component-restricted degree.  Consequently even exact target
degrees do not determine transversal matching rank.

### Theorem 4.3 (every nontrivial circuit is abstractly splittable)

Suppose \(D=(X,Y)\) is connected, \(|Y|>0\), and every target is exposed:

\[
                 \nu(D-x)=|Y|\qquad(x\in X).
\tag{4.4}
\]

Then some right occurrence admits a binary partition satisfying
Theorem 4.1.

#### Proof

Choose \(x_0\in X\) and a matching \(M\) of \(D-x_0\) saturating \(Y\).
Connectivity and \(|Y|>0\) give a neighbour \(y\in Y\) of \(x_0\).
Since \(M\) saturates \(Y\), it matches \(y\) to a target
\(x_1\ne x_0\).  Delete the edge \(x_1y\).  The remainder matches
\(X\setminus\{x_0,x_1\}\) into \(Y\setminus\{y\}\).

Partition \(\Gamma_D(y)\) into two nonempty parts which put \(x_0\) and
\(x_1\) in different children.  Theorem 4.1 now applies.  \(\square\)

The Hall-23 audit established (4.4) in all 23 deficient components.  Thus
every one with \(|Y|>0\) has an abstract binary splitter.  This is a genuine
matching theorem, but it says nothing about whether a segment braid can
materialize the required two physical child profiles.

A `1/0` zero component is categorically different: it has no right
occurrence to split.  It needs a first-cell ear.

## 5. Exact polarization of a 2/1 compiler cell

A physical compiler cell \(c\) has signature

\[
             \Sigma(c)=(E_c,F_c,(P_p)_{p\in I_c}),
\tag{5.1}
\]

and a target mask \(S\) is eligible exactly when

\[
 F_c\subseteq S\subseteq E_c,
 \qquad
 S\cap P_p\ne\varnothing\quad(p\in I_c).
\tag{5.2}
\]

Let \(K\subset K+\{e\}\), abbreviated \(K+e\).

### Lemma 5.1 (lower-only and upper-only criteria)

1. If \(K\) is eligible at \(c\), then \(K+e\) is ineligible exactly when
   \(e\notin E_c\).
2. If \(K+e\) is eligible at \(c\), then \(K\) is ineligible exactly when
   either
   \[
                              e\in F_c
   \tag{5.3}
   \]
   or some \(p\in I_c\) satisfies
   \[
                              P_p\cap K=\varnothing.
   \tag{5.4}
   \]
   Under the assumed eligibility of \(K+e\), (5.4) necessarily has
   \(e\in P_p\).

#### Proof

If \(K\) satisfies (5.2), enlarging it to \(K+e\) preserves the mandatory
containment and every positive hit.  The only possible failure is the upper
envelope, exactly \(e\notin E_c\).

Conversely, removing \(e\) from an eligible \(K+e\) automatically preserves
the upper-envelope condition.  It fails (5.2) precisely by deleting a
mandatory coordinate, giving (5.3), or by deleting the unique hit in one
of the displayed source masks, giving (5.4).  \(\square\)

Thus a sole shore \(\{K,K+e\}\) is polarized by one \(e\)-absent child and
one \(e\)-essential child.

For the certified split,

\[
                         K=4877,\qquad e=32
\tag{5.5}
\]

(coordinate label `6`).  The old cell has

\[
 (d,s,E,F)=(2,739,4909,4876)
\tag{5.6}
\]

and serves both targets.  The new lower child

\[
 (d,s,E,F)=(1,740,4877,4612)
\tag{5.7}
\]

is \(K\)-only because \(32\notin E\).  The new upper child

\[
 (d,s,E,F)=(2,739,4909,4652)
\tag{5.8}
\]

is \(K+32\)-only because \(32\in F\).

## 6. Neutral braids form a decorated groupoid

A decorated carrier \(C\) records at least:

1. the ordered middle path and its distinct physical cell occurrences;
2. every occurrence profile \(\Gamma_C(c)\);
3. the required lower and upper support ledger, or the full multiplicity
   ledger if that stronger statement is intended;
4. all residence collars;
5. a protected maximum matching and its exposed-root data; and
6. for a literal theorem, one explicit common-\(Q\) pin/owner witness.

A legal segment braid is reversible, but its cuts and endpoint tests depend
on the current carrier.  Consequently the carriers and legal braid paths
form a groupoid \(\mathscr R\):

* objects are decorated carriers;
* arrows are legal braid paths;
* inversion reverses a legal path.

Fix a protected ledger \(\lambda\), a transported common-\(Q\) witness
\(\mathcal Q\), and a matching rank \(n\).  The arrows between objects
having those data and rank \(n\) form the neutral subgroupoid

\[
                         \mathscr R_{\lambda,\mathcal Q,n}.
\tag{6.1}
\]

Only the closed loops

\[
                         \operatorname{Aut}_{\mathscr R}(C)
\]

at one fixed decorated carrier form a group.  Referring to all neutral
braids as a single group suppresses the state-dependent legality gate.

There is a second scope distinction.  If \(\lambda\) records only
\[
                         {\bf1}_{\mu_{q,S}>0},
\]
then (0.1) lies in the support-safe class.  If it records every
multiplicity \(\mu_{q,S}\), (1.9) proves that (0.1) does not lie in one
fixed stratum.

## 7. Splitter transport and the exact orbit theorem

A decorated rooted-ear installation at \(C\) is a tuple

\[
 p=(D,x,M_{D-x},M_{\rm out},B^-,B^+,
       \text{ordered seams},\text{collars},\lambda,\mathcal Q),
\tag{7.1}
\]

where:

* \(D\) is a live excess-one component;
* \(x\) is an exposed root;
* \(M_{D-x}\) matches \(D-x\);
* \(M_{\rm out}\) is the protected complement matching;
* \(B^-,B^+\) are occurrence-level old/new banks;
* the remaining data certify endpoint legality, residence, shadows, and
  common-\(Q\).

Transport of an installed splitter is not automatic from reversibility of
the router.  If

\[
\begin{array}{ccc}
C&\xrightarrow{s}&C^+\\
\downarrow r&&\downarrow r^+\\
C'&\xrightarrow{s'}&C'^+
\end{array}
\tag{7.2}
\]

is to transport \(s\) along a neutral router \(r\), one must audit a
commuting physical braid square

\[
                         s'\circ r=r^+\circ s
\tag{7.3}
\]

with both collars and \(\mathcal Q\) valid.  Without \(r^+\) or an
equivalent direct collar certificate, there is no conjugation theorem.

Define the **decorated lift graph** \(\mathcal K\) as follows.

* Its vertices are verified pairs \((C,p)\).
* Two vertices are adjacent when a neutral braid path transports the whole
  installation data in (7.1), with an audited square or direct equivalent.
* A vertex is labelled by the rooted circuit ear it services.

### Theorem 7.1 (necessary and sufficient routing orbit)

Fix a seed installation \((C_0,p_0)\).  A decorated circuit ear is routable
by this seed if and only if it labels a vertex in the connected component

\[
                         \mathcal K(C_0,p_0).
\tag{7.4}
\]

#### Proof

A path in \(\mathcal K\) composes its verified neutral transports and ends
at a legal installation of the seed at the desired ear.  Conversely, any
claimed route is, by definition, a sequence of such verified transports
and hence a path in \(\mathcal K\).  \(\square\)

If splitter transport is already known to be functorial, (7.4) is the
ordinary groupoid orbit.  The lift-graph formulation is safer because
functoriality is one of the facts that must be proved.

### Corollary 7.2 (rooted-ear transitivity criterion)

If the connected component (7.4) contains a valid installed port for every
live nonzero circuit, the seed splitter can discharge any chosen one of
them.  Transitivity on unlabelled roots, target supports, or shadow
marginals is insufficient.

Whole-component incidence conjugacy is also too rigid: it preserves
\((|X|,|Y|)\), while the Hall-22 deficient components have several different
sizes.  Rooted-ear ports avoid this artificial obstruction because the
exposed-root theorem has the same local form in every component size.

### Corollary 7.3 (packet-swap sufficient condition)

Suppose a carrier is decomposed into finitely many decorated packets and:

1. every required adjacent packet transposition has a verified
   \(\lambda,\mathcal Q\)-safe neutral braid square;
2. those transpositions generate a connected swap graph on the installed
   rooted-ear ports; and
3. every live circuit has a socket in that graph.

Then adjacent swaps route the seed to every socket.  If all adjacent
transpositions are available, the swap group is the full symmetric group;
a distinguished packet reaches any position in at most one less than the
number of movable packets.

This is a proved sufficient theorem.  Its hypotheses have not been
established for the Hall-22 carrier.

## 8. Turn-colour holonomy

For a Johnson edge \(UV\), define its turn colour by

\[
                         \chi(UV)=U\triangle V
                         \in\binom{[15]}2.
\tag{8.1}
\]

View these two-subsets as edges of the coordinate graph \(K_{15}\).

### Theorem 8.1 (Eulerian seam-current invariant)

Let \(T,T'\) be Johnson paths with the same ordered endpoints.  Let
\[
 \Delta_\chi(e)=
 \#\{i:\chi(T'_iT'_{i+1})=e\}
 -
 \#\{i:\chi(T_iT_{i+1})=e\}.
\tag{8.2}
\]

For every coordinate \(j\),

\[
                         \sum_{e\ni j}\Delta_\chi(e)\equiv0\pmod2.
\tag{8.3}
\]

If \(T'\) is a signed segment reassembly of \(T\), all internal edge colours
cancel, including inside reversed segments, so (8.2) is supported entirely
on the old and new seams.  Its mod-two seam current is therefore an Eulerian
subgraph of \(K_{15}\).

#### Proof

Along any Johnson path, membership of coordinate \(j\) toggles exactly on
the edges whose colour contains \(j\).  Hence the parity of their number is

\[
                         {\bf1}_{j\in T_0\triangle T_{W-1}}.
\]

The endpoints of \(T,T'\) agree, so subtracting the two equal parities gives
(8.3).  Segment transport and reversal preserve every internal unordered
turn colour, proving the localization statement.  \(\square\)

For the neutral router in (0.1), the old colours are

\[
                         \{3,8\},\{8,13\},\{8,15\}
\]

and the new colours are the identical multiset in another order.  Its
turn-colour current is zero.

For the splitter, cancellation of the common colour \(\{10,12\}\) leaves

\[
 +\{2,6\}+\{6,15\}-\{2,14\}-\{14,15\},
\tag{8.4}
\]

the alternating coordinate cycle

\[
                         2-6-15-14-2.
\tag{8.5}
\]

The local axis-\(6\) splitter is therefore accompanied by a remote second
axis-\(6\) port.  More generally, any proposed local collar having odd
turn-colour degree at coordinate \(j\) requires another \(j\)-port elsewhere
in the same compound.  This is a hard parity obstruction to isolated
one-port routing.

## 9. Common-\(Q\) is a separate decorated gate

Let \(\Phi\) be a selected physical owner/pin system.  For each coordinate
\(a\), its surviving source positions have the form

\[
 Z_a=
 \{p:a\in P_p\}
 \setminus
 \bigcup_{\substack{(I,S)\in\Phi\\a\notin S}} I.
\tag{9.1}
\]

One common nonzero word realizes the selected system exactly when:

1. every prescribed positive pin \((p,a)\) has \(p\in Z_a\);
2. every central four-window for a middle owner containing \(a\) meets
   \(Z_a\);
3. every selected interval \(I\) with target \(S\ni a\) meets \(Z_a\); and
4. every source position belongs to at least one \(Z_a\).

The maximal realizing word is \(A_p=\{a:p\in Z_a\}\).

If the controller and every old pin are fixed and one adds a new target pin
\((I,K)\), then exactly

\[
 Z'_a=
 \begin{cases}
 Z_a,&a\in K,\\
 Z_a\setminus I,&a\notin K.
 \end{cases}
\tag{9.2}
\]

Thus the new negative interval can erase a central witness, an old positive
pin witness, or the last coordinate at a source position.  Hall neutrality
does not control any of these failures.

### Lemma 9.1 (finite seam-collar common-\(Q\) audit)

For depth \(d\) and protected shadow depth at most \(H\), put

\[
                         R=\max\{H,2d\}.
\tag{9.3}
\]

Under a segment reassembly, a maximal-erosion position and every protected
interval wholly contained in a retained segment at distance more than \(R\)
from all old and new seams transport by translation or reflection with
unchanged coordinate data.  Consequently the common-\(Q\) conditions above
need fresh verification only for:

1. central windows meeting an old or new \(R\)-collar;
2. protected intervals cut by, or newly crossing, a seam;
3. positive pins installed in a changed bank; and
4. nonemptiness at source positions in the new collars.

Provided every demand outside these lists retains a transported witness,
passing these finite collar checks is necessary and sufficient for the
transported pin system.

#### Proof

Away from the collars, the relevant middle window and maximal erosion
window lie wholly in one retained segment.  Translation or reflection
preserves their intersection, and a protected interval inside that segment
remains contiguous with the same target label.  Hence its old witness maps
to a new witness.  Every condition not covered in this way is exactly one
of the four displayed boundary classes, and the global criterion above is a
conjunction of these demands.  \(\square\)

At `d=3`, compiler depth `h=0,1,2`, a seam at `a` can change a complete cell
signature beginning at `s` only if

\[
                         a-h-3\le s\le a+5.
\tag{9.4}
\]

Thus one seam changes at most `9+10+11=30` complete signatures.  For the
present all-upper ledger \(H=7\), (9.3) gives \(R=7\).

The Hall-22 JSON artifacts contain a middle path and an outer compiler Hall
report, but no selected matching \(\Phi\), common-\(Q\) certificate, or
literal word.  Therefore (0.1) proves neither common-\(Q\) preservation nor
a word of length `6438`.  A universal routing theorem must add exactly the
decoration and collar audit of this section.

## 10. Iteration theorem

### Theorem 10.1 (neutral-router/splitter descent)

Fix a support/residence/common-\(Q\) decorated class.  Suppose every carrier
in the class with deficiency \(h>0\) has:

1. a protected maximum matching whose deficient part is a direct sum of
   \(h\) occurrence-disjoint excess-one transversal circuits;
2. neutral routers which retain or explicitly reroute that matching;
3. for every chosen live nonzero circuit, a rooted-ear installation in the
   seed's lift-graph component;
4. a splitter which perfects that circuit, retains the complement matching,
   and outputs another carrier in the same decorated class with the other
   circuits still certified.

Then one splitter lowers Hall deficiency by exactly one.  Repeating reaches
Hall zero after exactly \(h\) splitter steps.  If at most \(a\) neutral
braids precede each splitter, at most \(h(a+1)\) braids are used.

#### Proof

Theorem 4.1 or the exposed-root ear lemma adds one matching edge in the
chosen direct summand.  The retained complement matching gives a global
matching larger by one.  One binary split adds only one right occurrence,
so the increase is exactly one.  Hypothesis 4 re-establishes the induction
with \(h-1\).  Every physical invariant persists because every router and
splitter arrow remains in the fixed decorated class.  \(\square\)

If a physical move changes other occurrence banks, local splitting is not
enough.  For

\[
 \sigma_C(S)=h(C)-\bigl(|S|-|N_C(S)|\bigr),\qquad
 I(S)=|N_{C'}(S)|-|N_C(S)|,
\tag{10.1}
\]

the exact global formula is

\[
 h(C')=h(C)-
 \min_{S\subseteq L}\bigl(\sigma_C(S)+I(S)\bigr).
\tag{10.2}
\]

Thus a one-unit descent requires the minimum in (10.2) to equal one.  This
is the all-shore replacement-component audit.

Theorem 10.1 does not include the seven `1/0` components.  Each requires a
first \(Q\)-compatible occurrence rather than a split.  A theorem covering
all components must add a zero-ear template and its own orbit/collar
conditions.

## 11. Sharp Hall-22 routing data

In the seven-zero Hall-22 carrier, the five remaining `2/1` circuits have
the following sole-cell signatures:

\[
\begin{array}{c|c|c|c|c}
K&e&s&E&F\\ \hline
2420&512&4136&2932&2416\\
2676&8192&1694&10868&2672\\
9524&64&1696&9588&1332\\
17683&4096&1685&21779&17683\\
19568&8192&3240&27760&19536.
\end{array}
\tag{11.1}
\]

The optional coordinate labels are respectively

\[
                         10,14,7,13,14.
\tag{11.2}
\]

Only axis `14` occurs twice.  Those two circuits are therefore the natural
candidate for a two-local-port compound whose same-axis holonomy closes
internally.  The axes `10`, `7`, and `13` each need a remote return port or
coupling to one of the larger deficient components.

This conclusion is only a parity-compatible target, not a braid
certificate.  The two local polarizations must still be placed in one
endpoint-valid signed block permutation, and every changed seam must pass
the exact support, residence, complement-matching, and common-\(Q\) audits.

The current exact next theorem can now be stated without ambiguity:

> Construct a connected decorated rooted-ear lift bank containing, for
> each remaining circuit axis \(e\), an \(e\)-polarized splitter together
> with an \(e\)-return port; or exhibit a lift-graph component invariant
> separating one of the ports from every such return.

One certified axis-\(6\) lift edge is not evidence of full connectedness.
Endpoint invariance, turn-colour holonomy, and protected common-\(Q\)
collars are already nontrivial component invariants.

## 12. Artifacts and hashes

The audited artifacts are:

* `scratch/k15_segment_braid_hall23.json`

  * file SHA-256:
    `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d`;
  * middle-path digest:
    `09b779278edaff5d00d4ef119a1ae6d15df8858557a3c700d9cac4764ef9c66b`.

* `scratch/k15_segment_braid_hall23_portal.json`

  * file SHA-256:
    `9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6`;
  * middle-path digest:
    `0e64bf84c77e2f7944717995e265d3677cebf60fbd2b7738cb39d5a4102f63d0`.

* `scratch/k15_segment_braid_hall22.json`

  * file SHA-256:
    `c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798`;
  * middle-path digest:
    `901edccb74a76656b838f034f3bb85029f5fba3e0466b7a0fd0b19661529cc3c`.

The independent exact reconstruction audit passes with no solver call.  It
reconstructs the segment permutations, Johnson chronology, residence,
every lower and upper support layer, the complete compiler graph, maximum
matchings, canonical DM shores, and contracted boundary ranks.

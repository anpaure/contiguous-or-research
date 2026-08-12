# Residence-safe erosion solves the literal lower schedule

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, or external input
is used.  No Greene--Kleitman/GMM order is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 H=\lceil A\sqrt m\rceil,
 \tag{0.1}
\]

where \(A>0\) is fixed.  Let \((M_t)\) be a disjoint union of cyclic
Johnson chronologies, on \(C\) components, which enumerate the \(W\)
rank-\(m\) masks once each.  Assume every positive coordinate residence
has length at least \(H+1\).  Suppose the morphological-preimage theorem has supplied
nonempty seeds \((Q_t^0)\) with

\[
 M_t=\bigcup_{j=t-H}^{t}Q_j^0,
 \qquad |Q_j^0|\le m-H.
 \tag{0.2}
\]

Define the forward erosions

\[
 D_{t,q}:=\bigcap_{i=0}^{q}M_{t+i}
 \quad(0\le q\le H),
 \qquad R_t:=D_{t,H}.
 \tag{0.3}
\]

Then the remaining **literal** lower-endpoint schedule has an exact
solution:

\[
 \boxed{|D_{t,q}|=m-q,}
 \tag{0.4}
\]

and

\[
 \boxed{
 \bigcup_{j=t-H+q}^{t}R_j=D_{t,q}
 \qquad(0\le q\le H).}
 \tag{0.5}
\]

Thus the componentwise cyclic word \(R=(R_t)\), of core length exactly
\(W\), retains every middle owner and simultaneously realizes the nested lower flag

\[
 M_t=D_{t,0}\supset D_{t,1}\supset\cdots\supset D_{t,H}
 \tag{0.6}
\]

at every endpoint.  Moreover \(Q_t^0\subseteq R_t\), so this is an
allowed enlargement of the sparse morphological seeds, not a second
word.

The coordinatewise forbidden-interval condition is automatic.  If a
coordinate residence is \([a,b]\), then its occurrences in \(R\) are
exactly \([a,b-H]\).  Every endpoint which drops that coordinate uses
the same port \(b-H\); survivor ports lie weakly before it.  Hence the
dropout arcs form one common-left packet per residence run, and packets
from different runs are disjoint.

What remains is no longer a physical scheduling problem.  It is the
following exact image/path-hitting census:

\[
 \Phi_q(t):=D_{t,q},\qquad
 \mathfrak H_H:=
 \sum_{q=1}^{H}
 \left(\binom n{m-q}-|\operatorname {im}\Phi_q|\right).
 \tag{0.7}
\]

The scheduled endpoint flags miss exactly the summands in (0.7).  If
\(\mathfrak H_H=o(W)\), appending the missing targets literally costs
\(o(W)\), and the lower annulus is finished at coefficient one.  At
depth \(q\), a target \(T\) lies in the image precisely when one factor
component contains a consecutive \((q+1)\)-owner Johnson path inside
the up-set of \(T\).  In particular, (0.7) is the exact path-hitting
gate requested in the attachment audit.

If one insists on **exact SCD ownership**, rather than merely literal
coverage, an additional integral grouping problem survives.  It asks
for nested endpoint sets \(A_H\subseteq\cdots\subseteq A_1\subseteq A_0\)
such that \(\Phi_q:A_q\to\binom{[n]}{m-q}\) is bijective for every
\(q\).  Section 5 gives the exact layered Hall formulation.  This
grouping is sufficient but is not needed for the weaker missing-target
criterion (0.7).

## 1. Exact ranks of the forward erosions

Every transition has the form

\[
 M_{s+1}=M_s-x_s+y_s.
 \tag{1.1}
\]

There are no equal consecutive owners because the chronology enumerates
the middle layer without repetition.

### Lemma 1.1 (no short recycling)

For fixed \(t\), the coordinates

\[
 x_t,x_{t+1},\ldots,x_{t+H-1}
 \tag{1.2}
\]

are distinct members of \(M_t\).  Consequently

\[
 D_{t,q}=M_t\setminus\{x_t,x_{t+1},\ldots,x_{t+q-1}\}
 \quad(0\le q\le H).
 \tag{1.3}
\]

#### Proof

If a coordinate inserted after time \(t\) were removed by time \(t+H\),
its resulting positive residence would have length at most \(H\),
contrary to residence safety.  Therefore every coordinate removed in
the next \(H\) transitions was already in \(M_t\).  Once it is removed,
it cannot be removed a second time in the same interval: that would
require an intervening insertion followed by a positive residence of
length at most \(H\).  Thus the removed coordinates are distinct, and
(1.3) follows.  \(\square\)

Equation (0.4) is immediate.  Notice that this is exactly where both
hypotheses matter.  If equal owner steps are allowed, or if a coordinate
may return and leave within \(H\) steps, the erosion can have rank larger
than \(m-q\), and the argument below no longer supplies an SCD-quality
rank flag.

## 2. The erosion-word identity

### Theorem 2.1 (residence-safe lower endpoint schedule)

For every \(0\le q\le H\), identity (0.5) holds.  Hence the word

\[
 R_t=\bigcap_{i=0}^{H}M_{t+i}
 \tag{2.1}
\]

has the following properties:

1. every letter is nonempty and has size exactly \(m-H\);
2. its \((H+1)\)-window ending at \(t\) has union \(M_t\);
3. its suffix beginning at \(t-H+q\) has union \(D_{t,q}\); and
4. it is an enlargement of every seed word satisfying (0.2).

#### Proof

It suffices to check (0.5) coordinatewise.  Lift one cyclic positive
residence of a coordinate \(x\) to an interval \([a,b]\).  By definition,

\[
 x\in R_j
 \quad\Longleftrightarrow\quad
 [j,j+H]\subseteq[a,b]
 \quad\Longleftrightarrow\quad
 a\le j\le b-H.
 \tag{2.2}
\]

If \(x\) is positive on the whole cyclic component, it belongs to every
set on both sides of (0.5), so there is nothing to prove.  Constant-zero
coordinates likewise contribute to neither side.  For a nonconstant
run, (2.2) gives

\[
 x\in\bigcup_{j=t-H+q}^{t}R_j
 \tag{2.3}
\]

if and only if the two integer intervals

\[
 [t-H+q,t]\quad\text{and}\quad[a,b-H]
 \tag{2.4}
\]

meet.  They meet if and only if \(a\le t\) and \(t+q\le b\).  The latter
condition is exactly

\[
 x\in\bigcap_{i=0}^{q}M_{t+i}=D_{t,q}.
 \tag{2.5}
\]

This proves (0.5).  Lemma 1.1 gives \(|R_t|=m-H>0\).  The case \(q=0\)
of (0.5) is the middle-window identity.

Finally, if \(x\in Q_t^0\), then (0.2) forces \(x\in M_s\) for every
\(s\in[t,t+H]\), because the letter at \(t\) occurs in each of those
backward windows.  Hence \(x\in R_t\), proving
\(Q_t^0\subseteq R_t\).  \(\square\)

Theorem 2.1 is the exact morphological opening identity for binary
residence runs of length at least \(H+1\).  It is noncanonical with
respect to Boolean SCDs: its deletion order is dictated by future
Johnson exits, not by a GMM bracketing order.

## 3. Forbidden-interval audit

Although (0.5) already constructs the literal word, it is useful to
audit it in the endpoint-port language.

Fix a positive residence \([a,b]\) of \(x\).  At endpoint \(t\), if
\(x\) is deleted within the protected depth, then

\[
 d_t(x)=b-t+1\in[H].
 \tag{3.1}
\]

The forced singleton port is

\[
 p_t(x)=t-H+d_t(x)-1=b-H,
 \tag{3.2}
\]

independent of \(t\).  The first absent suffix is

\[
 Z_t(x)=(b-H,t].
 \tag{3.3}
\]

Thus all dropout arcs belonging to this residence have the same left
boundary \(b-H\).  If the endpoint survives with \(x\) through depth
\(H\), then \(t+H\le b\), so its survivor port satisfies

\[
 t\le b-H.
 \tag{3.4}
\]

It lies outside every interval in (3.3).  The next packet begins no
earlier than the start of its positive residence, hence strictly after
the preceding positive residence ends.  Packets from distinct runs are
therefore disjoint.  A coordinate positive on an entire cyclic component
never drops and creates no dropout packet.

The seed audit is equally exact.  An occurrence \(x\in Q_j^0\) forces
\([j,j+H]\subseteq[a,b]\), hence

\[
 j\le b-H.
 \tag{3.5}
\]

No seed occurrence lies in the forbidden union (3.3).  Conversely,
\(R_{b-H}\) contains \(x\), so every dropout packet has its required
port occurrence.  Therefore, for every coordinate, every dropout port,
every survivor port, and every fixed seed occurrence passes the exact
coordinatewise forbidden-interval criterion.

This removes the cross-endpoint packet obstruction for the erosion
schedule.  The common-left packet is not something that must be found by
rounding; it is forced by the right endpoint \(b\) of the coordinate
residence.

## 4. The exact coverage and obstruction census

For \(1\le q\le H\), set

\[
 \mathcal T_q:=\binom{[n]}{m-q},
 \qquad \Phi_q(t):=D_{t,q},
 \tag{4.1}
\]

and define the scheduled load

\[
 L_q(T):=|\{t:\Phi_q(t)=T\}|.
 \tag{4.2}
\]

### Theorem 4.1 (path-hitting equivalence)

For \(T\in\mathcal T_q\), the following are equivalent.

1. \(L_q(T)>0\).
2. Some scheduled suffix of the erosion word has union \(T\).
3. Some factor component contains \(q+1\) consecutive middle owners all
   lying in the up-set

   \[
   U_T:=\{M\in\tbinom{[n]}m:T\subseteq M\}.
   \tag{4.3}
   \]

#### Proof

The equivalence of 1 and 2 is (0.5).  If \(\Phi_q(t)=T\), then by
definition every owner \(M_t,\ldots,M_{t+q}\) contains \(T\), proving 3.
Conversely, if those \(q+1\) owners contain \(T\), then
\(T\subseteq D_{t,q}\).  Both sets have rank \(m-q\) by Lemma 1.1, so
they are equal.  \(\square\)

### Lemma 4.2 (maximal up-set runs)

Every consecutive run of owners inside \(U_T\) has length at most
\(q+1\).  Consequently

\[
 L_q(T)=
 \#\{\text{positive runs of }\mathbf 1_{\{M_t\in U_T\}}
       \text{ having length exactly }q+1\}.
 \tag{4.3a}
\]

#### Proof

An owner containing \(T\) has exactly \(q\) coordinates outside \(T\).
During consecutive Johnson transitions which stay inside \(U_T\), no
coordinate of \(T\) may leave.  The first \(q\) outgoing coordinates
are distinct coordinates outside \(T\), by the same no-short-recycling
argument as Lemma 1.1.  After those \(q\) transitions, all \(q\) original
outside coordinates have been replaced.  A further transition could
remove neither a coordinate of \(T\) nor one of the newly inserted
coordinates, since the latter has had positive residence at most \(q\le
H\).  Thus the run stops after at most \(q+1\) owners.  Theorem 4.1 now
gives (4.3a).  \(\square\)

Consequently the number of targets not covered by the scheduled endpoint
flags at depth \(q\) is exactly

\[
 h_q=|\{T:L_q(T)=0\}|
 =\binom n{m-q}-|\operatorname {im}\Phi_q|,
 \tag{4.4}
\]

and the aggregate is \(\mathfrak H_H=\sum_{q=1}^{H}h_q\).

Every endpoint contributes one value of \(\Phi_q\), so

\[
 \sum_{T\in\mathcal T_q}L_q(T)=W.
 \tag{4.4b}
\]

Consequently the missing-target count is exactly the linear
repeat-excess hinge

\[
 \boxed{
 h_q=
 \sum_{T\in\mathcal T_q}(L_q(T)-1)_+
 -(W-|\mathcal T_q|).}
 \tag{4.4c}
\]

Thus no quadratic covariance objective is required for this route.  The
unavoidable repeat budget is \(W-|\mathcal T_q|\); only excess repeats
beyond that floor create holes.

This is also the exact one-layer Hall deficiency.  Join a target \(T\)
to every endpoint in \(\Phi_q^{-1}(T)\).  The endpoint fibres for
different targets are disjoint, and therefore

\[
 \boxed{
 \max_{\mathcal A\subseteq\mathcal T_q}
 \bigl(|\mathcal A|-|N_q(\mathcal A)|\bigr)_+=h_q.}
 \tag{4.4a}
\]

Indeed, every hit target contributes at least one private endpoint to
its neighborhood, while every missing target contributes none; the
maximum is attained by the set of missing targets.  Thus there is no
fractional-to-integral gap at a fixed depth.  Only the common nested
selection in Section 5 couples the depths.

### Corollary 4.3 (coefficient-one lower completion)

If

\[
 \mathfrak H_H=o(W),\qquad HC=o(W),
 \tag{4.5}
\]

then linearize each cyclic component by duplicating its first \(H\)
letters and append every scheduled missing target as one nonempty literal
letter.  The resulting word has length

\[
 W+HC+\mathfrak H_H=W+o(W)
 \tag{4.5a}
\]

and covers the whole lower band through depth \(H\).  The duplicated
prefix captures precisely the endpoint windows which cross the chosen
cycle cut; the middle masks remain covered by (0.5).

At Gaussian depth,

\[
 \frac{|\mathcal T_H|}{W}
 =\prod_{j=0}^{H-1}\frac{m-j}{m+2+j}
 =e^{-A^2+o(1)}.
 \tag{4.6}
\]

Hence a positive-density failure of the depth-\(H\) path-hitting
condition is a linear obstruction to this erosion schedule.  Residence
safety alone controls the ranks and literal ports, but it does not imply
that every up-set contains a consecutive \((H+1)\)-owner path.  Thus
(4.5), or a stronger exact SCD grouping theorem, is the remaining
chronology-dependent assertion.

The word \(R\) may accidentally cover additional targets by intervals
not among the scheduled suffixes.  Therefore \(\mathfrak H_H\) is an
exact deficit of the endpoint schedule and a sufficient literal repair
bill; a large value obstructs this schedule, not every possible use of
all other intervals of \(R\).

## 5. Exact SCD grouping as a layered integral problem

For exact SCD-quality ownership, assign a radius \(h_t\in\{0,\ldots,H\}\)
to each endpoint and retain the deterministic erosion prefix

\[
 D_{t,0}\supset D_{t,1}\supset\cdots\supset D_{t,h_t}.
 \tag{5.1}
\]

Put

\[
 y_{t,q}:=\mathbf 1_{\{h_t\ge q\}}.
 \tag{5.2}
\]

The exact integral system is

\[
 y_{t,0}=1,
 \qquad y_{t,q+1}\le y_{t,q},
 \qquad y_{t,q}\in\{0,1\},
 \tag{5.3}
\]

and

\[
 \boxed{
 \sum_{t:\Phi_q(t)=T}y_{t,q}=1
 \quad(1\le q\le H,\ T\in\mathcal T_q).}
 \tag{5.4}
\]

Equation (5.4) automatically gives the exact SCD radius census

\[
 |\{t:h_t\ge q\}|=\binom n{m-q}.
 \tag{5.5}
\]

Equivalently, define

\[
 A_q:=\{t:h_t\ge q\}.
 \tag{5.6}
\]

Here \(A_0\) is the full \(W\)-element endpoint set.  Then the system asks for

\[
 A_H\subseteq A_{H-1}\subseteq\cdots\subseteq A_1\subseteq A_0
 \tag{5.7}
\]

such that

\[
 \Phi_q|_{A_q}:A_q\longrightarrow\mathcal T_q
 \quad\text{is a bijection for every }q.
 \tag{5.8}
\]

The exact aggregate near-SCD deficiency is therefore

\[
 \boxed{
 \mathfrak D_H^{\rm SCD}:=
 \min_{\substack{A_H\subseteq\cdots\subseteq A_0,\ |A_0|=W\\
                  \Phi_q|_{A_q}\text{ injective}}}
 \sum_{q=1}^{H}\left(\binom n{m-q}-|A_q|\right).}
 \tag{5.8a}
\]

The desired approximate grouping statement is
\(\mathfrak D_H^{\rm SCD}=o(W)\).  Plainly
\(\mathfrak D_H^{\rm SCD}\ge\mathfrak H_H\), since nesting can only
discard endpoint occurrences.

### Theorem 5.1 (exact layered Hall/reachability formulation)

Suppose \(A_q\) already satisfies (5.8).  A next layer
\(A_{q+1}\subseteq A_q\) satisfying (5.8) exists if and only if

\[
 \boxed{
 A_q\cap\Phi_{q+1}^{-1}(T)\ne\varnothing
 \quad\text{for every }T\in\mathcal T_{q+1}.}
 \tag{5.9}
\]

When (5.9) holds, choose one endpoint from each displayed fibre.  The
fibres are disjoint, so the choice is integral and produces
\(A_{q+1}\).

For a near grouping, the exact next-layer deficiency from state \(A_q\)
is

\[
 \delta_{q+1}(A_q)
 :=\left|\left\{T\in\mathcal T_{q+1}:
 A_q\cap\Phi_{q+1}^{-1}(T)=\varnothing\right\}\right|.
 \tag{5.10}
\]

Thus the requested \(o(W)\)-deficiency theorem is precisely the existence
of successive choices in (5.7) for which the aggregate number of empty
fibres is \(o(W)\), with earlier choices optimized for all later layers.

#### Proof

Necessity of (5.9) is immediate.  For sufficiency, the sets
\(A_q\cap\Phi_{q+1}^{-1}(T)\), as \(T\) varies, are pairwise disjoint.
Selecting one point from each gives a set on which \(\Phi_{q+1}\) is
bijective.  Formula (5.10) is the same argument with empty fibres left
unmatched.  \(\square\)

For the first nontrivial look-ahead, make a bipartite occurrence graph
between \(\mathcal T_q\) and \(\mathcal T_{q+1}\), placing one edge
labelled \(t\) from \(\Phi_q(t)\) to \(\Phi_{q+1}(t)\).  Choosing one
occurrence over each \(q\)-target while ensuring every
\((q+1)\)-target is hit, assuming every \(q\)-target has an occurrence,
is possible exactly when this graph has a
matching saturating \(\mathcal T_{q+1}\), equivalently when

\[
 |N(\mathcal B)|\ge|\mathcal B|
 \quad\text{for every }\mathcal B\subseteq\mathcal T_{q+1}.
 \tag{5.11}
\]

Accordingly the exact adjacent-layer Hall obstruction is

\[
 \epsilon_{q+1}:=
 \max_{\mathcal B\subseteq\mathcal T_{q+1}}
 \bigl(|\mathcal B|-|N(\mathcal B)|\bigr)_+.
 \tag{5.11a}
\]

One has \(\mathfrak D_H^{\rm SCD}\ge\epsilon_{q+1}\) for every \(q\).
All \(\epsilon_{q+1}=0\) are necessary, and each is sufficient for its
isolated two-layer problem.

For more than two layers, pairwise choices must use the same endpoint
trace.  The retained state is therefore the whole prefix

\[
 (\Phi_1(t),\ldots,\Phi_q(t)),
 \tag{5.12}
\]

not just its last target.  This is the exact layered Hall state which an
unlabelled rank-by-rank flow loses.

## 6. Integrality audit

The physical part of the construction is completely integral: the word
is explicitly \(R_t=D_{t,H}\), and the literal port for every deletion
is explicitly \(b-H\).  No fractional rounding occurs in Sections 1--4.

The optional exact grouping system (5.3)--(5.4) is a different matter.
At two adjacent depths it is a bipartite matching problem and is
integral by (5.11).  Across three or more depths, nesting alone does not
give total unimodularity.  In the equivalent column formulation, let
\(z_{t,h}\) select the whole radius-\(h\) prefix at endpoint \(t\); its
target incidences are \((q,\Phi_q(t))\) for \(q\le h\).  Abstract
nested-chain columns already admit the determinant-two pattern

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \tag{6.1}
\]

obtained from three columns which agree pairwise at three different
depths.  For example, take a set \(C\), distinct \(u,v,w\notin C\), and
\(c\in C\).  Three depth-1/depth-2/depth-3 traces can begin

\[
 \begin{array}{c|ccc}
 &1&2&3\\ \hline
 1&C+u+v&C+u&(C-c)+u\\
 2&C+u+v&C+v&C\\
 3&C+u+w&C+u&C
 \end{array}.
 \tag{6.2}
\]

The rows corresponding to \(C+u+v\) at depth 1, \(C+u\) at depth 2,
and \(C\) at depth 3 give (6.1).  Therefore a TU claim for the natural
column matrix would have to use a special property of the actual Johnson
chronology; it does not follow from abstract nesting or residence safety
alone.  This is not a proof that the actual erosion catalogue contains
the minor.

This determinant does **not** obstruct the weaker coverage criterion
(4.5).  Coverage uses all endpoint flags simultaneously and permits
repeated witnesses.  It is exactly why the note separates literal
completion from exact SCD grouping.

## 7. Precise surviving gate

The lower-annulus interface now has the following status.

Proved:

1. every forward erosion has the exact required rank;
2. the erosion word \(R_t=\bigcap_{i=0}^{H}M_{t+i}\) retains all middle
   windows and realizes all forward lower flags;
3. the erosion word enlarges the given sparse morphological seeds;
4. all dropout, survivor, and seed occurrences satisfy the exact
   coordinatewise forbidden-interval criterion; and
5. the missing scheduled targets have the exact path-hitting census
   (0.7).

Still required for the weakest coefficient-one transfer:

\[
 \boxed{
 \sum_{q=1}^{H}
 \left(\binom n{m-q}-
 |\{\bigcap_{i=0}^{q}M_{t+i}:t\}|\right)=o(W).}
 \tag{7.1}
\]

together with the already familiar component ledger \(HC=o(W)\).

Still required only if exact SCD ownership is imposed:

\[
 \boxed{\text{an integral solution of (5.3)--(5.4), or an }o(W)
 \text{-deficiency version of it}.}
 \tag{7.2}
\]

Thus the lower endpoint **schedule and its literalization are closed**
under the stated exact-owner residence hypothesis.  The remaining
Gaussian question is target-image expansion of the actual chronology,
followed, only for the stronger SCD formulation, by synchronized
root-transversal selection.  The canonical GMM order plays no role.

# Lane X: shared PBBS seams after the quadratic toll — exact endpoint boundary

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Verdict

There are two separate conclusions.

First, the asserted premise in
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md` is false.
The condition \(d(D)=1\) does not force a return at
\(2\operatorname{ht}(D)+1\).  The primitive semilength-five word

\[
 D=1110011000
\]

has \(d(D)=1\) and height three, but has no gap-seven return.  Thus that
report does not disprove \((RP_A)\), and a shared seam cannot be demanded
from its claimed Catalan-positive primitive reservoir.

Second, the requested \(\Omega(H^2)\) one-cut lower bound is itself
impossible.  For every rank-\((m+1)\) Johnson walk and every cut, provided

\[
 2H\le m+1,
\]

there is a direct nonzero literal word of length

\[
 \boxed{4H-1}
\]

which realizes every floor-correct lower crossing intersection and every
upper crossing union through depth \(H\).  The lower word is a
\((2H-1)\)-vertex Pareto dominance staircase; the upper word is the
\(2H\)-owner collar.  An independent audit found no defect in the
departure injection, staircase interception, contiguity, nonzero-letter
bound, or multi-cut ledger.

The worst-case local order is therefore \(\Theta(H)\), not
\(\Theta(H^2)\).  What can still be fatal is paying this linear chart
independently at

\[
 J=\Theta(W/H)
\]

cuts, which costs \(\Theta(HJ)=\Theta(W)\).

The exact global endpoint dichotomy is the following.  At depth \(q\),
let \(R_q^\pm\) be the crossing requests at the selected cuts, and let
\(\kappa_q^\pm\) be the largest multiplicity of one literal target value.
Every **standalone** fused seam chart has length

\[
 \boxed{
 n\ge
 \max_{q,\pm}|\operatorname{supp}R_q^\pm|
 \ge
 \max_{q,\pm}{|R_q^\pm|\over\kappa_q^\pm}.}
\]

Hence \(qJ\) requests at some \(q\asymp H\), with bounded target
multiplicity, force \(\Omega(HJ)\) chart positions.  A standalone
\(o(HJ)\) repair is possible only if most requests are support-redundant
or if cross-cut target multiplicities diverge.

The weakest fusion target not killed by this theorem is consequently
**baseline-relative and support-selective**:

> Keep only one request for every target value which has no intact witness
> elsewhere.  Reuse or recode the original \(\ell=\Theta(HJ)\) baseline
> positions as the endpoints and interiors of one global word, insert only
> \(o(HJ)\) new positions, and realize all support-essential crossing and
> internal targets by one common Safe-Pin chronology.  Targets sharing an
> endpoint across depths must form nested flags.  For strict
> \(D=\Theta(H)\) towers, the increment pins must have harmonic
> common-target degree \(\Omega(H)\) on average.

Endpoint throughput permits this in-place theorem because the necessary
\(\Theta(HJ)\) endpoints are already paid for in the baseline.  It rules
out interpreting fusion as a separate short appendage which services every
crossing occurrence.

## 1. The primitive-return premise fails before seam questions

For the first-maximum factorization

\[
 D=P1R0S,
\]

put

\[
 \delta(D)=|P|+1,
 \qquad d(D)=|S|+1,
 \qquad \tau D=S1P0R.
\]

Take

\[
 D_0=1110011000,
 \qquad N=11.
\]

It is primitive, has height three, and has \(S=\varnothing\), so
\(d(D_0)=1\).  Exact applications of the block rotation give

\[
\begin{array}{c|c|c}
D_j&\delta(D_j)&d(D_j)\\ \hline
1110011000&3&1\\
1110001100&3&5\\
1100111000&7&1,
\end{array}
\qquad D_3=D_0.
\]

At the alleged height-three zero-winding hit,

\[
 \sum_{j=0}^{2}d(D_j)=1+5+1=7,
 \qquad
 \delta(D_3)=3.
\]

These are not even congruent modulo eleven.  Therefore there is no
gap-seven return.

The exact error in the proposed sector proof is that a forest transported
from a post-spine \(B\)-sector into a pre-spine \(A\)-sector can attain the
global height at its new positive attachment depth.  Controlling only its
relative height when it reaches the root seam is insufficient.  The
canonical first maximum can change before the alleged height cycle closes.

The Catalan height estimate and the later deck-packing calculation in the
purported counterexample are valid **conditional** calculations.  What is
missing is the claimed Catalan family of actual returns.  Accordingly the
named report supplies neither a disproof of \((RP_A)\) nor a
positive-density seam reservoir.

## 2. Exact linear one-cut seam

Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\},
 \qquad X_i\in\binom{\Omega}{m+1},
\]

and cut between \(X_{-1}\) and \(X_0\).  Put

\[
 C=X_{-1}\cap X_0,
 \qquad |C|=m.
\]

For \(1\le s,t\le H\), define

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.
\]

This intersection uses \(s+t\) owners and \(s+t-1\) Johnson
transitions, so

\[
 |P_{s,t}|\ge m+2-s-t.
\]

Call the query floor-correct when equality holds.

For \(x\in C\), let \(u_x,v_x\in[H]\) be its capped consecutive
left and right positive-run extents through the cut.  Then

\[
 \boxed{
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.}
 \tag{2.1}
\]

### Lemma 2.1 (southwest exclusion)

If \(P_{s,t}\) is floor-correct, there is no \(x\in C\) with

\[
 u_x<s,
 \qquad v_x<t.
\]

#### Proof

List the \(s+t\) owners in the query window.  Map every initial
coordinate absent from the full intersection to its first departure
transition.  This map is injective because one Johnson transition removes
only one coordinate.

If \(u_x<s\) and \(v_x<t\), then \(x\) has an internal arrival before a
later internal departure.  That later departure cannot be the first
departure of an initial coordinate: either \(x\) was not initial, or it
already departed before its displayed arrival.  Hence at most
\(s+t-2\) transitions lie in the first-departure image, and

\[
 |P_{s,t}|\ge(m+1)-(s+t-2)=m+3-s-t,
\]

contrary to floor correctness. \(\square\)

Take the Pareto-minimal points among

\[
 \{(u_x,v_x):x\in C\}\subseteq[H]^2
\]

and join them, in increasing first and decreasing second coordinate, by a
southeast unit lattice path \(\Gamma\) from \((1,H)\) to \((H,1)\).
Move east before south between consecutive minima.  Then

\[
 |V(\Gamma)|=2H-1.
\]

The southwest exclusion implies the rectangle-interception property:
whenever \(p_x\ge q=(s,t)\) and \(q\) is floor-correct, some

\[
 z\in V(\Gamma)
\]

satisfies \(q\le z\le p_x\).  Emit the actual set-letter

\[
 L_z=P_z
\]

at every staircase vertex.  Then

\[
 \boxed{
 P_q=igcup_{\substack{z\in V(\Gamma)\\z\ge q}}L_z.}
 \tag{2.2}
\]

Along \(\Gamma\), the condition on the first coordinate is a suffix and
the condition on the second is a prefix, so the letters in (2.2) form one
contiguous subword.  Also

\[
 |L_z|\ge m+2-2H\ge1,
\]

so every letter is legal and nonzero.

The second block

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}
\]

has length \(2H\) and realizes every crossing upper union through depth
\(H\).  Concatenating the two blocks gives length

\[
 (2H-1)+2H=4H-1.
\]

This construction is literal, integral, and uses no zero-winding,
FIFO/LIFO, or common-owner hypothesis.  It is a direct counterexample to
every universal \(\Omega(H^2)\) one-cut lower bound.

## 3. The sharp local order is linear

Let \(T_1,\ldots,T_s\) be distinct equal-rank targets represented by a
word, and choose one witness interval \([a_i,b_i]\) for each target.
Both endpoint maps

\[
 T_i\longmapsto a_i,
 \qquad
 T_i\longmapsto b_i
\]

are injective.  Indeed, two intervals with one common endpoint are nested,
so their ORs are comparable; distinct equal-rank sets are incomparable.
Therefore every such word has at least \(s\) positions.

Call a cut strongly clean through depth \(H\) when all arrival and
departure labels on its two radius-\(H\) arms are pairwise distinct.  At
such a cut, all \(q\) crossing windows of one sign and one depth \(q\)
have distinct correct-rank target values.  Taking
\(q\asymp H\) gives an \(\Omega(H)\) lower bound.  Together with the
\(4H-1\) construction, the worst-case one-cut order is

\[
 \boxed{\Theta(H).}
\]

No endpoint or raw interval-counting argument can restore a quadratic
local obstruction.

## 4. Exact support/multiplicity obstruction across cuts

Let \(J\) cuts be selected.  For depth \(q\) and sign \(\sigma\), let
\(R_q^\sigma\) be the multiset of crossing requests, and define

\[
 \kappa_q^\sigma
 =\max_T\#\{R\in R_q^\sigma:R\text{ has target value }T\}.
\]

### Theorem 4.1 (standalone cross-cut throughput)

Every standalone literal word realizing every requested target satisfies

\[
 \boxed{
 n\ge
 \max_{q,\sigma}|\operatorname{supp}R_q^\sigma|
 \ge
 \max_{q,\sigma}{|R_q^\sigma|\over\kappa_q^\sigma}.}
 \tag{4.1}
\]

#### Proof

For fixed \(q,\sigma\), the distinct target values have one common rank.
The endpoint injection above gives the first inequality.  The second is
the elementary support-versus-maximum-multiplicity bound. \(\square\)

Thus, if \(q\ge\alpha H\), all \(J\) cuts are strong at that depth, and
\(\kappa_q^\sigma\le K\), then

\[
 n\ge {\alpha HJ\over K}.
 \tag{4.2}
\]

This is the exact obstruction to a separate \(o(HJ)\) chart.  It has two
and only two support-level escapes:

1. many requests have the same target value, so \(K\to\infty\); or
2. most request values already have intact witnesses away from the cuts
   and need not be serviced by the fusion word.

The universal OR problem asks for one witness per target value, not one
witness per occurrence.  Any global lower bound which counts all destroyed
occurrences without quotienting by target support overcounts the actual
obligation.

### Append-only chain-width form

Let \(B\) be a fixed base word and append a block \(C\) of length \(R\).
Let \(\mathcal M\) be a family of targets represented by \(B|C\) but not
by \(B\).  Choose for every target a witness meeting \(C\), and assign it
to its right endpoint in \(C\).  Targets assigned to one endpoint form an
inclusion chain.  Therefore

\[
 \boxed{R\ge\operatorname{width}(\mathcal M).}
 \tag{4.3}
\]

In particular, for every rank \(r_0\),

\[
 R\ge|\mathcal M\cap\tbinom{\Omega}{r_0}|.
\]

So an append-only fusion needs an \(o(W)\)-chain cover of the genuinely
missing target support.  Rewriting or recoding baseline positions is the
only way around an \(\Omega(W)\) appendage-width obstruction.

### Near-width containment Hall condition

There is a sharper necessary condition for an in-place near-width word.
Let the final word have length

\[
 n=W+d,
\]

and choose witnesses for every target in one middle layer
\(\mathcal C\), where \(|\mathcal C|=W\).  Their left endpoints are
distinct and therefore occupy exactly \(W\) positions.  Let
\(\mathcal E\) be any distinct equal-rank family, and join
\(T\in\mathcal E\) to \(S\in\mathcal C\) when they are comparable in
the forced rank direction: \(T\subset S\) for a lower family and
\(S\subset T\) for an upper family.

For every \(X\subseteq\mathcal E\),

\[
 \boxed{|X|-|N_{\mathcal C}(X)|\le d.}
 \tag{4.4}
\]

Indeed at most \(d\) left endpoints used by \(X\) lie outside the
\(W\) middle endpoints.  Every remaining endpoint coincides with the
endpoint of a unique middle target.  The two witness intervals are nested,
so their OR targets are comparable and give distinct neighbors of \(X\).
The identical inequality holds for right endpoints.

Thus coefficient one forces left and right containment matchings with
only \(o(W)\) Hall deficiency.  If two middle layers of size \(W\) are
both represented in a word of length \(W+d\), their two left-endpoint sets
intersect in at least \(W-d\) positions, as do their right-endpoint sets.
The two intersections themselves meet in at least

\[
 2(W-d)-(W+d)=W-3d
\]

positions.  Hence \(d=o(W)\) forces a common-row endpoint skeleton on
\(W-o(W)\) positions.  Local seam charts must be recoded onto that
skeleton; merely concatenating them cannot meet the necessary Hall
geometry.

## 5. Endpoint order cannot give a superlinear bound

The canonical PBBS already has a common cut crossed by three short
residences whose insertion order is

\[
 x_4,x_1,x_6
\]

and whose removal order is

\[
 x_1,x_4,x_6.
\]

Thus the endpoint permutation is \(213\), neither FIFO nor LIFO.  This
invalidates a monotone-stack or monotone-queue seam proof, but it supplies
no superlinear lower bound.

Indeed every permutation \(\pi\in S_t\) has a common-portal interval
diagram in \(2t\) event positions:

\[
 I_i=[i,t+\operatorname{rank}_\pi(i)]
 \qquad(1\le i\le t).
\]

Insertion order is \(1,\ldots,t\), removal order is \(\pi\), and every
interval crosses the portal between \(t\) and \(t+1\).  Hence inversion
count, FIFO failure, or LIFO failure alone cannot imply
\(\Omega(t^2)\) literal length.

Likewise, a singleton sweep through the active labels overwrites their
last-occurrence order in \(t\) steps.  Such a sweep is only a terminal
state reset: windows crossing it are contaminated.  The true difficulty is
simultaneously preserving proper-target service while matching the common
state, not sorting the endpoint permutation.

## 6. A second necessary condition: harmonic pin sharing

Suppose \(r\) support-essential seam occurrences each require a strict
target tower

\[
 T_{i,0}\subsetneq T_{i,1}\subsetneq\cdots
 \subsetneq T_{i,D}=U_i.
\]

Choose

\[
 \xi_{i,0}\in T_{i,0},
 \qquad
 \xi_{i,p}\in T_{i,p}\setminus T_{i,p-1}
 \quad(1\le p\le D),
\]

and put

\[
 d_{i,p}=\#\{j:\xi_{i,p}\in U_j\}.
\]

### Theorem 6.1 (harmonic pin lower bound)

Every literal word realizing the towers satisfies

\[
 \boxed{
 n\ge\sum_{i=1}^r\sum_{p=0}^{D}{1\over d_{i,p}}
 \ge {r(D+1)\over\Delta_{\rm inc}},}
 \tag{6.1}
\]

where \(\Delta_{\rm inc}=\max_{i,p}d_{i,p}\).

#### Proof

Assign each pin request to one position of its target witness whose letter
contains that pin.  Two requests from one strict tower cannot use one
position: a later increment pin is absent from the earlier target.

Suppose one position serves \(s\) requests.  Its letter contains all their
pin coordinates and is contained in every corresponding witness target.
Consequently every served pin lies in all \(s\) corresponding outer
targets, and its degree is at least \(s\).  The reciprocal loads assigned
to that position sum to at most \(s(1/s)=1\).  Summing over positions gives
the first inequality; the second follows from
\(d_{i,p}\le\Delta_{\rm inc}\). \(\square\)

For \(D=\Theta(H)\), an \(O(r)\)-length in-place fusion therefore requires
\(\Theta(H)\)-way compatible pin sharing.  A bounded-degree or private-pin
packet costs \(\Omega(rH)\), even with arbitrary witness intervals.

This is a necessary theorem, not yet a PBBS lower bound: the known
private-chain packets have not been embedded as actual selected PBBS
occurrences.  A valid PBBS no-go would have to prove bounded pin degree for
the actual support-essential packet, which is currently unavailable.

## 7. Weakest surviving fusion theorem

The preceding results leave one quantitatively minimal positive target.

> **Baseline-relative common-row fusion — open.**  Let \(\ell\) be the
> total length of the original selected PBBS owner/erosion baseline and let
> \(J\) be the critical cuts.  After deleting every crossing occurrence
> whose literal target already has an intact witness, construct one global
> word of length
> \[
>  \ell+o(HJ)
> \]
> by reusing or recoding the \(\ell\) baseline positions and inserting only
> \(o(HJ)\) new positions.  Match the remaining target support to baseline
> endpoints so that targets sharing an endpoint across depths form nested
> flags.  Bundle strict tower pins with harmonic common-target degree
> \(\Omega(H)\), and realize all bundles by one Safe-Pin interval system:
> every witness letter is contained in its target and every target
> coordinate occurs in its witness.  The same word must retain all internal
> targets; if an MTF implementation is used, its protected history and
> entrance/exit states must also agree.

This statement is not contradicted by endpoint throughput: in the critical
regime \(\ell=\Theta(HJ)\), the necessary endpoints are already present.
It is strictly weaker than appending one local chart per cut, preserving
every destroyed occurrence, demanding FIFO/LIFO order, or adding an
independent seam block of length \(o(HJ)\).

The remaining mathematical gate is therefore a simultaneous

\[
 \boxed{
 \text{support selection}
 +\text{baseline endpoint matching}
 +\text{high-degree pin bundling}
 +\text{Safe-Pin chronology}.}
\]

No \(\Omega(H^2)\)-per-cut theorem survives, and no coefficient-one
conclusion follows here.

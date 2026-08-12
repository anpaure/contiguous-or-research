# Coordinatewise Catalan run pressure and the exact all-depth connector transducer

Date: 2026-07-31  
Status: proved all-\(m\) identities and exact finite characterizations;
independently audited finite calibration; no uniform rethread or
coefficient-one conclusion

## 0. Verdict

The Catalan seam ledger has a stronger coordinatewise form than its global
average.  If \(K=\operatorname {Cat}_m\) path components are joined
cyclically and \(s_x\) selected seams contain coordinate \(x\) on both
ends, then coordinate \(x\) has exactly \(K-s_x\) cyclic positive runs and
total positive mass \((m+1)K/2\).  At residence floor \(h\), its excess
over long runs minus its deficit under short runs is exactly

\[
 E_x^{(h)}-D_x^{(h)}
   ={m+1\over2}K-h(K-s_x).                         \tag{0.1}
\]

Thus the average-length theorem is not merely asymptotic: the complete
scalar obstruction is an explicit seam-quota inequality for each
coordinate.  These inequalities are necessary but not sufficient.  They do
not place the surplus beside the deficient collars.

There is also an exact nonprobabilistic formulation of the missing
redistribution.  A changed set of immediate-colour rows supports another
perfect diamond matching exactly when a derangement Hall condition holds.
In fact, for every \(m\ge2\), changing **all** rows is always possible:
removing the source matching leaves a positive regular bipartite graph.
Thus immediate-palette restitution and inherited-collar hitting are not the
uniform obstruction.
Physical residence additionally requires a cap-two acyclic Johnson lift
which avoids every forbidden short-run collar.  Endpoint joining and all
deeper shadows are then exactly one finite word transducer: it remembers the
coordinate run automata, the last \(m\) middle masks, and the uncovered
target set while components are ordered and oriented.

At \(m=5\), the authenticated item 2188 matching passes the central
derangement, cap-two, graphic, and forbidden-collar rows, so interior
residence is genuinely attainable.  Its fixed 42 path bodies nevertheless
have a separate two-dead-socket obstruction: no endpoint-only joining can
be depth-two resident.  Hence the correct uniform target is a joint
interior-rethread plus all-depth connector packet, not a scalar run-balancing
lemma and not a whole-path permutation theorem.

## 1. Catalan linear matching notation

Put

\[
 M={2m\choose m},\qquad N={2m\choose {m-1}},\qquad
 K=M-N=\operatorname {Cat}_m.                       \tag{1.1}
\]

Let \(F\) be a spanning path forest in \(J(2m,m)\) with \(N\) edges such
that its rank-\((m-1)\) intersection colours and rank-\((m+1)\) union
colours are each used exactly once.  Then \(F\) has \(K\) components.

For coordinate \(x\), write

\[
 n_x=\#\{A\in {[2m]\choose m}:x\in A\}
     ={2m-1\choose {m-1}}={m+1\over2}K.             \tag{1.2}
\]

The induced forest on vertices containing \(x\) has

\[
 {2m-1\choose {m-1}}-{2m-1\choose {m-2}}=K          \tag{1.3}
\]

components.  These are precisely the positive \(x\)-runs in the unjoined
path forest.

## 2. Exact coordinatewise redistribution identities

### Theorem 2.1 (cyclic coordinate identity)

Join the \(K\) components by \(K\) Johnson seams into one cyclic chronology.
For coordinate \(x\), let \(s_x\) be the number of selected seams whose
common rank-\((m-1)\) intersection contains \(x\).  Then

\[
 r_x=K-s_x,\qquad \sum_xs_x=(m-1)K,                 \tag{2.1}
\]

where \(r_x\) is the number of cyclic positive \(x\)-runs.

For a threshold \(h\ge1\), let their lengths be
\(\ell_{x,1},\ldots,\ell_{x,r_x}\) and put

\[
 D_x^{(h)}=\sum_i(h-\ell_{x,i})_+,\qquad
 E_x^{(h)}=\sum_i(\ell_{x,i}-h)_+.                  \tag{2.2}
\]

Then

\[
 \boxed{\;
 E_x^{(h)}-D_x^{(h)}
 =n_x-h(K-s_x)
 ={m+1\over2}K-h(K-s_x).\;}                         \tag{2.3}
\]

Consequently, a cyclic \(h\)-resident chronology necessarily satisfies

\[
 \boxed{\;
 s_x\ge K-\left\lfloor {n_x\over h}\right\rfloor
 =K-\left\lfloor{(m+1)K\over2h}\right\rfloor
 \quad\hbox{for every }x.\;}                        \tag{2.4}
\]

Summing (2.3) gives the exact global pressure

\[
 \boxed{\;
 \sum_x(E_x^{(h)}-D_x^{(h)})
 =(m+1)K(m-h).\;}                                   \tag{2.5}
\]

#### Proof

Before joining, coordinate \(x\) has \(K\) runs by (1.3).  A seam merges
two \(x\)-runs exactly when both endpoints contain \(x\), equivalently when
its intersection colour contains \(x\).  This proves \(r_x=K-s_x\).
Every seam intersection has size \(m-1\), proving the sum in (2.1).

For every positive integer \(\ell\),

\[
 (\ell-h)_+-(h-\ell)_+=\ell-h.
\]

Sum this identity over the \(r_x\) runs and use (1.2), proving (2.3).
If every run has length at least \(h\), then
\(K-s_x=r_x\le\lfloor n_x/h\rfloor\), which is (2.4).
Finally sum (2.3), use
\(\sum_xn_x=2mn_x=m(m+1)K\), and use
\(\sum_x(K-s_x)=(m+1)K\). \(\square\)

### Theorem 2.2 (linear endpoint correction)

Join the \(K\) components by \(K-1\) seams into a Hamilton path.  Let \(s_x\)
again count seams common to coordinate \(x\), and put

\[
 b_x=\mathbf1_{\{x\in A_{\rm first}\}}+
     \mathbf1_{\{x\in A_{\rm last}\}}.              \tag{2.6}
\]

If every internally bounded positive \(x\)-run has length at least \(h\),
then

\[
 \boxed{\;
 s_x\ge K-b_x-\left\lfloor{n_x-b_x\over h}\right\rfloor.
 \;}                                                \tag{2.7}
\]

#### Proof

The path has \(K-s_x\) positive \(x\)-runs.  Exactly \(b_x\) of them meet a
word boundary.  When \(b_x=2\), those two runs are distinct because a
Hamilton path contains middle sets omitting \(x\).  The boundary arms have
length at least one and the other \(K-s_x-b_x\) runs have length at least
\(h\).  Hence

\[
 n_x\ge h(K-s_x-b_x)+b_x,
\]

which is equivalent to (2.7). \(\square\)

Neither (2.4) nor (2.7) is sufficient.  Even with the same mass and run
count, replacing run lengths \((h,h)\) by \((1,2h-1)\) preserves both scalar
ledgers and creates a defect.

### Lemma 2.3 (literal merge credit)

If one seam merges positive endpoint runs of lengths \(p,q\), its reduction
of threshold-\(h\) deficit is

\[
 \gamma_h(p,q)
 =(h-p)_++(h-q)_+-(h-p-q)_+,\qquad 0\le\gamma_h(p,q)\le h. \tag{2.8}
\]

This identity is local and exact.  It does not assert that seams with the
desired credits can be selected compatibly.

## 3. The exact palette exchange row

Let

\[
 {\cal L}={[2m]\choose {m-1}},\qquad
 {\cal U}={[2m]\choose {m+1}},
\]

and let \(\mu_0:{\cal L}\to{\cal U}\) be the source perfect matching in the
diamond inclusion graph.  Index \(U_i=\mu_0(L_i)\).  For
\(S\subseteq{\cal L}\), form the bipartite graph \(B_S^\ast\) on two copies
of \(S\), with the nonloop edge

\[
 i_{\rm L}j_{\rm R}\in E(B_S^\ast)
 \quad\Longleftrightarrow\quad i\ne j\ \hbox{ and }\ L_i\subset U_j. \tag{3.1}
\]

### Theorem 3.1 (changed-support Hall theorem)

There is another perfect diamond matching whose set of changed source rows
is exactly \(S\) if and only if

\[
 \boxed{\quad |N_{B_S^\ast}(T)|\ge |T|
 \quad\hbox{for every }T\subseteq S.\quad}           \tag{3.2}
\]

#### Proof

Every new perfect matching has a unique representation
\(\mu(L_i)=U_{\pi(i)}\) for a permutation \(\pi\).  If its changed support
is \(S\), then \(\pi\) fixes the complement, maps \(S\) to itself, has no
fixed point on \(S\), and uses only inclusion arcs (3.1).  Thus its
restriction is a perfect matching of \(B_S^\ast\).

Conversely, a perfect matching of \(B_S^\ast\), extended by the identity
outside \(S\), is a permitted permutation with changed support exactly
\(S\).  Hall's theorem gives (3.2). \(\square\)

The symmetric difference with \(\mu_0\) is therefore a disjoint union of
alternating diamond circuits.  The theorem is only the immediate-palette
row: it contains no cap-two, forest, residence, deep-shadow, or compiler
conclusion.

### Theorem 3.2 (unconditional full-support palette rethread)

For every \(m\ge2\), there is a perfect diamond matching which changes
**every** row of any prescribed source perfect matching.

#### Proof

Each lower row \(L_i\) is contained in exactly

\[
 D={m+1\choose2}
\]

rank-\((m+1)\) columns, and each upper column contains exactly \(D\) lower
rows.  The source matching is one incident edge at every row and column.
Deleting all of those diagonal edges leaves the full nonloop exchange graph,
which is balanced and \((D-1)\)-regular.  Since \(D-1>0\) for \(m\ge2\),
regular bipartite Hall gives a perfect matching.  It uses no source edge and
therefore changes every row. \(\square\)

Consequently the unrestricted immediate-palette space has no singleton
locked row and no inherited collar which cannot be hit: the all-row
derangement destroys every literal old collar simultaneously.  This is a
genuine all-\(m\) palette-level existence theorem, but it gives no cap-two,
graphic, or new-collar guarantee.  The unique small exception is \(m=1\),
where \(D-1=0\).

## 4. Exact short-run collar constraints

An old internal positive run of coordinate \(x\), of length
\(1\le\ell<h\), has a collar consisting of the \(\ell+1\) consecutive
Johnson edges from the preceding zero through the run to the following
zero.  Identify those edges by their distinct lower colours, and let
\({\cal I}_h(F)\) be the resulting interval family.

### Proposition 4.1 (old-collar hitting)

If a changed-support set \(S\) yields an internally \(h\)-resident rethread,
then

\[
 S\cap I\ne\varnothing\qquad(I\in{\cal I}_h(F)).     \tag{4.1}
\]

Conversely, (4.1) destroys every literal old short-run occurrence, although
it may create new ones.

Since these collars are intervals on the source paths, their unrestricted
transversal number is the sum of the greedy interval-stabbing numbers on
the individual paths.  If \(R_h\) old defects are present, then

\[
 |S|\ge\tau({\cal I}_h(F))
       \ge\left\lceil{R_h\over m+1}\right\rceil,      \tag{4.2}
\]

because one Johnson edge lies in collars for at most the \(m+1\)
coordinates in the union of its endpoints.

Every changed row belongs to a nontrivial directed cycle in the exchange
digraph \(i\to j\iff L_i\subset U_j\).  Hence a collar disjoint from the
directed cyclic core is an obstruction in a **restricted** exchange
catalogue.  In the complete diamond graph with \(m\ge2\), Theorem 3.2 shows
that the nonloop core covers every row, so this particular palette
obstruction vanishes.

### Theorem 4.2 (exact physical residence row)

For \(1\le\ell<h\), let a forbidden \(h\)-collar be the \(\ell+1\)
diamond edges of a simple Johnson path

\[
 X_0,X_1,\ldots,X_{\ell+1}
\]

for which some coordinate \(x\) is absent from \(X_0,X_{\ell+1}\) and
present in \(X_1,\ldots,X_\ell\).  Call the family of all such edge sets
\({\cal C}_h\).

This is a family in the **final lifted Johnson graph**.  A forbidden path may
use any mixture of retained and inserted edges and may cross several old
component boundaries.  It is not enough to inspect each inserted seam in
isolation.

A perfect diamond matching lifts to an internally \(h\)-resident Catalan
path forest if and only if

1. the lifted Johnson graph has maximum degree at most two;
2. it is acyclic; and
3. it contains no member of \({\cal C}_h\) in full.

#### Proof

The first two rows make the \(N\)-edge spanning lift a union of paths.
Every internally bounded positive run of length \(\ell<h\) supplies exactly
one member of \({\cal C}_h\).  Conversely, under maximum degree two and
acyclicity, all edges of a member of \({\cal C}_h\) occur consecutively in
one path component and display precisely the forbidden bounded run.
\(\square\)

Thus central run redistribution is exactly the intersection of:

* the derangement Hall row (3.2);
* the cap-two row;
* the graphic row; and
* the forbidden-collar row.

The stable-cube \(D_4\) obstruction is not removed merely by Hall or by the
large scalar pressure (2.5).

## 5. Exact endpoint joining and all-depth support

Let \(P_1,\ldots,P_K\) be the path components of a fixed internally
\(h\)-resident Catalan forest.  Suppose internal windows already cover all
immediate colours.  For depth \(q\), a window is \(q+1\) consecutive middle
sets; its lower and upper labels are respectively their intersection and
union.  Let \({\cal D}_q^-,{\cal D}_q^+\) be the lower and upper targets
not witnessed inside one component.

### Theorem 5.1 (literal connector criterion)

The components admit a linear all-depth \(h\)-resident Hamilton chronology
if and only if one can choose an order and orientation of all components
such that:

1. consecutive endpoint masks are Johnson adjacent;
2. the concatenated coordinate traces have no internally bounded positive
   run of length below \(h\); and
3. every target in every \({\cal D}_q^-\cup{\cal D}_q^+\) is the
   intersection or union of a nonwrapping \(q+1\)-window in the
   concatenation.

All internally witnessed targets survive literally.  The same physical
order must satisfy all three rows; independent rankwise choices are not
allowed.

#### Proof

Necessity is the definition of a Johnson Hamilton chronology, internal
residence, and all-depth coverage.  Conversely, row 1 concatenates the
disjoint spanning components to one Johnson Hamilton path.  Row 2 is the
literal residence test.  Row 3 supplies every target absent from component
interiors, while all other witnesses are unchanged. \(\square\)

### Theorem 5.2 (exact finite transducer)

The criterion in Theorem 5.1 is recognized exactly by the following
component-order state:

1. the used-component set, the current endpoint, and the chosen
   orientations;
2. for each coordinate, the finite positive-run automaton which
   distinguishes the initial boundary arm, stores the current positive
   suffix length capped at \(h\), records the all-one/whole-fragment case,
   and rejects only when a newly internal run closes below \(h\);
3. the last \(m\) middle masks; and
4. the still-uncovered labelled banks
   \(({\cal D}_q^-,{\cal D}_q^+)_{1\le q\le m}\).

When a new middle mask is appended, every newly completed window of every
depth is computed from the tail in item 3 and removed from the appropriate
debt bank.  Acceptance means that all components are used, the run
automata accept with trailing boundary arms left open, and every debt bank
is empty.

This transducer is necessary and sufficient, not a claim of polynomial
size.  In particular, a window may cross several seams through a short
component, so a one-seam provider graph is only a sufficient submodel.

For a cyclic construction with a final cut, mark the cut before scanning.
Deleting one cyclic seam removes exactly \(q\) cyclic windows of length
\(q+1\) at depth \(q\).  The cut may also turn one short cyclic run into
two legal boundary arms.  More explicitly, an opening of type \(11\) splits
one cyclic positive run into two exempt boundary arms, a \(10\) or \(01\)
opening exposes one boundary arm, and a \(00\) opening exposes none.
Therefore cyclic residence or cyclic flag
coverage cannot be transferred to a linear word without this marked-cut
replay.

### Corollary 5.3 (pairwise safe-port face)

If every component has at least \(h\) vertices and is internally
\(h\)-resident, a newly forbidden short run cannot cross two seams.  For a
seam \(P\to Q\), let \(\operatorname{suf}_x(P)\) and
\(\operatorname{pre}_x(Q)\) be the positive endpoint-run lengths, with
value zero when the endpoint omits \(x\).  The proposed complete order is
resident exactly when every selected seam is Johnson and

\[
 \operatorname{suf}_x(P)+\operatorname{pre}_x(Q)
 \in\{0\}\cup[h,\infty)
 \qquad\hbox{for every }x.                          \tag{5.1}
\]

For fixed orientations, a cycle cover on these safe arcs is governed by
ordinary bipartite Hall.  It is one chronology only when its successor
permutation is one cycle.  If two arcs in different cycles can be replaced
by the two cross arcs and both cross arcs satisfy (5.1), the usual
two-switch merges those cycles while retaining residence.

Components shorter than \(h\), or an all-one coordinate trace through a
short component, require the full automaton of Theorem 5.2.  Pairwise
seam safety is then not sufficient: at \(h=3\), the fragments
\((0,1)\mid(1)\mid(0)\) have no defect detectable from either seam as an
isolated two-fragment operation, but their composition is \(0,1,1,0\).

## 6. Exact \(m=5\) calibration

The item 2188 certificate has \(M=252,N=210,K=42,h=3\).  Independent replay
gives:

* both immediate palettes exactly once;
* 210 lifted edges on 252 vertices and 42 path components;
* internal positive-run histogram
  \(3^{42}4^7 5^3 6^4 7^8 9\);
* 119 changed matching partners, whose matching symmetric difference has
  alternating half-length histogram
  \(2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1\); and
* exactly 21 internal deeper debts:

\[
\begin{array}{c|l|l}
q&{\cal D}_q^-&{\cal D}_q^+\\ \hline
2&38,41,50,73,400,704&
487,502,575,699,862,885,949,973,979,1009\\
3&66,72&495,703\\
4&\varnothing&1007\\
5&\varnothing&\varnothing.
\end{array}                                         \tag{6.1}
\]

The final matching is the theorem.  Its alternating decomposition does not
certify a physical forest or fixed decoration at every intermediate
circuit toggle.

A lightweight endpoint census independently gives 84 occurrence ports,
304 formal Johnson endpoint pairs, 293 distinct physical pairs, port
degrees from 4 to 11, 608 directed Johnson arcs, and 114 directed arcs
passing the strong one-seam test (5.1).  Sixteen path bodies have no
orientation with both a safe incoming and a safe outgoing arc; hence this
pairwise-safe submodel cannot span all 42 bodies.  Among its safe arcs, 56
serve at least one debt in (6.1), while the four debts

\[
 (2,-,50),\quad(2,-,73),\quad(2,+,502),\quad(2,+,885) \tag{6.2}
\]

have no one-seam provider.  This is not a connector no-go because the exact
transducer permits multi-seam windows and boundary absorption.

The stronger item 2190 audit does give a fixed-face no-go.  Both endpoints
of one specific path body have degree zero even under the necessary local
pair-safe filter.  Every connected
endpoint closure creates two edge-disjoint short-run collars, while the
unique overlap choice isolates a two-component cycle.  One opening can
destroy at most one collar.  Therefore no endpoint-only joining of the
fixed item 2188 path bodies is depth-two resident, even before the 21 debts
or compiler are imposed.

For each coordinate the 42 unjoined runs have total mass 126.  At \(h=3\),
(2.3) gives zero net pressure.  Their exact deficit/excess pairs are

\[
 (25,25),(26,26),(26,26),(21,21),(28,28),
 (27,27),(29,29),(29,29),(29,29),(20,20).           \tag{6.3}
\]

This is a literal illustration of the theorem: scalar mass is perfectly
balanced while the usable socket distribution fails.

## 7. Controlled-debt integration

A recursive repair state which can represent this rethread and its later
connectors must carry the product

\[
\begin{split}
(&\hbox{immediate palette/occurrence debt and pairing-resolved linkage},\\
 &\hbox{physical path pairing and ports},\
   \hbox{Pascal residual reachability},\\
 &\hbox{coordinate run automata},\
   \hbox{last-\(m\) owner tail and all-depth debt},\\
 &\hbox{current decoration/gap state and transition debt},\
   \hbox{compiler/common-\(Q\) state}).              \tag{7.1}
\end{split}
\]

Every entry refers to the same physical bundles.  Immediate-palette-neutral
interior rethreads are legitimate transitions, so a progress measure based
only on palette holes is invalid.  A fail-closed transition graph may
instead use an exact finite acyclic used-resource or stage coordinate; every
transition must service a declared debt or advance that coordinate.

For Pascal delete-first insertion \(T\to H\), the reachability row remains
independent and exact: the residual directed graph must be acyclic and have
no path \(H\leadsto T\).  The common-\(Q\) compiler is a terminal matching
predicate on the same chronology, not a rankwise afterthought.

## 8. Sharp remaining all-\(m\) theorem

The following is now the minimal positive supply statement sufficient for
this lane:

> For the required residence floor \(h=d+1\), construct a q1-exact perfect
> diamond rethread whose lift is a cap-two acyclic forest avoiding every
> forbidden \(h\)-collar, together with an ordered bounded-adhesion interior
> actuator and Johnson connector decomposition accepted by the exact run
> and all-depth transducer, carrying the decoration transition and Pascal
> reachability debt and ending with one exact exported decoration; the later
> transparent gluing list preserves that terminal decoration.  Then prove
> the maximal-envelope common-\(Q\) compiler matching for that same physical
> chronology.

Equivalently, one may supply a bounded-treewidth interaction graph whose
bags carry the product state (7.1).  Packet cardinality may grow; bounded
live interface, not bounded switch count, is the recursive invariant.

What is proved here is the exact coordinate pressure, the exact palette
support criterion, the exact physical collar criterion, and the exact
connector automaton.  What is not proved is the uniform existence of the
required rethread/connector bank, a bound on its footprint, a Pascal
preservation theorem for it, a common-\(Q\) compiler theorem, or
\(\nu(k)=B(k)\) for all \(k\).

## 9. Reproduction and authoritative dependencies

The m5 endpoint census is reproduced by

~~~text
python3 scratch/audit_r_m5_residence_connector_local_census_20260731.py
~~~

The exact matching and the fixed-socket no-go are independently replayed by

~~~text
python3 scratch/audit_catalan_m5_residence_rethread_c4c6_20260731.py
python3 scratch/audit_catalan_m5_residence_clean_socket_dead_component_h2_20260731.py
~~~

This theorem uses the exact scopes of:

* MATH_THEOREM_CATALAN_SEAM_RUN_COUNT_AND_RESIDENCE_MARGIN_20260731.md;
* MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md;
* MATH_THEOREM_CATALAN_INTERIOR_RETHREAD_GAIN_BRAUER_ACTUATOR_20260731.md;
* MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_SOCKET_DEAD_COMPONENT_NOGO_20260731.md;
* MATH_THEOREM_R_TURN_DEFECT_TRANSPORT_HALL_RELAY_LINKAGE_20260731.md.

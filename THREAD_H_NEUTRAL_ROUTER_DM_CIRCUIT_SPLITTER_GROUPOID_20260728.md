# Neutral legality routers and DM-circuit splitters at Hall 23

## 1. Result and exact boundary

The verified Hall-23 carrier admits the exact compound descent

\[
H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23
\xrightarrow{\operatorname{FR}(740,4051,6137)}H22.                 \tag{1.1}
\]

The first braid is a rank-neutral legality router.  It rotates a Boolean
packet in the large DM component rooted at `24610`, but it does not alter the
component-restricted incidence of the small DM circuit

\[
C=\{4877,4909\}.
\]

The second braid leaves the `24610` packet unchanged and replaces the one
restricted cell shore \(\{4877,4909\}\) by the two restricted singleton
shores \(\{4877\}\) and \(\{4909\}\).  Thus it raises the restricted rank of
\(C\) from one to two and removes precisely this component from the canonical
DM shore.

This proves an outer-Hall neutral-router/circuit-splitter descent, its literal
common-word lift on the critical DM shore, and a general transversal-circuit
splitting lemma.  The fully lifted router theorem in Section 5 is conditional:
one common-word lift of the complete maximum matching is not yet known.  Nor
does the example prove that one neutral braid group routes one universal
splitter to every remaining component.  Decorated legal transitions form a
state-dependent directed category; only its reversibly certified part is a
groupoid.  One projection of their common-word data obeys an exact cocycle
identity.  The exact remaining assertion is an orbit-hitting statement in
this lifted transition category.

The construction still does not prove a length-6438 word.  Hall deficiency is
22 and the main branch has seven target vertices of degree zero.  A separate
audited Pareto branch in Section 10 keeps Hall 22 and reduces this count to
six.  No simultaneous common-word lift of a full 16361-edge maximum compiler
matching is known.

## 2. Compiler circuits and physical states

For a certified carrier state \(z\), let

\[
G_z=(L,R_z;E_z)
\]

be its lower-target/physical-cell incidence graph and put

\[
h(z)=|L|-\nu(G_z).
\]

A *certified physical state* includes the carrier, its maximal erosion word,
the exact middle deck, Johnson chronology, depth-three residence, the
protected lower/upper support ledgers, and whatever target/cell matching has
been lifted to one common physical word.  Keeping only the carrier and the
scalar matching number is insufficient.

An induced bipartite component \(D=(X,Y)\) is an *excess-one transversal
circuit* when

\[
|X|=|Y|+1,
\qquad
X-\{x\}\text{ is matchable into }Y\quad(x\in X).                  \tag{2.1}
\]

Equivalently, every target of \(X\) can be the exposed target of a matching
saturating \(Y\).  In a canonical DM component of gap one, (2.1) follows by
flipping the alternating path from its unique exposed left root to the chosen
left vertex.

For a physical cell \(c\), its shore restricted to \(X\) is

\[
\Gamma_z(c;X)=N_{G_z}(c)\cap X.                                  \tag{2.2}
\]

All splitter statements below concern these restricted shores.  A physical
cell may have additional neighbours outside \(X\).

## 3. Every nontrivial excess-one circuit has an abstract one-cell split

### Theorem 3.1 (transversal circuit splitting)

Let \(D=(X,Y)\) satisfy (2.1), with \(Y\ne\varnothing\).  Choose any
\(y\in Y\) and any \(x\in N_D(y)\).  Then there is a partition

\[
N_D(y)=A\mathbin{\dot\cup}B,\qquad x\in A,\qquad B\ne\varnothing, \tag{3.1}
\]

such that replacing \(y\) by two right vertices with shores \(A,B\) makes
all of \(X\) matchable.

#### Proof

By (2.1), choose a matching \(M\) of \(X-\{x\}\) onto \(Y\).  The vertex
\(y\) is matched by \(M\) to some \(w\ne x\).  In particular
\(w\in N_D(y)-\{x\}\).  Take

\[
A=\{x\},\qquad B=N_D(y)-\{x\}.
\]

Match the first new right vertex to \(x\), the second to \(w\), and retain
all edges of \(M\) except \(wy\).  This matches all of \(X\).  \(\square\)

Thus there is no further abstract matching obstruction inside any nonzero
gap-one DM circuit: some split always perfects it.  What is hard is realizing
the required split by a legal braid while retaining the complement matching,
the shadow ledgers, residence, and one common word.

The hypothesis \(Y\ne\varnothing\) is sharp for this architecture.  A
degree-zero `1/0` component has no cell to split.  It requires a first-cell
creator, not a refinement of an existing shore.

## 4. The correct routing object is a lifted transition category

A legal signed-block braid is state-dependent: its new seams must be Johnson
edges, resident, shadow-safe, and compatible with the current physical pin
system.  Consequently legal neutral braids do not give a state-independent
group action on carriers.  Their decorated lifts give a directed category
whose objects are framed states

\[
\mathfrak X=(T,M,\Phi),                                           \tag{4.1}
\]

where \(T\) is the carrier, \(M\) is the protected matching certificate, and
\(\Phi\) is its simultaneous physical pin lift.  The carrier block
permutation is invertible, but a rerouted matching/pin lift need not have a
certified inverse.  An arrow belongs to the reversible subgroupoid only when
it includes certified transports
\((M,\Phi)\leftrightarrow(M',\Phi')\) in both directions.

The forbidden-set projection of the common-word datum has an exact cocycle
identity.  For a coordinate \(a\), define
the positions forbidden by a pin family \(\Phi\) by

\[
F_a(\Phi)=\bigcup_{(I,S)\in\Phi,\ a\notin S} I.                   \tag{4.2}
\]

Let \(g:\mathfrak X\to\mathfrak Y\) be a signed-block braid.  A lifted
morphism includes a chosen total bijection

\[
\widehat\theta_g:\Omega_{\mathfrak X}\longrightarrow
\Omega_{\mathfrak Y}                                             \tag{4.3}
\]

of the full controller/pin-position sets, agreeing with signed-block
transport away from the seam closure.  This extra datum is necessary because
the clipped controller endpoints and seam columns have no canonical block
transport.  Put

\[
\omega_a(g)=F_a(\Phi_{\mathfrak X})
\mathbin\triangle
\widehat\theta_g^{-1}F_a(\Phi_{\mathfrak Y}).                    \tag{4.4}
\]

For composable \(g,h\), use
\(\widehat\theta_{hg}=\widehat\theta_h\circ\widehat\theta_g\).  Then

\[
\boxed{\omega_a(hg)=
\omega_a(g)\mathbin\triangle
\widehat\theta_g^{-1}\omega_a(h).}                              \tag{4.5}
\]

Indeed, insert the pulled-back intermediate forbidden set into the symmetric
difference in (4.4); the two copies cancel.  Without a total
\(\widehat\theta_g\), the same formula holds on transported interiors and
the seam package is an additional defect.  Therefore two routes reaching
the same undecorated port frame can have different physical common-word
states.  Port-frame transitivity alone cannot prove routing.  One must retain
the full lifted state.  Since \(\omega_a\) is defined from endpoint data, it
is an exact coboundary for this forbidden-set projection; no nontrivial
holonomy theorem is claimed.

The forbidden sets \(F_a\) are only one projection of common-word data.
Controller availability and the positive-hit family

\[
\mathcal H_a(\Phi)=\{I:(I,S)\in\Phi,\ a\in S\}                  \tag{4.6}
\]

must also be transported.  Vanishing \(\omega_a\) is neither required for a
route which legitimately rethreads its pins nor sufficient for a common-word
lift.  The framed state retains the full controller and pin family; (4.5) is
an exact discrepancy identity inside that larger bundle.

There is a second exact obstruction to a naive conjugation theorem.  Suppose
a router preserves the complete decorated target/cell germ and fixes every
left target mask.  Conjugating a splitter by this router can only modify the
same left component, because the induced compiler-graph isomorphism is the
identity on \(L\).  Segment braids do not relabel coordinates.  Hence a
full-germ-preserving conjugate of the `4877/4909` splitter cannot become a
splitter at root `1920`, `24610`, or a zero target.  A router which does alter
the germ can enable a remote splitter, as (1.1) does, but then matching and
common-word feasibility must be audited anew.

## 5. Router-splitter descent theorem

### Theorem 5.1 (lifted neutral router plus unit splitter)

Let \(z_0\) be a certified state with \(h(z_0)=d\), and let
\(C\) be an excess-one DM circuit.  Suppose:

1. a neutral braid word \(g:z_0\to z_1\) preserves every protected physical
   invariant and transports a common-word maximum-matching certificate of
   size \(|L|-d\), with one exposed target in \(C\);
2. after a legal splitter \(s:z_1\to z_2\), there is a common-word matching
   \(\overline M\subseteq G_{z_2}\) of size \(\nu(G_{z_1})\), obtained after
   rerouting every deleted protected edge, and there is an
   \(\overline M\)-augmenting path which starts at the exposed target in
   \(C\) and ends at an unmatched right cell, such that the augmented
   matching is realized by that same physical word;
3. either \(\nu(G_{z_2})\le\nu(G_{z_1})+1\), or a retained Hall shore of gap
   \(d-1\) gives the same upper bound.

Then

\[
h(z_0)=h(z_1)=d,\qquad h(z_2)=d-1.                              \tag{5.1}
\]

#### Proof

Neutrality gives the first equality.  Flipping the augmenting path in (2)
produces a physically simultaneous matching of size
\(\nu(G_{z_1})+1=|L|-d+1\), so \(h(z_2)\le d-1\).  Hypothesis (3) gives the
reverse inequality.  All deck, chronology, residence, shadow, and literal
pin assertions are part of the certified-arrow hypotheses and hence survive
the composition.  \(\square\)

The theorem also permits a splitter which leaves one common-word matching of
size \(\nu(G_{z_1})-r\) and supplies \(r+1\) pairwise vertex-disjoint
augmenting paths relative to that same matching, provided the simultaneously
augmented matching has one common-word realization.  Applying all paths
raises total rank by one.  The circuit-ear case is \(r=0\).

### Exact Hall-current form

For \(S\subseteq L\), define the initial slack

\[
\sigma_{z_0}(S)=d-\bigl(|S|-|N_{G_{z_0}}(S)|\bigr)\ge0.           \tag{5.2}
\]

For a graph transition \(u\to v\), put

\[
I_{u,v}(S)=|N_{G_v}(S)|-|N_{G_u}(S)|.                            \tag{5.3}
\]

Currents telescope.  Hall's theorem gives the exact identity

\[
h(z_2)=d-\min_{S\subseteq L}
\bigl(\sigma_{z_0}(S)+I_{z_0,z_1}(S)+I_{z_1,z_2}(S)\bigr).       \tag{5.4}
\]

A neutral router only forces the corresponding minimum before the splitter
to be zero; it need not have zero current on each old maximum shore.  This is
why a neutral move in one DM component can be necessary for a later remote
splitter.

## 6. Direct seven-block product-box form of (1.1)

Cut the Hall-23 carrier at

\[
740,3799,4497,5788,6040,6138
\]

into forward blocks \(P_0,\ldots,P_6\), of lengths

\[
740,3059,698,1291,252,98,297.                                   \tag{6.1}
\]

Direct substitution of the two three-cut moves gives the single signed
seven-block braid

\[
\boxed{
P_0P_1P_2P_3P_4P_5P_6
\longmapsto
P_0\overleftarrow{P_3}P_2P_5P_4\overleftarrow{P_1}P_6.}         \tag{6.2}
\]

Write \(L_i,R_i\) for the forward endpoints of \(P_i\).  The old/new
connector symmetric difference is exactly the two alternating cycles

\[
R_0-_{o}L_1-_{n}L_6-_{o}R_5-_{n}L_4-_{o}R_3-_{n}R_0,            \tag{6.3}
\]

\[
R_1-_{o}L_2-_{n}L_3-_{o}R_2-_{n}L_5-_{o}R_4-_{n}R_1.            \tag{6.4}
\]

This follows simply by listing the six new connectors

\[
R_0R_3, L_3L_2, R_2L_5, R_5L_4, R_4R_1, L_1L_6.             \tag{6.5}
\]

More generally, two signed orders of the same blocks with the same actual
exterior ports, including their orientations, have connector symmetric
difference equal to a disjoint union of even alternating cycles: every
internal block endpoint has one old and one new connector.  This is the exact
port-circulation normal form for multiblock fusion.

When every block separating two seams has length at least \(q\), attach to a
directed connector \(e\) its complete oriented depth-\(q\) collar vector
\(\gamma_q(e)\).  Then

\[
\Delta_q=
\sum_{e\in E_{\rm new}}\gamma_q(e)
-\sum_{e\in E_{\rm old}}\gamma_q(e).                            \tag{6.6}
\]

Thus multiplicity-neutral port circulations are precisely those in the
kernel of every protected collar map.  Support preservation is weaker and
must be checked by last-witness inequalities.  In (6.1) the minimum block
length is 98, so the locality hypothesis holds at every audited depth
\(q\le7\).  The **combined direct macro** (6.3)--(6.4) preserves all required
supports; neither individual \(C_6\) is asserted to be support-safe by itself,
and the improving braid is not multiplicity-neutral at every depth.

## 7. Exact `24610` router and remote `4877/4909` splitter

All masks in this section are decimal bit masks and the displayed added bits
are disjoint.  Put \(K=24610\) and

\[
\begin{aligned}
U&=K+\mathcal P(\{1,64\}),\\
V&=(K+4096+\mathcal P(\{1,64\}))\setminus\{K+4096\},\\
W&=\{u+4:u\in U\}.
\end{aligned}                                                     \tag{7.1}
\]

Here \(K+\mathcal P(B)=\{K+s:s\text{ is a subset sum of }B\}\).
On the `24610` component, the neutral braid changes precisely

\[
\{U\cup V,W\}\longrightarrow\{U\cup W,V\}.                     \tag{7.2}
\]

This is a rank-neutral associator.  The improving braid makes no further
restricted-column change on this component.

On \(C=\{4877,4909\}\), the restricted columns are exactly

\[
\{\{4877,4909\}\}
\longrightarrow
\{\{4877,4909\}\}
\longrightarrow
\{\{4877\},\{4909\}\}.                                        \tag{7.3}
\]

The two final cells are literal native traces of the same maximal erosion
word:

\[
\begin{array}{c|c|c|c|c}
\text{cell}&(q,s)&\text{controller states}&\text{mandatory}&\text{trace}\\ \hline
7178&(1,740)&(781,4365)&4612&4877\\
13614&(2,739)&(809,781,4365)&4652&4909.
\end{array}                                                       \tag{7.4}
\]

Their full compiler shores are larger; (7.3) is their exact restriction to
the old two-target component.  The two distinct representatives in (7.4)
prove restricted rank \(1\to2\).

The neutral router preserves the same set of 984 native target labels.  Of
their cell/target pairs, 624 remain identical and 360 are rethreaded.  At
Hall 22, the maximal erosion word simultaneously realizes the 983 native
pins of the residual DM shore and the two pins (7.4).  These are 985 distinct
cell/target pairs on the former 1007-target Hall-23 shore, leaving exactly 22
roots.  This is a genuine common-word rank gain on the critical shore, not
merely an annealed Hall count.  It is not yet a common-word lift of a full
global maximum matching.

## 8. Full exact audit

The sequential common-core contractions are

\[
\begin{array}{c|c|c|c|c}
&\text{common cells}&\text{old/new banks}&\text{common rank}
&\text{contracted rank}\\ \hline
\text{router}&19293&18/18&16350&10\to10\\
\text{splitter}&19270&41/41&16343&17\to18.
\end{array}                                                       \tag{8.1}
\]

Hence

\[
\nu:16360\to16360\to16361,\qquad
h:23\to23\to22.                                                  \tag{8.2}
\]

For the three canonical shores, the cross-gap matrix is

\[
\begin{pmatrix}
23&23&22\\
23&23&22\\
22&22&22
\end{pmatrix}.                                                    \tag{8.3}
\]

The final DM shore removes exactly `4877,4909` and adds no target.

Both moves preserve:

* all 6435 rank-eight states exactly once;
* Johnson adjacency;
* depth-three residence and nonempty maximal erosion;
* complete upper support at every depth \(q=1,\ldots,7\).

The lower hole vectors are

\[
(4,19,6,1,0,0,0)
\to(4,19,6,1,0,0,0)
\to(4,18,6,1,0,0,0).                                             \tag{8.4}
\]

Thus the splitter gains lower depth-two target `4877` and loses no lower
support.  The seven zero-degree targets remain

\[
2575,5801,13616,13620,17738,21641,29776.                          \tag{8.5}
\]

At Hall 22 the canonical DM shore has 22 gap-one circuit components:

\[
\begin{array}{c|l}
169/168&1920\\
161/160&960,8217,24610\\
160/159&449,8218\\
5/4&4213,7504\\
3/2&1103,18970\\
2/1&2420,2676,9524,17683,19568\\
1/0&2575,5801,13616,13620,17738,21641,29776.
\end{array}                                                       \tag{8.6}
\]

The first 15 components admit an abstract split by Theorem 3.1.  The last
seven require a first-cell creator.

## 9. Exact orbit-hitting gate

For a circuit \(C\) at a lifted state \(z\), let

\[
\mathcal O_C(z)
\]

be the states reachable by neutral arrows which transport a pointed matching
certificate for \(C\) and its common-word lift.  Let \(\mathcal G_C\) be the
states admitting a legal, residence-safe, shadow-safe, common-word splitter
which retains or reroutes the complement matching, satisfies the unit-rank
cap (or retains a gap-\((h(z)-1)\) Hall shore), and has a certified descendant
state in the same transition class.

Within the neutral-router/splitter architecture, the exact
necessary-and-sufficient routing condition is

\[
\boxed{\mathcal O_C(z)\cap\mathcal G_C\ne\varnothing.}            \tag{9.1}
\]

If (9.1) holds after every discharge, Theorem 5.1 iterates and lowers Hall
deficiency once per step.  Full transitivity is stronger than necessary.
Conversely, port-frame transitivity without the full lifted data
(4.3)--(4.6) is not sufficient.

The pair (1.1) proves the outer-Hall and critical-shore/common-word projections
of (9.1) for \(C=\{4877,4909\}\).  It does **not** prove membership in the
full \(\mathcal G_C\) defined above, because no common-word lift of a complete
16361-edge maximum matching has been supplied.  The desired universal
nonzero-component lemma is:

> For each of the 15 nonzero Hall-22 circuits, its full lifted protected
> neutral reachability class meets a component-specific splitter locus, with
> one more augmenting path than lost protected matching edges.

For the next outer descent \(H22\to H21\), it is enough to prove this for one
of the 15 circuits.  For iteration through all nonzero components, the
orbit-hitting property must hold hereditarily after every preceding
discharge; separate one-step routes from the initial H22 state do not by
themselves compose.

For the zero floor, the corresponding smallest lemma replaces “splitter” by
“first-cell creator” for one target in (8.5).  Section 10 proves such a creator
for `2575`, but it exchanges the unresolved target rather than lowering Hall.
No refinement-only theorem can remove the whole zero floor.  Even after outer
Hall reaches zero, one full maximum matching must still pass the simultaneous
common-word criterion; the native critical-shore certificate in Section 7
does not by itself prove that global lift.

## 10. Separate Hall-22/zero-six Pareto branch

There is an independently audited compound

\[
(22,7)\xrightarrow{\operatorname{FF}(882,2606,3222)}(23,6)
\xrightarrow{\operatorname{RF}(1500,4943,6184)}(22,6),           \tag{10.1}
\]

where the ordered pair is `(Hall deficiency, degree-zero targets)`.  The
first braid temporarily loses lower targets `8905,713,8777`; the second
restores all of them.  The final state has the same lower hole vector

\[
(4,18,6,1,0,0,0)                                                \tag{10.2}
\]

as the Hall-22 state of Section 8, and every upper support layer remains
complete.  Exact deck, Johnson chronology, and residence also persist.

The final controller gives `2575` a literal first cell, while target `2607`
becomes the displaced unresolved target.  One physical word realizes 984
selected active-shore pins, including this exceptional repin, but the
certificate explicitly is not a common-word lift of a full global maximum
matching.  Thus (10.1) proves a first-cell routing mechanism and reduces the
zero count, but neither lowers Hall below 22 nor composes automatically with a
nonzero-circuit splitter.

## 11. Audit artifacts

The frozen carriers and hashes are:

* `scratch/k15_segment_braid_hall23.json`,
  `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d`;
* `scratch/k15_segment_braid_hall23_portal.json`,
  `9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6`;
* `scratch/k15_segment_braid_hall22.json`,
  `c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798`.

Independent reconstruction is in

* `scratch/audit_k15_h22_router_splitter_structure.py`;
* `scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json`;
* `scratch/k15_hall23_portal_native_dm_pins_certificate.json`;
* `scratch/k15_hall22_native_dm_pins_certificate.json`.

The combined 985-pin critical-shore lift is checked directly by

* `scratch/audit_k15_h22_router_splitter_common_q.py`, SHA-256
  `559d96a1fe0d490b7942ba923789e0898c9c75c4d2f1201a69bea0772a2c84a2`;
* `scratch/k15_h22_router_splitter_common_q_certificate.json`, SHA-256
  `fb8aae805a974e9a8c8b143db860ddaf7528913ee27aaa3e7034bbba39f292e9`.

The Pareto branch is checked by

* `scratch/k15_segment_braid_hall23_zero6_from22.json`, SHA-256
  `9cfc942a60de988545cf0e19c38b57ed50879df92d5f56d3ad2be9862e818bfb`;
* `scratch/k15_segment_braid_hall22_zero6.json`, SHA-256
  `bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778`;
* `scratch/audit_threadD_h22_zero6_common_q.py`, SHA-256
  `43d2190c9d4f521e26e1bbd7abbb40a30ab051b0bb88cabaa93dcef418bacd75`;
* `scratch/threadD_h22_zero6_common_q_certificate_20260728.json`, SHA-256
  `0f702d3bc1d005d977346779808949789da354744913721e5016a765933e6457`.

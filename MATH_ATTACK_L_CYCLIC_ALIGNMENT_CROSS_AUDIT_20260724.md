# Cross-audit of Lane L: cyclic alignment inside one exact wreath factor

Date: 2026-07-24

Method: pure mathematics only.  No web search, finite search, solver, or
computer-assisted enumeration was used.

## 0. Audit verdict

The five requested mathematical cores all pass:

1. the Hall--Bellman formulation is exact for the stated one-ascending-pass
   adjacent-swap class;
2. the cyclic point-regular quota construction is correct, but is rankwise
   only;
3. the directed toggle-cycle law is exact under point regularity at the two
   adjacent ranks;
4. every nontrivial exact-factor alternating \(C_8\) move has inherited-path
   profile
   \[
   3,n-3,3,n-3
   \]
   for \(m\ge3\); and
5. the corrected \(4(n-1)\) component-noise ledger and its Boolean-\(E_2\)
   stability consequence are valid.  In particular, the proposed
   same-window one-step near-baseline heat gate is impossible at every global
   minimizer.

No fatal counterexample was found.  The source does require the following
repairs or qualifications.

- In the overview and the \(C_8\) discussion, replace
  “\(\Theta(m)\) average reuse” by “\(\Omega(m)\) average updates of the
  persistent bookkeeping slots.”  Only a lower bound is proved.
- In Theorem 8.1, establish that every new seam crosses between the two old
  wreath supports before invoking the cross-neighbour calculation.
- Add the short signed-gluing lemma proved in Section 4.5 below.  It makes the
  orientation-frustration conclusion completely explicit.
- The determinant-\(2\) assertion following (3.5) is not proved inside the
  Lane L report.  It is true for the cited generic configuration matrix, but
  a self-contained report should display the minor or label the assertion as
  imported.  It does not concern the Hall--Bellman theorem itself.
- “Reachable” in the Bellman section should be read as ownerwise
  prefix-reachable.  The recursion from the initial state, rather than the
  bare state-space definition, enforces reachability through a balanced
  history.
- The heat no-go theorem requires the same \(H\)-window global minimizer,
  unnormalized counting norms, and one copy of each unordered coordinate
  transposition.  It closes this component-switch near-equality proposal,
  not every possible multistep, circuit, or adaptive heat mechanism.

With those repairs, the final proved/open ledger of Lane L is accurate.

## 1. Hall--Bellman formulation

Retain the source notation.  At stage \(q\), owner \(X\) has the two distinct
legal endpoints

\[
u_X=L_q(X),
\qquad
v_X=L_{q+1}(X)\cup\{\kappa_q(X)\}.
\tag{1.1}
\]

Choosing \(u_X\) is a non-toggle and choosing \(v_X\) is a toggle.  The
chosen endpoint is the depth-\(q\) set, so endpoint indegrees are exactly the
rank loads.

### 1.1 Prescribed quota criterion

Let \(G=(V,E)\) be the owner-labelled multigraph at one stage, let
\(i(U)\) be the number of edges internal to \(U\), and let
\(|\partial U|\) count boundary edges with multiplicity.  Let
\(b:V\to\mathbb Z_{\ge0}\) satisfy

\[
\sum_{v\in V}b(v)=|E|=W.
\tag{1.2}
\]

There is an orientation having indegree vector \(b\) if and only if

\[
\boxed{
i(U)\le b(U)\le i(U)+|\partial U|
\quad\text{for every }U\subseteq V.
}
\tag{1.3}
\]

#### Necessity

Every edge internal to \(U\) must place its head in \(U\), so
\(i(U)\le b(U)\).  Only internal and boundary edges can place a head in
\(U\), so \(b(U)\le i(U)+|\partial U|\).

#### Sufficiency

Make one left node for every labelled edge and \(b(v)\) right clones of
every vertex \(v\).  Join an edge-node to the clones of its two endpoints.
Hall's condition for this bipartite graph reduces to

\[
i(U)\le b(U)
\tag{1.4}
\]

for every endpoint family \(U\): among edge-node families whose neighbour
set is contained in \(U\), the largest is the set of all internal edges of
\(U\).  Since the two sides have the same total size, a saturating matching
uses every clone and assigns each edge to one endpoint with the prescribed
indegree.  The upper inequality in (1.3) is equivalently the lower inequality
for \(V\setminus U\), because

\[
|E|=i(U)+i(V\setminus U)+|\partial U|.
\]

Thus (3.1) of the source is exact.

### 1.2 Mobile balanced quotas

Write

\[
|V|=N_q,
\qquad
W=c_qN_q+\rho_q,
\qquad 0\le\rho_q<N_q.
\tag{1.5}
\]

An orientation with every indegree in \(\{c_q,c_q+1\}\) is the same as an
orientation with lower capacities \(c_q\), upper capacities \(c_q+1\), and
total \(W\).  The exact cut conditions are

\[
i(U)\le(c_q+1)|U|
\tag{1.6}
\]

and

\[
c_q|U|\le i(U)+|\partial U|.
\tag{1.7}
\]

Complementing (1.7) and using (1.5) gives

\[
i(V\setminus U)
\le c_q|V\setminus U|+\rho_q.
\tag{1.8}
\]

Renaming \(V\setminus U\) proves exactly the two inequalities in source
(3.2).  Integral lower/upper-capacity flow proves sufficiency.  The total
load automatically forces exactly \(\rho_q\) high vertices.

### 1.3 Immediate toggle program

At a carried state \(\kappa\), orient every edge initially toward
\(u_X=L_q(X)\).  Its load is the canonical histogram \(\mu_q^F\), even if
earlier stages toggled, because the non-toggle endpoint remains \(L_q(X)\).
A toggle changes the load by

\[
\mathbf e_{v_X}-\mathbf e_{u_X}.
\]

Consequently, for a prescribed feasible quota \(b_q\), the minimum number of
immediate toggles is exactly

\[
\min\left\{
\mathbf1^Tx:B_Dx=b_q-\mu_q^F, 0\le x\le1
\right\}.
\tag{1.9}
\]

The directed incidence matrix \(B_D\) is totally unimodular.  The right-hand
side and box bounds are integral, so every nonempty optimum face contains an
integral optimum.  Thus source (3.3) is correct.

### 1.4 Bellman recursion

For one owner, the recurrence

\[
\kappa_{q+1}=
\begin{cases}
\kappa_q,&\text{toggle},\\
a_{q+1},&\text{non-toggle}
\end{cases}
\tag{1.10}
\]

implies

\[
P_q=L_{q+1}\cup\{\kappa_{q+1}\}.
\tag{1.11}
\]

Every \(\kappa_q\in\{a_1,\ldots,a_q\}\) is reachable ownerwise: to carry
\(a_t\), install it when it first becomes available and toggle at every
later stage through \(q-1\).  A vector of such letters is therefore the
correct state space before balanced-history restrictions.

Given that state, the present orientation determines both its toggle cost and
the entire next state.  Backward induction then proves

\[
R_q^F(\kappa)=
\min_{\mathcal O\in\mathcal B_q(\kappa)}
\left[
\frac{T(\mathcal O)}{c_q}+R_{q+1}^F(\kappa')
\right].
\tag{1.12}
\]

Starting from \((a_1^X)_X\), the recursion visits only states generated by a
common balanced history.  Conversely, every balanced one-pass toggle history
chooses one term in (1.12).  Since

\[
e_q(F,P)=\#\{X:\varepsilon_q(X)=1\},
\tag{1.13}
\]

source (3.5) follows.

This is an exact theorem for the one-ascending-pass class.  It is not an
exact formulation of unrestricted downward flags, and the source states this
qualification correctly.

## 2. Point-regular quota construction

### Theorem 2.1

For fixed \(A>0\), all sufficiently large \(m\), and every
\(0\le q\le K_A\), there is a cyclically invariant family

\[
\mathcal H_q\subseteq\binom{[n]}r,
\qquad r=m-q,
\qquad |\mathcal H_q|=\rho_q.
\tag{2.1}
\]

The balanced quota

\[
b_q(S)=c_q+\mathbf1_{\mathcal H_q}(S)
\tag{2.2}
\]

then has point degree \(rB=rW/n\) at every coordinate.

#### Audit proof

Put

\[
g=\gcd(n,r),
\qquad L=\frac ng.
\tag{2.3}
\]

Because \(n=2m+1\) is odd,

\[
g=\gcd(n,2r)=\gcd(n,2q+1),
\tag{2.4}
\]

so \(g\le2q+1=O_A(\sqrt m)\).

If an \(r\)-set has stabilizer order \(h\) under cyclic rotation, then
\(h\mid n\) and invariance makes it a union of coordinate orbits of size
\(h\), so \(h\mid r\).  Hence \(h\mid g\), and its orbit length

\[
\frac nh=\frac ghL
\]

is a multiple of \(L\).  Therefore

\[
L\mid N_q.
\tag{2.5}
\]

Also \(n\mid W\), since \(W/n=\operatorname{Cat}_m\).  Thus

\[
L\mid W,\qquad
L\mid\rho_q,\qquad
L\mid(N_q-\rho_q).
\tag{2.6}
\]

Let

\[
e=\min(\rho_q,N_q-\rho_q).
\]

Since \(e/L\) is integral and \(n=gL\), Euclidean division gives uniquely

\[
e=an+bL,
\qquad a\ge0,quad0\le b<g.
\tag{2.7}
\]

There are enough full length-\(n\) orbits.  Every nonfull orbit has a
nontrivial stabilizer of odd order \(h\ge3\) dividing \(g\), so the number of
sets lying in nonfull orbits is at most

\[
\sum_{\substack{h\mid g\\h>1}}
\binom{n/h}{r/h}
\le\tau(g)2^{n/3}=o_A(N_q).
\tag{2.8}
\]

Here \(N_q\ge W/C_A\ge2^n/[C_A(n+1)]\).  Thus more than \(N_q/2\) sets lie
in full orbits, while \(an\le e\le N_q/2\); at least \(a\) full orbits are
available.

There are also enough exact length-\(L\) orbits.  Put \(k=r/g\).  Since

\[
\gcd(L,k)=1,
\tag{2.9}
\]

every length-\(L\), weight-\(k\) binary word is primitive: a proper
repetition number would divide both \(L\) and \(k\).  Repeating such a word
\(g\) times produces an \(r\)-set with stabilizer exactly \(g\), hence orbit
length exactly \(L\).  The number of these orbits is

\[
\frac1L\binom Lk.
\tag{2.10}
\]

Uniformly in the fixed window,

\[
L=\Omega_A(\sqrt m),
\qquad
\frac{k}{L}=\frac rn\in[1/3,1/2)
\tag{2.11}
\]

for large \(m\).  The quantity in (2.10) is therefore exponential in
\(L\), whereas \(g=O_A(\sqrt m)\); in particular it exceeds \(g>b\).

Choose \(a\) full orbits and \(b\) length-\(L\) orbits.  Their union
\(\mathcal E\) is cyclically invariant and has size \(e\).  If
\(\rho_q\le N_q/2\), take \(\mathcal H_q=\mathcal E\); otherwise take the
complement of \(\mathcal E\) in the full rank.  This gives (2.1).

Cyclic transitivity makes all point degrees of \(\mathcal H_q\) equal, and
double counting gives degree \(r\rho_q/n\).  Therefore

\[
\begin{aligned}
\sum_{S\ni x}b_q(S)
&=c_q\binom{n-1}{r-1}+\frac{r\rho_q}{n}\\
&=\frac{r(c_qN_q+\rho_q)}n
=\frac{rW}{n}=rB.
\end{aligned}
\tag{2.12}
\]

This verifies Theorem 4.1 of the source.

### Scope

The construction chooses \(\mathcal H_q\) independently at each rank.  It
does not prove any of the following:

- adjacent-rank clone Hall compatibility;
- existence of one nested resolution attaining all these quotas;
- orientability in any particular owner graph; or
- short toggle recourse.

The source explicitly records this limitation.  Thus the theorem removes a
rankwise first-moment obstruction and nothing stronger.

## 3. Directed toggle cycles

At stage \(q\), assign to owner \(X\) the directed coordinate arc

\[
a_{q+1}^X\longrightarrow\kappa_q(X).
\tag{3.1}
\]

A toggle replaces \(a_{q+1}^X\) by \(\kappa_q(X)\) in the chosen set, so its
point-incidence change is

\[
\mathbf e_{\kappa_q(X)}-\mathbf e_{a_{q+1}^X}.
\tag{3.2}
\]

Every canonical deletion position contains each coordinate exactly once per
wreath row, hence

\[
\#\{X:a_{q+1}^X=x\}=B.
\tag{3.3}
\]

Moreover,

\[
P_{q-1}(X)=L_q(X)\cup\{\kappa_q(X)\}
\tag{3.4}
\]

is a disjoint union.  The canonical depth-\(q\) sets have point degree
\((m-q)B\).  If the preceding load discrepancy is

\[
\Delta_{q-1,x}
=\#\{X:x\in P_{q-1}(X)\}-(m-q+1)B,
\]

then (3.4) gives

\[
\#\{X:\kappa_q(X)=x\}=B+\Delta_{q-1,x}.
\tag{3.5}
\]

Thus, when the preceding load is point-regular, the full coordinate
multidigraph (3.1) has indegree and outdegree \(B\) at every coordinate.

For the selected toggle arcs,

\[
\Delta_q
=\sum_{X:\varepsilon_q(X)=1}
(\mathbf e_{\kappa_q(X)}-\mathbf e_{a_{q+1}^X}).
\tag{3.6}
\]

If the attained depth-\(q\) quota is also point-regular, then
\(\Delta_q=0\).  Equation (3.6) says exactly that the selected directed
subgraph has equal indegree and outdegree at every coordinate.  Every finite
Eulerian directed multigraph decomposes into directed cycles.  Conversely,
every union of directed cycles has zero boundary and preserves all point
margins.  This proves Theorem 5.1.

For an arbitrary toggle set, the imbalance vector is indegree minus
outdegree.  The usual trail decomposition therefore has terminal endpoint
multiplicities \((\Delta_q)_+\) and initial endpoint multiplicities
\((-\Delta_q)_+\), after repeated vertices are split.  The sign convention
in the source is correct.

At \(q=1\), the two consecutive canonical deletion letters around one wreath
row are consecutive coordinates in its cyclic order.  After a harmless
index shift, the arcs are

\[
z_0\to z_1\to\cdots\to z_{n-1}\to z_0.
\tag{3.7}
\]

Hence each row contributes one directed Hamilton cycle.  Later carried
letters can destroy this rowwise identity, but (3.5) retains global
Eulerianity under point-regular preceding loads.

Finally, if both adjacent rank loads are point-regular, nestedness gives

\[
\#\{X:d_q^P(X)=x\}
=(m-q+1)B-(m-q)B=B.
\tag{3.8}
\]

Thus Corollary 5.2 is exact.  None of these first-order cycle identities
implies higher-set Hall feasibility, common cycle packets across depths, or
small total recourse.

## 4. Exact-factor \(C_8\) trades

Let \(O_m=KG(2m+1,m)\), let \(m\ge3\), and suppose exact wreath factors
\(F,F'\) have symmetric difference equal to one nontrivial simple
\(F\)-alternating \(C_8\).  Wreath supports are induced \(n\)-cycles in
\(O_m\).

### 4.1 The old and new cut shapes are \(2+2\)

If a touched old wreath loses only one factor edge, the remainder is an
\(n\)-vertex path.  It cannot inherit a positive external path inside a new
\(n\)-cycle.  Closing its two endpoints internally would require the removed
edge, because its support induces exactly the original cycle.  Thus every
touched old wreath loses at least two edges.

All four removed edges cannot lie in one old wreath.  Then all changed
vertices lie in that one \(n\)-vertex support.  A new exact factor would have
to put one \(n\)-cycle on precisely that support, but inducedness makes the
original cycle the only possibility.  The move would be trivial.  Therefore
the four removed edges split \(2+2\) between two old wreaths.  Applying the
same argument to the reverse switch gives a \(2+2\) split between two new
wreaths.

### 4.2 Every new seam crosses the two old supports

This step should precede the cross-neighbour calculation in the source
proof.  Any odd-graph edge whose endpoints both lie in one old wreath support
is, by inducedness, an old cycle edge.  It cannot belong to \(F'\setminus F\).
Hence each of the four added seams joins the two distinct old supports.

### 4.3 Cross-neighbours force distance three

Let \(Y,Y'\) be the endpoints of one removed edge in the second old wreath,
and let their new-seam neighbours in the first old wreath be \(X,X'\):

\[
X\cap Y=\varnothing,
\qquad
X'\cap Y'=\varnothing.
\]

Since \(Y,Y'\) are disjoint \(m\)-sets, their union omits one point \(p\).
The two old wreath supports are disjoint as vertex families.  Therefore

\[
X=(Y'\setminus\{y'\})\cup\{p\},
\qquad
X'=(Y\setminus\{y\})\cup\{p\},
\tag{4.1}
\]

and

\[
X\cap X'=\{p\}.
\tag{4.2}
\]

In a wreath cycle, vertices at separation \(2s\) have intersection
\(m-s\), while vertices at separation \(2s+1\) have intersection \(s\).
Thus intersection size one is equivalent to cyclic distance three.

### 4.4 The universal path profile

Index the two removed edges of the first old wreath as

\[
C_0C_1,\qquad C_aC_{a+1},
\qquad2\le a\le m,
\tag{4.3}
\]

choosing the shorter cut separation.  The endpoints of either removed edge
in the other old wreath have seam preimages consisting of one endpoint from
each cut in (4.3), since the two endpoints of one cut are adjacent rather
than distance three.

There are two possible pairings.  The parallel pairing

\[
\{C_0,C_a\},\qquad\{C_1,C_{a+1}\}
\]

forces \(a=3\).  The crossed pairing forces simultaneously

\[
a-1=3,
\qquad
\min(a+1,n-a-1)=3.
\tag{4.4}
\]

The first equation gives \(a=4\), while the second then asks
\(\min(5,n-5)=3\), impossible for odd \(n\ge7\).  Hence each old wreath is
cut into paths of vertex-orders \(3\) and \(n-3\).  Reversing the trade gives
the same statement for each new wreath.  The four inherited common paths
therefore have profile

\[
\boxed{3,n-3,3,n-3.}
\tag{4.5}
\]

This verifies the central claim of Theorem 8.1.

### 4.5 Incidence signs and the unique reversed short path

No new wreath can inherit both paths of one old wreath: that would give it
all \(n\) vertices of the old support, and inducedness would reproduce the
old cycle.  Thus the inherited-path incidence graph between the two old and
two new wreaths is the simple \(K_{2,2}\), viewed as a \(4\)-cycle.

Give each incidence edge the sign saying whether fixed old and new
orientations traverse that common path in the same direction.  The following
elementary gluing lemma supplies the implicit step in the source.

> **Signed gluing lemma.**  Follow alternately the old and new seam pairings
> around the incidence \(4\)-cycle while retaining the two endpoint states of
> each inherited path.  After one circuit, the endpoint state is flipped if
> and only if the product of the four path signs is negative.  Thus positive
> sign product splits the seam endpoints into two alternating \(4\)-cycles,
> while negative sign product joins them into one alternating \(8\)-cycle.

The symmetric difference is one simple \(C_8\), so the sign product is
negative.  Equivalently, a positive product would create alternating
\(C_4\)'s, which are also impossible because the odd graph is \(C_4\)-free:
two distinct \(m\)-sets cannot have two distinct common disjoint
\(m\)-neighbours.

Reversing one wreath orientation switches both incident signs.  On a signed
\(4\)-cycle of negative product, vertex switches can make any prescribed one
edge the unique negative edge.  Every new wreath inherits one short and one
long path.  Choose the unique negative edge to be short.  Then both long
paths agree and exactly one three-vertex inherited path reverses.  This
proves part 3 of Theorem 8.1.

### 4.6 Multidepth and packing conclusions

For a preserved path of vertex-order \(\ell\), only the first and last
\(q\) centres can change its depth-\(q\) cyclic color, so its coupling ceiling
is \(\min(\ell,2q)\).  Summing over (4.5) gives

\[
R_1=4\cdot2=8
\tag{4.6}
\]

and, for \(2\le q\le m-1\),

\[
R_q=2\cdot3+2\cdot2q=4q+6.
\tag{4.7}
\]

For pointed flags the one reversed short path must be charged in full.  This
changes the depth-one ceiling from \(8\) to \(9\); for \(q\ge2\), the short
path was already charged in full.  Hence

\[
\widetilde R_1=9,
\qquad
\widetilde R_q=4q+6\quad(2\le q\le m-1).
\tag{4.8}
\]

These are upper coupling ceilings, not asserted exact histogram distances.
They imply the source Lipschitz bounds for \(O_q\), \(e_q\), \(\Phi_A\), and
\(J_A\).  Since \(c_1=1\), summation gives exactly the corrections \(-2\)
and \(-1\) in source (8.7) and (8.8).

At depth one, one move changes overload by at most eight.  A sequential chain
changing it by \(\delta W\) therefore has at least \(\delta W/8\) moves.
Each move updates two of the \(B=W/n\) persistent wreath positions, so the
average number of updates per bookkeeping slot is at least

\[
\frac{2(\delta W/8)}B=\frac{\delta n}{4}=\Omega(m).
\tag{4.9}
\]

There is no upper bound on this average: neutral moves may be arbitrarily
numerous.  This is why the overview's \(\Theta(m)\) wording must be changed
to \(\Omega(m)\).

A simultaneously support-disjoint family uses two old wreaths per move and
therefore has at most \(B/2\) moves.  Its total depth-one effect is at most
\(4B=o(W)\).  These bookkeeping slots need not retain the same actual wreath
supports along a sequential chain, exactly as the source cautions.

## 5. Corrected heat ledger

This section audits all conclusions in Sections 11--12 of the source that
depend on Boolean-\(E_2\) stability.

For depth \(q\), put

\[
f_q=\mu_q-a_q\mathbf1,
\qquad a_q=\frac{W}{N_q}=c_q+\theta_q.
\]

Every oriented wreath row contributes all \(n\) cyclic intervals of rank
\(r=m-q\), so every coordinate occurs exactly \(r\) times in that row.
Consequently

\[
\sum_{S\ni x}\mu_q(S)=rB
=a_q\binom{n-1}{r-1}.
\tag{5.1}
\]

Thus \(f_q\) has zero total and zero point-star margins:

\[
f_q^{(0)}=f_q^{(1)}=0.
\tag{5.2}
\]

### 5.1 Component heat identity and global minimality

Fix an unordered transposition \(\tau\).  In an ownership-overlay component
\(C\), let \(u_{q,C}\) and \(w_{q,C}\) be the two complete-side histograms.
Fair independent component switching gives

\[
\mathbb E V_q(F')
=\left\|
\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1
\right\|_2^2
+\frac14\sum_C\|u_{q,C}-w_{q,C}\|_2^2.
\tag{5.3}
\]

Since \(\mu_q\) and \(\tau\mu_q\) have equal norm about the constant vector,

\[
V_q(F)
=\left\|
\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1
\right\|_2^2
+\frac14\|\mu_q-\tau\mu_q\|_2^2.
\tag{5.4}
\]

Every component child is an exact oriented factor.  If \(F\) is a global
minimizer of the **same weighted \(H\)-window objective**, then weighting
(5.3)--(5.4), summing over \(q\), and multiplying by four gives

\[
A_{\tau,H}\le N_{\tau,H}.
\tag{5.5}
\]

After summing once over unordered transpositions,

\[
D_H\le R_H.
\tag{5.6}
\]

This is the only step that uses global minimality.  It is invalid for an
arbitrary factor or for a minimizer of a different window.

### 5.2 Sharp Johnson coefficient

For the Johnson harmonic decomposition on rank \(r\),

\[
\sum_{\tau}\|f-\tau f\|_2^2
=2\sum_{j\ge0}j(n-j+1)\|f^{(j)}\|_2^2,
\tag{5.7}
\]

where every unordered coordinate transposition occurs once and norms are
unnormalized counting norms.  By (5.2), \(j\ge2\).  Therefore

\[
\sum_\tau\|f-\tau f\|_2^2
\ge4(n-1)\|f\|_2^2,
\tag{5.8}
\]

and the exact excess is

\[
2\sum_{j\ge3}
(j-2)(n-j-1)\|f^{(j)}\|_2^2.
\tag{5.9}
\]

For integer loads of total \(W\),

\[
Q_q=V_q-V_q^{\min}
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)\ge0.
\tag{5.10}
\]

Also \(Q_q\ge2O_q\): every unit below \(c_q\) or above \(c_q+1\) costs at
least two units of the quadratic floor energy.  Hence

\[
P_H\le\frac{E_H}{2}.
\tag{5.11}
\]

Using \(\|f_q\|_2^2=V_q^{\min}+Q_q\), equations (5.6)--(5.9) give

\[
R_H\ge D_H\ge4(n-1)(B_H+E_H).
\tag{5.12}
\]

Therefore

\[
P_H\le\frac{E_H}{2}
\le\frac{R_H-4(n-1)B_H}{8(n-1)}.
\tag{5.13}
\]

The exact nonnegative slack decomposition is

\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+[D_H-4(n-1)(B_H+E_H)]\\
&+4(n-1)E_H.
\end{aligned}
\tag{5.14}
\]

This verifies source (11.3)--(11.6), including the factor-two correction from
\(2n\) to \(4(n-1)\).

### 5.3 Size of the unavoidable floor baseline

Since \(N_q=W/a_q\),

\[
\frac{V_q^{\min}}{c_q}
=W\frac{\theta_q(1-\theta_q)}{a_qc_q}.
\tag{5.15}
\]

For \(q=x\sqrt m+o(\sqrt m)\),

\[
a_q=e^{x^2+o(1)}.
\]

The fixed-window Riemann sum gives

\[
B_H\sim\beta_AW\sqrt m,
\tag{5.16}
\]

where

\[
\beta_A=
\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.
\tag{5.17}
\]

The integrand is positive except at the discrete floor-crossing points, and
is positive on every sufficiently small interval to the right of zero, so
\(\beta_A>0\) for every \(A>0\).

It follows immediately that the old proposed upper gate

\[
R_H\le2nB_H+o(nW)
\tag{5.18}
\]

is impossible: its leading baseline is below the forced floor
\(4(n-1)B_H\) by

\[
[4(n-1)-2n]B_H
=(2n-4)B_H=\Theta_A(nW\sqrt m).
\tag{5.19}
\]

### 5.4 Boolean-\(E_2\) stability input

The imported theorem is valid in the required nondegenerate central ranks.
For every compact \(I\subset(0,\theta_*)\),

\[
\theta_*:=\frac{3-\sqrt6}{6},
\]

there is \(\varepsilon_I>0\) such that every Boolean family
\(\mathcal B\subseteq\binom{[n]}r\) of density \(\theta\in I\) satisfies

\[
\left\|
P_{E_1\oplus E_{\ge3}}
(\mathbf1_{\mathcal B}-\theta\mathbf1)
\right\|_2^2
\ge\varepsilon_I\binom nr.
\tag{5.20}
\]

The proof has no hidden influence or inverse-theorem assumption.  Every
\(E_2\) function is represented by a symmetric zero-diagonal harmonic matrix
\(A\mathbf1=0\).  On a central slice,

\[
\mathbb Eh^2=\alpha S_2,
\qquad
\mathbb Eh^3=aC_3+b\operatorname{tr}(A^3),
\]

with

\[
\alpha=\frac1{16}+O(n^{-1}),
\qquad a=O(n^{-1}),
\qquad b=\frac1{64}+O(n^{-1}).
\]

The elementary bounds

\[
|C_3|\le S_2^{3/2},
\qquad
|\operatorname{tr}(A^3)|\le(2S_2)^{3/2}
\]

give standardized skew at most \(2\sqrt2+O(n^{-1})\).  A centered Boolean
indicator has standardized skew

\[
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}},
\]

which exceeds \(2\sqrt2\) precisely for \(0<\theta<\theta_*\).  The uniform
fourth-moment bound for \(E_2\) transfers the strict compact skew gap into
the \(L^2\) stability (5.20).  This verifies the exact imported input used by
Lane L.

### 5.5 Integer rounding and the rankwise dichotomy

Fix \(A>0\) and choose

\[
0<u<v<\min\{A,\sqrt{\log(17/16)}\}.
\tag{5.21}
\]

For every integer \(q\in[u\sqrt m,v\sqrt m]\), after a fixed small shrinking
of \([u,v]\),

\[
c_q=1,
\qquad
\theta_q=a_q-1\in I\Subset(0,1/16),
\qquad
N_q=\Theta_{A,u,v}(W).
\tag{5.22}
\]

Round the integer load \(\mu_q\) to a vector

\[
b_q=\mathbf1+\mathbf1_{\mathcal B_q}
\]

of the same mass.  Nearest adjacent-integer rounding followed by exactly the
necessary number of flips gives

\[
\|\mu_q-b_q\|_2^2
\le2\mathcal E_q+2\sqrt{N_q\mathcal E_q},
\qquad \mathcal E_q=Q_q.
\tag{5.23}
\]

The pointwise inequality behind (5.23) is

\[
(\mu-\widetilde b)^2
\le(\mu-1)(\mu-2),
\]

and Cauchy--Schwarz bounds the mass discrepancy by
\(\sqrt{N_q\mathcal E_q}\).  If \(\widetilde b\) has \(t\) entries equal to
two and the required bonus count is \(\rho_q\), then there are automatically
at least \(|t-\rho_q|\) entries of the required kind to flip: use twos when
\(t>\rho_q\), and use the \(N_q-t\ge\rho_q-t\) ones when \(t<\rho_q\).
Thus the mass correction invoked in (5.23) is always feasible.

Put

\[
\mathcal H_q=\sum_{j\ge3}\|f_q^{(j)}\|_2^2.
\]

Because \(f_q^{(1)}=0\), projection, (5.20), and (5.23) give

\[
\varepsilon_IN_q
\le2\mathcal H_q+4\mathcal E_q
+4\sqrt{N_q\mathcal E_q}.
\tag{5.24}
\]

After replacing \(\varepsilon_I\) by \(\min(\varepsilon_I,1)\), (5.24)
implies

\[
\boxed{
\mathcal H_q\ge\frac{\varepsilon_I}{4}N_q
\quad\text{or}\quad
\mathcal E_q\ge\frac{\varepsilon_I^2}{256}N_q.
}
\tag{5.25}
\]

The constants leave ample slack, so the dichotomy is valid.

### 5.6 Quantitative no-go theorem

At the same-window global minimizer, (5.9) and (5.14) refine to

\[
\begin{aligned}
R_H-4(n-1)B_H
\ge{}&4(n-1)\sum_{q=1}^H\frac{\mathcal E_q}{c_q}\\
&+2\sum_{q=1}^H\frac1{c_q}
\sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\end{aligned}
\tag{5.26}
\]

For \(3\le j\le m\),

\[
(j-2)(n-j-1)\ge n-4.
\tag{5.27}
\]

At each of the \(\Theta_{u,v}(\sqrt m)\) depths in (5.22), the dichotomy
(5.25) makes one of the two lines of (5.26) at least

\[
\min\left\{
\frac{(n-4)\varepsilon_I}{2}N_q,
\frac{(n-1)\varepsilon_I^2}{64}N_q
\right\}
=\Omega_A(nW).
\tag{5.28}
\]

Summing gives a constant \(\kappa_A>0\) such that

\[
\boxed{
R_H-4(n-1)B_H
\ge\kappa_A nW\sqrt m.
}
\tag{5.29}
\]

Thus the corrected proposed gate

\[
R_H\le4(n-1)B_H+o(nW)
\tag{5.30}
\]

is impossible at every global minimizer of the same fixed Gaussian-window
objective.  The contradiction is stronger than needed: its unavoidable gap
is order \(nW\sqrt m\), whereas (5.30) allows only \(o(nW)\).

### 5.7 Exact logical consequences

All downstream heat conclusions in the source are correct with the following
scope.

1. The old \(2nB_H\) baseline is already below the sharp spectral floor.
2. If the corrected near-baseline upper bound (5.30) were true at a
   same-window minimizer, (5.13) would imply \(E_H=o(W)\) and
   \(P_H=o(W)\).
3. Boolean-\(E_2\) stability proves that (5.30) is false at every such
   minimizer.
4. The lower gap (5.29) does **not** imply \(E_H\) or \(P_H\) is large.  It
   may be paid entirely by Johnson degrees at least three.
5. Even an independent proof of \(P_H=o(W)\) would remain unlabelled; no
   implication \(P_H=o(W)\Rightarrow J_A(F)=o(W)\) is proved.
6. The result refutes this one-step complete-component resampling
   near-equality certificate.  It does not refute MWB, labelled
   synchronization, the contiguous-OR conjecture, a macrotrade plateau
   argument, or a genuinely different multistep/adaptive heat inequality.

Accordingly, phrases such as “the corrected component-noise near-equality
proposal is closed” are accurate.  A phrase claiming that every possible
heat or legal-circuit route is closed would be too broad.

## 6. Final corrected ledger

### Fully verified

- Exact prescribed and mobile Hall cuts, the integral immediate-toggle LP,
  and the Bellman recursion for one common one-pass trajectory.
- Existence of cyclic point-regular balanced quotas at every individual
  fixed-window rank.
- Directed-cycle decomposition of a toggle set when both adjacent loads have
  exact point margins, and exact deletion-position regularity along such a
  trajectory.
- Universal exact-factor \(C_8\) profile \(3,n-3,3,n-3\), unique optimally
  forced short-path reversal, and all stated multidepth coupling ceilings.
- The \(\Omega(W)\) sequential depth-one move lower bound, the
  \(\Omega(m)\) persistent-slot update lower bound, and the disjoint-packing
  ceiling.
- The exact component heat identity, sharp \(4(n-1)\) Johnson floor,
  Boolean-\(E_2\) stability conversion, and quantitative no-go theorem
  (5.29).

### Not supplied by these results

- Nested compatibility of the point-regular quota families.
- A factor/trajectory satisfying \(\mathrm{CAHR}_A\).
- Higher-order Hall expansion or short supported recourse.
- A simultaneous productive packing of local \(C_8\) moves.
- A retraction from small unlabelled overload to one common labelled nested
  resolution.
- A no-go theorem for all multistep or legal-circuit heat mechanisms.

The Lane L report therefore remains a rigorous collection of reductions and
obstructions rather than a proof or disproof of cyclic alignment, MWB, or the
contiguous-OR conjecture.

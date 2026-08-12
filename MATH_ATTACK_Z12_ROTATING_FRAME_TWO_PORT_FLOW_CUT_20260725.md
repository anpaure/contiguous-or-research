# Rotating-frame two-port packets: exact state flow and the phase-age cut

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Fix

\[
n=2m+1,\qquad 1\le q\le H\le m-2,
\]

and one pair-omission source phase with omitted pair

\[
A=\{a_1,a_2\}.
\]

Let the packet contain \(p\) requests, where \(1\le p\le H\). Any
\(O(1)\) below is required to be uniform in \(H\), as in the proposed
entry-neutral seam.

The rotating-frame two-port problem has an exact integral state-network
model, but its relevant capacity cut rules out the requested
\(p+O(1)\) packet for every nontrivial same-phase packet.

1. Ordered-partition states form a directed move-to-front state graph.
   After augmenting a state by its protected two-sided \(H\)-collar, its
   used owner/support resources, and the occurrence requests already
   served, minimum realization length is a shortest path in a directed
   acyclic graph. Its node--arc matrix is totally unimodular. Common
   exposed entrance and exit labels are handled by minimizing over the
   common port pair and its allowed joint tuple of augmented lifts; the
   tuple relation records any no-reset collar coupling. There is no
   fractional integrality gap in this exact, though exponential,
   formulation.
2. In the switched realization of a phase-\(A\), depth-\(q\)
   owner-fixed spike, an actual coordinate of \(A\) first enters exactly
   \(q\) owner transitions after the designated owner. Physicality through
   depth \(H\) keeps it present for at least \(H\) consecutive owners.
   Every other designated phase-\(A\) owner, and all of its upper flags
   below \(q\), avoid \(A\). Hence two switched starts obey

   \[
   \boxed{t'-t\ge H+q.}
   \tag{0.1}
   \]

3. Put \(D=H+q\). On a module with \(L\) principal owner positions,
   same-phase start indicators obey the interval-capacity system

   \[
   \sum_{u=\max(0,t-D+1)}^t y_u\le1
   \qquad(0\le t<L).
   \tag{0.2}
   \]

   This interval matrix is totally unimodular, and its integral and
   fractional optima are both

   \[
   \boxed{
   \max\sum_ty_t
   =1+\left\lfloor\frac{L-1}{D}\right\rfloor
   =\left\lceil\frac LD\right\rceil.
   }
   \tag{0.3}
   \]

   Thus \(p\) requests require

   \[
   \boxed{L\ge1+(p-1)(H+q).}
   \tag{0.4}
   \]

4. A packet of length at most \(p+C\) must have

   \[
   \boxed{C\ge(p-1)(H+q-1).}
   \tag{0.5}
   \]

   Already \(p=2\) needs overhead at least \(H+q-1\); \(p=H\) needs
   \(\Omega(H^2)\) total length. The obstruction applies to the switched
   realization alone and does not use either endpoint, so common ports,
   arbitrary ports, frame orientation, helper choice, or occurrence order
   cannot remove it.
5. The \(D\)-separated age-independence family is not itself a matroid. A
   second natural compact model, selecting a mode/entrance/exit triple, has
   a determinant-two minor and is not totally unimodular. The two
   unconditional TU formulations proved here are the full state expansion
   and the one-phase interval scheduler; the latter has the exact cut
   above.

Consequently the entry-neutral same-phase rotating-frame packet requested in
DIFFUSE_COLLISION_FUSION_ATTACK_20260725.md is false, even before imposing
common entrance and exit states. A surviving constant-one route would have
to interleave different source phases globally, packetize by compatible
phase ages, or abandon canonical Pascal towers and construct literal OR
targets directly. None of those alternatives is proved here.

---

## 1. Ordered-partition exchange states

Let \(\Omega\) be the coordinate ground set. An ordered partition state is

\[
\Sigma=(C_1,\ldots,C_r),
\]

where the nonempty blocks partition \(\Omega\). For a nonempty mask \(X\),
the move-to-front update is

\[
M_X(\Sigma)
=\bigl(X,C_1\setminus X,\ldots,C_r\setminus X\bigr),
\tag{1.1}
\]

with empty blocks deleted.

For a target state

\[
\Pi=(B_1,\ldots,B_s),\qquad
U_0=\varnothing,\qquad
U_t=B_1\cup\cdots\cup B_t\quad(1\le t\le s),
\]

write

\[
D_U(\Sigma)
=\bigl(C_1\setminus U,\ldots,C_r\setminus U\bigr)
\]

after deleting empty blocks, and define

\[
t_*(\Sigma,\Pi)
=\min\{0\le t\le s:
D_{U_t}(\Sigma)=(B_{t+1},\ldots,B_s)\}.
\tag{1.2}
\]

The set is nonempty because \(U_s=\Omega\).

### Lemma 1.1 -- exact nonempty bridge distance

The minimum length of a nonempty MTF word carrying \(\Sigma\) exactly to
\(\Pi\) is

\[
\boxed{
d^+_{\rm MTF}(\Sigma,\Pi)=\max\{1,t_*(\Sigma,\Pi)\}.
}
\tag{1.3}
\]

#### Proof

After updates \(X_1,\ldots,X_k\), the leading blocks of the final state are
the nonempty last-occurrence differences

\[
X_k,\quad
X_{k-1}\setminus X_k,\quad\ldots,\quad
X_1\setminus\bigcup_{j=2}^kX_j,
\]

followed by

\[
D_{X_1\cup\cdots\cup X_k}(\Sigma).
\]

If the final state is \(\Pi\), the leading differences form a target
prefix of length \(t\le k\), so (1.2) holds and \(k\ge t_*\).
Conversely, for \(t=t_*>0\), the updates

\[
U_t,U_{t-1},\ldots,U_1
\]

produce \(\Pi\). If \(t_*=0\), then \(\Sigma=\Pi\), and updating by
\(B_1\) is a legal one-letter idempotent word. \(\square\)

## 2. Exact state-flow formulation

Let \(I=\{1,\ldots,p\}\) be the occurrence requests. For side
\(\epsilon\in\{0,1\}\), give request \(i\) a finite acceptance predicate
\(\mathsf{Serve}_i^\epsilon\) on a completed two-sided depth-\(H\) collar
and its ordered-partition state. It holds exactly when that collar realizes
the required lower-owner incidence and, respectively, the old or
occurrence-specific conjugate flag tower. The predicate may quantify over
helper choice, either bijection between omitted pairs, and local
orientation.

Let \(\mathcal E\) and \(\mathcal X\) be the allowed *exposed* entrance
and exit labels. For the seam requested in
`DIFFUSE_COLLISION_FUSION_ATTACK_20260725.md`, these labels are ordered
partition states. A genuine physical network state also contains protected
history and collar data. Write \(\pi_E,\pi_X\) for the maps from admissible
augmented endpoint states to their exposed labels. Thus the two
realizations must have the same pair

\[
(E,X)\in\mathcal E\times\mathcal X,
\]

but may use different internal collar histories projecting to that pair.
This models condition 3 of the requested seam. Condition 5, reset-free
physical concatenation, is strictly stronger: it requires the exit lift of
one packet and the entrance lift of the next to satisfy the finite
cross-boundary collar/resource compatibility relation. Equivalently, for a
black-box port type, include the complete augmented collar interface in the
exposed label and require equality of that stronger label. The state model
below supports either convention; they must not be conflated.

### Theorem 2.1 -- exact augmented-state flow

Fix \(\epsilon\), an exposed pair \((E,X)\), and an integer length bound
\(B\ge0\). An augmented physical state

\[
\widehat\Sigma=(\Sigma,\mathcal H,\mathcal U,\mathcal P,S)
\]

records:

* the current ordered partition \(\Sigma\);
* the completed two-sided depth-\(H\) collar history \(\mathcal H\): it is
  enough to retain the last \(2H+1\) principal owners together with the
  corresponding lower-incidence data;
* the already used constrained middle/lower owners and support resources
  \(\mathcal U\);
* the finite set \(\mathcal P\) of designated starts whose future collar
  is not yet complete; and
* the served request set \(S\subseteq I\).

Time-expand these states through levels \(0,\ldots,B\). For every nonempty
mask \(Y\), add a unit-cost arc to the updated state precisely when the
update is Johnson/physical through the protected history, respects all
owner and support constraints, updates pending certificates, and moves a
request into \(S\) only after its entire two-sided collar verifies the
required tower. In the unrestricted MTF relaxation, omit
\(\mathcal H,\mathcal U,\mathcal P\); its partition component changes by
\(M_Y(\Sigma)\).

Then a word of length at most \(B\), whose augmented endpoints project to
\(E\) and \(X\), serving every request exists if and only if the augmented
graph has a source--sink path of cost at most \(B\), where a supersource is
joined to all admissible augmented lifts of \(E\), initialized with
\(S=\varnothing\) and the pending data forced by the supplied left collar.
These are zero-cost initialization arcs. At the other end, zero-cost
verification arcs expose the supplied right collar, resolve every pending
certificate, and join to the supersink only when \(S=I\) and no pending
certificate remains. The corresponding unit-flow formulation is integral
and has a totally unimodular constraint matrix.

For fixed augmented endpoint lifts \((\widehat E,\widehat X)\), let
\(\ell_\epsilon(\widehat E,\widehat X)\) be the corresponding shortest
charged path length, with value \(+\infty\) when no path exists. Let
\(\widehat{\mathcal L}_\epsilon(E,X)\) be the set
of admissible lift pairs for side \(\epsilon\). Finally, let

\[
\mathfrak C(E,X)\subseteq
\widehat{\mathcal L}_0(E,X)\times
\widehat{\mathcal L}_1(E,X)
\]

be the allowed joint four-lift relation. It is the full product when only
the common ordered-partition labels of condition 3 are imposed; it is a
diagonal or, more generally, a prescribed collar-compatibility relation
when common surroundings or condition 5 couple the two sides.
Every minimum over an empty relation is understood as \(+\infty\).

Two words satisfying the selected common-port convention and individual
length bound \(B\) exist if and only if

\[
\boxed{
\min_{(E,X)\in\mathcal E\times\mathcal X}
\ \min_{((\widehat E_0,\widehat X_0),
          (\widehat E_1,\widehat X_1))\in\mathfrak C(E,X)}
\max_{\epsilon\in\{0,1\}}
\ell_\epsilon(\widehat E_\epsilon,\widehat X_\epsilon)
\le B.
}
\tag{2.2}
\]

For a sequence of packets, enlarge the superstate by the chosen side and
collar type, and join a preceding exit lift to a following entrance lift
only across the prescribed cross-boundary compatibility relation. If
packet bits must remain independently switchable, impose this relation for
every allowed adjacent alternative pair. The result is again a directed
state-flow network, and its incidence matrix remains totally unimodular.

#### Proof

The augmentation records all history and resources on which legality
depends. Reading a physical word one update at a time gives a path, and
reading the arc labels of a path gives the word. Thus the correspondence is
exact, including incidental service of several requests at one visited
state.

The flow equations use a directed node--arc incidence matrix, which is
totally unimodular. Integral supply one therefore has an integral extreme
optimum. Enumerating the finite exposed pair and its allowed joint lift
tuples gives (2.2). \(\square\)

Theorem 2.1 settles formal integrality but is exponential and does not
imply a short route. For a prescribed occurrence order, and when bridge
interiors serve no additional requests, the unrestricted MTF graph may be
compressed to layers with arc cost (1.3). That bare graph is only a
relaxation: it may use lazy, non-Johnson, or short-residence bridges. The
phase-age cut below holds in every exact physical augmented-state network
and is independent of all port restrictions.

### Proposition 2.2 -- the natural compact port matrix is not TU

Suppose one tries to avoid the state expansion by variables
\(z_{i,e,x}\), selecting a mode \(i\), entrance label \(e\), and exit
label \(x\), with separate module, entrance, and exit marginal equations.
The resulting three-index incidence matrix is not totally unimodular.

Indeed, take the four columns

\[
(1,a,c),\quad(1,b,d),\quad(2,a,d),\quad(2,b,c)
\]

and the four rows

\[
\text{module }1,\quad
\text{entrance }a,\quad
\text{entrance }b,\quad
\text{exit }c.
\]

The induced matrix is

\[
\begin{pmatrix}
1&1&0&0\\
1&0&1&0\\
0&1&0&1\\
1&0&0&1
\end{pmatrix},
\]

whose determinant is \(-2\).

Equivalently, let mode \(1\) allow the diagonal port pairs
\((a,c),(b,d)\), and mode \(2\) allow the anti-diagonal pairs
\((a,d),(b,c)\). Assigning \(1/2\) to all four triples satisfies the
separate marginals, but no integral common port pair exists. Thus common
entrance and exit marginals are insufficient; the joint port pair must be
retained or enumerated.

---

## 3. The phase-residence invariant

Let

\[
X_0,X_1,\ldots,X_{L-1}\in\binom{[n]}m
\]

be the principal middle-owner path of a proposed switched realization.
For every valid start \(t\), define

\[
L_h(t)=\bigcap_{j=0}^hX_{t+j},
\qquad
U_h(t)=\bigcup_{j=0}^hX_{t+j}.
\tag{3.1}
\]

The path is physical through depth \(H\) when

\[
|L_h(t)|=m-h,\qquad |U_h(t)|=m+h
\tag{3.2}
\]

for every \(1\le h\le H\) and every valid start.

### Lemma 3.1 -- minimum coordinate residence

Suppose coordinate \(a\) enters at

\[
X_{r-1}\longrightarrow X_r
\]

and \(X_{r+s}\) is the first later owner not containing \(a\). Then

\[
\boxed{s\ge H.}
\tag{3.3}
\]

If a construction explicitly assumes residence strictly greater than
\(H\), then \(s\ge H+1\).

#### Proof

If \(s<H\), inspect

\[
X_{r-1},X_r,\ldots,X_{r+s},
\]

which has \(s+1\le H\) transitions. Coordinate \(a\) both enters and
leaves, and was not in the initial owner. At most \(s\) of the
\(s+1\) departures can therefore remove coordinates of \(X_{r-1}\).
The full intersection has size at least \(m-s\), whereas (3.2) requires
\(m-(s+1)\), a contradiction. \(\square\)

### Lemma 3.2 -- forced phase-coordinate entrance

Take an owner-fixed upper spike from source phase \(A\), distinguished at
depth \(q\). Its helper conjugacy fixes the central owner and every upper
flag below \(q\). The old source row avoids \(A\), while its switched
depth-\(q\) flag replaces the entering marker \(b_i\) by one coordinate
\(a(i)\in A\).

If the switched tower is realized at principal start \(t\), then

\[
X_t,\ldots,X_{t+q-1}\text{ avoid }A,
\]

and

\[
\boxed{a(i)\in X_{t+q}\setminus X_{t+q-1}.}
\tag{3.4}
\]

#### Proof

For \(h<q\), the realized union \(U_h(t)\) is the old phase-\(A\) flag
and avoids \(A\). At \(h=q\), the switched union meets \(A\) in exactly
\(a(i)\). Hence this coordinate first appears in the last owner of the
window. \(\square\)

### Theorem 3.3 -- same-phase age separation

Let \(t<t'\) be two switched owner-fixed spike starts from the same source
phase \(A\) and the same distinguished depth \(q\), on one path physical
through depth \(H\). Then

\[
\boxed{t'-t\ge H+q.}
\tag{3.5}
\]

If residence strictly greater than \(H\) is an explicit hypothesis, replace
the right side by \(H+q+1\).

#### Proof

Let \(a\in A\) be the coordinate forced by the first spike. It enters at
\(X_{t+q}\).

If \(0<t'-t<q\), put \(h=q-(t'-t)\). Then
\(1\le h<q\), and the next spike's upper depth-\(h\) window contains
\(X_{t+q}\), hence contains \(a\). But every upper flag below \(q\) of
the next spike is an old phase-\(A\) flag and avoids \(A\).

If \(q\le t'-t<q+H\), Lemma 3.1 keeps \(a\) in \(X_{t'}\). The next
designated central owner is fixed from the phase-\(A\) source row and
avoids \(A\). Both cases are impossible. \(\square\)

This proof permits arbitrary helpers, either bijection between omitted
pairs, arbitrary occurrence ordering, arbitrary rotating-frame names, and
arbitrary entrance and exit states. It follows the actual trace

\[
t\longmapsto X_t\cap A,
\]

which no relabelling of the current frame changes.

---

## 4. Exact age-only TU scheduler and its dual cut

Put

\[
D=H+q.
\]

For principal positions \(0,\ldots,L-1\), let \(y_t=1\) when \(t\) is a
designated switched phase-\(A\), depth-\(q\) start. Every physical start
vector satisfies

\[
\sum_{u=\max(0,t-D+1)}^t y_u\le1
\tag{4.1}
\]

for \(0\le t<L\). These are the consecutive length-\(D\) windows ending
at \(t\), truncated only at the left boundary. They exactly describe the
binary \(D\)-separation condition. They are not claimed sufficient for
realization of the corresponding physical towers.

### Theorem 4.1 -- exact integral age-only scheduler

The polytope

\[
\mathcal P_{L,D}
=\{y\in\mathbb R_{\ge0}^L:Ay\le\mathbf1\},
\tag{4.2}
\]

where \(A\) is the interval matrix in (4.1), is integral. It is the exact
age-only scheduler, and every physical start schedule projects into it.
Its integral points are exactly the \(D\)-separated start sets, and

\[
\boxed{
\max_{y\in\mathcal P_{L,D}}\mathbf1^Ty
=\left\lceil\frac LD\right\rceil
=1+\left\lfloor\frac{L-1}{D}\right\rfloor.
}
\tag{4.3}
\]

The dual optimum is an integral cover of the position line by
\(\lceil L/D\rceil\) disjoint consecutive cliques of diameter less than
\(D\).

#### Proof

Order the window rows by their right endpoint \(t\). In every column, the
rows containing that column are consecutive. For any subset of rows, assign
alternating signs in their induced order. In each column the signed sum is
\(0,1\), or \(-1\). The Ghouila-Houri criterion proves that \(A\) is
totally unimodular. Appending nonnegativity constraints preserves
integrality for the integer right-hand side.

Every integral point satisfies (4.1), hence selected positions are pairwise
at distance at least \(D\); the converse is immediate. The starts

\[
0,D,2D,\ldots
\]

give \(\lceil L/D\rceil\) positions. Conversely, consecutive selected
positions differ by at least \(D\), giving the same upper bound.

For the LP dual, take the rows whose right endpoints are

\[
L-1,\ L-1-D,\ L-1-2D,\ldots
\]

until the index becomes negative. Their possibly left-truncated windows
are disjoint, cover all positions, and number \(\lceil L/D\rceil\). Giving
these rows dual weight one matches the primal construction. \(\square\)

There is also a literal network-matrix form. Put

\[
Y_t=\sum_{u=0}^t y_u,\qquad Y_s=0\quad(s<0).
\]

Then (4.1) and nonnegativity become

\[
Y_t-Y_{t-D}\le1,
\qquad
Y_{t-1}-Y_t\le0.
\tag{4.4}
\]

Every row is a signed incidence vector of an arc in a graph on the prefix
nodes, so this difference-constraint matrix is totally unimodular.
Summing the first inequalities at
\(t=L-1,L-1-D,L-1-2D,\ldots\) telescopes to

\[
Y_{L-1}=\sum_ty_t\le\left\lceil\frac LD\right\rceil.
\tag{4.5}
\]

This is the explicit integral LP-dual/capacity-cut certificate in the
necessary age projection of the exact state flow. Pulling it back to the
augmented network shows that no length-\(L\) target node can have served
more than \(\lceil L/D\rceil\) requests from this phase/depth stratum. It
is not asserted to be a literal max-flow min-cut equality for the full
physical network. A \(D\)-separated binary vector need not extend to
compatible Boolean owners, collars, or support resources.

### Corollary 4.2 -- packet length and overhead cut

A physical module containing \(p\ge1\) switched requests from one
phase/depth stratum has

\[
\boxed{L\ge1+(p-1)(H+q).}
\tag{4.6}
\]

If its literal length is at most \(p+C\), then necessarily

\[
\boxed{C\ge(p-1)(H+q-1).}
\tag{4.7}
\]

Under an explicit strict-residence hypothesis these become

\[
L\ge1+(p-1)(H+q+1),
\qquad
C\ge(p-1)(H+q).
\tag{4.8}
\]

#### Proof

The condition \(p\le\lceil L/(H+q)\rceil\) from Theorem 4.1 is equivalent
to (4.6). Moving between consecutive principal owners consumes a new
physical update position. Common initialization can alter only an outside
endpoint term and cannot shorten this internal span. Subtracting \(p\)
gives (4.7). The strict version is identical. \(\square\)

This is the requested cut obstruction. It already occurs in the fractional
relaxation of the complete ordered-state flow. There is no rounding loss
for total unimodularity to remove.

### Proposition 4.3 -- no matroid augmentation route

For \(D\ge2\) and \(L\ge D+1\), the family of \(D\)-separated subsets of
\(\{0,\ldots,L-1\}\) is not a matroid.

#### Proof

Both

\[
P=\{0,D\},\qquad Q=\{D-1\}
\]

are feasible, and \(|P|>|Q|\). Neither element of \(P\setminus Q\) can
be added to \(Q\): its distance from \(D-1\) is \(D-1\) or \(1\), both
less than \(D\). This violates matroid augmentation. \(\square\)

---

## 5. Physical run splitting cannot repair the cut

Suppose \(p\) requests are divided among \(r\) separately literalized,
nonempty physical runs, with \(p_j\) requests in run \(j\). The phase-age
cut gives

\[
L_j\ge1+(p_j-1)D.
\]

Summing,

\[
\sum_{j=1}^rL_j
\ge r+(p-r)D.
\tag{5.1}
\]

Under the standard separately literalized two-sided radius-\(H\)
convention, a run of \(L_j\) principal owners supplies \(H\) collar
positions on each side and has literal length \(L_j+2H\). Therefore every
fully paid split realization has length at least

\[
\boxed{
r+(p-r)D+2Hr
=pD+r(2H+1-D).
}
\tag{5.2}
\]

This fully paid formula is stronger than needed for a two-port lower
bound. Grant, in the packet's favour, one entire outer \(2H\)-collar for
free from the common ports. The charged length still obeys

\[
\begin{aligned}
\ell_{\rm ch}
&\ge r+(p-r)D+2H(r-1)\\
&=1+(p-1)D+(r-1)(H-q+1).
\end{aligned}
\tag{5.3}
\]

Consequently

\[
\boxed{
C\ge(p-1)(H+q-1)+(r-1)(H-q+1).
}
\tag{5.4}
\]

For the unconditional \(D=H+q\),

\[
2H+1-D=H-q+1\ge1.
\]

For strict residence \(D=H+q+1\),

\[
2H+1-D=H-q\ge0,
\]

with equality only at \(q=H\). In the favourable one-free-collar
accounting, the strict-residence version of (5.4) is

\[
C\ge(p-1)(H+q)+(r-1)(H-q).
\tag{5.5}
\]

Thus splitting never improves the lower bound, even after common ports pay
one entire collar; generically it makes the bound strictly worse. The
physical run penalty strengthens rather than repairs the phase-age cut.

---

## 6. The obstruction occurs on genuine rainbow packets

The separation theorem would be logically enough to refute a universal
packet compiler once a two-request packet is presented. The following
count shows that packets of the full requested size \(H\) actually occur
inside every sufficiently large local exact omitted-pair phase.

### Proposition 6.1 -- collision-fibre lower bound

Fix a source phase \(A\), and view its local exact row factor on
\(Q_A=[n]\setminus A\) as the actual lower-saturating, middle-simple phase
token matching. Assume, as in the pair-omission construction, that it uses
every middle owner once and supplies the complete physical depth-\(H\)
flag tower at every occurrence. At depth \(q\), put

\[
M=\binom{2m-1}{m},\qquad
N_q=\binom{2m-1}{m+q},\qquad
R_q=\binom{m+q}{m}.
\tag{6.1}
\]

If \(c_q\) is the number of upper depth-\(q\) target fibres having load
at least two, then

\[
\boxed{
c_q\ge\frac{M-N_q}{R_q-1}
\ge\frac{2^{m-q-1}}{m(m+1)}.
}
\tag{6.2}
\]

Consequently, if

\[
2^{m-H-1}\ge Hm(m+1),
\tag{6.3}
\]

then every depth \(1\le q\le H\) has at least \(H\) distinct collision
fibres in that local row factor. Selecting one occurrence from each of any
\(H\) such fibres gives a genuine *local-row* rainbow packet of \(H\)
legal owner-fixed spikes.

#### Proof

There are \(M\) owner occurrences and only \(N_q\) possible upper targets.
For a fixed upper target \(U\), every owner mapping to it is an \(m\)-subset
of \(U\), so the fibre load is at most \(R_q\). A noncollision target has
load at most one. Therefore

\[
M\le (N_q-c_q)+c_qR_q
=N_q+c_q(R_q-1),
\]

which proves the first inequality in (6.2). Since \(q\ge1\),

\[
N_q\le N_1=M\frac{m-1}{m+1},
\qquad
M\ge\frac{2^{2m-2}}m,
\qquad
R_q\le2^{m+q}.
\]

Here the middle inequality follows because \(M\) is a largest coefficient
among the \(2m\) binomial coefficients of order \(2m-1\). Substitution
gives the second inequality in (6.2). For \(q\le H\), (6.3) makes its
right side at least \(H\). Distinct fibres contain distinct occurrences,
and the owner-fixed helper exists because \(H\le m-2\). \(\square\)

For every fixed \(A_0<\infty\), condition (6.3) holds for all sufficiently
large \(m\), uniformly for \(H\le A_0\sqrt m\). Thus the obstruction is
nonvacuous throughout every fixed Gaussian window. This count does **not**
bound the fibre loads by a separately prescribed constant \(K\). It
therefore refutes the unrestricted same-phase rainbow-packet compiler, but
does not by itself produce a counterexample whose every selected fibre lies
in a bounded-load-only subfamily. Nor does the count alone prove that a
specified later global lower-perfect phase matching retains those same
occurrences; that survival is an additional global-selection question.

---

## 7. Common ports cannot cross the cut

The common entrance/exit condition couples only the endpoints of the two
integral paths in Theorem 2.1. The phase-age cut concerns internal
designated starts of the switched path and was proved without mentioning
either endpoint. Consequently:

* choosing the best common port pair cannot change (4.6);
* allowing unrelated old and switched ports cannot change (4.6);
* padding the state graph with additional frame orientations cannot change
  (4.6);
* choosing between \(a_1\) and \(a_2\) at each spike cannot double
  capacity, because the next phase-\(A\) central owner avoids both;
* shifted Gray cuts preserve actual coordinate residence and cannot cross
  the cut.

A theorem uniform in \(H\), valid for every packet of size at most \(H\),
already fails on \(p=2\):

\[
|R^1|\ge H+q+1,
\]

whereas the requested form is \(2+O(1)\). At \(p=H\),

\[
|R^1|\ge1+(H-1)(H+q)=\Omega(H^2).
\tag{7.1}
\]

The common-port network is integral but infeasible at the requested budget.
This is a cut failure, not a fractional selection or matching failure.

---

## 8. Exact proved boundary

### Proved

1. Ordered-state selection has the exact augmented-state shortest-flow
   formulation of Theorem 2.1. It is integral but exponential. Projected
   common ordered ports model the single-packet condition; no-reset packet
   concatenation additionally uses common augmented interfaces or the
   explicit collar-compatibility relation.
2. The natural compact three-index port matrix is not TU; separate entrance
   and exit marginals do not enforce a common port pair.
3. Same-phase, same-depth switched spikes are separated by \(H+q\), for
   arbitrary rotating frames and arbitrary ports.
4. The interval-capacity relaxation is integral and has exact optimum
   \(\lceil L/(H+q)\rceil\).
5. Minimum overhead is at least
   \((p-1)(H+q-1)\), and separately literalized runs cannot lower it.
6. The direct \(D\)-separated age-independence family is not a matroid.
   Its correct positive structure is an interval-network polytope whose
   dual supplies the obstruction. This does not rule out every extended
   matroid-intersection formulation for a more structured physical
   subfamily.
7. Proposition 6.1 supplies \(H\) distinct collision fibres in every full
   local phase throughout fixed Gaussian windows for all large \(m\). It
   does not supply bounded fibre loads or survival through a later global
   phase selection.

### Not proved or not ruled out

1. A global scheduler may interleave useful requests from different source
   phases during forced residence intervals. Its constraint matrix is not
   the one-phase interval matrix analyzed here.
2. An age-compatible rainbow theorem might packetize collision occurrences
   according to a global physical chronology rather than compile arbitrary
   rainbow bins afterward.
3. A direct contiguous-OR crossing word might realize the target without
   using it as the canonical union of \(q+1\) consecutive principal owners.
   Such a construction needs a new proof of lower ownership, middle
   injectivity, and literal length.
4. No constant-one theorem follows.

The independent same-phase rotating-frame packet lane is closed. The
remaining non-tautological network problem is a global cross-phase
phase-age scheduler, not a two-port compiler for arbitrary abstract
rainbow packets.

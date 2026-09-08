# The graph absorber is a positive-resident lower-rainbow packet; fusion, not dual residence, is its physical gate

**Date:** 2026-08-13  
**Inputs:**
`MATH_AUDIT_GRAPH_STAR_CYCLE_ONE_OWNER_ABSORBER_AND_TICKET_SCOPE_20260813.md`,
the exact flat-antecedent theorem, and the protected Middle-Levels factor
theorems.  
**Status:** unconditional local promotion with an exact conditional host
theorem.  The final run-safe fusion and exterior upper-backup hypotheses are
not constructed here.

## 1. Setup

Use the graph absorber notation

\[
 |D|=R-2q,\qquad |V|=2q+2,\qquad
 \Omega(ab)=D\cup(V\setminus\{a,b\}).                 \tag{1.1}
\]

There is a graph `S` with one distinguished edge `uv` such that

\[
 S=G\sqcup\{uv\},                                    \tag{1.2}
\]

`S` is the edge-disjoint union of `q+1` copies of
`K_(1,q+1)`, and `G` is the edge-disjoint union of `q` copies of
`C_(q+2)`.  In the short graph-to-owner realization, a star or cycle piece
is read in its natural cyclic order, and its owner row is the image under
`Omega` of its cyclic edge list.

The owner identity and its composition with the special conformal macro are
already exact.  The purpose of this note is to identify the least physical
conditions under which this local identity may be used.

## 2. Only positive residence is needed for flat inversion

Let `d=q-1`.  For a cyclic binary owner trace `t`, define its maximal
depth-`d` erosion by

\[
 a_i=\bigwedge_{j=0}^{d}t_{i-j}.                     \tag{2.1}
\]

The standard cyclic sliding-OR inverse criterion says

\[
 \bigvee_{j=0}^{d}a_{i+j}=t_i\quad\text{for every }i  \tag{2.2}
\]

if and only if every nonconstant positive run of `t` has length at least
`d+1=q`.  No lower bound on a zero gap occurs in this criterion.

### Lemma 2.1 (minimal residence of the short absorber)

Every short star and cycle component of the graph absorber satisfies the
cyclic flat-antecedent criterion at depth `d=q-1`.

#### Proof

In a period-`q+1` star rail, every active coordinate has trace
`1^q 0`; in a period-`q+2` cycle rail it has trace `1^q 0^2`.
Core coordinates are constantly one and unused coordinates constantly zero.
Thus every nonconstant positive run has length exactly `q`, and (2.2)
applies coordinatewise. \(\square\)

The zero gaps of lengths one and two therefore do **not** prevent literal
source inversion.  They prevent a stronger dual/complement-residence claim
and remove most freedom to cut or splice the cycles.  Those are later
robustness issues, not local flat-inversion failures.

## 3. Exact lower-rainbow and upper-support ledgers

For adjacent graph edges `xy,yz`, the immediate turn values are

\[
 L(x,y,z)=D\cup(V\setminus\{x,y,z\}),\qquad
 U(y)=D\cup(V\setminus\{y\}).                       \tag{3.1}
\]

### Lemma 3.1 (aggregate lower simplicity)

On either shore separately, every immediate-lower value is used at most
once.

#### Proof

The lower value determines the unordered triple `{x,y,z}`.  Two different
wedges on the same triple have two different centres and hence share one of
the three graph edges.  The star pieces on the `S` shore, and the cycle
pieces on the `G` shore, are edge-disjoint decompositions.  Thus two such
wedges cannot occur in different pieces.  Inside one simple star or simple
cycle, the cyclic wedge is recovered uniquely, up to reversing the same
occurrence. \(\square\)

Thus suppressing the lower turns gives a simple Johnson cycle bank, and its
incidence lift is a properly phased degree-two protected Middle-Levels bank.

Immediate-upper simplicity is not true.  A star centred at `x` contributes

\[
 (q+1)e_{D\cup(V\setminus\{x\})}.                   \tag{3.2}
\]

For a cycle decomposition of `G`, the multiplicity of the upper value
`U(y)` is

\[
 \frac{\deg_G(y)}2,                                 \tag{3.3}
\]

because every cycle containing `y` supplies one turn centred there.
Consequently the complete set of upper values touched by either shore is
contained in

\[
 \mathcal U_{D,V}:=
 \{D\cup(V\setminus\{y\}):y\in V\},
 \qquad |\mathcal U_{D,V}|=2q+2.                    \tag{3.4}
\]

This distinction is useful: the absorber has `Theta(q^2)` upper
**occurrences**, but only `O(q)` named immediate-upper values.

## 4. Protected-host promotion

Call an exterior upper bank `W_up` an **absorber backup** if every named
upper target which loses its designated occurrence when the absorber state
is changed has a protected occurrence outside the absorber.  In particular,
for the immediate row it is enough to back up the subset of
`mathcal U_(D,V)` which was designated before the change.  Repeated internal
upper occurrences may simply be left undesignated: a universal OR word
needs a witness, not injectivity of the complete upper-occurrence row.

For a linearized protected bank, call its splices **run-safe** if every
positive owner run made internal by the splices has length at least `q`.
Equivalently, the concatenated owner chronology passes the exact
flat-antecedent residence test.  This is an occurrence condition and is
stronger than existence of an abstract two-factor.

### Theorem 4.1 (minimal protected-host theorem)

Fix one state of the short graph absorber.  Suppose:

1. its incidence-cycle bank is contained, with its alternating phase, in a
   spanning Middle-Levels two-factor;
2. the selected opening and fusion of that factor are run-safe;
3. every affected upper witness has an absorber backup, and every wider
   upper witness cut by the fusion has either a disjoint old occurrence or
   a protected new crossing occurrence;
4. all lower pins and common-cap claims use the literal occurrence addresses
   of the terminal factor, and their joint compiler is feasible.

Then the graph-absorber state is a valid positive-resident,
lower-rainbow protected partial Shadow--Braid packet.  Replacing it by the
other graph state preserves the owner identity and remains valid under the
same four hypotheses for that state.

#### Proof

The graph identity supplies the exact owner shore.  Lemma 3.1 supplies a
simple immediate-lower row, and the occurrence-lift theorem gives each
selected incidence its literal lower turn, adjacent owner halfport, and
alternating phase.  Lemma 2.1 plus run-safe fusion gives the exact
depth-`d` antecedent.  Hypothesis 3 is precisely the witness-survival
condition for every upper target; no injectivity of unused upper occurrences
is needed.  Hypothesis 4 supplies the remaining lower/common-cap rows.
These are the owner, residence, upper, and compiler clauses of the fixed
Shadow--Braid theorem. \(\square\)

This theorem is deliberately conditional only where occurrence-level data
are genuinely needed.  Neither dual residence nor an injective complete
immediate-upper row is among its hypotheses.

## 5. Factor extension is not the live obstruction

For one absorber shore the protected incidence bank has

\[
 e=2(q+1)^2=O(q^2)=2^{o(m)}
 \quad\text{on the star shore},                    \tag{5.1}
\]

and `2q(q+2)` incidences on the cycle shore.  Every protected lower and
upper incidence vertex has degree two.

### Lemma 5.1 (exact exposure bounds)

For either shore, in the notation of the subexponential low-exposure
protected-factor theorem,

\[
 \boxed{\alpha\le3,\qquad \beta\le2q.}              \tag{5.2}
\]

#### Proof

Let `P` be the incidence lift of one shore.  Its saturated lower vertices
are precisely the immediate-lower values in Lemma 3.1, and each has degree
two.  Every protected lower value is `D` together with `2q-1` points of
`V`.  If a rank-`R` upper owner contains one, then it contains `D`; write it
as `D union Y`, `|Y|=2q`.  Every protected lower facet contained in it is
then `D union (Y-{y})` for some `y in Y`.  There are at most `2q` such
facets.  Thus `beta<=2q`.

For `alpha`, fix an unprotected lower vertex `L_0`.  A protected upper owner
containing it is one of the graph owners `Omega(e)`.  If `L_0` contains a
point outside `D union V`, there are no such owners.  Put

\[
 a=|D\setminus L_0|.
\]

Since `|L_0|=|D|+2q-1`, containment in an `Omega(e)` forces `a<=1`.
If `a=0`, write `L_0=D union X`, `|X|=2q-1`.  Containment says

\[
 X\subseteq V\setminus e.                          \tag{5.3}
\]

The three omitted points `V-X` contain `e`, giving at most
`binom(3,2)=3` possibilities.  If `a=1`, then `|L_0 cap V|=2q`; its
two-point complement in `V` forces `e` uniquely.  Hence `alpha<=3`.
\(\square\)

Consequently, for the central regime `q=O(sqrt(m))`,

\[
 e=2^{o(m)},\qquad \alpha,\beta=o(m).               \tag{5.4}
\]

The subexponential low-exposure theorem therefore applies unconditionally
to either **already constructed phased incidence-cycle shore**: for all
sufficiently large `m`, it is contained in a spanning ordered two-SDR which
retains every protected phase.

Even after factor extension, the protected cycles remain saturated factor
components.  The factor theorem does not open or join them.  Hence the live
chronological row is the run-safe fusion premise in Theorem 4.1.

## 6. Exact cut audit

There is no nontrivial cut of an isolated short component which is harmless
without a collar.

### Lemma 6.1 (every isolated cut clips a threshold run)

For a period-`q+1` or period-`q+2` short absorber rail, every cut lies in
the positive run of some active coordinate.  In the opened path that run is
split into two endpoint arms whose total length is `q` but whose individual
lengths are both smaller than `q`, except when the cut is at one boundary of
that coordinate's run.

#### Proof

At every owner position of a pure rail exactly `q` active coordinates are
present.  A cut immediately after that position therefore lies inside the
positive run of each of those coordinates unless that position is its last
positive occurrence.  Only one coordinate exits at a Johnson transition,
so for `q>=2` at least `q-1` present coordinates are genuinely split.  Their
two endpoint arms are nonempty and sum to the original cyclic run length
`q`; hence both are shorter than `q`. \(square\)

Thus a short cycle cannot be opened and treated as an independently resident
path.  Its clipped arms must be paired with compatible arms of neighbouring
components.

For two oriented opened components `P,Q`, let `s_x(P)` be the terminal
one-arm and `p_x(Q)` the initial one-arm.  The seam is run-safe exactly when

\[
 s_x(P)+p_x(Q)\ge q
 \quad\text{for every }x\text{ with both seam bits }1, \tag{6.1}
\]

and every one-sided arm which is closed at the seam already has length at
least `q`.  Equation (6.1) is the exact socket-compatibility test.  The
star/cycle edge decompositions supply no theorem that their ports admit a
Hamilton path under this compatibility relation.

Indeed, using the displayed odd-`q` cycle decomposition and the most natural
cuts at the `u`-incident edges, concatenating the `q` cycles in their index
order leaves an `a_j`-positive run of length `q-2` for every `j`.  Thus even
the explicit cyclic symmetry does not provide automatic run-safe fusion.

## 7. The odd star shore has an explicit run-safe fusion

For odd `q`, the star shore itself can nevertheless be fused exactly.  Use
the notation

\[
 A=\{a_0,\ldots,a_{q-1}\},\qquad
 B_0=\{b_0,\ldots,b_{q-1}\}.                        \tag{7.1}
\]

The star at `a_j` has leaves `B_0 union {u}`, and the star at `u` has
leaves `B_0 union {v}`.  Open and concatenate their graph-edge owner lists
in the following order:

\[
 P_0,\ P_*,\ P_1,\ldots,P_{q-1},                   \tag{7.2}
\]

where

\[
\begin{aligned}
 P_0={}&(a_0b_0,a_0b_1,\ldots,a_0b_{q-1},a_0u),\\
 P_*={}&(ub_0,ub_1,\ldots,ub_{q-1},uv),             \tag{7.3}
\end{aligned}
\]

and, for `1<=j<q`,

\[
 P_j=(a_jb_{q+1-j},\ldots,a_jb_{q-1},a_ju,
       a_jb_0,\ldots,a_jb_{q-j}),                   \tag{7.4}
\]

with an empty first range when `j=1`.  Formula (7.4) is the cyclic rotation
by `q+1-j` of the common leaf order
`(b_0,...,b_(q-1),u)`.

### Theorem 7.1 (explicit odd-star resident path)

The `Omega`-image of (7.2)--(7.4) is one simple Johnson owner path of length
`(q+1)^2` which:

1. uses every owner of the odd-`q` star shore exactly once;
2. has a simple complete immediate-lower row, including its new seams; and
3. has no internal positive run shorter than `q`.

Hence the complete odd star shore has an unconditional run-safe linear
fusion and exact flat depth-`q-1` inversion.

#### Proof

The first seam joins `a_0u` to `ub_0`, and the second joins `uv` to
`a_1u`.  For `1<=j<q-1`, the last edge of `P_j` is
`a_jb_(q-j)` and the first edge of `P_(j+1)` is
`a_(j+1)b_(q-j)`.  Each pair shares exactly one graph vertex, so its
`Omega`-owners are Johnson adjacent.  All graph edges are distinct and the
star decomposition partitions `S`, proving owner simplicity and Item 1.

Internal lower triples have one of the forms

\[
 \{a_j,t,t'\},\qquad \{u,b_t,b_{t+1}\},
 \qquad \{u,b_{q-1},v\}.                            \tag{7.5}
\]

The seam triples are

\[
 \{a_0,u,b_0\},\qquad \{u,v,a_1\},\qquad
 \{a_j,b_{q-j},a_{j+1}\}\ (1<=j<q-1).             \tag{7.6}
\]

The first triple in (7.6) is precisely the deleted closing wedge of `P_0`;
the others have label-type signatures absent from (7.5).  The last family
has two `A` labels and its value of `j` is recoverable.  Thus all lower
triples, hence all literal immediate-lower values, are distinct.

It remains to check residence.  A coordinate `a_j` is zero exactly on its
own complete block `P_j`, and `v` is zero only at `uv`; neither creates a
short internal positive run.  The `u`-zeros form the terminal edge of
`P_0`, all of `P_*`, the initial edge of `P_1`, and one edge of every later
`P_j`.  Between the `u`-zero in `P_j` and that in `P_(j+1)` there are

\[
 (q-j+1)+j=q+1                                    \tag{7.7}
\]

positive owners.

Finally fix `b_t` and put `n=q+1`.  Its zero positions in `P_0,P_*` are
`t,n+t`.  In `P_j`, `1<=j<q`, its local zero position is

\[
 \ell_j(t)=(t+j)\bmod n.                            \tag{7.8}
\]

Before the unique wrap of (7.8), and after it, consecutive global zero
positions differ by `n+1`, giving a positive run of length `n=q+1`; at the
wrap they differ by one, giving no positive run.  The first pair differs by
`n`, giving a run of length `q`.  The only unchecked gap meets an endpoint
of the linear path and is clipped.  Thus every internal positive run has
length at least `q`. \(\square\)

The construction does not solve the cycle shore, and it does not make the
upper row injective.  It proves that run-safe fusion is a genuinely
state-dependent issue rather than a universal obstruction to the short
absorber.  The cycle-side task remains the exact paired-orientation port
problem (6.1); common graph vertices alone do not certify that inequality.

### Theorem 7.2 (explicit even-star resident path)

For even `q`, use the star decomposition from the graph absorber.  Thus the
stars at `a_j`, `0<=j<q`, have common leaf set `B_0 union {v}`, and the last
star at `u` has leaf set `A union {v}`.  Put

\[
 L=(b_0,b_1,\ldots,b_{q-1},v),\qquad n=q+1.         \tag{7.9}
\]

Let `P_0` use the leaf order `L`.  For `1<=j<q`, let `P_j` use the cyclic
rotation of `L` beginning at position `n-j`.  Finally use

\[
 P_*=(ua_{q-1},ua_{q-2},\ldots,ua_0,uv).            \tag{7.10}
\]

Then

\[
 P_0,P_1,\ldots,P_{q-1},P_*                        \tag{7.11}
\]

is a simple Johnson owner path through every even-star-shore owner exactly
once.  Its complete immediate-lower row is simple, and every internal
positive run has length at least `q`.

#### Proof

The first seam is `a_0v,a_1v`.  For `1<=j<q-1`, `P_j` ends at
`a_jb_(q-j)` and `P_(j+1)` begins at `a_(j+1)b_(q-j)`.  The last `a`-block
ends at `a_(q-1)b_1`, and `P_*` begins at `ua_(q-1)`.  Thus all seams are
Johnson adjacencies.  The graph star decomposition is edge-disjoint, so the
owners are simple.

Internal lower triples have one star centre.  Seam triples are

\[
 \{a_0,a_1,v\},\quad
 \{a_j,a_{j+1},b_{q-j}\}\ (1<=j<q-1),\quad
 \{a_{q-1},b_1,u\}.                                \tag{7.12}
\]

Their label-type signatures and indices distinguish them from each other
and from every internal wedge.  Hence the lower row is simple.

For residence, every `a_j` has one full zero block `P_j` and one singleton
zero in `P_*`.  These are adjacent for `j=q-1`; for every other `j`, the
positive run between them has length at least `q+2`, while the other arm is
clipped at a path endpoint.  For `b_t`, its zero position in block `P_j` is

\[
 jn+((t+j)\bmod n).                                 \tag{7.13}
\]

Successive positions differ by `n+1`, except once when they differ by one.
Thus every internal positive run has length `n=q+1` or is empty.  The
`u`-zeros are the terminal full block `P_*`.  The `v`-zero positions first
coalesce across the `P_0|P_1` seam, then differ by `n+1`, and the final gap
to `uv` has length `n+2`; their positive runs are therefore at least `q`.
This covers all coordinates. \(\square\)

Theorems 7.1--7.2 close run-safe fusion for the star shore in both parities.
Only the cycle shore remains.

## 8. Exact arm matching for the cycle shore

The cycle-side socket problem has a useful exact finite form.  Let

\[
 P=(p_0,p_1,\ldots,p_{n-1}),\qquad
 Q=(r_0,r_1,\ldots,r_{n-1}),\qquad n=q+2,          \tag{8.1}
\]

be vertex orders for two opened simple graph cycles.  Thus the graph-edge
owner lists are

\[
 p_0p_1,p_1p_2,\ldots,p_{n-1}p_0
 \quad\hbox{and}\quad
 r_0r_1,r_1r_2,\ldots,r_{n-1}r_0.                 \tag{8.2}
\]

For a graph vertex `x`, define

\[
s_P(x)=
\begin{cases}
n,&x\notin V(P),\\
0,&x=p_0\text{ or }p_{n-1},\\
n-i-1,&x=p_i,\ 1\le i\le n-2,
\end{cases}                                      \tag{8.3}
\]

and

\[
p_Q(x)=
\begin{cases}
n,&x\notin V(Q),\\
0,&x=r_0\text{ or }r_1,\\
i-1,&x=r_i,\ 2\le i\le n-1.
\end{cases}                                      \tag{8.4}
\]

These are respectively the terminal and initial positive-arm lengths of
the coordinate `x` in the `Omega`-owner words.

### Lemma 8.1 (exact arm-matching criterion)

Suppose the last graph edge `p_(n-1)p_0` and first graph edge `r_0r_1`
meet in exactly one vertex.  Their `Omega`-owners form a run-safe Johnson
seam if and only if, for every graph vertex `x`,

\[
\begin{array}{ll}
s_P(x)+p_Q(x)\ge q,
 &x\notin\{p_{n-1},p_0,r_0,r_1\},\\
s_P(x)\ge q,
 &x\notin\{p_{n-1},p_0\},\ x\in\{r_0,r_1\},\\
p_Q(x)\ge q,
 &x\in\{p_{n-1},p_0\},\ x\notin\{r_0,r_1\}.
\end{array}                                      \tag{8.5}
\]

There is no condition when the coordinate is zero on both sides of the
seam.

In particular, write the seam graph edges as `{x,y}` and `{y,z}`.

1. If `z` occurs in `P`, then `z=p_1`; otherwise `z` is absent from `P`.
2. If `x` occurs in `Q`, then `x=r_(n-1)`; otherwise `x` is absent from
   `Q`.
3. If a vertex `w` occurs as `p_i=r_j`, with `1<=i<=n-2` and
   `2<=j<=n-1`, and is positive on both seam owners, then its two-sided
   condition is exactly `j>=i`.

#### Proof

A graph vertex is absent from exactly the two consecutive `Omega`-owners
corresponding to its two incident cycle edges; if it is not a vertex of the
cycle, it is present throughout the component.  This gives (8.3)--(8.4).
Closing a positive arm against a zero requires that arm itself to have
length at least `q`; joining two positive arms requires their sum to have
length at least `q`.  This proves (8.5).

For Item 1, `z` is positive in the last owner of `P` and zero in the first
owner of `Q`.  If `z=p_i`, then (8.3) must be at least `q=n-2`, forcing
`i=1`.  Item 2 is the reversed statement.  In Item 3, (8.5) reads

\[
 (n-i-1)+(j-1)\ge n-2,
\]

which is precisely `j>=i`. \(\square\)

Thus the odd-cycle fusion is an order-preserving arm-matching problem, not
merely an edge-intersection problem.

### Proposition 8.2 (the natural `u` ports of the odd cycles never mate)

Let `q=2h+1` and let `Gamma_j` be the explicit odd cycle

\[
 (u,a_j,b_{j+h},a_{j+1},b_{j+h-1},\ldots,a_{j+h},b_j,u).
                                                               \tag{8.6}
\]

Open two distinct cycles `Gamma_i,Gamma_j` between their two `u`-incident
edges, in arbitrary orientations.  No concatenation of the two opened
cycles is run-safe.

#### Proof

The non-`u` vertex set of `Gamma_i` is

\[
 \{a_t,b_t:t\in I_i\},\qquad
 I_i=\{i,i+1,\ldots,i+h\}\subseteq\mathbb Z_q.    \tag{8.7}
\]

At a `u`-opening, the unique noncommon endpoint of the outgoing edge is
either `a_i` or `b_i`; the unique noncommon endpoint of the incoming edge
of `Gamma_j` is either `a_j` or `b_j`.  At a `u`-opening, the start centre
of `Gamma_i` is the other endpoint of its first `u`-edge, and the end centre
of `Gamma_j` is the other endpoint of its last `u`-edge.  The two endpoints
of a given `Gamma_t` have different label types (`a_t` and `b_t`).  Hence
the outgoing endpoint of `Gamma_i` cannot equal its own start centre, and
the incoming endpoint of `Gamma_j` cannot equal its own end centre.

By Items 1--2 of Lemma 8.1, the incoming endpoint of `Gamma_j` must
therefore be absent from `Gamma_i`, and the outgoing endpoint of `Gamma_i`
must be absent from `Gamma_j`.  Since both label types of index `t` occur
in a cycle exactly when `t` lies in its interval `I`, run safety requires
simultaneously

\[
 j\notin I_i\qquad\hbox{and}\qquad i\notin I_j.    \tag{8.8}
\]

Put `d=j-i` in `Z_q`.  The first exclusion says
`d in {h+1,...,2h}`, whereas the second says
`d in {1,...,h}`.  This is impossible. \(\square\)

Hence a successful fusion of the displayed `Gamma_j` family must use
genuinely non-`u` cuts (and must route the resulting clipped `u` arms); no
ordering or orientation of the canonical `u` ports can work.

## 9. The even cycle shore has a direct resident Euler ordering

For even `q>=6`, one can avoid the Sotteau component-port problem entirely.
Put

\[
 h=(q+2)/2,\qquad A=\mathbb Z_q,
 \qquad B=\{b_{\epsilon,j}:\epsilon\in\mathbb Z_2,
                                  j\in\mathbb Z_h\}.             \tag{9.1}
\]

For a half-step `t=r+q ell`, with `r in Z_q` and `ell in Z_h`, set

\[
 A_t=a_r,\qquad
 B_t=b_{\epsilon,\,\ell+\lfloor r/2\rfloor},
 \qquad \epsilon=r\pmod2.                         \tag{9.2}
\]

Read subscripts cyclically and take the graph-edge word

\[
 A_tB_t,\ B_tA_{t+1}
 \qquad(0\le t<qh).                                \tag{9.3}
\]

### Theorem 9.1 (even-cycle resident Euler cycle)

For every even `q>=6`, (9.3) is an Euler cycle of `K_(q,q+2)`.  Its
`Omega`-image is one simple closed Johnson owner cycle which:

1. uses every owner of the even cycle shore exactly once;
2. has a simple complete immediate-lower row; and
3. has every positive coordinate run of length at least `q`.

#### Proof

Fix `b_(epsilon,j)`.  The half-steps at which it occurs are obtained by
choosing every `r congruent epsilon (mod 2)` and then the unique

\[
 \ell=j-\lfloor r/2\rfloor\pmod h.                 \tag{9.4}
\]

At that half-step (9.3) uses the two edges from `b_(epsilon,j)` to
`a_r,a_(r+1)`.  For `epsilon=0` these pairs are
`{0,1},{2,3},...`; for `epsilon=1` they are
`{1,2},{3,4},...,{q-1,0}`.  Each family partitions `A`.  Thus every edge
of `K_(q,q+2)` occurs exactly once.  Consecutive edges in (9.3) share
alternately `B_t` and `A_(t+1)`, including at the cyclic wrap, proving the
Euler assertion and owner simplicity.

Every immediate-lower value is the complement of the three graph vertices
in a consecutive wedge.  Wedges centred in `B` have type `A-B-A`, while
wedges centred in `A` have type `B-A-B`, so the two families cannot collide.
Inside either family, the centre and its two incident graph edges recover
the half-step `t`; since no graph edge repeats, no wedge repeats.  Hence the
lower row is simple.

For `a_s`, its incident edges occur in adjacent pairs at the turns centred
at `a_s`.  For fixed `s`, solving `A_t=a_s` gives one half-step in each
`ell`-block, so consecutive half-step gaps are exactly `q`.  The
corresponding zero-pairs are therefore separated by `2q-2` positive
owners.

Now fix `b_(epsilon,j)` and order its half-steps from (9.4) cyclically.
Writing `q=2s`, consecutive half-step gaps are `q-2`, except for one gap
`3q-2`.  Indeed, increasing the parity-compatible `r` by two decreases
`ell` by one modulo `h=s+1`; hence all but the wrap have absolute cyclic
gap `q-2`, and the remaining gap is forced by the total `qh`:

\[
 qh-(s-1)(q-2)=3q-2.                               \tag{9.5}
\]

Each occurrence of `B_t` contributes a zero-pair, so a half-step gap
`Delta` gives `2Delta-2` positive owners.  The minimum is therefore

\[
 2(q-2)-2=2q-6\ge q                                \tag{9.6}
\]

for `q>=6`.  This proves Item 3. \(\square\)

The finite case `q=4` is not covered by this ordering.  Asymptotically the
even cycle shore is now completely fused; the remaining raw short-cycle
fusion problem is confined to the odd `Gamma_j` shore.

### Remark 9.2 (the even ordering is not a `C_(q+2)` decomposition)

Theorem 9.1 deliberately replaces the Sotteau cycle decomposition by one
Euler ordering of all graph edges.  This is legitimate for the cycle-shore
owner packing because the `Omega` current depends only on the graph-edge
multiset.  It is not a proof that the particular `q` short Sotteau cycles
can be opened and concatenated residently, and any application requiring
the original component partition must keep that distinction explicit.

## 10. Stronger whole-fibre alternative

The complementary-fibre lift replaces every graph edge by a period-`2q`
biresident rail and turns (1.2) into

\[
 \mathcal B(S)=\mathcal B(G)\sqcup\mathcal B(uv).   \tag{7.1}
\]

It simultaneously restores dual residence and simple proper interval decks,
but changes the residual from the singleton owner `H` to the entire rail
`mathcal B(uv)`.  Therefore (7.1) is a structured-leave theorem, not a
direct lift of `e_H-Y_H`.  Closing the original special residue requires
either a cover-down whose leave is the whole rail `mathcal B(uv)`, or a new
puncture absorber for the other `2q-1` owners of that rail.

## 11. Exact remaining local gate

The short graph absorber itself is already sufficient for flat inversion and
lower-q1 protection.  Its exact remaining physical interface is:

\[
 \boxed{\text{run-safe phased fusion}
 \; + \;\text{external backups for the }O(q)\text{ affected upper values}
 \; + \;\text{terminal occurrence-level compiler}.}
\]

The factor extension row is conditional only on the explicit low-exposure
test.  The graph decompositions do not solve the run-safe fusion, and the
whole-fibre dilation trades the singleton residue for a complete-rail leave.

# Partial cyclic packets through depth two: the ordered-coloured factor normal form and a sharp endpoint obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad r=m-q_0,\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 W=\binom{2m}{m},
\tag{0.1}
\]

where \(a>0\) is fixed, and write

\[
 N_i=\binom n{r-i}\qquad(i=0,1,2).
\tag{0.2}
\]

Thus \(N_i=(e^{-a^2}+o(1))W\), and

\[
 N_0-N_i=O(W/\sqrt m)=o(W)\qquad(i=1,2).
\tag{0.3}
\]

This note audits the proposed two-stage argument

\[
 \text{fixed-rank near-factor}
 \quad+\quad
 \text{endpoint assignment}
 \quad\Longrightarrow\quad
 \text{depth-two near-cover}.
\tag{0.4}
\]

The conclusion is precise.

1.  An actual cyclic packet has an exact ordered-coloured normal form.
    Its rank-\(r\) states, rank-\((r-1)\) endpoint colours, and
    rank-\((r-2)\) turn colours are

    \[
    A_i=\{a_i,\ldots,a_{i+r-1}\},\quad
    B_i=\{a_{i+1},\ldots,a_{i+r-1}\},\quad
    C_i=\{a_{i+1},\ldots,a_{i+r-2}\}.
    \tag{0.5}
    \]

    In particular

    \[
       A_i=B_{i-1}\cup B_i,
       \qquad C_i=B_{i-1}\cap B_i.
    \tag{0.6}
    \]

    The endpoint cycle is a packet if and only if it satisfies the
    global FIFO law in Theorem 2.2 below.  Endpoints cannot be reassigned
    after a packet has been selected.

2.  If the FIFO law is omitted, (0.4) is false by a linear margin.  There
    is an ordered endpoint factor using distinct rank-\(r\) owners and
    distinct rank-\((r-1)\) endpoints which covers all but \(o(W)\) of
    both layers, but whose rank-\((r-2)\) turn colours miss

    \[
             \left(\frac34-o(1)\right)N_2=\Theta(W)
    \tag{0.7}
    \]

    targets.  The factor is a disjoint union of four-cycles.  On one
    four-cycle all four turn colours equal the same \((r-2)\)-set, while
    its four owner colours are distinct.  A fixed-uniformity matching
    theorem packs these gadgets through all but \(o(W)\) endpoint and
    owner vertices.

3.  Therefore a fixed-rank near-perfect matching plus a marginal Hall
    assignment of endpoints cannot be extended through depth two as a
    formal consequence.  The missing hypothesis is not another endpoint
    capacity inequality; it is the packet word law itself, together with
    near-rainbow control of the inherited turn colours.

4.  The genuine packet catalogue has an exact symmetric fractional point
    covering ranks \(r-1\) and \(r-2\) at load at least one while matching
    rank \(r\) up to the \(O(m)\) divisibility leave.  Hence there is no
    fractional Hall cut at depth two.  The remaining assertion is the
    integral FIFO-coloured packet factor stated in Section 7.

The four-cycle construction is an obstruction to the proposed *two-stage
reduction*.  It is not a no-go theorem for actual cyclic packets, because
its four-cycles deliberately violate the FIFO law.  No positive-density
cut for the FIFO-constrained catalogue is proved here.

## 1. The three consecutive ranks and the endpoint factor

Let

\[
 \mathcal A=\binom{[n]}r,\qquad
 \mathcal B=\binom{[n]}{r-1},\qquad
 \mathcal C=\binom{[n]}{r-2}.
\tag{1.1}
\]

An **ordered endpoint factor** is a family of cyclic alternating walks

\[
 B_{p,0},A_{p,1},B_{p,1},A_{p,2},\ldots,
 B_{p,\ell_p-1},A_{p,0},B_{p,0}
\tag{1.2}
\]

such that

\[
 B_{p,i-1}\subset A_{p,i}\supset B_{p,i},
 \qquad
 B_{p,i-1}\ne B_{p,i}.
\tag{1.3}
\]

Every owner \(A_{p,i}\) is then forced to be

\[
 A_{p,i}=B_{p,i-1}\cup B_{p,i},
\tag{1.4}
\]

and its depth-two colour is

\[
 C_{p,i}=B_{p,i-1}\cap B_{p,i}\in\mathcal C.
\tag{1.5}
\]

We call the factor upper-rainbow if the \(A_{p,i}\)'s are distinct, and
vertex-rainbow if the \(B_{p,i}\)'s are distinct.  Thus an upper-rainbow,
vertex-rainbow endpoint factor is exactly the combinatorial information
provided by a fixed-rank owner matching together with a collision-free
endpoint assignment.  Depth two asks in addition that the edge colours
(1.5) cover almost all of \(\mathcal C\).

This is already a two-sided colour problem on the Johnson graph
\(J(n,r-1)\): its vertices are \(\mathcal B\), the upper colour of the
edge \(BB'\) is \(B\cup B'\), and its lower colour is \(B\cap B'\).

## 2. Exact cyclic-packet normal form

Let \(a=(a_0,\ldots,a_{n-1})\) be a cyclic permutation of \([n]\), with
indices read modulo \(n\).  Its rank-\(r\) packet is

\[
 A_i=\{a_i,a_{i+1},\ldots,a_{i+r-1}\}.
\tag{2.1}
\]

### Theorem 2.1 (hereditary endpoint and turn colours)

For the packet (2.1), put

\[
 B_i=A_i\cap A_{i+1},
 \qquad
 C_i=A_{i-1}\cap A_i\cap A_{i+1}.
\tag{2.2}
\]

Then

\[
 B_i=\{a_{i+1},\ldots,a_{i+r-1}\},
 \qquad
 C_i=\{a_{i+1},\ldots,a_{i+r-2}\}.
\tag{2.3}
\]

Equivalently,

\[
 A_i=B_{i-1}\cup B_i,
 \qquad
 B_{i-1}\cap B_i
   =\{a_{i+1},\ldots,a_{i+r-2}\}.
\tag{2.4}
\]

All \(A_i\), all \(B_i\), and all \(C_i\) are distinct inside one
packet.

#### Proof

Consecutive length-\(r\) windows have common part from positions \(i+1\)
through \(i+r-1\); the three windows with starts \(i-1,i,i+1\) have
common part from positions \(i+1\) through \(i+r-2\).  This proves
(2.3)--(2.4).
Distinct starting positions give distinct proper cyclic intervals of a
cyclic permutation. \(\square\)

The preceding formula has an exact converse which records the global
condition lost by a bare endpoint assignment.

### Theorem 2.2 (FIFO characterization)

Consider one cyclic component

\[
 B_{-1},A_0,B_0,A_1,\ldots,B_{n-2},A_{n-1},B_{-1}
\tag{2.5}
\]

of an ordered endpoint factor, of length exactly \(n\).  Write the
transition from \(B_{i-1}\) to \(B_i\) as

\[
 B_i=B_{i-1}-\delta_i+\eta_i.
\tag{2.6}
\]

Put \(s=r-1\).  The component is the endpoint factor of one ordinary
rank-\(r\) cyclic packet if and only if

\[
 (\delta_0,\ldots,\delta_{n-1})
 \text{ is a permutation of }[n]
\tag{2.7}
\]

and

\[
                  \boxed{\eta_i=\delta_{i+s}}
                  \qquad(i\in\mathbb Z_n).
\tag{2.8}
\]

When these conditions hold,

\[
 B_{i-1}=\{\delta_i,\ldots,\delta_{i+s-1}\},
 \qquad
 A_i=\{\delta_i,\ldots,\delta_{i+s}\}.
\tag{2.9}
\]

#### Proof

For a packet, take \(\delta_i=a_i\).  The transition between the two
rank-\((r-1)\) windows deletes \(a_i\) and inserts
\(a_{i+r-1}=a_{i+s}\), proving necessity.

Conversely assume (2.7)--(2.8).  During transitions
\(0,\ldots,s-1\), the distinct labels
\(\delta_0,\ldots,\delta_{s-1}\) are deleted, while the inserted labels
are \(\delta_s,\ldots,\delta_{2s-1}\).  In particular none of the first
\(s\) deleted labels has previously been reinserted.  Since
\(|B_{-1}|=s\),

\[
 B_{-1}=\{\delta_0,\ldots,\delta_{s-1}\}.
\]

Now (2.6) and (2.8) give (2.9) inductively.  With
\(a_i=\delta_i\), the second formula in (2.9) is exactly the cyclic
window rule. \(\square\)

Thus the packet condition is not merely that endpoint stubs can be paired
into cycles.  It is the lag-\((r-1)\) identity (2.8) on one globally
permuted direction word.

## 3. Exact hole and repeat ledgers through depth two

Let \(\mathscr P\) be a family of \(K\) actual cyclic packets and put
\(M=nK\).  For \(i=0,1,2\), let \(\mu_i(T)\) be the multiplicity of the
rank-\((r-i)\) target \(T\) among the corresponding packet windows.  Put

\[
 h_i=|\{T:\mu_i(T)=0\}|,
 \qquad
 c_i=\sum_T(\mu_i(T)-1)_+.
\tag{3.1}
\]

### Lemma 3.1 (floor ledger)

For \(i=0,1,2\),

\[
                         \boxed{h_i=N_i-M+c_i.}
\tag{3.2}
\]

If the rank-\(r\) packet traces form a matching, then \(c_0=0\) and
\(h_0=N_0-M\).  If \(M=N_0-O(m)\), then

\[
 h_1+h_2=o(W)
 \quad\Longleftrightarrow\quad
 c_1+c_2=o(W).
\tag{3.3}
\]

#### Proof

At every one of the three ranks the packets contribute exactly \(M\)
occurrences.  Relative to the complete layer, every hole removes one unit
and every repeat copy adds one, proving (3.2).  Formula (0.3) then proves
(3.3). \(\square\)

For actual packets the upper rank-\((m+q_0+i)\) trace is the complement
of the lower rank-\((m-q_0-i)\) trace, up to a cyclic shift.  Hence the
upper and lower hole counts are identical.  It is enough to solve the
lower ordered-colour problem.

## 4. The four-star obstruction

We now prove that upper-rainbow owners plus a vertex-rainbow endpoint
assignment do not control the turn colours.

Fix \(C\in\mathcal C\), choose a four-set
\(Q\subseteq[n]\setminus C\), and choose one of the three undirected
Hamilton cycles \(H\) of the complete graph on \(Q\).  Define the eight
resources

\[
 \mathcal V(C,Q,H)
 =\{C\cup\{x\}:x\in Q\}
   \ \dot\cup\
   \{C\cup e:e\in E(H)\}.
\tag{4.1}
\]

The first four resources lie in \(\mathcal B\), the last four in
\(\mathcal A\).  Around \(H\), consecutive \(\mathcal B\)-vertices have
union equal to the corresponding \(\mathcal A\)-resource and intersection
equal to \(C\).  Thus (4.1) is one upper-rainbow, vertex-rainbow
four-cycle whose four lower edge colours are all \(C\).

Let \(\mathcal H_4\) be the 8-uniform hypergraph on
\(\mathcal A\dot\cup\mathcal B\) whose hyperedges are (4.1).

### Lemma 4.1 (degrees)

The degrees on the two shores are

\[
 d_B=3(r-1)\binom{n-r+1}{3}
 \qquad(B\in\mathcal B),
\tag{4.2}
\]

and

\[
 d_A=2\binom r2\binom{n-r}{2}
 \qquad(A\in\mathcal A).
\tag{4.3}
\]

Moreover

\[
                 \frac{d_A}{d_B}=\frac r{n-r+1}
                 =1-O(m^{-1/2}).
\tag{4.4}
\]

#### Proof

For fixed \(B\), choose the unique point of \(B\setminus C\) in
\(r-1\) ways, choose the other three members of \(Q\) outside \(B\),
and choose one of the three Hamilton cycles of \(Q\).  This gives (4.2).

For fixed \(A\), choose \(C\subset A\) in \(\binom r2\) ways, choose
the other two points of \(Q\) outside \(A\), and note that exactly two
Hamilton cycles of \(K_4\) contain the prescribed edge \(A\setminus C\).
This gives (4.3).  Simplification gives (4.4). \(\square\)

### Lemma 4.2 (pair codegrees)

The maximum pair codegree of \(\mathcal H_4\) is \(O(m^3)\).  Since
\(d_A,d_B=\Theta(m^4)\),

\[
                         \frac{\Delta_2(\mathcal H_4)}
                              {\min(d_A,d_B)}=O(m^{-1})=o(1).
\tag{4.5}
\]

#### Proof

For two \(\mathcal B\)-vertices to occur together, their intersection
must have size \(r-2\), which fixes \(C\).  The two remaining members of
\(Q\) can then be chosen in \(O(m^2)\) ways.

For two distinct \(\mathcal A\)-vertices, a common core exists only when
their intersection has size at least \(r-2\).  At Johnson distance one,
there are at most \(r-1\) choices for the core and \(O(m)\) choices for
the fourth point of \(Q\), giving \(O(m^2)\).  At distance two the core
is fixed and the codegree is bounded by two.

Finally take \(B\in\mathcal B\) and \(A\in\mathcal A\).  If
\(B\subset A\), there are \(r-1\) choices of the point removed from
\(B\) to form \(C\), \(\binom{n-r}{2}\) choices of the other two points
of \(Q\), and two compatible Hamilton cycles.  This is \(O(m^3)\).  If
\(|A\cap B|=r-2\), the core is fixed and there are only \(O(m)\) choices;
all other cases have codegree zero. \(\square\)

We use the standard fixed-uniformity near-matching lemma: if a fixed
\(k\)-uniform hypergraph has all degrees \((1+o(1))D\), with
\(D\to\infty\), and maximum pair codegree \(o(D)\), then it has a
matching leaving \(o(|V|)\) vertices.  Here \(k=8\) is fixed, so there is
no growing-uniformity quantifier issue.

### Theorem 4.3 (linear depth-two failure after a near-perfect endpoint assignment)

There is an ordered endpoint factor with the following properties:

1. all its rank-\(r\) owner colours are distinct and cover
   \(N_0-o(W)\) members of \(\mathcal A\);
2. all its rank-\((r-1)\) endpoint vertices are distinct and cover
   \(N_1-o(W)\) members of \(\mathcal B\); and
3. its rank-\((r-2)\) turn-colour support has size at most
   \((1/4+o(1))N_2\).  Consequently its depth-two hole count is at least

   \[
             \boxed{\left(\frac34-o(1)\right)N_2=\Theta(W).}
   \tag{4.6}
   \]

#### Proof

Lemmas 4.1--4.2 and the fixed-uniformity matching lemma give a matching
\(\mathcal M\) in \(\mathcal H_4\) leaving \(o(W)\) vertices of
\(\mathcal A\dot\cup\mathcal B\).  Every selected hyperedge supplies the
four-cycle described after (4.1).  Hypergraph disjointness makes all its
\(\mathcal A\)-colours and all its \(\mathcal B\)-vertices globally
distinct.

If \(L=|\mathcal M|\), then

\[
 4L=N_1-o(W).
\tag{4.7}
\]

The same number of \(\mathcal A\)-vertices is covered.  Since
\(N_0-N_1=o(W)\), this is \(N_0-o(W)\).  Each four-cycle uses only one
turn colour, its core \(C\).  Even if all selected cores are distinct, its
turn-colour support has size at most

\[
 L=\frac14N_1+o(W)=\left(\frac14+o(1)\right)N_2.
\]

This proves (4.6). \(\square\)

### Corollary 4.4 (the marginal two-stage implication is false)

No theorem using only

* near-perfect fixed-rank owner matching,
* near-perfect endpoint coverage, and
* local legality \(B^-\subset A\supset B^+\)

can imply \(o(W)\) depth-two holes.  A valid positive theorem must use an
additional global condition which excludes Theorem 4.3.  For cyclic
packets that condition is exactly Theorem 2.2.

## 5. What is positive before ordering

The obstruction is not a local capacity shortage.  There is even a simple
exact unordered diamond assignment covering all three ranks.

### Proposition 5.1 (an exact unordered three-rank cover)

There is a choice, for every \(A\in\mathcal A\), of a set
\(C(A)\in\mathcal C\) with \(C(A)\subset A\), such that the diamonds

\[
 [C(A),A]
 =\{C(A),\ C(A)\cup\{x\},\ C(A)\cup\{y\},\ A\},
 \qquad A\setminus C(A)=\{x,y\},
\tag{5.1}
\]

cover every member of \(\mathcal B\) and every member of
\(\mathcal C\).  If any \(\rho\) owners are then discarded, at most
\(2\rho\) endpoint targets and at most \(\rho\) depth-two targets lose
their displayed witness.

#### Proof

Fix a symmetric-chain decomposition of the Boolean lattice.  If the chain
through \(A\) reaches rank \(r-2\), take its rank-\((r-2)\) member as
\(C(A)\).  Every \(C\in\mathcal C\) lies on a chain which reaches rank
\(r\), so every \(C\) is selected once this way.

Now fix \(B\in\mathcal B\).  Its chain reaches rank \(r\).  If that chain
also reaches rank \(r-2\), the selected diamond on the same chain contains
\(B\).  If the chain starts at rank \(r-1\), let \(A\) be its rank-\(r\)
member and choose any \(C(A)\subset B\) of rank \(r-2\); the resulting
diamond contains \(B\).  Owners whose chains start at rank \(r\) may be
assigned arbitrarily.  Thus both lower ranks are covered.  Deleting one
diamond removes at most its two \(\mathcal B\)-members and its one
\(\mathcal C\)-member. \(\square\)

Proposition 5.1 proves that nesting through depth two is integrally easy
when chronology is forgotten.  Theorem 4.3 proves that even a very strong
endpoint factor can be chronologically bad.  The missing constraint is
therefore genuinely ordered.

## 6. The exact fractional cyclic-packet point

Let \(\Omega_n\) be the directed cyclic orders on \([n]\), modulo
rotation.  A fixed rank-\(s\) target is an interval in exactly

\[
                         d_s=s!(n-s)!
\tag{6.1}
\]

members of \(\Omega_n\).  Put

\[
 K=\left\lfloor\frac{N_0}{n}\right\rfloor,
 \qquad
 \beta=\frac{nK}{N_0}=1-O(m/W),
\tag{6.2}
\]

and assign every cyclic order the weight

\[
                         x_\pi=\frac\beta{d_r}.
\tag{6.3}
\]

### Proposition 6.1 (simultaneous fractional depth-two cover)

The weights (6.3) have total mass \(K\).  Their load on every target of
rank \(r-i\) is

\[
                         \ell_i=\beta\frac{d_{r-i}}{d_r}
                         =\beta\frac{N_0}{N_i}
                         \qquad(i=0,1,2).
\tag{6.4}
\]

Thus \(\ell_0=\beta\), while \(\ell_1,\ell_2>1\) for all sufficiently
large \(m\).  The fractional defect is exactly the divisibility leave
\(N_0-nK<n=O(m)\), all at rank \(r\), and is zero at depths one and two.

#### Proof

Double counting packet-target incidences gives

\[
 \sum_{\pi\in\Omega_n}x_\pi
 =\frac{\beta(n-1)!}{r!(n-r)!}
 =\frac{\beta N_0}{n}=K.
\]

Equation (6.4) follows from (6.1) and

\[
 \frac{d_{r-i}}{d_r}
 =\frac{\binom nr}{\binom n{r-i}}
 =\frac{N_0}{N_i}.
\]

Since \(1-\beta=O(m/W)\), whereas
\(N_0/N_i-1=\Theta(m^{-1/2})\) for \(i=1,2\), the latter loads exceed
one. \(\square\)

Consequently no nonnegative fractional Hall inequality separates the
actual packet catalogue at the first two inherited depths.  The
four-cycle obstruction is an integral chronology obstruction to a weak
reduction, not a fractional capacity obstruction to cyclic packets.

## 7. The exact remaining integral gate

The depth-two partial cyclic-packet theorem can now be stated without any
hidden endpoint freedom.

> **FIFO-coloured partial factor, depth two (FCPF\(_2\)).**  There are
> \(K=N_0/n+O(1)\) cyclic permutations
> \(a^{(p)}=(a^{(p)}_i)_{i\in\mathbb Z_n}\) such that, with
> \[
> A_{p,i}=\{a^{(p)}_i,\ldots,a^{(p)}_{i+r-1}\},
> \]
> the \(A_{p,i}\)'s have total collision-plus-hole defect \(o(W)\), and
> the two inherited colour families
> \[
> B_{p,i}=\{a^{(p)}_{i+1},\ldots,a^{(p)}_{i+r-1}\},
> \qquad
> C_{p,i}=\{a^{(p)}_{i+1},\ldots,a^{(p)}_{i+r-2}\}
> \]
> miss only \(o(W)\) targets in aggregate.

If exact entrance matching is imposed, use \(K=\lfloor N_0/n\rfloor\)
and allow the unavoidable leave smaller than \(n\).  If the coefficient-one
compiler also requires middle-owner disjointness, add the antipodal
middle-pair capacity constraints from the partial-annulus packet programme;
they have constant fractional slack and do not alter the endpoint
obstruction above.

By Lemma 3.1, FCPF\(_2\) is equivalently the demand

\[
                         c_1+c_2=o(W)
\tag{7.1}
\]

for the inherited endpoint and turn colours of one common packet
selection.  Theorem 4.3 shows that (7.1) does not follow from separate
near-matchings at ranks \(r\) and \(r-1\).  Proposition 6.1 shows that it
is not ruled out by any fractional Hall cut.

There is also no post-selection endpoint repair: by Theorem 2.1 the
families \(B_{p,i}\) and \(C_{p,i}\) are functions of the selected cyclic
orders.  Changing one endpoint changes the direction word and hence
replaces a whole packet column.  Therefore the exact surviving operation
is a whole-packet alternating trade preserving the rank-\(r\) matching
while changing the two inherited colour vectors.

## 8. Audited boundary

Proved here:

1. the exact ordered-coloured factor normal form through depth two;
2. the exact FIFO characterization distinguishing packets from arbitrary
   endpoint factors;
3. the exact hole/repeat ledger at the first three ranks;
4. a fixed-rank, near-perfect, upper-rainbow and vertex-rainbow endpoint
   factor with \((3/4-o(1))N_2\) depth-two holes;
5. an exact unordered three-rank diamond cover, showing there is no
   nesting-capacity obstruction; and
6. simultaneous fractional feasibility of the true packet catalogue
   through depth two.

Not proved here:

1. FCPF\(_2\);
2. a positive-density integral Hall cut for the FIFO catalogue; or
3. a whole-packet absorber which rounds the symmetric point while keeping
   both inherited colour excesses \(o(W)\).

The strongest rigorous verdict is therefore:

\[
\boxed{
\begin{minipage}{0.86\linewidth}
A fixed-rank near-perfect matching plus an independently solved endpoint
assignment does not extend through depth two; it may leave
\(\Theta(W)\) holes.  Once the exact cyclic FIFO law is imposed, the
counterexample disappears and no fractional obstruction remains.  The
minimal unresolved object is the common FIFO-coloured packet factor
FCPF\(_2\), not another marginal matching or endpoint Hall theorem.
\end{minipage}}
\]

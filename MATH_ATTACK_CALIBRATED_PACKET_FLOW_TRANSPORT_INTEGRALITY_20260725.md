# Calibrated top packets versus balanced flag flow: exact integrality audit

Date: 2026-07-25

Pure mathematics only.  No computation, solver, random experiment, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q},
\]

and take the calibrated first crossing

\[
 H=\min\{h:\lambda_h\ge m+h\},\qquad M=m+H,
 \qquad S=M N_H.
\tag{0.1}
\]

Thus

\[
 H\sim\sqrt{m\log m},\qquad
 S=W-o(W),\qquad HN_H=o(W).
\tag{0.2}
\]

This note gives an exact flow/transport formulation and locates its integral
boundary.

1.  In the bipartite containment graph from rank-\(M\) tops to middle
    owners, every top can be assigned \(M\) owners, with no owner assigned
    twice.  This is an immediate integral \(b\)-matching consequence of
    biregularity and the calibrated inequality \(\lambda_H\ge M\).

2.  Much more is true after cyclic synchronization is removed.  There is
    an integral family of \(S\) nested Boolean paths, exactly \(M\) starting
    at every top, such that every rank-\(r\) target has path multiplicity

    \[
       \left\lfloor {S\over\binom{2m}{r}}\right\rfloor
       \quad\hbox{or}\quad
       \left\lceil {S\over\binom{2m}{r}}\right\rceil
    \tag{0.3}
    \]

    throughout the complete band \(m-H\le r\le M\).  This is one
    lower-bounded directed network, hence is exactly integral by total
    unimodularity.  At rank \(m\) the paths use \(S\) distinct owners.

3.  For a fixed top there is also an exact order-prefix network whose unit
    path extreme points are cyclic orders, hence full promotion packets.
    The uniform barycentre of these packet paths maps to the uniform
    fractional Boolean flow in item 2.

4.  The two integral statements do **not** combine by adjoining the target
    incidence rows.  The genuine calibrated packet-versus-owner matrix
    contains

    \[
       \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
       \qquad \det=-2.
    \tag{0.4}
    \]

    Thus the natural coupled formulation is not totally unimodular.  The
    minor is realized by three actual cyclic packets in one top, not by an
    abstract configuration gadget.

5.  The middle-owner supports of packets in one top are not the integer
    bases of a polymatroid.  Every packet has point degree exactly \(m\) on
    every coordinate of its top.  Replacing one owner block by a different
    owner block destroys that identity, so the one-unit base-exchange axiom
    fails.

6.  There is a zero-optimum fractional configuration LP for the exact
    remaining problem.  On integral points its objective is

    \[
      \delta_{m,H}
       =\sum_{r=m-H}^{M-1}
          \left(
          \min\!\left\{\binom{2m}{r},S\right\}
          -\#\{\hbox{rank-}r\hbox{ targets hit}\}
          \right).
    \tag{0.5}
    \]

    The nonsynchronized integral flow has discrepancy zero.  For packets,
    proving \(\delta_{m,H}=o(W)\) is precisely the surviving bounded-defect
    rounding gate.  It is weaker than the perfect augmented matching gate
    and is already sufficient for a \(W+o(W)\) word.

7.  Independent rounding does not approach this gate: it leaves
    \((e^{-1}+o(1))W\) middle owners uncovered in expectation.  The full
    band augmented hypergraph also lies outside the usual small-rank
    codegree regime, since its edge rank is \(1+2HM\), its symmetric
    fractional pair mass is at least \((2+o(1))/m\), and their product is
    \((4+o(1))H\to\infty\).

Hence ordinary network TU completely solves nested balance but not packet
synchronization; the raw packet catalog is not a polymatroid; and no generic
bounded-defect rounding theorem audited here closes the gap.  The exact
remaining integral discrepancy is (0.5).

## 1. Calibration ledger

Let

\[
 c={\lambda_H\over M},\qquad S={W\over c},\qquad D=W-S.
\tag{1.1}
\]

Minimality of \(H\), together with

\[
 {\lambda_{h+1}\over\lambda_h}={m+h+1\over m-h},
\tag{1.2}
\]

gives

\[
 1\le c<1+{2H-2\over m-H+1},
 \qquad
 0\le D<{2H-2\over M-1}W.
\tag{1.3}
\]

In particular

\[
 {S\over W}={1\over c}=1-O(H/m).
\tag{1.4}
\]

The standard expansion

\[
 \log\lambda_h={h^2\over m}
  +O\!\left({h\over m}+{h^3\over m^2}\right)
 \qquad(h=o(m^{2/3}))
\tag{1.5}
\]

locates the first crossing at

\[
 H=(1+o(1))\sqrt{m\log m}.
\tag{1.6}
\]

Consequently \(N_H=(1+o(1))W/m\) and \(HN_H=o(W)\).

Write

\[
 \mathcal J=\{m-H,m-H+1,\ldots,M-1\},
 \qquad N(r)=\binom{2m}{r},
\tag{1.7}
\]

and define the scalar load at rank \(r\) by

\[
 \mu_r={S\over N(r)}.
\tag{1.8}
\]

At the middle, \(\mu_m=S/W=1/c\le1\); at the top,
\(\mu_M=S/N_H=M\).

## 2. The owner-only bipartite transport is integral

Let \(\mathcal U=\binom{[2m]}M\) be the top layer and
\(\Omega=\binom{[2m]}m\) the owner layer.  Join \(U\in\mathcal U\) to
\(X\in\Omega\) exactly when \(X\subset U\).

### Theorem 2.1 (exact calibrated owner transport)

There is a set of containment edges such that every top has degree exactly
\(M\) and every owner has degree at most one.

#### Proof

The containment graph is biregular.  Its left and right degrees are

\[
 d_L=\binom Mm,\qquad d_R=\binom mH,
\tag{2.1}
\]

respectively.  Double-counting containment pairs gives

\[
 N_Hd_L=Wd_R,
 \qquad {d_L\over d_R}={W\over N_H}=\lambda_H.
\tag{2.2}
\]

For any family \(\mathcal A\subseteq\mathcal U\), all \(d_L|\mathcal A|\)
incident edges end in its owner neighbourhood \(N(\mathcal A)\), and each
owner receives at most \(d_R\) of them.  Therefore

\[
 |N(\mathcal A)|\ge {d_L\over d_R}|\mathcal A|
 =\lambda_H|\mathcal A|\ge M|\mathcal A|.
\tag{2.3}
\]

This is precisely Hall's condition for a left demand of \(M\) and a right
capacity of one.  The bipartite \(b\)-matching polytope is a network-flow
polytope, so it has an integral feasible point. \(\square\)

Thus neither the calibrated top count nor top-to-owner containment creates
an integral obstruction.  The missing condition is that the \(M\) owners
assigned to one top must be the \(M\) cyclic \(m\)-windows of one order.

## 3. The whole nested band has an exact integral flow

Consider the downward Boolean inclusion DAG on ranks

\[
 M,M-1,\ldots,m-H.
\]

Its rank-\(r\) vertices are the \(r\)-subsets of \([2m]\), and it has an
arc \(B\to T\) when \(T\subset B\) and \(|B|=|T|+1\).

### Theorem 3.1 (integral balanced top-rooted flags)

There is an integral family of \(S\) downward paths with the following
properties.

1. Exactly \(M\) paths start at every rank-\(M\) top \(U\).
2. For every \(m-H\le r<M\) and every rank-\(r\) target \(T\), the number
   of paths through \(T\) belongs to

   \[
     \{\lfloor\mu_r\rfloor,\lceil\mu_r\rceil\}.
   \tag{3.1}
   \]

3. In particular, the middle vertices on these paths are \(S\) distinct
   owners.

#### Proof

Split every Boolean vertex into an entrance and an exit joined by a node
arc.  Give a rank-\(r\) node arc the integral lower and upper bounds

\[
 \lfloor\mu_r\rfloor,qquad\lceil\mu_r\rceil
\tag{3.2}
\]

for \(m-H\le r<M\).  At every top give the node arc both lower and upper
bound \(M\).  Add a source arc of value \(M\) into each top, retain the
downward inclusion arcs with sufficiently large integral capacity, and
join the bottom node exits to one sink.

This lower-bounded network is fractionally feasible.  Give every rank-\(r\)
node throughput \(\mu_r\).  From a rank-\((r+1)\) set \(B\), send

\[
 {\mu_{r+1}\over r+1}
\tag{3.3}
\]

along each of its \(r+1\) deletion arcs.  A fixed rank-\(r\) set has
\(2m-r\) immediate supersets, so it receives

\[
 {2m-r\over r+1}\mu_{r+1}
 ={2m-r\over r+1}{S\over N(r+1)}
 ={S\over N(r)}=\mu_r.
\tag{3.4}
\]

At the top this assigns throughput \(\mu_M=M\), exactly as required.
Every node throughput lies between the two bounds (3.2).

After the usual lower-bound shift, the constraint matrix is the directed
node-arc incidence matrix of a finite network.  It is totally unimodular,
and all supplies and bounds are integral.  Fractional feasibility therefore
implies integral feasibility.  Because the network is acyclic, decompose
the resulting integral flow into \(S\) unit paths.

Finally, \(\mu_m=S/W\le1\), so every middle node has capacity at most one.
The \(S\) paths consequently use \(S\) distinct middle owners. \(\square\)

Each unit path through an owner \(X\) is a full nested lower/upper flag:
the downward segment below \(X\) records its deletion sequence, and the
reverse of the segment from the top down to \(X\) records its addition
sequence.  Thus nestedness, top containment, middle ownership, and exact
floor/ceiling balance are simultaneously integral.

The theorem does not order the \(M\) paths from a common top into a
bridge-one promotion cycle.  This is the only condition omitted.

## 4. An exact order network whose extreme points are packets

Fix a top \(U\) and a distinguished root \(\rho(U)\in U\).  Let
\(\mathcal D_U\) be the acyclic prefix-order graph whose nodes are injective
words

\[
 (\rho(U),u_1,\ldots,u_k),\qquad 0\le k\le M-1,
\tag{4.1}
\]

and whose arcs append one unused element.  Join every full word to a
terminal sink.  A unit source-sink path is exactly a linear order of \(U\)
beginning with \(\rho(U)\), hence exactly one directed cyclic order of
\(U\).

The unit-flow polytope on \(\mathcal D_U\) is integral.  Its extreme points
are its source-sink paths.  Therefore the product

\[
 \mathcal O=\prod_{U\in\mathcal U}P(\mathcal D_U)
\tag{4.2}
\]

is an exact network extended formulation whose extreme points choose one
cyclic order at every top.

For a terminal order \(\pi\), put

\[
 I_\pi(t,r)=\{u_t,u_{t+1},\ldots,u_{t+r-1}\},
 \qquad t\in\mathbb Z_M.
\tag{4.3}
\]

For a middle phase \(t\), define

\[
 F_{\pi,t}(r)=I_\pi(t+m-r,r),
 \qquad m-H\le r\le M.
\tag{4.4}
\]

Then

\[
 F_{\pi,t}(r+1)=I_\pi(t+m-r-1,r+1)
 \supset I_\pi(t+m-r,r)=F_{\pi,t}(r),
\tag{4.5}
\]

so \(r\mapsto F_{\pi,t}(r)\) is a downward Boolean path, obtained at each
step by deleting the current left endpoint.  Also

\[
 F_{\pi,t}(m)=I_\pi(t,m),\qquad F_{\pi,t}(M)=U.
\tag{4.6}
\]

The corresponding packet bundle is the family of these \(M\) paths as
\(t\) ranges over \(\mathbb Z_M\).  At every proper band rank, translation
of \(t\) in (4.4) shows that the bundle uses exactly the \(M\) cyclic
intervals of that rank.  At the middle it uses the \(M\) owners
\(I_\pi(t,m)\) of the promotion cycle.

The lower part of the path through owner \(I_\pi(t,m)\) deletes the future
departure queue, and the upper part, read upward, adds the past departure
queue.  Consequently the transition from phase \(t\) to phase \(t+1\) is
the last-position bridge-one promotion.  Thus (4.4), rather than the
fixed-start chain \(I_\pi(t,r)\), is the chronology-correct full flag.

Conversely, the full-flag bundle of a calibrated promotion packet has the
form (4.4) for one terminal path of \(\mathcal D_U\).

Thus packet selection itself has an integral network extension.  What is
not a network constraint is the global demand that the interval-incidence
outputs of terminal paths be simultaneously balanced.

### Proposition 4.1 (common fractional point)

Give each of the \((M-1)!\) terminal orders at every top weight
\(1/(M-1)!\).  Its image under (4.4) is the uniform fractional flow used in
Theorem 3.1.

#### Proof

Every packet has \(M\) paths and therefore \(M\) occurrences at each
proper rank.  The total packet weight is \(N_H\), so the total occurrence
mass at each rank is \(S\).  Relabelling transitivity makes the mass uniform
over the \(N(r)\) rank-\(r\) targets, hence it is \(S/N(r)=\mu_r\).

Likewise, at a fixed adjacent-rank pair, every packet contributes \(M\)
arcs from (4.5).  Relabelling is transitive on Boolean cover pairs, so the
arc mass is uniform.  Conservation then forces it to be
\(\mu_{r+1}/(r+1)\), the value in (3.3). \(\square\)

The fractional packet transport and the integral nonsynchronized flag flow
therefore occupy the same scalar point.  The question is purely whether
the packet bundles can be rounded without losing the target outputs.

## 5. The coupled packet matrix is not totally unimodular

For a packet \(P=(U,\pi)\), let its middle incidence column have a one in
row \(X\in\binom{[2m]}m\) exactly when \(X\) is a cyclic \(m\)-interval of
\(\pi\).  The following minor occurs inside one calibrated top.

### Theorem 5.1 (genuine determinant-two packet minor)

For all sufficiently large \(m\), the packet-versus-owner incidence matrix
contains the minor (0.4).

#### Proof

The calibrated depth tends to infinity, so assume \(H\ge4\).  Choose
disjoint sets and points

\[
 |C|=m-1,\qquad |F|=H-2,\qquad a,b,c\notin C\cup F,
\tag{5.1}
\]

and put

\[
 U=C\cup F\cup\{a,b,c\},\qquad
 X_a=C+a,\quad X_b=C+b,\quad X_c=C+c.
\tag{5.2}
\]

Split \(F=F^-\sqcup F^+\) with both parts nonempty.  For a pair
\(\{i,j\}\subset\{a,b,c\}\), let \(k\) be the third point and take the
cyclic order

\[
 i,\ F^-,\ k,\ F^+,\ j,\ C,
\tag{5.3}
\]

with arbitrary internal orders inside the displayed blocks.  Call its
packet \(P_{ij}\).

The complement in \(U\) of \(X_i\) is

\[
 F\cup\{j,k\}=F^-,k,F^+,j,
\]

a cyclic \(H\)-interval in (5.3).  The complement of \(X_j\) is

\[
 F\cup\{i,k\}=i,F^-,k,F^+,
\]

also a cyclic \(H\)-interval.  Hence \(X_i,X_j\) are cyclic
\(m\)-intervals and belong to \(P_{ij}\).

The complement of \(X_k\) is \(F\cup\{i,j\}\).  Its elements are separated
by the omitted point \(k\) on one cyclic arc and by the nonempty block
\(C\) on the other.  Because both \(F^-\) and \(F^+\) are nonempty, it is
not a cyclic interval.  Hence \(X_k\notin P_{ij}\).

On the rows \(X_a,X_b,X_c\) and columns
\(P_{ab},P_{ac},P_{bc}\), the incidence matrix is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
\]

whose determinant is \(-2\). \(\square\)

The same three terminal variables occur in the order-prefix extension of
Section 4.  Appending equations for their owner-incidence outputs therefore
inserts this minor into the natural extended constraint matrix.  The order
flow block remains TU, but the coupled matrix does not.

This theorem rules out ordinary total unimodularity of the natural packet
configuration formulation.  It does not rule out a presently unknown,
substantially different integral extended formulation.

## 6. Raw packet supports are not polymatroid bases

Fix a top \(U\).  Let \(\mathscr B_U\) be the family of distinct middle
owner supports of its cyclic packets, viewed as \(0\)-\(1\) vectors on
\(\binom Um\).

### Theorem 6.1 (one-unit exchange obstruction)

The family \(\mathscr B_U\) is not the integer base family of a
polymatroid.  In particular it is not the base family of a matroid.

#### Proof

Every packet consists of \(M\) sliding \(m\)-windows.  Each coordinate
\(u\in U\) belongs to exactly \(m\) of them.  Thus every
\(P\in\mathscr B_U\) satisfies the point-margin identities

\[
 \sum_{X\in P}{\bf1}_{u\in X}=m
 \qquad(u\in U).
\tag{6.1}
\]

Take two distinct packet supports \(P,Q\), and choose \(X\in P-Q\).  If
the integer polymatroid base-exchange axiom held, there would be some
\(Y\in Q-P\) for which

\[
 P'=P-X+Y
\tag{6.2}
\]

were another integer base, hence another packet support.  Comparing (6.1)
for \(P\) and \(P'\) gives

\[
 {\bf1}_{u\in X}={\bf1}_{u\in Y}\qquad(u\in U),
\]

so \(X=Y\), contrary to \(X\in P-Q\) and \(Y\in Q-P\).  Thus no required
one-unit exchange exists. \(\square\)

Consequently the packet synchronization constraint cannot be inserted into
the flag flow by declaring each top catalog to be an integral polymatroid
base and invoking polymatroid union or box-integrality.  A direct
two-polymatroid-intersection theorem also has no identified pair of
submodular rank functions to which it applies.  The theorem does not
exclude a non-obvious enlargement of the state space whose projection is
the packet polytope; it excludes the raw catalog criterion.

## 7. The exact bounded-defect configuration LP

For each top \(U\), let \(\Pi(U)\) be its rooted cyclic orders.  For
\(\pi\in\Pi(U)\), define

\[
 b_{r,T}(U,\pi)
 =\begin{cases}
 1,&T\in\mathcal I_r(U,\pi),\\
 0,&T\notin\mathcal I_r(U,\pi).
 \end{cases}
\tag{7.1}
\]

An integral one-packet-per-top selection is a vector
\(z_{U,\pi}\in\{0,1\}\) satisfying

\[
 \sum_{\pi\in\Pi(U)}z_{U,\pi}=1\qquad(U\in\mathcal U).
\tag{7.2}
\]

Its rank loads are

\[
 y_{r,T}(z)=
 \sum_{U,\pi}b_{r,T}(U,\pi)z_{U,\pi}.
\tag{7.3}
\]

Since every packet supplies \(M\) targets at every proper band rank,

\[
 \sum_Ty_{r,T}(z)=S.
\tag{7.4}
\]

Define its excess-hole discrepancy by

\[
 \boxed{
 \delta(z)=\sum_{r\in\mathcal J}
 \left[
   \min\{N(r),S\}-\#\{T:y_{r,T}(z)>0\}
 \right].}
\tag{7.5}
\]

Every summand is nonnegative by (7.4).

### Proposition 7.1 (zero fractional optimum, exact integral objective)

Consider the linear program

\[
 \sum_{\pi}x_{U,\pi}=1,\qquad x_{U,\pi}\ge0,
\tag{7.6}
\]

\[
 y_{r,T}=\sum_{U,\pi}b_{r,T}(U,\pi)x_{U,\pi},
\tag{7.7}
\]

\[
 0\le h_{r,T}\le1,qquad h_{r,T}\le y_{r,T},
\tag{7.8}
\]

with objective

\[
 \Delta(x,h)=
 \sum_{r\in\mathcal J}
 \left[
   \min\{N(r),S\}-\sum_Th_{r,T}
 \right].
\tag{7.9}
\]

Its optimum is zero.  If \(x=z\) is integral, minimizing over \(h\) gives
exactly \(\Delta(z,h)=\delta(z)\).

#### Proof

For every feasible point,

\[
 \sum_Th_{r,T}\le N(r)
 \quad\hbox{and}\quad
 \sum_Th_{r,T}\le\sum_Ty_{r,T}=S,
\]

so the objective is nonnegative.

Set \(x_{U,\pi}=1/(M-1)!\).  Proposition 4.1 gives

\[
 y_{r,T}=\mu_r={S\over N(r)}.
\]

Taking

\[
 h_{r,T}=\min\{1,\mu_r\}
\]

makes the rank-\(r\) sum of the \(h\)'s equal to
\(\min\{N(r),S\}\).  Hence \(\Delta=0\).

If \(x=z\) is integral, then every \(y_{r,T}\) is a nonnegative integer.
The optimal choice in (7.8) is consequently
\(h_{r,T}={\bf1}_{y_{r,T}>0}\), which turns (7.9) into (7.5). \(\square\)

Theorem 3.1 attains the analogue of \(\delta=0\) integrally in the larger
nonsynchronized path-flow polytope: if \(\mu_r<1\), its loads are zero or
one and it hits exactly \(S\) targets; if \(\mu_r\ge1\), every target has
load at least one.  Thus all of the integrality gap in Proposition 7.1 is
caused by requiring the \(M\) paths at each top to form one cyclic packet.

### Proposition 7.2 (\(o(W)\) discrepancy is sufficient)

Let

\[
 \delta_{m,H}=\min\{\delta(z):z\hbox{ satisfies }(7.2)\}.
\tag{7.10}
\]

If \(\delta_{m,H}=o(W)\), then the calibrated packet construction has only
\(o(W)\) aggregate holes in the controlled band.

#### Proof

For every integral selection, the exact number of missing controlled-band
targets is

\[
 \begin{aligned}
 \sum_{r\in\mathcal J}\left[N(r)-\#\{T:y_{r,T}>0\}\right]
 &={}
 \sum_{r\in\mathcal J}(N(r)-S)_+ +\delta(z).
 \end{aligned}
\tag{7.11}
\]

It remains to bound the scalar first term.  At ranks \(r=m\pm q\),

\[
 \mu_r={\lambda_q\over c}.
\tag{7.12}
\]

Let \(Q=\max\{q\le H:\lambda_q\le c\}\).  From
\(\log\lambda_q\ge q^2/(m+q)\) and \(\log c=O(H/m)\), one obtains

\[
 Q=O(\sqrt H).
\tag{7.13}
\]

Only at most \(2Q+1\) ranks have \(N(r)\ge S\), and at each of them

\[
 0\le N(r)-S\le W-S=D=O(WH/m).
\]

Therefore

\[
 \sum_{r\in\mathcal J}(N(r)-S)_+
 =O\!\left({WH^{3/2}\over m}\right)=o(W).
\tag{7.14}
\]

Combining (7.11), (7.14), and the hypothesis proves the claim. \(\square\)

Cutting one promotion cycle per top has toll \(2HN_H=o(W)\), and the two
outer tails have size \(O(W/H)=o(W)\).  Thus (7.10) with value \(o(W)\)
is sufficient for the coefficient-one conclusion.  It is strictly weaker
than demanding a perfect matching in every augmented clone class.

At the middle, (7.5) has a particularly transparent meaning.  Since there
are \(S\) middle occurrences,

\[
 \delta_m(z)
 =S-\#\{X:y_{m,X}>0\}
 =\sum_X(y_{m,X}-1)_+.
\tag{7.15}
\]

It is exactly the middle-owner collision excess.

## 8. Why generic rounding does not yet close (7.10)

### 8.1 Independent top rounding has linear defect

Choose one uniform cyclic order independently at every top.  Fix an owner
\(X\).  It belongs to

\[
 K=\binom mH
\tag{8.1}
\]

tops.  Inside a fixed containing top, the probability that \(X\) is one of
the \(M\) cyclic \(m\)-windows is

\[
 p={m!H!\over(M-1)!}={M\over\binom Mm}.
\tag{8.2}
\]

The identity (2.2) gives

\[
 Kp={S\over W}={1\over c}=1-o(1),
\tag{8.3}
\]

while \(p=o(1)\).  Independence across tops therefore yields

\[
 \Pr(X\hbox{ is uncovered})=(1-p)^K
 =\exp(-Kp+O(Kp^2))=e^{-1}+o(1).
\tag{8.4}
\]

By linearity of expectation, the expected number of uncovered middle
owners is \((e^{-1}+o(1))W\).  Independent rounding is therefore a linear
distance from (7.10).

### 8.2 The raw polymatroid route is unavailable

Theorem 6.1 rules out the exact hypothesis needed for polymatroid-union or
box-integrality rounding on the packet supports.  Enlarging to the order
network restores local integrality, but the determinant-two output minor
of Theorem 5.1 remains after the global target rows are added.

### 8.3 The full-band generic nibble regime is unavailable

If every controlled-rank occurrence is made a capacity vertex, with the
standard mandatory-clone/overflow augmentation at loads exceeding one, a
decorated packet edge has rank

\[
 R=1+2HM.
\tag{8.5}
\]

Under the symmetric fractional packet measure, a prescribed middle owner
and a prescribed one-point upper extension have joint fractional mass
\((2+o(1))/m\) after the appropriate clone normalization.  Hence

\[
 R\max_{v\ne w}\Omega(v,w)
 \ge(4+o(1))H\longrightarrow\infty.
\tag{8.6}
\]

Thus a matching theorem whose hypothesis requires edge rank times
normalized pair mass to tend to zero cannot be invoked on the complete
band augmentation.  The owner-only packet hypergraph has much smaller
same-rank codegrees and remains a plausible first-stage near-matching
object, but owner balance alone gives no control of the other summands in
\(\delta(z)\).

These calculations do not disprove a packet-aware dependent rounding or a
nonlocal absorber.  They show exactly why independent rounding, the raw
polymatroid criterion, and the standard growing-rank codegree template do
not supply it.

## 9. Exact surviving theorem

The flow/transport route reduces to the following statement.

> **Packet bounded-defect transport \((\mathrm{PBDT})\).**  At the
> calibrated first-crossing depth (0.1), choose one cyclic order at every
> top so that
> \[
>       \delta(z)=o(W),
> \]
> with \(\delta\) defined by (7.5).

The uniform fractional packet transport has objective zero.  The larger
Boolean flag-flow relaxation has an integral objective-zero point.  The
remaining problem is to round between these two points while respecting
the all-or-none cyclic bundle at every top.

Equivalently, it is the integral discrepancy between

\[
 \left\{
 \begin{array}{c}
 S\text{ individually routed, nested, balanced Boolean paths}\\
 M\text{ paths rooted at each top}
 \end{array}
 \right\}
\]

and

\[
 \left\{
 \begin{array}{c}
 N_H\text{ cyclic-order configurations}\\
 \text{one all-or-none }M\text{-path translate bundle per top}.
 \end{array}
 \right\}
\]

Total unimodularity proves the first set is nonempty.  The order-prefix
network proves every local packet is an integral path state.  The
determinant-two minor and the exchange obstruction show why those two facts
do not imply an integral point in their coupled target-balance section.
Within this flow reduction, no separate scalar, divisibility,
owner-containment, or nested-flow discrepancy remains; all remaining loss
is measured by \(\mathrm{PBDT}\).

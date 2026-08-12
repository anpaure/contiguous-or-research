# The faithful FIFO joint catalogue: exact codegrees, flow collapse, and the growing-rank gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or web input is used.

## 0. Exact scope

Put

\[
 L=2m,\qquad k=m-H,\qquad \ell=m+H,\qquad
 N=\binom{2m}{k},\qquad W=\binom{2m}{m},
\]

and

\[
 \lambda={W\over N}={k!\ell!\over(m!)^2},\qquad
 r=\lfloor\lambda\rfloor.
\]

Assume

\[
 1\le r\le H,\qquad 2H<m,\qquad \gcd(\ell,r)=1.       \tag{0.1}
\]

Thus the ordered-slot permutation \(F_r=S O^{r-1}\) is one \(L\)-cycle,
and one physical orbit has \(L\) root blocks and \(Lr\) elementary middle
owners. The necessary overlapping-collar inequality \(tr\ge2H\) is
satisfied here with \(t=L=2m\), but that inequality is not a sufficiency
theorem. Literal seam closure here comes from return of the complete
ordered state after one \(F_r\)-orbit; it does not make different orbit
columns independently selectable or authorize external target rows.

At the calibrated scale

\[
 H=\lfloor\sqrt{m\log\log m}\rfloor
\]

we have \(r=\log m+O(1)\). All asymptotic statements below are for
sufficiently large \(m\).

The conclusions are:

1. all \(Lr\) owners inside one closed ordered orbit are distinct;
2. every deterministic subdivision of the prescribed \(F_r\) successor
   circulation collapses exactly to whole \(L\)-block orbit variables;
3. the joint root-owner catalogue has exact nearly equal degrees and an
   exact root-saturating fractional matching;
4. all root-root, root-owner, and owner-owner codegrees admit exact
   formulas;
5. at reduced scale the maximum nontrivial relative codegree
   \(\eta_m\) satisfies \(s\eta_m=o(1)\), where
   \(s=L(r+1)\) is the full rank;
6. nevertheless, an independent residual contains no catalogue column
   below density \(e^{-1}-o(1)\) with high probability, and exact state
   conservation prevents rank reduction by deterministic subdivision of
   the prescribed \(F_r\) successor.
7. more strongly, there are exact scalar-compatible,
   coordinate-regular residual root/owner families of positive density
   below \(e^{-1}-o(1)\) whose faithful residual catalogue is empty.

No near-perfect integral packing is claimed.

## 1. Positional normal form and internal simplicity

Index the single \(F_r\)-slot cycle by \(Z=\mathbb Z/L\mathbb Z\).
There is a consecutive interval \(I\subset Z\), \(|I|=k\), consisting
of the ordered exterior/root slots. For \(0\le a<r\), let
\(J_a\subset Z\), \(|J_a|=m\), be the positions whose labels form the
middle owner after the first \(a\) ordinary \(O\)-moves of a block. At
that phase the root has not changed, so

\[
                         J_a\cap I=\varnothing.       \tag{1.1}
\]

If \(b\in Z\) is the block index, the root and owner position sets are,
up to reversing every displayed translation,

\[
                         I+b,\qquad J_a+b.             \tag{1.2}
\]

### Theorem 1.1 (internal owner simplicity)

Under (0.1), the \(Lr\) owner sets in (1.2) are pairwise distinct:

\[
 J_a+b=J_{a'}+b'
 \quad\Longleftrightarrow\quad
 b=b'\pmod L,\quad a=a'.                                \tag{1.3}
\]

#### Proof

Use the cyclic top-slot chart

\[
 u_0=Q_0,\quad
 u_1,\ldots,u_m=P_{m-1},\ldots,P_0,\quad
 u_{m+1},\ldots,u_{\ell-1}=Q_{H-1},\ldots,Q_1.
\]

Let \(c=r^{-1}\pmod\ell\). In the exact \(F_r\)-cycle chart, the top
positions are \(0,\ldots,\ell-1\), and

\[
 I=\{\ell,\ldots,L-1\}.
\]

The complement of the phase-\(a\) owner is

\[
 C_a=I\cup G_a,\qquad
 G_a=\{c(q-a)\pmod\ell:0\le q<H\}.                       \tag{1.4}
\]

Because \(0\le a<r\le H\),

\[
                         0\in G_a,\qquad \ell-1\notin G_a. \tag{1.5}
\]

Suppose \(C_a=C_{a'}+d\), and let \(|d|_L\le m\) be the least cyclic
magnitude. The two \(G\)-sets have size \(H\), so

\[
 |I\mathbin\triangle(I+d)|\le2H.
\]

The left side is \(2\min(|d|_L,k)\). Since \(k>H\),
\(|d|_L\le H\). If \(1\le d\le H\), equality forces

\[
 \{\ell-d,\ldots,\ell-1\}\subseteq G_{a'},
\]

contrary to (1.5). If \(-H\le d\le-1\), it similarly forces
\(\ell-1\in G_a\). Hence \(d=0\).

In the original \(u\)-chart the sets \(G_a\) are rotations by \(-a\)
of one nonempty proper cyclic \(H\)-interval. Such an interval has
trivial rotation stabilizer, so \(a=a'\). Complementing proves
(1.3). \(\square\)

This is also proved, with the complete slot derivation, in
MATH_THEOREM_R_INTERNAL_OWNER_SIMPLICITY_OF_FIFO_REROOT_CYCLE_20260727.md.

An oriented cyclic coordinate order is a bijection
\(\omega:Z\to[2m]\), modulo translation of \(Z\). It determines the
complete ordered triple

\[
 (Q_{b,a}(\omega),P_{b,a}(\omega),E_b(\omega))
\]

at every time, including the FIFO order in \(Q\) and \(E\). The
faithful catalogue column \(C_\omega\) is this full chronological
object. Its capacity support is

\[
 \{\omega(I+b):b\in Z\}
 \ \sqcup\
 \{\omega(J_a+b):b\in Z,\ 0\le a<r\}.                  \tag{1.6}
\]

The first layer consists of root vertices \(\binom{[2m]}k\), and the
second of middle-owner vertices \(\binom{[2m]}m\). Consecutive proper
root intervals are distinct, and Theorem 1.1 handles the owners.
Therefore (1.6) is a simple hyperedge of rank

\[
                         s=L(r+1)=2m(r+1).             \tag{1.7}
\]

The edge must still be indexed by \(\omega\), rather than only by its
unordered support. Different ordered columns with the same projected
support need not have the same queue or seam chronology.

## 2. Faithful flow formulation and exact collapse

Let \(\mathcal S\) be the set of all fully ordered block-start states

\[
 \Sigma=(Q=(q_0,\ldots,q_{H-1});
         P=(p_0,\ldots,p_{m-1});
         E=(e_0,\ldots,e_{k-1})).
\]

Make the directed graph

\[
                         \Sigma\longrightarrow F_r\Sigma.  \tag{2.1}
\]

The arc at \(\Sigma\) carries the root \(E(\Sigma)\) and the \(r\)
middle owners encountered during that macro. Let \(y_\Sigma\) be its
selection variable. The faithful fractional circulation/packing system
is

\[
\begin{aligned}
 y_\Sigma&=y_{F_r^{-1}\Sigma}
       &&(\Sigma\in\mathcal S),                              \tag{2.2}\\
 \sum_{\Sigma:E(\Sigma)=A}y_\Sigma&\le1
       &&\left(A\in\binom{[2m]}k\right),                     \tag{2.3}\\
 \sum_{\Sigma}\sum_{a=0}^{r-1}
 1_{\{P(O^a\Sigma)=U\}}y_\Sigma&\le1
       &&\left(U\in\binom{[2m]}m\right),                     \tag{2.4}\\
 y_\Sigma&\ge0.                                              \tag{2.5}
\end{aligned}
\]

For an integral packing impose \(y_\Sigma\in\{0,1\}\).

### Theorem 2.1 (faithful flow collapse)

Every component of (2.1) is a directed \(L\)-cycle, and (2.2) forces
\(y_\Sigma\) to be constant on it. After eliminating the flow
equations, (2.2)--(2.5) is exactly the fractional set-packing system of
the master columns \(C_\omega\). In particular, subdivision into
bounded or \(O(r)\)-resource macro arcs does not reduce the effective
rank of the integral problem.

#### Proof

The action of \(F_r\) on the \(L\) ordered slots is one \(L\)-cycle by
(0.1). Since state labels are distinct, a state first returns after
exactly \(L\) macros. Thus (2.1) is one-in/one-out and every component
has length \(L\). Successively applying (2.2) makes all arc variables
on a component equal to one variable \(x_\omega\). Summing (2.3) and
(2.4) around that component gives precisely the root and owner
incidences in (1.6). Conversely every master-column solution, copied
to all arcs in its orbit, satisfies (2.2). This is a bijection of the
fractional and integral feasible sets. \(\square\)

The network matrix in (2.2) is totally unimodular by itself. The side
capacity rows (2.3)--(2.4) are the entire difficulty: eliminating the
network rows recovers the growing-rank hypergraph matrix. Coarsening
the state while retaining only projected root arcs destroys the ordered
FIFO datum and reintroduces the proved projected-cycle nonlift
phenomenon. A genuinely branched faithful graph is not ruled out, but
it would require a new literal queue-changing switch between complete
ordered states; deterministic subdivision of \(F_r\) supplies none.

### Theorem 2.2 (arbitrary forward chunks only resegment a whole orbit)

Fix one directed \(F_r\)-orbit and identify its elementary macro arcs
with the directed cycle \(\mathbb Z/L\mathbb Z\). Permit any collection
of faithful forward chunks

\[
                  (i,a):i\longrightarrow i+a\pmod L,
                  \qquad a\in\mathbb Z_{>0},
\tag{2.6}
\]

where the chunk is charged to every elementary macro arc in the
forward interval of length \(a\). Let an integral selection of chunks
be conserved at every fully ordered endpoint state and have total
capacity at most one on every elementary macro arc. Then its restriction
to this orbit is either empty or is a resegmentation of one complete
forward lap. In the latter case every elementary macro arc, and hence
every root and owner in (1.6), is used exactly once.

#### Proof

An integral nonnegative circulation decomposes into directed cycles of
selected chunks. On one such directed cycle, lift the successive states
from \(\mathbb Z/L\mathbb Z\) to \(\mathbb Z\). If its chunk lengths
are \(a_1,\ldots,a_q>0\), closure says

\[
                         a_1+\cdots+a_q=wL
\tag{2.7}
\]

for an integer winding number \(w\ge1\). Expanding the chunks therefore
walks forward around the elementary \(L\)-cycle exactly \(w\) times and
uses every elementary macro arc exactly \(w\) times. Capacity one forces
\(w=1\), and it also prevents a second nonempty circulation cycle on the
same orbit. Thus the selected chunks merely partition one full lap.
\(\square\)

The positivity and forward-expansion hypotheses in Theorem 2.2 are
essential. A new exact packet could escape only by an ordered
queue-changing transition, or by a signed physical relation whose
negative terms are installed simultaneously and whose full seam ledger
is proved. Projected cancellation is not such a transition.

## 3. Exact singleton degrees and fractional optimum

There are \((L-1)!\) oriented cyclic coordinate orders.

### Theorem 3.1 (joint singleton degrees)

Every root has degree

\[
                         D_R=k!\ell!,                       \tag{3.1}
\]

and every middle owner has degree

\[
                         D_M=r(m!)^2.                       \tag{3.2}
\]

Consequently

\[
 {D_R\over D_M}={\lambda\over r},
 \qquad
 1\le{D_R\over D_M}<1+{1\over r}.                          \tag{3.3}
\]

The uniform fractional assignment

\[
                         x_\omega={1\over D_R}              \tag{3.4}
\]

saturates every root exactly and loads every middle owner by

\[
                         {D_M\over D_R}={r\over\lambda}\le1. \tag{3.5}
\]

Its total mass is \(N/L\), the largest possible fractional matching
mass allowed by root capacity.

#### Proof

For (3.1), place a fixed \(k\)-set in the root interval and order it
and its complement. For (3.2), count owner incidences in two ways.
There are \((L-1)!\) columns, each with \(Lr\) distinct owners, while
the symmetric group is transitive on the \(W\) owners. Hence

\[
 {(L-1)!Lr\over W}={L!r\over W}=r(m!)^2.
\]

Equation (3.3) is the definition of \(\lambda\), and (3.4)--(3.5)
follow. Finally

\[
 {(L-1)!\over D_R}={N\over L}.
\]

No fractional matching has larger mass, since every column consumes
\(L\) roots and total root capacity is \(N\). \(\square\)

Thus scalar root/owner balance is not the obstruction. Integral
rounding must lose only \(o(N)\) roots while respecting owner capacity
and the ordered orbit equations.

### Corollary 3.2 (exact leave relation and singleton marginals)

Let an integral joint matching contain \(c\) orbit columns. Its root
and owner leaves have sizes

\[
 z=N-Lc,\qquad d=W-Lrc,                                    \tag{3.6}
\]

and satisfy the exact scalar relation

\[
                         d=(\lambda-r)N+rz.                 \tag{3.7}
\]

Every coordinate occurs in exactly

\[
                         {kz\over L}                        \tag{3.8}
\]

root sets of the root leave and in exactly

\[
                         {d\over2}                          \tag{3.9}
\]

owner sets of the owner leave. In particular, the two leaves must be
coordinate-regular. At calibrated scale, \(z=o(N)\) implies
\(d=o(W)\).

#### Proof

In one cyclic coordinate order, each coordinate lies in exactly \(k\)
of the \(L\) root intervals. At each fixed phase it lies in exactly
\(m\) of the \(L\) middle-owner translates, hence in \(mr\) owners
over all phases. The complete root and owner layers have coordinate
degrees \(kN/L\) and \(W/2\), respectively. Subtracting the selected
columns proves (3.8)--(3.9). Equations (3.6)--(3.7) use
\(W=\lambda N\). Finally,

\[
 d\le N+rz=o(rN)=o(W)
\]

when \(z=o(N)\) and \(r\sim\lambda\to\infty\). \(\square\)

## 4. Exact pair-codegree formulas

For \(d\in Z\), put

\[
 \delta(d)=|I\setminus(I+d)|.
\]

If \(q=\min(d,L-d)\in\{0,\ldots,m\}\), then

\[
                         \delta(d)=\min(q,k).                \tag{4.1}
\]

For \(0\le h\le k\), define the positional root-owner census

\[
 a_h=\#\{(a,d):0\le a<r,\ d\in Z,\
                    |I\cap(J_a+d)|=h\}.                    \tag{4.2}
\]

For \(0\le h\le m\), define the ordered owner-owner census

\[
 b_h=\#\{(a,a',d):(a',d)\ne(a,0),\
        |J_a\cap(J_{a'}+d)|=h\}.                            \tag{4.3}
\]

### Theorem 4.1 (exact joint pair incidences)

1. Two distinct roots at Johnson distance \(d\), \(1\le d<k\), have
   codegree

   \[
      2(k-d)!(d!)^2(\ell-d)!,                               \tag{4.4}
   \]

   and relative codegree

   \[
      {2\over\binom kd\binom\ell d}.                        \tag{4.5}
   \]

   Two disjoint roots have codegree

   \[
      (2H+1)(k!)^2(2H)!,                                    \tag{4.6}
   \]

   with relative value \((2H+1)/\binom\ell k\). Hence the exact
   maximum distinct-root relative codegree is

   \[
      \max\left\{{2\over k\ell},
                  {2H+1\over\binom\ell k}\right\}.           \tag{4.6a}
   \]

   At the calibrated scale, the first term is the maximum for all
   sufficiently large \(m\).

2. If a root \(A\) and owner \(U\) satisfy \(|A\cap U|=h\), then

   \[
     \operatorname{codeg}(A,U)
      =a_h\,h!(k-h)!(m-h)!(H+h)!,                           \tag{4.7}
   \]

   and

   \[
     {\operatorname{codeg}(A,U)\over D_R}
      ={a_h\over\binom kh\binom\ell{m-h}}.                  \tag{4.8}
   \]

3. If \(U\ne V\) are owners and \(|U\cap V|=h\), then

   \[
     \operatorname{codeg}(U,V)
      =b_h(h!)^2((m-h)!)^2.                                 \tag{4.9}
   \]

   Writing \(j=m-h\),

   \[
     {\operatorname{codeg}(U,V)\over D_M}
      ={b_h\over r\binom mj^2}.                             \tag{4.10}
   \]

#### Proof

The root-root formulas follow by anchoring the first root interval and
ordering the four consecutive regions.

For (4.7), anchor the root occurrence at \(I\). For each positional
pair counted in \(a_h\), the four membership cells have sizes

\[
 h,\quad k-h,\quad m-h,\quad H+h.
\]

Assigning the corresponding four label cells gives the factorial in
(4.7). Division by (3.1) gives (4.8).

For (4.9), anchor the first owner occurrence and retain its phase
\(a\). The four cells of two middle sets have sizes

\[
 h,\quad m-h,\quad m-h,\quad h.
\]

The anchored positional choices are exactly (4.3), giving (4.9).
Theorem 1.1 gives a unique occurrence of each prescribed owner inside
a column, so occurrence codegree equals column codegree. Division by
(3.2) proves (4.10). \(\square\)

These formulas retain phase and relative block displacement. Replacing
owners by unlabelled clones would erase (4.3) and would not enforce the
physical capacity-one condition.

## 5. Usable bounds from the root interval

Assume \(k\ge2H\), as holds at the calibrated scale.

### Lemma 5.1 (root-owner displacement band)

If \(|I\cap(J_a+d)|=h\), then

\[
                         h\le\delta(d)\le h+H.              \tag{5.1}
\]

Consequently

\[
                         a_h\le r(4H+1).                    \tag{5.2}
\]

#### Proof

The owner \(J_a+d\) is disjoint from its contemporaneous root \(I+d\).
Inside \((I+d)^c\), the \(H\) positions not used by the owner are the
ordered \(Q\)-slots. Thus the \(\delta(d)\) points of
\(I\setminus(I+d)\) contribute all but at most \(H\), and at most all,
to \(I\cap(J_a+d)\). This proves (5.1).

By (4.1), every value below \(k\) has at most two displacements, while
the plateau value \(k\) has \(2H+1\). An interval of \(H+1\) allowed
values therefore contains at most \(4H+1\) displacements. Multiply by
the \(r\) phases. \(\square\)

The denominator in (4.8) obeys

\[
 \binom kh\binom\ell{m-h}\ge\binom\ell H.                  \tag{5.3}
\]

Indeed, the left side is a positive log-concave sequence of \(h\), so
its minimum occurs at an endpoint, and both endpoint values equal
\(\binom\ell H\). Therefore

\[
 {\operatorname{codeg}(A,U)\over D_R}
 \le {r(4H+1)\over\binom\ell H}.                            \tag{5.4}
\]

### Lemma 5.2 (owner-owner displacement band)

Let \(j=m-|J_a\cap(J_{a'}+d)|\). Then

\[
                         |j-\delta(d)|\le H.                \tag{5.5}
\]

Hence

\[
                         b_{m-j}\le r^2(6H+1).              \tag{5.6}
\]

#### Proof

Write

\[
 J_a^c=I\sqcup Q_a,\qquad
 (J_{a'}+d)^c=(I+d)\sqcup Q_{a',d},\qquad
 |Q_a|=|Q_{a',d}|=H.
\]

Complementation preserves Johnson distance. The \(\delta(d)\) points
of \(I\setminus(I+d)\) can lose at most \(H\) to the second \(Q\)-set,
while the first \(Q\)-set can add at most \(H\). This proves (5.5).

The allowed interval of \(\delta\)-values has width at most \(2H\).
Below \(k\), each value has two displacements. If the interval reaches
the plateau \(\delta=k\), the plateau contributes \(2H+1\), and there
are at most \(2H\) lower values because \(k\ge2H\). Thus there are at
most \(6H+1\) displacements per ordered phase pair. \(\square\)

For \(1\le j\le m-1\), (4.10) and (5.6) give

\[
 {\operatorname{codeg}(U,V)\over D_M}
 \le {r(6H+1)\over\binom mj^2}
 \le {r(6H+1)\over m^2}.                                  \tag{5.7}
\]

The endpoint \(j=0\) is equality of owners and is excluded by
Theorem 1.1. The endpoint \(j=m\) is a complementary pair and requires
a separate argument.

## 6. Complementary owners do not co-occur at reduced scale

### Theorem 6.1 (no complementary phase pair)

Assume

\[
 H\ge2,\qquad r\ge2,\qquad r(2H-1)<\ell-1.                 \tag{6.1}
\]

Then no owner template \(J_a+b\) is the complement of another owner
template. Thus \(b_0=0\), and (5.7) bounds every distinct owner pair.

#### Proof

Along the \(F_r\)-cycle, the top slots occur as

\[
 v_z=u_{m+1+rz\pmod\ell},
 \qquad z\in\mathbb Z/\ell\mathbb Z,                        \tag{6.2}
\]

followed by the \(k\) consecutive exterior slots. The \(m\) owner
slots at phase \(a\) form a cyclic interval of length \(m\) in the
\(u\)-order. Hence the \(H\) holes of \(J_a\) inside the top are a set
\(B_a\subset\mathbb Z/\ell\mathbb Z\) whose image under
\(z\mapsto rz\) is a cyclic interval of \(H\) consecutive residues.

We first show that \(J_a\) contains no run of \(k\) consecutive
positions of the full \(F_r\)-cycle. Such a run cannot meet an exterior
slot, because \(J_a\) is top-only. If it existed, all \(H\) top holes
\(B_a\) would lie in the complementary cyclic top interval \(D\) of
length

\[
                         \ell-k=2H.                         \tag{6.3}
\]

But \(rD\) contains no two consecutive residues. Indeed, if two points
of \(D\) with cyclic separation \(1\le q\le2H-1\) had images differing
by \(1\), then

\[
                         rq\equiv\pm1\pmod\ell.
\]

Condition (6.1) gives \(1<rq<\ell-1\), impossible. On the other hand,
\(rB_a\subset rD\) is an interval of \(H\ge2\) consecutive residues,
a contradiction.

Every complement \(J_a^c\) contains the \(k\) exterior slots as a
consecutive run. If \(J_{a'}+d=J_a^c\), the left side would therefore
contain a run of \(k\) consecutive positions, contrary to the preceding
paragraph. \(\square\)

At the calibrated scale \(rH=o(m)\), so (6.1) holds. This is an exact
ordered-template statement, not a random-label heuristic.

## 7. Local overlap scale

Let

\[
                         D_0=\min(D_R,D_M)=D_M.
\]

By (3.3)--(6.1), the maximum distinct-vertex codegree divided by
\(D_0\) is at most

\[
 \eta_m=\max\left\{
 {2(1+1/r)\over k\ell},
 {(1+1/r)(2H+1)\over\binom\ell k},
 {(r+1)(4H+1)\over\binom\ell H},
 {r(6H+1)\over m^2}
 \right\}.                                                  \tag{7.1}
\]

At the calibrated scale,

\[
 \eta_m=O\!\left({rH\over m^2}\right),\qquad
 s\eta_m=O\!\left({r^2H\over m}\right)=o(1).               \tag{7.2}
\]

Thus there is no pair-codegree obstruction. Even after retaining the
full ordered queue, all nontrivial pair overlaps are small on the
\(1/s\) scale. In particular, the projected-arc large codegrees are
not inherited by the genuine full-orbit catalogue.

This is not a matching theorem. The edge rank \(s=2m(r+1)\) tends to
infinity, so a fixed-uniformity matching theorem cannot be diagonalized
without quantitative dependence on \(s\). Even the optimistic
logarithmic pair diagnostic

\[
                         {s\Delta_2\log|V|\over D_0}=o(1)   \tag{7.3}
\]

also fails sharply, where \(|V|=N+W\). Indeed, the distance-one
root-root pair alone gives

\[
\begin{aligned}
 {s\Delta_2\log|V|\over D_0}
 &\ge
 s\,{D_R\over D_0}\,{2\over k\ell}\log(N+W)\\
 &=(8\log2+o(1))r\longrightarrow\infty.                    \tag{7.4}
\end{aligned}
\]

Thus any criterion requiring (7.3) to vanish is unavailable here, even
though \(s\eta_m=o(1)\). The previously audited growing-rank criterion
with an exponential rank loss fails a fortiori; already its factor

\[
                         e^{2s}{2\over k\ell}\log D_R
\]

diverges.

### Theorem 7.1 (unconditional elementary matching bite)

The joint catalogue always has an integral matching of size at least

\[
 \nu\ge
 { (L-1)!\over
   1+L(D_R-1)+Lr(D_M-1)}
 \ge {N\over Ls}
 ={N\over L^2(r+1)}.                                      \tag{7.5}
\]

This covers at least a \(1/s\) fraction of the root layer. The desired
near-factor has \((1-o(1))N/L\) columns, so the elementary guarantee is
short by a factor \(s=2m(r+1)\).

#### Proof

Use the line graph on catalogue columns. A fixed column meets other
columns through any of its \(L\) root vertices or \(Lr\) owner
vertices. Its closed line-graph neighbourhood therefore has size at
most the first denominator in (7.5). Greedy selection of an independent
set gives the first inequality. Since \(D_M\le D_R\), that denominator
is at most

\[
 1+s(D_R-1)\le sD_R.
\]

Finally \((L-1)!/D_R=N/L\). \(\square\)

## 8. Exact obstruction to an independent-residual nibble

Stirling's formula gives

\[
 \log D_R
 =2m\log m-2m+{H^2\over m}
   +O\!\left({H^4\over m^3}+\log m\right),                 \tag{8.1}
\]

whereas

\[
                         s=2m(r+1),\qquad
 {\log D_R\over s}=1+o(1).                                 \tag{8.2}
\]

More generally, if roots and owners are retained independently with
probabilities \(u_R,u_M\), then, conditional on the specified root or
owner itself being retained, its expected residual degree is respectively

\[
 D_Ru_R^{L-1}u_M^{Lr},
 \qquad
 D_Mu_R^Lu_M^{Lr-1}.                                      \tag{8.3}
\]

The scalar proportions of every genuine partial matching obey

\[
 u_M=1-{r\over\lambda}+{r\over\lambda}u_R,                 \tag{8.4}
\]

so \(u_M=u_R+O(1/r)\). In particular, for a common independent
retention probability \(u\), the expected residual degree is at most

\[
                         D_Ru^{s-1}.                        \tag{8.5}
\]

For every fixed \(\varepsilon>0\), (8.5) tends to zero exponentially
when

\[
                         u<e^{-1-\varepsilon}.              \tag{8.6}
\]

There is also a catalogue-wide form. Write
\(\mathcal C=\{C_\omega\}\) for the full oriented column catalogue.
Since

\[
 |\mathcal C|=(L-1)!,
 \qquad
 {\log|\mathcal C|\over s}=1+o(1),                         \tag{8.7}
\]

an independently retained two-part residual has expected surviving
column count

\[
 |\mathcal C|u_R^Lu_M^{Lr}.                                \tag{8.8}
\]

If \(\max(u_R,u_M)\le e^{-1-\varepsilon}\), then (8.8) is
\(\exp[-(\varepsilon-o(1))s]\). By Markov's inequality the residual
contains no catalogue column with probability \(1-o(1)\). Along the
forced scalar line (8.4), the same conclusion holds whenever
\(u_R\le e^{-1-2\varepsilon}\), for all sufficiently large \(m\).

Therefore a nibble whose residual resources are approximately
independently thinned loses its catalogue degrees after only a constant
fraction of resources has been covered. It cannot by itself reach an
\(o(1)\) leave. This is a procedural obstruction to that nibble, not a
proof that a highly correlated packing does not exist.

The same point explains why cutting an orbit into short arcs is
misleading. Independent arc choices may look like a low-rank matching,
but exact queue conservation makes the choices identical around every
whole orbit by Theorem 2.1. A successful proof must maintain a
structured, coordinate-regular residual catalogue rather than an
independently thinned one.

### Theorem 8.1 (exact coordinate-regular dead residuals)

Assume in addition

\[
 H\ge2,\qquad r\ge2,\qquad r(2H-1)<\ell-1,
\tag{8.9}
\]

and take the calibrated scale, so \(r=\log m+O(1)\). For every fixed
\(\varepsilon>0\) and all sufficiently large \(m\), there are residual
families

\[
 {\cal R}\subseteq\binom{[L]}k,\qquad
 {\cal M}\subseteq\binom{[L]}m
\tag{8.10}
\]

and an integer \(c\ge0\) such that

\[
 |{\cal R}|=N-Lc,\qquad
 |{\cal M}|=W-Lrc,
\tag{8.11}
\]

both residuals are exactly coordinate-regular,

\[
 \deg_{\cal R}(x)={k|{\cal R}|\over L},\qquad
 \deg_{\cal M}(x)={|{\cal M}|\over2}
 \quad(x\in[L]),
\tag{8.12}
\]

their two densities are bounded away from zero, the owner density
satisfies

\[
 {|{\cal M}|\over W}<e^{-1-\varepsilon},
\tag{8.13}
\]

and no faithful catalogue column has all its root and owner resources
inside \({\cal R}\sqcup{\cal M}\).

Thus the exact cardinality relation (3.7), all congruences and singleton
leave equations in Corollary 3.2, and positive residual density do not
guarantee even one continuation column.

#### Proof

Set \(u=e^{-1-2\varepsilon}\) and choose

\[
 c=\left\lfloor{(1-u)W\over Lr}\right\rfloor,\qquad
 z=N-Lc,\qquad d=W-Lrc.
\tag{8.14}
\]

Since \(W=\lambda N\) and \(\lambda/r=1+O(1/r)\),

\[
 {z\over N}
 =1-(1-u){\lambda\over r}+o(1)=u+O(1/r),
\qquad
 {d\over W}=u+o(1).
\tag{8.15}
\]

In particular both are positive fixed fractions for large \(m\), and
(8.13) holds.

Let \(\tau=(1\,2\,\cdots\,L)\). Apart from \(o(N)\) root sets, the
\(\langle\tau\rangle\)-orbits on the \(k\)-th layer have full length
\(L\). Indeed, a non-full binary necklace has a proper period at most
\(L/2\), so the number of its labelled words is at most

\[
                         L\,2^{L/2}=o\!\binom Lk
\tag{8.16}
\]

at the calibrated scale. Equation (8.15) therefore leaves at least
\(c\) full root orbits for large \(m\), since

\[
 {c\over N/L}=(1-u){\lambda\over r}+o(1)<1-{u\over2}
\tag{8.16a}
\]

eventually. Remove any \(c\) of them from
the complete root layer and call the remainder \({\cal R}\). Every
full orbit contains each coordinate in exactly \(k\) of its \(L\)
members. Subtracting these orbits from the complete layer proves the
first equation in (8.12), as well as \(|{\cal R}|=z\).

Partition the middle layer into its \(W/2\) complementary pairs

\[
                            \{U,[L]\setminus U\}.
\tag{8.17}
\]

The integer \(d\) is even: \(W=\binom{2m}m\) is even and \(Lrc\) is
even. Choose uniformly \(d/2\) of the pairs in (8.17), and let
\({\cal M}\) be their union. Each chosen pair contains every coordinate
exactly once, so the second equation in (8.12) holds for every choice.

By Theorem 6.1, the \(Lr\) owner vertices of one catalogue column lie
in \(Lr\) distinct complementary pairs. Hence the probability that a
fixed column has all its owners in the random \({\cal M}\) is

\[
 { (d/2)_{Lr}\over (W/2)_{Lr}}
 \le\left({d\over W}\right)^{Lr},
\tag{8.18}
\]

with the left side interpreted as zero if \(d/2<Lr\). The expected
number of columns whose owner support lies in \({\cal M}\) is at most

\[
 (L-1)!\left({d\over W}\right)^{Lr}.
\tag{8.19}
\]

Stirling's formula and \(r=\log m+O(1)\) give

\[
 {\log((L-1)!)\over Lr}
 ={\,\log L-1+o(1)\over r}=1+o(1).
\tag{8.20}
\]

By (8.13), (8.19) is \(\exp[-\Omega_\varepsilon(Lr)]<1\).
Therefore some exact complement-pair choice \({\cal M}\) contains the
complete owner support of no catalogue column. For this choice no
column can lie in \({\cal R}\sqcup{\cal M}\), irrespective of the root
residual. Equations (8.11)--(8.12) were already proved. \(\square\)

Theorem 8.1 is not a nonexistence theorem for a global matching: the
constructed residual pair is not proved to be reachable as the leave
of a partial matching. It is an exact obstruction to every regenerative
argument whose maintained state consists only of the scalar leave,
congruences, and singleton coordinate marginals. A successful rounding
must preserve a stronger catalogue-specific correlation from the start,
or use a literal ordered queue-changing switch.

### Corollary 8.2 (even all unordered Gaussian-depth profiles can look correct)

The residuals in Theorem 8.1 can be chosen so that, uniformly for
every \(1\le q\le H\) and \(T\in\binom{[L]}q\),

\[
\begin{aligned}
 \#\{A\in{\cal R}:T\subseteq A\}
   &=\left({|{\cal R}|\over N}+o(1)\right)
      \binom{L-q}{k-q},\\
 \#\{U\in{\cal M}:T\subseteq U\}
   &=\left({|{\cal M}|\over W}+o(1)\right)
      \binom{L-q}{m-q}.
\end{aligned}
\tag{8.21}
\]

#### Proof

Choose the \(c\) removed full coordinate-shift root orbits uniformly,
and choose the \(d/2\) owner complement-pairs uniformly as in the proof
of Theorem 8.1. For sampling \(p\) blocks without replacement with
weights in \([0,b]\), the exposure martingale gives

\[
 \Pr(|X-\mathbb EX|\ge t)
 \le2\exp\left(-{t^2\over2pb^2}\right).
\tag{8.22}
\]

Use \(b=L\) for root orbits and \(b=1\) for complement-pairs. The
smallest relevant complete inclusion degrees, at \(q=H\), are still
\(\exp(\Theta(m))\). With relative error \(1/\log m\), the two
exponents in (8.22) are \(\exp(\Theta(m))\), whereas the number of
sets \(T\) under consideration is at most \(2^L=\exp(O(m))\).
The non-full root orbits contribute at most
\(L2^{L/2}=o(\binom{L-H}{k-H})\). Hence (8.21) holds with probability
\(1-o(1)\).

The expected number of columns surviving the owner choice remains
\(\exp[-\Omega_\varepsilon(Lr)]\), so with probability \(1-o(1)\)
there is no column. The two events therefore occur simultaneously.
The complete expectation and martingale calculation is given in
MATH_THEOREM_R_FIFO_PROJECTED_LATTICE_HALL_AND_REGULAR_DEAD_RESIDUAL_20260727.md,
Theorem 5.1. \(\square\)

### Corollary 8.3 (linear-order local indistinguishability)

Put \(h=Lr\), \(P=W/2\), \(Q=d/2\), and \(v=Q/P=d/W\) in the
complement-pair construction. Condition the uniform \(Q\)-subset of
the \(P\) owner complement-pairs on the event \({\cal D}\) that no
faithful column owner support survives. Let

\[
 v_0=e^{-1-2\varepsilon},\qquad
 \alpha_\varepsilon={1\over4}\min(v_0,1-v_0),
\]

\[
 \kappa_\varepsilon
 =\min\left\{{1\over4},
 {\varepsilon\over4\log(1/\alpha_\varepsilon)}\right\}.
\tag{8.23}
\]

After adjoining an independent uniformly conjugated
scalar-compatible root residual from Theorem 8.1, this gives an exactly
\(S_L\)-invariant law on joint coordinate-regular dead residuals.
Uniformly for every
\(j\le\kappa_\varepsilon h\), every \(j\) distinct complement-pair
variables, and every prescribed pattern with \(a\) retained and
\(b=j-a\) omitted pairs,

\[
 \Pr(\text{pattern}\mid{\cal D})
 =(1+o(1))v^a(1-v)^b.
\tag{8.24}
\]

#### Proof

The no-complement theorem and (8.18) give

\[
 \delta_m:=\Pr({\cal D}^c)
 \le(L-1)!{(Q)_h\over(P)_h}
 \le(L-1)!v^h
 \le e^{-\varepsilon h}.
\tag{8.25}
\]

The unconditioned probability of the prescribed pattern is exactly

\[
 p_A={ (Q)_a(P-Q)_b\over(P)_j}
 =(1+o(1))v^a(1-v)^b
 \ge\alpha_\varepsilon^j,
\tag{8.26}
\]

uniformly, because \(j=O(h)\) is polynomial while \(P,Q,P-Q\) are
exponential. Moreover,

\[
 |\Pr(A\mid{\cal D})-\Pr(A)|
 \le{\delta_m\over1-\delta_m}.
\]

Dividing by (8.26) and using (8.23) gives a relative error at most

\[
                         2e^{-3\varepsilon h/4}=o(1).
\]

Coordinate permutations preserve both the uniform fixed-size law and
the event \({\cal D}\), proving exact invariance. The full proof,
including the uniform falling-factorial estimate, is Theorem 5.2 of
the projected-lattice companion report. Finally, independently apply a
uniform random coordinate permutation to one fixed scalar-compatible
root residual constructed in Theorem 8.1. Its law is \(S_L\)-invariant,
every realization remains coordinate-regular, and owner-deadness
already excludes every joint column. \(\square\)

## 9. Exact proved/open boundary

The following are proved.

1. The full ordered \(F_r\) trajectory has \(L\) distinct roots and
   \(Lr\) distinct owners.
2. Its faithful one-in/one-out circulation collapses to whole
   \(L\)-block master columns. There is no faithful fixed-uniformity
   reduction merely by subdividing time.
3. The joint catalogue is nearly regular, with exact degrees
   (3.1)--(3.2), and has the exact root-saturating fractional optimum
   (3.4).
4. All three pair-codegree types are given exactly by
   (4.4)--(4.10).
5. Root-interval geometry gives the uniform bounds (5.2), (5.4), and
   (5.7).
6. At reduced scale, complementary middle owners never co-occur in one
   column.
7. The resulting relative codegree satisfies \(s\eta_m=o(1)\).
8. The logarithmic pair diagnostic (7.3) diverges as
   \((8\log2+o(1))r\), the audited exponential-rank criterion also
   fails, and the elementary greedy theorem reaches only a \(1/s\)
   fraction of the roots.
9. An independent-residual nibble has the constant-density
   degree-collapse threshold (8.6); below the corresponding scale the
   entire random residual catalogue is empty by (8.7)--(8.8).
10. Even exact scalar-compatible, coordinate-regular positive-density
    residuals can be catalogue-empty, by Theorem 8.1.
11. Such a dead residual may simultaneously have every unordered
    inclusion profile through \(q=H\) correct up to relative \(o(1)\),
    by Corollary 8.2.
12. After conditioning on deadness, every admissible cylinder involving
    at most \(\kappa_\varepsilon Lr\) complement-pair variables remains
    asymptotically Bernoulli, by Corollary 8.3.

The following remain unproved.

1. A rank-sensitive matching theorem that uses the special orbit
   structure to round (3.4) while retaining a structured residual.
2. A near-perfect integral family with pairwise disjoint roots and
   owners.
3. Residual all-depth target completion, connector installation, and a
   literal contiguous-OR word.

Thus globally owner-simple packing is not refuted by local codegrees.
Its exact remaining form is:

> Round the uniform root-saturating fractional point (3.4) in the
> deterministic orbit system (2.2)--(2.4), losing \(o(N)\) roots and
> respecting every middle-owner capacity, by a correlated procedure
> whose residual is not an independent thinning. Any proposed
> bounded-block flow must either prove this rounding after the orbit
> equalities are eliminated, or exhibit an actual queue-changing
> switch; ordinary network integrality does neither.

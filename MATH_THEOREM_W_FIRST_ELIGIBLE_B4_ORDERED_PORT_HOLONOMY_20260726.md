# First-eligible \(B_4\) packets: ordered ports, whole-factor path closure, and three-seed holonomy

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Verdict

Let

\[
 {\cal M}=\binom{[2m]}m,\qquad
 W=|{\cal M}|=\binom{2m}{m},\qquad
 H\ll r\le m/16,\qquad h=2r,
\tag{0.1}
\]

and use the first-eligible \(B_4\) packet factor. Its retained owner set has
size

\[
 G=W-E,\qquad E=e^{-\Omega(m)}W,
\tag{0.2}
\]

and is partitioned into physical cycles of length

\[
                         2h=4r.
\tag{0.3}
\]

There are two synchronization questions, and they must not be identified.

1. For any fixed union of whole exact packet cycles, ordered-port Hall is
   already solved. If \(d_t=X_t\setminus X_{t+1}\) is the physical deletion
   word, then

   \[
   L_t=(d_t,\ldots,d_{t+H-2};d_{t-1}),\qquad
   R_t=(d_{t+1},\ldots,d_{t+H-1};d_t)=L_{t+1}.
   \tag{0.4}
   \]

   Cut one wrap edge from each cycle and order the remaining vertices
   chronologically, concatenating cycles in any context-dependent order.
   Including the omitted owners as singletons gives

   \[
   \boxed{
      p\le {W-E\over2h}+E={W-E\over4r}+E=o(W/H).}
   \tag{0.5}
   \]

   Hence, conditionally on the unresolved target/Hoffman assignment being
   realizable with whole packet germs, \(p_{\rm Hoff}=o(W/H)\).

2. The first-eligible theorem has not proved that the fixed germs admit the
   required nested lower and upper target assignment. Equation (0.5) does
   not prove nonemptiness of that target/Hoffman feasible set. This remains
   the cross-packet gate.

The three natural \(B_4\) relabellings do not give a free ownerwise escape.
They are the three equators of the octahedron \(J(4,2)\). For the cyclic
relabelings

\[
 \sigma_0={\rm id},\qquad \sigma_1=(234),\qquad \sigma_2=(243),
\tag{0.6}
\]

the exact local reduced ports are computed below. Every whole equator is
port-balanced, but the three have nontrivial phase holonomy:

\[
 (\theta_1-\theta_0)+(\theta_2-\theta_1)
       +(\theta_0-\theta_2)=-3=1\pmod4.
\tag{0.7}
\]

Thus no common \(\mathbb Z_4\) phase is cyclic on all three seeds, although
any two are compatible.

There is also a sharp integral local port cut. If all six local middle
owners are assigned ownerwise to one of the two equators containing them,
then

\[
 \boxed{
 {1\over2}\|R-L\|_1
 ={1\over2}\sum_{s=0}^2\sum_{t\in\mathbb Z_4}
       |z_{s,t}-z_{s,t-1}|\ge2.}
\tag{0.8}
\]

The fractional choice \(z_{s,t}=1/2\) has zero imbalance.

At the global three-atlas level there is a stronger exact run-boundary
potential. Let \(F_s\) be the first-eligible factor made from the \(s\)-th
seed, and let \(c(X)\in\{0,1,2\}\) choose the forward \(F_{c(X)}\)-germ.
Put

\[
 B(c)=\sum_{s=0}^2
 \#\{X:c(X)=s,\ c(F_sX)\ne s\},
\tag{0.9}
\]

with a successor outside the retained common domain counted as a boundary.
Distinct omission classes have no full \(H\ge2\) bridge. Therefore

\[
 \boxed{p(c)=B(c)+Z(c),\qquad 0\le Z(c)\le {W\over2h},}
\tag{0.10}
\]

apart from the exponentially small common-domain leave. Here \(Z(c)\) is
the number of whole \(F_s\)-cycles coloured \(s\). Thus the exact remaining
ordered-port condition for an ownerwise three-atlas Hoffman solution is

\[
                         B(c)=o(W/H).
\tag{0.11}
\]

Current target/Hoffman results do not control (0.9).

The proved boundary is:

\[
\boxed{
 \begin{array}{c}
 \text{whole-factor ordered-port closure: proved at }o(W/H);\\
 \text{ownerwise three-seed synchronization: governed exactly by }B(c);\\
 \text{naive common-phase three-seed overlay: locally obstructed};\\
 \text{nested cross-packet target/Hoffman feasibility: unproved.}
 \end{array}}
\tag{0.12}
\]

No coefficient-one conclusion is claimed.

## 1. The three relabellings and what is canonical

The first-eligible packet theorem itself fixes only

\[
 C_0:\quad14\longrightarrow12\longrightarrow23
       \longrightarrow34\longrightarrow14.
\tag{1.1}
\]

There are twenty-four coordinate relabellings, together with choices of root
and orientation. The canonical unrooted trichotomy is by the omitted
antipodal pair of \(J(4,2)\), equivalently by one of the three perfect
matchings of \([4]\). We use the cyclic representatives (0.6):

\[
\begin{array}{c|c|c}
s&C_s&\text{omitted middle owners}\\ \hline
0&(14,12,23,34)&\{13,24\},\\
1&(12,13,34,24)&\{14,23\},\\
2&(13,14,24,23)&\{12,34\}.
\end{array}
\tag{1.2}
\]

Every two-set belongs to exactly two active alphabets. The three cycles are
the three equators of the octahedron. Their twelve undirected edges are
pairwise disjoint and exhaust the twelve edges of \(J(4,2)\).

Other rooted representatives give coordinate-conjugate versions of the
results below. Equality of reduced coordinate signatures between two such
representatives does not create a physical bridge: a full port also retains
the middle-owner trajectory.

## 2. Exact local shadows and ordered ports

For

\[
 C_s=(X_{s,t}:t\in\mathbb Z_4),
\tag{2.1}
\]

put

\[
 d_{s,t}=X_{s,t}\setminus X_{s,t+1}.
\tag{2.2}
\]

This is the FIFO deletion symbol, not the singleton intersection shadow.
The complete local data are

\[
\begin{array}{c|c|c|c|c}
s&(X_{s,t})&(d_{s,t})
 &(X_{s,t}\cap X_{s,t+1})
 &(X_{s,t}\cup X_{s,t+1})\\ \hline
0&(14,12,23,34)&(4,1,2,3)&(1,2,3,4)
  &(124,123,234,134),\\
1&(12,13,34,24)&(2,1,3,4)&(1,3,4,2)
  &(123,134,234,124),\\
2&(13,14,24,23)&(3,1,4,2)&(1,4,2,3)
  &(134,124,234,123).
\end{array}
\tag{2.3}
\]

In particular, \((1,2,3,4)\) in the original seed theorem is the lower
singleton-shadow list for \(C_0\); the deletion word is \((4,1,2,3)\).

### 2.1 The isolated depth-two projection

If two consecutive local steps of one displayed equator are read in
isolation, then at \(X_{s,t}\)

\[
 \beta_1=d_{s,t-1},\qquad
 \alpha_1=d_{s,t},\qquad
 \alpha_2=d_{s,t+1}.
\tag{2.4}
\]

Thus

\[
 L_{s,t}=(d_{s,t};d_{s,t-1}),\qquad
 R_{s,t}=(d_{s,t+1};d_{s,t})=L_{s,t+1}.
\tag{2.5}
\]

Writing \(ab\to cd\) for \(L=(a,b)\), \(R=(c,d)\), the exact table is

\[
\begin{array}{c|cccc}
C_0&14:43\to14&12:14\to21&23:21\to32&34:32\to43,\\
C_1&12:24\to12&13:12\to31&34:31\to43&24:43\to24,\\
C_2&13:32\to13&14:13\to41&24:41\to24&23:24\to32.
\end{array}
\tag{2.6}
\]

Each row is a directed cycle of port equalities and has equal left and
right histograms.

The full \(H=2\) physical ports retain the two middle owners:

\[
 \ell^{\rm full}_{s,t}=(X_{s,t},X_{s,t+1}),\qquad
 r^{\rm full}_{s,t}=(X_{s,t+1},X_{s,t+2}).
\tag{2.7}
\]

The three equators partition the physical edge set, so their full local
port alphabets are disjoint.

### 2.2 The actual protected-depth port

In the packet factor, the two cube directions belonging to one \(B_4\)
block are separated in the recursive Hamming chronology. A protected
window of length at most \(r\) touches a local block at most once. Therefore
(2.6) is a local projection, not the literal chronology of a global
protected window.

Let

\[
 X_0,X_1,\ldots,X_{2h-1},X_{2h}=X_0
\tag{2.8}
\]

be an actual physical packet cycle and put

\[
                         d_t=X_t\setminus X_{t+1}.
\tag{2.9}
\]

For the forward \(H\)-germ rooted at \(X_t\),

\[
 \alpha_j(X_t)=d_{t+j-1}\quad(1\le j\le H),\qquad
 \beta_1(X_t)=d_{t-1}.
\tag{2.10}
\]

Hence

\[
 \boxed{
 \begin{aligned}
 L_t&=(d_t,d_{t+1},\ldots,d_{t+H-2};d_{t-1}),\\
 R_t&=(d_{t+1},d_{t+2},\ldots,d_{t+H-1};d_t)=L_{t+1}.
 \end{aligned}}
\tag{2.11}
\]

The local seed table supplies the one coordinate \(d_j\) when its block is
touched. The other entries come from neighboring global block phases. Thus
a local relabelling alone does not determine a full protected-depth port.

## 3. The specialized ordered-port Hall problem

Let \(U\) be the retained owner set. For each \(X\in U\), take the forward
physical \(H\)-state \(\omega_X\) on its packet cycle. For a total order
\(\prec\), form the split-copy bridge graph

\[
 B_\prec=(U_L,U_R;E_\prec),
\tag{3.1}
\]

where \(X_LY_R\) is an edge when the full exit port of \(\omega_X\) equals
the full entrance port of \(\omega_Y\) and \(X\prec Y\). Its exact Hall
deficiency is

\[
 p(U,\prec)=|U|-\nu(B_\prec)
 =\max_{S\subseteq U}\bigl(|S|-|N_{B_\prec}(S)|\bigr).
\tag{3.2}
\]

### Theorem 3.1 (whole-cycle ordered-port closure)

Suppose \(U\) is partitioned into physical \(C_{2h}\)'s and the selected
states are their forward \(H\)-germs. Then some context-dependent total
order \(\prec\) satisfies

\[
 \boxed{
 \max_{S\subseteq U}\bigl(|S|-|N_{B_\prec}(S)|\bigr)
 \le {|U|\over2h}.}
\tag{3.3}
\]

The complete left and right port histograms are exactly equal.

#### Proof

Choose one cut phase in each cycle. Order each resulting list
chronologically, and concatenate the lists in any order depending on their
packet indices and frozen exteriors. Every nonwrap successor
\(X_t\to X_{t+1}\) increases \(\prec\), and (2.11) gives

\[
                         R_t=L_{t+1}.
\tag{3.4}
\]

These arcs form a split-copy matching with \(2h-1\) edges per cycle. Since
there are \(|U|/(2h)\) cycles, its size is

\[
                         |U|-{|U|\over2h}.
\tag{3.5}
\]

Equation (3.2) proves (3.3). Before cutting, (3.4) is a cyclic bijection
from the multiset of exits to the multiset of entrances, proving equality
of the two histograms. \(\square\)

### Corollary 3.2 (the exact first-eligible bound)

Pay the \(E\) omitted owners as singletons. Then

\[
 p\le {W-E\over2h}+E,
\tag{3.6}
\]

and

\[
 {p\over W/H}
 \le {H\over2h}+{EH\over W}
 ={H\over4r}+e^{-\Omega(m)}H=o(1).
\tag{3.7}
\]

The exact full-radius path compiler therefore pays

\[
 (2H+1)p
 \le (2H+1)\left({W-E\over2h}+E\right)=o(W).
\tag{3.7a}
\]

Attaching nested radius labels to the fixed germs does not change this:
an owner of short radius retains its physical forward extension; only its
later target incidences are ignored.

### Corollary 3.3 (conditional \(p_{\rm Hoff}\) theorem)

Let \({\cal H}_{B_4}^{\rm fixed}\) be the set of integral nested
target/Hoffman assignments using the fixed forward germs. If

\[
                         {\cal H}_{B_4}^{\rm fixed}\ne\varnothing,
\tag{3.8}
\]

then

\[
                         p_{\rm Hoff}=o(W/H).
\tag{3.9}
\]

The same conclusion holds if a target solution chooses one whole exact
\(C_{2h}\)-factor in each owner-disjoint packet or cell.

#### Proof

Apply Corollary 3.2 to the whole factors used by the target solution.
Hoffman constraints decide which target incidences are retained; they do
not destroy successor bridges inside a selected whole factor. \(\square\)

Hypothesis (3.8) is not proved here. It is the unresolved cross-packet
target synchronization.

## 4. Nonzero phase holonomy of the three equators

Normalize phases by

\[
\begin{array}{c|cccc}
C_0&\theta_0(14)=0&\theta_0(12)=1&
     \theta_0(23)=2&\theta_0(34)=3,\\
C_1&\theta_1(12)=0&\theta_1(13)=1&
     \theta_1(34)=2&\theta_1(24)=3,\\
C_2&\theta_2(13)=0&\theta_2(14)=1&
     \theta_2(24)=2&\theta_2(23)=3.
\end{array}
\tag{4.1}
\]

On pairwise overlaps,

\[
\begin{aligned}
 \theta_1-\theta_0&=-1
       &&\text{on }C_0\cap C_1=\{12,34\},\\
 \theta_2-\theta_1&=-1
       &&\text{on }C_1\cap C_2=\{13,24\},\\
 \theta_0-\theta_2&=-1
       &&\text{on }C_2\cap C_0=\{14,23\}.
\end{aligned}
\tag{4.2}
\]

### Theorem 4.1 (three-seed phase obstruction)

There are no constants \(c_0,c_1,c_2\in\mathbb Z_4\) for which the shifted
phases \(\theta_s+c_s\) agree on every overlap. Equivalently, the three
displayed successors admit no common owner phase which advances by one on
every seed edge. Any two seeds are compatible.

#### Proof

The constancy in (4.2) proves pairwise compatibility. Around the triangle
of seeds, the transition constants sum to

\[
                         -1-1-1=-3=1\pmod4.
\tag{4.3}
\]

Adding \(c_1-c_0,c_2-c_1,c_0-c_2\) does not alter this sum. Thus all three
overlap differences cannot vanish. \(\square\)

This is orientation-independent. A cyclic \(\mathbb Z_4\) phase on an
equator gives opposite vertices equal parity and adjacent vertices opposite
parity. The three antipodal pairs of \(J(4,2)\) would receive three parity
values, with every two opposite. That would 2-colour a triangle.

Thus a genuine three-seed overlay needs an additional phase state or a seam
on every seed-transition loop carrying nonzero holonomy. This alone gives
no coefficient-scale lower bound because no result forces
\(\Omega(W/H)\) edge-disjoint nonzero-holonomy loops.

## 5. The sharp six-owner integral port potential

For \(s\in\{0,1,2\}\) and \(t\in\mathbb Z_4\), let

\[
 z_{s,t}\in\{0,1\}
\tag{5.1}
\]

mean that owner \(X_{s,t}\) uses the pure forward germ of seed \(s\). Exact
owner selection is

\[
 \sum_{s:X\in C_s}z_{s,X}=1
 \qquad\left(X\in\binom{[4]}2\right).
\tag{5.2}
\]

Define

\[
 I(z)={1\over2}\sum_{s=0}^2\sum_{t\in\mathbb Z_4}
          |z_{s,t}-z_{s,t-1}|.
\tag{5.3}
\]

### Theorem 5.1 (sharp local integral imbalance)

Every integral section satisfying (5.2) obeys

\[
 \boxed{I(z)={1\over2}\|R_z-L_z\|_1\ge2.}
\tag{5.4}
\]

The constant two is sharp. The fractional section

\[
 z_{s,X}={1\over2}\qquad(X\in C_s)
\tag{5.5}
\]

satisfies (5.2) and has \(I(z)=0\).

#### Proof

Let

\[
 e_{s,t}=(X_{s,t},X_{s,t+1})
\tag{5.6}
\]

be the full local entrance label. Its entrance multiplicity is \(z_{s,t}\),
while its exit multiplicity is \(z_{s,t-1}\). The equators partition the
twelve physical edges, so these labels are distinct. Hence

\[
 {1\over2}\|R_z-L_z\|_1
 ={1\over2}\sum_{s,t}|z_{s,t-1}-z_{s,t}|=I(z).
\tag{5.7}
\]

A nonconstant cyclic binary word contributes at least one to \(I\). If at
least two seed words are nonconstant, (5.4) follows.

Suppose only \(z_2\) is nonconstant and write the other constants as
\(c_0,c_1\). On \(C_0\cap C_1\), (5.2) gives \(c_0+c_1=1\). On the two
vertices of \(C_0\cap C_2\), it gives \(z_2=1-c_0\); on the two vertices
of \(C_1\cap C_2\), it gives \(z_2=1-c_1=c_0\). Those pairs alternate
around \(C_2\), so \(z_2\) is \(0101\) or \(1010\), contributing two.

Taking \(c_0=1,c_1=0\) shows sharpness. The fractional choice (5.5) is
constant on every seed and gives \(1/2+1/2=1\) at every owner. \(\square\)

By the general port cut, any path cover of this pure local menu has at
least two components. This is an exact integral obstruction invisible at
the balanced fractional point.

## 6. The exact global three-atlas run-boundary theorem

For \(s=0,1,2\), apply the relabelled seed \(C_s\) to every physical
four-block and perform the first-\(r\)-eligible construction. This gives a
global factor \(F_s\) on a good invariant set \(U_s\), with

\[
                         |{\cal M}\setminus U_s|
                         =e^{-\Omega(m)}W.
\tag{6.1}
\]

Put

\[
 U=U_0\cap U_1\cap U_2.
\tag{6.2}
\]

Then

\[
                         |{\cal M}\setminus U|
                         \le3e^{-\Omega(m)}W.
\tag{6.3}
\]

For an ownerwise choice \(c:U\to\{0,1,2\}\), select at \(X\) the forward
\(H\)-germ of \(F_{c(X)}\). Define \(B(c)\) by (0.9), interpreting
\(c(F_sX)\ne s\) whenever \(F_sX\notin U\). Let \(Z(c)\) be the number of
full \(F_s\)-cycles all of whose owners lie in \(U\) and have colour \(s\).

### Lemma 6.1 (different omission classes have no full bridge)

Assume \(H\ge2\). If the state at \(X\) uses \(F_s\) and the state at
\(Y\) uses \(F_t\), and these states bridge, then \(s=t\) and \(Y=F_sX\).

#### Proof

A bridge first forces

\[
                         Y=F_sX.
\tag{6.4}
\]

Because \(H\ge2\), it also forces

\[
                         F_tY=F_s^2X.
\tag{6.5}
\]

Thus the outgoing physical transition from \(Y\) under \(F_t\) must equal
the outgoing transition from \(Y\) under \(F_s\). Each transition changes
one selected four-block along an edge of the corresponding equator.

If the two transitions touch different disjoint blocks, their resulting
middle sets differ. If they touch the same block, equality would give a
common edge of \(C_s\) and \(C_t\). The three equators in (1.2) have
disjoint edge sets, so this is impossible for \(s\ne t\). Therefore
\(s=t\), and (6.4) gives the stated successor. \(\square\)

### Theorem 6.2 (exact run-boundary formula)

For the selected state vector \(c\), the minimum compatible path-cover
number is

\[
                         \boxed{p(c)=B(c)+Z(c).}
\tag{6.6}
\]

Moreover,

\[
                         0\le Z(c)\le {|U|\over2h}.
\tag{6.7}
\]

#### Proof

Put

\[
                         A_s=\{X\in U:c(X)=s\}.
\tag{6.8}
\]

By Lemma 6.1, the bridge digraph is exactly the disjoint union, over \(s\),
of the arcs

\[
                         X\longrightarrow F_sX
\quad\text{with }X,F_sX\in A_s.
\tag{6.9}
\]

On an \(F_s\)-cycle, the induced graph on \(A_s\) is a disjoint union of
directed runs, unless the whole cycle is selected. Every proper nonempty
run has exactly one final owner \(X\) with \(F_sX\notin A_s\). Hence the
number of proper runs over all seeds is exactly \(B(c)\). Every wholly
selected cycle contributes one additional path component after one wrap
edge is cut. This proves (6.6).

Whole selected cycles for different seeds are owner-disjoint because the
sets \(A_s\) partition \(U\). Each contains \(2h\) owners, proving (6.7).
\(\square\)

### Corollary 6.3 (exact three-atlas ordered-Hall gate)

Let \({\cal H}_{B_4}^{(3)}\) be the set of integral target/Hoffman-feasible
ownerwise choices from the three global atlases. Up to the leave in (6.3),

\[
 p_{\rm Hoff}^{(3)}
 =\min_{c\in{\cal H}_{B_4}^{(3)}}\bigl(B(c)+Z(c)\bigr).
\tag{6.10}
\]

Since \(H/h\to0\),

\[
 \boxed{
 p_{\rm Hoff}^{(3)}=o(W/H)
 \quad\Longleftrightarrow\quad
 \min_{c\in{\cal H}_{B_4}^{(3)}}B(c)=o(W/H),}
\tag{6.11}
\]

provided the feasible set is nonempty.

Thus no further choice of total order can repair a Hoffman colouring with
macroscopic \(B(c)\). Conversely, ordering every monochromatic run
chronologically realizes (6.6).

Equation (6.11) is the requested exact ordered-port Hall recasting. The
unproved positive lemma is a near-cycle-invariant target/Hoffman colouring,
not merely a depthwise target Hall theorem.

## 7. Why the finite local obstruction does not tensor automatically

Two tempting deductions from Section 5 are invalid.

First, choosing a two-letter deletion word for all six middle owners of one
\(B_4\) orients the six edges of \(K_4\). Every coordinate has odd degree
three, so exact Euler balance is impossible. That valid SCD-extension
obstruction does not apply to one selected first-eligible block: its four
active restrictions already form an Eulerian directed four-cycle, while
the two omitted restrictions acquire later eligible blocks globally.

Second, every protected window \(q\le H\ll r\) touches a given block at
most once. The consecutive same-block deletions used in the isolated table
(2.6) do not occur in the actual protected queue. Summing \(I(z)\) over
all coordinate blocks would introduce artificial interfaces and
double-count global path ends.

The global potential \(B(c)\) in Section 6 avoids that error because it is
defined on actual full successor germs. However, current target/Hoffman
theorems neither prove \(B(c)=o(W/H)\) nor force \(B(c)=\Omega(W/H)\).

## 8. The exact remaining target gate

For the fixed factor \(F\), put

\[
 \tau^-_{q,F}(X)=\bigcap_{j=0}^qF^jX,\qquad
 \tau^+_{q,F}(X)=\bigcup_{j=0}^qF^jX.
\tag{8.1}
\]

The fixed-germ problem is to choose

\[
 \bar\rho:U\longrightarrow\{0,1,\ldots,H\},\qquad
 U_q=\{X\in U:\bar\rho(X)\ge q\},
\tag{8.2}
\]

with

\[
 |U_q|=N_q+e_q,\qquad \sum_{q=0}^H|e_q|=o(W),
\tag{8.3}
\]

such that the lower and upper maps (8.1), restricted to \(U_q\), have
aggregate baseline-relative defect \(o(W)\) through all \(q\le H\).
Equivalently, one needs the corresponding exact layered Hoffman
inequalities for these fixed germs.

If this holds, Theorem 3.1 gives the path bound automatically. If one uses
ownerwise three-atlas states instead, Section 6 adds the exact condition
\(B(c)=o(W/H)\). If one constructs new whole factors by a multi-state phase
lift or associator, Theorem 3.1 again applies directly to those whole
factors.

What is ruled out is the shortcut “choose one of the three seeds
independently at every owner and impose one common phase”: Theorems 4.1 and
5.1 obstruct it exactly.

## 9. Audit summary

1. The FIFO deletion word is \(X_t\setminus X_{t+1}\), not the singleton
   intersection list.
2. The three unrooted omission classes are canonical; rooted
   representatives are not. We fixed the cyclic \(C_3\)-orbit (0.6).
3. Reduced coordinate-port equality is only necessary. Full ports retain
   the owner trajectory.
4. Every whole exact factor is port-balanced. The context-dependent
   chronological order proves \((W-E)/(4r)+E=o(W/H)\).
5. This only conditionally bounds \(p_{\rm Hoff}\), because the
   target/Hoffman feasible set is not known nonempty for the fixed germs.
6. The three-seed phase holonomy is nonzero, and the sharp six-owner
   integral port toll is two.
7. For actual ownerwise mixing of the three global atlases, the exact path
   potential is the monochromatic run boundary \(B(c)\).
8. Neither the finite \(B_4\) Euler obstruction nor the isolated local
   toll may be summed over the first-eligible tensor without a full-context
   theorem.
9. No MWB, SCI, or coefficient-one implication is asserted.

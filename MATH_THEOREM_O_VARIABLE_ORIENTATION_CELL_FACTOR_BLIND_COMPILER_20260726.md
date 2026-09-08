# Variable orientation cells: factor-blind compilation, prefix toll, and the exact cross-cell gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
                         W=\binom{2m}{m}.
\tag{0.1}
\]

Suppose an owner-disjoint part of the middle layer is partitioned into
physical orientation cells \(Q_D\) of variable dimensions \(D\). In a
\(D\)-cell choose

\[
                         n(D)=8\cdot2^t\le D
\tag{0.2}
\]

physical active directions. Fixing the other \(D-n(D)\) orientations
partitions \(Q_D\) into \(Q_{n(D)}\)-faces. On each such face install the
valid recursive context-array factor: its coarse context dimension is
\(n(D)/2=4\cdot2^t\), its physical components are isometric
\(C_{2n(D)}\)'s, and all literal signed traces are injective through
physical depth

\[
                         H\le {n(D)\over4}-1.
\tag{0.3}
\]

If \(M_D\) is the retained owner mass in the \(D\)-cells, then the exact
number of physical cycles is

\[
                         K_D={M_D\over2n(D)}.
\tag{0.4}
\]

Consequently the complete cyclic-linearization toll is

\[
 \boxed{
 \mathsf P_H=2H\sum_DK_D
             =H\sum_D{M_D\over n(D)}.}
\tag{0.5}
\]

There is no extra toll for changing dimensions, inactive directions,
cell boundaries, or concatenation seams.

Choose \(n(D)\) to be the largest number of the form (0.2) not exceeding
\(D\). Then

\[
                         {D\over2}<n(D)\le D.
\tag{0.6}
\]

Thus, if all but owner mass \(B\) have \(D\ge d_*\), where

\[
 d_*\ge8(H+1),\qquad {H\over d_*}\longrightarrow0,
\tag{0.7}
\]

and the exceptional cells are quarantined, then

\[
 \boxed{
 \mathsf P_H\le {2H\over d_*}(W-B)=o(W).}
\tag{0.8}
\]

For the canonical fixed-pair partition, the owner-weighted dimension
random variable is concentrated at \(m/2\). A direct second-moment proof
below gives

\[
 \boxed{
 B:=\sum_{D<m/3}\widehat M_D\le {18\over m}W.}
\tag{0.9}
\]

Hence, for every \(H=o(m)\), all cells with \(D\ge m/3\) admit the
construction for large \(m\), and

\[
 \boxed{
 \mathsf P_H\le {6H\over m}W=o(W).}
\tag{0.10}
\]

The discarded cells create at most \(2HB\le36(H/m)W=o(W)\) raw signed
capacity shortage through depth \(H\).

The remaining issue is not within-cell trace injectivity. That is exact.
Inside a family built from one common ambient pair partition, a fixed
target also forces the source dimension, so different dimensions are
disjoint. Across genuinely different physical frames this extra statement
need not hold: the same target can have different pair-status descriptions.
All such repetitions remain in the global ledger below. If
\(\Omega_q^\pm\) is their duplicate excess and \(G=W-B\), define

\[
 X_q^\pm=\Omega_q^\pm-(G-N_q)_+,\qquad
 N_q=\binom{2m}{m-q}.
\tag{0.11}
\]

Then the exact number of holes is

\[
 \boxed{
 M_q^\pm=(N_q-G)_++X_q^\pm.}
\tag{0.12}
\]

Thus literal pairwise target-disjointness is neither true nor required:
when \(G>N_q\), at least \(G-N_q\) repetitions are forced. The full-layer
multiframe gate is exactly one simultaneous choice of active frame and
context factor in every cell for which

\[
 \boxed{
 \sum_{q=1}^H(X_q^-+X_q^+)=o(W).}
\tag{0.13}
\]

Under (0.13), \(H/\sqrt m\to\infty\), and \(H=o(m)\), the variable-cell
construction and the product-SCD tail give coefficient one. No new
prefix, seam, parity, or tail interface remains.

## 1. Variable orientation cells and the valid context factor

The cellwise and compiler statements in Sections 1--3 allow different
cells to use different coordinate-disjoint physical pair frames. To define
one cell, fix its frame locally as follows.

Let the physical ground coordinates be paired. A \(D\)-dimensional
orientation cell is specified by:

* a set \(I\) of \(D\) split ground-coordinate pairs;
* a set \(F\), disjoint from \(I\), of pairs frozen full; and
* all remaining pairs frozen empty.

The middle-rank condition is

\[
                         2|F|+|I|=m,
\tag{1.0}
\]

equivalently the number of frozen empty pairs equals \(|F|\).

It is

\[
 \mathcal Q(I,F)=
 \left\{
 \bigcup_{i\in F}P_i\ \cup\
 \{z_i:i\in I,\ z_i\in P_i\}
 \right\}
 \cong Q_D.
\tag{1.1}
\]

In the common-frame specialization, different choices of \((I,F)\)
partition the middle layer. In a multiframe partition, owner-disjointness
of the listed cells is assumed, but their local pair frames need not agree.

### 1.1 Normalization of the active dimension

The valid recursive context array has coarse dimension

\[
                         r=4\cdot2^t.
\tag{1.2}
\]

Its paired physical lift acts on \(2r\) physical cube directions and has
components of length \(4r\). In this report the symbol \(n(D)\) counts
physical active directions, so

\[
                         n(D)=2r=8\cdot2^t,
\qquad
                         4r=2n(D).
\tag{1.3}
\]

This convention prevents a factor-two ambiguity in the toll. If one
instead writes \(r(D)\) for the coarse context dimension, then every
formula below is recovered by substituting \(n(D)=2r(D)\).

Choose an active set

\[
                         A(I,F)\subseteq I,\qquad |A(I,F)|=n(D).
\tag{1.4}
\]

Fixing the orientations in \(I\setminus A(I,F)\) partitions
\(\mathcal Q(I,F)\) into exactly

\[
                         2^{D-n(D)}
\tag{1.5}
\]

coordinate-disjoint \(Q_{n(D)}\)-faces. Install the valid paired
context-array factor on every face.

### Lemma 1.1 (exact cell factor and cycle count)

The resulting union partitions all \(2^D\) owners of \(\mathcal Q(I,F)\)
into isometric \(C_{2n(D)}\)'s. Its cycle count is

\[
 \boxed{
 2^{D-n(D)}{2^{n(D)}\over2n(D)}
 ={2^D\over2n(D)}.}
\tag{1.6}
\]

#### Proof

Each active face is owner-disjoint from the others and the faces exhaust
the cell. The valid context-array theorem is an exact factor of
\(Q_{n(D)}\) into \(C_{2n(D)}\)'s. Multiplying its cycle count by (1.5)
gives (1.6). \(\square\)

### Lemma 1.2 (cell-wide literal injectivity)

If (0.3) holds, then for every \(1\le q\le H\), both physical signed
depth-\(q\) maps are injective on the whole cell \(\mathcal Q(I,F)\), not
only inside one active face.

#### Proof

Inside one active face this is the literal half-step theorem for the valid
context array. Every direction outside \(A(I,F)\) is untouched. Therefore
either signed target retains exactly one endpoint of every inactive split
pair and hence recovers its frozen orientation. Targets from two different
active faces cannot be equal. Combining this separation with injectivity
inside each face proves the assertion. \(\square\)

This proof uses the coordinate-disjoint physical swap-pair interface and
one active ground-direction set \(A(I,F)\), fixed across every spectator
fibre of the outer cell. With unlabelled cube bits, only the augmented
trace statement is automatic. If the active frame depends on spectator
orientation, or re-pairs coordinates inside the cell, refine the cell into
fixed-frame packets and retain their between-packet collisions in Section
5.

## 2. The exact variable-cell factor-blind compiler

Let \(\mathscr C\) be any owner-disjoint family of orientation cells.
Write

\[
 M_D=\sum_{\substack{C\in\mathscr C\\\dim C=D}}|C|,
\qquad
 G=\sum_DM_D,
\qquad
 B=W-G.
\tag{2.1}
\]

The omitted middle owners, of total number \(B\), need not form cells.
Assume (0.3) for every retained dimension. Let

\[
 \mathcal I_{C,q}^\pm
\tag{2.2}
\]

be the physical signed depth-\(q\) image of cell \(C\), and define the
actual target-hole counts

\[
 M_q^\pm
 =N_q-\left|\bigcup_{C\in\mathscr C}\mathcal I_{C,q}^\pm\right|,
\qquad
 \Delta_H=\sum_{q=1}^H(M_q^-+M_q^+).
\tag{2.3}
\]

### Theorem 2.1 (variable-cell compiler)

For every \(1\le H\le m-1\) satisfying (0.3),

\[
 \boxed{
 \nu(2m)\le
 W+H\sum_D{M_D\over n(D)}
 +\Delta_H+L_m(m-H-1).}
\tag{2.4}
\]

The complete-word trimmed lift gives

\[
 \boxed{
 \nu(2m+1)\le
 2\left[
 W+H\sum_D{M_D\over n(D)}
 +\Delta_H+L_m(m-H-1)
 \right].}
\tag{2.5}
\]

#### Proof

By Lemma 1.1, the number of retained cycles is

\[
 K=\sum_D{M_D\over2n(D)}.
\tag{2.6}
\]

Every physical cycle has a doubled-permutation direction word on its
\(n(D)\) active directions. In particular, no physical coordinate changes
twice within the protected delay range. Cutting one cycle and applying the
standard cyclic delay-\(H\) factor produces a literal word of length

\[
                         2n(D)+2H.
\tag{2.7}
\]

Thus all retained cycles cost

\[
 G+2HK
 =G+H\sum_D{M_D\over n(D)}.
\tag{2.8}
\]

Append every omitted middle owner once. The base becomes

\[
                         G+B=W;
\tag{2.9}
\]

there is no \(HB\) term outside the actual positive-depth hole ledger.
Append every missing signed central target once, at cost \(\Delta_H\).
Finally append the single product-SCD exterior word. It covers both even
tails at cost \(L_m(m-H-1)\).

Every advertised witness remains inside one cell-cycle word, singleton,
or product gadget. Variable cycle lengths and changes of cell dimension
therefore create no seam cost. This proves (2.4). Applying the trimmed
one-coordinate lift to the complete even word doubles its length exactly
and proves (2.5). \(\square\)

The exact odd excess, with

\[
 W_o=\binom{2m+1}{m}=2W-{W\over m+1},
\tag{2.10}
\]

is

\[
 \nu(2m+1)-W_o
 \le {W\over m+1}
 +2H\sum_D{M_D\over n(D)}
 +2\Delta_H+2L_m(m-H-1).
\tag{2.11}
\]

## 3. Prefix toll as a harmonic-mean functional

The exact toll (0.5) may be written

\[
 {\mathsf P_H\over G}
 =H\,\mathbb E_G\!\left[{1\over n(D)}\right],
\tag{3.1}
\]

where the expectation uses the owner-weighted dimension distribution
\(\Pr_G\{D=d\}=M_d/G\). Thus the exact necessary and sufficient numerical
condition for the prefix toll alone to be \(o(W)\) is

\[
 \boxed{
 H\sum_D{M_D\over n(D)}=o(W).}
\tag{3.2}
\]

### Lemma 3.1 (dyadic active dimension)

For \(D\ge8\), let \(n(D)\) be the largest integer of the form
\(8\cdot2^t\) not exceeding \(D\). Then

\[
                         {D\over2}<n(D)\le D.
\tag{3.3}
\]

If \(D\ge8(H+1)\), then (0.3) holds.

#### Proof

The next admissible dyadic value is \(2n(D)>D\), proving (3.3). Moreover
\(n(D)>D/2\ge4(H+1)\), so

\[
                         {n(D)\over4}-1\ge H.
\]

\(\square\)

### Theorem 3.2 (deterministic concentration-to-toll lemma)

Let \(d_*=d_*(m)\) satisfy (0.7), and retain every cell with
\(D\ge d_*\), using Lemma 3.1. Then

\[
 \boxed{
 \mathsf P_H
 <2H\sum_{D\ge d_*}{M_D\over D}
 \le {2H\over d_*}G.}
\tag{3.4}
\]

In particular, \(\mathsf P_H=o(W)\).

More generally, suppose the owner-weighted dimensions are concentrated in
\([\mu-w,\mu+w]\), outside owner mass \(B\), where

\[
 \mu-w\ge8(H+1),
\qquad
 {H\over\mu-w}\longrightarrow0.
\tag{3.5}
\]

Quarantining the exceptional mass gives

\[
 \boxed{
 \mathsf P_H\le {2H\over\mu-w}(W-B)=o(W).}
\tag{3.6}
\]

#### Proof

Equation (3.3) gives \(1/n(D)<2/D\). Summation proves (3.4), and
(3.6) is its specialization with \(d_*=\mu-w\). \(\square\)

Only the prefix toll is under discussion in Theorem 3.2. If the
exceptional owners are discarded, their middle cost cancels as in (2.9),
but a support-free bound on their lost signed occurrences is

\[
                         2HB.
\tag{3.7}
\]

Thus \(B=o(W)\) suffices for the toll, while the stronger
\(HB=o(W)\) is a simple sufficient condition for their complete raw
positive-depth quarantine. Measuring the actual holes in (2.3) can be
strictly sharper.

## 4. Full fixed-pair layer: a hand concentration theorem

Now take the complete fixed-pair partition (1.1). Let a uniformly random
middle owner be \(S\), and let

\[
 D(S)=\#\{i:|S\cap P_i|=1\}.
\tag{4.1}
\]

Write

\[
 \widehat M_d
 =\#\left\{S\in\binom{[2m]}m:D(S)=d\right\}.
\tag{4.1a}
\]

Thus \(\widehat M_d/W\) is the probability mass of \(D=d\). After the
low-dimensional quarantine we set \(M_d=\widehat M_d\) for retained
dimensions and \(M_d=0\) otherwise.

For each pair \(i\), let \(X_i\) be the indicator that it is split. Then
\(D=\sum_iX_i\). Direct counting gives

\[
 p:=\mathbb EX_i
 ={2\binom{2m-2}{m-1}\over\binom{2m}{m}}
 ={m\over2m-1},
\tag{4.2}
\]

and, for \(i\ne j\),

\[
 \mathbb E(X_iX_j)
 ={4\binom{2m-4}{m-2}\over\binom{2m}{m}}
 ={m(m-1)\over(2m-1)(2m-3)}.
\tag{4.3}
\]

Therefore

\[
 \boxed{
 \mathbb ED={m^2\over2m-1}}
\tag{4.4}
\]

and

\[
 \boxed{
 \operatorname {Var}D
 ={2m^2(m-1)^2\over(2m-1)^2(2m-3)}
 \le {m\over2}.}
\tag{4.5}
\]

### Proposition 4.1 (linear lower concentration)

For every \(m\ge2\),

\[
 \boxed{
 \Pr\{D<m/3\}\le {18\over m}.}
\tag{4.6}
\]

Equivalently, (0.9) holds.

#### Proof

Equation (4.4) gives

\[
                         \mathbb ED-{m\over3}>{m\over6}.
\tag{4.7}
\]

Chebyshev's inequality and (4.5) imply

\[
 \Pr\{D<m/3\}
 \le {\operatorname {Var}D\over(m/6)^2}
 \le {18\over m}.
\]

\(\square\)

### Corollary 4.2 (full-layer prefix and quarantine toll)

Assume

\[
                         {H\over m}\longrightarrow0.
\tag{4.8}
\]

Discard the cells with \(D<m/3\), and in every other cell use the largest
admissible \(n(D)\). For all sufficiently large \(m\), (0.3) holds and

\[
 \boxed{
 \mathsf P_H\le {6H\over m}W,}
\tag{4.9}
\]

\[
 \boxed{
 2HB\le {36H\over m}W.}
\tag{4.10}
\]

Both are \(o(W)\).

#### Proof

For a retained cell, (3.3) and \(D\ge m/3\) give

\[
 {H\over n(D)}<{2H\over D}\le {6H\over m}.
\]

Sum over its owner mass to obtain (4.9). Equation (4.10) follows from
(0.9). Since \(H=o(m)\), both normalized bounds tend to zero. The trace
range follows because \(D\ge m/3\ge8(H+1)\) eventually. \(\square\)

For the canonical endgame choice

\[
                         H=\left\lceil\sqrt{m\log m}\right\rceil,
\tag{4.11}
\]

both (4.9) and (4.10) are

\[
                         O\!\left(\sqrt{{\log m\over m}}\right)W,
\tag{4.12}
\]

while

\[
 {L_m(m-H-1)\over W}
 \le C_0e^{-H^2/(8m)}
 \le C_0m^{-1/8}.
\tag{4.13}
\]

## 5. The exact cross-cell overlap ledger

Fix \(q\le H\) and one sign. By Lemma 1.2,

\[
                         |\mathcal I_{C,q}^\pm|=|C|
\tag{5.1}
\]

for every retained orientation cell. Put

\[
 \Omega_q^\pm
 =\sum_C|\mathcal I_{C,q}^\pm|
  -\left|\bigcup_C\mathcal I_{C,q}^\pm\right|
 =G-\left|\bigcup_C\mathcal I_{C,q}^\pm\right|.
\tag{5.2}
\]

This is the complete duplicate excess. Every unit in it is a collision
between distinct orientation cells; there is no within-cell contribution.
Since the union has size at most \(N_q\),

\[
                         \Omega_q^\pm\ge(G-N_q)_+.
\tag{5.3}
\]

Define the baseline-corrected excess \(X_q^\pm\) by (0.11). Then

\[
\begin{aligned}
 M_q^\pm
 &=N_q-\left|\bigcup_C\mathcal I_{C,q}^\pm\right|\\
 &=N_q-G+\Omega_q^\pm\\
 &=(N_q-G)_++X_q^\pm.
\end{aligned}
\tag{5.4}
\]

This proves (0.12). In particular,

\[
 \Delta_H
 =\sum_{q=1}^H\sum_{\pm}
 \left((N_q-G)_++X_q^\pm\right).
\tag{5.5}
\]

Since \(N_q\le W\) and \(G=W-B\),

\[
 \boxed{
 \sum_{q=1}^H\sum_{\pm}(N_q-G)_+\le2HB.}
\tag{5.6}
\]

Thus after the concentration quarantine, the only uncontrolled term in
\(\Delta_H\) is

\[
                         X_H:=\sum_{q=1}^H(X_q^-+X_q^+).
\tag{5.7}
\]

### 5.1 Optional packetwise decomposition

If the cells are grouped into larger physical packets \(P\), there are two
distinct cross-cell ledgers. For completeness, allow a possibly imperfect
local cell map and put

\[
 \gamma_{C,q}^\pm
 =|C|-|\mathcal I_{C,q}^\pm|.
\tag{5.7a}
\]

Define the collision excess between cells of one packet by

\[
 \omega_{P,q}^\pm
 =\sum_{C\subseteq P}|\mathcal I_{C,q}^\pm|
  -\left|\bigcup_{C\subseteq P}\mathcal I_{C,q}^\pm\right|,
\tag{5.7b}
\]

and the overlap between packet images by

\[
 \Omega_{q}^{\pm,\mathrm{out}}
 =\sum_P\left|\bigcup_{C\subseteq P}\mathcal I_{C,q}^\pm\right|
  -\left|\bigcup_C\mathcal I_{C,q}^\pm\right|.
\tag{5.7c}
\]

Then the exact identity is

\[
 \boxed{
 M_q^\pm
 =N_q-G+\sum_C\gamma_{C,q}^\pm
       +\sum_P\omega_{P,q}^\pm
       +\Omega_q^{\pm,\mathrm{out}}.}
\tag{5.7d}
\]

For the construction of Section 1, \(\gamma_{C,q}^\pm=0\). A packet-wide
face-separation theorem is exactly the assertion
\(\omega_{P,q}^\pm=0\). If completed directions erase the local cell
label, that collision belongs to \(\omega_P\), not to the outer-packet
term. In targetwise form, if

\[
 d_{P,T}^\pm
 =\#\{C\subseteq P:T\in\mathcal I_{C,q}^\pm\},
\]

then

\[
 \omega_{P,q}^\pm
 =\sum_T(d_{P,T}^\pm-1)_+.
\tag{5.7e}
\]

The global condition still does not ask that the sum of these three
collision terms be \(o(W)\). Their mandatory floor is
\((G-N_q)_+\); only excess beyond that floor, equivalently actual target
holes, must be small.

### 5.2 Exact geometric candidate cells in one common frame

Assume throughout this subsection that all cells use one common ambient
pair partition. The fixed-pair geometry then gives more separation than
(5.2) alone suggests.
For any physical target \(T\), define

\[
\begin{aligned}
 F_T&=\{i:P_i\subseteq T\},\\
 S_T&=\{i:|P_i\cap T|=1\},\\
 E_T&=\{i:P_i\cap T=\varnothing\}.
\end{aligned}
\tag{5.8}
\]

### Lemma 5.1 (candidate-cell classification)

Let \(T\) have rank \(m-q\). It is a lower depth-\(q\) target of the
orientation cell \(\mathcal Q(I,F)\) only if, for a unique
\(q\)-set \(J\),

\[
 \boxed{
 F=F_T,\qquad
 I=S_T\mathbin{\dot\cup}J,\qquad
 J\subseteq E_T.}
\tag{5.9}
\]

Conversely, (5.9) is the exact geometric condition that \(T\) be the
lower trace of the affine \(q\)-face obtained by varying \(J\) in that
cell.

Let \(T\) have rank \(m+q\). It is an upper depth-\(q\) target of
\(\mathcal Q(I,F)\) only if

\[
 \boxed{
 I=S_T\mathbin{\dot\cup}J,\qquad
 J\subseteq F_T,\qquad
 F=F_T\setminus J.}
\tag{5.10}
\]

Again this is the exact geometric face condition.

In both cases every candidate source cell has the forced dimension

\[
 \boxed{
                         D=|S_T|+q.}
\tag{5.11}
\]

#### Proof

In a lower trace, every varied split pair becomes empty, every unvaried
split pair retains one endpoint, and frozen full and empty pairs remain
unchanged. This gives (5.9). The upper statement follows by replacing
“varied becomes empty” by “varied becomes full.” In either case the source
split set is \(S_T\dot\cup J\), proving (5.11). The reverse constructions
are immediate coordinate by coordinate. \(\square\)

Before the active-frame and consecutive-factor restrictions are imposed,
the numbers of geometric candidate cells are therefore

\[
 \boxed{
 d_q^-(T)=\binom{|E_T|}{q},\qquad
 d_q^+(T)=\binom{|F_T|}{q}.}
\tag{5.12}
\]

Equation (5.12) counts the complete common-frame status partition. After
the low-\(D\) quarantine, or in any owner-disjoint subatlas, the actual
candidate degree is the number of listed cells which were retained. It
may be smaller, including zero.

For a chosen factor, a geometric candidate in (5.9) or (5.10) actually
supplies \(T\) precisely when

1. \(J\subseteq A(I,F)\), and
2. the corresponding affine face lies in the consecutive trace image of
   the installed context-array factor.

Injectivity makes the supplying start unique whenever it exists.

### Corollary 5.2 (what is already disjoint)

At fixed \(q\) and sign:

1. traces from different active subfaces of one orientation cell are
   disjoint;
2. traces from different source dimensions \(D\) are disjoint; and
3. all remaining repetitions occur among distinct orientation cells of
   the single dimension forced by (5.11).

#### Proof

Item 1 is Lemma 1.2. If two targets are equal, (5.11) gives the same source
dimension, proving item 2. Item 3 is the remaining possibility. \(\square\)

The erased \(q\)-set \(J\) is exactly the part of the source-cell label
which a lower or upper trace can forget. Thus neither dimension
concentration nor the local context theorem makes different cells
target-disjoint.

For a genuine multiframe atlas, Corollary 5.2(2) must not be used across
different ambient matchings. The same physical target can have different
sets \(F_T,S_T,E_T\), and hence different forced values of \(D\), relative
to two frames. Unless a retained physical spectator tag identifies the
frame, every such overlap remains in \(\Omega_q^\pm\). The generic identity
(5.4) and the simultaneous target (5.14) require no common-frame
assumption and already include these cross-frame collisions.

### 5.3 The exact simultaneous multiframe target

Let \(\Theta_C\) be the allowed menu of active frames and valid
context-factor conjugates in cell \(C\). A physical construction chooses
one

\[
                         \theta_C\in\Theta_C
\tag{5.13}
\]

for each cell, once and for all. The same choices must serve every depth,
both signs, and every target. Define the resulting images
\(\mathcal I_{C,q}^\pm(\theta_C)\) and \(X_q^\pm(\theta)\) by
(5.2)--(5.4).

The exact surviving statement is

> **Full-layer multiframe cross-cell theorem.** There is one simultaneous
> choice \(\theta=(\theta_C)_C\) such that
> \[
>       \sum_{q=1}^H
>       \bigl(X_q^-(\theta)+X_q^+(\theta)\bigr)=o(W).
> \tag{5.14}
> \]

This is a baseline-corrected target-resolution theorem, not pairwise
disjointness. Separate choices for different \(q\), signs, or target
fibres do not define one cycle factor. Macro balance of active directions
does not imply (5.14), because the candidate sets (5.9)--(5.10) depend on
the physical target.

## 6. Full-layer endgame implication

Combine Theorem 2.1 with (5.5)--(5.7).

### Theorem 6.1 (finite full-layer multiframe compiler)

For the fixed-pair construction with cells \(D\ge m/3\), for all
sufficiently large \(m\) and every \(H=o(m)\),

\[
 \boxed{
 \nu(2m)\le
 W+{6H\over m}W+{36H\over m}W
 +X_H+L_m(m-H-1).}
\tag{6.1}
\]

Equivalently,

\[
 \boxed{
 \nu(2m)\le
 W+{42H\over m}W
 +X_H+L_m(m-H-1).}
\tag{6.2}
\]

#### Proof

The prefix toll is bounded by (4.9). Equations (5.5)--(5.6) bound the
unavoidable capacity shortage by \(2HB\), and (4.10) bounds this by
\(36(H/m)W\). The remaining hole term is \(X_H\). Substitute these three
bounds in (2.4). \(\square\)

### Corollary 6.2 (conditional coefficient one)

Retain the common-fixed-matching status partition used in Section 4, or
assume separately for a multiframe partition the same owner-weighted
low-dimensional estimate \(B=O(W/m)\).

Choose \(H=H(m)\) so that

\[
 {H\over\sqrt m}\longrightarrow\infty,
\qquad
 {H\over m}\longrightarrow0.
\tag{6.3}
\]

If the simultaneous cross-cell theorem (5.14) holds, then

\[
 \nu(2m)=(1+o(1))W
\tag{6.4}
\]

and

\[
 \nu(2m+1)
 =(1+o(1))\binom{2m+1}{m}.
\tag{6.5}
\]

#### Proof

The first error in (6.2) is \(o(W)\), as is \(X_H\) by hypothesis. The
factor-blind product-tail estimate gives

\[
 {L_m(m-H-1)\over W}
 \le C_0e^{-H^2/(8m)}=o(1).
\tag{6.6}
\]

This proves the even upper bound. The middle-layer endpoint injection is
the matching lower bound. Apply (2.5), or equivalently the complete-word
trimmed lift, and use
\(\binom{2m+1}{m}=2W-W/(m+1)\) to obtain (6.5). \(\square\)

The explicit choice (4.11) is admissible. Under that choice, every proved
noncollision term in (6.2) is

\[
 O\!\left(\sqrt{{\log m\over m}}\right)W
 +O(m^{-1/8})W.
\tag{6.7}
\]

## 7. Audited boundary

The following are proved:

1. variable-dimensional cells may be compiled together with exact toll
   (0.5);
2. the largest valid active dimension satisfies (0.6);
3. owner-weighted dimension concentration implies prefix toll \(o(W)\);
4. in the full fixed-pair partition, the elementary bound (0.9) is enough
   to make both prefix and raw low-dimensional quarantine costs \(o(W)\);
5. the valid context array gives exact cell-wide two-sided literal
   injectivity;
6. within a common ambient matching, at fixed depth and sign, different
   source dimensions cannot collide; in a genuine multiframe atlas no such
   cross-frame separation is asserted; and
7. the exact remaining overlap is (0.13), equivalently (5.14).

What is not proved is the simultaneous multiframe choice (5.14).
Ordinary target-disjointness is impossible whenever \(G>N_q\); only the
baseline-corrected excess can be \(o(W)\). The candidate-cell formulas
(5.9)--(5.12) identify the remaining target-dependent Hall fibres
exactly. A proof must remain integral inside each chosen context factor
and use one common choice across every protected depth and both signs.

Independent audits verified the factor-two normalization in (0.5), the
literal range (0.3), the moments and constants \(18,36,42\), and the
candidate-cell formulas. They also forced the two scope clauses retained
above: the active frame must be fixed across a cell's spectator fibres,
and different source dimensions are automatically separated only inside
one common ambient matching.

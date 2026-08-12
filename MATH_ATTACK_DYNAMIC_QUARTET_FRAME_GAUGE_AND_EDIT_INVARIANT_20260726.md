# Dynamic quartet frames: exact alternating atlas, gauge invariance, and the staggered-edit obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Let \(\mathscr S\) be a symmetric-chain decomposition of \(B_{2m}\).  A
middle owner \(X\) of SCD radius \(\rho(X)\) has deletion and insertion
flags

\[
 \delta _1(X),\ldots,\delta _{\rho(X)}(X)\in X,
 \qquad
 \eta _1(X),\ldots,\eta _{\rho(X)}(X)\notin X,
\]

and opposite corners

\[
 G_q(X)=X-\{\delta _1,\ldots,\delta _q\}
          +\{\eta _1,\ldots,\eta _q\}.                 \tag{0.1}
\]

The desired promotion law is

\[
 G_1(G_tX)=G_{t+1}X.                                  \tag{0.2}
\]

This note gives four exact conclusions about the proposed escape in which
the quartet decomposition is allowed to depend on the owner height/profile.

1. **Frame gauge.**  Once \(P=G_1\) is fixed, (0.2) fixes every flag and
   every opposite corner:

   \[
       G_q(X)=P^qX,qquad
       (\delta_q(X),\eta_q(X))
       =(X_{q-1}\setminus X_q,X_q\setminus X_{q-1}),  \tag{0.3}
   \]

   where \(X_i=P^iX\).  Changing quartet frames without changing \(P\)
   cannot change a single lower or upper target, target multiplicity, Hall
   deficiency, or laminar SCD-selection obstruction.

2. **Exact full-carrier atlas.**  Conversely, every literal isometric
   \(C_{2m}\) row, for even \(m\), admits two alternating global quartet
   frames in which every two consecutive swaps are one relabelled central
   \(B_4\) chart.  These frames satisfy (0.2) through the full geodesic
   half and have trivial order-two frame holonomy.  Thus local
   power-consistency is not itself the obstruction.

3. **Macroscopic frame reassociation.**  If an owner frame serially
   realizes consecutive flag pairs by central quartet blocks, then its
   successor frame must use the staggered blocks.  With

   \[
       N_q=\binom{2m}{m-q},\qquad W=\binom{2m}{m},     \tag{0.4}
   \]

   the total number of changed quartet blocks through protected depth
   \(H\) is at least

   \[
       \boxed{\displaystyle
       \sum_{k=1}^{\lfloor H/2\rfloor}N_{2k+1}.}      \tag{0.5}
   \]

   It is \((1+o(1))\lfloor H/2\rfloor W\), hence
   \((1+o(1))HW/2\) when \(H\to\infty\) and \(H=o(\sqrt m)\), and it
   saturates at

   \[
       \left({\sqrt\pi\over4}+o(1)\right)W\sqrt m    \tag{0.6}
   \]

   when the full SCD radii are used.  In particular, every radius-at-least
   three owner changes frame, and there are

   \[
       N_3=\left(1-{9\over m}+O(m^{-2})\right)W       \tag{0.7}
   \]

   such owners.

4. **Height-only equivariance obstruction.**  No coordinate-natural rule
   can partition more than four indistinguishable child carriers into
   quartets using only their common height/profile.  More generally, an
   equivariant uniform \(b\)-block selector requires every profile fibre
   to have size at most \(b\).  Hence a dense dynamic frame
   must carry label/phase memory not present in the unordered height
   profile.

The alternating atlas shows that the edit count (0.5) is not automatically
a literal word-overhead count: a recursive rule could encode dense frame
changes internally.  Therefore (0.5) rules out sparse or bounded-local
frame surgery, not all moving-frame constructions.  The exact remaining
gate is to construct a new owner permutation \(P\) whose trace occurrence
graphs admit one laminar SCD selection.  Reframing an existing \(P\) does
not address that gate.

## 1. Frame gauge under the power law

Put

\[
 \lambda_j(X)=(\delta_j(X),\eta_j(X)),
 \qquad
 \Lambda_j(X)=\{\delta_j(X),\eta_j(X)\}.             \tag{1.1}
\]

The \(\Lambda_j(X)\)'s are pairwise disjoint: all deletions are distinct
members of the initial \(X\), all insertions are distinct members of
\(X^c\), and a deletion can therefore never equal an insertion.

### Theorem 1.1 (frame-gauge theorem)

Suppose (0.2) holds through depth \(H\), and put \(P=G_1\).  For every
\(X\) of radius at least \(q\le H\),

\[
 G_q(X)=P^qX,                                         \tag{1.2}
\]

and

\[
 \delta_j(X)=P^{j-1}X\setminus P^jX,
 \qquad
 \eta_j(X)=P^jX\setminus P^{j-1}X.                  \tag{1.3}
\]

Consequently every signed SCD target is the literal trace target

\[
 D_q(X)=\bigcap_{i=0}^qP^iX,
 \qquad
 E_q(X)=\bigcup_{i=0}^qP^iX.                         \tag{1.4}
\]

In particular, two quartet atlases realizing the same \(P\) have identical
target occurrence multigraphs at every depth.

#### Proof

Equation (0.2), beginning with \(G_0=\mathrm{id}\), inductively gives
\(G_q=G_1^q=P^q\).  A Johnson edge \(Y\to PY\) uniquely determines its
deleted and inserted coordinates as \(Y\setminus PY\) and
\(PY\setminus Y\).  Applying this at \(Y=P^{j-1}X\) proves (1.3).  Since
the path is geodesic on the certified interval, its persistent and exposed
coordinates give (1.4).  All statements are independent of the auxiliary
quartet frames. \(\square\)

Thus a frame change may be useful in *defining a new* \(P\).  It is not a
post hoc operation that can repair the signed shadows of a fixed \(P\).

## 2. The exact alternating full-carrier atlas

Let a physical isometric row be written

\[
 X_t=\{z_t,z_{t+1},\ldots,z_{t+m-1}\},               \tag{2.1}
\]

with indices modulo \(2m\).  Its transition at time \(t\) deletes \(z_t\)
and inserts \(z_{t+m}\).  Define the antipodal pair-carriers

\[
 \Lambda_t=\{z_t,z_{t+m}\},                          \tag{2.2}
\]

indexed modulo \(m\).  Every \(\Lambda_s\) has exactly one coordinate in
every \(X_t\).

Assume \(m\) is even and define

\[
 \Pi_t=
 \bigl\{\Lambda_{t+2j}\cup\Lambda_{t+2j+1}:
             0\le j<m/2\bigr\}.                     \tag{2.3}
\]

### Theorem 2.1 (alternating-frame realization)

The \(\Pi_t\)'s are quartet partitions of \([2m]\),

\[
                         \Pi_{t+2}=\Pi_t,             \tag{2.4}
\]

and the frame at \(X_t\) serially realizes the complete flag

\[
 \delta_j(X_t)=z_{t+j-1},
 \qquad
 \eta_j(X_t)=z_{t+m+j-1}qquad(1\le j\le m).         \tag{2.5}
\]

Its opposite corners are

\[
                         G_q(X_t)=X_{t+q},            \tag{2.6}
\]

so (0.2) holds exactly for every \(t+q\le m\).

#### Proof

The \(m\) pair-carriers in (2.2) partition the \(2m\) coordinates, and
(2.3) pairs them, proving that \(\Pi_t\) is a quartet partition.  Shifting
\(t\) by two only cyclically reindexes its blocks, proving (2.4).

In the block

\[
 B_{t,j}=\Lambda_s\cup\Lambda_{s+1},
 \qquad s=t+2j,                                      \tag{2.7}
\]

the owner contains \(z_s,z_{s+1}\) and omits
\(z_{s+m},z_{s+m+1}\).  Relabel the radius-two middle shore \(14\) of the
central \(B_4\) seed by

\[
 4\mapsto z_s,\quad 2\mapsto z_{s+m},\quad
 1\mapsto z_{s+1},\quad 3\mapsto z_{s+m+1}.          \tag{2.8}
\]

The seed's two flag swaps \((4\to2),(1\to3)\) are exactly the two row
swaps at times \(s,s+1\).  Serially reading the blocks in (2.3) proves
(2.5).  Performing the first \(q\) swaps deletes
\(z_t,\ldots,z_{t+q-1}\) and inserts
\(z_{t+m},\ldots,z_{t+m+q-1}\), which is \(X_{t+q}\).  This proves
(2.6) and then (0.2). \(\square\)

For \(m\ge4\), \(\Pi_t\) and \(\Pi_{t+1}\) have no common block.  Thus
this exact zero-holonomy atlas changes all \(m/2\) quartet blocks at every
row step.  It is a full-carrier construction, not a bounded seam.

The theorem assigns a coherent maximal flag to each row state separately.
It does **not** assert that these chains form one SCD.  In fact, taking all
of them at full radius repeats \(\varnothing\) and \([2m]\) at every
owner.  By Theorem 1.1, selecting legal radii so that all ranks are used
once is exactly the original laminar trace-contained SCD problem.

## 3. Staggered frames force macroscopic edit

Call a quartet frame \(\Pi_X\) **serial-central through depth \(r\)** if

\[
 \Lambda_{2j-1}(X)\cup\Lambda_{2j}(X)\in\Pi_X
 \qquad(1\le j\le\lfloor r/2\rfloor).               \tag{3.1}
\]

This is precisely the local grammar in which a central \(B_4\) carrier is
consumed for its two consecutive flag swaps before the next carrier is
entered.  For two quartet partitions define

\[
 d_{\rm fr}(\Pi,\Pi')=|\Pi'\setminus\Pi|.            \tag{3.2}
\]

If \(m\) is odd, one may permit one residual two-cell; it does not affect
any argument involving the displayed quartet blocks.

### Theorem 3.1 (staggered-frame edit bound)

Suppose \(X\) has radius \(r\), (0.2) holds on its flag, and both
\(\Pi_X\) and \(\Pi_{G_1X}\) are serial-central through the available
depths.  Then

\[
 \boxed{
 d_{\rm fr}(\Pi_X,\Pi_{G_1X})
       \ge \left\lfloor{r-1\over2}\right\rfloor.}   \tag{3.3}
\]

With certification truncated at depth \(H\), the right side becomes

\[
              \left\lfloor{\min(r-1,H)\over2}\right\rfloor.  \tag{3.4}
\]

#### Proof

Power consistency gives

\[
 \Lambda_j(G_1X)=\Lambda_{j+1}(X).                  \tag{3.5}
\]

Hence the successor frame contains

\[
 C_j=\Lambda_{2j}(X)\cup\Lambda_{2j+1}(X),
 \qquad 1\le j\le\lfloor(r-1)/2\rfloor.             \tag{3.6}
\]

The old frame contains

\[
 B_j=\Lambda_{2j-1}(X)\cup\Lambda_{2j}(X).          \tag{3.7}
\]

The new block \(C_j\) intersects \(B_j\) in the nonempty pair
\(\Lambda_{2j}(X)\), but it is not equal to \(B_j\), because all the
pair-carriers are disjoint.  Since blocks of \(\Pi_X\) are disjoint,
\(C_j\) cannot be any block of \(\Pi_X\).  The \(C_j\)'s are mutually
disjoint, so they contribute the stated number of new blocks.  Truncation
gives (3.4). \(\square\)

### Corollary 3.2 (aggregate frame area)

For an SCD-shift-consistent promotion through depth \(H\),

\[
 \sum_Xd_{\rm fr}(\Pi_X,\Pi_{G_1X})
 \ge
 \sum_{k=1}^{\lfloor H/2\rfloor}N_{2k+1}.           \tag{3.8}
\]

#### Proof

The SCD radius census is

\[
 |\{X:\rho(X)\ge q\}|=N_q.                         \tag{3.9}
\]

Moreover,

\[
 \left\lfloor{\min(\rho(X)-1,H)\over2}\right\rfloor
 =\sum_{k=1}^{\lfloor H/2\rfloor}
       \mathbf1_{\{\rho(X)\ge2k+1\}}.              \tag{3.10}
\]

Sum (3.4) over \(X\) and interchange the sums. \(\square\)

For fixed \(q=o(\sqrt m)\),

\[
 {N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}
 =\exp\left(-{q^2\over m}+O\left({q^3\over m^2}
                                  +{q\over m}\right)\right).  \tag{3.11}
\]

This proves the first asymptotic in (0.5).  Summing the Gaussian limit on
the odd indices gives

\[
 \sum_{k\ge1}N_{2k+1}
 =\left({\sqrt\pi\over4}+o(1)\right)W\sqrt m,        \tag{3.12}
\]

which proves (0.6).  At radius three, (3.3) gives one changed block and

\[
 {N_3\over W}
 ={m(m-1)(m-2)\over(m+1)(m+2)(m+3)}
 =1-{9\over m}+O(m^{-2}),                            \tag{3.13}
\]

proving (0.7).

### Corollary 3.3 (bounded-local schemes cover negligible mass)

Suppose \(H\ge2K+2\), and a serial-central moving-frame rule changes at
most \(K\) quartet blocks on every owner edge in a set \(\mathcal U\).
Then

\[
 |\mathcal U|\le W-N_{2K+3},                         \tag{3.14}
\]

and

\[
 { |\mathcal U|\over W}
 \le { (2K+3)^2\over m}.                             \tag{3.15}
\]

Thus \(K=o(\sqrt m)\) permits only \(o(W)\) owners.

#### Proof

Theorem 3.1 implies that every \(X\in\mathcal U\) has
\(\rho(X)\le2K+2\), proving (3.14).  Put \(q=2K+3\).  From (3.11)'s exact
product form and \(1-\prod(1-a_i)\le\sum a_i\),

\[
 1-{N_q\over W}
 \le\sum_{i=0}^{q-1}{2i+1\over m+i+1}
 \le {q^2\over m},                                  \tag{3.16}
\]

which proves (3.15). \(\square\)

This is the sharp obstruction to a two-scale proposal which changes only
\(O(1)\), or more generally \(o(\sqrt m)\), local quartet cells at a
promotion step.  It does not obstruct the global alternating atlas of
Theorem 2.1, which changes \(m/2\) cells at once.

## 4. A height/profile selector cannot be coordinate-natural

The following elementary stabilizer obstruction applies before the
power-consistency test.

### Proposition 4.1 (profile-fibre indivisibility)

Let \(I\) be a finite child set, let \(h:I\to\mathcal T\) be a height or
local-profile assignment, and suppose \(\Phi(h)\) is a partition of \(I\)
into blocks of one common size \(b\ge2\).  Assume coordinate equivariance:

\[
 \Phi(h\circ\sigma^{-1})=\sigma\Phi(h)
 \qquad(\sigma\in\operatorname{Sym}(I)).             \tag{4.1}
\]

Then every profile fibre \(h^{-1}(a)\) has size at most \(b\).

#### Proof

Let \(C=h^{-1}(a)\), choose \(c\in C\), and let \(B\) be its block.  For
any \(c'\in C\), the transposition \((c\ c')\) fixes \(h\), so it must
preserve the block partition.  If \(c'\notin B\), the image
\((B-\{c\})\cup\{c'\}\) would be another block intersecting \(B\) in
\(B-\{c\}\), which is impossible in a partition.  Hence \(C\subseteq B\)
and \(|C|\le b\). \(\square\)

For quartet blocks, \(b=4\).  In the pair-carrier description of Theorem
2.1 the relevant selector is a perfect matching, so \(b=2\), and every
pair-carrier has the same balanced local height.  Consequently the two
alternating matchings cannot be recovered from the unordered height
profile: their cyclic phase order is indispensable additional memory.

If the local profile alphabet has fixed size \(s\), Proposition 4.1 rules
out an equivariant quartet selector as soon as \(|I|>4s\).  A rule using
fixed child labels to break ties evades the proposition, but is no longer a
height/profile-only construction and remains subject to the staggered-edit
bound.

## 5. Exact implication boundary

The following statements are proved.

* Every isometric physical row has an exact full-carrier, order-two
  alternating quartet atlas, and its local flags obey the promotion power
  law through the entire geodesic half.
* The atlas is necessarily macroscopic in the serial-central grammar:
  almost every SCD owner changes frame, and bounded-local frame updates
  cover only negligible owner mass.
* A coordinate-natural selector cannot manufacture the required frame
  from a dense unordered height/profile with repeated child types.
* Once \(G_1\) is fixed, frames are gauge and cannot change the signed
  target incidence or the laminar SCD-selection problem.

The following are **not** proved.

* The changed quartet blocks in (0.5) are not automatically literal reset
  entries.  An internal rotating-frame implementation may absorb them.
* The alternating atlas does not partition Boolean ranks into one SCD.
  It equips each owner with a coherent private flag, and those private
  chains heavily reuse rank resources.
* No universal obstruction is obtained for a construction which jointly
  designs a new owner permutation, uses dense global phase memory, permits
  cross-quartet/off-centre carriers, and solves the laminar target matching
  at the same time.

Thus the natural two-scale idea has an exact dichotomy.  Sparse local frame
surgery is impossible on positive-density owners.  Dense global reframing
can satisfy power consistency, but by Theorem 1.1 it supplies no target
balance beyond that already present in the owner permutation.  The
remaining mathematical object is therefore not a free-standing frame
resolver; it is a simultaneous construction of the owner rotor and its
laminar trace-contained SCD.

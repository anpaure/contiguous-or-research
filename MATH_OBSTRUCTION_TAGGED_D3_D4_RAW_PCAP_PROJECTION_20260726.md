# The tagged \(D_3/D_4\) repair does not descend to the raw PCap carrier

Date: 2026-07-26

Method: pure mathematics only. No computation, script, solver, search, or
web input is used. The certified \(D_3\) and \(D_4\) path tables are taken
as exact finite inputs.

## 0. Verdict

The tagged direction

\[
                         e_{E_3}-e_{E_2},
 \qquad E_2=\{4,5\},\quad E_3=\{6,7\},                \tag{0.1}
\]

does **not** descend to a legal signed atom in the complete untagged target
ledger used by PCap/MWB. For one selected \(b_1\) occurrence, adjoining
its exterior carrier is of course injective on the local coordinate
\(x\). The obstruction is that this injection does not commute with adding
the other compulsory starts of the exact factor.

There are two exact reasons.

1. In the actual prefix-\(D_4\)/pentagon product, the distinguished
   first-insertion start \(b_1\) and the compulsory opposite boundary
   start \(a_4\) have the same exterior carrier at raw lower depth three:

   \[
                         K_B=P_*\cup B.                \tag{0.2}
   \]

   Their pair profiles are

   \[
          -e_{E_2}+e_{E_3},
          \qquad 2e_{E_2}-2e_{E_3}.                   \tag{0.3}
   \]

   Hence the actual untagged singleton target family over \(K_B\) sees

   \[
                         \boxed{e_{E_2}-e_{E_3},}      \tag{0.4}
   \]

   the **opposite** of the decorated direction. After all nine starts are
   placed on one common matched carrier, the six open starts have signed
   profile

   \[
                 d=2e_2-3e_3-3e_6+4e_7,
   \]

   the three complementary starts have \(-d\), and the complete raw image
   is zero. Thus \(-e_{E_2}+e_{E_3}\) is not a legal standalone
   exact-factor atom.

   The \(D_3\) pentagon has the analogous selected-occurrence warning:
   its intrinsic direction is nonzero, but a selected \(C_8\) arm and its
   completion companions cannot be separated merely by naming the arm.

2. At larger depths, exterior collars can separate some of these starts,
   so universal raw cancellation is false. Nevertheless the literal
   prefix-\(D_4\)/pentagon cross is a bounded edit of four coordinate
   blocks of lengths \(4,3,4,3\). For every lower depth \(q\),

   \[
      {1\over2}\|\mu_q^+-\mu_q^-\|_1
                    \le 208\operatorname {Cat}_{m-7}.               \tag{0.5}
   \]

   Hence, for \(H_A=\lceil A\sqrt m\rceil\),

   \[
   \boxed{
   \sum_{q=1}^{H_A}
     \left(V_q^-+V_q^+\right)
       \le416(H_A+1)\operatorname {Cat}_{m-7}
       =\left({13A\over1024}+o(1)\right){W\over\sqrt m}
       =o(W),}                                                       \tag{0.6}
   \]

   where \(V_q^\pm\) are the lower/upper raw total variations and
   \(W=\binom{2m+1}{m}=(2m+1)\operatorname {Cat}_m\).

Every directed cap-tail or balanced-hinge improvement is bounded by the
same total variation. Thus this positive-density family of Catalan root
rows has only \(o(W)\) total action in a fixed Gaussian depth window. It
cannot repair an \(\Omega(W)\) PCap/MWB deficit.

This is a projection-and-locality obstruction, not a claim that every
higher collar is zero. The \(D_4\) factor has genuine nonzero length-two
and length-three carrier profiles in a separated parent context. What
fails is the inference

\[
 \boxed{\text{nonzero pair tag}\Longrightarrow
        \text{injective raw PCap carrier with Gaussian-scale drain}.} \tag{0.7}
\]

## 1. The actual untagged target ledger

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B_m=\operatorname {Cat}_m={W\over n}.                \tag{1.1}
\]

For a row cyclic order

\[
                         w=(w_0,\ldots,w_{n-1}),       \tag{1.2}
\]

write

\[
 I_w(j,L)=\{w_j,w_{j+1},\ldots,w_{j+L-1}\},            \tag{1.3}
\]

with cyclic indices. The middle owner at start \(j\) is

\[
                         X_j=I_w(j,m).                 \tag{1.4}
\]

For a lower target \(T\in\binom{[n]}{m-q}\), a consecutive
\((q+1)\)-vertex Johnson path

\[
                         X_j,X_{j+1},\ldots,X_{j+q}    \tag{1.5}
\]

lies in the up-set of \(T\) exactly when

\[
             T=X_j\cap\cdots\cap X_{j+q}
               =I_w(j+q,m-q).                         \tag{1.6}
\]

Thus the untagged lower depth-\(q\) target histogram of a factor \(F\) is

\[
 \mu_q^F(T)
 =\#\{(R,j):I_{w_F(R)}(j,m-q)=T\}.                    \tag{1.7}
\]

The harmless shift in (1.6) will be suppressed below. Upper depth \(q\)
is the complement of lower depth \(q-1\), so an upper variation is the
corresponding lower variation after complementation and an index shift.

There are exactly \(B_m\) rows and \(n\) starts per row. Hence

\[
                         \sum_T\mu_q^F(T)=nB_m=W       \tag{1.8}
\]

at every depth.

The raw group in (1.7) has basis \(e_T\) indexed only by the physical set
\(T\). It remembers neither:

* the root owner \(R\);
* the cyclic start \(j\);
* whether the occurrence came from an open or complementary collar; nor
* the local pair label \(E_i\).

Let \(\widehat{\mathcal T}_q\) be the free occurrence group retaining all
four labels, and let

\[
                         A_q:\widehat{\mathcal T}_q
                                  \longrightarrow\mathbb Z^{\binom{[n]}{m-q}}
                                                                  \tag{1.9}
\]

forget them and retain only \(T\). The question in this note is exactly
whether the distinguished pair direction survives \(A_q\) after every
compulsory occurrence is included.

## 2. Complete \(X/Y\) ownership of the cross packet

Use consecutive local blocks \(J_4,J_3\), of sizes eight and six, followed
by a Dyck suffix \(B\in D_{m-7}\). A canonical root is

\[
                         QP B,\qquad Q\in D_4,\quad P\in D_3.       \tag{2.1}
\]

Fix

\[
                         P_*=125,\qquad Q_*=1234.      \tag{2.2}
\]

The cross packet makes two changes:

1. on the fourteen roots \(QP_*B\), replace the canonical \(D_4\)
   path by the certified \(D_4\) pair-transfer path;
2. on the five roots \(Q_*PB\), replace the canonical \(D_3\) path by
   the pentagon path.

The crossing root \(Q_*P_*B\) receives both replacements. Thus eighteen
of the seventy roots in the cylinder change. Over all suffixes, the
changed-row count is

\[
 18\operatorname {Cat}_{m-7}
   =\left({18\over4^7}+o(1)\right)\operatorname {Cat}_m,             \tag{2.2a}
\]

so this is a positive-density packet in the Catalan row space.

### Theorem 2.1 (complete ownership and seam audit)

For every suffix \(B\), the cross packet has exactly the same complete
middle-owner \(X\) ledger and adjacent-union \(Y\) ledger as the canonical
seventy-root cylinder. Every seam and both outer ports agree row by row.
The packets belonging to distinct suffixes are resource-disjoint.

#### Proof

On the fibre \(P=P_*\), adjoining the fixed spectator \(P_*B\) transports
the complete \(D_4\) \(X/Y\) identities injectively. The terminal state of
the first slab is

\[
                         \overline Q\,P_*B             \tag{2.3}
\]

on both sides.

On the fibre \(Q=Q_*\), adjoining \(\overline {Q_*}\) on the left and
\(B\) on the right transports the complete \(D_3\) \(X/Y\) identities
injectively. Its initial and terminal states are

\[
                         \overline {Q_*}PB,\qquad
                         \overline {Q_*}\,\overline P B.            \tag{2.4}
\]

The initial state of the second slab is omitted when paths are
concatenated, but it is the same rooted state on both factors; deleting
this identical column preserves the \(X\)-ledger equality. Every
adjacent-union colour internal to either slab is included exactly once.
There is no additional seam colour: the first Johnson edge of the second
slab is already one of its displayed \(Y\)-resources.

At the crossing root, (2.3) and (2.4) are the same literal state, so the
two replacements commute. Their aggregate resource sets remain the two
canonical slab resource sets, which are disjoint except for the identified
seam. The final port is

\[
                         \overline Q\,\overline P\,\overline B,
                                                                  \tag{2.5}
\]

unchanged row by row.

Distinct \(B\)'s index disjoint canonical root cylinders. Each replacement
preserves its cylinder's complete resource set, so disjointness persists.
\(\square\)

This closes ownership only. It does not permit one selected boundary child
to be counted while its other cyclic starts are discarded.

## 3. Exact raw depth-three collision in the product packet

For a \(D_4\) row write its local coordinate word as

\[
 q_H(Q)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,\infty),
 \qquad H\in\{F,G\}.                                  \tag{3.1}
\]

The global cyclic word has the form

\[
 (a^{(4)}_1,a^{(4)}_2,a^{(4)}_3,a^{(4)}_4,
       R_B,
  b^{(4)}_1,b^{(4)}_2,b^{(4)}_3,b^{(4)}_4,\ldots),     \tag{3.2}
\]

where the exterior deletion word \(R_B\) has length \(m-4\) and symbol set

\[
                         K_B=P_*\cup B.                \tag{3.3}
\]

At lower depth three, raw targets are cyclic intervals of length \(m-3\).
Exactly two intervals in (3.2) have exterior part \(K_B\) and a singleton
intersection with \(J_4\):

\[
                         \{a_4\}\cup K_B,\qquad
                         K_B\cup\{b_1\}.               \tag{3.4}
\]

The first is the right boundary of the deletion block; the second is the
left boundary of the insertion block. The pentagon may reorder \(R_B\) on
the crossing row, but (3.4) contains the whole block, so its set \(K_B\)
is unchanged.

The distinguished \(b_1\) raw profile is

\[
\begin{aligned}
 q_G^+-q_F^+
   &=-4e_2+4e_3-e_4-e_6+2e_7,\\
 \Pi(q_G^+-q_F^+)
   &=-e_{E_2}+e_{E_3}.                                \tag{3.5}
\end{aligned}
\]

The compulsory \(a_4\) profile is

\[
\begin{aligned}
 q_G^--q_F^-
   &=2e_2-2e_3+2e_5+3e_6-5e_7,\\
 \Pi(q_G^--q_F^-)
   &=2e_{E_2}-2e_{E_3}.                               \tag{3.6}
\end{aligned}
\]

### Theorem 3.1 (the marked raw carrier is reversed)

Project the complete raw lower depth-three signed histogram to targets
\(T\) satisfying

\[
                         T\setminus J_4=K_B,\qquad
                         |T\cap J_4|=1.                \tag{3.7}
\]

For one suffix \(B\), this projection is

\[
\boxed{
 K_B\star\left(
 -2e_2+2e_3-e_4+2e_5+2e_6-3e_7
 \right),}                                             \tag{3.8}
\]

has positive and negative mass six, and has pair projection

\[
                         \boxed{e_{E_2}-e_{E_3}.}      \tag{3.9}
\]

The supports belonging to distinct suffixes \(B\) are disjoint.

#### Proof

The two intervals (3.4) are the only intervals with the property (3.7):
an interval entering either four-coordinate \(D_4\) block any farther
contains at least two local coordinates, while an interval stopping before
the block contains none. Thus the projected raw profile is the common
carrier push-forward of the sum of (3.5) and (3.6). Adding their coordinate
vectors gives (3.8), and adding their pair vectors gives (3.9).

On a \(D_3\)-only row \(Q_*PB\), the corresponding complete exterior set
is \(P\cup B\). It equals \(K_B=P_*\cup B\) only for \(P=P_*\), which is
the already counted crossing row. Hence no other pentagon row enters this
projection. Rows outside the packet are identical on the two factors and
contribute zero signed mass.

The coefficient sums in (3.8) give positive mass
\(2+2+2=6\) and negative mass \(2+1+3=6\).
Finally \(K_B\cap J_3=P_*\) and \(K_B\) retains the literal suffix-root
set \(B\). Therefore \(K_B=K_{B'}\) implies \(B=B'\), proving
support-disjointness. \(\square\)

Thus the selected \(b_1\) vector does have a nonzero raw occurrence in
the product, but its compulsory seam mate reverses its pair direction on
the very same physical target family. This is an exact failure of the
decorated-to-raw identification, not merely an unknown cap sign.

Summing over all suffixes and using support-disjointness gives the literal
nonzero raw certificate

\[
 \sum_{B\in D_{m-7}}K_B\star
 \left(-2e_2+2e_3-e_4+2e_5+2e_6-3e_7\right),          \tag{3.9a}
\]

and therefore

\[
                         V_3^-\ge
                         6\operatorname {Cat}_{m-7}.   \tag{3.9b}
\]

Thus the packet has a nonzero raw carrier, but its certified raw mass is
only \(\Theta(W/m)\) and its pair orientation is the reverse of the
proposed repair.

## 3A. Complete matched-child cancellation

For completeness, the six starts in the open local parent sector are

\[
                         a_2,a_3,a_4,b_1,b_2,b_3,      \tag{3.10}
\]

and the three complementary starts are

\[
                         a_1,b_4,\infty.               \tag{3.11}
\]

Let \(u_H,v_H\) be their aggregate singleton histograms over all fourteen
ports. The exact path tables give

\[
 \begin{aligned}
 u_F&=(9,9,12,12,12,12,9,9),\\
 u_G&=(9,11,9,12,12,9,13,9),                           \tag{3.12}\\
 v_F&=(5,5,2,2,2,2,5,5,14),\\
 v_G&=(5,3,5,2,2,5,1,5,14).
\end{aligned}
\]

Consequently

\[
                         u_G-u_F=d,\qquad v_G-v_F=-d,  \tag{3.13}
\]

where

\[
                         d:=2e_2-3e_3-3e_6+4e_7.
\]

### Proposition 3.2 (common-carrier kernel)

Let \(K\) be the common exterior intersection of a literal matched
\(D_4\) child. After all six open starts, all three complementary starts,
and both seams are included, its complete physical target change is

\[
                         \boxed{K\star d-K\star d=0,}  \tag{3.14}
\]

where \(K\star e_x=e_{K\cup\{x\}}\).

The distinguished first-insertion pair vector

\[
                         -e_{E_2}+e_{E_3}              \tag{3.15}
\]

therefore belongs to the kernel of the passage from the selected decorated
start to the legal complete raw packet in this common-carrier
specialization.

#### Proof

Every singleton start in (3.10)--(3.11) lies in the same matched local
child, so adjoining its spectator context gives the same exterior set
\(K\). Since \(K\cap J_4=\varnothing\), adjoining \(K\) is injective on
local singleton targets. Equation (3.13) then pushes forward to (3.14).

The start \(b_1\) alone has pair change (3.15), but exact-factor legality
requires the other eight starts. Their signed push-forwards complete
(3.14). Thus selecting \(b_1\) is a projection in the occurrence group,
not a subpacket of the raw factor. \(\square\)

This common-carrier proposition and Theorem 3.1 are compatible. The actual
product geometry identifies \(a_4\) with \(b_1\) on the carrier \(K_B\)
but sends the other starts to other collar carriers. A fully matched
common-carrier placement identifies all nine and cancels them.

### Lemma 3.3 (the two intrinsic carriers split immediately above depth three)

Let \(R_B\) be the distinct-symbol exterior word in (3.2), of length
\(m-4\). At lower depth \(q\ge4\), put

\[
                         k_q=m-q-1.                   \tag{3.16}
\]

The \(a_4\) boundary target uses the prefix
\(K^+_{B,q}\) of \(R_B\) of length \(k_q\), while the \(b_1\) boundary
target uses its suffix \(K^-_{B,q}\) of the same length. For
\(4\le q\le m-2\),

\[
                         K^+_{B,q}\ne K^-_{B,q}.       \tag{3.17}
\]

For \(6\le q\le m-4\), both carrier sets are independent of the old/new
order of the intervening \(D_3\) block.

#### Proof

A depth-\(q\) target interval has length \(m-q=k_q+1\). The interval
leaving the deletion block through \(a_4\) takes \(a_4\) followed by the
first \(k_q\) symbols of \(R_B\); the interval entering the insertion
block through \(b_1\) takes the last \(k_q\) symbols of \(R_B\) followed
by \(b_1\).

For \(q\ge4\), one has \(k_q<m-4=|R_B|\); for \(q\le m-2\), one has
\(k_q\ge1\). A nonempty proper prefix of a distinct-symbol word cannot
equal the equal-length suffix: the former contains the first symbol and
not the last, while the latter contains the last and not the first. This
proves (3.17).

The \(D_3\) deletion block is the first three symbols of \(R_B\). If
\(q\ge6\), then the suffix omits all three of them. If \(q\le m-4\), the
prefix has length at least three and contains all three as a set.
Reordering that block therefore changes neither carrier set. \(\square\)

Thus the exact reversal (3.9) is a depth-three seam phenomenon. At
Gaussian depths \(q\ge6\), the two intrinsic carriers are locally
separated. This does not restore a quotient map: the remaining collar
starts and possible collisions between different suffix contexts are still
occurrence-resolved, and their complete action is governed by (5.2).

## 4. The analogous \(D_3\) warning

For each rooted \(D_3\) path, adjoining \(\infty\) gives a seven-symbol
cyclic coordinate word. Across the five rows, the complete seven-start
singleton point margin is

\[
                         5\sum_{x\in J_3\cup\{\infty\}}e_x          \tag{4.1}
\]

for every exact \(C_7\)-factor: every row word is a permutation of the
seven coordinates.

The pentagon's selected intrinsic child has the genuine signed direction

\[
                         \delta_{\rm pent}
                            =2e_3+e_5-e_4-2e_2.        \tag{4.2}
\]

The clean \(C_8\) arm \(3\to6\) is one still finer selected occurrence
inside its alternating-cycle ledger. Neither (4.2) nor that one arm is a
complete seven-start raw packet.

### Proposition 4.1 (matched-child compensation)

In a literal matched \(D_3\) child with one common exterior \(O\), the
sum of the selected pentagon singleton profile and all its companion
singleton starts is zero.

#### Proof

The complete old and new singleton point margins are both the common
push-forward of (4.1). Their difference is zero. Isolating the selected
intrinsic start leaves its negative on the other six starts. Adjoining the
same \(O\) preserves this identity. \(\square\)

Thus the formal equality

\[
 (\text{pentagon residual})+(E_2\to E_3)=0             \tag{4.3}
\]

in an owner/phase quotient does not imply equality of the two complete raw
target ledgers. Each selected direction has its own compulsory companion
tensor.

## 5. Why the pair quotient cannot determine a higher collar

In a general aligned parent context, an indexed local occurrence
\(\omega=(Q,j)\) has an exterior carrier \(O_{\omega,q}\). Its physical
singleton target is

\[
                         \Phi_q(\omega,x)
                              =O_{\omega,q}\cup\{x\}.   \tag{5.1}
\]

The complete signed depth-\(q\) profile is occurrence-resolved:

\[
 \Delta_q^{\rm raw}
 =\sum_{\omega}
   \left(e_{\Phi_q(\omega,t_G(\omega))}
            -e_{\Phi_q(\omega,t_F(\omega))}\right).   \tag{5.2}
\]

The pair quotient first sums occurrences having labels in the same
\(E_i\), then forgets \(\omega\). These operations commute with (5.2) only
if the physical carrier is common and injective on precisely the
occurrences being aggregated.

### Theorem 5.1 (nonfactorization of the raw carrier map)

There is no context-independent linear map

\[
 \overline\Phi_q:
       \mathbb Z\langle E_0,E_1,E_2,E_3\rangle
        \longrightarrow\mathbb Z^{\binom{[n]}{m-q}}                 \tag{5.3}
\]

whose value on the local pair vector always equals the complete raw
profile (5.2).

#### Proof

Use two legal carrier placements of the same certified \(D_4\) factor.

* In the matched placement of Proposition 3.2, all nine singleton starts have
  one common exterior. The complete raw profile is zero.
* In a separated placement, give the six open starts one fixed exterior
  carrier and the three complementary starts another, with disjoint
  physical images. The complete raw profile is the disjoint sum of \(d\)
  and \(-d\), has positive mass twelve, and is nonzero.

The local factor and its distinguished pair vector (3.15) are identical in
the two placements, but the complete raw images differ. Hence no map
depending only on the pair vector can produce both. \(\square\)

The actual untagged target \(T\) can sometimes recover a local coordinate
from \(T\cap J_4\). It does not thereby recover the owner, start, sector,
or exterior carrier. Those forgotten data are exactly what distinguish
the two cases in Theorem 5.1.

At local interval lengths two and three the complete uniform-carrier
\(D_4\) profiles are indeed nonzero, with positive masses nineteen and
twenty-two. At lengths one, four, five, and eight they vanish. This confirms
both sides of the obstruction:

* higher collars can expose real raw movement;
* the pair tag alone neither identifies that movement nor gives its sign.

## 6. A cyclic interval-cut lemma

The remaining question is whether the literal product cross could still
have enough higher-collar action after its selected tag fails. A sharp
bounded-locality estimate answers this negatively.

### Lemma 6.1 (block-permutation interval bound)

Let \(w,w'\) be cyclic words on the same \(n\) distinct symbols. Suppose
they agree outside disjoint contiguous position blocks
\(C_1,\ldots,C_s\), and inside each \(C_i\) they contain the same symbol
set, possibly in different orders. Put \(c_i=|C_i|\).

For every proper interval length \(1\le L\le n-1\), the number of starts
\(j\) for which

\[
                         I_w(j,L)\ne I_{w'}(j,L)       \tag{6.1}
\]

is at most

\[
                         2\sum_{i=1}^s(c_i-1).         \tag{6.2}
\]

#### Proof

If an interval contains none or all of \(C_i\), its contribution from that
block is the same set in \(w,w'\).

Suppose first that \(L\ge c_i\). A changed interval can meet \(C_i\) only
in a proper prefix or proper suffix. For each
\(1\le h<c_i\), at most one start takes the prefix of length \(h\) through
the right boundary and at most one takes the suffix of length \(h\)
through the left boundary. This gives \(2(c_i-1)\).

If \(L<c_i\), the interval may lie partly or wholly inside \(C_i\).
Exactly \(L+c_i-1\) cyclic starts have a nonempty intersection with the
block before any possible wrap overlap is identified. Since
\(L\le c_i-1\),

\[
                         L+c_i-1\le2(c_i-1).
\]

Thus the same bound holds in both cases. Taking the union bound over the
blocks proves (6.2). \(\square\)

No assumption about the interval length or the spacing between the blocks
enters the bound.

## 7. Exact Gaussian-window locality ceiling

For a root \(QPB\), the global cyclic coordinate word has block form

\[
\begin{aligned}
w_H(Q,P,B)=(&a_H^{(4)}(Q),a_H^{(3)}(P),a^B(B),\\
            &b_H^{(4)}(Q),b_H^{(3)}(P),b^B(B),\infty).
                                                               \tag{7.1}
\end{aligned}
\]

Fixed ports imply that old and new words have the same symbol set in every
displayed block. A \(D_4\)-only row permutes two blocks of length four, so
Lemma 6.1 gives at most

\[
                         2(4-1)+2(4-1)=12             \tag{7.2}
\]

changed target starts at any fixed depth. A \(D_3\)-only row permutes two
blocks of length three and gives at most

\[
                         2(3-1)+2(3-1)=8.              \tag{7.3}
\]

The crossing row changes both and gives at most twenty. Per suffix \(B\)
there are thirteen \(D_4\)-only rows, four \(D_3\)-only rows, and one
crossing row. Therefore

\[
                         13\cdot12+4\cdot8+20=208.     \tag{7.4}
\]

### Theorem 7.1 (raw total-variation ceiling)

Let \(F^-,F^+\) be the global canonical and cross-packet factors obtained
by installing the construction for every \(B\in D_{m-7}\). For every
lower depth \(q\),

\[
 V_q^-:={1\over2}\|\mu_q^{F^+}-\mu_q^{F^-}\|_1
                    \le208\operatorname {Cat}_{m-7}.                \tag{7.5}
\]

For \(H\ge1\),

\[
                         \sum_{q=1}^HV_q^-
                    \le208H\operatorname {Cat}_{m-7}.                \tag{7.6}
\]

The complementary upper depths satisfy

\[
                         \sum_{q=1}^HV_q^+
                    \le208(H+1)\operatorname {Cat}_{m-7}.           \tag{7.7}
\]

#### Proof

Fix \(q\), so every raw target is an interval of one fixed proper length
\(m-q\). For one changed row, Lemma 6.1 bounds the number of old/new
interval pairs whose target sets differ. Each such pair contributes
\(e_{T'}-e_T\), whose positive and negative masses are one. Aggregating
equal physical targets can only reduce total variation. Equation (7.4)
therefore gives at most 208 per suffix, proving (7.5).

Summing (7.5) proves (7.6). Upper depth \(q\) is the complement of lower
depth \(q-1\). Complementation preserves total variation; adding the
possible endpoint index gives the harmless \(H+1\) bound in (7.7).
\(\square\)

### Corollary 7.2 (directed drain is \(o(W)\))

Let \(c_q\ge1\) be arbitrary PCap/MWB weights, and let
\(\beta_q(T)\) be arbitrary target quotas or fixed backgrounds. Then the
maximum possible decrease of the weighted lower/upper hinge functional

\[
 \sum_{q\le H}{1\over c_q}
       \sum_T(\mu_q(T)-\beta_q(T))_+                  \tag{7.8}
\]

under the cross-packet switch is at most

\[
                         416(H+1)\operatorname {Cat}_{m-7}.         \tag{7.9}
\]

For \(H=H_A=\lceil A\sqrt m\rceil\),

\[
 416(H_A+1)\operatorname {Cat}_{m-7}
 =\left({13A\over1024}+o(1)\right){W\over\sqrt m}
 =o(W).                                                \tag{7.10}
\]

#### Proof

For one depth, put
\(\delta_T=\mu_q^{F^+}(T)-\mu_q^{F^-}(T)\). Its total sum is zero.
Coordinatewise, a hinge difference has the form \(s_T\delta_T\) for some
\(0\le s_T\le1\). Hence its absolute value after summation is at most

\[
             \sum_{\delta_T>0}\delta_T
                ={1\over2}\sum_T|\delta_T|=V_q.        \tag{7.11}
\]

Since \(1/c_q\le1\), Theorem 7.1 gives (7.9).

Finally,

\[
 {\operatorname {Cat}_{m-7}\over\operatorname {Cat}_m}
                   =4^{-7}(1+O(m^{-1})),\qquad
 W=(2m+1)\operatorname {Cat}_m.                       \tag{7.12}
\]

Substitution into (7.9) gives

\[
 {416A\sqrt m\over(2m+1)4^7}W
       =\left({13A\over1024}+o(1)\right){W\over\sqrt m}.
\]

\(\square\)

Thus even an adversarially perfect orientation of every surviving higher
collar cannot give more than \(o(W)\) Gaussian-window drain.

## 8. Consequences

The current tagged repair closes finite ownership but not coefficient one.

1. Every middle owner, adjacent-union colour, slab seam, and outer port is
   exact by Theorem 2.1.
2. In the actual product, Theorem 3.1 includes the compulsory \(a_4\)
   seam mate and proves that it reverses the marked pair direction on the
   same raw target family.
3. The analogous selected \(D_3\) arm also has compulsory matched-child
   compensation.
4. In a fully common-carrier matched child, Proposition 3.2 gives exact
   nine-start cancellation.
5. At higher depths the raw image is occurrence-resolved and cannot be
   reconstructed from \(e_{E_3}-e_{E_2}\).
6. Whatever raw higher-collar movement survives has total Gaussian-window
   action \(o(W)\) by Corollary 7.2.

Therefore the decorated \(D_3\)-pentagon plus \(D_4\) carrier repair is not
a literal PCap/MWB absorber as presently signed, and it does not by itself
prove constant one. The \(o(W)\) locality bound does not exclude using
such bounded packets against a separately proved \(o(W)\) residual; it
excludes crediting them with an \(\Omega(W)\) Gaussian-window correction.

This does not obstruct a new parent-aligned construction with
\(\Omega(W/H_A)\) independently serviceable carrier atoms per depth, nor a
critical-scale growing packet. Such a construction must keep the full
occurrence tensor (5.2), make its carrier sectors physically recoverable
from the untagged target, and prove the actual balanced-hinge sign. A
pair-stratum label by itself cannot serve as that theorem.

## 9. Correction to the preceding tagged note

The earlier tagged note correctly proved:

* the seventy-root cross packet is a literal \(X/Y\)-exact factor trade;
* the selected \(b_1\) boundary child has nonzero start-resolved profile;
* its pair quotient is \(E_2\to E_3\).

It overstated the PCap consequence in two ways.

1. A selected boundary child is not the complete untagged depth ledger.
   In the actual product, Theorem 3.1 adds the compulsory \(a_4\) seam
   mate and reverses the marked pair direction. In the fully matched
   common-carrier specialization, Proposition 3.2 adds all companion
   starts and obtains exact cancellation.
2. Comparing the rank of a pentagon \(Y\)-resource with the rank of a
   lower intersection target mixes the ownership and PCap ledgers. The
   authoritative obstruction is the occurrence projection (3.8), the
   nonfactorization theorem in Section 5, and the
   Gaussian locality ceiling (7.10), not that cross-ledger rank comparison.

Accordingly the correct final verdict is the negative one in Section 0.

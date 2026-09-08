# A literal closed moving-exterior common-core carrier packet

Date: 2026-07-26

Method: pure hand mathematics. No computation, search, solver, or web input is
used.

## 0. Exact outcome

There is a literal, integral, closed common-core carrier trade on three
rank-\(10\) middle-level strands.

* The old and new packets use exactly the same \(33\) lower \(X\)-states and
  the same \(30\) upper \(Y\)-colours, once each.
* Every old and new strand has ten Johnson transitions and joins a \(10\)-set
  to its literal complement in a \(20\)-set.  Hence every strand is a minimum
  Johnson geodesic, equivalently a literal minimum wreath strand.
* The packet contains two common-core \(C_6\) switches.  Their relative
  monodromies are inverse, so the total endpoint monodromy is the identity.
* Each switch uses owner-dependent exterior motion with

  \[
       e_i=|P_i\setminus \tau(P_i)|=1.
  \]

* For the linear protected lower-state intersection ledger, the aggregate
  depth-one change is zero and the depth-two change is a nonzero sum of
  twelve distinct signed atoms.
* For the complete literal \(21\)-letter cyclic OR word, the corresponding
  changes have respectively six and thirty distinct signed atoms.  Thus the
  reverse half, infinity collar, connectors, and cap add payload rather than
  canceling the physical carrier.

Thus the abstract common-core carrier has a physical closed realization; it
is not merely an incidence cycle.  What is **not** proved is that the old
three-path packet extends to a spanning \(D_{10}\)-port factor, or that
positive-density contextual copies exist.  Consequently no constant-one
conclusion is claimed.

Before giving the construction, Section 1 records the exact invariant that
explains why one isolated identity-to-twist router cannot work even after a
common exterior is moved.

## 1. The assignment-cost invariant

For two equal-sized sets, write

\[
                 d_J(A,B)=|A\setminus B|.
\]

### Theorem 1.1 (exact boundary assignment cost)

Let \(A_1,\ldots,A_h\) and \(B_1,\ldots,B_h\) be lower middle-level
states.  Suppose an old packet consists of Johnson geodesics

\[
                 \Gamma_i:A_i\longrightarrow B_{\mu(i)}
\]

for a permutation \(\mu\).  Suppose a proposed replacement is a family of
valid inclusion walks from \(A_i\) to \(B_{\nu(i)}\), and that the two
packets have the same total upper-colour \(Y\)-ledger, with multiplicity.
Then

\[
 \boxed{
 \sum_i\bigl(|\Gamma_i'|-d_J(A_i,B_{\nu(i)})\bigr)
 =
 \sum_i d_J(A_i,B_{\mu(i)})
 -
 \sum_i d_J(A_i,B_{\nu(i)}).}
 \tag{1.1}
\]

In particular, all new rows are geodesics if and only if the old and new
boundary matchings have equal total Johnson cost.

#### Proof

The number of Johnson transitions in a lower--upper--lower path is the
number of upper-colour occurrences.  Equality of the complete \(Y\)-ledgers
therefore gives

\[
                         \sum_i|\Gamma_i'|
                         =\sum_i|\Gamma_i|.
\]

The old paths are geodesics, so the right side is

\[
                         \sum_i d_J(A_i,B_{\mu(i)}).
\]

Subtract the total new endpoint distance.  Every summand on the left of
(1.1) is nonnegative by the triangle inequality, so their sum is zero
exactly when every new row is geodesic. \(\square\)

This proof uses neither one cut nor aligned cut depths.  Arbitrarily many
internal switches and collars are allowed, provided their \(Y\)-colours are
actually entered in the ledger.

### Corollary 1.2 (common moving exterior cancels)

Let \(|J|=2r\), let \(P_i\in\binom Jr\), and put

\[
 A_i=O_L\cup P_i,
 \qquad
 B_j=O_R\cup(J\setminus P_j),
 \qquad
 e=|O_L\setminus O_R|,
 \tag{1.2}
\]

where \(O_L,O_R\) are disjoint from \(J\) and have the same size.  Then

\[
 \boxed{
 d_J(A_i,B_j)
 =e+|P_i\cap P_j|
 =e+r-|P_i\setminus P_j|.}
 \tag{1.3}
\]

Consequently, from the identity boundary matching to a permutation \(\nu\),
the exact total geodesic defect is

\[
 \boxed{
 \sum_i\bigl(|\Gamma_i'|-d_J(A_i,B_{\nu(i)})\bigr)
 =\sum_i|P_i\setminus P_{\nu(i)}|.}
 \tag{1.4}
\]

Thus no nonidentity permutation of distinct ports is an exact same-boundary
replacement, for any value of the common exterior motion \(e\).

#### Proof

The disjoint decomposition

\[
 A_i\setminus B_j
 =(O_L\setminus O_R)\mathbin{\dot\cup}(P_i\cap P_j)
\]

proves (1.3).  Insert it into Theorem 1.1 with \(\mu=1\). \(\square\)

For an \(r\)-transition *open* twisted slab, (1.3) is equivalent to the
familiar equation

\[
                         e=|P_i\setminus P_j|.
 \tag{1.5}
\]

The accounting error in the forbidden identity-to-twist argument is that
the old identity slab with the same moving exterior has length \(r+e\), not
\(r\).  Hence exterior motion cannot pay for a twist while leaving the old
boundary assignment fixed.

If the exterior is owner-dependent, put

\[
 e_{ij}=|O_i^L\setminus O_j^R|.
\]

Then an identity baseline and a new matching \(\nu\) can have equal total
cost only if

\[
 \boxed{
 \sum_i(e_{i,\nu(i)}-e_{ii})
 =\sum_i|P_i\setminus P_{\nu(i)}|.}
 \tag{1.6}
\]

The construction below supplies this exterior correlation locally, and
then cancels its endpoint monodromy before the outer boundary.

## 2. Coordinates and the two stage cores

All indices are in \(\mathbb Z/3\mathbb Z\).  Let the \(20\)-element ground
set be the disjoint union

\[
 \Omega=
 \{h\}
 \mathbin{\dot\cup}D_0\mathbin{\dot\cup}D_1
 \mathbin{\dot\cup}A_0\mathbin{\dot\cup}A_1
 \mathbin{\dot\cup}A_2
 \mathbin{\dot\cup}\{b_0,b_1\},
 \tag{2.1}
\]

where

\[
 D_s=\{k_s,t_{s,0},t_{s,1},t_{s,2}\},
 \qquad
 A_s=\{a_{s,0},a_{s,1},a_{s,2}\}.
 \tag{2.2}
\]

Thus

\[
                         |\Omega|=1+8+9+2=20.
\]

Define \(9\)-element common cores

\[
\begin{aligned}
 K_0&=\{h\}\cup D_0\cup D_1,\\
 K_1&=(K_0\setminus D_0)\cup A_0\cup\{b_0\},\\
 K_2&=(K_1\setminus D_1)\cup A_1\cup\{b_1\}.
\end{aligned}
\tag{2.3}
\]

Equivalently,

\[
 K_1=\{h\}\cup D_1\cup A_0\cup\{b_0\},
 \qquad
 K_2=\{h\}\cup A_0\cup A_1\cup\{b_0,b_1\}.
 \tag{2.4}
\]

The two common-core routers have opposite orientations:

\[
                         \varepsilon_0=+1,
 \qquad
                         \varepsilon_1=-1.
 \tag{2.5}
\]

## 3. One oriented four-transition stage

Fix \(s\in\{0,1\}\), abbreviate

\[
 K=K_s,\quad k=k_s,\quad t_i=t_{s,i},\quad
 a_i=a_{s,i},\quad c_i=a_{s+1,i},\quad
 b=b_s,\quad \varepsilon=\varepsilon_s,
\]

and put \(T=\{t_0,t_1,t_2\}\).  Define the following lower \(10\)-sets:

\[
\begin{aligned}
 E_i&=K\cup\{a_i\},\\
 Z_i&=(K\setminus\{k\})\cup\{a_i,a_{i+\varepsilon}\},\\
 W_i&=(K\setminus\{k,t_i\})
       \cup\{a_i,a_{i+\varepsilon},b\},\\
 R_i&=(K\setminus D_s)
       \cup\{t_{i-\varepsilon}\}\cup A_s\cup\{b\},\\
 E_i'&=(K\setminus D_s)\cup A_s\cup\{b,c_i\}
       =K_{s+1}\cup\{c_i\}.
\end{aligned}
\tag{3.1}
\]

Define upper \(11\)-sets

\[
\begin{aligned}
 Y_i&=K\cup\{a_i,a_{i+\varepsilon}\},\\
 V_i&=(K\setminus\{k\})
       \cup\{a_i,a_{i+\varepsilon},b\},\\
 Q_i&=(K\setminus\{k,t_i\})\cup A_s\cup\{b\},\\
 S_i&=(K\setminus D_s)
       \cup\{t_{i-\varepsilon}\}\cup A_s\cup\{b,c_i\}.
\end{aligned}
\tag{3.2}
\]

The old stage paths are

\[
 E_i-Y_i-Z_i-V_i-W_i-Q_i-R_i-S_i-E_i',
 \qquad i\in\mathbb Z_3,
 \tag{3.3}
\]

and the new stage paths are

\[
 E_{i+\varepsilon}-Y_i-Z_i-V_i-W_i-Q_i-R_i-S_i-E_i'.
 \tag{3.4}
\]

### Lemma 3.1 (literal incidence and stage geodesicity)

Every adjacency in (3.3)--(3.4) is literal containment.  Every old and new
stage row is a four-transition Johnson geodesic.  The two stage packets use
the same lower and upper vertices, once each.

#### Proof

For the old row with suffix index \(i\), the four exchanges are

\[
\begin{array}{c|c}
\text{deleted}&\text{inserted}\\ \hline
k&a_{i+\varepsilon}\\
t_i&b\\
t_{i+\varepsilon}&a_{i-\varepsilon}\\
t_{i-\varepsilon}&c_i.
\end{array}
\tag{3.5}
\]

Because the indices are modulo three, \(a_i,a_{i+\varepsilon},
a_{i-\varepsilon}\) are all three elements of \(A_s\), and the three
\(t\)'s are all of \(T\).  The four deleted and four inserted coordinates
are distinct.  Formulae (3.1)--(3.2) are exactly the successive unions and
deletions in (3.5).

For the new row, the initial active coordinate is \(a_{i+\varepsilon}\),
and the first exchange inserts \(a_i\) instead.  The remaining three
exchanges are unchanged.  Again all four exchanges are permanent and
distinct.  Thus both rows have endpoint distance four.

Finally, (3.3) and (3.4) differ only in the first incidence

\[
                         E_iY_i
 \quad\longleftrightarrow\quad
                         E_{i+\varepsilon}Y_i.
\]

These are the two alternating matchings of the common-core \(C_6\) on

\[
 E_0,E_1,E_2;\qquad Y_0,Y_1,Y_2.
\]

All other vertices and incidences are identical. \(\square\)

### Lemma 3.2 (stage monodromy)

The old stage sends label \(i\) to label \(i\).  The new stage sends

\[
                         j\longmapsto j-\varepsilon.
 \tag{3.6}
\]

#### Proof

The suffix indexed by \(i\) ends at \(E_i'\).  It is entered from \(E_i\)
in the old packet and from \(E_{i+\varepsilon}\) in the new packet. \(\square\)

Consequently the two new stage actions are \(\tau^{-1}\) and \(\tau\), and

\[
                         \tau^{-1}\tau=1.
 \tag{3.7}
\]

Both complete packets therefore carry \(E_{0,i}\) to \(E_{2,i}\).

## 4. The two-transition complementary cap

Put \(M=K_2\).  Define

\[
\begin{aligned}
 P_i&=M\cup\{a_{2,i},a_{2,i+1}\},\\
 C_i&=(M\setminus\{a_{0,i}\})
        \cup\{a_{2,i},a_{2,i+1}\},\\
 T_i^*&=(M\setminus\{a_{0,i}\})\cup A_2,\\
 F_i&=(M\setminus\{a_{0,i},h\})\cup A_2.
\end{aligned}
\tag{4.1}
\]

Here \(P_i,T_i^*\) are upper \(11\)-sets and \(C_i,F_i\) are lower
\(10\)-sets.  Append the unchanged cap

\[
                  E_{2,i}-P_i-C_i-T_i^*-F_i.
 \tag{4.2}
\]

Its exchanges are

\[
                         a_{0,i}\mapsto a_{2,i+1},
 \qquad
                         h\mapsto a_{2,i-1}.
 \tag{4.3}
\]

The order in (4.3) matters: deleting \(a_{0,i}\) before deleting \(h\)
keeps the three second cap colours \(T_i^*\) distinct.

### Theorem 4.1 (closed literal factor trade)

Concatenate the two stages and the cap.  Both the old and new packet are
families of three pairwise vertex-disjoint length-ten Johnson geodesics

\[
                         E_{0,i}\longrightarrow F_i,
 \qquad i\in\mathbb Z_3,
\]

and

\[
                         F_i=\Omega\setminus E_{0,i}.
 \tag{4.4}
\]

They use the same complete \(X/Y\) ledger.

#### Proof

By Lemma 3.2, the two opposite new monodromies cancel, so both packets
arrive at the same \(E_{2,i}\) before using the common cap.

For either packet, the coordinates deleted on the row rooted at
\(E_{0,i}\) are exactly

\[
                         D_0\mathbin{\dot\cup}D_1
                         \mathbin{\dot\cup}\{h,a_{0,i}\}.
 \tag{4.5}
\]

These are precisely the ten coordinates of

\[
                         E_{0,i}=\{h\}\cup D_0\cup D_1\cup\{a_{0,i}\}.
\]

The inserted coordinates are exactly

\[
 \{b_0,b_1\}
 \mathbin{\dot\cup}(A_0\setminus\{a_{0,i}\})
 \mathbin{\dot\cup}A_1
 \mathbin{\dot\cup}A_2,
 \tag{4.6}
\]

the ten coordinates of its complement.  To see (4.6) for the new packet,
note that the first stage inserts the two missing \(A_0\)-coordinates and
one \(A_1\)-coordinate; the reverse-oriented second stage inserts the two
remaining \(A_1\)-coordinates and, because the monodromy has closed, the
coordinate \(a_{2,i}\).  The cap inserts the remaining two \(A_2\)-coordinates.

No coordinate in (4.5) or (4.6) repeats.  Hence every row is a ten-step
path between complementary \(10\)-sets and is a Johnson geodesic.

The exact equality of the ledgers follows stagewise from Lemma 3.1 and
from the common cap.  Pairwise distinctness of all ledger tokens is proved
in Section 5. \(\square\)

By the middle-level path normal form, each path in Theorem 4.1 reconstructs
a literal odd-cycle wreath after adjoining infinity.  Thus this is a
physical path trade, not an abstract endpoint permutation.

## 5. Complete \(X/Y\) crossing-collar ledger

There are no suppressed collars.  For one stage, put

\[
                         L_s=K_s\setminus D_s.
\]

Suppressing the stage index on the active symbols, the complete stage
ledger is as follows; in the two tables, \(+\) denotes union of the
displayed disjoint coordinate blocks.

\[
\begin{array}{c|l|c}
\text{lower state}&\text{set}&
(|D_s\cap X|,|A_s\cap X|,1_{b_s\in X},|A_{s+1}\cap X|)\\ \hline
E_i&L_s+D_s+a_i&(4,1,0,0)\\
Z_i&L_s+T_s+a_i+a_{i+\varepsilon}&(3,2,0,0)\\
W_i&L_s+(T_s\setminus t_i)+a_i+a_{i+\varepsilon}+b_s&(2,2,1,0)\\
R_i&L_s+t_{i-\varepsilon}+A_s+b_s&(1,3,1,0)\\
E_i'&L_s+A_s+b_s+a_{s+1,i}&(0,3,1,1),
\end{array}
\tag{5.1}
\]

and

\[
\begin{array}{c|l|c}
\text{upper colour}&\text{set}&
(|D_s\cap Y|,|A_s\cap Y|,1_{b_s\in Y},|A_{s+1}\cap Y|)\\ \hline
Y_i&L_s+D_s+a_i+a_{i+\varepsilon}&(4,2,0,0)\\
V_i&L_s+T_s+a_i+a_{i+\varepsilon}+b_s&(3,2,1,0)\\
Q_i&L_s+(T_s\setminus t_i)+A_s+b_s&(2,3,1,0)\\
S_i&L_s+t_{i-\varepsilon}+A_s+b_s+a_{s+1,i}&(1,3,1,1).
\end{array}
\tag{5.2}
\]

These signatures distinguish the families.  Within a family, the active
singleton or pair, the missing \(t_i\), the retained
\(t_{i-\varepsilon}\), or the added \(a_{s+1,i}\) distinguishes the
three indices.

Across the two stages, the vector

\[
                         (|D_0\cap U|,|D_1\cap U|)
\]

distinguishes all tokens except the intended identities

\[
                         E_{0,i}'=E_{1,i},
 \qquad
                         E_{1,i}'=E_{2,i}.
\]

Indeed, stage-zero internal states have a positive \(D_0\)-count and all
four \(D_1\)-coordinates; stage-one internal states have no \(D_0\) and a
strictly decreasing \(D_1\)-count.  No upper colour is shared between
stages.

For the cap, the membership triples

\[
 (1_{h\in U},|A_0\cap U|,|A_2\cap U|)
\]

are

\[
\begin{array}{c|ccc}
E_2&(1,3,1)\\
C&(1,2,2)\\
F&(0,2,3)
\end{array}
\qquad
\begin{array}{c|ccc}
P&(1,3,2)\\
T^*&(1,2,3).
\end{array}
\tag{5.3}
\]

The missing \(a_{0,i}\) and the \(A_2\)-pair distinguish indices.  Hence
all cap tokens are distinct from each other and from the stage tokens.

The exact ledger sizes are therefore

\[
\begin{aligned}
 |\mathcal X|
 &=3\cdot3+2\cdot3\cdot3+2\cdot3
 =33,\\
 |\mathcal Y|
 &=2\cdot4\cdot3+2\cdot3
 =30.
\end{aligned}
\tag{5.4}
\]

These equal \(3(10+1)\) lower occurrences and \(3\cdot10\) upper
occurrences, exactly as required for three disjoint length-ten strands.

## 6. Exterior motion is exact, row by row

At stage \(s\), take the fixed local four-set

\[
 J_s=\{k_s,a_{s,0},a_{s,1},a_{s,2}\},
 \qquad
 P_{s,j}=\{k_s,a_{s,j}\}.
 \tag{6.1}
\]

For suffix \(i\), put

\[
 O_s^L=K_s\setminus\{k_s\},
 \qquad
 O_{s,i}^R=(K_s\setminus\{k_s,t_{s,i}\})\cup\{b_s\}.
 \tag{6.2}
\]

Then

\[
 |O_s^L\setminus O_{s,i}^R|=1,
 \tag{6.3}
\]

and

\[
 W_{s,i}
 =O_{s,i}^R\cup
   (J_s\setminus P_{s,i-\varepsilon_s}).
 \tag{6.4}
\]

The old input port is \(P_{s,i}\), while the new input port is
\(P_{s,i+\varepsilon_s}\).  Both are distinct from
\(P_{s,i-\varepsilon_s}\), so

\[
 \boxed{
 |O_s^L\setminus O_{s,i}^R|
 =|P_{s,i}\setminus P_{s,i-\varepsilon_s}|
 =|P_{s,i+\varepsilon_s}\setminus P_{s,i-\varepsilon_s}|
 =1.}
 \tag{6.5}
\]

Thus the two-transition carrier part

\[
                         E-Y-Z-V-W
\]

satisfies the moving-exterior metric equation exactly on both shores.
The remaining two transitions do not hide another abstract matching: they
are the displayed literal collar which absorbs all three active petals
into \(K_{s+1}\) and exposes the next active coordinate.

## 7. Linear protected-target carrier audit

For a lower-state path

\[
                         \mathcal V=(V_0,\ldots,V_m),
\]

define its depth-\(q\) lower intersection ledger by

\[
 \Phi_q(\mathcal V)
 =\sum_{j=0}^{m-q}
   \mathbf e_{V_j\cap V_{j+1}\cap\cdots\cap V_{j+q}}.
 \tag{7.1}
\]

Sum this over the three rows and put

\[
                         \Delta_q=\Phi_q(\text{new})-
                                  \Phi_q(\text{old}).
\]

### Theorem 7.1 (nonzero prefix-robust linear carrier)

For the closed packet of Theorem 4.1,

\[
 \boxed{\Delta_1=0,}
 \tag{7.2}
\]

while

\[
 \boxed{
 \Delta_2=\delta_0+\delta_1\ne0,}
 \tag{7.3}
\]

where

\[
 \delta_s=
 \sum_{i\in\mathbb Z_3}
 \left(
 \mathbf e_{(K_s\setminus\{k_s,t_{s,i}\})
                    \cup\{a_{s,i+\varepsilon_s}\}}
 -
 \mathbf e_{(K_s\setminus\{k_s,t_{s,i}\})
                    \cup\{a_{s,i}\}}
 \right).
 \tag{7.4}
\]

All twelve signed atoms in (7.4) are distinct.  Hence

\[
                         \|\Delta_2\|_1=12.
 \tag{7.5}
\]

#### Proof

Inside suffix \(i\) of stage \(s\), the only changed consecutive lower
pair is the first one.  Its old and new intersections are

\[
\begin{aligned}
 E_i\cap Z_i
   &=(K_s\setminus\{k_s\})\cup\{a_{s,i}\},\\
 E_{i+\varepsilon_s}\cap Z_i
   &=(K_s\setminus\{k_s\})\cup\{a_{s,i+\varepsilon_s}\}.
\end{aligned}
\tag{7.6}
\]

Summing (7.6) over \(i\) is a cyclic reindexing, so it is zero.  Every
other consecutive pair lies wholly in an unchanged physical suffix or in
the common cap.  This proves (7.2).

For three consecutive lower states, the local router window gives

\[
\begin{aligned}
 E_i\cap Z_i\cap W_i
   &=(K_s\setminus\{k_s,t_{s,i}\})\cup\{a_{s,i}\},\\
 E_{i+\varepsilon_s}\cap Z_i\cap W_i
   &=(K_s\setminus\{k_s,t_{s,i}\})
       \cup\{a_{s,i+\varepsilon_s}\}.
\end{aligned}
\tag{7.7}
\]

These are exactly the terms of \(\delta_s\).

It remains to audit the collars.  At an entrance \(E_{s,j}\), the new
suffix has index (j-\varepsilon_s), and

\[
 E_{s,j}\cap Z_{s,j}
 =E_{s,j}\cap Z_{s,j-\varepsilon_s}
 =(K_s\setminus\{k_s\})\cup\{a_{s,j}\}.
 \tag{7.8}
\]

Therefore, for an arbitrary predecessor lower state \(H_j\),

\[
 H_j\cap E_{s,j}\cap Z_{s,j}
 =H_j\cap E_{s,j}\cap Z_{s,j-\varepsilon_s}.
 \tag{7.9}
\]

Thus every predecessor--entrance crossing window cancels rowwise.  Every
other three-state window is wholly inside a fixed suffix and is merely
reassigned to another owner.  At the exit of the second stage the two
monodromies have already canceled, so all cap-crossing windows are
literally unchanged.  Equations (7.7)--(7.9) prove (7.3).

Within one \(\delta_s\), equality of a positive atom indexed by \(i\) and
a negative atom indexed by \(j\) first forces

\[
                         j=i+\varepsilon_s
\]

from the unique \(A_s\)-coordinate, and then forces

\[
                         t_{s,i}=t_{s,j},
\]

contrary to the three distinct tags.  Hence the six atoms in each
\(\delta_s\) are distinct.  Finally, every atom of \(\delta_1\) contains
\(b_0\in K_1\), while no atom of \(\delta_0\) contains \(b_0\).  The two
supports are disjoint, proving (7.5). \(\square\)

The opposite endpoint monodromies therefore do **not** negate the quota
improvement.  They cancel only the transported port permutation; their
depth-two carrier atoms live in different full contexts and add.

## 8. Complete literal cyclic-OR ledger

The linear ledger of Section 7 is the protected \(X\)-path target.  A
literal contiguous-OR audit must also include the complementary reverse
half and the infinity seam of the reconstructed odd cycle.  This section
does so exactly.

Write the coordinates of a minimum wreath in deletion order, insertion
order, and then infinity.  For the old row rooted at \(E_{0,i}\), the
resulting \(21\)-letter cyclic word is

\[
\begin{aligned}
\Pi_i^-={}&(
k_0,t_{0,i},t_{0,i+1},t_{0,i-1},
k_1,t_{1,i},t_{1,i-1},t_{1,i+1},a_{0,i},h,\\
&a_{0,i+1},b_0,a_{0,i-1},a_{1,i},
a_{1,i-1},b_1,a_{1,i+1},a_{2,i},
a_{2,i+1},a_{2,i-1},\infty).
\end{aligned}
\tag{8.1}
\]

The new row first uses stage-zero suffix \(i-1\), then stage-one suffix
\(i\), and has word

\[
\begin{aligned}
\Pi_i^+={}&(
k_0,t_{0,i-1},t_{0,i},t_{0,i+1},
k_1,t_{1,i},t_{1,i-1},t_{1,i+1},a_{0,i},h,\\
&a_{0,i-1},b_0,a_{0,i+1},a_{1,i-1},
a_{1,i},b_1,a_{1,i+1},a_{2,i},
a_{2,i+1},a_{2,i-1},\infty).
\end{aligned}
\tag{8.2}
\]

In each word, the first ten symbols form \(E_{0,i}\), the next ten form
\(\Omega\setminus E_{0,i}\), and infinity is last.  Every coordinate of
\(\Omega\cup\{\infty\}\) therefore occurs exactly once.  Thus
(8.1)--(8.2) are literal minimum-wreath cyclic words, not formal strand
labels.

For a cyclic word \(\Pi=(z_0,\ldots,z_{20})\), let

\[
 I_\Pi(j,\ell)=\{z_j,z_{j+1},\ldots,z_{j+\ell-1}\},
\tag{8.3}
\]

with indices modulo \(21\), and define the full pointed cyclic histogram

\[
 {\cal H}_q(\Pi)=\sum_{j=0}^{20}
          \mathbf e_{I_\Pi(j,10-q)}.
\tag{8.4}
\]

Put

\[
 \widehat\Delta_q=\sum_i
       \bigl({\cal H}_q(\Pi_i^+)-{\cal H}_q(\Pi_i^-)\bigr).
\tag{8.5}
\]

For compactness, write

\[
 H=\{h\},\qquad B=\{b_0,b_1\},\qquad
 T_{s,\widehat j}=T_s\setminus\{t_{s,j}\}.
\tag{8.6}
\]

The two intrinsic stage terms \(\delta_0,\delta_1\) are those in (7.4).
Define four collar terms:

\[
\begin{aligned}
\eta_1
={}&\sum_i\Bigl(
\mathbf e_{\{b_1,\infty,k_0\}\cup A_2\cup\{a_{1,i}\}
                    \cup T_{0,\widehat i}}\\
&\hspace{44mm}-
\mathbf e_{\{b_1,\infty,k_0\}\cup A_2\cup\{a_{1,i}\}
                    \cup T_{0,\widehat{i+1}}}
\Bigr),
\end{aligned}
\tag{8.7}
\]

\[
\begin{aligned}
\eta_{11}
={}&\sum_i\Bigl(
\mathbf e_{B\cup A_1\cup\{a_{0,i}\}
                    \cup(A_2\setminus\{a_{2,i+1}\})}\\
&\hspace{36mm}-
\mathbf e_{B\cup A_1\cup\{a_{0,i}\}
                    \cup(A_2\setminus\{a_{2,i}\})}
\Bigr),
\end{aligned}
\tag{8.8}
\]

\[
\begin{aligned}
\eta_{15}
={}&\sum_i\Bigl(
\mathbf e_{\{b_1,\infty,k_0\}\cup A_2
                    \cup\{a_{1,i},t_{0,i+1}\}}\\
&\hspace{40mm}-
\mathbf e_{\{b_1,\infty,k_0\}\cup A_2
                    \cup\{a_{1,i},t_{0,i-1}\}}
\Bigr),
\end{aligned}
\tag{8.9}
\]

\[
\begin{aligned}
\eta_{16}
={}&\sum_i\Bigl(
\mathbf e_{\{\infty,k_0\}\cup A_2\cup\{a_{1,i}\}
                    \cup T_{0,\widehat i}}\\
&\hspace{38mm}-
\mathbf e_{\{\infty,k_0\}\cup A_2\cup\{a_{1,i}\}
                    \cup T_{0,\widehat{i+1}}}
\Bigr).
\end{aligned}
\tag{8.10}
\]

### Theorem 8.1 (complete cyclic carrier)

The complete cyclic-word changes are

\[
 \boxed{\widehat\Delta_1=\eta_1,\qquad
        \|\widehat\Delta_1\|_1=6,}
\tag{8.11}
\]

and

\[
 \boxed{\widehat\Delta_2
 =\delta_0+\delta_1+\eta_{11}+\eta_{15}+\eta_{16},
 \qquad
 \|\widehat\Delta_2\|_1=30.}
\tag{8.12}
\]

In particular both complete literal cyclic ledgers are nonzero.

#### Proof

Compare the \(21\) cyclic intervals in (8.4) directly using the displayed
words (8.1)--(8.2).  An interval which avoids all changed positions is
identical.  If its change is only a cyclic shift of the row index, its
sum over \(i\) is zero.  The complete surviving-start table is

\[
\begin{array}{c|c}
q&\text{nonzero aggregate cyclic starts}\\ \hline
1&15:\eta_1\\
2&2:\delta_0,\quad 6:\delta_1,\quad
   11:\eta_{11},\quad15:\eta_{15},\quad16:\eta_{16}.
\end{array}
\tag{8.13}
\]

All other starting positions are identical or cancel by cyclic
reindexing.  Thus at \(q=1\) the only surviving orbit is the
infinity/reverse collar (8.7).  At \(q=2\), the two forward router windows
are exactly \(\delta_0,\delta_1\); the three additional surviving orbits
are respectively the complementary cap, the infinity collar, and the
reverse \(D_0\)-collar in (8.8)--(8.10).

For noncancellation, the five \(q=2\) orbit supports have different block
signatures:

* \(\delta_0\) contains \(h\) and the full block \(D_1\), but not \(b_0\);
* \(\delta_1\) contains \(h,A_0,b_0\) and a two-subset of \(T_1\);
* \(\eta_{11}\) contains \(B,A_1\), one \(A_0\)-coordinate and two
  \(A_2\)-coordinates, but neither \(h\) nor infinity;
* \(\eta_{15}\) contains \(\infty,k_0,b_1,A_2\) and one \(t_0\);
* \(\eta_{16}\) contains \(\infty,k_0,A_2\) and two \(t_0\)'s, but not
  \(b_1\).

Hence atoms from different orbits cannot coincide.  Within each orbit,
the displayed owner coordinate first forces equality of the indices, and
then the missing \(t\)- or \(a\)-coordinate differs between the positive
and negative atom.  Thus every orbit consists of six distinct signed
atoms.  Equation (8.11) has one such orbit and (8.12) has five. \(\square\)

This independent reverse-half audit strengthens, rather than weakens, the
linear result: inverse monodromy closes the physical ports while all
literal cyclic collar contributions remain nonzero.

## 9. Minimality within the absorption normal form

The construction has the smallest parameters in the following explicit
class.

> A block-disjoint absorption packet is a serial packet in which each
> common-core \(C_6\) stage has a fixed local four-port chart, a common
> deleted coordinate \(k_s\), three distinct private exterior tags
> \(t_{s,0},t_{s,1},t_{s,2}\), and a geodesic connector which absorbs the
> current active triple into the next common core and exposes a fresh
> active triple.

### Proposition 9.1 (sharp rank in this class)

A closed productive packet in this class has rank at least \(10\).  The
construction above attains rank \(10\).

#### Proof

One \(C_6\) switch has nonidentity order-three monodromy, so at least two
stages are needed.  Two stages can close with opposite orientations, as
above.

For a prefix-robust invariant depth-two tag, one stage needs the four
distinct deleted coordinates

\[
                         D_s=\{k_s,t_{s,0},t_{s,1},t_{s,2}\}.
\]

On a global minimum path a deleted coordinate cannot be reinserted, so
the deletion blocks of two stages are disjoint.  Absorbing the petals and
exposing the next stage requires three active triples

\[
                         A_0,A_1,A_2
\]

and one common filler \(b_s\) per stage.  Thus the construction requires
at least

\[
                         2\cdot4+3\cdot3+2=19
\]

distinct coordinates.  A middle-level ground set has even size \(2m\),
so \(2m\ge20\) and \(m\ge10\).  Equations (2.1)--(2.4) use exactly twenty
coordinates. \(\square\)

This is not an absolute classification of all possible overlapping or
multiway carrier trades.  Rank below ten outside the stated normal form is
not ruled out.

## 10. Exact implication boundary

The following statements are proved.

1. Common exterior motion never turns an identity anchored port slot into
   a nonidentity exact replacement; Theorem 1.1 remains valid with
   arbitrary internal collars and multiple cuts.
2. Owner-dependent exterior motion can be made literal and geodesic.
3. Two oppositely oriented common-core \(C_6\) stages admit a fully closed
   rank-\(10\) realization with identity total monodromy.
4. The complete lower/upper token ledger, both connectors, the stage seam,
   and the complementary cap are exact.
5. The linear depth-two carrier has twelve distinct atoms, and the full
   cyclic-word depth-two carrier has thirty; both survive inverse-monodromy
   closure.

All carrier formulae above are unlabelled three-row aggregate histograms.
The stronger common-owner-labelled profile changes at additional starts
and has not been claimed to satisfy balanced owner quotas.

The following statements remain unproved.

1. The old \(33/30\)-token packet has not been extended to a spanning
   \(D_{10}\)-port-transversal middle-level path factor.
2. No positive-density packing of contextual copies inside growing exact
   factors is established.
3. The signed atoms in (7.4) have not yet been aligned with every Gaussian
   deletion quota, and no \(PCap=o(W)\) estimate follows here.
4. Therefore the sharp constant-one theorem is not claimed.

The surviving theorem target is now concrete: embed and pack this closed
rank-\(10\) trade, rather than trying to realize an isolated abstract
incidence cycle.  Any such embedding must preserve the literal port roots,
all \(33\) lower states, all \(30\) upper colours, the twelve-atom linear
ledger (7.4), and the thirty-atom cyclic ledger (8.12).

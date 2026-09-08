# Fixed-12 recharge: owner-resolved relative installation and the PBBS/SCD gate

**Date:** 2026-07-27  
**Lane:** O, deterministic fixed-12 recharge source allocation  
**Method:** pure mathematics only

---

## 0. Outcome

Put
\[
n=2m,\qquad M=m+H,\qquad
\kappa=4H-1,\qquad d=M-\kappa=m-3H+1,
\tag{0.1}
\]
and
\[
N=\binom nM,\qquad W=\binom nm,\qquad
\lambda=\frac WN.
\tag{0.2}
\]
Assume
\[
H=o(m),\qquad H\ge3,\qquad M\ge18H-10,
\qquad M\le\lambda,\qquad \lambda-M=O(H).
\tag{0.3}
\]
Then
\[
W-dN=(\lambda-d)N=\Theta(HN)=o(W),
\qquad dN=W-o(W).
\tag{0.4}
\]
Also \(N/W=1/\lambda=O(1/m)\).  In particular, polynomially many
rows or owner occurrences are negligible on the \(N\)- or \(W\)-scale,
respectively.  (The calibrated relation in (0.3) in particular forces
\(H\to\infty\).)

This report proves the following.

1. A one-cyclic-word-per-\(M\)-top owner table is, after complementation,
   exactly the already isolated one-frame-per-\((m-H)\)-root **CPM
   entrance object**.  Loads, holes, and repeat excess agree
   coefficientwise.  This does not by itself supply all signed CPM
   target requirements.

2. There is no scalar owner Hall obstruction if the cyclic-word
   condition is erased.  The top--owner inclusion graph has an integral
   \(b\)-matching assigning \(d\) distinct owners to every top and using
   every owner at most once.  The entire difficulty is that the \(d\)
   assigned owners at one top, equivalently their omitted \(H\)-sets,
   must be consecutive \(H\)-windows of one word.

3. There is a sharp deterministic relative-installation theorem.  If
   \(o\) is the owner-occurrence vector removed from selected top rows
   and \(b\) is the equal-mass vector inserted by fixed-12 source rows,
   then, with \(\mu_1=\mu_0-o+b\),
   \[
   \frac12\|b-o\|_1\le Z_0+\operatorname{Exc}(\mu_1),
   \tag{0.5}
   \]
   and
   \[
   \operatorname{Exc}(\mu_1)
   \le \operatorname{Exc}(\mu_0)+\frac12\|b-o\|_1.
   \tag{0.6}
   \]
   Hence, from a table with \(o(W)\) holes and repeats, a
   positive-density source installation has \(o(W)\) repeats **if and
   only if**
   \[
   \|b-o\|_1=o(W).
   \tag{0.7}
   \]
   This is the exact owner-resolved source condition.  Equivalently,
   the inserted positive-density deck must be squarefree up to \(o(W)\),
   and all but \(o(W)\) of its owners must occupy slots whose final old
   occurrence was removed.

4. Once a fixed-12 source shore has been installed, firing the packet
   preserves the complete middle-owner multiplicity vector, not merely
   its support.  It also preserves every protected trace vector and
   every rooted position--label histogram.  Thus no additional
   cross-packet owner-disjointness is required for a top-disjoint packet
   layer.

5. Rooted-position breadth is free for a **sublinear prescribed bank**,
   but is not proved free for a positive-density packet layer.  Any
   top-disjoint bank of \(t=o(N)\) repaired packets can be installed
   relative to a partial low-repeat word table, with total excess
   increase at most
   \[
   d\ell+12dt+(4H-1)N=o(W),
   \]
   where \(\ell=o(N)\) is the number of initially missing rows; all
   rooted position--label cells still have \((1-o(1))N/n\) support.
   In particular, one may use only \(O(m^3)\) packets to obtain a
   literal source for every signed adjacent position and ordered
   adjacent label pair at cost \(O(m^4)=o(W)\) owner occurrences.

6. This sparse positive theorem cannot be scaled blindly.  At
   \(\Theta(N)\) packets its black-box overwrite cost is \(\Theta(W)\),
   and (0.5) makes aggregate deck alignment necessary.  Moreover, a
   common cyclic shift of the twelve words preserves their full cyclic
   decks and balances histograms, but the repaired trace telescope is
   rooted: its local theorem certifies only the displayed source phase.
   Positive-density root balancing therefore also requires a
   phase-compatible packet selection; it does not follow by rerooting
   already selected packets.  For one approximate layer, arbitrary
   phases have only \(\|\Delta_h\|_1\le2N\) at each protected rank and
   total seam \(O(HN)=o(W)\), but this is not exact and cannot be summed
   blindly through \(\Theta(m)\) layers.

7. Fixed, bounded, or polynomial libraries of ambient-order
   BTK/SCD frames are rigorously excluded.  If all but \(12K\) top words
   are restrictions of \(L\) ambient cyclic orders, then their retained
   owner support is at most
   \[
   nL\,2^{-H}W+12dK.
   \tag{0.9}
   \]
   Thus \(L=o(2^H/n)\) and \(dK=o(W)\) force \(W-o(W)\) holes and
   repeats.

8. Direct use of an intact product-SCD diagonal is also impossible.
   A top-frame owner word must satisfy the portal identity
   \[
   a_t=b_{t+H},
   \tag{0.10}
   \]
   whereas a product diagonal removes labels in one fixed half and
   inserts labels in the disjoint half.  No intact segment longer than
   \(H\) can be a source row.  Covering \(W-o(W)\) owners by such pieces
   needs at least \((1-o(1))W/H\) pieces.

9. The same portal identity is the exact **local necessary PBBS
   chronology test**.  A complete cyclic frame additionally requires
   distinct insertion labels and one consistent \(M\)-top, as in
   Proposition 10.1.  PBBS owner disjointness and its known \(q=1,2\)
   support theorems do not imply (0.10) on \(W-o(W)\) starts.  An
   edge-faithful PBBS installation must first factor or rethread its
   owner chronology into promotion rings satisfying all of (10.2).

Accordingly, a broad sparse fixed-12 source bank is proved relative to
an already physical low-repeat partial word table.  No existing abstract
PBBS/SCD factor is converted into such a table here.  A positive-density
owner-resolved layer remains open.  Its exact gate is
the joint selection of a top-disjoint fixed-12 packet family and source
variants satisfying both the deck-distance condition (0.7) and the
rooted full-trace phase equations (5.9), with the required broad
position--label ledger.

---

## 1. Top words and their middle decks

For every top \(U\in\binom{[n]}M\), let
\[
\pi_U=(u_0,u_1,\ldots,u_{M-1})
\]
be a cyclic order of its labels.  Write
\[
I_h(\pi_U,t)=\{u_t,u_{t+1},\ldots,u_{t+h-1}\},
\qquad 0\le h\le2H,\quad t\in\mathbb Z_M,
\tag{1.1}
\]
with \(I_0=\varnothing\).  The middle deck uses \(h=H\).
The full cyclic middle deck is
\[
\Omega(U,\pi_U)
=\{\,U\setminus I_H(\pi_U,t):t\in\mathbb Z_M\,\}.
\tag{1.2}
\]
Because \(H<M/2\), its \(M\) members are distinct.

After choosing a root, normalize the retained starts to
\[
J_d=\{0,1,\ldots,d-1\}.
\]
The retained deck is
\[
\Omega_d(U,\pi_U)
=\{\,U\setminus I_H(\pi_U,t):t\in J_d\,\}.
\tag{1.3}
\]

For a table \(\Pi=(\pi_U)_U\), let
\[
\mu_{\rm cyc}(X)
=\#\{(U,t):X=U\setminus I_H(\pi_U,t),\ t\in\mathbb Z_M\},
\tag{1.4}
\]
and define \(\mu_d\) analogously with \(t\in J_d\).  Put
\[
\operatorname{Exc}(\mu)
=\sum_{X\in\binom{[n]}m}(\mu(X)-1)_+,
\qquad
Z(\mu)=\#\{X:\mu(X)=0\}.
\tag{1.5}
\]

### Lemma 1.1 (mass identities)

One has
\[
\operatorname{Exc}(\mu_{\rm cyc})-Z(\mu_{\rm cyc})
=MN-W,
\tag{1.6}
\]
and
\[
Z(\mu_d)-\operatorname{Exc}(\mu_d)
=W-dN.
\tag{1.7}
\]
In particular,
\[
\operatorname{Exc}(\mu_d)=o(W)
\quad\Longrightarrow\quad
Z(\mu_d)=o(W).
\tag{1.8}
\]

#### Proof

For any nonnegative integer load vector of total mass \(T\),
\[
\sum_X(\mu(X)-1)=T-W.
\]
Its positive part is the repeat excess and each zero coordinate
contributes \(-1\).  Apply this with \(T=MN\) and \(T=dN\), then use
(0.4). ∎

### Lemma 1.2 (retained and full decks are asymptotically equivalent)

For a fixed rooted table,
\[
\operatorname{Exc}(\mu_d)
\le\operatorname{Exc}(\mu_{\rm cyc})
\le\operatorname{Exc}(\mu_d)+\kappa N.
\tag{1.9}
\]
Consequently either excess is \(o(W)\) if and only if the other is.

#### Proof

Deleting occurrences cannot increase repeat excess, proving the first
inequality.  The full table is obtained by adding exactly
\((M-d)N=\kappa N=O(HN)=o(W)\) occurrences.  Each added occurrence
increases excess by at most one. ∎

---

## 2. Exact equivalence with the one-frame-per-root CPM entrance gate

Put
\[
A=[n]\setminus U,\qquad |A|=m-H.
\]
Complementing a middle owner in (1.2) gives
\[
[n]\setminus\bigl(U\setminus I_H(\pi_U,t)\bigr)
=A\cup I_H(\pi_U,t).
\tag{2.1}
\]

### Theorem 2.1 (complement equivalence)

Choosing one cyclic order on every rank-\(M\) top is in bijection with
choosing one cyclic \(H\)-extension frame on every rank-\((m-H)\) root.
Under complementation:

1. every phase occurrence corresponds bijectively;
2. every target load is preserved;
3. support size, holes, and repeat excess are identical; and
4. changing the cyclic root changes neither full deck.

Thus the present owner-resolved source-table problem contains exactly
the one-frame-per-root CPM entrance gate, not the later simultaneous
signed-target conclusions of a full CPM theorem.

#### Proof

The map \(U\leftrightarrow A=U^c\) is a bijection between the two root
layers, and complementation is a bijection of the middle layer.  Equation
(2.1) identifies every phase occurrence.  All four assertions follow
coefficientwise. ∎

This equivalence is important for implication scope: PBBS or SCD data
which solve only an abstract owner partition, separate signed layers, or
individual histories do not yet supply the one-frame-per-root object.

---

## 3. The scalar owner relaxation is integrally feasible

Let \(\mathcal I\) be the bipartite inclusion graph with left side
\[
\mathcal U=\binom{[n]}M
\]
and right side
\[
\mathcal X=\binom{[n]}m,
\]
where \(U\sim X\) if \(X\subset U\).

Its left and right degrees are
\[
L=\binom MH,\qquad R=\binom mH.
\tag{3.1}
\]
Double counting gives
\[
\frac LR=\frac WN=\lambda.
\tag{3.2}
\]

### Theorem 3.1 (uncyclic exact owner allocation)

There is an integral selection of \(d\) distinct incident owners at
every top such that no owner is selected at two tops.

#### Proof

For any \(\mathcal S\subseteq\mathcal U\),
\[
L|\mathcal S|
=e(\mathcal S,N(\mathcal S))
\le R|N(\mathcal S)|.
\]
Therefore
\[
|N(\mathcal S)|\ge\lambda|\mathcal S|\ge d|\mathcal S|,
\]
using \(d<M\le\lambda\).  These are exactly the capacitated Hall
inequalities for left demand \(d\) and right capacity one.  Integral
max-flow gives the desired selection. ∎

The theorem gives zero repeats and exactly \(W-dN=o(W)\) unused owners.
It proves that neither top capacity nor owner capacity is the missing
gate.

### Proposition 3.2 (the exact cyclic row condition)

Suppose owners \(X_{U,0},\ldots,X_{U,d-1}\subset U\) have been assigned
to one top, and put
\[
D_{U,t}=U\setminus X_{U,t}\in\binom UH.
\]
They are the retained deck of one word on \(U\) in the stated order if
and only if there are distinct labels
\[
z_0,z_1,\ldots,z_{d+H-2}\in U
\]
such that
\[
D_{U,t}=\{z_t,z_{t+1},\ldots,z_{t+H-1}\}
\qquad(0\le t<d).
\tag{3.3}
\]
The unused labels of \(U\) may then be inserted in the remaining word
positions arbitrarily.

#### Proof

Necessity is the definition of consecutive retained \(H\)-windows.
Conversely, the displayed distinct sequence can be completed to an
ordering of \(U\), and its first \(d\) windows are exactly (3.3). ∎

Thus Theorem 3.1 becomes the physical source table only after imposing
(3.3) simultaneously in every row.  This is the precise cyclic packet
constraint hidden by the scalar Hall relaxation.

---

## 4. The sharp relative deck-distance theorem

Let \(\mu_0\) be the retained middle load of an existing one-word-per-top
table.  Select a set \(\mathcal S\) of tops.  Let \(o_X\) count the old
occurrences removed from their rows and let \(b_X\) count the occurrences
inserted by proposed fixed-12 source rows.  Thus
\[
0\le o_X\le\mu_0(X)\qquad\text{for every }X.
\]
Both vectors have the same
mass
\[
\sum_Xo_X=\sum_Xb_X=d|\mathcal S|.
\tag{4.1}
\]
The new load is
\[
\mu_1=\mu_0-o+b.
\tag{4.2}
\]
Define
\[
\Delta(o,b)
:=\sum_X(b_X-o_X)_+
=\frac12\|b-o\|_1.
\tag{4.3}
\]

### Theorem 4.1 (relative installation inequalities)

With
\[
E_i=\operatorname{Exc}(\mu_i),
\qquad Z_0=Z(\mu_0),
\]
one has
\[
\boxed{E_1\le E_0+\Delta(o,b)}
\tag{4.4}
\]
and
\[
\boxed{\Delta(o,b)\le Z_0+E_1.}
\tag{4.5}
\]
Consequently, if \(E_0+Z_0=o(W)\), then
\[
\boxed{
E_1=o(W)\quad\Longleftrightarrow\quad
\|b-o\|_1=o(W).}
\tag{4.6}
\]

#### Proof

For (4.4), use the pointwise inequality
\[
(\mu_0(X)+b_X-o_X-1)_+
\le(\mu_0(X)-1)_+ +(b_X-o_X)_+.
\]
Sum over \(X\).

For (4.5), put \(\delta_X=b_X-o_X\).  If \(\delta_X>0\) and
\(\mu_0(X)\ge1\), then
\[
\delta_X\le\mu_1(X)-1.
\]
If \(\mu_0(X)=0\), then \(o_X=0\) and
\[
\delta_X\le1+(\mu_1(X)-1)_+.
\]
Summing over positive \(\delta_X\) gives (4.5).  Equal total masses in
(4.1) give the second identity in (4.3).  The equivalence (4.6) follows
from (4.4)--(4.5). ∎

There is also an exact slot form.  Put \(\nu=\mu_0-o\) and
\(s=\sum_Xb_X\).  Then
\[
\boxed{
\operatorname{Exc}(\nu+b)
=\operatorname{Exc}(\nu)+s
-|\operatorname{supp}b\cap\{X:\nu(X)=0\}|.}
\tag{4.7}
\]
Indeed, an occurrence added to an occupied slot always creates excess,
whereas precisely the first occurrence at an empty slot is free.

### Corollary 4.2 (positive-density vacated-slot law)

Assume \(E_0+Z_0=o(W)\), let \(s=\Theta(W)\), and suppose
\(E_1=o(W)\).  Then
\[
\bigl|\operatorname{supp}b\cap\{X:\mu_0(X)-o_X=0\}\bigr|
=s-o(W),
\tag{4.8}
\]
and in particular
\[
\sum_X(b_X-1)_+
=s-|\operatorname{supp}b|
=o(W).
\tag{4.9}
\]
All but \(o(W)\) of the distinct inserted owners therefore occupy slots
whose final old occurrence was removed; only \(o(W)\) can use
pre-existing holes of \(\mu_0\).  Conversely, (4.8) alone, together
with \(E_0=o(W)\), implies \(E_1=o(W)\).

#### Proof

Put \(\nu=\mu_0-o\).  Removal cannot increase excess, so
\(\operatorname{Exc}(\nu)\le E_0=o(W)\).  Equation (4.7) gives
\[
|\operatorname{supp}b\cap Z(\nu)|
=s+\operatorname{Exc}(\nu)-E_1=s-o(W),
\]
which is (4.8).  Since this intersection has size at most
\(|\operatorname{supp}b|\le s\), (4.9) follows.  At most \(Z_0=o(W)\)
members of \(Z(\nu)\) were already zero under \(\mu_0\); every other
such slot was emptied by removing all of its old occurrences.  The
converse is immediate from (4.7). ∎

Equation (4.6) is the deterministic positive-density gate requested in
the prompt.  A blind overwrite of \(\Theta(N)\) tops moves
\(\Theta(W)\) owner mass.  It is coefficient-safe only if the inserted
fixed-12 deck reproduces the freed deck to \(o(W)\) in total variation.

---

## 5. Owner-safe rerooting and the rooted packet phase lock

For a rooted table define
\[
H_{j,c}=\#\{U:\pi_U(j)=c\},
\qquad j\in\mathbb Z_M,\ c\in[n].
\tag{5.1}
\]

### Theorem 5.1 (blockwise root balancing for full decks)

Suppose the tops are partitioned into blocks of size at most twelve.
Within each block the cyclic words are fixed, but their roots may be
shifted by one common amount.

For all sufficiently large \(m\), there is a choice of one common cyclic
shift in each block such that, simultaneously for all \(j,c\),
\[
\left|H_{j,c}-\frac Nn\right|
\le
8\sqrt{\frac Nn\log(2nM)}.
\tag{5.2}
\]
In particular,
\[
H_{j,c}=(1+o(1))\frac Nn>0.
\tag{5.3}
\]
The shifts preserve every full cyclic owner deck.  They are not asserted
to preserve rooted fixed-12 source compatibility.

#### Proof

Choose the common shift of each block (including each singleton block)
independently and uniformly from \(\mathbb Z_M\).  For fixed \(j,c\),
let \(Y_B\) be the number of rows
of block \(B\) putting \(c\) in position \(j\).  If \(t_{B,c}\) rows
of \(B\) contain \(c\), then
\[
0\le Y_B\le12,\qquad
\mathbb EY_B=\frac{t_{B,c}}M,\qquad
\mathbb EY_B^2\le12\mathbb EY_B.
\tag{5.4}
\]
Since
\[
\sum_Bt_{B,c}=\binom{n-1}{M-1},
\]
we have
\[
\mathbb EH_{j,c}
=\frac1M\binom{n-1}{M-1}
=\frac Nn,
\qquad
\sum_B\operatorname{Var}Y_B\le12\frac Nn.
\tag{5.5}
\]
Bernstein's inequality and a union bound over the \(nM\) cells give
(5.2), with room in the displayed constant.  Full cyclic decks are
invariant under shifts. ∎

The distinction in the last sentence is essential.  For
\(0\le h\le2H\), write
\[
{\cal D}_h(U,p)=\sum_{s=0}^{d-1}e_{U\setminus I_h(p,s)}.
\tag{5.6}
\]
For one repaired packet, let
\[
P_h(a)=\sum_{i=0}^5{\cal D}_h(U_i^P,r^ap_i),
\qquad
Q_h(a)=\sum_{i=0}^5{\cal D}_h(U_i^Q,r^aq_i).
\tag{5.7}
\]
At common phase \(a\), the formal source and target shores would be
\[
r^a{\bf p}\sqcup r^{a+1}{\bf q}
\quad\longrightarrow\quad
r^{a+1}{\bf p}\sqcup r^a{\bf q}.
\tag{5.8}
\]
Their aggregate length-\(h\) derivative is exactly
\[
\bigl(P_h(a+1)-P_h(a)\bigr)
-
\bigl(Q_h(a+1)-Q_h(a)\bigr).
\tag{5.9}
\]
Consequently the formal exchange at phase \(a\) is aggregate
full-trace-neutral if and only if the two discrete derivatives in (5.9)
agree for every protected \(0\le h\le2H\).  The repaired packet theorem
proves this at its
displayed phase \(a=0\), because the two six-cycle telescopes vanish
there separately.  Its filler-column identity proves rooted histogram
cancellation at every common phase, but it does **not** prove (5.9) at
arbitrary \(a\).  Thus Theorem 5.1 cannot reroot a selected packet layer
while retaining its certified source shores.  In particular, (5.9)
alone does not reprove the rooted squarefreeness of the two shores at a
new phase.

There is nevertheless a sharp one-layer approximate statement.  One
cyclic step changes only the entering and leaving boundary atoms:
\[
\bigl\|{\cal D}_h(U,rp)-{\cal D}_h(U,p)\bigr\|_1\le2.
\tag{5.10}
\]
Indeed \(I_h(rp,s)=I_h(p,s+1)\), so all terms cancel except the
entering start \(d\) and the leaving start \(0\); inverse rotation is
identical with the signs reversed.
Consequently a top-disjoint layer, with one arbitrary common phase chosen
for each fixed-12 packet and touching at most \(N\) tops, has
\[
\|\Delta_h\|_1\le2N\quad(0\le h\le2H),
\qquad
\sum_{h=0}^{2H}\|\Delta_h\|_1
\le2(2H+1)N=o(W).
\tag{5.11}
\]
At the middle rank its repeat excess can rise by at most \(N=o(W)\).
Thus one arbitrary-phase approximate layer has aggregate trace-ledger
defect \(o(W)\), but it is not an exact packet firing and the estimate
cannot be summed over \(\Theta(m)\) layers.

### Corollary 5.2 (retained owner ledger after owner-only balancing)

If the original full cyclic excess is \(o(W)\), then every retained
length-\(d\) table produced by Theorem 5.1 has
\[
\operatorname{Exc}(\mu_d)=o(W),\qquad Z(\mu_d)=o(W).
\tag{5.12}
\]

#### Proof

The retained table is a submultiset of the unchanged full table, so its
excess is no larger.  Apply Lemma 1.1. ∎

The full-deck premise is asymptotically equivalent to any one rooted
length-\(d\) premise by Lemma 1.2.  Thus rooted phase choice creates no
new asymptotic **owner-load** gate.  Simultaneous rooted packet legality
is the additional phase-lock condition (5.9).

---

## 6. Sparse literal fixed-12 installation

Even without a positive-density compatible partition, broad literal
fixed-12 sources can be installed at negligible owner cost.

### Theorem 6.1 (sublinear relative source-bank installation)

Let a partial table carry one rooted cyclic word on all but
\(\ell=o(N)\) tops, and suppose its retained repeat excess is \(E=o(W)\).
Let \(\mathscr P\) be any prescribed top-disjoint family of
\(t=o(N)\) repaired fixed-12 packets, including a prescribed rooted
source shore on their \(12t\) tops.  Then the partial table can be
completed and overwritten to a table \(\Pi'\) such that:

1. every top carries exactly one rooted word;
2. every packet in \(\mathscr P\) occurs literally on its prescribed
   source shore;
3. for every \(j\in\mathbb Z_M\) and \(c\in[n]\),
   \[
   H_{j,c}(\Pi')
   \ge
   \frac Nn-\frac{12t}{M}
   -2\sqrt{\frac Nn\log(2nM)}
   =(1-o(1))\frac Nn;
   \tag{6.1}
   \]
4. and
   \[
   \operatorname{Exc}(\Pi')
   \le E+d\ell+12dt+\kappa N=o(W).
   \tag{6.2}
   \]

This conclusion is relative only to an already physical partial word
table.  In particular, it does not turn an abstract PBBS or SCD owner
factor into top words.

#### Proof

Fill the \(\ell\) missing rows arbitrarily.  This adds at most \(d\ell\)
to repeat excess.  On every packet top discard the current retained row
and insert the prescribed source row.  Deletion cannot increase excess,
and the \(12t\) inserted rows contain \(12dt\) occurrences, so this step
adds at most \(12dt\).

Keep the packet roots fixed.  Give every other row an independent
uniform cyclic phase.  Changing the root of one word replaces one
length-\(d\) interval of starts in \(\mathbb Z_M\) by another.  The
complements of these intervals both have size
\(\kappa=M-d\); hence at most \(\kappa\) new starts are introduced.
Arbitrary rerooting of all free rows therefore raises repeat excess by
at most \(\kappa N\).  This proves (6.2), since
\[
d\ell+12dt=o(dN)=o(W),\qquad
\kappa N=O(HN)=o(W).
\tag{6.3}
\]

Fix \(j,c\).  There are
\[
\binom{n-1}{M-1}-r_c
\qquad\text{free tops containing }c,
\qquad 0\le r_c\le12t.
\]
Each independently puts \(c\) in column \(j\) with probability \(1/M\).
Thus the free-row contribution has mean
\[
\mu_{j,c}
=\frac1M\left(\binom{n-1}{M-1}-r_c\right)
\ge\frac Nn-\frac{12t}{M}.
\tag{6.4}
\]
The lower-tail Chernoff bound with
\(2\sqrt{\mu_{j,c}\log(2nM)}\), followed by a union bound over the
\(nM\) pairs, leaves positive probability that all cells satisfy
(6.1); replacing \(\mu_{j,c}\) in the error by the larger \(N/n\)
only weakens the bound.  The fixed packet rows contribute
nonnegatively.  Since \(t=o(N)\) and \(N/n\) is exponential in \(m\),
the right side of (6.1) is \((1-o(1))N/n\).  Choose one such phase
assignment. ∎

The theorem is sharp in scale for a black-box overwrite.  At
\(t=\Theta(N)\), the term \(12dt\) is \(\Theta(W)\), and the
deck-distance condition of Theorem 4.1 becomes necessary.

### Theorem 6.2 (polynomial universal source bank)

Starting from any one-word-per-top table with \(o(W)\) middle repeats,
one may overwrite a top-disjoint bank of at most
\[
K\le2Mn(n-1)=O(m^3)
\tag{6.5}
\]
repaired fixed-12 source packets so that:

1. for every adjacent rooted pair \(j,j+1\);
2. for every ordered coordinate pair \(c\ne c'\); and
3. for each of the two rotation signs,

some certified source row has \(c,c'\) in those adjacent positions and
moves in the prescribed sign.  The two signs mean, explicitly, the
certified source moves \(p\mapsto rp\) and \(rq\mapsto q\).

The resulting table still has one word per top and has middle repeat
excess \(o(W)\).

#### Proof

For each requested tuple, take a fresh relabelled copy of the fixed-12
template.  In a source row having the requested rotation sign, take the
two abstract labels occupying columns \(j,j+1\), and map them in order
to \(c,c'\).  Relabeling preserves every packet identity, so this gives
the requested literal adjacency.
Choose its common \((M-2)\)-core, subject to the membership forced by
the two distinguished labels, so that it is not contained in any top
used earlier.  After polynomially many choices, only polynomially many
cores are forbidden: one earlier top contains only
\(\binom M{M-2}=O(M^2)\) candidate cores, whereas every one of the four
possible forced membership classes has exponentially many admissible
cores.  Choose the remaining carrier labels outside the core and
complete the six-element carrier and the relabeling.  There are enough
outside labels because \(n-(M-2)=m-H+2\ge6\) under (0.3).  The new
twelve tops are disjoint from every earlier packet.

Replacing one top row deletes \(d\) old occurrences and adds \(d\) new
ones, increasing repeat excess by at most \(d\).  Hence all replacements
increase it by at most
\[
12dK=O(m^4)=o(W).
\]
This proves the owner assertion and all prescribed rows are literal by
the repaired fixed-12 theorem. ∎

This theorem proves broad **sparse** installability.  It does not scale
to \(K=\Theta(N)\): the same estimate then becomes \(\Theta(W)\), and
Theorem 4.1 requires actual deck alignment.

---

## 7. Exact fixed-12 relative firing theorem

For a rooted table \(\Pi\), let \(\mathcal K(\Pi)\) be the 12-uniform
hypergraph on rank-\(M\) tops whose edges are precisely the repaired
fixed-12 packet supports whose source shore equals the twelve current
rows of \(\Pi\).

### Theorem 7.1 (owner-free simultaneous firing after source resolution)

Let \(\mathscr M\) be any matching in \(\mathcal K(\Pi)\).  Simultaneously
fire all packets in \(\mathscr M\).  Then:

1. there remains exactly one rooted word on every top;
2. every rooted position--label histogram \(H_{j,c}\) is unchanged;
3. every protected aggregate target vector at deleted length
   \(0\le h\le2H\) is unchanged;
4. the complete retained middle multiplicity vector \(\mu_d\) is
   unchanged coefficientwise; and
5. its holes and repeat excess are therefore unchanged.

The same conclusions hold through an arbitrary chronology of already
source-resolved top-disjoint layers.

#### Proof

The repaired twelve-top theorem proves all coefficientwise equalities
on each packet.  Top disjointness permits the twelve source rows of
different packets to be replaced simultaneously.  Sum the local
identities over \(\mathscr M\).  Induct over chronological layers. ∎

This theorem explains why middle owners must not be inserted as fresh
capacity vertices after the source table has been resolved: packets may
share owner labels across blocks, but firing them does not change the
global load vector at all.

### Corollary 7.2 (fixed-uniformity relative matching criterion)

Suppose there is a set \(\mathcal G\) of \(N-o(N)\) tops such that, in
the induced hypergraph
\(\mathcal K_{\mathcal G}:=\mathcal K(\Pi)[\mathcal G]\), for some
\(D_*\to\infty\) and \(\varepsilon_m\to0\),
\[
d_{\mathcal K_{\mathcal G}}(U)=(1\pm\varepsilon_m)D_*
\quad(U\in\mathcal G),
\tag{7.1}
\]
and
\[
\Delta_2(\mathcal K_{\mathcal G})\le\varepsilon_mD_*.
\tag{7.2}
\]
Then the standard fixed-uniformity near-matching theorem gives a
matching covering \(N-o(N)\) tops.  If \(\Pi\) has \(o(W)\) repeats,
the resulting fixed-12 layer is owner-safe by Theorem 7.1.

The undecorated top hypergraph satisfies favorable formulas
\[
D_{\rm top}=12\binom M2\binom{n-M}4,
\tag{7.3}
\]
\[
\frac{\Delta_{2,\rm top}}{D_{\rm top}}
=\frac6{M(n-M)}=O(m^{-2}).
\tag{7.4}
\]
These do not imply (7.1)--(7.2) for the source-compatible subhypergraph.
In particular, near-regularity merely outside an exceptional
\(o(N)\)-set in the original hypergraph is insufficient: every edge at
a good top could still meet that exceptional reservoir.

---

## 8. A fixed-12 histogram cut beyond broad support

Inside one packet, let \(a_{j,c}\) be the multiplicity of \(c\) in
column \(j\) of the six \(P\)-rows.  Column alignment gives the same
array for the six unshifted \(Q\)-rows.  The old source shore is
\(\mathbf p\sqcup r\mathbf q\), so its twelve-row histogram is
\[
h_{j,c}=a_{j,c}+a_{j+1,c}.
\tag{8.1}
\]

### Proposition 8.1 (alternating-position cut)

If \(M\) is even, every fixed-12 source packet obeys
\[
\sum_{j=0}^{M-1}(-1)^jh_{j,c}=0
\qquad(c\in[n]).
\tag{8.2}
\]
If all but \(R\) tops of a table are partitioned into source packets,
then
\[
\left|\sum_{j=0}^{M-1}(-1)^jH_{j,c}\right|\le R
\qquad(c\in[n]).
\tag{8.3}
\]

If \(M\) is odd and \(h\) denotes the aggregate histogram of the
packet-covered rows, their aggregate preimage array is uniquely
determined over \(\mathbb Q\) by
\[
a_{\bullet,c}
=\frac12(I-S+S^2-\cdots+S^{M-1})h_{\bullet,c},
\tag{8.4}
\]
where \(S\) is cyclic shift.  Nonnegative integrality of this preimage is
a necessary cone condition.  If a full table has residual-row histogram
\(\rho\), the formula applies coordinatewise to
\(h_{\bullet,c}=H_{\bullet,c}-\rho_{\bullet,c}\), not to the full
histogram \(H_{\bullet,c}\) unless \(\rho=0\).

#### Proof

Equation (8.2) follows by alternating (8.1); the two sums cancel when
\(M\) is even.  Each residual top contributes either \(1\) or \(-1\) to
the alternating sum for a coordinate it contains, proving (8.3).
For odd \(M\),
\[
(I+S)(I-S+\cdots+S^{M-1})=I+S^M=2I,
\]
which proves (8.4). ∎

Near-uniform histograms satisfy (8.3) at the \(o(N)\) scale, but broad
support alone does not imply the packet cone condition.  This is a
genuine fixed-12 compatibility invariant, not a middle-owner invariant.

---

## 9. Deterministic ambient-order SCD obstruction

Fix a cyclic ambient order \(\sigma\) of \([n]\).  Give a top \(U\) the
cyclic order induced by restricting \(\sigma\) to \(U\).

### Lemma 9.1 (ambient-run necessity)

If a middle owner \(X\) occurs in a cyclic deck induced by \(\sigma\),
then \(X\) avoids some block of \(H\) consecutive ambient coordinates.

#### Proof

Write \(X=U\setminus D\), where \(D\) is an \(H\)-window in the induced
order on \(U\).  Between the two neighboring \(X\)-labels surrounding
this induced window, the ambient order contains every member of \(D\)
and no member of \(X\).  Hence that ambient gap has length at least
\(H\) and contains an ambient \(H\)-block disjoint from \(X\). ∎

### Theorem 9.2 (few ambient orders have negligible owner support)

Suppose all unmodified top words are restrictions of a library of
\(L\) ambient cyclic orders.  After overwriting \(K\) top-disjoint
fixed-12 packets, the retained middle support is at most
\[
\boxed{
nL\binom{n-H}{m}+12dK
\le nL\,2^{-H}W+12dK.}
\tag{9.1}
\]
If
\[
L=o(2^H/n),\qquad dK=o(W),
\tag{9.2}
\]
then the resulting table has \(W-o(W)\) holes and \(W-o(W)\) repeats.

#### Proof

For a fixed ambient \(H\)-block, the number of middle sets avoiding it
is \(\binom{n-H}{m}\).  Lemma 9.1 and a union bound over the \(n\)
cyclic starts and \(L\) orders give the first term in (9.1).  Each
overwritten packet contributes at most \(12d\) new supported owners.
Finally
\[
\frac{\binom{n-H}{m}}{\binom nm}
=\prod_{i=0}^{H-1}\frac{m-i}{2m-i}
\le2^{-H}.
\]
Under (9.2), the support is \(o(W)\), while the occurrence mass is
\(dN=W-o(W)\).  Both the hole and repeat conclusions follow. ∎

Thus a fixed, bounded, or polynomial library of natural ambient-order
BTK/Greene--Kleitman frames cannot be the desired source table at the
calibrated \(H\).  A successful SCD construction must use exponentially
many root-dependent order profiles or directly solve the CPM frame
factor.

For completeness, the assertion about polynomial libraries follows
from the calibration rather than from an unstated growth hypothesis.
Indeed
\[
\lambda
=\prod_{i=1}^{H}\frac{m+i}{m-i+1},
\qquad
\log\lambda
\le\sum_{i=1}^{H}\frac{2i-1}{m-H+1}
=\frac{H^2}{m-H+1}.
\tag{9.3}
\]
Since \(\lambda\ge M\ge m\) and \(H=o(m)\), this forces
\[
H=\Omega(\sqrt{m\log m}).
\tag{9.4}
\]
Hence \(2^H/n\) dominates every fixed polynomial in \(m\).  The theorem
still applies only to words literally obtained by restricting the
specified ambient orders; it does not exclude arbitrary root-dependent
BTK/SCD rethreadings.

---

## 10. The SCD and PBBS portal obstruction

### Proposition 10.1 (promotion-ring criterion)

Let
\[
X_0,X_1,\ldots,X_{M-1},X_0
\]
be a simple Johnson cycle of \(m\)-sets, and write
\[
X_{t+1}=X_t-a_t+b_t.
\tag{10.1}
\]
It is the complete cyclic owner deck of one top word if and only if,
after cyclic indexing,
\[
\boxed{
b_0,b_1,\ldots,b_{M-1}\text{ are distinct},
\qquad a_t=b_{t+H}\quad(t\in\mathbb Z_M).}
\tag{10.2}
\]
Then
\[
U=\{b_0,\ldots,b_{M-1}\},
\qquad
X_t=U\setminus\{b_t,b_{t+1},\ldots,b_{t+H-1}\}.
\tag{10.3}
\]

For a retained linear segment of a top word, the necessary portal
identity is
\[
a_t=b_{t+H}
\tag{10.4}
\]
whenever both transitions lie in the segment.

#### Proof

For a top word \(b_0,\ldots,b_{M-1}\), shifting the missing
\(H\)-window gives
\[
X_{t+1}=X_t-b_{t+H}+b_t,
\]
proving necessity.

Conversely, under (10.2), coordinate \(b_j\) is inserted at transition
\(j\) and removed at transition \(j-H\).  It is absent in exactly the
\(H\) states whose missing windows contain it and present in the other
\(M-H=m\) states.  Summing these incidences over all \(b_j\) already
accounts for all \(Mm\) state-coordinate incidences, so no coordinate
outside \(U\) occurs.  Formula (10.3) follows. ∎

### Corollary 10.2 (intact product-SCD diagonals cannot be source rows)

Consider the standard oriented product diagonal on a fixed ground
partition \(L\dot\cup R\),
\[
X_i=C_i\cup D_{m-i},
\]
where \(C_i\) moves upward in a chain on \(L\) and \(D_{m-i}\) moves
downward in a chain on \(R\).  Every removed label then lies in \(R\)
and every inserted label lies in the disjoint half \(L\).  Hence (10.4)
fails wherever it is required.  No intact segment of more than \(H\)
transitions is a top-frame source segment.

An edge-faithful cover of \(W-o(W)\) owner occurrences by intact
product-SCD pieces therefore needs at least
\[
\frac{W-o(W)}{H+1}
=(1-o(1))\frac WH
\tag{10.5}
\]
pieces.  In particular it cannot supply an \(o(W/H)\)-component direct
installation that retains those intact pieces as physical components.
Nonlocal endpoint joins are not excluded.

#### Proof

The two sides of (10.4) belong to disjoint coordinate halves.  Thus a
piece contains at most \(H\) transitions and at most \(H+1\) states.
Divide the required owner mass by \(H+1\).  The final asymptotic equality
uses \(H\to\infty\), which follows from the calibrated assumptions. ∎

There is a useful but conditional local diagnostic.  When \(M>2H\), the
Johnson-adjacency graph induced by the cyclic \(H\)-windows of one word
is the cycle \(C_M\): two distinct windows meet in \(H-1\) labels only
when their starts are consecutive.  Hence it contains no triangle.
The natural balanced-product SCD block contains triples
\[
S+\{b\},\qquad S+\{x\},\qquad S+\{y\},
\tag{10.6}
\]
which are pairwise adjacent.  They cannot be installed as three phases
of one top frame **if** a proposed bundling requires those three omitted
\(H\)-sets to lie in that common frame.  The present report does not
prove that a general SCD source assignment imposes this common-top
identification, so this triangle observation is not counted as an
unconditional obstruction.  Nonlocal reassignment among different
blocks remains open.

### PBBS implication scope

For an edge-faithful PBBS installation, Proposition 10.1 applies at
every interior start left after cutting and rethreading.  It applies on
all but \(o(W)\) starts only when the row-boundary loss is \(o(W)\), for
example when the number \(R\) of rows satisfies
\((H+1)R=o(W)\).  The known PBBS middle-owner factor gives owner
uniqueness, and its shallow support results control target images.
Neither statement implies the lag-\(H\) transition identity
\(a_t=b_{t+H}\).

The native centered PBBS chronology makes the missing condition fully
explicit.  On its odd ground set of size \(2r+1\), put
\(W_{\rm PBBS}=\binom{2r+1}{r}\), write \(A_s\) for the PBBS states,
and write \(\lambda_s\) for the omitted edge label.  A centered parity row
\[
B_i=A_{\epsilon+2i}
\]
obeys the audited transition formula
\[
B_{i+1}
=B_i-\{\lambda_{\epsilon+2i+1}\}
     +\{\lambda_{\epsilon+2i}\}.
\tag{10.7}
\]
Therefore a native centered segment can be the middle deck of one
\(H\)-window word only if
\[
\boxed{
\lambda_{\epsilon+2i+1}
=\lambda_{\epsilon+2i+2H}}
\tag{10.8}
\]
at every interior start for which both transitions occur.  In other
words, the relevant omitted label must recur at offset exactly
\(2H-1\) PBBS edges; for general \(H\), this need not be its next
occurrence.  A row of \(L+1\) owner states requires (10.8) at
\((L-H)_+\) consecutive starts.  More exactly, if \(R\) edge-disjoint
rows contain \(S\) owner states in total and row \(j\) has \(L_j\)
transitions, then the number of forced instances of (10.8) is at least
\[
\sum_{j=1}^R(L_j-H)_+
\ge S-(H+1)R.
\tag{10.9}
\]
Hence an edge-faithful collection covering
\(W_{\rm PBBS}-o(W_{\rm PBBS})\) owner states and satisfying
\((H+1)R=o(W_{\rm PBBS})\) would require (10.8) on
\(W_{\rm PBBS}-o(W_{\rm PBBS})\) physical starts.  The audited
no-gap-three theorem already makes the native condition impossible at
\(H=2\); at \(H=3\), the exact gap-five population is only
\((2r+1)(r-1)=o(W_{\rm PBBS})\).  These fixed-depth checks do not
settle the calibrated growing \(H\), but they show concretely why
first-shadow balance is logically orthogonal to source-row legality.

Thus PBBS can close the present gate only by proving a promotion-ring
factorization or a nonlocal rethreading theorem whose output satisfies
(10.2).  Treating the existing PBBS owner cycles as already being
top-word frames is invalid.

---

## 11. The final deterministic source gate

For a family \(\mathscr F\) of top-disjoint candidate fixed-12 packets,
let \(\Gamma_d(\mathscr F)\) be the union of all middle owners which can
occur in any allowed retained source realization of those packets.
Every source selection has occurrence mass \(12d|\mathscr F|\), and
therefore
\[
\operatorname{Exc}_{\rm packet}
\ge
\bigl(12d|\mathscr F|-|\Gamma_d(\mathscr F)|\bigr)_+.
\tag{11.1}
\]
A family for which the right side is \(\Omega(W)\) is a definitive
owner Hall obstruction.  No such positive-density family has been
proved for the full root-dependent packet catalogue.

The exact surviving positive statement is:

> **Owner-resolved fixed-12 source factor (open).** Construct an
> owner-resolved rooted one-frame-per-root CPM entrance table \(\Pi\)
> with full cyclic excess
> \(o(W)\) and broad position--label support, such that the rooted
> compatibility hypergraph \(\mathcal K(\Pi)\) has a positive-density,
> preferably near-perfect, top matching.  For a relative construction
> from a physical PBBS/SCD-derived table, a chosen rooted packet layer
> must in addition have inserted and removed deck vectors at
> \(L^1\)-distance \(o(W)\).

Under the standing \(o(W)\)-hole and \(o(W)\)-excess premise, the
\(L^1\) condition is exactly necessary and sufficient for the owner
load once the rooted layer has been chosen; it is not by itself
equivalent to rooted packet compatibility or to the phase-lock condition
(5.9).  If the displayed object exists, Theorem 7.1 gives exact
simultaneous packet firing without changing its owner or histogram
ledgers.  If it does not, a proof must exhibit either
the owner Hall cut (11.1), a mixed incidence-lattice/odd-set inequality,
or a lower bound
\[
\|b-o\|_1=\Omega(W)
\]
for every positive-density compatible packet selection.

---

## 12. Audited implication boundary

### Proved

1. Exact complement equivalence with the one-frame-per-root CPM entrance
   object.
2. Exact scalar owner \(b\)-matching with no repeats before cyclic row
   constraints.
3. The sharp two-sided relative deck-distance inequalities
   (4.4)--(4.6) and the positive-density vacated-slot law
   (4.8)--(4.9).
4. Near-uniform rooted-position balancing by arbitrary bounded-block
   shifts at the full-deck/owner level; no packet-legality claim is
   attached to those shifts.
5. Relative installation of every prescribed \(o(N)\)-packet
   top-disjoint source bank, with broad rooted-position support and
   \(o(W)\) repeat cost, conditional only on an already physical partial
   low-repeat word table.
6. A universal polynomial, top-disjoint literal fixed-12 source bank
   at \(o(W)\) owner cost.
7. Exact owner and histogram invariance of every installed packet layer.
8. The alternating-position packet cut.
9. The ambient-order BTK/SCD support obstruction (9.1).
10. The promotion-ring portal criterion and the intact product-diagonal
   obstruction.

### Not proved

1. A positive-density or near-perfect fixed-12-compatible matching in
   one low-excess CPM frame table.
2. The deck alignment \(\|b-o\|_1=o(W)\) for a positive-density
   PBBS/SCD-relative installation.
3. A PBBS promotion-ring factorization satisfying the lag-\(H\) portal
   identity on \(W-o(W)\) starts.
4. A nonlocal rethreading of product-SCD histories into one cyclic frame
   per top.
5. A positive-density phase selection satisfying the full-trace
   phase-lock equations (5.9) together with broad rooted support.
6. A chronology of \(\Theta(m)\) compatible layers with distinct useful
   directions.

No constant-one theorem is claimed.  The theorem-level advance is the
complete separation of the two former ambiguities:

- rooted-position breadth is free for every prescribed \(o(N)\)-packet
  bank, because the remaining rows can be phased independently; but
- positive-density source installation has two surviving coupled
  requirements: aggregate owner-deck transport, quantified exactly by
  (4.6), and rooted packet phase compatibility, quantified by (5.9).
  Neither is supplied by ordinary top packing or by the currently proved
  PBBS/SCD projections.

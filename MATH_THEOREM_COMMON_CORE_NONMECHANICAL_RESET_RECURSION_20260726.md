# A deletion-robust nonmechanical common-core reset atlas

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Decision

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 M=m+H,
\]

and assume the calibrated common-core regime

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \Lambda={W\over N_H}=\Theta(m),\qquad
 L=m-3H+1,
\tag{0.1}
\]

with

\[
 \Lambda-L\ge c_0H
\tag{0.2}
\]

for a fixed constant \(c_0>0\). Fix a balanced half
\(P\in\binom{[2m]}m\).

There is a positive answer at the state-atlas and configuration-LP
levels.

For every fixed \(C>0\), set

\[
 D=\lfloor CH\rfloor.
\tag{0.3}
\]

On all but \(e^{-\Omega(m)}N_H\) critical tops, a proportion

\[
 1-e^{-\Omega(m)}
\tag{0.4}
\]

of all labelled common-core orders are at insertion--deletion distance
greater than \(D\) from every exact mechanical necklace. These states
have the following properties.

1. Every state supplies one literal common-core tail order and hence one
   actual \(L\)-phase promotion path.
2. Deleting any one label from a radius-\(D\) state gives a
   radius-\((D-1)\) state. Thus the family is closed under parent
   deletion through \(D=\Theta(H)\) consecutive levels. Insertion gives
   the reverse transition with the safety index reduced by one.
3. Conditioning on any specified physical trace at any deletion length
   \(1\le\ell\le2H\) removes only an \(e^{-\Omega(m)}\) fraction of its
   order realizations.
4. Consequently the complete nonmechanical common-core configuration LP
   retains one unit of root mass on
   \((1-e^{-\Omega(m)})N_H\) tops, uses only literal ordered paths, has
   target load at most one at every signed internal rank, and has total
   unused rank capacity

   \[
      O(H^{3/2}N_H)+e^{-\Omega(m)}W=o(W).
   \tag{0.5}
   \]

Thus the mechanical empty-neighbourhood cut is not an obstruction to a
nonmechanical reset *catalogue*. There is an exponentially dense,
deletion-robust replacement, and it preserves the common-core atlas's
rankwise capacity margins.

This does not yet give an integral one-state-per-top selection. If one
also requires the selected state to be independent of the deletion
history, restriction confluence returns and the ambient-order obstruction
still applies. The surviving coefficient-one gate is therefore an
integral, nonconfluent common-history rounding theorem, not the existence
or the rankwise capacity of reset states.

## 1. Ordered common-core states

Fix a critical top \(U\in\binom{[2m]}M\). An ordered state is a linear
order

\[
 \pi=(\pi_1,\ldots,\pi_M)
\tag{1.1}
\]

of \(U\). It determines

\[
 Q(\pi)=\{\pi_1,\ldots,\pi_{2H}\},\qquad
 w(\pi)=(\pi_{2H+1},\ldots,\pi_M).
\tag{1.2}
\]

Use the displayed orders on the core and the tail. The common-core path
retains the \(L=M-4H+1=m-3H+1\) phases whose full central \(2H\)-word
lies in the tail. At deletion length \(1\le\ell\le2H\), phase \(j\)
owns

\[
 T_{j,\ell}(\pi)
 =U\setminus
 \{w_{j+2H-\ell},\ldots,w_{j+2H-1}\},
 \qquad 1\le j\le L.
\tag{1.3}
\]

This is one literal tail order. No phase clone is assigned independently.

The \(P/P^c\)-shadow of \(\pi\) is the rooted binary word

\[
 \beta(\pi)_i=\mathbf1_{\pi_i\in P}.
\tag{1.4}
\]

The exact mechanical atlas at length \(n\) and weight \(t\) has the word

\[
 b_i^{n,t}
 =\left\lfloor{(i+1)t\over n}\right\rfloor
  -\left\lfloor{it\over n}\right\rfloor.
\tag{1.5}
\]

Let \(\mathcal M\) be the language containing, for every \(n,t\), all
rooted rotations and reversals of (1.5). Let \(d_{\rm ID}\) be binary
insertion--deletion distance. Define

\[
 \mathcal R_D(U)
 =\{\pi:\ d_{\rm ID}(\beta(\pi),\mathcal M)>D\}.
\tag{1.6}
\]

Every member of \(\mathcal R_D(U)\) is nonmechanical, including after
any sequence of at most \(D\) deletions which stays within the safety
budget.

## 2. Exponential density of the reset alphabet

Write

\[
 h_*=-{1\over3}\log{1\over3}-{2\over3}\log{2\over3}>0.
\tag{2.1}
\]

### Lemma 2.1 (edit-ball count)

For a binary word of length \(M\) and weight

\[
 {M\over3}\le t\le {2M\over3},
\tag{2.2}
\]

the proportion of its type class at distance at most \(D\) from
\(\mathcal M\) is at most

\[
 \varepsilon_{M,D}
 \le
 \exp\{-h_*M+O(D\log M+\log M)\}.
\tag{2.3}
\]

In particular, when \(D=O(H)\),

\[
 \varepsilon_{M,D}=e^{-\Omega(m)}.
\tag{2.4}
\]

#### Proof

Only mechanical words of lengths in \([M-D,M+D]\) can lie within
distance \(D\). At a fixed length \(n\), there are at most
\(2n(n+1)\) rooted mechanical words: at most \(n+1\) weights, at most
\(n\) rotations, and a factor two for reversal.

Fix one such word \(z\) of length \(n\). If a length-\(M\) word \(x\)
has insertion--deletion distance at most \(D\) from \(z\), delete
\(a\) positions from \(x\) and \(b\) positions from \(z\), where
\(a+b\le D\), to obtain a common word. For fixed \(a,b\), the number
of possible \(x\)'s is at most

\[
 \binom nb\binom Ma2^a
 \le (2(M+D))^{a+b}.
\tag{2.5}
\]

Summing over \(a,b\), over the \(2D+1\) possible lengths, and over all
mechanical words gives

\[
 \#\{x:d_{\rm ID}(x,\mathcal M)\le D\}
 \le \exp\{O(D\log M+\log M)\}.
\tag{2.6}
\]

On the other hand, uniformly under (2.2), Stirling's formula gives

\[
 \binom Mt\ge \exp\{h_*M-O(\log M)\}.
\tag{2.7}
\]

Division proves (2.3). Finally,

\[
 D\log M=O(H\log m)
 =O(\sqrt m(\log m)^{3/2})=o(m),
\tag{2.8}
\]

which proves (2.4). \(\square\)

For a fixed top type \(t=|U\cap P|\), every binary word of weight
\(t\) has exactly \(t!(M-t)!\) labelled realizations. Lemma 2.1
therefore applies without change to labelled orders.

### Lemma 2.2 (only exponentially few top types are quarantined)

Let

\[
 \mathcal G
 =\left\{U:\ {2M\over5}\le|U\cap P|\le{3M\over5}\right\}.
\tag{2.9}
\]

Then

\[
 \left|\binom{[2m]}M\setminus\mathcal G\right|
 =e^{-\Omega(m)}N_H.
\tag{2.10}
\]

#### Proof

The exact type census is

\[
 \#\{U:|U\cap P|=t\}
 =\binom mt\binom m{M-t}.
\tag{2.11}
\]

Its normalized logarithm is strictly maximized at \(t=M/2\).
Uniform Stirling estimates outside the fixed interval
\([2M/5,3M/5]\) lose a positive constant times \(m\) in the exponent.
Summing the \(O(m)\) types proves (2.10). \(\square\)

The extreme types may genuinely have no radius-\(CH\) nonmechanical
state: when one symbol occurs only \(O(H)\) times, every word can be
within \(O(H)\) edits of its mechanical representative. This is why
the quarantine in (2.10) is real rather than merely technical. Its
total physical mass is nevertheless

\[
 L e^{-\Omega(m)}N_H=e^{-\Omega(m)}W=o(W).
\tag{2.12}
\]

## 3. Exact parent-deletion recursion

### Theorem 3.1 (deletion closure)

Let \(x\) be any label of a state \(\pi\in\mathcal R_D(U)\), and let
\(\pi-x\) denote the induced order on \(U\setminus\{x\}\). Then

\[
 \boxed{\pi\in\mathcal R_D(U)
 \quad\Longrightarrow\quad
 \pi-x\in\mathcal R_{D-1}(U\setminus\{x\}).}
\tag{3.1}
\]

Conversely, if \(\pi\in\mathcal R_D(U)\), insertion of a new labelled
symbol at any position produces a state in \(\mathcal R_{D-1}\).

#### Proof

Insertion or deletion of one labelled coordinate inserts or deletes one
bit from the binary shadow. Hence for every mechanical word \(z\),

\[
 d_{\rm ID}(\beta(\pi-x),z)
 \ge d_{\rm ID}(\beta(\pi),z)-1>D-1.
\tag{3.2}
\]

Taking the minimum over \(z\in\mathcal M\) proves (3.1). The insertion
statement is identical. \(\square\)

Thus a radius-\(D\) state has all of its labelled parent deletions in
the radius-\((D-1)\) alphabet. In a height-stable two-coordinate
suspension, a child top containing exactly one new coordinate deletes
that coordinate and recovers its parent order literally. At a height
increment, two successive deletions consume two units of the safety
budget. Since \(D=\Theta(H)\), the atlas supports a growing
\(\Theta(H)\)-level reset band.

The margin in (2.9) ensures that after any \(D=O(H)=o(M)\) insertions
or deletions, every encountered type still lies in
\([n/3,2n/3]\) at its current length \(n\). Lemma 2.1 therefore gives
the same \(1-e^{-\Omega(m)}\) state density at every level of the
band, not only at its initial level.

After deletion, the first \(2H\) surviving labels are declared to be
the parent core and the rest retain their induced literal order. If the
deleted label was in the tail, the core is unchanged; if it was in the
core, the first old tail label enters the new core. This is precisely a
nonmechanical reset: the order is inherited, but the common-core boundary
is allowed to move.

The theorem removes the previous mechanical empty-neighbourhood cut.
No state in \(\mathcal R_D\) has zero parent degree: it has every one of
its labelled deletions. The price is a decreasing safety index, not a
loss of transition support.

### Theorem 3.2 (projectively coherent reset measure)

Fix a deletion chain

\[
 U_0\supset U_1\supset\cdots\supset U_j,
 \qquad |U_i|=|U_0|-i,\qquad j\le D,
\tag{3.3}
\]

whose types stay in the central range of Lemma 2.1. Choose \(\pi_0\)
uniformly from \(\mathcal R_D(U_0)\), and obtain \(\pi_i\) by literally
deleting the prescribed labels of \(U_0\setminus U_i\). Then:

1. \(\pi_i\in\mathcal R_{D-i}(U_i)\) almost surely;
2. the orders are exactly consistent under parent deletion; and
3. if \(u_i\) is the uniform measure on all orders of \(U_i\), then

   \[
    \|\mathcal L(\pi_i)-u_i\|_{\rm TV}
    \le {\varepsilon_{|U_0|,D}\over1-\varepsilon_{|U_0|,D}}
    =e^{-\Omega(m)}.
   \tag{3.4}
   \]

#### Proof

Item 1 follows by iterating Theorem 3.1, and item 2 is the definition of
the construction. Start instead with a uniform unrestricted order on
\(U_0\). Its restriction to \(U_i\) is uniform on the orders of
\(U_i\). Conditioning the initial order on membership in
\(\mathcal R_D(U_0)\) changes its law in total variation by at most
\(\varepsilon_{|U_0|,D}/(1-\varepsilon_{|U_0|,D})\). Deterministic
deletion cannot increase total variation, proving (3.4). \(\square\)

Thus the construction is not merely a collection of dense alphabets.
It carries an exact parent-consistent probability law through a growing
band. Different deletion histories are deliberately allowed to start
from different top orders; no confluence assertion is made.

### Theorem 3.3 (exact physical front-tail lift)

Let a parent state have ordered core \((q_1,\ldots,q_{2H})\), tail
\(w=(w_1,\ldots,w_s)\), and targets \(T_{j,\ell}\) from (1.3). Insert
a new label \(x\) at the literal front of the tail:

\[
 \pi^+=(q_1,\ldots,q_{2H},x,w_1,\ldots,w_s).
\tag{3.5}
\]

The child has \(L+1\) retained phases. For every parent phase
\(1\le j\le L\) and every \(1\le\ell\le2H\),

\[
 \boxed{
 T^+_{j+1,\ell}=T_{j,\ell}\cup\{x\},\qquad
 T^+_{j+1,\ell}\setminus\{x\}=T_{j,\ell}.}
\tag{3.6}
\]

If the parent lies in \(\mathcal R_D\), the child lies in
\(\mathcal R_{D-1}\).

#### Proof

Write \(w^+=(x,w_1,\ldots,w_s)\). For the child phase \(j+1\), its
deleted interval is

\[
 \{w^+_{j+1+2H-\ell},\ldots,w^+_{j+1+2H-1}\}
 =\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\}.
\tag{3.7}
\]

The child top is the parent top together with \(x\), so complementing
the common deletion interval proves (3.6). The safety statement is the
insertion half of Theorem 3.1. \(\square\)

Thus one may inherit every old phase and every signed trace literally;
only the new first phase is a reset phase. This is the exact chronology
available on a chosen parent edge. Requiring these chosen edges to be
history-independent on every deletion diamond would, however, restore
the confluence obstruction in Section 6.2.

## 4. Conditioning on a physical trace does not destroy density

Fix a top \(U\in\mathcal G\), a deletion length
\(1\le\ell\le2H\), a retained phase, and an \(\ell\)-set
\(I\subset U\). Let \(E(I)\) be the event, for a uniformly random
labelled order, that the labels of \(I\) occupy the prescribed
length-\(\ell\) tail interval. Then

\[
 \Pr(E(I))={1\over\binom M\ell}.
\tag{4.1}
\]

### Lemma 4.1 (trace-conditioned pruning bound)

Uniformly in \(U\in\mathcal G\), the phase, \(\ell\le2H\), and
\(I\),

\[
 \Pr(\pi\notin\mathcal R_D(U)\mid E(I))
 \le \eta_m,
\tag{4.2}
\]

where

\[
 \eta_m
 :=\varepsilon_{M,D}\max_{0\le\ell\le2H}\binom M\ell
 =e^{-\Omega(m)}.
\tag{4.3}
\]

#### Proof

By Lemma 2.1 and (4.1),

\[
 \Pr(\pi\notin\mathcal R_D(U)\mid E(I))
 \le {\varepsilon_{M,D}\over\Pr(E(I))}
 =\varepsilon_{M,D}\binom M\ell.
\tag{4.4}
\]

Moreover,

\[
 \log\binom M\ell
 \le2H\log{eM\over2H}
 =o(m).
\tag{4.5}
\]

Equations (2.3), (2.8), and (4.5) prove (4.3). \(\square\)

It follows that under the uniform distribution on
\(\mathcal R_D(U)\),

\[
 \Pr(E(I)\mid\pi\in\mathcal R_D(U))
 ={1+O(\eta_m)\over\binom M\ell}.
\tag{4.6}
\]

In particular every physical top--phase--target incidence of the full
common-core order catalogue still has a nonmechanical realization. This
is stronger than preservation of the first moment: the support graph on
the central top shore is unchanged.

### Corollary 4.2 (the core may be frozen in advance)

Fix an arbitrary ordered \(2H\)-core \(Q\subset U\). Among the orders
whose first \(2H\) labels are exactly that ordered core, the unsafe
proportion is at most

\[
 \widehat\varepsilon_m
 \le\varepsilon_{M,D}(M)_{2H}=e^{-\Omega(m)}.
\tag{4.7}
\]

After also requiring a prescribed \(\ell\)-set, \(\ell\le2H\), to
occupy a prescribed tail interval, the unsafe conditional proportion is
still \(e^{-\Omega(m)}\).

#### Proof

The event that a uniform order begins with the prescribed ordered core
has probability \(1/(M)_{2H}\). Conditional on it, a prescribed
\(\ell\)-set in the remaining \(s=M-2H\) labels occupies a prescribed
tail interval with probability \(1/\binom s\ell\). Hence the two
successive conditioning costs have logarithm at most

\[
 2H\log M+2H\log{eM\over2H}=o(m).
\tag{4.8}
\]

Apply the same division argument as in Lemma 4.1. \(\square\)

Thus the pruning can be performed after fixing the simultaneous
degree-capped cores of the common-core theorem; it is not necessary to
average over different cores to retain the physical trace support.

## 5. Rankwise near-balance with one common literal order

Use the common-core threshold counts

\[
 b_0=L,
\tag{5.1}
\]

and, for \(1\le q<H\),

\[
 b_q=\min\left\{L-1,
 \max\left\{0,\left\lfloor{N_q\over N_H}\right\rfloor-1\right\}
 \right\}.
\tag{5.2}
\]

Since \((b_q)\) is nonincreasing, put a fixed nested threshold pattern
of these sizes on the \(L\) phases of every literal path. This uses one
tail order for the middle and for both signs at every depth.

For \(-H<r<H\), put \(q=|r|\), \(\ell=H-r\), and

\[
 \Lambda_q={N_q\over N_H},\qquad
 \rho_q={b_qN_H\over N_q}.
\tag{5.3}
\]

At the middle use \(\rho_0=LN_H/W=L/\Lambda\).

### Lemma 5.1 (exact unpruned load)

Under the uniform distribution on all orders at every top, every target
of rank \(m+r\) has load exactly \(\rho_q\).

#### Proof

A fixed active phase in a fixed containing top produces a specified
target with probability \(1/\binom M\ell\). A rank-\((m+r)\) target is
contained in \(\binom{m-r}{H-r}\) critical tops. Therefore its load is

\[
 b_q{\binom{m-r}{H-r}\over\binom M{H-r}}
 =b_q{N_H\over N_q}=\rho_q.
\tag{5.4}
\]

The middle identity is the case \(r=0\). \(\square\)

### Theorem 5.2 (deletion-robust fractional near-resolution)

Give, for every \(U\in\mathcal G\), equal weights summing to one to the
literal states in \(\mathcal R_D(U)\), with the nested tag pattern
above. Give the quarantined tops weight zero. For all sufficiently large
\(m\):

1. every used configuration is one actual common-core promotion path;
2. every signed internal target has total load at most one; and
3. the aggregate unused target capacity over the middle and all signed
   internal ranks is

   \[
      O(H^{3/2}N_H)+e^{-\Omega(m)}HW=o(W).
   \tag{5.5}
   \]

#### Proof

By (4.6), pruning multiplies the contribution of any fixed
top--phase--target incidence by at most \(1+O(\eta_m)\). Removing the
quarantined top shore only decreases load. Lemma 5.1 therefore gives

\[
 \operatorname{load}(Y)
 \le(1+O(\eta_m))\rho_q.
\tag{5.6}
\]

Whenever \(b_q>0\), definition (5.2) implies

\[
 b_q\le\Lambda_q-1.
\tag{5.7}
\]

Since \(\Lambda_q\le\Lambda=O(m)\),

\[
 \rho_q\le1-{1\over\Lambda_q}\le1-{c\over m}
\tag{5.8}
\]

for some fixed \(c>0\). At the middle, (0.2) gives

\[
 \rho_0={L\over\Lambda}
 \le1-c'{H\over m}.
\tag{5.9}
\]

Because \(\eta_m=e^{-\Omega(m)}=o(1/m)\), (5.6)--(5.9) prove the
capacity assertion. If \(b_q=0\), there is no load.

Every nonquarantined top contributes exactly \(b_q\) occurrences at
depth \(q\). Hence its unused capacity is the original common-core
ledger plus at most

\[
 b_q\left(N_H-|\mathcal G|\right)
 \le e^{-\Omega(m)}W
\tag{5.10}
\]

at each rank. The original aggregate ledger is
\(O(H^{3/2}N_H)\). Summing (5.10) over \(O(H)\) signed ranks proves
(5.5). Literal path validity is (1.2)--(1.3). \(\square\)

The same proof applies to every ancestor marginal in Theorem 3.2:
(3.4), followed by conditioning on a trace event of probability
\(1/\binom n\ell\) with \(\ell\le2H\), changes its relative trace load
by only \(e^{-\Omega(m)}\). Hence rankwise near-balance and literal
parent chronology hold simultaneously throughout the reset band.

There is also a fixed-core version which interfaces directly with the
integral degree caps in the common-core atlas. Fix one of its core
assignments \((Q_U)_U\), fix an order on every \(Q_U\), and use only
safe tail orders. Write \(d_r=\binom{s}{H-r}\). Corollary 4.2 gives a
uniform distortion \(1+\widehat\eta_m\), where
\(\widehat\eta_m=e^{-\Omega(m)}\). Give every nonquarantined top total
weight \((1+\widehat\eta_m)^{-1}\). The degree cap

\[
 \deg_r(Y)\le {d_r\over b_{|r|}}
\tag{5.11}
\]

then gives

\[
 \operatorname{load}(Y)
 \le {1\over1+\widehat\eta_m}
      (1+\widehat\eta_m)b_{|r|}{\deg_r(Y)\over d_r}
 \le1.
\tag{5.12}
\]

At the middle use \(d_0/L\). The lost root and trace mass is only
\(e^{-\Omega(m)}W\), so (5.5) is unchanged. Therefore the projective
recursion is available in the fully symmetric ordered atlas, while at
each fixed level its rank-capacity certificate may simultaneously be
frozen inside one literal preassigned common-core system. Compatibility
of independently frozen core assignments across levels is not asserted.

This theorem couples every rank inside each configuration: there is one
ordered state, not a separate clone assignment at each rank. Its
remaining fractional choice is only between whole literal states of the
same top.

## 6. What this recursion does and does not solve

The construction proves that the mechanical deletion obstruction was a
support obstruction of the exact balanced-word subcatalogue. It is not
an obstruction to a deletion-closed common-core order atlas. The reset
alphabet has density \(1-e^{-\Omega(m)}\), all its physical trace cells
survive, and the common-core rank margins dominate the exponentially
small pruning error.

There are two exact limitations.

### 6.1 The safety band is growing but not all-depth

The density proof requires

\[
 D\log m=o(m).
\tag{6.1}
\]

It therefore covers \(D=\Theta(H)\), and more generally every
\(D=o(m/\log m)\). It cannot require a state to remain nonmechanical
under deletion all the way to a one-letter word: the terminal words are
mechanical. A longer induction must renew the safety radius in successive
bands. Renewing it means choosing another whole ordered state, which is
exactly a nonconfluent reset rather than mechanical inheritance.

### 6.2 Integral selection remains the tight-path fusion gate

Theorem 5.2 is a common-history configuration-LP point. It does not prove
that one may choose one of its orders at every top while keeping total
repeat excess \(o(W)\). Convex combinations of literal paths need not
round to one literal path per root.

If one strengthens parent deletion to deletion-path confluence of the
selected orders, all orders are restrictions of ambient cyclic orders.
One ambient order covers at most

\[
 2m\,2^{-H}W
\tag{6.2}
\]

middle owners, and a union of \(K\) hereditary ambient-order profiles
needs

\[
 K\ge(1-o(1)){2^H\over2m}
\tag{6.3}
\]

to cover \(W-o(W)\). Thus a deterministic deletion-confluent section of
the reset atlas is still impossible at small state complexity.

The positive construction and the obstruction fit together cleanly:
the atlas is deletion closed, but the eventual selector must be
nonconfluent and must retain exponentially many deletion histories. The
unresolved theorem is an integral rounding or circulation on those whole
state histories with interval-influence control. It is not another
rankwise Hall inequality and not another mechanical-necklace repair.

## 7. Final theorem-grade statement

### Theorem 7.1 (nonmechanical reset recursion, exact scope)

At calibrated height, for every fixed \(C>0\), the common-core state
space contains a radius-\(CH\), parent-deletion-closed family of
nonmechanical ordered reset states on
\((1-e^{-\Omega(m)})N_H\) critical tops. On each such top the family has
relative density \(1-e^{-\Omega(m)}\). Every state is one literal
promotion path, every physical trace incidence survives, and whole-state
fractional weights give target load at most one at every signed internal
rank with aggregate unused capacity \(o(W)\).

Hence no positive-density empty-neighbourhood obstruction survives after
passing from exact mechanical words to the deletion-robust common-core
reset alphabet. What remains unproved is an integral, nonconfluent choice
of one state per top. Requiring the choice itself to be deletion
confluent restores the ambient-order lower bound (6.2)--(6.3).

## 8. Dependency ledger

This note uses:

- `MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md` for
  the literal common-core path, the counts \(b_q\), the exact fractional
  rank loads, and the \(O(H^{3/2}N_H)\) hole ledger;
- `MATH_AUDIT_MECHANICAL_MULTITYPE_RECURSION_CLONE_HALL_COMPATIBILITY_20260726.md`
  for the exact mechanical deletion empty-neighbourhood cut; and
- `MATH_AUDIT_GLOBAL_RECURSIVE_SCD_TO_PROMOTION_RING_FACTORIZATION_20260726.md`
  for the restriction-confluence and ambient-order coverage bounds.

No fixed-rank matching theorem or unproved integral rounding statement is
used.

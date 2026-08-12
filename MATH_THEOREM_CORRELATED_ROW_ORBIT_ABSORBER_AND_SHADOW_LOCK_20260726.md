# Correlated-row orbit absorption in the Johnson graph

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \rho_q={W\over N_q}.                              \tag{0.1}
\]

The exact row/column gate from the preceding note can be coupled across
all depths without multiplying marginal survival probabilities.

There are three conclusions.

1. For \(H=o(\sqrt m)\), every \(q\le H\) lies in the cap-two regime
   \(1<\rho_q<2\).  Put
   \[
    s_q=W-N_q=(\rho_q-1)N_q.                        \tag{0.2}
   \]
   If a completed cyclic window system has load at most two and at most
   \(s_q\) doubled targets at each sign and depth, then it automatically
   covers every target and has the exact balanced load vector.  Thus the
   global **duplicate-budget invariant** already contains all terminal
   lower quotas.

2. Fix arbitrary doubled-target families
   \(D_q^-\subseteq\binom{[2m]}{m-q}\) and
   \(D_q^+\subseteq\binom{[2m]}{m+q}\), with
   \(|D_q^\pm|\le s_q\).  On the full coordinate orbit of return-free
   endpoint suffixes, the expected total number of forbidden row and
   column incidences is
   \[
    \mathbb E Z
    \le
    2\sum_{q\le H}(m-q+1)(\rho_q-1)
    =\left({2\over3}+o(1)\right)H^3.                \tag{0.3}
   \]
   This is one joint first-moment identity, not a product of marginal
   estimates.  Consequently, if \(H=o(m^{1/3})\), all but \(o(1)\) of
   the orbit shores have \(m-o(m)\) simultaneously admissible rows and
   columns.  More generally, for
   \(H=\alpha m^{1/3}\), an orbit shore exists with at least
   \[
     \left(1-{2\alpha^3\over3}-o(1)\right)m        \tag{0.4}
   \]
   rows and the same number of columns, whenever
   \(2\alpha^3/3<1\).

3. A terminal Hamilton path is missing exactly \(q\) cyclic
   depth-\(q\) windows.  Suppose a switchable seam atlas moves a fixed
   return-free \(2H\)-collar through a coordinate orbit *relative to a
   fixed preload*.  If the internal path has at most \(s_q-q\) doubled
   targets at both signs and depth \(q\), then every target is already
   covered once.  A uniformly orbit-distributed seam meets a doubled
   target with expectation at most
   \[
       2\sum_{q\le H}q(\rho_q-1)
       =\left({1\over2}+o(1)\right){H^4\over m}.    \tag{0.5}
   \]
   Hence for \(H=o(m^{1/4})\), a \(1-o(1)\) fraction of the shores close
   the Hamilton path, avoid every doubled target, and fill every terminal
   quota exactly.  This is a deterministic orbit-absorption lemma.

The relative-orbit hypothesis in item 3 is essential.  Globally relabeling
both the seam and preload changes no collision.  Moreover, a deficient
depth-\(q\) target \(T\) can be locked by saturating its entire lower
shadow at depth \(q+1\).  Thus bulk row slack does not by itself give
targeted terminal absorption.  The exact extra invariant is a fibrewise
shadow-escape condition, stated in Section 6.

The net positive window is therefore

\[
             \boxed{H=o(m^{1/4})}                  \tag{0.6}
\]

for an exact terminal absorber whose shores form a relative coordinate
orbit, while the bulk correlated-row extraction itself works through
\(H=o(m^{1/3})\).

## 1. Cap two and the duplicate-budget invariant

The exact cap ratio is

\[
 \rho_q
 ={(m+q)!(m-q)!\over(m!)^2}
 =\prod_{j=1}^q\left(1+{q\over m-q+j}\right).      \tag{1.1}
\]

Therefore

\[
 0<\log\rho_q
 \le {q^2\over m-q+1}.                             \tag{1.2}
\]

In particular, \(H=o(\sqrt m)\) implies
\(\max_{q\le H}\rho_q=1+o(1)<2\).  The balanced loads are then one and
two, and the required number of doubled targets is (0.2).

For a signed depth-\(q\) load vector \(\ell\in\{0,1,2\}^{N_q}\), write

\[
 z_q=\#\{T:\ell(T)=0\},\qquad
 d_q=\#\{T:\ell(T)=2\}.                            \tag{1.3}
\]

### Lemma 1.1 (duplicate budget forces coverage)

Suppose a completed cyclic system has exactly \(W\) signed
depth-\(q\) occurrences, every target has load at most two, and

\[
                         d_q\le s_q.                \tag{1.4}
\]

Then

\[
                         z_q=0,\qquad d_q=s_q.       \tag{1.5}
\]

Thus every target is covered and its load is one or two.

#### Proof

The total-load identity is

\[
 W=(N_q-z_q-d_q)+2d_q=N_q-z_q+d_q.
\]

Since \(W=N_q+s_q\), this says

\[
                         d_q-z_q=s_q.               \tag{1.6}
\]

Together with \(d_q\le s_q\) and \(z_q\ge0\), equation (1.6) forces
(1.5). \(\square\)

Lemma 1.1 applies separately to lower and upper targets and simultaneously
at every depth.  It replaces all terminal lower-quota constraints by the
single cardinal invariant (1.4), plus the pointwise cap two.  No
distributional assumption is present.

## 2. Uniform return-free endpoint flags

Let \({\cal F}_H\) be the set of oriented return-free suffixes

\[
                         P=(X_{-H+1},\ldots,X_0)    \tag{2.1}
\]

of \(H-1\) Johnson transitions.  Choose \(P\) uniformly from
\({\cal F}_H\).  Equivalently, choose its endpoint \(X_0\) uniformly,
then choose ordered, distinct recent insertion coordinates in \(X_0\)
and ordered, distinct recent removal coordinates outside \(X_0\).

For \(1\le q\le H\), put

\[
 I_{q-1}(P)=\bigcap_{j=0}^{q-1}X_{-j},\qquad
 U_{q-1}(P)=\bigcup_{j=0}^{q-1}X_{-j}.              \tag{2.2}
\]

Coordinate transitivity gives the exact marginal laws

\[
 I_{q-1}(P)\text{ is uniform on }\binom{[2m]}{m-q+1},\qquad
 U_{q-1}(P)\text{ is uniform on }\binom{[2m]}{m+q-1}.           \tag{2.3}
\]

The objects in (2.3) are strongly dependent as \(q\) varies.  We shall
not assert or use independence.

For a family \(D^-\subseteq\binom{[2m]}{m-q}\), define its upper
incidence degree at \(I\in\binom{[2m]}{m-q+1}\) by

\[
 d^-_{D^-}(I)=\#\{T\in D^-:T\subset I\}.            \tag{2.4}
\]

For \(D^+\subseteq\binom{[2m]}{m+q}\), define

\[
 d^+_{D^+}(U)=\#\{T\in D^+:U\subset T\}.           \tag{2.5}
\]

Double counting the inclusion edges gives

\[
\begin{aligned}
 {1\over\binom{2m}{m-q+1}}
 \sum_I d^-_{D^-}(I)
 &= (m-q+1){|D^-|\over N_q},\\
 {1\over\binom{2m}{m+q-1}}
 \sum_U d^+_{D^+}(U)
 &= (m-q+1){|D^+|\over N_q}.                        \tag{2.6}
\end{aligned}
\]

The equality of the two coefficients in (2.6) is useful: the lower and
upper signs have exactly the same endpoint-incidence cost.

## 3. The cubic-window correlated-row theorem

Fix doubled-target families \(D_q^\pm\) satisfying

\[
                         |D_q^\pm|\le s_q.          \tag{3.1}
\]

For a suffix \(P\), let \({\cal R}_q(P)\) be the eligible removal rows
whose new lower depth-\(q\) target belongs to \(D_q^-\), and let
\({\cal C}_q(P)\) be the analogous insertion columns for \(D_q^+\).
The exact exchange-matrix formula is

\[
 N_{\rm cap}(P)
 =\left|A(P)\setminus\bigcup_{q\le H}{\cal R}_q(P)\right|
  \left|B(P)\setminus\bigcup_{q\le H}{\cal C}_q(P)\right|.    \tag{3.2}
\]

Since eligible rows form a subset of the deletions from \(I_{q-1}(P)\),

\[
 |{\cal R}_q(P)|\le d^-_{D_q^-}(I_{q-1}(P)),\qquad
 |{\cal C}_q(P)|\le d^+_{D_q^+}(U_{q-1}(P)).       \tag{3.3}
\]

Define the joint congestion

\[
 Z(P)=\sum_{q\le H}\bigl(|{\cal R}_q(P)|+|{\cal C}_q(P)|\bigr).           \tag{3.4}
\]

### Theorem 3.1 (deterministic orbit slack)

For arbitrary families satisfying (3.1),

\[
 \mathbb E_{P\in{\cal F}_H} Z(P)
 \le 2\sum_{q\le H}(m-q+1)(\rho_q-1).              \tag{3.5}
\]

Consequently, for every \(\eta>0\), the proportion of suffixes with

\[
 \left|\bigcup_{q\le H}{\cal R}_q(P)\right|>\eta m
 \quad\hbox{or}\quad
 \left|\bigcup_{q\le H}{\cal C}_q(P)\right|>\eta m             \tag{3.6}
\]

is at most

\[
 {2\sum_{q\le H}(m-q+1)(\rho_q-1)\over\eta m}.    \tag{3.7}
\]

In particular, if \(H=o(m^{1/3})\), all but \(o(1)\) of the coordinate
orbit satisfies, for every fixed \(\eta>0\),

\[
\begin{aligned}
 \left|A(P)\setminus\bigcup_q{\cal R}_q(P)\right|
 &\ge (1-\eta)m-H+1,\\
 \left|B(P)\setminus\bigcup_q{\cal C}_q(P)\right|
 &\ge (1-\eta)m-H+1.                               \tag{3.8}
\end{aligned}
\]

In fact one may take any \(\eta=\eta(m)\to0\) with
\(H^3/(\eta m)\to0\).  Then a \(1-o(1)\) fraction of the shores has
\(m-o(m)\) available rows, \(m-o(m)\) available columns, and therefore
\(m^2-o(m^2)\) cap-admissible exchanges by (3.2).

#### Proof

Take expectations in (3.3), use (2.3) and (2.6), and then use
\(|D_q^\pm|/N_q\le s_q/N_q=\rho_q-1\).  Summing the resulting two exact
one-sign estimates proves (3.5).

Each union in (3.6) is at most \(Z(P)\).  Hence (3.6) implies
\(Z(P)>\eta m\), and Markov's inequality proves (3.7).  Finally,
\(|A(P)|,|B(P)|\ge m-H+1\), which gives (3.8). \(\square\)

This proof sums correlated incidences on the same suffix.  In particular,
it never replaces a joint survival probability by a product of marginal
survival probabilities.

### Corollary 3.2 (sharp polynomial scale from this moment)

Uniformly for \(H=o(\sqrt m)\),

\[
 \rho_q-1
 \le \exp\left({q^2\over m-q+1}\right)-1.          \tag{3.9}
\]

Therefore, if \(H=o(m^{1/3})\),

\[
 2\sum_{q\le H}(m-q+1)(\rho_q-1)
 =2\sum_{q\le H}q^2(1+o(1))
 =\left({2\over3}+o(1)\right)H^3.                 \tag{3.10}
\]

If \(H=\alpha m^{1/3}\), the same calculation, with an \(o(m)\)
remainder, gives an orbit shore with both available row and column counts
at least (0.4).

#### Proof

Inequality (3.9) is (1.2).  In the stated range its exponent is uniformly
\(o(1)\), so

\[
 (m-q+1)(\rho_q-1)=q^2(1+o(1)).
\]

Sum over \(q\le H\).  Since some suffix has \(Z(P)\le\mathbb EZ\),
(3.2) yields the last assertion. \(\square\)

The exponent \(1/3\) is the threshold of this exact first incidence
moment: depth \(q\) costs \(\Theta(q^2)\) blocked row-plus-column
incidences on average, and \(\sum_{q\le H}q^2=\Theta(H^3)\).

## 4. Exact terminal seam bookkeeping

Let

\[
                         P=(X_0,\ldots,X_{W-1})     \tag{4.1}
\]

be a Hamilton path.  At depth \(q\), its internal linear windows have
starts \(0,\ldots,W-q-1\), so their number is exactly \(W-q\).  Closing
the edge \(X_{W-1}X_0\) creates the remaining \(q\) cyclic windows.  In
this section every internal window through depth \(H\) is assumed
return-free.

For the internal signed depth-\(q\) load vector, again let \(z_q\) and
\(d_q\) be the numbers of zero and double loads.

### Lemma 4.1 (the seam deficit identity)

If every internal load is at most two and

\[
                         d_q\le s_q-q,              \tag{4.2}
\]

then

\[
                         z_q=0,\qquad d_q=s_q-q.     \tag{4.3}

Thus all targets are already covered once, and the closing seam has to
turn exactly \(q\) distinct single loads into double loads.

#### Proof

Now the total-load identity is

\[
 W-q=N_q-z_q+d_q=N_q+s_q-q.
\]

Hence \(d_q-z_q=s_q-q\), and (4.2) forces (4.3). \(\square\)

The lemma applies independently to both signs.  It is the exact reason a
collision-free seam fills, rather than merely avoids exceeding, every
terminal quota.

### Lemma 4.2 (distinct crossing targets)

Suppose the \(2H\) transitions surrounding the proposed closing edge are
return-free.  For each \(q\le H\), the \(q\) new crossing lower targets
are pairwise distinct, and the \(q\) new crossing upper targets are
pairwise distinct.

#### Proof

Compare two consecutive length-\(q\) crossing windows.  Shifting the
window one transition forward inserts into its intersection the coordinate
inserted at the old left boundary and deletes from its intersection the
coordinate removed at the new right boundary.  Return-freeness makes
these coordinates distinct and makes every such coordinate new throughout
the \(2H\)-collar.  After any positive number of shifts, the set of gained
coordinates is disjoint from the set of lost coordinates, so the lower
targets cannot repeat.  The union statement is the dual argument. \(\square\)

## 5. A relative-orbit terminal absorber

Fix the internal preload of a Hamilton path and its doubled-target
families \(D_q^\pm\).  A **relative coordinate-orbit seam atlas** is a
family of switchable shores indexed uniformly by
\(\pi\in\operatorname{Sym}([2m])\) such that:

1. the internal preload, and hence every \(D_q^\pm\), is fixed;
2. the \(2H\)-collar target list on shore \(\pi\) is the image under
   \(\pi\) of one fixed return-free collar target list; and
3. all internal signed window loads are identical across shores; and
4. every shore closes the same spanning Hamilton path or an equivalent
   spanning path shore.

Only item 2 is used in the collision calculation; items 1, 3, and 4 are
the physical absorber requirements.

### Theorem 5.1 (exact orbit-seam absorption)

Assume the internal path satisfies, for both signs and every \(q\le H\),

\[
                  \ell_q^\pm(T)\le2,\qquad
                  |D_q^\pm|\le s_q-q.              \tag{5.1}
\]

For a uniformly chosen shore of a relative coordinate-orbit seam atlas,
let \(C\) be the number of new crossing targets which belong to the
corresponding doubled family.  Then

\[
 \mathbb EC
 \le 2\sum_{q\le H}q\,{s_q\over N_q}
 =2\sum_{q\le H}q(\rho_q-1).                       \tag{5.2}
\]

If the right side of (5.2) is less than one, the atlas contains a shore
which closes the path and gives the exact balanced target loads at every
depth and both signs.

For \(H=o(m^{1/4})\), a \(1-o(1)\) fraction of all shores work.  More
precisely,

\[
 2\sum_{q\le H}q(\rho_q-1)
 =\left({1\over2}+o(1)\right){H^4\over m}.          \tag{5.3}
\]

Thus the same conclusion holds for
\(H=\alpha m^{1/4}\) whenever \(\alpha^4<2\), for all sufficiently large
\(m\).

#### Proof

Under a uniform relative permutation, each individual lower crossing
target is uniform on \(\binom{[2m]}{m-q}\), and each individual upper
crossing target is uniform on \(\binom{[2m]}{m+q}\).  There are \(q\) of
each sign.  Linearity of expectation therefore gives

\[
 \mathbb EC
 =\sum_{q\le H}q\left({|D_q^-|\over N_q}
                         +{|D_q^+|\over N_q}\right),
\]

which implies (5.2).  No independence between targets is asserted.

If \(\mathbb EC<1\), some integral value of \(C\) is zero.  Lemma 4.2
says that at depth \(q\) the seam adds \(q\) distinct targets of each
sign.  Lemma 4.1 says every one of them currently has load one.  Hence
the seam raises exactly \(q\) single loads to double loads and produces
the exact terminal balance.

Finally, (3.9) gives \(\rho_q-1=(1+o(1))q^2/m\) uniformly in the stated
range, and

\[
 {2\over m}\sum_{q\le H}q^3
 =\left({1\over2}+o(1)\right){H^4\over m}.
\]

Markov's inequality gives the claimed proportion of successful shores.
\(\square\)

Theorem 5.1 is an absorption statement rather than a near-coverage
statement: its hypotheses and the no-collision conclusion force all
terminal lower quotas exactly.

The word **relative** cannot be dropped.  If a global permutation moves
both \(D_q^\pm\) and the seam target list, every collision is preserved.
The theorem requires a physical switch which moves the collar against a
common fixed preload.

## 6. A sharp higher-window target lock

The orbit-average theorem does not imply that a specified missing target
has a usable occurrence.  The obstruction is already literal between two
adjacent depths.

For a lower target \(T\in\binom{[2m]}{m-q}\), write

\[
 \partial T=\{T-x:x\in T\}
 \subseteq\binom{[2m]}{m-q-1}.                     \tag{6.1}
\]

For an upper target \(U\in\binom{[2m]}{m+q}\), write

\[
 \nabla U=\{U+x:x\notin U\}
 \subseteq\binom{[2m]}{m+q+1}.                     \tag{6.2}
\]

### Proposition 6.1 (adjacent-depth locking)

Let a return-free depth-\(q\) window with lower target \(T\) be the
terminal subwindow of a return-free depth-\(q+1\) window.  Then the latter
lower target is \(T-x\) for some \(x\in T\).  Dually, if its upper target
is \(U\), the enclosing upper target is \(U+y\) for some \(y\notin U\).

Consequently:

\[
 \partial T\subseteq D_{q+1}^-
 \quad\Longrightarrow\quad
 \text{no appended occurrence of }T\text{ is cap-feasible},              \tag{6.3}
\]

and the upper analogue holds with \(\nabla U\subseteq D_{q+1}^+\).

#### Proof

Write the enclosing window as \((Y_0,Y_1,\ldots,Y_{q+1})\), and let the
first transition remove \(y\) and insert \(x\).  Return-freeness implies
that \(x\) remains present throughout \(Y_1,\ldots,Y_{q+1}\), so
\(x\in T\), but \(x\notin Y_0\).  Hence

\[
 \bigcap_{i=0}^{q+1}Y_i=T-x.
\]

Likewise \(y\notin U=\bigcup_{i=1}^{q+1}Y_i\) and
\(\bigcup_{i=0}^{q+1}Y_i=U+y\).  If every possible enclosing target is
already doubled, the new depth-\(q+1\) window exceeds cap two. \(\square\)

For example, let \(R\) be an uncovered lower depth-one target of size
\(m-1\).  Saturating only

\[
                         D_2^-\supseteq\{R-x:x\in R\}             \tag{6.4}
\]

uses \(m-1\) depth-two doubled targets and blocks every appended
occurrence of \(R\).  This is negligible compared with the allowed
budget

\[
 s_2=(\rho_2-1)N_2={4m+2\over m(m-1)}N_2.          \tag{6.5}
\]

Thus neither the duplicate-budget cardinality nor the bulk orbit estimate
prevents a specified deficit from being locked.

The example is a statewise obstruction.  It does not assert that every
such state is produced by a particular canonical Hamilton-prefix
construction.

## 7. The exact shadow-escape invariant

Proposition 6.1 identifies the missing correlated condition.  For a
lower target \(T\) at depth \(q<H\), define

\[
 e_q^-(T)=\#\{x\in T:T-x\notin D_{q+1}^-\}.         \tag{7.1}
\]

For an upper target \(U\), define

\[
 e_q^+(U)=\#\{y\notin U:U+y\notin D_{q+1}^+\}.     \tag{7.2}
\]

A robust terminal absorber must maintain, on every still-demanded target
fibre,

\[
 e_q^-(T),e_q^+(U)\ge\kappa(m-q)                  \tag{7.3}
\]

for some fixed \(\kappa>0\), or an equivalent multilevel Hall condition.
This is fibrewise and cannot be inferred from \(|D_{q+1}^\pm|/N_{q+1}\).

Iterating (7.3) gives a genuine, proved branching estimate.  If every
node reached from a demanded lower/upper flag \(T\subset U\),
\(|U\setminus T|=2q\), satisfies (7.3), then the number of pairs of
unsaturated enclosing chains from depth \(q\) through depth \(H\) is at
least

\[
 \boxed{
 \kappa^{,2(H-q)}
 \left((m-q)_{\underline{H-q}}\right)^2.}          \tag{7.4}
\]

Indeed, at level \(r\) the lower chain has at least
\(\kappa(m-r)\) choices of the next deleted element, and the upper chain
has the same number of choices of the next added element.  These choices
are independent because the former lie inside the current lower set and
the latter outside the current upper set.  Multiplying is legitimate here
because (7.3) is a conditional lower bound in every individual fibre, not
a marginal-density assertion.

Estimate (7.4) certifies the nested enclosing windows only.  A complete
physical collar must additionally certify all shorter windows lying
strictly inside the added collar.  The exchange-matrix slack theorem gives
many such generic collars in the bulk, but Proposition 6.1 shows that a
targeted collar needs the fibrewise condition (7.3).

## 8. Exact remaining construction task

The unrestricted Johnson approach now has a precise two-part absorber
target.

1. **Bulk shore supply.**  Build switchable shores whose endpoint flags
   contain a depth-balanced coordinate orbit.  Theorem 3.1 then gives
   simultaneous row/column slack through \(H=o(m^{1/3})\), against every
   admissible correlated doubled-target profile.

2. **Relative terminal motion.**  Move a return-free \(2H\)-seam collar
   relative to a common preload.  Theorem 5.1 then closes all quotas
   exactly through \(H=o(m^{1/4})\).

If the construction instead absorbs specified missing targets one at a
time, it must establish the shadow-escape condition (7.3) throughout the
relevant descendant fibres.  The cardinal duplicate budget alone cannot
do this.

Thus the higher-window obstruction does not destroy the unrestricted
lane, but it changes the required object.  A global symmetric relabeling
is useless; a relative-orbit seam switch, or a fibrewise shadow-expanding
atlas, is the exact missing physical theorem.

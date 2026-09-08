# AD29: actual residual chains and horizontal rotor expansion after one bite

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Exact conclusion

Put

\[
 W=\binom{2m}{m},\qquad
 R_q=\binom{2m}{m-q}=\binom{2m}{m+q},
 \qquad 0\le q\le Q,
\]

and assume

\[
 1\le Q<H<m,\qquad Q=o(H),\qquad H=o(m).
\]

At the calibrated top crossing write

\[
 M=m+H,\qquad N=\binom{2m}{M},\qquad
 \rho=\frac{MN}{W}=1-o(1).
\]

Let one rigorous owner-scale bite use $k=O(N/M)$ trajectories and let
$w^{\rm bite}$ be its already compiled literal word.  Write

\[
 L_{\rm bite}=|w^{\rm bite}|=kM+r_{\rm init},
 \qquad r_{\rm init}\le (2Q+1)k,
\]

and let $F_{\rm lit}$ be the set of all distinct middle masks physically
exposed by the word, including masks exposed unintentionally by reset or
seam intervals.  Put

\[
 f=|F_{\rm lit}|.
\]

Then

\[
 kM\le f\le L_{\rm bite}=O(N)=O(W/M).
\tag{0.1}
\]

The exact results are as follows.

1. If ${\cal L}$ is the physical literal hole family in ranks
   $m-Q,\ldots,m+Q$, then

   \[
   \boxed{
   W-f\le \operatorname{width}({\cal L})
   \le \left\lfloor W-\frac{f}{m+1}\right\rfloor.}
   \tag{0.2}
   \]

   Thus the actual residual width is $W-o(W)$, not a small donor width.

2. Fix any Boolean symmetric chain decomposition.  After removing at
   most

   \[
   \boxed{2Qf=O(QN)=o(W)}
   \tag{0.3}
   \]

   exceptional literal holes, the remaining physical holes have width
   and minimum chain-cover number exactly

   \[
   \boxed{W-f.}
   \tag{0.4}
   \]

   The exceptions themselves have a direct literal repair of length at
   most

   \[
   \boxed{(2Q+1)f=o(W).}
   \tag{0.5}
   \]

   Hence the actual vertical chain gate is closed, with exact integrality.

3. The actual adjacent- and two-step-shadow Hall deficiencies are also
   $o(W)$.  The physical-support bound is

   \[
   E_1\le 2Q L_{\rm bite}=O(QN)=o(W),\qquad
   E_2\le 2(Q-1)L_{\rm bite}=O(QN)=o(W).
   \tag{0.6}
   \]

   For the certified catalogue claims, the sharper bound is

   \[
   \boxed{E_1,E_2
   \le \frac{2k}{N}\sum_{q=1}^Q R_q
   \le (C\sqrt\pi+o(1))\frac{W}{\sqrt m}}
   \tag{0.7}
   \]

   whenever $k/N\le C/m$.

4. Two saturated band columns $C,C'$ are consecutive in one literal
   rotor trajectory if and only if one common arrival $y$ satisfies

   \[
   \boxed{
   C'_{-Q}=C_{-Q}-x+y,\qquad
   C'_d=C_{d-1}+y\quad(-Q<d\le Q).}
   \tag{0.8}
   \]

   This is the exact horizontal cone identity.  Separate-rank Hall does
   not imply it.  Moreover, every arbitrary rotor window of at most
   $Q+1$ transitions has middle owners satisfying
   $d_J(X_s,X_t)=|s-t|$; short blocks are necessarily monotone Johnson
   geodesics even without assuming the canonical grid template.

5. On the complete global state reservoir, deleting $b$ states causes
   successor-matching deficiency at most $b$.  The rotor graph has
   directed girth at least $2Q+2$.  Hence the good states $G$ have a
   literal path cover with at most

   \[
   \boxed{
   \frac{|G|}{2Q+2}
   +\left(1-\frac1{2Q+2}\right)b}
   \tag{0.9}
   \]

   paths, and a cover by blocks of at most $2Q+2$ states with fewer
   than

   \[
   \boxed{b+\frac{|G|}{Q+1}+1}
   \tag{0.10}
   \]

   blocks.  For deletion by the actual used owner set,
   $b/|\mathscr S_Q|=f/W=O(1/m)=o(1/Q)$, so this is an integral literal
   $O(Q)$-phase block theorem on the complete residual-owner reservoir.

6. There is a stronger integral long-run multicover.  Ordering the two
   unordered blocks lifts every quotient state to a permutation of
   ([2m]); cyclic right shift is exactly one rotor update.  The
   permutation orbits are literal cycles of length (2m).  After deleting
   all occurrences with owner in $F_{\rm lit}$, the remaining occurrence
   multicover has path density at most

   \[
   \boxed{\frac1{2m}+\frac fW=O(1/m)=o(1/Q).}
   \tag{0.11}
   \]

   Thus horizontal expansion is excellent integrally at full
   multiplicity.

The missing step is not width, shadow expansion, rotor regularity, or
literalization.  It is the following integral thinning:

> Choose one saturated extension for each of the $W-f$ retained SCD
> chains while retaining a rotor path cover with $p=o(W/Q)$.

The complete reservoir and the permutation lift use enormous
multiplicity.  Dividing by that multiplicity is only a fractional answer.
The exact grid formulas below show the local obstruction: consecutive
same-rank prescribed masks must be Johnson-adjacent, and a grid run forces
its middle owners to form a monotone Johnson geodesic with common
opposite-edge labels at every occupied rectangle.

Consequently no coefficient-one theorem is claimed.  The precise proved
boundary is the positive full-reservoir expansion together with the
unresolved one-copy-per-chain desymmetrization.

## 1. One endpoint exposes at most one mask of each rank

### Lemma 1.1 (endpoint-chain lemma)

Let $w=(w_1,\ldots,w_L)$ be any literal OR word.  For a fixed right
endpoint (t), the masks

\[
 \bigvee_{j=s}^t w_j,\qquad 1\le s\le t,
\]

form an inclusion chain as (s) decreases.  Therefore at most one
distinct interval ending at (t) has any prescribed cardinality.
Consequently a word of length $L$ exposes at most $L$ distinct masks
of each fixed rank.

#### Proof

If $s'<s\le t$, then $[s,t]\subseteq[s',t]$, so

\[
 \bigvee_{j=s}^t w_j
 \subseteq
 \bigvee_{j=s'}^t w_j.
\]

Comparable finite sets of equal cardinality are equal.  Assign every
interval to its right endpoint and sum over the $L$ endpoints.
\(\square\)

The $kM$ selected trajectory phases expose $kM$ distinct owners, so
$f\ge kM$.  Lemma 1.1 gives $f\le L_{\rm bite}$, proving (0.1).  The
same lemma controls complete physical support in every nonmiddle row; no
assumption that only designated intervals exist is being made.

## 2. Exact physical width and SCD condensation

Let

\[
 {\cal B}_r=\binom{[2m]}{m+r},\qquad -Q\le r\le Q,
\]

let ${\cal C}_r\subseteq{\cal B}_r$ be the complete distinct physical
support of $w^{\rm bite}$, and put

\[
 {\cal L}_r={\cal B}_r\setminus{\cal C}_r,\qquad
 {\cal L}=\bigcup_{r=-Q}^Q{\cal L}_r.
\]

Thus ${\cal L}$ is the literal hole family, not a family of withheld or
duplicate claims.  We have $|{\cal L}_0|=W-f$.

### Theorem 2.1 (actual-hole width sandwich)

For $Q\ge1$,

\[
 W-f\le \operatorname{width}({\cal L})
 \le \left\lfloor W-\frac{f}{m+1}\right\rfloor.
\tag{2.1}
\]

#### Proof

The $W-f$ middle holes form an antichain, giving the lower bound.

Let ${\cal A}\subseteq{\cal L}$ be any antichain and write

\[
 a_0=|{\cal A}\cap{\cal B}_0|,\qquad
 a_*=|{\cal A}|-a_0.
\]

The LYM inequality gives

\[
 \frac{a_0}{W}
 +\sum_{r\ne0}\frac{|{\cal A}\cap{\cal B}_r|}{|{\cal B}_r|}
 \le1.
\]

Every off-middle row in the controlled band has size at most

\[
 R_1=\binom{2m}{m-1}=\frac{m}{m+1}W.
\]

Hence

\[
 \frac{a_0}{W}+\frac{a_*}{R_1}\le1,
\]

and therefore

\[
 |{\cal A}|
 \le R_1+\left(1-\frac{R_1}{W}\right)a_0.
\]

The right side increases with $a_0$, while $a_0\le W-f$.  Substitution
of $R_1/W=m/(m+1)$ gives

\[
 |{\cal A}|\le W-\frac{f}{m+1}.
\]

Take the integer floor. \(\square\)

### Theorem 2.2 (optimal physical SCD condensation)

Fix any symmetric chain decomposition $\mathscr D$ of $2^{[2m]}$.
There is $E_{\rm lit}\subseteq{\cal L}$ such that

\[
 |E_{\rm lit}|\le2Qf
\tag{2.2}
\]

and

\[
 \operatorname{width}({\cal L}\setminus E_{\rm lit})
 =\operatorname{cc}({\cal L}\setminus E_{\rm lit})
 =W-f,
\tag{2.3}
\]

where $\operatorname{cc}$ denotes the minimum number of inclusion chains
in a chain cover.

#### Proof

Every symmetric chain has exactly one middle member, so $\mathscr D$
has exactly $W$ chains.  Delete the $f$ SCD chains whose middle members
belong to $F_{\rm lit}$, and let $E_{\rm lit}$ be the literal holes in
the controlled band which lie on deleted chains.

The middle member of every deleted chain is physically covered and is not
a hole.  A chain has at most one member in each of the other $2Q$
controlled ranks.  Thus $|E_{\rm lit}|\le2Qf$.

Every hole outside $E_{\rm lit}$ lies on one of the $W-f$ retained
SCD chains.  Conversely, the middle members of all retained chains are
the $W-f$ middle holes, which form an antichain.  Hence both the width
and the minimum chain-cover number equal $W-f$. \(\square\)

At owner scale, (0.1) and $MN=(1-o(1))W$ give

\[
 2Qf=O(QN)=O(WQ/M)=o(W).
\tag{2.4}
\]

### Corollary 2.3 (the exceptional chains are literally cheap)

The exceptional family $E_{\rm lit}$ has a direct literal cover of
length at most

\[
 (2Q+1)f=o(W).
\tag{2.5}
\]

#### Proof

For each deleted SCD chain, extend its controlled portion to a saturated
band chain

\[
 L\subset L+z_1\subset\cdots\subset L+z_1+\cdots+z_{2Q}.
\]

The word block

\[
 \{z_{2Q}\},\{z_{2Q-1}\},\ldots,\{z_1\},L
\tag{2.6}
\]

has length $2Q+1$, and its suffix ORs are exactly the displayed band
chain.  Concatenate one such block for each deleted SCD chain.  Cross-block
intervals may expose extra masks but do not destroy any required witness.
Use (2.4). \(\square\)

Thus neither the huge raw width nor the deleted-priority donor strings are
the correct vertical obstruction.  Up to $o(W)$ literal work, the actual
holes are exactly one chain per unused physical middle owner.

## 3. Actual adjacent- and two-step-shadow loss

For $q\ge1$, let $\varepsilon_{q,1}^-$ be the Hall deficiency from
${\cal L}_{-q}$ into ${\cal L}_{-(q-1)}$ in the inclusion graph, and
define $\varepsilon_{q,1}^+$ dually above the middle.  For $q\ge2$,
define $\varepsilon_{q,2}^{\pm}$ using two-step inclusion toward the
middle.  Put

\[
 E_1=\sum_{q=1}^Q
 (\varepsilon_{q,1}^-+\varepsilon_{q,1}^+),
 \qquad
 E_2=\sum_{q=2}^Q
 (\varepsilon_{q,2}^-+\varepsilon_{q,2}^+).
\]

### Lemma 3.1 (target deletion in a normalized matching graph)

Let $V\to V'$ be a normalized-matching bipartite graph with
$|V'|/|V|=\alpha>1$.  After deleting $u$ vertices from $V'$, the
Hall deficiency from any surviving subfamily of (V) into the surviving
target row is at most

\[
 \left\lfloor\frac u\alpha\right\rfloor.
\tag{3.1}
\]

#### Proof

A source family of size $a$ has at least $\lceil\alpha a\rceil$
neighbors before deletion and at least
$\max(0,\lceil\alpha a\rceil-u)$ afterward.  If $\alpha a\le u$, its
deficiency is at most $a\le u/\alpha$.  If $\alpha a>u$, its
deficiency is at most

\[
 a-(\alpha a-u)=u-(\alpha-1)a\le u/\alpha.
\]

The deficiency is integral. \(\square\)

### Theorem 3.2 (physical shadow bounds)

Write $c_r=|{\cal C}_r|$.  Then

\[
 \varepsilon_{q,1}^-\le
 \left\lfloor c_{-(q-1)}\frac{R_q}{R_{q-1}}\right\rfloor,
 \qquad
 \varepsilon_{q,1}^+\le
 \left\lfloor c_{q-1}\frac{R_q}{R_{q-1}}\right\rfloor,
\tag{3.2}
\]

and

\[
 \varepsilon_{q,2}^-\le
 \left\lfloor c_{-(q-2)}\frac{R_q}{R_{q-2}}\right\rfloor,
 \qquad
 \varepsilon_{q,2}^+\le
 \left\lfloor c_{q-2}\frac{R_q}{R_{q-2}}\right\rfloor.
\tag{3.3}
\]

In particular,

\[
 E_1\le2Q L_{\rm bite},\qquad
 E_2\le2(Q-1)L_{\rm bite}.
\tag{3.4}
\]

#### Proof

The full inclusion graph from rank $m-q$ to rank $m-q+1$ has
normalized expansion ratio $R_{q-1}/R_q$.  Apply Lemma 3.1 after
deleting the $c_{-(q-1)}$ physically covered targets in the latter row.
Complementation proves the upper formula.  The same argument in the
two-step inclusion graph gives (3.3).

By Lemma 1.1, $c_r\le L_{\rm bite}$ for every row.  Since every displayed
binomial ratio is at most one, summing proves (3.4). \(\square\)

Since $L_{\rm bite}=O(N)$ and $QN=o(W)$, (3.4) is $o(W)$.

For comparison, suppose one uses only the certified catalogue claims:

\[
 c_0=kM,\qquad c_{-q}=c_q=k\bar c_q,\qquad
 \bar c_q\le\frac{R_q}{N}.
\tag{3.5}
\]

The calibration $M\le W/N$ handles the $q=1$ target row, and (3.2)
gives

\[
 E_1\le\frac{2k}{N}\sum_{q=1}^Q R_q.
\tag{3.6}
\]

The same proof gives (3.6) for $E_2$, with a possibly shorter sum.  The
exact central ratio obeys

\[
 \frac{R_q}{W}
 =\prod_{i=1}^q\frac{m-i+1}{m+i}
 \le \exp\left(-\frac{q^2}{m+Q}\right).
\tag{3.7}
\]

Indeed, apply $\log(1-x)\le-x$ and use
$\sum_{i=1}^q(2i-1)=q^2$.  Therefore

\[
 \sum_{q=1}^Q R_q
 \le W\sum_{q\ge1}e^{-q^2/(m+Q)}
 \le \frac{\sqrt\pi}{2}W\sqrt{m+Q}.
\tag{3.8}
\]

If $k/N\le C/m$, (0.7) follows.

Matching consecutive rows toward the middle yields a chain cover with at
most

\[
 |{\cal L}_0|+E_1=W-f+E_1
\tag{3.9}
\]

components.  This is a genuine actual-hole statement, but Theorem 2.2 is
stronger after its explicit $o(W)$ exception set.

## 4. Low-run priority inside one selected grid

The priority schedule itself has favorable horizontal geometry, although
this geometry concerns claims on the selected grid and is not a
donor-to-global-hole transport theorem.

### Proposition 4.1 (deadline order with few cyclic runs)

Fix one cyclically ordered trajectory.  Suppose $B$ phases have a finite
first-block depth and the deadline inequalities $B_q\le d_q$ hold.
There is a legal priority assignment such that, for every depth $q$,
both the claimed phase set and its complement have at most

\[
 \boxed{2B+1}
\tag{4.1}
\]

cyclic runs.

#### Proof

Use deadline Hall to place the $B$ blocked phases injectively in legal
slots.  Fill all remaining slots, in increasing slot order, by the
unblocked phases in their physical cyclic order.

For a fixed $q$, the unblocked phases in the first $d_q$ slots form an
initial segment of the cyclic order after deletion of the $B$ blocked
points.  In the original cycle this is one cyclic interval with at most
$B$ points deleted, hence at most $B+1$ runs.  The blocked phases in
the prefix add at most $B$ singleton runs.  The prefix and its cyclic
complement have the same boundary pairs, so both have at most $2B+1$
runs. \(\square\)

Across the rigorous bite, the audited blocked-phase ledger is
$o(W/Q)$.  Proposition 4.1 therefore gives a low-run description of the
physically selected grid cells.  It does not identify their unclaimed
cells with the global holes: another trajectory can hit the same mask,
and a missing distinct claim can lie elsewhere.

## 5. Exact rotor cone and grid-strip criterion

Put $\ell=m-Q$.  A global radius-$Q$ state is

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=|R|=\ell,
\]

where the displayed blocks partition $[2m]$.  Its signed flag column is

\[
 C_d(\omega)=L\cup\{z_1,\ldots,z_{Q+d}\},
 \qquad -Q\le d\le Q.
\tag{5.1}
\]

For a fixed $M$-carrier $U$, replace $R$ by a tail $R_U$ of size
$H-Q$, and require every arrival to lie in $R_U$.

### Theorem 5.1 (common-arrival cone identity)

Let $x\in L$ and $y\in R$.  The rotor update

\[
 (L;z_1,\ldots,z_{2Q};R)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q})
\tag{5.2}
\]

satisfies

\[
 C'_{-Q}=C_{-Q}-x+y,
\tag{5.3}
\]

and

\[
 \boxed{C'_d=C_{d-1}+y\qquad(-Q<d\le Q).}
\tag{5.4}
\]

Conversely, two saturated band columns satisfying (5.3)--(5.4) for
$x\in C_{-Q}$ and $y\notin C_Q$ are consecutive global rotor states.
They are consecutive inside one fixed $M$-carrier whenever a common
$M$-set containing $C_Q\cup\{y\}$ is specified.

#### Proof

The new bottom is $L-x+y$.  For $d>-Q$,

\[
\begin{aligned}
 C'_d
 &=(L-x+y)\cup\{x,z_1,\ldots,z_{Q+d-1}\}\\
 &=L\cup\{z_1,\ldots,z_{Q+d-1}\}\cup\{y\}\\
 &=C_{d-1}+y.
\end{aligned}
\]

For the converse, recover the ordered collar from the successive singleton
differences in the first column.  Equations (5.3)--(5.4) say that update
(5.2) has exactly the second column.  In the fixed-top case, complete
$C_Q\cup\{y\}$ to an $M$-set; this is possible because $H>Q$.
\(\square\)

Thus a list of residual inclusion chains can occupy successive state
columns in one literal block if and only if it has saturated extensions
satisfying the same common-arrival cone identities successively.  This is
an exact necessary-and-sufficient horizontal condition, not a rankwise
projection.

### Grid form

For a two-chain grid write

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
   \cup\{b_1,\ldots,b_j\}.
\tag{5.5}
\]

At phase (t), every signed flag has the unified expression

\[
 \boxed{F_d(t)=G_{t-d,t}.}
\tag{5.6}
\]

The canonical transition uses

\[
 x_t=a_{t+Q+1},\qquad y_t=b_{t+1},
\]

and gives

\[
 F_d(t+1)=F_{d-1}(t)+b_{t+1}.
\tag{5.7}
\]

The middle owners are

\[
 X_t=G_{t,t}
 =C\cup\{a_{t+1},\ldots,a_g\}
   \cup\{b_1,\ldots,b_t\},
\]

so

\[
 X_{t+1}=X_t-a_{t+1}+b_{t+1},
 \qquad
 \boxed{d_J(X_s,X_t)=|s-t|.}
\tag{5.8}
\]

Moreover,

\[
 G_{i,j+1}\setminus G_{i,j}=\{b_{j+1}\}
 \quad\text{independently of }i,
\tag{5.9}
\]

and

\[
 G_{i-1,j}\setminus G_{i,j}=\{a_i\}
 \quad\text{independently of }j.
\tag{5.10}
\]

These are the equal-opposite-edge constraints on every Boolean rectangle.

### Proposition 5.2 (sharp same-rank local test)

Let $S,T\in{\cal B}_d$ be distinct.  There are consecutive rotor columns
whose rank-$(m+d)$ flags are $S,T$, respectively, if and only if

\[
 \boxed{d_J(S,T)=1.}
\tag{5.11}
\]

#### Proof

For $d>-Q$, write $C_d=C_{d-1}+z$.  Formula (5.4) gives

\[
 T=C_{d-1}+y=S-z+y,
\]

with $y\notin S$.  The bottom case is identical from (5.3).

Conversely, write $T=S-z+y$.  Choose a saturated band chain through
$S$ whose increment into rank $m+d$ is $z$ (or put $z$ in the
bottom core when $d=-Q$), extend it above $S$ without using $y$,
and apply the converse part of Theorem 5.1. \(\square\)

Thus even pairwise vertical chain compatibility does not batch arbitrary
components.  A grid block requires a Johnson path at every prescribed row,
a monotone Johnson geodesic on owners, and the common labels (5.9)--(5.10)
across all rows simultaneously.

### Proposition 5.3 (universal short-window owner geodesicity)

Let

\[
 \omega_0\to\omega_1\to\cdots\to\omega_t
\]

be any global or fixed-carrier rotor trajectory, and let $X_i$ be its
middle owner at state $i$.  If $0\le s<t$ and

\[
 t-s\le Q+1,
\tag{5.12}
\]

then

\[
 \boxed{d_J(X_s,X_t)=t-s.}
\tag{5.13}
\]

More exactly, if edge $i$ removes $a_i=z_{Q,i}$ from the owner and
adds the arrival $b_i=y_i$, then the $2(t-s)$ labels

\[
 a_s,\ldots,a_{t-1},b_s,\ldots,b_{t-1}
\]

are pairwise distinct and

\[
 X_t
 =X_s-\{a_s,\ldots,a_{t-1}\}
      +\{b_s,\ldots,b_{t-1}\}.
\tag{5.14}
\]

#### Proof

After $a_i$ leaves owner position $Q$, it occupies collar position
$Q+1$ in state $i+1$.  It reaches collar position $2Q$ in state
$i+Q$, is ejected on edge $i+Q$, and can first be chosen as a new
arrival on edge $i+Q+1$.  Thus it cannot equal a later arrival whose
edge index differs from $i$ by at most $Q$.

After $b_i$ arrives, it lies in the lower block in state $i+1$.  Even
if it is chosen as the next lower departure $x_{i+1}$, it enters collar
position one in state $i+2$, reaches owner-departure position $Q$ in
state $i+Q+1$, and first leaves the owner on edge $i+Q+1$.  Hence it
cannot equal a later owner-departure label in an edge interval of length
at most $Q+1$.  The same latency argument excludes repeated departure
labels and repeated arrival labels in that interval.  Reversing the roles
of the two indices excludes the remaining cross-equalities.

The owner recurrence is $X_{i+1}=X_i-a_i+b_i$.  With all exchange
labels distinct, iteration gives (5.14), whose two difference sets both
have size $t-s$.  This is (5.13). \(\square\)

The threshold is locally sharp: choose an arrival $b_i$ as the lower
departure $x_{i+1}$.  It then becomes the owner-departure label
$a_{i+Q+1}$, so a $Q+2$-edge window can cease to be geodesic.

## 6. Complete-reservoir successor expansion

Let $\mathscr S_Q$ be the set of all global saturated columns.  Its size
is

\[
 V=|\mathscr S_Q|=\frac{(2m)!}{(\ell!)^2}.
\tag{6.1}
\]

Theorem 5.1 gives exactly $\ell^2$ successors and $\ell^2$
predecessors per state.  The outdegree count chooses $x\in L$ and
$y\in R$.  Conversely, from a target
$(L';w_1,\ldots,w_{2Q};R')$, choose the old arrival $y\in L'$ and the
old last collar label $v\in R'$; the predecessor is forced to be

\[
 (L'-y+w_1;w_2,\ldots,w_{2Q},v;R'-v+y).
\]

Thus the indegree is also $\ell^2$.  For a fixed $M$-carrier the
corresponding numbers are

\[
 V_U=\frac{M!}{(m-Q)!(H-Q)!},
 \qquad D_U=(m-Q)(H-Q).
\tag{6.2}
\]

### Theorem 6.1 (deleted-state Hall)

Let $B\subseteq\mathscr S_Q$, $b=|B|$, and
$G=\mathscr S_Q\setminus B$.  For every $A\subseteq G$,

\[
 \boxed{|N_G^+(A)|\ge |A|-b.}
\tag{6.3}
\]

Hence the maximum matching deficiency in the good-to-good successor graph
is at most $b$.

#### Proof

The full successor bipartite graph is regular, hence satisfies Hall:
$|N^+_{\mathscr S_Q}(A)|\ge|A|$.  Passing to the good target class
deletes at most the $b$ vertices of $B$. \(\square\)

### Lemma 6.2 (directed girth)

Every directed rotor cycle has length at least $2Q+2$.

#### Proof

Track a label (x) chosen from the lower block on the first edge.  It
occupies collar positions $1,2,\ldots,2Q$ after the next $2Q$ moves.
On move $2Q+1$ it is ejected into the residual block.  The arrival for
that move was chosen before the ejection, so (x) cannot return to the
lower block until move $2Q+2$.  Before then the lower block, and hence
the state, cannot equal its initial value. \(\square\)

### Theorem 6.3 (integral literal path and short-block cover)

The good states (G) have a vertex-disjoint directed rotor path cover with
at most

\[
 \frac{|G|}{2Q+2}
 +\left(1-\frac1{2Q+2}\right)b
\tag{6.4}
\]

paths.  They have a literal cover by rotor blocks of at most $2Q+2$
states with fewer than

\[
 b+\frac{|G|}{Q+1}+1
\tag{6.5}
\]

blocks.

#### Proof

Take a maximum matching in the good successor graph and identify the left
and right copies of every state.  The resulting directed graph has
indegree and outdegree at most one.  If the matching deficiency is $d$,
there are exactly $d$ path components, including isolated vertices.
Those components use at least $d$ vertices.  Every remaining cycle has
at least $g=2Q+2$ vertices by Lemma 6.2, so cutting one edge per cycle
gives at most

\[
 d+\frac{|G|-d}{g}
 \le \frac{|G|}{g}+\left(1-\frac1g\right)b
\]

paths.  This proves (6.4).

If the resulting path lengths are $v_1,\ldots,v_p$, splitting into
pieces of at most $g$ vertices uses at most

\[
 \sum_i\left\lceil\frac{v_i}{g}\right\rceil
 \le \frac{|G|}{g}+\left(1-\frac1g\right)p
 < b+\frac{2|G|}{g}+1.
\]

Since $2/g=1/(Q+1)$, (6.5) follows.  Every retained edge is an actual
rotor update, so the cover is literal and integral. \(\square\)

The middle-flag projection is uniform on the $W$ owners.  If $B$
consists exactly of the states whose owner lies in $F_{\rm lit}$, then

\[
 \frac bV=\frac fW=O(1/M)=o(1/Q).
\tag{6.6}
\]

Equations (6.4)--(6.5) give a positive integral $O(Q)$-phase block
cover of the complete residual-owner state reservoir.

For all-row deletion, let $Z_r\subseteq{\cal B}_r$ be forbidden target
families and put

\[
 \eta=\sum_{r=-Q}^Q\frac{|Z_r|}{|{\cal B}_r|}.
\tag{6.7}
\]

Transitivity and a union bound give $b/V\le\eta$.  For the certified
one-bite claims,

\[
 \eta\le\frac{kM}{W}+\frac{2Qk}{N}
 =\frac{k}{N}(\rho+2Q)=O(Q/M).
\tag{6.8}
\]

At $Q^2/M\sim\log\log m$, the $O(Q/M)$ deletion term is larger than
the natural $1/Q$ short-block scale by the factor $Q^2/M$.  This is a
limitation of direct row-density deletion, not a negative theorem against
correlated selection.

## 7. A $2m$-cycle integral lift

The full reservoir has much longer exact chronology than the girth bound
alone shows.

### Theorem 7.1 (ordered-lift rotor circulation)

There is an integral occurrence multicover of $\mathscr S_Q$ in which

1. every quotient state occurs exactly $(m-Q)!^2$ times;
2. all occurrences split into directed literal rotor cycles of exact
   length $2m$;
3. every middle owner occurs exactly $(m!)^2$ times.

After deleting all occurrences whose middle owner belongs to a set
$F\subseteq{\cal B}_0$, the remaining occurrences split into literal
rotor paths whose number $p_F$ satisfies

\[
 \boxed{
 \frac{p_F}{(2m)!}
 \le\frac1{2m}+\frac{|F|}{W}.}
\tag{7.1}
\]

In particular, for $F=F_{\rm lit}$, the right side is
$O(1/m)=o(1/Q)$.

#### Proof

For a permutation

\[
 \pi=(p_1,\ldots,p_{2m}),
\]

define

\[
 L(\pi)=\{p_1,\ldots,p_\ell\},
\]

\[
 z_j(\pi)=p_{\ell+j}\quad(1\le j\le2Q),
\]

and

\[
 R(\pi)=\{p_{\ell+2Q+1},\ldots,p_{2m}\}.
\]

Let $\tau$ be cyclic right shift:

\[
 \tau\pi=(p_{2m},p_1,\ldots,p_{2m-1}).
\]

If

\[
 x=p_\ell,\qquad y=p_{2m},
\]

then

\[
 L(\tau\pi)=L(\pi)-x+y,
\]

the new collar is

\[
 (x,z_1,\ldots,z_{2Q-1}),
\]

and

\[
 R(\tau\pi)=R(\pi)-y+z_{2Q}.
\]

Thus one right shift is exactly one global rotor update.

All entries of $\pi$ are distinct, so every $\tau$-orbit has length
$2m$.  The projected quotient states within one orbit are also distinct:
their middle owners are the $2m$ cyclic intervals of length $m$ in
the cyclic order $\pi$, and two different such intervals cannot have
the same underlying set.  Therefore every permutation orbit projects to
a literal rotor cycle of length $2m$.

For a fixed quotient state, the collar order is prescribed while the
orders inside $L$ and $R$ are arbitrary.  It therefore has exactly
$\ell!^2=(m-Q)!^2$ permutation lifts.  A fixed owner $X$ is the set of
the first $m$ permutation entries, so it occurs in exactly
$(m!)^2$ permutations.  This proves assertions 1--3.

There are

\[
 \frac{(2m)!}{2m}
\]

permutation cycles.  Deleting all owner-$F$ occurrences removes exactly
$|F|(m!)^2$ vertices.  Deleting $d$ vertices from a directed cycle
creates at most $d$ nonempty runs when $d>0$, while an untouched cycle
is cut once.  Hence

\[
 p_F\le\frac{(2m)!}{2m}+|F|(m!)^2.
\]

Finally,

\[
 (2m)!=W(m!)^2,
\]

which gives (7.1). \(\square\)

More generally, if a forbidden quotient-state set has density $b/V$,
then deleting all its permutation lifts gives path density at most

\[
 \frac1{2m}+\frac bV.
\tag{7.2}
\]

Thus (6.7) gives $1/(2m)+\eta$ for all-row deletion.

### Corollary 7.2 (literal length of the owner-deleted lift)

Let $T=(2m)!$, let $F\subseteq{\cal B}_0$, and delete every lifted
state occurrence whose owner lies in $F$.  Hard-starting the paths from
Theorem 7.1 gives a direct literal word of length at most

\[
\begin{aligned}
 T-|F|(m!)^2+2Qp_F
 &\le T\left(
 1-\frac{|F|}{W}
 +\frac{Q}{m}
 +2Q\frac{|F|}{W}
 \right)\\
 &=T\left(
 1+\frac{Q}{m}
 +(2Q-1)\frac{|F|}{W}
 \right).
\end{aligned}
\tag{7.3}
\]

For $F=F_{\rm lit}$, this is $T(1+O(Q/m))=T(1+o(1))$.

#### Proof

There are exactly $T-|F|(m!)^2$ surviving state occurrences.  Apply
the direct path ledger $B+2Qp$, Theorem 7.1, and
$T=W(m!)^2$. \(\square\)

Theorem 7.1 is an integral theorem, not a fractional circulation.  Its
scope is nevertheless crucial: it covers every quotient state
$(m-Q)!^2$ times.  It does not choose one state for each residual SCD
chain.  A path may also change the inferred calibrated $M$-top; it is a
direct literal trajectory in the full $[2m]$ MTF state space, not a path
inside one fixed exact truncated top factor.

## 8. Exact coefficient-one ledger and the remaining gate

The first bite has length $O(N)=o(W)$.  Therefore a residual compiler
of length $W+o(W)$ would finish coefficient one.  A residual compiler
built from independently hard-started rotor paths has a stricter
horizontal requirement.

A directed rotor path with $a\ge1$ state columns has direct hard-reset
length

\[
 a+2Q.
\tag{8.1}
\]

Indeed, its first column is initialized by the $2Q+1$ entries in (2.6),
and every further rotor state costs one new entry.  Thus $B$ state
columns in $p$ paths cost

\[
 \boxed{B+2Qp.}
\tag{8.2}
\]

Writing a complete residual block at every hard start gives the more
conservative buffered ledger $B+(2Q+1)p$.

Every physical middle hole needs a distinct right endpoint by Lemma 1.1,
so any appended literal repair, rotor-based or not, has length at least

\[
 W-f=W-o(W).
\tag{8.3}
\]

This is the expected coefficient-one baseline, not by itself an
obstruction.  The obstruction to bounded short rotor blocks is their
reset toll.  Under the designated-state convention, if every path has at
most $CQ$ state columns and $e=o(W)$ middle holes are repaired
separately, then

\[
 B\ge W-f-e,\qquad
 p\ge\left\lceil\frac{W-f-e}{CQ}\right\rceil,
\]

and (8.2) gives

\[
 \boxed{
 B+2Qp
 \ge\left(1+\frac2C-o(1)\right)W.}
\tag{8.4}
\]

If initialization endpoints are allowed to cover additional unlisted
middle holes, the extra $2/C$ in (8.4) need not follow.  The unconditional
statement is only (8.3).  Thus (8.4) is a sharp obstruction for the
standard designated-column compiler, not a lower bound against every
possible endpoint-sharing OR word.

For a $W+o(W)$-column state compiler, (8.2) shows that coefficient one
requires and is implied by

\[
 \boxed{p=o(W/Q).}
\tag{8.5}
\]

Equivalently, the average rotor-run length must be $\omega(Q)$.  Merely
proving $O(W/Q)$ blocks of $O(Q)$ phases leaves an $O(W)$ reset toll
unless those resets are absorbed in place by an additional literal braid.

The exact surviving positive statement can now be isolated without donor
proxies.

> **Actual residual SCD--rotor thinning gate.**  Start with the $W-f$
> retained SCD chains from Theorem 2.2.  Choose one saturated global (or
> coherently fixed-carrier) extension of every chain so that the selected
> columns have a literal rotor path cover with $p=o(W/Q)$.  The
> exceptional holes then cost only $o(W)$ by Corollary 2.3.

Theorems 6.3 and 7.1 prove the analogous horizontal assertion on the full
state reservoir and on an integral permutation multicover.  They do not
prove the thinning gate.  A thin rank-balanced table can have an empty
successor graph, so neither row marginals nor division by state-fibre
multiplicity is valid.  The exact local conditions which a successful
thinning must preserve are (5.3)--(5.4) and, in grid form,
(5.8)--(5.10).

## 9. Independent decisive-step audit

The following points were checked separately from the derivations which
suggested them.

1. The factor $2Q$ in Theorem 2.2 excludes the middle row: a deleted SCD
   chain's middle member is physically covered, so only the $2Q$
   nonmiddle controlled ranks can contribute exceptions.
2. The direct exceptional repair costs $2Q+1$, not $2Q+2$: the final
   entry $L$ is already the first state endpoint.  Adding a residual
   block is optional for a direct literal word.
3. The directed girth is $2Q+2$, not merely $2Q+1$: the ejected label
   cannot be chosen as the arrival on the same update that ejects it.
4. The matching-to-path count subtracts the vertices already lying in
   path components before charging cycle components, giving the factor
   $(1-1/(2Q+2))b$ in (0.9).
5. In Theorem 7.1, right rotation uses $x=p_\ell$ and $y=p_{2m}$.
   Both unordered blocks update exactly as required, every permutation
   orbit has length $2m$, and projected states do not repeat because
   their length-$m$ cyclic owner windows do not repeat.
6. The full-reservoir and permutation-lift theorems are deliberately not
   divided by their multiplicities.  The one-copy-per-chain selection is
   precisely the unproved step.

This closes the assigned lane as far as the present hypotheses allow:
actual vertical condensation and full-multiplicity horizontal expansion
are proved with exact constants and literal chronology; coefficient one
still depends on the integral SCD--rotor thinning gate or on a genuinely
new in-place reset-sharing braid.

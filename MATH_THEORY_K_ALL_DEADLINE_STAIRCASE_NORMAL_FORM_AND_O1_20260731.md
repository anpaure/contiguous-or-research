# Deadline staircases: the forced normal form and the additive-constant gate

Date: 2026-07-31  
Status: proved normal-form and compiler lemmas; the all-\(k\) existence
theorem remains open

## 0. Why the carrier model has to be enlarged

The optimal odd words at \(k=11,13,15\) have a flat middle row:
\(D^dA\) is a permutation of the middle layer.  The verified optimum at
\(k=16\) is different.  Its depth-three row contains both ranks eight and
nine, while middle-rank sets first appear at more than one depth.  Thus a
flat carrier is a useful construction subclass, but it is not the normal
form forced by optimality.

The correct invariant is the **first-middle deadline staircase**.  It is
already implicit in the monotone-deadline lower bound.  This note makes that
normal form explicit, proves the exact upper-transfer and residence
criteria, and states the resulting \(B(k)+O(1)\) interface.

Throughout put

\[
 r=\lceil k/2\rceil,\qquad W=\binom kr,
 \qquad B(k)=W+d,
\]

where \(d=d(k)\) is the proved deadline lower-bound depth.

## 1. Every optimum contains a monotone deadline staircase

Let \(A=(A_0,\ldots,A_{L-1})\) be a word of nonempty subsets of \([k]\),
and write

\[
 U(i,j)=\bigcup_{p=i}^j A_p.
\]

For a start \(i\), if its row ever reaches rank \(r\), let \(F_i\) be the
first endpoint at which it does and put \(T_i=U(i,F_i)\).

### Theorem 1.1 (forced staircase)

If \(L=W+d\) and the word covers every rank-\(r\) target, then there is a
set \(I\subseteq\{0,\ldots,L-1\}\) of exactly \(W\) starts such that:

1. \(\{T_i:i\in I\}=\binom{[k]}r\);
2. if \(i<i'\) are in \(I\), then \(F_i<F_{i'}\);
3. consequently exactly \(d\) physical starts and exactly \(d\) physical
   deadlines are omitted.

#### Proof

For a fixed start, the cells \(U(i,i),U(i,i+1),\ldots\) form an inclusion
chain, so that row contains at most one *distinct* rank-\(r\) set.  Covering
all \(W\) rank-\(r\) sets therefore uses at least \(W\) distinct starts;
choose one start for every target and call the resulting set \(I\).

If \(i<i'\) and \(F_i=F_{i'}\), then

\[
 U(i',F_i)\subseteq U(i,F_i).
\]

Both have rank \(r\), so they are equal, contrary to the choice of distinct
targets.  The standard deletion monotonicity

\[
 U(i+1,j)\subseteq U(i,j)
\]

also implies that first-middle deadlines are nondecreasing with the start.
They are therefore strictly increasing on \(I\).  There are \(L=W+d\)
possible starts and deadlines, leaving exactly \(d\) of each outside the
chosen staircase. \(\square\)

Write the selected starts and deadlines in increasing order as

\[
 s_0<\cdots<s_{W-1},\qquad q_0<\cdots<q_{W-1},
\]

where \(q_i=F_{s_i}\), and put

\[
                       T_i=U(s_i,q_i).
\tag{1.1}
\]

The flat carrier is the special case \(s_i=i,q_i=i+d\).  The \(k=16\)
certificate instead uses an order-preserving variable-span schedule.

### Theorem 1.2 (start--deadline debt identity)

Let \(X\) and \(Y\) be the omitted starts and deadlines, respectively, in a
length-\(L=W+d\) staircase.  Count the cells strictly before the selected
middle occurrence in every selected start row, and the cells below the
middle in every omitted start row.  Define

\[
 \begin{aligned}
 \operatorname{sdebt}(X)
   &=dL-\sum_{x\in X}\bigl(x+\min(d,L-x)\bigr),\\
 \operatorname{ddebt}(Y)
   &=\sum_{y\in Y}y-\binom d2.
 \end{aligned}
\tag{1.2}
\]

Then both debts are nonnegative and

\[
 \boxed{
 {\cal C}_{<r}\le
 dW+\binom{d+1}2-\operatorname{sdebt}(X)
                       -\operatorname{ddebt}(Y).}
\tag{1.3}
\]

Equality holds if every omitted start row attains its depth cap.  The maximum
is attained by the terminal omitted starts
\(X=\{L-d,\ldots,L-1\}\) and the earliest omitted deadlines
\(Y=\{0,1,\ldots,d-1\}\).

#### Proof

The selected rows contribute

\[
 \sum_i(q_i-s_i)
 =\left(\sum_{t=0}^{L-1}t-\sum_{y\in Y}y\right)
  -\left(\sum_{t=0}^{L-1}t-\sum_{x\in X}x\right)
 =\sum_{x\in X}x-\sum_{y\in Y}y.
\]

The depth-cap lemma from the lower-bound proof says that an omitted row
starting at \(x\) has at most \(\min(d,L-x)\) cells below rank \(r\).
Adding these caps over \(X\) gives

\[
 {\cal C}_{<r}\le
 \sum_{x\in X}\bigl(x+\min(d,L-x)\bigr)-\sum_{y\in Y}y,
\]

which is (1.3) after inserting (1.2).  Each summand in the start sum is at
most \(L\), and the smallest sum of \(d\) distinct nonnegative deadlines is
\(\binom d2\), proving nonnegativity and the equality statement. \(\square\)

If

\[
 \operatorname{slack}(k)=
 dW+\binom{d+1}2-\sum_{j=1}^{r-1}\binom kj,
\]

then scalar lower-layer feasibility forces

\[
 \operatorname{sdebt}(X)+\operatorname{ddebt}(Y)\le
                  \operatorname{slack}(k).
\tag{1.4}
\]

Terminal omitted starts have zero start debt.  In that important subclass,
only delayed omitted deadlines spend slack, which is the one-jump mechanism
used by the \(k=16\) carrier.  Moving starts earlier can repair residence and
chain alignment, but it spends the explicitly measured start debt in (1.2).
Integral common-cap feasibility is still stronger than (1.4).

### Corollary 1.3 (critical-dimension rigidity)

If \(\operatorname{slack}(k)=0\), then every optimal word must omit exactly
the terminal starts and the earliest deadlines \(0,1,\ldots,d-1\), every
omitted start row must attain its depth cap, and every pre-middle cell is
forced to represent a distinct lower target.  More generally, the combined
start/deadline debt is at most \(\operatorname{slack}(k)\).

This explains why the zero-slack cases such as \(k=9\) force qualitatively
different witnesses, while positive-slack cases permit endpoint rerooting.

### Theorem 1.4 (particle/queue normal form)

There is a second exact parametrization which is much more useful for
constructing non-flat staircases.  Write the omitted starts and deadlines as

\[
 X=\{x_0<\cdots <x_{d-1}\},\qquad
 Y=\{y_0<\cdots <y_{d-1}\},
\]

and define their owner-time thresholds

\[
                    G_t=x_t-t,\qquad H_t=y_t-t.
\tag{1.5}
\]

Conversely, every pair of nondecreasing integer sequences
\(0\le G_0\le\cdots\le G_{d-1}\le W\) and
\(0\le H_0\le\cdots\le H_{d-1}\le W\) reconstructs valid omitted
positions by \(x_t=G_t+t\), \(y_t=H_t+t\).  Thus this is a bijective
parametrization, not merely notation for schedules already known to exist.

For owner \(i\), put

\[
 g_i=\#\{t:G_t\le i\},\qquad
 h_i=\#\{t:H_t\le i\}.
\tag{1.6}
\]

Then:

1. \(s_i=i+g_i\) and \(q_i=i+h_i\);
2. the owner support has length
   \[
                      q_i-s_i+1=1+h_i-g_i;
   \tag{1.7}
   \]
3. the supports are nonempty iff \(H_t\le G_t\) for every \(t\);
4. subject to the nonempty-support condition in 3, chain alignment is
   equivalent to
   \[
       H_t\le G_t-\mathbf 1_{\{0<G_t<W\}}
                 \qquad(0\le t<d);
   \tag{1.8}
   \]
5. the separable start/deadline debts from Theorem 1.2 are
   \[
   \boxed{
    \operatorname{ddebt}=\sum_{t=0}^{d-1}H_t,\qquad
    \operatorname{sdebt}=\sum_{t=0}^{d-1}(W-G_t-t)^+.}
   \tag{1.9}
   \]
6. the sharper exact loss of cells under the monotone middle boundary is
   \[
   \boxed{
   \operatorname{Loss}(G,H)=
      \sum_tH_t+\sum_t(W-G_t)
      +\#\{(t,u):G_t<H_u\}.}
   \tag{1.10}
   \]
   Hence the full pre-middle staircase catalogue has exactly
   \[
      dW+\binom{d+1}{2}-\operatorname{Loss}(G,H)
   \tag{1.11}
   \]
   cells.  In particular, scalar feasibility requires
   \(\operatorname{Loss}(G,H)\le\operatorname{slack}(k)\).

Moreover, an internal coordinate run \([a,b]\) of length
\(\ell=b-a+1\) satisfies the residence corridor iff

\[
 \boxed{
 \#\{t:H_t\le a-1\}-\#\{t:G_t\le b+1\}\le \ell-1.}
\tag{1.12}
\]

#### Proof

Before the selected start \(s_i\), exactly \(g_i\) start positions have
been omitted, which gives \(s_i=i+g_i\); the deadline formula is identical.
This proves (1.7).  For two nondecreasing threshold lists, the cumulative
inequalities \(g_i\le h_i\) for every \(i\) are equivalent to the
coordinatewise inequalities \(H_t\le G_t\), proving the nonempty-support
claim.

Chain alignment is \(g_{i+1}\le h_i\).  If \(0<G_t<W\), apply this at
\(i=G_t-1\) to obtain \(H_t\le G_t-1\).  If \(G_t=0\), support feasibility
forces \(H_t=0\), while if \(G_t=W\), that threshold is never crossed by an
owner transition and only \(H_t\le W\) remains.  These are exactly (1.8),
and the converse follows by reversing the same argument.

Since \(y_t=H_t+t\), the deadline debt in (1.2) is \(\sum_tH_t\).  Also

\[
 \operatorname{sdebt}
 =\sum_{x\in X}\bigl(L-x-\min(d,L-x)\bigr)
 =\sum_{x\in X}(W-x)^+,
\]

and substituting \(x_t=G_t+t\) proves (1.9).  Finally, substitute
\(q_{a-1}=a-1+h_{a-1}\) and
\(s_{b+1}=b+1+g_{b+1}\) into (3.3).  The result is
\(h_{a-1}-g_{b+1}\le\ell-1\), which is (1.12).

For the exact catalogue count, an omitted start with threshold \(G_t<W\)
lies immediately before selected owner \(G_t\), so its available cells stop
at \(q_{G_t}\).  Relative to the extremal rectangle its loss is

\[
 L-q_{G_t}
 =W-G_t+\#\{u:G_t<H_u\}.
\]

The selected-deadline boundary loses \(\sum_uH_u\) further cells.  Summing
over the omitted starts proves (1.10)--(1.11). \(\square\)

The interpretation is a FIFO queue of \(d\) delay particles.  The omitted
deadline threshold \(H_t\) activates particle \(t\), and the omitted-start
threshold \(G_t\) discharges it.  The queue height at owner \(i\) is
\(h_i-g_i\), exactly the support span minus one.  Equation (1.12) says that
at most \(\ell-1\) particles activated before a length-\(\ell\) run may
remain undischarged after it.  Formula (1.9) separates the coarse start and
deadline debts; (1.10) adds the exact crossing interaction between early
start omissions and delayed deadline omissions.

This turns variable-depth residence into a finite scheduling problem with
only \(2d\) monotone thresholds.  It also explains the raw \(k=16\) optimum:

\[
 G=(W,W,W),\qquad H=(0,1,6387),
\]

so its queue heights are \(1^1,2^{6386},3^{6483}\).  The first shallow band
absorbs the exceptional boundary behaviour, the span-two band absorbs all
length-three runs placed before the last activation, and only the suffix
needs flat depth-three residence.

## 2. Exact upper transfer for a chain-aligned staircase

Call the staircase **chain aligned** if

\[
                         s_{i+1}\le q_i+1
               \qquad(0\le i<W-1).
\tag{2.1}
\]

### Theorem 2.1 (staircase transfer identity)

For every \(0\le a\le b<W\), a chain-aligned staircase satisfies

\[
        \boxed{
        \bigcup_{i=a}^b T_i
        =\bigcup_{p=s_a}^{q_b}A_p.}
\tag{2.2}
\]

Hence every target represented by a consecutive union in the staircase
word \(T\) is represented by one physical interval of \(A\).

#### Proof

The support of \(T_i\) is the physical interval \([s_i,q_i]\).  The starts
and deadlines are increasing, and (2.1) says successive supports overlap or
touch.  Their union for \(a\le i\le b\) is therefore the single interval
\([s_a,q_b]\).  Taking the union of the letters over those supports proves
(2.2). \(\square\)

This is the precise reason the mixed-depth \(k=16\) solution still has a
carrier/compiler interpretation.  Constant depth is unnecessary;
order-preserving supports are enough.

## 3. Maximal envelopes and the exact residence corridor

Given only \(T\) and its supports, define the maximal legal source envelope

\[
 P_p=\bigcap_{i:\ s_i\le p\le q_i}T_i.
\tag{3.1}
\]

At a physical position contained in no support, set \(P_p=[k]\); such a
position is irrelevant to middle preservation.  Every source realizing
(1.1) must satisfy \(A_p\subseteq P_p\).

Fix a coordinate \(x\), and let \([a,b]\) be a maximal positive run of
\(x\) in \(T_0,\ldots,T_{W-1}\).  Use the boundary conventions
\(q_{-1}=-1\) and \(s_W=L\).

### Theorem 3.1 (residence-corridor criterion)

The maximal envelopes realize every middle target,

\[
                 \bigcup_{p=s_i}^{q_i}P_p=T_i
                 \qquad(0\le i<W),
\tag{3.2}
\]

if and only if every internal coordinate run \([a,b]\) satisfies

\[
                         q_{a-1}+1<s_{b+1}.
\tag{3.3}
\]

For the flat schedule this reduces to \(b-a+1\ge d+1\), the familiar
minimum-residence condition.

#### Proof

A physical position can contain \(x\) only if every staircase support
covering it belongs to the run \([a,b]\).  The safe positions are therefore

\[
                    [q_{a-1}+1,\ s_{b+1}-1].
\tag{3.4}
\]

Because starts and deadlines are strictly increasing, every support
\([s_i,q_i]\), \(a\le i\le b\), meets (3.4) exactly when (3.4) is nonempty,
which is (3.3).  In that case \(x\) occurs in the union of the envelopes for
every owner in the run.  If (3.3) fails, no position can carry \(x\) without
putting it into an adjacent owner outside the run.  Applying this argument
coordinatewise proves (3.2).  Boundary runs have only one outside neighbour
and are automatic under the displayed conventions. \(\square\)

### Corollary 3.2 (one-jump residence exchange)

Fix the selected starts \(s_i=i\), omit the terminal \(d\) physical starts,
and omit deadlines

\[
                    Y=\{0,1,\ldots,d-2,M+d-1\}.
\tag{3.5}
\]

Then

\[
 q_i=\begin{cases}
       i+d-1,&i<M,\\
       i+d,&i\ge M,
     \end{cases}
\tag{3.6}
\]

and the deadline debt is exactly \(M\).  Every internal run of length at
least \(d+1\) is safe; a run of length exactly \(d\), starting at \(a\), is
safe exactly when \(a\le M\); and every shorter internal run is unsafe.

#### Proof

The selected-deadline order after deleting (3.5) gives (3.6), and (1.2)
gives debt \(M\).  For a run \([a,a+\ell-1]\), equation (3.3) becomes

\[
 q_{a-1}+1<a+\ell.
\]

If \(a\le M\), its left adjacent owner lies in the short-span region and
the left side is \(a+d-1\), so the condition is \(\ell\ge d\).  If
\(a>M\), the left side is \(a+d\), so it is \(\ell\ge d+1\). \(\square\)

For \(d=3\), spending debt \(M\) creates a prefix of \(M\) span-two owners
which can absorb every length-three run starting there; length-two runs still
have to be eliminated, cut, or moved to a true boundary.  The raw \(k=16\)
optimum uses precisely this mechanism: it has 1,425 length-three staircase
runs in total (1,423 internal and two boundary runs) but no bad residence
corridor.  At \(k=17\), scalar slack 7,401 is
therefore a budget for a 7,401-owner run-three absorption region.  A strong
globally min-run-four factor is sufficient but substantially stronger than
necessary.

### Theorem 3.3 (exact minimum residence debt for a fixed chronology)

Keep the terminal omitted starts, so \(s_i=i\).  For
\(0\le j<W\), define

\[
 c_j=\min\left(
 d,
 \{\,|R|-1:R\text{ is an internal positive run starting at }j+1\,\}
 \right),
\tag{3.7}
\]

where the minimum of the empty set is ignored, and put

\[
 h_j^*=\min_{t\ge j}c_t,
 \qquad
 \mathfrak D_d(T)=\sum_{j=0}^{W-1}(d-h_j^*).
\tag{3.8}
\]

Then \(\mathfrak D_d(T)\) is exactly the minimum deadline debt among all
monotone schedules with these starts which satisfy every residence corridor.
Consequently such a scalar-feasible staircase exists if and only if

\[
                  \mathfrak D_d(T)\le
                  \operatorname{slack}(k).
\tag{3.9}
\]

#### Proof

Write \(h_i=q_i-i\).  Strictly increasing deadlines are equivalent to a
nondecreasing integer profile

\[
                 0\le h_0\le\cdots\le h_{W-1}\le d;
\]

conversely every such profile determines the selected deadlines and the
complementary set of \(d\) omitted deadlines.  Theorem 3.1 says that an
internal run of length \(\ell\) starting at \(a\) is safe exactly when

\[
                     h_{a-1}<\ell,
\]

which is precisely the pointwise constraint \(h_j\le c_j\).  Any feasible
nondecreasing profile obeys \(h_j\le c_t\) for every \(t\ge j\), hence
\(h_j\le h_j^*\).  The suffix-minimum profile \(h^*\) is itself
nondecreasing and feasible, so it uniquely maximizes \(\sum h_j\).
By Theorem 1.2 its debt is \(dW-\sum h_j\), proving (3.8)--(3.9).
\(\square\)

Thus fixed-chronology residence is not a SAT problem and not a weighted
motif count: it is one suffix-minimum scan.  For the raw \(k=16\) optimum,
\(\mathfrak D_3(T)=6384\), while its realized first-middle staircase spends
6388; the extra four units come from the simultaneous compiler, not from
residence.  For \(k=11,\ldots,15\), the same audit gives zero minimum
residence debt.

### Theorem 3.4 (exact arbitrary-start staircase optimizer)

Fix a nondecreasing start-threshold vector
\(G=(G_0,\ldots,G_{d-1})\), and let \(g_i\) be as in (1.6).  For
\(1\le j\le d\), define

\[
 \rho_j^G=
 \max\Bigl(
  \{a:\ [a,b]\text{ is an internal coordinate run and }
       (b-a+1)+g_{b+1}\le j\}\cup\{0\}
 \Bigr).
\tag{3.10}
\]

Then a deadline-threshold vector \(H\) realizes every middle owner iff

\[
                       H_{j-1}\ge\rho_j^G
                       \qquad(1\le j\le d).
\tag{3.11}
\]

For this fixed \(G\), the unique coordinatewise-minimal row-exact choice is

\[
                         H^G_{j-1}=\rho_j^G.
\tag{3.12}
\]

It is a legal chain-aligned schedule exactly when (1.8) holds for
\((G,H^G)\).  If it fails chain alignment, increasing any threshold in
\(H^G\) cannot repair it.  Consequently the exact arbitrary-start
row-exact/scalar criterion is

\[
 \boxed{
 \min_{\substack{0\le G_0\le\cdots\le G_{d-1}\le W\\
                  (G,H^G)\text{ satisfies }(1.8)}}
       \operatorname{Loss}(G,H^G)
       \le \operatorname{slack}(k).}
\tag{3.13}
\]

This criterion concerns the staircase geometry and the exact number of
available lower cells.  Nonempty common envelopes, labelled lower targets,
pins, and the common-cap coupling remain additional conditions.

#### Proof

For a run \([a,b]\) of length \(\ell\), (1.12) fails precisely when
\(h_{a-1}\ge \ell+g_{b+1}\).  For \(j=\ell+g_{b+1}\), the inequality
\(h_{a-1}<j\) is equivalent to \(H_{j-1}\ge a\).  Taking the maximum over
all runs which constrain level \(j\) proves (3.11).  The frontiers are
nondecreasing in \(j\), so (3.12) is a valid nondecreasing vector.

Both \(\sum H_t\) and the crossing term in (1.10) are nondecreasing when
an \(H_t\) moves right.  Hence (3.12) uniquely minimizes the exact loss.
Moving it right only decreases the deadline profile \(h\), so it cannot
repair a failed inequality \(g_{i+1}\le h_i\).  Combining this with
Theorem 1.4 proves (3.13). \(\square\)

For terminal omitted starts, \(G=(W,\ldots,W)\), the crossing and start
terms vanish.  In that case \(\rho_j^G\) is simply the latest start of an
internal run of length at most \(j\), and

\[
                         \mathfrak D_d(T)=\sum_{j=1}^d\rho_j^G,
\tag{3.14}
\]

which is the threshold form of Theorem 3.3.

The six-integer \(\delta/\tau\) replay used at \(k=17\) is exactly (3.3)
written in threshold coordinates.  Thus the finite search is testing the
general residence theorem, not a special motif heuristic.

## 4. One common-cap compiler

Let \({\cal Z}\) be a family of lower targets.  Assign each
\(Z\in{\cal Z}\) to a distinct physical interval \(J_Z\).  Define

\[
 A_p=P_p\cap\bigcap_{Z:\ p\in J_Z} Z.
\tag{4.1}
\]

### Theorem 4.1 (simultaneous compiler criterion)

The word in (4.1) realizes the whole staircase and every assigned lower
target if and only if

\[
 \begin{aligned}
 &\forall i,\ x\in T_i,\quad
   \exists p\in[s_i,q_i]\text{ with }x\in A_p,\\
 &\forall Z\in{\cal Z},\ x\in Z,\quad
   \exists p\in J_Z\text{ with }x\in A_p,
 \end{aligned}
\tag{4.2}
\]

and every \(A_p\) required as a letter is nonempty.

#### Proof

By construction \(A_p\subseteq P_p\), so no staircase owner gains an
illegal coordinate.  The first line of (4.2) says none loses a required
coordinate, proving (1.1).  Likewise, (4.1) gives \(A_p\subseteq Z\) on
\(J_Z\), while the second line of (4.2) supplies every coordinate of \(Z\);
hence \(\bigcup_{p\in J_Z}A_p=Z\).  The converse follows by reading these
necessary coordinate witnesses from any successful realization. \(\square\)

This is the phase-free mathematical content of the common-cap CNF that
finished \(k=16\).  A Hall matching of targets to intervals is only the
marginal part; (4.2) is the exact overlap coupling.

## 5. The defect-tolerant theorem

### Theorem 5.1 (staircase certificate)

Suppose a length-\(B(k)\) staircase satisfies:

1. its \(T_i\) enumerate the rank-\(r\) layer;
2. it is chain aligned and satisfies (3.3);
3. consecutive unions of \(T\) cover every upper target except a family
   \({\cal U}_{\rm miss}\);
4. a common-cap assignment realizes every lower target except a family
   \({\cal L}_{\rm miss}\).

Then

\[
 \nu(k)\le B(k)+|{\cal U}_{\rm miss}|+|{\cal L}_{\rm miss}|.
\tag{5.1}
\]

In particular, uniformly bounded total defect proves \(B(k)+O(1)\), and
zero defect proves \(\nu(k)=B(k)\).

#### Proof

Theorem 2.1 transfers every certified upper witness to a physical interval;
Theorem 4.1 supplies the middle and lower witnesses.  Append every omitted
target as a one-letter interval. \(\square\)

The point is not the elementary append operation.  The point is that the
four apparent global tasks have become four literal certificate conditions
on one monotone staircase, with no flatness or Hamiltonicity assumption.

## 6. Reconciliation of the known exact constructions

The raw-answer audit gives the following exact picture.

* \(k=11,13,14\): the first-middle staircase is flat.  At \(k=12\) there is
  one span-one owner among 923 span-two owners; at \(k=15\) there is one
  span-one owner among 6,434 span-three owners.  The \(k=13\) and \(k=15\)
  carriers are obtained by opening two cyclic components and replacing the
  two cut edges by one seam.  Connectivity of the original factor is not
  required.
* \(k=16\): the optimum is genuinely nonflat.  At depth three its OR row
  has 6,484 rank-eight cells and 6,386 rank-nine cells; the missing
  rank-eight owners first occur in shallower rows.  The construction-time
  carrier schedule had selected area 32,224.  Independently extracting the
  first-middle staircase from the final word gives spans
  \(1^1,2^{6386},3^{6483}\), selected area 32,222, omitted starts
  \(12870,12871,12872\), and omitted deadlines \(0,2,6389\).  It is completed
  by one common-cap assignment.  This is a direct finite instance of
  Theorems 1.1--4.1.
* The canonical odd PBBS two-matching factor already has exact lower colours
  and complete lower/upper support at **every depth** for all odd \(k\).
  It need not satisfy (3.3) after opening, and its lower common-cap compiler
  is not automatic.

The PBBS topology is now exact as well.  Its component counts begin

\[
 1,2,3,6,12,26,73,146,360,1408,\ldots,
\]

and are given in all dimensions by the action--angle determinant sum in
`MATH_THEOREM_K_ALL_PBBS_ACTION_ANGLE_COMPONENT_CENSUS_AND_SEAM_SLACK_20260731.md`.
Every PBBS period is odd, so the centered factor has exactly the same
component count as the PBBS permutation.  At the later tight dimensions the
raw seam count is already below scalar staircase slack: \(1408<9579\) at
\(k=21\), and \(26{,}478{,}632<815{,}150{,}707\) at \(k=39\).  Thus raw
component abundance is not the asymptotic obstruction.  Recycling their
cut colours inside one common cap is.

Thus the direct constructions do not support a universal flat-carrier
conjecture.  They support a stronger and more flexible statement:

> every dimension should admit a protected PBBS/Pascal rethreading whose
> first-middle occurrences form a chain-aligned deadline staircase with a
> bounded-defect common cap.

## 7. The actual \(O(1)\) conjecture after the synthesis

For a cyclic all-depth factor, assign each upper target to one component
that realizes it and choose one opening per component.  The upper cost is
the total cut-kernel loss; the lower cost is whatever the common-cap
compiler cannot recycle.  Component count by itself is not the cost.

The general additive-constant conjecture is therefore reduced to proving
the following bounded-defect transport statement.

### Protected staircase conjecture

For every sufficiently large \(k\), the canonical PBBS/Pascal shadow factor
can be moved by degree-preserving alternating circuits to a state admitting
ordered openings and a deadline staircase for which:

1. the global normalized upper cut-kernel mass is \(O(1)\);
2. the residence corridors (3.3) all hold;
3. the common-cap compiler misses only \(O(1)\) lower targets.

Together with the global kernel-mass lemma in
`MATH_THEORY_K_ALL_BALANCED_TWO_EXTENSION_HEXAGON_AND_O1_REDUCTION_20260731.md`,
this proves

\[
                         \boxed{\nu(k)=B(k)+O(1)}.
\]

For exact equality, replace both bounded defects by zero or recycle them in
the staircase halo.  That is a strictly sharper endpoint problem.

The current evidence splits the protected staircase conjecture into three
more concrete claims.

1. **Protected transport:** alternating incidence circuits can cluster or
   remove short runs while retaining the PBBS all-depth decks.  Primitive
   greedy descent is false; compound or neutral plateau motion is necessary.
2. **Deadline/facet exchange:** the scalar seam bill can be converted into
   internal rank-\((r-1)\) service by moving the omitted starts and spending
   bounded deadline debt.  Theorem 1.2 proves the exact scalar exchange;
   the missing assertion is its integral common-cap version.  The nonflat
   \(k=16\) optimum is the first complete witness to this mechanism.
3. **Common-cap closure:** after the protected chronology and staircase are
   fixed, the lower target/interval assignment has a simultaneous solution
   of (4.2) with only bounded defect.

The exact fragment ledger sharpens the first claim.  If \(b\) source edges
are cut and \(j\) of the \(b-1\) seams are Johnson, then the number \(H\) of
missing lower q1 colours and the total repeat excess \(E\) satisfy

\[
                              H-E=b-j.
\]

Thus even a braid with thousands of fragments has exactly the single forced
boundary hole when all seams are Johnson and their colours are a distinct
\((b-1)\)-subset of the cut colours.  Large fragmentation is therefore
compatible with the exact formula; the missing theorem is a **rainbow
endpoint routing** theorem, not a bounded-fragment theorem.  See
`MATH_THEOREM_K_ALL_FRAGMENT_BRAID_LOCALITY_AND_SERVICE_20260731.md`.

At the present \(k=17\) endpoint, every one of the 1,838 deep holes has at
least 82 run-safe Johnson seam providers, while one provider serves at most
five holes.  Double counting proves Hall with factor \(82/5\), so all holes
already admit distinct local providers.  What remains is to select them with
pairwise compatible endpoints and protected spans in one rainbow path cover,
then pass the exact threshold and common-cap tests.

This is narrower than the older request for a brand-new all-depth factor:
PBBS has already supplied the factor and the entire shadow tower.

## 8. What has and has not been proved

Proved here:

* the staircase is forced in every length-\(B(k)\) solution;
* chain alignment gives the exact upper-transfer identity;
* (3.3) is the exact variable-depth residence condition;
* (4.2) is the exact simultaneous common-cap condition;
* bounded total defect implies \(B(k)+O(1)\).

Still open:

* protected alternating-circuit connectivity to a staircase-resident state;
* bounded global cut-kernel mass for a compatible opening distribution;
* a uniform common-cap theorem with \(O(1)\) defects;
* the zero-defect strengthening needed for \(\nu(k)=B(k)\).

The main conceptual gain is that flatness, a single Hamilton cycle, and a
bounded number of components are no longer mistaken for necessary gates.
The forced object is the deadline staircase, and the quantitative object is
total defect.

The raw-word replay for \(k=11,\ldots,16\), including strict deadlines,
chain alignment, every residence corridor, and complete upper transfer, is
retained in
`scratch/audit_deadline_staircase_known_optima_20260731.py`; its normalized
audit payload is
`f2a7569f9ffb61eb677775becd627283fff7ee6c5b194f9b39a630a375f2c782`.

## 9. Construction order: braid before demanding perfection

The exact \(k=13\) and \(k=15\) words give a final warning about the order of
the gates.  Their useful cyclic factors have multiple components; cutting,
orienting, ordering, and seaming those components simultaneously changes

* the deleted and newly supplied lower colours;
* the upper witnesses destroyed by cuts and created across seams;
* coordinate runs at component ends; and
* the staircase corridor profile.

Therefore neither cyclic all-upper completeness nor cyclic strong residence
is necessary before the braid is chosen.  A factor can have cyclic deep
holes which are filled by suffix--prefix intervals across seams, and cyclic
short runs which are lengthened or placed in a shallow staircase region.

For a candidate factor the correct finite object is a **budgeted decorated
braid CSP**: choose cuts (possibly more than one per original component),
orient and order the resulting fragments, recycle their deleted lower
colours at seams, replay the resulting *linear* upper palette and the exact
debt functional (3.8), then invoke the common-cap compiler.  Extra cuts are
not gratuitous: they create suffix--prefix service opportunities and can
cluster residence debt.  Their count is paid from the scalar slack and their
colours must be recycled integrally.  This is strictly weaker than demanding
a Hamilton, all-depth, globally min-run factor and is the direct
generalization of the seam mechanisms visible at \(k=13,14,15,16\).

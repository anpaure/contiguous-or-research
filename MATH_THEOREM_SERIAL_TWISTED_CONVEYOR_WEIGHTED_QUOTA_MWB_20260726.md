# Serial twisted conveyors in the exact weighted-quota norm

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Serial twist cancellation enlarges the exact construction space:
individual slabs may have nonidentity port monodromy, provided the
transported product is the identity, every row has the prescribed final
length, and all seams and crossing collars have exact ownership.

None of those facts controls MWB. The authoritative shallow statistic is
the final mobile floor/ceiling mismatch
\[
 \boxed{
 \mathfrak Q_A(F)=
 \sum_{q\le H_A}
 \frac{\operatorname {dist}_1(\mu_q^F,\mathcal B_q)}
      {2c_q}
 =
 \sum_{q\le H_A}\frac{O_q(F)}{c_q},}                  \tag{0.1}
\]
where \(H_A=\lceil A\sqrt m\rceil\). This is a distance from the final
histogram to the finite set of balanced quota vectors; it is not a norm
of an isolated local carrier.

For a serial conveyor core \(\mathcal M\) and one exact completion
\(\mathcal C\), the exact chosen-quota identity is
\[
\boxed{\begin{aligned}
 \sum_S(\mu_q^{\mathcal M}+\mu_q^{\mathcal C}-b_q)_+
={}&
 \sum_S(\mu_q^{\mathcal M}-b_q)_+\\
 &+\sum_S\left(
 \mu_q^{\mathcal C}-(b_q-\mu_q^{\mathcal M})_+
 \right)_+ .
\end{aligned}}                                        \tag{0.2}
\]
The first term is the final conveyor-core exceedance; the second is the
exact completion spill into its remaining mobile quota. Their
\(1/c_q\)-weighted sum must be \(o_A(W)\).

The nonvacuous serial theorem below requires a growing local scale and a
positive fraction of distinct global rows genuinely altered by
nonidentity twisted packets. It cannot be satisfied by declaring the
core empty and calling an arbitrary MWB witness the completion.

The clean row-count-only specialization is:

* the near-full conveyor core is quota-safe at every protected depth;
* it has one exact rooted completion of
  \[
                       R=o_A(\operatorname {Cat}_m/\sqrt m)             \tag{0.3}
  \]
  rows.

This implies fixed-window MWB. For every fixed \(A\), diagonalization then
gives MWB and hence coefficient one. No current construction proves these
hypotheses.

## 1. Mobile balanced quotas, exactly

Put
\[
 n=2m+1,\qquad W=\binom nm,\qquad
 B=\frac Wn=\operatorname {Cat}_m,                    \tag{1.1}
\]
\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
 \rho_q=W-c_qN_q.                                     \tag{1.2}
\]
Let
\[
 \mathcal B_q=
 \left\{
 b:\binom{[n]}{m-q}\to\{c_q,c_q+1\}:
 |\{S:b(S)=c_q+1\}|=\rho_q
 \right\}.                                            \tag{1.3}
\]
Every \(b\in\mathcal B_q\) has total mass \(W\).
Write
\[
 \operatorname {dist}_1(x,\mathcal B_q)
 =\min_{b\in\mathcal B_q}\|x-b\|_1.
\]
Throughout, \(q\le H_A\) means \(1\le q\le H_A\); depth \(0\) is already
owned exactly once by an exact middle factor and contributes zero.

For a family \(\mathcal R\) of literal cyclic rows, let
\[
 \mu_q^{\mathcal R}(S)
 =\bigl|\{(\Pi,h):\Pi\in\mathcal R,\,
                 I_\Pi(h,m-q)=S\}\bigr|.             \tag{1.4}
\]
Thus a complete \(B\)-row family has
\(\sum_S\mu_q^{\mathcal R}(S)=nB=W\), while a partial family of
\(B-R\) rows has mass \(n(B-R)\). We abbreviate
\(O_q(\mathcal R)=O_q(\mu_q^{\mathcal R})\) for a complete family.

For an integer histogram \(x\) of total mass \(W\), define
\[
                         H_b(x)=\sum_S(x(S)-b(S))_+,  \tag{1.5}
\]
\[
                         O_q(x)=\min_{b\in\mathcal B_q}H_b(x).          \tag{1.6}
\]

### Lemma 1.1 (exact mobile-ceiling formula)

Let
\[
 K_{c_q}(x)=\sum_S(x(S)-c_q)_+,\qquad
 t_q(x)=|\{S:x(S)\ge c_q+1\}|.
\]
Then
\[
 \boxed{
 O_q(x)=K_{c_q}(x)-\min\{\rho_q,t_q(x)\}
       =\frac12\operatorname {dist}_1(x,\mathcal B_q).}               \tag{1.7}
\]

#### Proof

Starting from the constant floor \(c_q\), assigning a ceiling quota to a
target with \(x(S)\ge c_q+1\) removes exactly one unit of positive excess.
Assigning it elsewhere removes none. The \(\rho_q\) ceiling slots must be
assigned to distinct targets, so the maximum reduction is
\(\min\{\rho_q,t_q(x)\}\). This proves the first equality.

For every \(b\in\mathcal B_q\), \(x\) and \(b\) have equal total mass.
Their positive and negative discrepancies are equal, hence
\[
                         H_b(x)=\frac12\|x-b\|_1.
\]
Minimization gives the second equality. \(\square\)

In particular,
\[
 O_q(x)\ne\bigl(K_{c_q}(x)-\rho_q\bigr)_+             \tag{1.8}
\]
in general: a large excess concentrated in one target can use only one
ceiling slot. The PCap positive-floor formula cannot be transferred to
MWB by changing the cap symbol.

For fixed \(A\), put
\[
 H_A=\lceil A\sqrt m\rceil,\qquad
 S_A(m)=\sum_{q=1}^{H_A}\frac1{c_q}.                  \tag{1.9}
\]
The exact ratio
\[
 \frac W{N_q}
 =\prod_{i=1}^q\frac{m+1+i}{m-q+i}
\]
gives, uniformly for \(q\le H_A\),
\[
 \log\frac W{N_q}=\frac{q(q+1)}m+O_A(m^{-1/2}).       \tag{1.10}
\]
Therefore
\[
                         1\le c_q\le C_A,\qquad
                         S_A(m)=\Theta_A(\sqrt m).     \tag{1.11}
\]

## 2. The fixed-quota carrier derivative

Fix a depth \(q\). Write the old physical histogram as
\[
                         \mu_q=\beta_q+u_q,            \tag{2.1}
\]
where \(\beta_q\) is the unaffected background and \(u_q\) is the complete
old histogram of the slots changed by one fully assembled serial
conveyor. Let \(D_q\) be its complete new-minus-old physical histogram.

For \(b\in\mathcal B_q\), put
\[
                         \kappa_{q,b}(S)=(b(S)-\beta_q(S))_+.           \tag{2.2}
\]
Define
\[
 R_{q,b}=
 \sum_{D_q(S)<0}
 \min\{-D_q(S),(u_q(S)-\kappa_{q,b}(S))_+\},           \tag{2.3}
\]
\[
 A_{q,b}=
 \sum_{D_q(S)>0}
 \min\{D_q(S),(u_q(S)+D_q(S)-\kappa_{q,b}(S))_+\}.     \tag{2.4}
\]

### Proposition 2.1 (weighted-quota carrier identity)

For every fixed balanced quota,
\[
 \boxed{
 H_b(\mu_q+D_q)-H_b(\mu_q)=A_{q,b}-R_{q,b}.}          \tag{2.5}
\]
After allowing the ceiling positions to move,
\[
 \boxed{
 O_q(\mu_q+D_q)
 =\min_{b\in\mathcal B_q}
 \bigl[H_b(\mu_q)+A_{q,b}-R_{q,b}\bigr].}             \tag{2.6}
\]

#### Proof

For nonnegative \(\beta,u\) and integer quota \(b\),
\[
 (\beta+u-b)_+
 =(\beta-b)_+ +(u-(b-\beta)_+)_+.                    \tag{2.7}
\]
The first term is unchanged by the conveyor. If \(D_q(S)=-d<0\), the
second hinge falls by
\[
                         \min\{d,(u_q(S)-\kappa_{q,b}(S))_+\};
\]
if \(D_q(S)=d>0\), it rises by
\[
                         \min\{d,(u_q(S)+d-\kappa_{q,b}(S))_+\}.
\]
Summing proves (2.5); minimizing the final expression over the mobile
quota set proves (2.6). \(\square\)

There is no cap \(n\), no PCap baseline \(W-N_q\), and no active/inactive
outer positive part in (2.5)--(2.6). A useful conveyor must make the final
weighted quantity (0.1) \(o_A(W)\), not merely decrease it strictly.

## 3. Exact serial composition and the complete carrier

Consider a bundle passing through twisted slabs
\(S_1,\ldots,S_k\). The \(i\)-th local factor joins port \(P\) to the
complement of \(\tau_i(P)\). Let \(\alpha_i\) be the literal label chart
implemented by the unchanged connector from slab \(i\) to slab \(i+1\).
Every slab in this section is assumed to have a literal ambient
geodesic realization, including whatever exterior motion is needed by
the fixed-exterior obstruction; an abstract two-shore path ledger is not
such a realization.
After transporting all labels to the first port set, write
\[
 \widehat\tau_i=A_i^{-1}\tau_iA_i,\qquad
 A_1=1,\quad A_i=\alpha_{i-1}\cdots\alpha_1,           \tag{3.1}
\]
and define the cumulative transported tail permutation by
\[
 T_0=1,\qquad T_i=\widehat\tau_iT_{i-1}.              \tag{3.2}
\]
Let \(\gamma_{\rm out}\) be the terminal literal chart from the last exit
frame back to the initial closing frame, transported to the first port
set, and put
\[
                    \operatorname {Mon}=\gamma_{\rm out}T_k.          \tag{3.3}
\]

### Proposition 3.1 (serial legality conditions)

The reassembled bundle consists of literal closed rows with exact middle
ownership provided:

1. every local twisted factor partitions its complete \(X\)- and
   \(Y\)-resource shores;
2. every connector, seam, and crossing collar has exactly one owner;
3. the transported final monodromy is
   \[
                             \operatorname {Mon}=1;                   \tag{3.4}
   \]
4. for every entering label \(P\), the sum of the transported local and
   connector lengths equals the prescribed cylinder length.

Intermediate open twisted bundles need not themselves be global exact
factors.

#### Proof

Each local factor uses its two shores exactly and merely permutes outgoing
tails. The literal connectors then route every tail into one next entrance
and exhaust their stated seam resources. Thus all local and seam ledgers
are exact. Condition (3.4) returns every initial label to its original
closing tail, while the rowwise length equation makes every closed row a
cyclic order of the required common length. Exact middle ownership and
the common prescribed odd length then give literal wreaths: each row is
the minimum odd cycle of interval middle sets determined by its cyclic
coordinate order. \(\square\)

If the terminal closing chart is the identity, (3.4) reduces to
\(T_k=1\). Omitting \(\gamma_{\rm out}\) is otherwise an incorrect
monodromy test.

Monodromy one is only a closure theorem. The shallow carrier must be
computed from the final literal words.

Let \(\Pi_P^0\) and \(\Pi_P\) be the baseline and final cyclic coordinate
orders of one reassembled bundle, including every connector. Define its
authoritative depth-\(q\) carrier by
\[
 \boxed{
 \Delta_q=
 \sum_{P,h}
 \left(
 e_{I_{\Pi_P}(h,m-q)}
 -e_{I_{\Pi_P^0}(h,m-q)}
 \right).}                                            \tag{3.5}
\]
It has total mass zero.

Let \(\mathscr A_\Gamma\) be the finite activity set consisting of every
changed slab, connector, collar, and transported-tail dependency of the
assembled conveyor. Pair each final pointed window
\(\omega=(P,h)\) with the baseline window having the same root and
start. Define \(J(\omega)\subseteq\mathscr A_\Gamma\) from **both**
members of this pair, and include every activity region on which either
word segment depends. Thus, by definition,
\[
                  J(\omega)=\varnothing
          \quad\Longrightarrow\quad
 I_{\Pi_P}(h,m-q)=I_{\Pi_P^0}(h,m-q).                \tag{3.6}
\]
This enlarged activity set is necessary because a transported suffix can
change a later window which meets no locally toggled slab position.
Partitioning paired occurrences now gives the exact identity
\[
 \boxed{
 \Delta_q=
 \sum_{\varnothing\ne I\subseteq\mathscr A_\Gamma}
                         \Xi_{I,q},}                  \tag{3.7}
\]
where \(\Xi_{I,q}\) is the signed sum over windows with
\(J(\omega)=I\). This is a partition of occurrences, not an
inclusion--exclusion formula. The omitted empty class is zero term by
term by (3.6).

Some singleton terms in (3.7) are physically transported isolated stage
carriers. The other terms include connector-only, noncovariant
singleton, transported-suffix, and genuinely mixed crossing-window
effects. Resource-disjoint slab interiors do not make these vanish.

### Corollary 3.2 (correct scope of the orbit norm)

For \(d\) coherent copies of one order-\(d\) twist, suppose the complete
physical charts act by permutations of the target cells and every
affected paired occurrence is assigned exactly once to covariant stage
carriers forming one \(\tau\)-orbit. Then
\[
 \boxed{
 \Delta_q=N_\tau\delta_q,\qquad
 N_\tau=1+\tau+\cdots+\tau^{d-1}.}                    \tag{3.8}
\]
If a target-cell permutation action and a candidate covariant stage
carrier \(\delta_q\) are defined but the once-only assignment fails, the
exact formula is
\[
                         \Delta_q=N_\tau\delta_q+\Xi_q^{\rm rem}.     \tag{3.9}
\]
Here, in full generality,
\(\Xi_q^{\rm rem}:=\Delta_q-N_\tau\delta_q\); the occurrence partition
identifies it as the aggregate of all connector-only, noncovariant,
transported-tail, multiply active, or otherwise unassigned terms.
If no literal target-cell action exists, \(N_\tau\delta_q\) is not
defined and (3.7), rather than an orbit formula, is authoritative.
Consequently
\[
 \|\Delta_q\|_1
 \le d\|\delta_q\|_1+\|\Xi_q^{\rm rem}\|_1.          \tag{3.10}
\]

#### Proof

After \(j\) stages the assigned covariant carrier is transported by
\(\tau^j\), giving \(N_\tau\delta_q\). Equation (3.7) contains every
unassigned occurrence; their aggregate is \(\Xi_q^{\rm rem}\), proving
(3.9). Under the exact assignment hypothesis the remainder vanishes,
proving (3.8). The transported action is an \(L^1\)-isometry because it
permutes literal target cells, so the triangle inequality gives (3.10).
\(\square\)

Thus \(\tau^d=1\) does not imply carrier cancellation. A
\(\tau\)-invariant carrier adds \(d\)-fold, while a zero-orbit-sum carrier
cancels. Equal cyclic orientation alone proves neither condition.

## 4. A nonvacuous serial-conveyor theorem

Fix once and for all a standard Catalan root set \(D_m\), of cardinality
\(B\). For fixed \(A\), a **nonvacuous serial-conveyor certificate**
consists of:

1. A scale
   \[
              1\le s=s_A(m)\le m,\qquad s_A(m)\longrightarrow\infty.  \tag{4.1}
   \]
2. A set \(G\subseteq D_m\) and a partial family
   \(\mathcal M=\{\Pi_P:P\in G\}\) of \(|G|=B-R\) literal global cyclic
   rows whose middle windows are pairwise disjoint, with the distinguished
   infinity cut of \(\Pi_P\) giving the rooted global path
   \(P\longrightarrow[2m]\setminus P\).
3. A set of at least \(\delta_A B\) distinct rows of \(\mathcal M\),
   where \(\delta_A>0\) is independent of \(m\), which are genuinely
   traversed by a nonidentity \(D_s\)-twisted packet and have a
   noncosmetic final serviced-depth change: if \(\mu_{q,P}\) and
   \(\mu^0_{q,P}\) are their individual row histograms, then
   \[
      \sum_{q\le H_A}\|\mu_{q,P}-\mu^0_{q,P}\|_1>0.                  \tag{4.2}
   \]
4. For every active bundle, all conditions of Proposition 3.1, including
   transported monodromy and rowwise length, and the complete final
   carrier (3.5), including (3.7).
5. One integral rooted completion
   \(\mathcal C=\{\Pi_P:P\in D_m\setminus G\}\) of \(R\) rows such that
   \[
                         F=\mathcal M\mathbin{\dot\cup}\mathcal C       \tag{4.3}
   \]
   is one exact middle wreath factor.

The lower bound in item 3 counts distinct global rows, not overlapping
local packet incidences.

### Theorem 4.1 (exact final weighted-quota normal form)

Assume a nonvacuous serial-conveyor certificate and balanced quotas
\(b_q\in\mathcal B_q\), one at each \(q\le H_A\), for which
\[
 \boxed{
 \sum_{q\le H_A}\frac1{2c_q}
 \left\|
 \mu_q^{\mathcal M}+\mu_q^{\mathcal C}-b_q
 \right\|_1=o_A(W).}                                  \tag{4.4}
\]
Then
\[
 \boxed{
 \sum_{q\le H_A}\frac{O_q(F)}{c_q}=o_A(W).}           \tag{4.5}
\]

#### Proof

The serial hypotheses and exact completion make \(F\) one literal exact
factor. Its depth-\(q\) histogram and \(b_q\) both have mass \(W\), so
\[
 \frac12\|\mu_q^F-b_q\|_1
       =\sum_S(\mu_q^F(S)-b_q(S))_+.
\]
The minimum defining \(O_q(F)\) is no larger than this exhibited-quota
value. Multiply by \(1/c_q\), sum, and apply (4.4). \(\square\)

Minimizing the left side of (4.4) over the quota vectors gives exactly
\(\mathfrak Q_A(F)\) in (0.1). Thus (0.1) is the weakest exact
floor-aware final carrier gauge. Condition (4.4) is not a separate hole
surrogate.

Accordingly Theorem 4.1 is an exact normal form, not by itself a new
estimate: after quota minimization its hypothesis is fixed-window MWB.
Its value is to identify what a serial construction must estimate and to
exclude hole control as a substitute. The independently checkable
constructive implication is Theorem 7.1 below.

The positive-density and growing-scale clauses are structural
nonvacuity conditions; the proof of (4.4) does not manufacture them.
They prevent Theorem 4.1 from being satisfied by
\(\mathcal M=\varnothing,\mathcal C=F\).

## 5. The exact carrier-plus-completion decomposition

Fix \(q\) and \(b_q\in\mathcal B_q\). Define the final conveyor-core
exceedance
\[
 \operatorname {Car}_{q,b_q}(\mathcal M)
 =\sum_S(\mu_q^{\mathcal M}(S)-b_q(S))_+,             \tag{5.1}
\]
the nonnegative residual capacity
\[
 r_{q,b_q}(S)=(b_q(S)-\mu_q^{\mathcal M}(S))_+,       \tag{5.2}
\]
and the completion spill
\[
 \operatorname {Spill}_{q,b_q}(\mathcal C\mid\mathcal M)
 =\sum_S\left(\mu_q^{\mathcal C}(S)-r_{q,b_q}(S)\right)_+.
                                                               \tag{5.3}
\]

### Theorem 5.1 (exact final overload decomposition)

For every core, completion, and balanced quota,
\[
\boxed{\begin{aligned}
 H_{b_q}(\mu_q^F)
 ={}&
 \operatorname {Car}_{q,b_q}(\mathcal M)\\
 &+\operatorname {Spill}_{q,b_q}(\mathcal C\mid\mathcal M).
\end{aligned}}                                        \tag{5.4}
\]
Consequently
\[
\boxed{
 \sum_{q\le H_A}\frac{O_q(F)}{c_q}
 =
 \sum_{q\le H_A}\frac1{c_q}
 \min_{b_q\in\mathcal B_q}
 \left[
 \operatorname {Car}_{q,b_q}
 +\operatorname {Spill}_{q,b_q}
 \right].}                                            \tag{5.5}
\]
Equivalently, defining
\[
 \mathcal E_A(\mathcal M,\mathcal C)
 =
 \sum_{q\le H_A}\frac1{c_q}
 \min_{b_q\in\mathcal B_q}
 \left[
 \operatorname {Car}_{q,b_q}(\mathcal M)
 +\operatorname {Spill}_{q,b_q}(\mathcal C\mid\mathcal M)
 \right],
                                                               \tag{5.5a}
\]
one has the exact equality
\[
                    \boxed{\mathcal E_A(\mathcal M,\mathcal C)
                           =\mathfrak Q_A(F).}         \tag{5.5b}
\]

#### Proof

The scalar identity
\[
 (x+y-b)_+
 =(x-b)_+ +(y-(b-x)_+)_+                             \tag{5.6}
\]
holds in the two cases \(x\ge b\) and \(x<b\). Apply it with
\(x=\mu_q^{\mathcal M}(S)\), \(y=\mu_q^{\mathcal C}(S)\), and sum over
targets to prove (5.4). Minimizing over \(\mathcal B_q\), dividing by
\(c_q\), and summing proves (5.5). Definitions (0.1) and (5.5a) then
turn (5.5) into (5.5b). \(\square\)

Equations (5.5), (5.5a), and (5.5b) are the exact answer to the relative
carrier-and-completion question for a fixed split.

* The canonical minimum final gauge is
  \(\sum_q\operatorname {dist}_1(\mu_q^F,\mathcal B_q)/(2c_q)\).
* For a chosen core/completion split and a common chosen quota, (5.1) is
  its core exceedance and (5.3) is its exact residual completion spill.
* Their **quota-minimized sum**, weighted by \(1/c_q\), is exactly the
  final overload and must be \(o_A(W)\).

The two summands are not individually canonical minima: both depend on
the split and on the same quota. Neither is a norm of an isolated signed
carrier. A nonzero
carrier may move one balanced quota vector to another and have zero final
cost, while a small carrier can be harmful on a saturated background.
In particular, along any sequence of nonvacuous certificates, the
quota-minimized weighted Car+Spill expression is \(o_A(W)\) if and only
if the resulting factors satisfy fixed-window MWB.

### Corollary 5.2 (quota-safe core)

Suppose, for every \(q\le H_A\), some balanced quota dominates the final
core:
\[
                         \mu_q^{\mathcal M}\le b_q.    \tag{5.7}
\]
Put
\[
                         s_q=b_q-\mu_q^{\mathcal M}\ge0.              \tag{5.8}
\]
Then \(\operatorname {Car}_{q,b_q}=0\), and
\[
 \boxed{
 H_{b_q}(\mu_q^F)
 =\sum_S(\mu_q^{\mathcal C}(S)-s_q(S))_+
 =\frac12\|\mu_q^{\mathcal C}-s_q\|_1.}               \tag{5.9}
\]

#### Proof

The first equality is (5.4). Both \(s_q\) and
\(\mu_q^{\mathcal C}\) have total mass \(nR\), because the core has
\(B-R\) rows. Their positive discrepancy is therefore half their
\(L^1\)-distance. \(\square\)

Thus the exact quota-safe completion condition is
\[
 \boxed{
 \sum_{q\le H_A}\frac1{c_q}
 \sum_S(\mu_q^{\mathcal C}(S)-s_q(S))_+=o_A(W).}      \tag{5.10}
\]
A larger completion is allowed whenever (5.10) is proved directly.

### Corollary 5.3 (universal row-count envelope)

For an arbitrary completion of \(R\) rows,
\[
 \operatorname {Spill}_{q,b_q}\le
                         \sum_S\mu_q^{\mathcal C}(S)=nR.              \tag{5.11}
\]
Hence a quota-safe conveyor core has harmless arbitrary completion if
\[
                         R S_A(m)=o_A(B),              \tag{5.12}
\]
or, equivalently,
\[
 \boxed{
 R=o_A(B/\sqrt m)
  =o_A\!\left(\frac{W}{n\sqrt m}\right).}             \tag{5.13}
\]
There is no extra factor two: the raw \(L^1\)-distance in (5.9) is at
most \(2nR\), and overload is half that distance.

The rate (5.13) is the universal bound obtainable from the number of
uncontrolled rows alone, not a necessity theorem for structured literal
completions.

## 6. What an isolated carrier norm can and cannot prove

Let \(F^0\) be the baseline partial row family and let
\(\Delta_q=\mu_q^{\mathcal M}-\mu_q^{F^0}\) be the complete final
serial carrier from (3.5). Complete the same baseline roots by the same
rooted family \(\mathcal C\). When this is also an exact completion of
\(F^0\), write
\[
                       \widetilde F^0=F^0\mathbin{\dot\cup}\mathcal C.
                                                               \tag{6.1}
\]
If the stage carriers are separated into an exactly assigned covariant
part and the remainder from (3.9), then
\[
 \|\Delta_q\|_1
 \le \sum_{\text{stages }i}\|\delta^{\rm cov}_{i,q}\|_1
       +\|\Xi_q^{\rm rem}\|_1.                       \tag{6.2}
\]
The remainder must include connector-only, noncovariant singleton,
transported-tail, and mixed-window terms; resource-disjointness alone
does not remove it.

The correct baseline comparison is
\[
 \operatorname {dist}_1(\mu_q^F,\mathcal B_q)
 \le
 \operatorname {dist}_1(\mu_q^{\widetilde F^0},\mathcal B_q)
 +\|\Delta_q\|_1.                                    \tag{6.3}
\]
Indeed distance to a fixed set is \(1\)-Lipschitz. Equivalently, for the
two full \(B\)-row families,
\[
 |O_q(F)-O_q(\widetilde F^0)|
                         \le\frac12\|\Delta_q\|_1.     \tag{6.4}
\]
Therefore
\[
 \sum_{q\le H_A}\frac{\|\Delta_q\|_1}{2c_q}=o_A(W)    \tag{6.5}
\]
is sufficient to preserve fixed-window MWB of an already MWB comparison
factor. It is not
an implication from an arbitrary baseline to balance: (6.3) retains the
baseline mismatch term. The minimum final quantity remains (0.1) or,
relative to a nonvacuous core and completion, (5.5).

Thus
\[
                    \|\Delta\|_{{\rm pres},A}
       :=\sum_{q\le H_A}\frac{\|\Delta_q\|_1}{2c_q}    \tag{6.6}
\]
is a universal **preservation norm**. It is not the minimum constructive
carrier gauge; that gauge is the background-dependent final distance
\(\mathfrak Q_A\). No norm of \(\Delta\) alone can distinguish a harmless
permutation of mobile ceiling positions from a harmful move into a
saturated target.

A bound only at the deepest depth is insufficient. Exact \(X/Y\)
ownership and identity monodromy give no interpolation among the
\(\Theta_A(\sqrt m)\) shallow histograms.

## 7. The clean nonvacuous theorem sufficient for constant one

### Theorem 7.1 (serial twisted near-completion implies MWB)

Assume that, for every fixed positive integer \(A\) and all sufficiently
large \(m\), there is a nonvacuous serial-conveyor certificate satisfying:

1. the final core is quota-safe through \(H_A\);
2. its one exact rooted completion has
   \[
                         R=o_A(B/\sqrt m).             \tag{7.1}
   \]

Then fixed-window MWB holds for every \(A\). Consequently there are
\(\omega(m)\to\infty\), with
\[
 H_m=\lceil\sqrt m\,\omega(m)\rceil=o(m),
\]
and exact factors \(F_m\) satisfying
\[
                         \sum_{q\le H_m}\frac{O_q(F_m)}{c_q}=o(W).
                                                               \tag{7.2}
\]
Hence
\[
 \boxed{
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.}        \tag{7.3}
\]

#### Proof

Corollary 5.3 gives
\[
 \sum_{q\le H_A}\frac{O_q(F_{A,m})}{c_q}
 \le nR S_A(m)=o_A(W)                                 \tag{7.4}
\]
for each fixed \(A\).

Choose thresholds \(T_j\ge j^8\) such that the normalized cost in (7.4)
is at most \(1/j\) whenever \(m\ge T_j\), and put
\[
 a(m)=\max\{j:T_j\le m\},\qquad
 H_m=\lceil a(m)\sqrt m\rceil.
\]
Then \(a(m)\to\infty\), \(a(m)\le m^{1/8}\), and
\(H_m\le m^{5/8}+1=o(m)\). Choosing the single factor for the
\(a(m)\)-window proves (7.2).

For completeness, every missing depth-\(q\) target costs at least \(c_q\)
units of balanced underload, so
\[
                         M_q(F_m)\le O_q(F_m)/c_q.
\]
Thus the total central-band hole repair is \(o(W)\). The literal wreath
block has seam cost \(O(H_mW/m)=o(W)\), while the product-SCD word covers
both outer tails in \(o(W)\) because \(H_m/\sqrt m\to\infty\).
This gives \(\nu(2m+1)\le W+o(W)\). The standard one-coordinate lift
and the width lower bound give (7.3) in both parities. \(\square\)

The more general structured-spill hypothesis (5.5) also implies Theorem
7.1's conclusion and permits \(R\) larger than (7.1). The small-leave
form is simply the strongest conclusion available without using any
structure of the completion rows.

## 8. Adversarial audit and precise open boundary

The following points are load-bearing.

1. **Transported monodromy.** The product uses the literal connector
   charts, not the product of locally written permutations.
2. **Length is separate.** Identity monodromy does not repair unequal
   row lengths. Strict paths or an audited orbit-length equation are
   required.
3. **Exact seams are separate.** Abstract row-name reconnection does not
   own connector states or crossing OR colours.
4. **Mixed carriers are compulsory.** A protected interval may meet two
   resource-disjoint slabs. The orbit norm is exact only under the
   exact occurrence-assignment hypothesis of Corollary 3.2; otherwise
   (3.7)--(3.9) are authoritative.
5. **Mobile quotas are compulsory.** Formula (1.7), not a PCap floor,
   describes balanced overload. The high-quota positions may change with
   the final histogram.
6. **The final factor is common across depths.** Twists, charts,
   completion, and active rows cannot be chosen separately for different
   \(q\). Only the balanced quota vector may vary with \(q\).
7. **Positive density is literal.** It counts distinct global rows
   genuinely altered by nonidentity packets, not overlapping local
   incidences.
8. **No hole surrogate.** Small hole count or cap-\(n\) PCap gives no
   bound on (0.1).
9. **No cosmetic nonvacuity.** Inverse packet pairs which return every
   serviced row profile to baseline do not satisfy (4.2).
10. **The isolated carrier norm is preservative only.** Inequality
   (6.3) carries along the mismatch of the completed baseline; it cannot
   create balanced quotas from an arbitrary one.
11. **Physical realizability precedes algebra.** The local twist order
   must fit a literal ambient geodesic, including exterior displacement,
   exact collars, and the terminal closure chart. Abstract port
   monodromy alone supplies none of these.

The Catalan first-edge data from the prior PCap carrier note remain exact,
as does the instruction to sum physical collisions before applying a
hinge. Its cap-\(n\) thresholds do not transfer. On a fixed Gaussian
window \(c_q\le C_A\), while an almost-uniform local histogram
\(\operatorname {Cat}_s/(2s)\) grows without bound. Balancing mass among
only \(2s\) local labels therefore does not make it quota-safe; the
conveyor must create many distinct physical exterior targets or remove
existing balanced overload.

The exact unproved alternatives are now:

> **Structured serial theorem.** Construct the nonvacuous positive-density
> serial bank of Section 4 and prove the final carrier-plus-spill bound
> (5.5).

or the cleaner stronger statement:

> **Quota-safe serial near-factor.** Construct such a bank on a near-full
> rooted core, quota-safe through every fixed Gaussian window, with one
> exact completion leaving \(o_A(\operatorname {Cat}_m/\sqrt m)\) rows.

The ballot-forced alternating-cycle bank gives only local degree-factor
certificates. It does not prove strand admissibility, coherent serial
placement, the complete mixed carrier tensor, or either weighted-quota
bound above. Therefore coefficient one remains unproved.

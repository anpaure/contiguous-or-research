# Calibrated top packets: the OWNER near-transversal nibble

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N=\binom{2m}{m-H},\qquad M=m+H,
\]

where (H) is the least positive integer for which

\[
 \lambda_H:=\frac WN\ge M.
\]

Then (H=(1+o(1))\sqrt{m\log m}), and, with

\[
 \rho=\frac{MN}{W}=\frac{M}{\lambda_H},
\]

one has

\[
 \rho=1-O(H/m),\qquad MN=\rho W=W-o(W).                 \tag{0.1}
\]

For a top (U\in\binom{[2m]}M), let a column be a directed cyclic order
of (U), modulo rotation, and let its owner packet be its (M) cyclic
(m)-windows.  The tagged column hypergraph has tag degree

\[
 D=(M-1)!                                                        \tag{0.2}
\]

and owner degree (D_0=\rho D).  Its maximum relative owner codegree is
(2/m^2).

This note proves three further assertions.

1. There is an entirely elementary one-bite matching of
   
   \[
    \left(\frac12-o(1)\right)\frac NM
   \]
   
   packets.  More generally, a bite of intensity (0<\theta\le1) has
   size at least
   
   \[
    \left(\theta-\frac{\rho\theta^2}{2}\right)\frac NM.          \tag{0.3}
   \]

2. After contracting the one-choice-per-top fibres, the complete
   cross-top factorial overlap hierarchy is subcritical.  For every packet
   (P), define
   
   \[
    \Psi_j(P)=\frac1{D_0}
      \sum_{F:\,\operatorname{top}(F)\ne\operatorname{top}(P)}
      \binom{|P\cap F|}{j}.
   \]
   
   Then, uniformly for (2\le j\le H),
   
   \[
    \boxed{
    \Psi_j(P)\le(1+o(1))
       \frac{M j!}{\binom m{j-1}^{2}},}                          \tag{0.4}
   \]
   
   while \(\Psi_j(P)=0\) for (j>H).  Consequently
   
   \[
    \boxed{
    \max_{2\le j\le H}\Psi_j(P)^{1/(j-1)}
       \le C\frac{H^3}{m^2}
       =O\!\left(\frac{\log^{3/2}m}{\sqrt m}\right)=o(1).}       \tag{0.5}
   \]

3. A single explicit dynamic lemma now suffices.  It is a
   chronology-sensitive link-flatness assertion for the uniform
   available-packet random greedy process, stated in Section 6.  At the
   stopping density \(\eta=1/\log m\), it would give a matching of
   
   \[
    (1-\eta-o(1))N=(1-o(1))N                                      \tag{0.6}
   \]
   
   packets.  Hence the omitted packet count would be (o(N)=o(W/m)),
   the packets would cover (W-o(W)) owners, and all reset and literal
   repair costs would be (o(W)).

The dynamic lemma is **not proved here**.  The static hierarchy (0.4) is
the correct input, but it does not by itself justify adaptive iteration.
Section 7 gives the exact failed bounded-difference estimate and two
packet-free dense residuals which rule out replacing link-flatness by
density or fixed-order marginal balance.  Thus this route does not yet
prove coefficient one.

## 1. The tagged packet hypergraph

For a directed cyclic order

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

of a top (U), put

\[
 P(U,\pi)=\{X_t:t\in\mathbb Z_M\},\qquad
 X_t=\{u_t,u_{t+1},\ldots,u_{t+m-1}\}.              \tag{1.1}
\]

Cyclic rotations of \(\pi\) are identified; reversal is retained.  A
tagged column is

\[
 e(U,\pi)=\{\tau_U\}\cup P(U,\pi).                  \tag{1.2}
\]

Every column has one tag and (M) owners.  There are (D=(M-1)!)
columns above a fixed tag.  A fixed owner lies in

\[
 D_0=\binom mH m!H!=\rho D                           \tag{1.3}
\]

columns.  We use the already audited owner-pair census

\[
 \frac{d(X,Y)}{D_0}=\frac2{\binom mq^2}
 \quad(1\le q<H),                                    \tag{1.4}
\]

where (q=|X-Y|=|Y-X|); the (q=H) value is

\[
 \frac{m-H+1}{\binom mH^2},                          \tag{1.5}
\]

and the codegree is zero for (q>H).

Two packets on distinct tops meet in at most (H) owners.  Indeed, if
(U,V) differ in (d\ge1) elements on each side, a common owner has in
(U) a complementary cyclic (H)-interval containing the fixed
(d)-set (U-V), and there are at most (H-d+1\le H) such intervals.

The column degree is not being inflated by an arbitrary parametrization.
For \(H\ge2\), the Johnson-distance-one graph induced by the owners of one
packet is exactly \(C_M\): two packet owners have distance one exactly when
their cyclic starts are adjacent.  Hence the unordered owner support
recovers its cyclic owner order up to direction.  Along an oriented owner
edge, the unique removed and inserted coordinates recover the cyclic
coordinate order.  Every unlabelled owner support therefore has exactly
two directed presentations, related by reversal.

## 2. An unconditional alteration bite

For every top (U), choose a packet uniformly from its (D) columns.
For an owner (X), write

\[
 p_{U,X}=\Pr(X\in P(U,\pi)).                         \tag{2.1}
\]

Thus (p_{U,X}=0) unless (X\subset U), and otherwise

\[
 p_{U,X}=\frac{m!H!}{D}=\frac{M}{\binom MH}.         \tag{2.2}
\]

The total load at every owner is

\[
 \ell_X:=\sum_U p_{U,X}=\frac{D_0}{D}=\rho.         \tag{2.3}
\]

### Theorem 2.1 (one sparse alteration bite)

For every fixed (0<\theta\le1), the tagged packet hypergraph has a
matching of at least

\[
 \boxed{
 \left(\theta-\frac{\rho\theta^2}{2}\right)\frac NM}             \tag{2.4}
\]

columns.  In particular, at \(\theta=1\) it has a matching of

\[
 \left(\frac12-o(1)\right)\frac NM.                \tag{2.5}
\]

#### Proof

Activate every top independently with probability

\[
 q=\frac\theta M,                                   \tag{2.6}
\]

and, at every activated top, choose one uniform packet.  Let (A) be
the number of activated tops.  Join two activated tops in a collision
graph if their chosen packets share an owner, and let (C) be the number
of edges of this graph, counted once even if the two packets share several
owners.  Then

\[
 \mathbb EA=qN=\frac{\theta N}{M}.                  \tag{2.7}
\]

For each owner (X), the expected active load contributed by top (U)
is (q p_{U,X}).  A union bound over owners gives

\[
\begin{aligned}
 \mathbb EC
 &\le q^2\sum_X\sum_{U<V}p_{U,X}p_{V,X}\\
 &\le\frac{q^2}{2}\sum_X\left(\sum_U p_{U,X}\right)^2\\
 &=\frac{q^2}{2}W\rho^2
  =\frac{\rho\theta^2}{2}\frac NM,                \tag{2.8}
\end{aligned}
\]

where (W\rho=MN) was used last.

Every finite graph has an independent set of size at least its number of
vertices minus its number of edges: delete one endpoint of each edge.
Thus the chosen packets contain a matching of size at least (A-C).
Taking expectations in (2.7)--(2.8), some outcome has an independent set
of size at least (2.4). \(\square\)

This proof is valid for the growing packet size.  It is an alteration
calculation, not an invocation of a fixed-rank nibble theorem.

## 3. The isolated-column version of one bite

The preceding constant can also be obtained by marking columns directly.
This form records the exact conflict-neighbourhood estimate needed by a
semi-random iteration.

For a column (e), let \(\Gamma[e]\) be the set of columns meeting it in
at least one tag or owner.  Put

\[
 \Lambda=D+MD_0=D(1+M\rho).                         \tag{3.1}
\]

The sum of owner-pair codegrees over the (M) owners of one packet is

\[
 \frac1{D_0}\sum_{\{X,Y\}\subset P}d(X,Y)
   =\frac{2+o(1)}m.                                 \tag{3.2}
\]

The sum of its tag-owner codegrees, divided by (D), is

\[
 M\frac{m!H!}{D}=\frac{M^2}{\binom MH}=o(m^{-A})    \tag{3.3}
\]

for every fixed (A).  Bonferroni therefore gives, uniformly in (e),

\[
 \boxed{
 \Lambda-O(D/m)\le |\Gamma[e]|\le\Lambda.}         \tag{3.4}
\]

Mark every column independently with probability

\[
 p=\frac\theta\Lambda                               \tag{3.5}
\]

and retain a marked column only if no other marked column meets it.  The
retained columns form a matching, and (3.4) gives

\[
\begin{aligned}
 \mathbb E|\mathcal B|
 &=ND\,p(1-p)^{|\Gamma[e]|-1}\\
 &=\left(\theta e^{-\theta}+o(1)\right)\frac NM.    \tag{3.6}
\end{aligned}
\]

Thus (3.6) is a second, fully rigorous one-round nibble estimate.  It does
not justify repeating the round on the induced residual system.

## 4. The exact cross-top factorial hierarchy

The raw hypergraph has large high-order links inside one top: two nearby
cyclic orders on the same top can share (M-O(1)) owners.  Those links are
irrelevant to a grouped process which makes at most one choice at each top.
The right statistic sums only over a different top.
All span assertions below are for sufficiently large \(m\), when
\(H<M/2\).

Fix a packet (P=P(U,\pi)), and for (j\ge2) define

\[
 \Psi_j(P)=\frac1{D_0}
 \sum_{F:\,\operatorname{top}(F)\ne U}
 \binom{|P\cap F|}{j}.                              \tag{4.1}
\]

### Lemma 4.1 (common-column count for (j) owners)

Let \(\mathcal S=\{X_1,\ldots,X_j\}\) be (j) owners occurring in one
packet, and put

\[
 s=\left|\bigcup_{i=1}^jX_i\right|-m.               \tag{4.2}
\]

If (s<H), then the number of all packet columns containing
\(\mathcal S\) is at most

\[
 \boxed{
 d(\mathcal S)\le D_0\frac{j!}{\binom ms^2}.}       \tag{4.3}
\]

If (s=H), the union of the owners is their unique top; hence every
column containing \(\mathcal S\) has that same top.

#### Proof

In a containing top (V), put (Q_i=V-X_i).  These are distinct cyclic
(H)-intervals, and

\[
 \left|\bigcap_iQ_i\right|=H-s.                    \tag{4.4}
\]

When \(s<H\), the distinct starts lie in one cyclic span of length \(s\).
It contains \(j\) distinct integer positions, so \(s\ge j-1\).

When (s<H), cut the cyclic order inside their nonempty common
intersection.  For one linear order of their starts, let the positive gaps
be (g_1,\ldots,g_{j-1}), so that

\[
 \sum_{r=1}^{j-1}g_r=s.                             \tag{4.5}
\]

The membership atoms have sizes

\[
 H-s,\quad m-s,\quad g_1,g_1,\ldots,g_{j-1},g_{j-1}.
\]

Therefore the number of compatible directed cyclic orders for this start
order is at most

\[
 (H-s)!(m-s)!\prod_{r=1}^{j-1}(g_r!)^2
 \le (H-s)!(m-s)!(s!)^2.                            \tag{4.6}
\]

There are at most (j!) orders of the labelled starts.  The union in
(4.2) has size (m+s), so it lies in

\[
 \binom{m-s}{H-s}                                   \tag{4.7}
\]

tops.  Multiplying (4.6)--(4.7), and using

\[
 D_0=\frac{m!^2}{(m-H)!},
\]

gives

\[
 \frac{d(\mathcal S)}{D_0}
 \le j!\left(\frac{s!(m-s)!}{m!}\right)^2
 =\frac{j!}{\binom ms^2},                           \tag{4.8}
\]

which is (4.3).

If (s=H), (4.2) says that the owner union has size (m+H=M).
Every containing top has size (M), so it must equal this union. \(\square\)

### Theorem 4.2 (cross-top factorial overlap theorem)

Uniformly for every packet (P) and (2\le j\le H),

\[
 \boxed{
 \Psi_j(P)
 \le\sum_{s=j-1}^{H-1}
     M\binom{s-1}{j-2}\frac{j!}{\binom ms^2}
 \le(1+o(1))\frac{M j!}{\binom m{j-1}^{2}}.}       \tag{4.9}
\]

For (j>H), \(\Psi_j(P)=0\).

#### Proof

Write the owners of (P) as complements of the (M) cyclic
(H)-windows.  If (j) of their start positions have union expansion
(s<H), their starts have a unique cyclic span (s), because
(H<M/2).  Choose its first endpoint and its (j-2) interior starts.
The number of such owner (j)-sets is exactly

\[
 M\binom{s-1}{j-2}.                                 \tag{4.10}
\]

Interchanging the two sums in (4.1), applying Lemma 4.1, and observing
that the (s=H) sets have no cross-top columns gives the first inequality
in (4.9).

The ratio of the summand at (s+1) to the summand at (s) is

\[
 \frac{s}{s-j+2}\left(\frac{s+1}{m-s}\right)^2
 \le(1+o(1))\frac{H^3}{m^2}=o(1),                  \tag{4.11}
\]

uniformly on the summation range.  Hence the first term dominates and
proves the second inequality.  Finally, two packets on distinct tops meet
in at most (H) owners, so every summand in (4.1) is zero when (j>H).
\(\square\)

### Corollary 4.3 (one uniform small parameter)

There is an absolute constant (C) such that

\[
 \max_{2\le j\le H}\Psi_j(P)^{1/(j-1)}
 \le C\frac{H^3}{m^2}.                              \tag{4.12}
\]

#### Proof

Put (t=j-1).  From (4.9) and

\[
 \binom mt\ge(m/t)^t,
\]

the required root is at most

\[
 \frac{M^{1/t}(t+1)^{1+1/t}t^2}{m^2}               \tag{4.13}
\]

up to an absolute factor.  On (2\le t\le H), the function
(M^{1/t}t^3) has its maximum at an endpoint; both endpoint values are
at most (O(H^3)).  The case (t=1) follows directly from

\[
 \Psi_2(P)\le(2+o(1))M/m^2=O(1/m).
\]

This proves (4.12). \(\square\)

At the intended stopping density \(\eta=1/\log m\), (4.12) gives

\[
 \frac1\eta\max_j\Psi_j(P)^{1/(j-1)}
 =O\!\left(\frac{\log^{5/2}m}{\sqrt m}\right)=o(1). \tag{4.14}
\]

This is the precise favorable parameter which the maximum pair codegree
alone does not display.

## 5. A minimal energy form of the iterative gate

Let a partial packet matching have (T) unmatched tops and let
\(\mathcal A_U\) be the packets above an unmatched top (U) which avoid
all already used owners.  Suppose that for every such top we have a
probability distribution \(\mu_U\) supported on \(\mathcal A_U\).  Define
the residual owner loads

\[
 \ell_X=\sum_U\Pr_{P\sim\mu_U}(X\in P).             \tag{5.1}
\]

The identity

\[
 \sum_X\ell_X=MT                                    \tag{5.2}
\]

is automatic.

### Proposition 5.1 (energy-controlled bite)

If

\[
 \boxed{
 \sum_X\ell_X^2\le(1+\varepsilon_m)MT,\qquad
 \varepsilon_m=o(1),}                              \tag{5.3}
\]

then, for every (0<\theta\le1), the current matching can be extended by
at least

\[
 \boxed{
 \left(\theta-\frac{(1+\varepsilon_m)\theta^2}{2}\right)
 \frac TM}                                          \tag{5.4}
\]

packets.

#### Proof

Repeat the proof of Theorem 2.1, activating each unmatched top with
probability \(\theta/M\) and sampling from \(\mu_U\).  All sampled packets
avoid the old matching.  The expected activated count is \(\theta T/M\),
while the expected number of collision-graph edges is at most

\[
 \frac12\left(\frac\theta M\right)^2
 \sum_X\ell_X^2
 \le\frac{(1+\varepsilon_m)\theta^2}{2}\frac TM.
\]

Delete one endpoint per collision edge as before. \(\square\)

Thus (5.3), if preserved after each bite, is enough to iterate.  It is
also sharp in scale: by Cauchy--Schwarz, (MT) is the natural energy when
the available owner capacity is of order (MT).

## 6. The exact unproved dynamic lemma

The following packet-specific statement is the smallest non-tautological
link-flatness assertion isolated by this attack.

> **Dynamic link flatness \(\mathrm{DLF}(\eta)\).**  Run the random greedy
> process which, at each step, chooses uniformly from all packet columns
> whose tag and owners have not yet been used.  Put
> \[
>   x_i=1-i/N,\qquad y_i=1-Mi/W.
> \]
> With probability \(1-o(1)\), simultaneously and uniformly for
> \(i\le(1-\eta)N\), apart from \(o(N-i)\) exceptional
> unmatched tops, the available-order links satisfy
> \[
>  A_i(U;\mathcal S)
>   =(1+o(1)),d_U(\mathcal S)y_i^{M-|\mathcal S|}   \tag{6.1}
> \]
> for every compatible owner set \(\mathcal S\) needed in the
> cross-top hierarchy, with errors summable over the process.  In
> particular,
> \[
>  A_i(U)=(1+o(1))Dy_i^M,                            \tag{6.2}
> \]
> \[
>  \frac{A_i(U;X)}{A_i(U)}
>   \le(1+o(1))\frac{M}{\binom MH\,y_i},             \tag{6.3}
> \]
> and the analogous owner and cross-link degrees have the trajectories
> (D_0x_i y_i^{M-1}) and
> (d(\mathcal S)x_i y_i^{M-|\mathcal S|}).

Here (d_U(\mathcal S)) denotes the initial number of columns above (U)
containing \(\mathcal S\).  Formula (6.1) is required only for links which
can enter the crossing-blocker expansion; large same-top links are kept as
one top fibre, not treated as independent packet columns.

### Theorem 6.1 (conditional near-transversal)

If \(\mathrm{DLF}(1/\log m)\) holds, then the tagged owner hypergraph has a
matching of

\[
 \boxed{
 \left(1-\frac1{\log m}-o(1)\right)N}               \tag{6.4}
\]

packets.  It leaves (o(W/m)) top packets unused and (o(W)) owners
uncovered.

#### Proof

At every time (i\le(1-1/\log m)N), (6.2) leaves all but (o(N-i))
unmatched tops with a positive available packet count.  The total number
of available columns is therefore positive until the process reaches

\[
 i=\left(1-\frac1{\log m}-o(1)\right)N.
\]

The chosen columns are a matching by construction, proving (6.4).  The
number of omitted tops is

\[
 O(N/\log m)+o(N)=o(N)=o(W/m).                      \tag{6.5}
\]

The owner leave is

\[
\begin{aligned}
 W-Mi
 &=W-\rho W\left(1-\frac1{\log m}-o(1)\right)\\
 &=O(WH/m)+O(W/\log m)+o(W)=o(W),                   \tag{6.6}
\end{aligned}
\]

using (0.1). \(\square\)

The scalar degree at this stopping point is enormous:

\[
 \log\left(D(\log m)^{-M}\right)
 =m\bigl(\log m-\log\log m-1+o(\log m)\bigr)\to\infty. \tag{6.7}
\]

Thus degree exhaustion is not the issue.  The issue is proving the
chronology-sensitive concentration in (6.1).

## 7. Why the static hierarchy is not yet an iteration proof

Let

\[
 K=\binom MH,qquad a=m!H!=D\frac MK.                \tag{7.1}
\]

One selected packet on a different top meets at most (H) owners lying in
a fixed top (U).  Consequently one selection can change the available
order count at (U) by at most

\[
 Ha=D\frac{HM}{K}.                                  \tag{7.2}
\]

At owner density (y=1/\log m), the trajectory in (6.2) is

\[
 Dy^M=D(\log m)^{-M}.                               \tag{7.3}
\]

The ratio of the raw bounded difference (7.2) to (7.3) is

\[
 \frac{HM}{K} (\log m)^M,                           \tag{7.4}
\]

whose logarithm is

\[
 M\log\log m-\log K+O(\log m)\to+\infty,           \tag{7.5}
\]

because

\[
 \log K=\Theta\bigl(H\log(m/H)\bigr)=o(m\log\log m).
\]

Therefore Azuma or a raw Lipschitz argument on top availability cannot
prove (6.2).  One must show that the large changes in (7.2) are themselves
spread through the lower links according to (6.1).  This is precisely the
unproved propagation step; omitting it would be a false proof.

There are also deterministic warnings against replacing (6.1) by density.

### Proposition 7.1 (a dense packet-free star)

For a point (a\in[2m]), the owner family

\[
 \mathcal R_a=\{X\in\tbinom{[2m]}m:a\in X\}
\]

has size (W/2) and contains no complete packet.

#### Proof

If a packet top omits (a), none of its owners belongs to \(\mathcal R_a\).
If its top contains (a), exactly (m) of its (M) cyclic (m)-windows
contain (a), while the other (H) omit it.  In neither case is the whole
packet contained in \(\mathcal R_a\). \(\square\)

There is a stronger marginal warning on the subsequence for which
(\gcd(m,H)=1).  Fix (A\subset[2m]), \(|A|=m\), and color an owner by

\[
 \chi(X)=|X\cap A|\pmod2.                             \tag{7.6}
\]

Neither parity fibre contains a packet.  Indeed, for a cyclic order
\(u_t\) put (c_t=1_A(u_t)).  If all packet owners had the same parity,
then

\[
 0=\chi(X_{t+1})-\chi(X_t)=c_{t+m}-c_t\pmod2        \tag{7.7}
\]

for every \(t\in\mathbb Z_M\).  Since

\[
 \gcd(m,M)=\gcd(m,H)=1,
\]

the shift by \(m\) is transitive on \(\mathbb Z_M\), so all \(c_t\) are
equal.  This would force \(U\subset A\) or \(U\subset A^c\), impossible
because \(|U|=M>m\).  On the other hand, coefficient extraction from

\[
 (1-z)^m(1+z)^m=(1-z^2)^m                         \tag{7.8}
\]

shows that each parity fibre has size (W/2+e^{-\Omega(m)}W).  More
precisely, after prescribing any fixed containment/omission pattern on a
fixed coordinate set, deleting the corresponding fixed number of factors
in (7.8) shows that the two parity counts differ by
\(e^{-\Omega(m)}W\).  This is asserted only when
\(\gcd(m,H)=1\); no claim about the frequency of that arithmetic event is
needed.

Thus neither positive density nor bounded-order marginal balance prevents
a residual from being packet-free.  The common-owner chronology in
\(\mathrm{DLF}\) is essential.

## 8. Quantitative composition into the OR ledger

Suppose the conditional matching (6.4) is available.  It uses

\[
 (1-o(1))N=(1+o(1))W/m                              \tag{8.1}
\]

full promotion packets.  Cutting each packet once costs

\[
 O(HN)=O(WH/m)=o(W).                                \tag{8.2}
\]

The omitted top count is (o(W/m)), and the middle-owner leave is (6.6),
which can be appended literally at (o(W)) cost.  Thus the owner stage is
coefficient-safe.  This note does not claim the separate simultaneous
shallow-shadow balancing theorem.

## 9. Audit ledger

### Proved unconditionally

1. The alteration bite (2.4), including its exact collision-energy
   estimate.
2. The isolated-column bite (3.6), including the growing-rank
   conflict-neighbourhood estimate (3.4).
3. The common-owner count (4.3).
4. The full contracted cross-top hierarchy (4.9), its zero tail above
   (H), and the uniform parameter (4.12).
5. The residual energy-to-bite implication (5.4).
6. The quantitative implication
   \(\mathrm{DLF}(1/\log m)\Rightarrow\) a matching of
   \((1-o(1))N\) packets, with (o(W/m)) omitted packets and (o(W))
   owner leave.
7. The dense star and conditional parity-fibre obstructions to scalar or
   fixed-marginal residual arguments.

### Not proved

1. Dynamic link flatness (6.1)--(6.3).
2. Hence the requested owner near-transversal itself.
3. The later all-depth flag alignment.

The smallest live mathematical gate in this lane is no longer a generic
growing-uniformity matching theorem.  It is the packet-specific preservation
of the available-order link ratios in (6.1), with the initial cross-top
factorial hierarchy (4.9) as its exact input.  Any claimed iteration which
uses only (\Delta_2/D=2/m^2), or only the packetwise (O(1/m)) pair sum,
misses the divergence in (7.4) and is incomplete.

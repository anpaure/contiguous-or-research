# Synchronized annular repeat excess: an exact conditional SCD home compiler, deterministic phase bounds, and PBBS bundling cuts

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome and exact scope

Put

\[
 n=2m,\qquad K=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b,
\tag{0.1}
\]

\[
 \widehat N_q=\binom{2m}{m-q},\qquad
 R=m-q_0,\qquad D=H-q_0,\qquad
 N_d=\binom n{R-d}=\widehat N_{q_0+d}.
\tag{0.2}
\]

Let \(s\) literal cyclic-order packets form a matching at entrance rank
\(R\), and write

\[
 G=Ks=N_0-L,
 \qquad 0\le L\le C\frac{N_0}{\sqrt m},
\tag{0.3}
\]

where \(C\) is fixed. At every relative depth \(d\), the same packets
supply exactly \(G\) occurrences. This report proves the following.

1. If \(\mu_d\) is the depth-\(d\) target load and \(S_d\) its support,
   then the excess above the forced floor is exactly

   \[
   \boxed{
   \widetilde E_d
   =\min(G,N_d)-S_d
   =\frac12\bigl(\|\mu_d-\mathbf1\|_1-|G-N_d|\bigr).}
   \tag{0.4}
   \]

   Consequently

   \[
   \boxed{H_d=(N_d-G)_++\widetilde E_d.}
   \tag{0.5}
   \]

2. A selected entrance packet already determines its coordinate cycle up
   to reversal. Hence it determines every deeper target and every
   \(\widetilde E_d\). Rotation, orientation, or an SCD chosen after the
   packet matching cannot repair the repeat profile. A successful
   construction must choose or rethread the entrance matching itself.

3. There is an exact conditional SCD accounting theorem. For a full SCD, let
   \(A_d\) be the entrance sets whose chains extend at least \(d\) ranks
   farther downward, and let \(h_d\) be their native SCD homes. If
   \(\mathcal L\) is the entrance leave and \(F_d\) is the set of selected
   roots whose packet trace disagrees with its home, then

   \[
   \boxed{
   \widetilde E_d
   \le |\mathcal L\cap A_d|
      -\bigl(L-(N_0-N_d)\bigr)_+
      +|F_d|.}
   \tag{0.6}
   \]

   Choosing the leave from the lowest truncated SCD-residence classes
   minimizes the first two terms. **Conditional on a physical packet
   realization with exact rooted flag coherence**, this gives
   \(\widetilde E_d=0\) at every depth, including after the short SCD
   chains end. For (0.3), the complete scalar bill is
   \(O_{a,C}(W/\sqrt m)=o(W)\).

4. The first unavailable implication is the existence of an acyclic
   full-tail compatibility subgraph, prescribed tails in it, and an
   all-subset ordered-Hall inequality for those choices, together with an
   equitable decomposition into \(s\) paths of exactly \(K\) vertices,
   simultaneous physical collars after native tails expire, and the
   literal nonreturn/packet closure law

   \[
   (u_0,\ldots,u_{K-1})\text{ is a permutation of }[K],
   \qquad v_i=u_{i+R}.
   \tag{0.7}
   \]

   Separate-rank Hall matchings, SCD rank counts, and PBBS homomesy do not
   imply either assertion.

5. A conditional periodic PBBS component-phase lemma is exact: two-component
   target redundancy would make the aggregate phase-cut loss
   \(O(W/\sqrt m)\). At every depth where the corrected scalar-optimal
   reference support is complete, at least

   \[
   (2N_d-G)_+
   \tag{0.8}
   \]

   targets have a unique reference occurrence. On a positive-width early
   Gaussian subannulus this makes the expected loss under the periodic
   independent-phase model \(\Omega(W)\). New seam-crossing windows could still
   repair those targets, so this closes the retention argument, not every
   correlated PBBS rethreading.

6. A genuine architecture no-go is proved for intact, endpoint-only,
   fixed-frame BTK product paths. Put

   \[
   \mathfrak D(b)
   =\operatorname{erf}(b/2)
     -\frac b{\sqrt\pi}e^{-b^2/4}.
   \tag{0.9}
   \]

   If

   \[
   \boxed{
   \mathfrak D(b)>1-e^{-a^2},}
   \tag{0.10}
   \]

   the corrected entrance census necessarily uses a positive owner mass
   of coherent-history sink paths. No such intact selection can be
   cyclically packetized; every open endpoint-only fusion has at least

   \[
   \left(2\bigl[e^{-a^2}-(1-\mathfrak D(b))\bigr]-o(1)\right)
   \frac WH
   \tag{0.11}
   \]

   components. Internal cuts and transverse/nonproduct SCD frames remain
   exact escapes.

7. Finally, injective owner assignment alone does not imply PBBS global
   factorization. A new logarithmic-block construction has near-regular
   departure degrees, distinct assigned middle starts, and individually
   legal return-free geodesics, but its departure chromatic index is
   \((2-o(1))\) times its maximum degree. It refutes the formal
   owner-spread hypothesis, though not the actual canonical PBBS factor.

Thus this report supplies an exact zero-excess **conditional** compiler
theorem and closes the intact fixed-BTK sector (0.10). It does not
construct the required full-tail Hall matching or a literal PBBS packet
factor in the unrestricted sector. No coefficient-one conclusion is
claimed.

## 1. The floor-correct support identity

For a directed cyclic order \(\pi=(z_i)_{i\in\mathbb Z_K}\), write

\[
 I_\pi(i,r)=\{z_i,z_{i+1},\ldots,z_{i+r-1}\}.
\tag{1.1}
\]

Its entrance states and relative-depth traces are

\[
 A_{\pi,i}=I_\pi(i,R),
\qquad
 \tau_d(\pi,i)=I_\pi(i+d,R-d).
\tag{1.2}
\]

Because \(d\le D=o(m)\), and hence \(R+D<n\) for all sufficiently
large \(m\), there is no wrap ambiguity in the following exact endpoint
identity:

\[
 \boxed{
 \tau_d(\pi,i)=A_{\pi,i}\cap A_{\pi,i+d}.}
\tag{1.3}
\]

Let \(\mu_d(T)\) count selected occurrences with trace \(T\), and put

\[
 S_d=|\operatorname{supp}\mu_d|,
\qquad
 E_d=\sum_T(\mu_d(T)-1)_+,
\qquad
 H_d=|\{T:\mu_d(T)=0\}|.
\tag{1.4}
\]

Every packet contains \(K\) distinct intervals of each positive proper
length, so

\[
 \sum_T\mu_d(T)=G.
\tag{1.5}
\]

### Theorem 1.1 (exact synchronized support identity)

At every \(0\le d\le D\),

\[
 E_d=G-S_d,
 \qquad H_d=N_d-S_d,
\tag{1.6}
\]

and, with \(\widetilde E_d=E_d-(G-N_d)_+\),

\[
 \boxed{
 \widetilde E_d
 =\min(G,N_d)-S_d
 =\min(E_d,H_d).}
\tag{1.7}
\]

Equations (0.4)--(0.5) follow. In particular,

\[
 \boxed{
 \sum_{d=0}^{D}\widetilde E_d=o(W)}
\tag{1.8}
\]

is equivalent to

\[
 \boxed{
 \sum_{d=0}^{D}
 \left[
   \min(G,N_d)
   -\left|\{\tau_d(\pi,i):\pi,i\}\right|
 \right]=o(W).}
\tag{1.9}
\]

#### Proof

For every nonzero load \(x\), one has \((x-1)_+=x-1\). Summing over
the support gives \(E_d=G-S_d\); the hole identity is immediate. If
\(G\ge N_d\), then \(E_d-H_d=G-N_d\), so
\(\widetilde E_d=H_d\). If \(G\le N_d\), then
\(H_d-E_d=N_d-G\), so \(\widetilde E_d=E_d\). This proves (1.7) and
(0.5).

Finally,

\[
 \begin{aligned}
 \|\mu_d-\mathbf1\|_1
 &=H_d+E_d\\
 &=|G-N_d|+2\widetilde E_d,
 \end{aligned}
\]

which is (0.4). Substitution of (1.3) proves (1.9). \(\square\)

Complementing inside \([n]\) takes every lower interval to the
corresponding upper packet target. Hence the complete lower and upper load
vectors agree after a target bijection; all identities above hold with the
same values on both signs.

## 2. Postmatching rigidity and the exact seam influence

### Theorem 2.1 (entrance packets reconstruct all deeper ranks)

Assume \(2\le R<n/2\). The unordered entrance deck

\[
 \mathcal E_R(\pi)=\{I_\pi(i,R):i\in\mathbb Z_n\}
\tag{2.1}
\]

determines the undirected coordinate cycle \(\pi\) uniquely. Therefore it
determines every family \(\mathcal E_{R-d}(\pi)\), every load \(\mu_d\),
and every \(\widetilde E_d\). The two directed realizations differ only
by reversal and have identical target sets at every depth.

#### Proof

Make a graph on \(\mathcal E_R(\pi)\) by joining two targets whose
intersection has size \(R-1\). Since \(R<n/2\), two cyclic
\(R\)-intervals have such an intersection exactly when their starts differ
by \(1\) or \(-1\). The graph is therefore the cycle \(C_n\), recovering
the cyclic order of the entrance targets up to reversal.

Along either orientation, the singleton differences

\[
 I_\pi(i,R)\setminus I_\pi(i+1,R)=\{z_i\}
\tag{2.2}
\]

recover the coordinate cycle. Formula (1.3) then recovers every deeper
trace. \(\square\)

Thus an SCD selected after an already fixed entrance packet matching is a
certificate only. It has no remaining physical order variable with which
to alter (1.9).

### Corollary 2.2 (no postmatching order compiler)

For a fixed entrance matching by literal packet decks,

\[
 \boxed{
 \min_{\substack{\text{packet rotations and orientations}\\
                  \text{post hoc SCD certificates}}}
 \sum_{d=0}^{D}\widetilde E_d
 =
 \sum_{d=0}^{D}\widetilde E_d(\mathcal M).}
\tag{2.2a}
\]

Thus the requested deterministic order selection is possible after the
matching is frozen if and only if that matching already satisfies (1.9).
Any genuine compiler must alter which entrance roots share a packet, not
merely phase or orient the existing decks.

### Lemma 2.3 (exact transition-replacement influence)

Replacing \(t\) directed transitions in a family of entrance cycles
changes at most

\[
 u_d\le\min\{G,td\}
\tag{2.3}
\]

depth-\(d\) occurrences. Consequently

\[
 \|\Delta\mu_d\|_1\le2u_d,
 \qquad
 |\Delta\widetilde E_d|\le u_d.
\tag{2.4}
\]

#### Proof

A \(d\)-edge trace window changes only if it contains a replaced
transition. Each transition belongs to exactly \(d\) cyclic windows, so
the union bound gives (2.3); overlap can only improve it. Replacing one
occurrence subtracts one unit at its old target and adds one at its new
target. This gives the first inequality in (2.4). Formula (0.4) and the
reverse triangle inequality give the second. \(\square\)

If one seam per packet is replaced, then, using

\[
 s=\left(e^{-a^2}+o(1)\right)\frac W{2m},
 \qquad D=(b-a+o(1))\sqrt m,
\]

the one-sign worst-case all-depth influence is

\[
 \sum_{d=1}^{D}sd
 =\left(\frac{e^{-a^2}(b-a)^2}{4}+o(1)\right)W.
\tag{2.5}
\]

This is an upper bound, not a lower bound. Target-level cancellation can
make the actual change zero. A seam count or provenance-turnover count
alone cannot prove failure of (1.8).

## 3. A floor-correct pair potential and the exact support dual

For integers \(G,N\ge1\), define the balanced pair floor

\[
 \begin{aligned}
 P(G,N)
 &=\min_{\substack{x_1+\cdots+x_N=G\\x_j\in\mathbb Z_{\ge0}}}
     \sum_{j=1}^{N}\binom{x_j}{2}\\
 &=N\binom{c}{2}+cr,
 \qquad G=cN+r,\quad0\le r<N\\
 &=\sum_{h\ge1}(G-hN)_+.
 \end{aligned}
\tag{3.1}
\]

Put

\[
 C_d=\sum_T\binom{\mu_d(T)}2,
 \qquad
 \Phi_d=C_d-P(G,N_d),
 \qquad
 M_d=\min(G,N_d),
\tag{3.2}
\]

and, with the harmless boundary convention \(\kappa_d=1\) when
\(M_d=1\),

\[
 \kappa_d=
 \begin{cases}
 P(G,M_d-1)-P(G,M_d),&M_d\ge2,\\
 1,&M_d=1.
 \end{cases}
\tag{3.3}
\]

### Theorem 3.1 (pair excess controls support excess)

For every depth,

\[
 \boxed{
 \Phi_d\ge\kappa_d\widetilde E_d,\qquad\kappa_d\ge1.}
\tag{3.4}
\]

More sharply,

\[
 \boxed{
 \Phi_d\ge
 P(G,M_d-\widetilde E_d)-P(G,N_d).}
\tag{3.5}
\]

Uniformly in the fixed Gaussian annulus (where \(M_d\to\infty\)),

\[
 1\le\kappa_d\le C_{a,b}<\infty.
\tag{3.6}
\]

#### Proof

If \(M_d=1\), necessarily \(\widetilde E_d=0\), so the assertion is
immediate. Assume henceforth that \(M_d\ge2\). The load is supported on exactly
\(S_d=M_d-\widetilde E_d\) targets. Convexity of
\(x\mapsto\binom x2\) says that its pair count is at least
\(P(G,S_d)\), proving (3.5). The function \(P(G,N)\), as the number of
available bins \(N\) decreases, has nondecreasing discrete increments.
Therefore

\[
 P(G,M_d-t)-P(G,M_d)
 \ge t\,[P(G,M_d-1)-P(G,M_d)].
\]

Also \(P(G,M_d)=P(G,N_d)\): both are zero when \(G\le N_d\), and
\(M_d=N_d\) otherwise. This proves (3.4). Removing one bin from a
balanced placement of \(G\ge1\) balls creates at least one pair, so
\(\kappa_d\ge1\). Finally \(G/N_d\) is bounded above and below by
positive constants depending only on \(a,b\), which bounds the displayed
integer marginal above. \(\square\)

### Corollary 3.2 (deterministic conditional-expectation compiler)

For any probability distribution on fully legal packet compilers, if

\[
 \sum_{d=0}^{D}
 \frac{\mathbb E C_d-P(G,N_d)}{\kappa_d}=o(W),
\tag{3.7}
\]

then some deterministic compiler satisfies (1.8). Exposing any finite
sequence of compiler choices and always choosing a branch of no larger
conditional expectation derandomizes the assertion.

The exact sharp expectation, which does not pay the pair-energy
relaxation, is

\[
 \mathbb E\widetilde E_d
 =M_d-\sum_T\Pr(\mu_d(T)>0).
\tag{3.8}
\]

There is no universal linear obstruction on the unrestricted literal
packet catalogue. Give every directed cyclic coordinate order, modulo
rotation, weight

\[
 \frac1{R!(n-R)!}.
\tag{3.9}
\]

Every entrance target then has load one. A rank-\((R-d)\) target has load

\[
 \frac{(R-d)!(n-R+d)!}{R!(n-R)!}
 =\frac{N_0}{N_d}.
\tag{3.10}
\]

Thus the fractional repeat is exactly the forced floor at every depth.
All summands in (3.9) are literal packets and already satisfy antipodality,
coordinate balance, and zero monodromy. Hence an unrestricted no-go must
use entrance-matching integrality or a PBBS/SCD-restricted catalogue cut.
In particular, no linear inequality valid for the full fractional
entrance-matching relaxation can exclude this point. A separating
inequality valid only for integral entrance matchings, or an integrality,
congruence, or catalogue-dependent side condition, remains possible.

For later comparison, every allowed catalogue also has the exact support
dual. For arbitrary \(0\le\lambda_{d,T}\le1\) and every entrance-disjoint
packet family \(\mathcal M\),

\[
 \boxed{
 \sum_d\widetilde E_d
 \ge
 \sum_{d,T}\lambda_{d,T}
 -\sum_{P\in\mathcal M}\sum_d\sum_{T\in P_d}\lambda_{d,T}
 -\sum_d(N_d-G)_+.}
\tag{3.11}
\]

For a fixed \(\mathcal M\), equality is obtained by taking
\(\lambda_{d,T}\) to be the indicator of its holes.

Indeed, the weighted support is at most the weighted occurrence mass, so
the weighted hole count is bounded below by the first two terms in
(3.11). Subtracting the scalar hole floor gives the inequality. The hole
indicator makes the occurrence term zero and recovers
\(H_d-(N_d-G)_+=\widetilde E_d\).

## 4. The exact SCD home compiler

Fix a full symmetric-chain decomposition \(\mathscr D\) of \(B_n\). Every
chain whose endpoint ranks are \(m-r,m+r\) is said to have radius \(r\).
Every rank-\(R\) set \(T\) lies on a chain of radius at least \(q_0\). Let

\[
 \rho(T)=\text{the number of downward SCD steps available below }T,
\tag{4.1}
\]

and put

\[
 A_d=\{T\in\tbinom{[n]}R:\rho(T)\ge d\}.
\tag{4.2}
\]

If \(T\in A_d\), let \(h_d(T)\) be the chain's rank-\((R-d)\) member.
The SCD rank census gives

\[
 |A_d|=N_d,
 \qquad
 h_d:A_d\longrightarrow\binom{[n]}{R-d}
 \text{ is a bijection}.
\tag{4.3}
\]

Let \(\mathcal C\subseteq\binom{[n]}R\) be the entrance support of the
packet matching, so \(|\mathcal C|=G\), and let

\[
 \mathcal L=\binom{[n]}R\setminus\mathcal C,
 \qquad |\mathcal L|=L.
\tag{4.4}
\]

For \(T\in\mathcal C\), let \(x(T)\) be its unique packet occurrence,
and define the rooted home-failure set

\[
 F_d=\{T\in\mathcal C\cap A_d:
          \tau_d(x(T))\ne h_d(T)\}.
\tag{4.5}
\]

### Theorem 4.1 (SCD residence and home bound)

For every \(0\le d\le D\),

\[
 \boxed{H_d\le|\mathcal L\cap A_d|+|F_d|,}
\tag{4.6}
\]

and

\[
 \boxed{
 \widetilde E_d
 \le |\mathcal L\cap A_d|
  -\bigl(L-(N_0-N_d)\bigr)_+
  +|F_d|.}
\tag{4.7}
\]

In particular,

\[
 \boxed{
 \sum_{d=0}^{D}\widetilde E_d
 \le
 \underbrace{
 \sum_{d=0}^{D}
 \left[|\mathcal L\cap A_d|
  -\bigl(L-(N_0-N_d)\bigr)_+\right]}_{
 \text{leave--residence mismatch}}
 +\sum_{d=0}^{D}|F_d|.}
\tag{4.8}
\]

#### Proof

Every \(T\in\mathcal C\cap A_d\setminus F_d\) contributes the target
\(h_d(T)\). These targets are distinct by (4.3), so the support has size
at least

\[
 N_d-|\mathcal L\cap A_d|-|F_d|.
\]

This proves (4.6). The packet occurrences belonging to short SCD chains
\(T\notin A_d\) still produce physical depth-\(d\) targets after their
SCD chains end. They are extra occurrences and can only enlarge support;
discarding them in this lower bound is legitimate.

Now

\[
 (N_d-G)_+
 =\bigl(L-(N_0-N_d)\bigr)_+.
\]

Subtract this scalar floor from (4.6) and use (0.5), proving (4.7) and
(4.8). \(\square\)

### Proposition 4.2 (the sharp residence minimum)

For every leave \(\mathcal L\),

\[
 \boxed{
 \sum_{d=0}^{D}|\mathcal L\cap A_d|
 \ge B(L):=
 \sum_{d=0}^{D}\bigl(L-(N_0-N_d)\bigr)_+.}
\tag{4.9}
\]

Equality holds exactly when the leave selects the \(L\) smallest values
of the truncated residence weight

\[
 w_D(T)=\min\{\rho(T),D\}+1.
\tag{4.10}
\]

Equivalently, below the terminal plateau it consists of every lower
\(\rho\)-shell and part of one boundary shell. If the boundary weight is
\(D+1\), the chosen boundary roots may be mixed arbitrarily among all
shells \(\rho\ge D\).

#### Proof

At depth \(d\), at most \(N_0-N_d\) entrance sets lie outside \(A_d\).
Therefore

\[
 |\mathcal L\cap A_d|
 \ge\bigl(L-(N_0-N_d)\bigr)_+.
\]

Summation proves (4.9). Also

\[
 \sum_d|\mathcal L\cap A_d|
 =\sum_{T\in\mathcal L}(\min\{\rho(T),D\}+1).
\]

This sum is minimized by taking the smallest available truncated weights
\(w_D(T)\). Such a selection contains all roots with \(\rho(T)<d\)
whenever it reaches beyond that census, and otherwise lies entirely among
those roots; hence it attains
\(|\mathcal L\cap A_d|=(L-(N_0-N_d))_+\) simultaneously for every
\(d\le D\). This proves both attainability of \(B(L)\) and the stated
equality characterization. \(\square\)

### Corollary 4.3 (zero-excess longest-chain compiler)

Choose the unique integer \(t\ge q_0\) under the half-open convention

\[
 \widehat N_{t+1}<G\le \widehat N_t.
\tag{4.11}
\]

Suppose \(\mathcal C\) consists of the rank-\(R\) members of every SCD
chain of radius at least \(t+1\), together with exactly
\(G-\widehat N_{t+1}\) chains of radius \(t\), and suppose
\(F_d=\varnothing\)
for every \(d\le D\). Then

\[
 \boxed{\widetilde E_d=0\quad(0\le d\le D).}
\tag{4.12}
\]

For every absolute depth \(q_0\le q\le t\), every selected chain reaches the target rank and gives
one of \(G\) distinct homes. For \(q\ge t+1\), every SCD chain which
reaches that rank was selected, so the home occurrences cover all
\(\widehat N_q\) targets. The extra packet traces of shorter chains can only add
duplicates. This is the direct proof of (4.12); it is also the equality
case of (4.7).

Under (0.3),

\[
 t-q_0=O_{a,C}(1),
 \qquad
 B(L)=O_{a,C}(N_0/\sqrt m)=o(W).
\tag{4.13}
\]

Indeed,

\[
 \widehat N_r-\widehat N_{r+1}
 =\widehat N_r\frac{2r+1}{m+r+1},
\tag{4.14}
\]

so each of a fixed number of first radius shells has
\((2a+o(1))N_0/\sqrt m\) chains. Taking any fixed
\(J>C/(2a)+1\) makes the first \(J\) shells contain more than \(L\)
chains for large \(m\). Only those \(O_{a,C}(1)\) depths contribute to
the scalar floor, each by \(O_{a,C}(N_0/\sqrt m)\).

If, in addition, every packet occurrence's physical middle owner is the
middle member of its assigned SCD chain, the middle owners are distinct
and middle damage is exactly zero. Without this extra identity, the
independent middle collision charge remains.

## 5. The full-tail ordered-Hall gate

Write the downward SCD word at an entrance set as

\[
 \delta_1(T),\ldots,\delta_{\rho(T)}(T),
 \qquad
 h_d(T)=T\setminus\{\delta_1(T),\ldots,\delta_d(T)\}.
\tag{5.1}
\]

Put \(\ell(T)=\min\{\rho(T),D\}\). Define the protected full-tail
digraph \(\mathcal G_D\) on entrance sets as follows. If \(\ell(T)\ge1\),
put \(T\to T'\) when

1. \(T,T'\) are Johnson adjacent and
   \(T\setminus T'=\{\delta_1(T)\}\);
2. \(\ell(T')\ge\ell(T)-1\); and
3. the residual native tail shifts exactly:

   \[
   \delta_j(T')=\delta_{j+1}(T)
   \qquad(1\le j<\ell(T)).
   \tag{5.2}
   \]

When \(\ell(T)=0\), the native SCD flag imposes no outgoing condition,
so all Johnson arcs are provisionally allowed. A later collar or physical
packet choice must choose among them.

If \(T_0\to\cdots\to T_d\) and \(\ell(T_0)\ge d\), induction in (5.2)
shows that its successive departures are

\[
 \delta_1(T_0),\ldots,\delta_d(T_0),
\tag{5.2a}
\]

and hence

\[
 \bigcap_{i=0}^{d}T_i=h_d(T_0).
\tag{5.2b}
\]

This does **not** by itself imply the endpoint identity
\(T_0\cap T_d=h_d(T_0)\): a previously deleted coordinate could return.
If the path is a segment of a literal packet satisfying the FIFO law
(7.2), no departure returns within \(d\le D<K-R\), and then the endpoint
identity does follow. Thus the full-tail condition and literal closure
are jointly sufficient; neither is being silently substituted for the
other.

The use of the entire tail in (5.2) is essential. Keeping only one-depth
arcs and then asking for simultaneous representatives under
\(d=1,\ldots,D\) is an intersection of many partition constraints;
ordinary Hall does not apply to it. The residual-length condition in the
definition is equally essential: after a native chain expires, its
outgoing collar is free rather than nonexistent.

### Theorem 5.1 (prescribed-terminal ordered Hall)

Assume an acyclic subgraph \(\mathcal A\) of the induced graph
\(\mathcal G_D[\mathcal C]\) is fixed. Prescribe vertex-disjoint directed
terminal tails \(Q_1,\ldots,Q_p\) contained in \(\mathcal A\), ending at
distinct vertices \(z_1,\ldots,z_p\). Let \(F_0\) be their arc set,
\(U_0\) its set of arc tails, \(V_0\) its set of arc heads, and
\(Z=\{z_1,\ldots,z_p\}\). Put

\[
 \mathcal L'=\mathcal C\setminus(U_0\cup Z),
 \qquad
 \mathcal R'=\mathcal C\setminus V_0.
\tag{5.3}
\]

If

\[
 \boxed{
 |N^+_{\mathcal A}(X)\cap\mathcal R'|
 \ge|X|\qquad(X\subseteq\mathcal L'),}
\tag{5.4}
\]

then the prescribed tails extend to a spanning directed path cover of
\(\mathcal C\) with exactly \(p\) paths, each ending at its prescribed
\(z_i\). Conversely, (5.4) is necessary for such an extension inside the
fixed acyclic digraph \(\mathcal A\).

#### Proof

Hall's theorem gives a matching from all left copies of \(\mathcal L'\)
into the right copies of \(\mathcal R'\). Add it to \(F_0\). The result
has indegree and outdegree at most one and exactly

\[
 |F_0|+|\mathcal L'|=|\mathcal C|-p
\]

arcs. The only vertices without outgoing arcs are the \(z_i\). Acyclicity
excludes directed cycles, so the graph consists of exactly \(p\) paths
ending there. Necessity is ordinary Hall applied to the nonprescribed
arcs. \(\square\)

Theorem 5.1 controls only the **number** of paths. Even when \(p=s\), its
\(G=Ks\) vertices need not be distributed as \(K\) vertices on every
path. Literal packetization therefore needs a separate equitable
strengthening

\[
 |V(P_i)|=K\qquad(1\le i\le s),
\tag{5.4a}
\]

or a redistribution theorem preserving all protected arcs and terminal
tails. The provisional arcs leaving \(\ell=0\) roots must simultaneously
be realized by actual collars. Neither condition follows from Hall's
inequality (5.4).

For the intended scale \(p=s\), the uncorrected rank census has large
scalar room for terminal tails. Uniformly for
\(1\le d\le D\),

\[
 \frac{N_0-N_d}{ds}
 =\bigl(\gamma_{a,b}(d/\sqrt m)+o(1)\bigr)\sqrt m,
\tag{5.5}
\]

where

\[
 \gamma_{a,b}(x)
 =\frac{2(1-e^{-2ax-x^2})}{x},
 \qquad \gamma_{a,b}(0)=4a,
\tag{5.6}
\]

and the minimum on \([0,b-a]\) is positive. Corollary 4.3 shows that the
leave can change the active status of only \(O_{a,C}(1)\) initial radius
shells. These statements are cardinality comparisons only: no compatible
tail, arc, or terminal set has been constructed. No available PBBS or SCD
theorem supplies an acyclic \(\mathcal A\), prescribed tails, the
all-subset cut (5.4), and then the physical closure law (0.7).

For an actual packet cycle with advance map \(g\), define its global
physical departure map by \(u(T)=T\setminus g(T)\). Native home coherence
requires

\[
 \delta_j(T)=u(g^{j-1}T)
 \qquad(1\le j\le\ell(T)),
\tag{5.7}
\]

while physical advancement and coordinate completeness require

\[
 g(T)=T-u(T)+u(g^R T),
 \qquad
 (u(T),u(gT),\ldots,u(g^{K-1}T))
 \text{ is a permutation of }[K].
\tag{5.8}
\]

These pointwise equations are strictly stronger than aggregate PBBS site
homomesy.

## 6. The conditional PBBS phase compiler and its unique-target cut

The following lemma records exactly what random component phases can and
cannot do.

### Proposition 6.1 (deterministic phase selection, conditional on bundling)

Suppose a reference family of directed components is scalar-optimal at
every relative depth, meaning that its depth-\(d\) support
\(\mathcal T_d\) has size

\[
 |\mathcal T_d|=M_d:=\min(G,N_d).
\tag{6.0}
\]

Assume every component is cyclically indexed, has length divisible by
\(K\), and carries the free periodic cut action in which phase
\(\theta_C\in\mathbb Z_K\) places cuts exactly at edge indices congruent
to \(\theta_C\pmod K\). Finally suppose
a separate physical theorem turns the resulting blocks into legal
\(K\)-slot packets while preserving every reference window which crosses
no cut.

For a reference-supported target \(T\in\mathcal T_d\), let
\(b_{C,d}(T)\) be the number of phases which
destroy every depth-\(d\) occurrence of \(T\) on component \(C\). Then

\[
 0\le b_{C,d}(T)\le d,
\tag{6.1}
\]

and independent uniform phases destroy every reference occurrence of
\(T\) with exact probability

\[
 \prod_{C\text{ supporting }T}\frac{b_{C,d}(T)}K.
\tag{6.2}
\]

Consequently some deterministic phase vector has aggregate excess at most

\[
 \boxed{
 \frac1K\sum_d d|\mathcal S_d|
 +\frac1{K^2}\sum_d d^2(M_d-|\mathcal S_d|),}
\tag{6.3}
\]

where \(\mathcal S_d\subseteq\mathcal T_d\) is the set of supported
targets occurring on only one reference component. Baseline targets
outside \(\mathcal T_d\) are not loss events. New seam-crossing windows
can only improve this upper bound.

#### Proof

A fixed \(d\)-window crosses a periodic cut for exactly \(d\) cut phases
(here \(d<K\)).
All occurrences of one target on the same component die only when the
phase lies in the intersection of their bad-phase sets, proving (6.1).
Phases on distinct components are independent, proving (6.2). A
one-component supported target has loss probability at most \(d/K\), and
every other supported target at most \((d/K)^2\). Losing \(r\) targets
from an initially scalar-optimal support increases \(\widetilde E_d\) by
at most \(r\); replacement seam windows only reduce that increase. Sum
and choose a phase vector no worse than the expectation. \(\square\)

If \(\mathcal S_d=\varnothing\), then

\[
 \sum_d\widetilde E_d
 \le\frac W{K^2}\sum_{d=1}^{D}d^2
 =\frac{WD(D+1)(2D+1)}{6K^2}
 =O(W/\sqrt m).
\tag{6.4}
\]

But the corrected entrance mass prevents this premise on the early
annulus. Suppose explicitly that the scalar-optimal reference support is
complete at depth \(d\), so \(G\ge N_d\), and let \(U_d\) be the number
of targets with exactly one reference occurrence. Then

\[
 G\ge U_d+2(N_d-U_d),
\]

so

\[
 \boxed{U_d\ge(2N_d-G)_+.}
\tag{6.5}
\]

For

\[
 a<x<\min\{b,\sqrt{a^2+\log2}\},
 \qquad q=x\sqrt m+O(1),
\]

the right side of (6.5) is \(\Omega_{a,b}(W)\). Across any closed
subinterval of this range,

\[
 \frac1K\sum_d dU_d=\Omega_{a,b}(W).
\tag{6.6}
\]

Every globally unique occurrence has exactly \(d\) bad phases, so the
periodic independent-phase model destroys a linear number of old unique
targets in expectation. Crossing windows might replace them, so (6.6) is
not a lower bound on final holes. It proves that the phase-retention lemma
alone cannot establish (1.8).

## 7. Literal packet closure

### Theorem 7.1 (exact \(K\)-slot FIFO law)

Let \((A_i)_{i\in\mathbb Z_K}\) be a directed cycle in \(J(K,R)\),
with

\[
 A_{i+1}=A_i-\{u_i\}+\{v_i\}.
\tag{7.1}
\]

It is the rank-\(R\) trace of one literal cyclic coordinate order if and
only if

\[
 \boxed{
 (u_i)_{i\in\mathbb Z_K}\text{ is a permutation of }[K],
 \qquad v_i=u_{i+R}\quad(i\in\mathbb Z_K).}
\tag{7.2}
\]

In that case

\[
 A_i=\{u_i,u_{i+1},\ldots,u_{i+R-1}\}.
\tag{7.3}
\]

#### Proof

For a literal coordinate cycle, shifting the window removes its first
coordinate and inserts the coordinate \(R\) positions later, proving
necessity. Conversely, under (7.2), coordinate \(u_j\) is inserted at
transition \(j-R\) and removed at transition \(j\). It belongs to
exactly the states with \(i\le j\le i+R-1\), proving (7.3). \(\square\)

Local PBBS fan geodesicity proves neither the global departure permutation
nor the pointwise \(R\)-shift in (7.2).

## 8. A statewise fixed-BTK/product-SCD no-go

Split the coordinates into \(A\dot\cup B\), \(|A|=|B|=m\), and use
the standard BTK product SCD. An atomic rank-\(m\) product path of length
\(h\) has active alphabets

\[
 I_A(P)\subseteq A,
 \qquad I_B(P)\subseteq B,
 \qquad |I_A(P)|=|I_B(P)|=h.
\tag{8.1}
\]

The audited coherent-history sink theorem states: if an entire atomic path
is traversed in either orientation and

\[
 h\ge4,\qquad 2h+3\le H,
\tag{8.2}
\]

then no endpoint seam into another intact BTK product path preserves both
signed flags through depth \(H\). Internal cuts or a change of SCD frame
are not covered by that theorem. This is the proved stack-nesting theorem
in `MATH_OBSTRUCTION_BTK_PRODUCT_SCD_COHERENT_HISTORY_ENDPOINT_SINK_20260726.md`,
not an unproved lemma introduced here.

### Theorem 8.1 (wide-annulus corrected-census obstruction)

Let

\[
 \mathfrak D(b)
 =\frac4{\sqrt\pi}\int_0^{b/2}x^2e^{-x^2}\,dx
 =\operatorname{erf}(b/2)-\frac b{\sqrt\pi}e^{-b^2/4}.
\tag{8.3}
\]

The middle-owner mass in intact BTK paths satisfying (8.2) is

\[
 (\mathfrak D(b)+o(1))W.
\tag{8.4}
\]

Therefore, if

\[
 \Delta(a,b):=e^{-a^2}-(1-\mathfrak D(b))>0,
\tag{8.5}
\]

every union of whole atomic paths containing the corrected entrance mass
\(G=(e^{-a^2}+o(1))W\) contains at least
\((\Delta(a,b)-o(1))W\) owners on sink paths. It cannot be bundled into
cyclic endpoint-only packets. Every open endpoint-only path cover has

\[
 \boxed{
 p\ge(2\Delta(a,b)-o(1))\frac WH.}
\tag{8.6}
\]

#### Proof

For \(h\equiv m\pmod2\), put \(r=(m-h)/2\). The exact number of
atomic product paths of length \(h\) is

\[
 P_h=\binom mr^2-\binom m{r-1}^2.
\tag{8.7}
\]

Indeed, the number of atomic paths of length at least \(h\) is
\(\binom mr^2\): independently choose the two factor-chain positions at
rank \(r\). Subtracting the corresponding census
\(\binom m{r-1}^2\) for length at least \(h+2\) gives (8.7).

Uniformly for \(h=x\sqrt m\) in a fixed compact interval, Stirling's
formula gives

\[
 \binom mr^2
 =\left(\frac2{\sqrt\pi}+o(1)\right)
   \frac W{\sqrt m}e^{-x^2},
\]

and

\[
 1-\left(\frac{\binom m{r-1}}{\binom mr}\right)^2
 =1-\left(\frac r{m-r+1}\right)^2
 =\frac{4x+o(1)}{\sqrt m}.
\]

Hence

\[
 P_h=\left(\frac{8x}{\sqrt\pi}e^{-x^2}+o(1)\right)\frac Wm.
\tag{8.8}
\]

Admissible \(h\)'s have step two, so

\[
 \frac1W\sum_{h\le c\sqrt m}(h+1)P_h
 \longrightarrow
 \frac4{\sqrt\pi}\int_0^c x^2e^{-x^2}\,dx.
\tag{8.9}
\]

Taking \(c=b/2\), deleting the finitely many \(h<4\), and imposing the
exact cutoff \(2h+3\le H\) changes only \(o(W)\), proving (8.4).

The nonsink paths contain only
\((1-\mathfrak D(b)+o(1))W\) owners. If (8.5) holds, the claimed sink
owner mass is forced. Every sink path has at most \(H/2+O(1)\) owners,
so these owners occupy at least
\((2\Delta(a,b)-o(1))W/H\) distinct terminal paths. This proves (8.6),
and a cyclic endpoint-only bundle is impossible because every constituent
would require an outgoing seam. \(\square\)

There is also a local entrance-rank version. Fix
\(0<\alpha<\beta<a/2\), and let \(J\) intact paths have lengths in
\([\alpha\sqrt m,\beta\sqrt m]\) and occur as intact constituents of
literal cyclic endpoint-only output packets, so that each of these
\(J\) paths has an outgoing seam. Put

\[
 \ell_m=q_0-2\lceil\beta\sqrt m\rceil-2,
 \qquad
 D_m=1+\left\lceil
 \frac{q_0}{\lfloor\alpha\sqrt m\rfloor-2}
 \right\rceil.
\tag{8.10}
\]

One sign then has at least

\[
 \boxed{\frac{J\ell_m}{2D_m}}
\tag{8.11}
\]

wrong-rank entrance windows. Indeed, every outgoing seam shares an active
coordinate with the adjacent path. Let \(d_e\) be the length of the
smallest transition interval containing its two opposite uses; then
\(d_e\le2h+3\), and exactly \(q_0-d_e+1\) entrance windows contain both
uses (the output cycle has length \(2m\), so there is no wrap ambiguity).
An inserted-then-removed coordinate leaves at most \(q_0-1\) distinct
initial deletions, while a removed-then-inserted coordinate leaves at most
\(q_0-1\) distinct insertions. Thus one signed rank is wrong. Candidate
seams are spaced by at least \(\lfloor\alpha\sqrt m\rfloor-2\), so a
start lies in at most \(D_m\) bad intervals; sign pigeonholing proves
(8.11).

An actual literal packet has no wrong-rank windows. Thus (8.11) is a
literal packetization obstruction, not an instance of (0.5). In a relaxed
Johnson compiler which discards wrong-rank occurrences, the corrected
ledger is instead

\[
 H_d=N_d-(G-R_d)+E_d,
\tag{8.12}
\]

where, for the sign under discussion, \(R_d\) is the total wrong-rank
occurrence count and \(E_d\) counts repeats only among the remaining
valid rank-\(d\) occurrences. The two ledgers must not be conflated.

## 9. Owner spread alone does not imply PBBS factorization

The earlier projective-plane countermodel was too concentrated in its
owner shadow. The following logarithmic-block construction survives an
injective starting-owner requirement.

Continue with the even ground set \(n=2m\). Choose
\(h=\Theta(\log m)\), and put

\[
 v=2h-1,
 \qquad E=\binom vh,
 \qquad Q=\binom{v-1}{h-1},
 \qquad \frac EQ=\frac{2h-1}{h}.
\tag{9.1}
\]

Let \(B=\Theta(W/m)\) be the intended packet count and set

\[
 w=\left\lfloor\frac BQ\right\rfloor.
\tag{9.2}
\]

Choose \(c\) minimally so that

\[
 \binom{2c}{c}
 \ge\left\lfloor\frac n{2h-1}\right\rfloor,
\tag{9.3}
\]

and reserve a marker set \(M\) of size \(r=2c\). Then
\(r=\Theta(\log m)\). Partition all but fewer than \(v\) coordinates
outside \(M\) into \(b\) disjoint blocks
\(Q_1,\ldots,Q_b\) of size \(v\), and choose distinct marker words

\[
 C_j\in\binom Mc.
\tag{9.4}
\]

On each \(Q_j\), take \(w\) parallel copies of every \(h\)-set.

### Theorem 9.1 (factor-two owner-spread cut)

The resulting departure multihypergraph \(\mathcal D\) has

\[
 \Delta(\mathcal D)=wQ=(1-o(1))B,
\tag{9.5}
\]

on all but \(o(n)\) coordinates,

\[
 |E(\mathcal D)|=(1+o(1))\frac{nB}{h},
 \qquad \nu(\mathcal D)=b,
\tag{9.6}
\]

and

\[
 \boxed{
 \chi'(\mathcal D)=wE
 =\left(2-\frac1h\right)\Delta(\mathcal D)
 =(2-o(1))B.}
\tag{9.7}
\]

Moreover, its edge copies admit distinct assigned starting owners
\(X_e\in\binom{[n]}m\), with \(e\subseteq X_e\), and each pair
\((e,X_e)\) extends individually to a literal return-free \(h\)-step
Johnson geodesic and hence to a cyclic-order segment.

#### Proof

Every coordinate of a block belongs to \(Q\) of its \(E\) many
\(h\)-sets, proving (9.5). Any two \(h\)-subsets of a
\((2h-1)\)-set intersect. Hence a departure matching uses at most one
edge copy from each block, while it can use one from every block. This
gives \(\nu=b\). All \(wE\) copies inside one block are pairwise
intersecting, and different blocks are disjoint, so the chromatic index is
exactly \(wE\). Equations (9.6)--(9.7) follow.

It remains to assign owners. For block \(j\), use the disjoint pool

\[
 \mathcal X_j={X\in\tbinom{[n]}m:X\cap M=C_j\}.
\tag{9.8}
\]

Every pool has size

\[
 V=\binom{2(m-c)}{m-c}.
\tag{9.9}
\]

For \(X=C_j\cup Y\), put \(t=|Y\cap Q_j|\). Complementation on
\([n]\setminus M\) sends \(t\) to \(v-t\). Since \(v\) is odd,
exactly \(V/2\) owners have \(t\ge h\).

Make a bipartite graph from \(D\in\binom{Q_j}h\) to these usable owners,
joining \(D\) to \(X\) when \(D\subset X\). Give a usable owner \(X\)
weight \(1/\binom th\) on each of its incident \(D\)'s. Its total right
load is one. By symmetry of \(Q_j\), every left vertex receives the same
load; summing over the \(E\) left vertices shows that this load is
\(V/(2E)\).

Minimality in (9.3) and Stirling give

\[
 2^r=\Theta((m/h)\sqrt r),
 \qquad
 \frac VW=(1+o(1))2^{-r},
 \qquad
 \frac VB=\Theta(h/\sqrt r)\longrightarrow\infty.
\tag{9.10}
\]

Therefore

\[
 \frac{w}{V/(2E)}
 \le2\frac EQ\frac BV=o(1).
\]

Scaling the fractional flow supplies left demand \(w\) with right
capacity at most one. Integrality of bipartite flow assigns \(w\) distinct
owners to every \(D\). The pools (9.8) are disjoint, so all assigned
starts are globally distinct.

For an assigned \(D\subset X\), choose an \(h\)-set
\(A\subseteq[n]\setminus(M\cup X)\), order

\[
 D=(d_0,\ldots,d_{h-1}),
 \qquad A=(a_0,\ldots,a_{h-1}),
\]

and put

\[
 X_t=
 (X\setminus\{d_0,\ldots,d_{t-1}\})
 \cup\{a_0,\ldots,a_{t-1}\}.
\tag{9.11}
\]

No coordinate changes twice, so this is a return-free Johnson geodesic.
To see literal completion directly, order the remaining coordinates as

\[
 X\setminus D=(x_h,\ldots,x_{m-1}),
 \qquad
 [n]\setminus(X\cup A)=(y_h,\ldots,y_{m-1}),
\]

and take the cyclic direction order

\[
 (d_0,\ldots,d_{h-1},x_h,\ldots,x_{m-1},
   a_0,\ldots,a_{h-1},y_h,\ldots,y_{m-1}).
\tag{9.12}
\]

Its first rank-\(m\) interval is \(X\), and its first \(h\) shifts are
exactly (9.11). Thus no external completion lemma is being assumed.
\(\square\)

Theorem 9.1 disproves the implication

\[
 \text{near-regular departures + distinct assigned starts
 + local geodesicity}
 \Longrightarrow
 \chi'=(1+o(1))B.
\tag{9.13}
\]

It does **not** refute actual PBBS factorization. Only the starting owners
are globally distinct; the intermediate states are not proved to form one
owner-disjoint permutation. The construction supplies no PBBS chronology,
common arrival coloring, ordered-slot compatibility, or shadow support.

## 10. Exact boundary

Proved:

1. the exact identity (0.4)--(0.5) and endpoint normal form (1.3);
2. postmatching rigidity and the seam influence constant (2.5);
3. the floor-correct pair potential (3.4) and exact support dual (3.11);
4. the SCD home bound (4.7), sharp residence minimum (4.9), and the
   conditional zero-excess longest-chain compiler (4.12);
5. the prescribed-terminal ordered-Hall theorem (5.4);
6. the conditional periodic PBBS phase formula (6.2), its positive two-component
   bound, and the unique-target cut (6.5)--(6.6);
7. the literal packet FIFO law (7.2);
8. the fixed-BTK corrected-census no-go throughout (8.5); and
9. the factor-two owner-spread countercut (9.7) with distinct starts and
   individually legal fragments.

Not proved:

1. the all-subset Hall inequality (5.4) for an actual PBBS or
   noncanonical SCD full-tail graph;
2. an equitable \(K\)-vertex path partition, simultaneous physical
   collars for expired native tails, and a cycle selection satisfying both
   SCD home coherence and literal closure (7.2);
3. repair of the linear unique-target phase loss by crossing windows;
4. a no-go after internal BTK cuts or transverse/nonproduct SCD changes;
5. an actual PBBS factor obstruction from Theorem 9.1; or
6. the coefficient-one theorem.

For constant-one use, define \(C_{\rm mid}\) to be the repeated-middle
owner charge of the selected physical packet occurrences. The exact
positive successor is therefore:

\[
 \boxed{
 \begin{gathered}
 \mathcal L\text{ is SCD-residence-minimal},\qquad
 \sum_d|F_d|=o(W)\text{ after closure},\\
 C_{\rm mid}=o(W),\\
 \text{some acyclic full-tail subgraph and prescribed tails satisfy (5.4),}\\
 \text{admit simultaneous physical collars and an equitable }K
 \text{-vertex partition, and survive FIFO cycle closure.}
 \end{gathered}}
\]

The phrase "post-closure" is essential: each closing arc can change every
window crossing its endpoint, so a pre-closure estimate for \(F_d\) does
not automatically survive packetization.

Equivalently on the negative side, one must exhibit a fixed low-complexity
weight in (3.11), or a PBBS/SCD-specific Hall cut, with a linear deficit
against every entrance matching. Rankwise entropy, packetwise residence,
and owner spread by themselves cannot do this.

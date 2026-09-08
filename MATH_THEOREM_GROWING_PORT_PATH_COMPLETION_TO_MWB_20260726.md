# Growing port-path completion: the exact theorem sufficient for MWB

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

A growing \(D_s\)-port factor, even with exact Chung--Feller phase
ownership, does not by itself imply MWB. The missing quantitative datum
is the balanced overload of the **completed literal cyclic rows** at every
depth in one fixed Gaussian window.

There are three logically distinct sufficient statements.

1. The weakest unlabelled statement is the direct fixed-window overload
   bound
   \[
     \sum_{q\le \lceil A\sqrt m\rceil}
       \frac{O_q(F_{A,m})}{c_q}=o_A(W).                 \tag{0.1}
   \]
2. The exact port-core normal form is a quota-safe integral rooted-path
   core with one exact rooted completion whose weighted spill is
   \(o_A(W)\). This becomes a genuinely constructive growing-port theorem
   only when the core has audited growing-packet provenance and is
   quantitatively nonvacuous.
3. A stronger labelled statement aligns the same exact factor with one
   common balanced nested deletion resolution and has weighted mismatch
   \(o_A(W)\).

Any of these statements, for every fixed \(A\), implies MWB by
diagonalization and hence the sharp coefficient-one theorem
\[
                    \nu(k)=(1+o(1))
                    \binom{k}{\lfloor k/2\rfloor}.      \tag{0.2}
\]

The simple worst-case completion form has an exact rate. If \(R\) whole
cyclic rows remain outside the quota-safe port core, it is enough that
\[
       R=o_A\!\left(\frac{W}{(2m+1)\sqrt m}\right)
        =o_A\!\left(\frac{\operatorname {Cat}_m}{\sqrt m}\right).
                                                               \tag{0.3}
\]
The weaker condition \(R=o(W/(2m+1))\) is not enough without a structured
spill theorem.

Throughout, \(o_A(W)\) means a quantity whose ratio to \(W\) tends to
zero as \(m\to\infty\) with \(A\) fixed; no uniformity in \(A\) is
asserted.

This report also corrects one implication in
MATH_THEOREM_W_PORT_PATH_PCAP_CONSTANT_ONE_SYNTHESIS_20260726.md.
The PPR hypothesis there controls the actual number of holes and therefore
is sufficient for coefficient one. It is not presently sufficient for
MWB: its cap is \(2m+1\), whereas MWB uses the bounded Gaussian-window
floor \(c_q\). Small hole count does not control balanced overload.

## 1. Exact balanced-overload notation

Put
\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 B=\frac Wn=\operatorname {Cat}_m,                    \tag{1.1}
\]
and, for \(1\le q\le m\),
\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
 \rho_q=W-c_qN_q.                                     \tag{1.2}
\]

A balanced quota vector is a function
\[
 b:\binom{[n]}{m-q}\longrightarrow\{c_q,c_q+1\}
\]
having exactly \(\rho_q\) entries equal to \(c_q+1\). Its total mass is
\(W\). Denote the set of all such vectors by \(\mathcal B_q\).

Let \(F\) be a family of \(B\) oriented cyclic coordinate orders. For a
cyclic order \(\pi\), let \(I_\pi(j,r)\) be its length-\(r\) cyclic
interval beginning at \(j\). Define
\[
 \mu_q^F(S)=
 \#\{(\pi,j):\pi\in F,\ I_\pi(j,m-q)=S\}.             \tag{1.3}
\]
There are \(n\) pointed occurrences in every row, so
\[
                         \sum_S\mu_q^F(S)=nB=W.        \tag{1.4}
\]

If the length-\(m\) intervals of the rows partition
\(\binom{[n]}m\), then \(F\) is an exact middle wreath factor. Its
balanced overload is
\[
 \boxed{
 O_q(F)=\min_{b\in\mathcal B_q}
          \sum_S(\mu_q^F(S)-b(S))_+.}                 \tag{1.5}
\]
Equal total masses give the useful exact identity
\[
 O_q(F)=\frac12\min_{b\in\mathcal B_q}
                    \|\mu_q^F-b\|_1.                  \tag{1.6}
\]

For fixed \(A>0\), write
\[
 H_A=\lceil A\sqrt m\rceil,\qquad
 S_A(m)=\sum_{q=1}^{H_A}\frac1{c_q}.                  \tag{1.7}
\]

### Lemma 1.1 (bounded Gaussian-window capacities)

For every fixed \(A\), there is \(C_A<\infty\) such that, for all
sufficiently large \(m\) and every \(q\le H_A\),
\[
                         1\le c_q\le C_A,              \tag{1.8}
\]
and consequently
\[
                         S_A(m)=\Theta_A(\sqrt m).      \tag{1.9}
\]

#### Proof

The exact ratio is
\[
 \frac W{N_q}
 =\prod_{i=1}^{q}\frac{m+1+i}{m-q+i}.                 \tag{1.10}
\]
Expanding the logarithm uniformly for \(q\le A\sqrt m+1\) gives
\[
 \log\frac W{N_q}
   =\frac{q(q+1)}m+O_A(m^{-1/2}).                     \tag{1.11}
\]
Thus \(1\le W/N_q\le \exp(A^2+o_A(1))\), which proves
(1.8) after taking a floor. Now
\[
 \frac{H_A}{C_A}\le S_A(m)\le H_A,
\]
proving (1.9). \(\square\)

The factor and all of its rows must be common to every depth in (0.1).
The quota vector may vary with \(q\): MWB is unlabelled. Requiring the
quota vectors to come from one nested owner flow is a valid stronger
theorem, not part of the definition of \(O_q\).

## 2. The exact growing port-path object

Let \(J\) have size \(2s\), let
\[
 D_s\subseteq\binom Js,\qquad |D_s|=\operatorname {Cat}_s,
\]
be the inherited affine Dyck port family, and let
\(\mathsf M(J)\) be the inclusion graph on
\(\binom Js\sqcup\binom J{s+1}\).
Put
\[
                         \overline D_s=
                  \{J\setminus P:P\in D_s\}.
\]
Every member of \(D_s\) begins with the distinguished Dyck-side
coordinate, while its complement does not, so
\[
                         D_s\cap\overline D_s=\varnothing.      \tag{2.0}
\]

A rooted \(D_s\)-port path factor is a vertex partition of
\(\mathsf M(J)\) into
\[
 P=X_0\subset Y_0\supset X_1\subset\cdots
 \subset Y_{s-1}\supset X_s=J\setminus P,
 \qquad P\in D_s.                                     \tag{2.1}
\]
Thus both the \(X\)-shore and the \(Y\)-shore are owned exactly once, and
the two ordered endpoints are the physical entrance and exit ports.

### Lemma 2.1 (literal wreath reconstruction)

Every path (2.1) has unique deletion and insertion orders
\[
 (a_1,\ldots,a_s)\text{ of }P,\qquad
 (b_1,\ldots,b_s)\text{ of }J\setminus P              \tag{2.2}
\]
such that
\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
          \cup\{b_1,\ldots,b_t\}.                     \tag{2.3}
\]
After adjoining the local infinity coordinate, the literal cyclic
coordinate order is
\[
                 \pi_P=(a_1,\ldots,a_s,b_1,\ldots,b_s,\infty).
                                                               \tag{2.4}
\]
Its ordinary length-\(s\) cyclic intervals are the corresponding odd
cycle. A path factor (2.1) is therefore an integral
exact local wreath factor, not merely a graph decomposition.

#### Proof

Every two-step move \(X_{t-1}\subset Y_{t-1}\supset X_t\) replaces one
coordinate of \(P\) by one coordinate of its complement. The path has
\(s\) such moves and joins complementary \(s\)-sets, whose Johnson
distance is \(s\). Hence no coordinate can be deleted, inserted, or
reversed twice; the moves give the two permutations in (2.2) and
(2.3).

For \(0\le t<s\), the length-\(s\) interval of \(\pi_P\) beginning
at \(a_{t+1}\) is exactly
\[
 (P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\}=X_t.                    \tag{2.4a}
\]
The interval beginning at \(b_1\) is \(X_s\).
For the other middle windows, put
\[
 Z_{t-1}=\{\infty\}\cup(J\setminus Y_{t-1}).
\]
Since
\[
 Z_{t-1}
 =\{b_{t+1},\ldots,b_s,\infty,a_1,\ldots,a_{t-1}\},   \tag{2.4b}
\]
for \(1\le t<s\) this is the length-\(s\) interval beginning at
\(b_{t+1}\); for \(t=s\), it begins at \(\infty\). These are all
\(2s+1\)
ordinary windows of \(\pi_P\). Partition of the two shores owns,
respectively, all middle vertices avoiding and containing \(\infty\).
\(\square\)

### Proposition 2.2 (exact completion certificate)

Put
\[
 \mathcal X_s=\binom Js,\quad
 \mathcal Y_s=\binom J{s+1}.                          \tag{2.4c}
\]
Choose inclusion perfect matchings
\[
 M^\uparrow:\mathcal X_s\setminus\overline D_s
                         \longleftrightarrow\mathcal Y_s,
 \qquad
 M^\downarrow:\mathcal Y_s
                         \longleftrightarrow\mathcal X_s\setminus D_s.
                                                               \tag{2.4d}
\]
Let \(T=M^\downarrow\circ M^\uparrow\), and close it to a permutation of
\(\mathcal X_s\) by adjoining the marked arrows
\[
                         J\setminus P\longrightarrow P
                         \qquad(P\in D_s).             \tag{2.4e}
\]
The two matchings form a rooted port-path factor if and only if every
cycle of the closed permutation contains exactly one marked arrow.

#### Proof

Deleting the marked arrow turns each such cycle into a directed path from
one \(P\) to its own complementary endpoint. A cycle with no marked arrow
is an unwanted internal alternating cycle; a cycle with two marked arrows
joins two prescribed port pairs. Conversely, closing the complementary
endpoints of a factor (2.1) gives exactly one marked arrow in each cycle.
The total number of successor arcs forces every resulting path to have
the minimum length \(s\), so it is a complement geodesic. \(\square\)

The Chung--Feller fixed-layer model is a sufficient certificate for
(2.1), but not the general one. If \(X_t(P)\) are the canonical flaw
layers, permutations \(p_0,\ldots,p_s\) give an exact phase-layer factor
provided
\[
 p_0=p_s,                                              \tag{2.5}
\]
every \(X_t(p_tP),X_{t+1}(p_{t+1}P)\) is Johnson
adjacent, and
\[
 \biguplus_{t,P}
  \{X_t(p_tP)\cup X_{t+1}(p_{t+1}P)\}
              =\binom J{s+1}.                         \tag{2.6}
\]
Equation (2.5) is zero endpoint monodromy and (2.6) is the exact
aggregate \(Y\)-ledger. Independent adjacent-layer matchings or phase
marginals do not imply either condition.

Nor do (2.1), (2.5), and (2.6) control shallow shadows. If
\(A_t=\{a_1,\ldots,a_t\}\) and
\(B_t=\{b_1,\ldots,b_t\}\), then
\[
 \bigcap_{t=i}^{i+q}X_t=(P\setminus A_{i+q})\cup B_i,
 \qquad
 \bigcup_{t=i}^{i+q}X_t=(P\setminus A_i)\cup B_{i+q}. \tag{2.7}
\]
Thus \(q\)-step profiles depend on whole flags, not on layer marginals or
one-step colours. In a parent context they also acquire literal exterior
carriers and crossing collars. All overload hypotheses below are
therefore imposed on the final reconstructed cyclic rows (2.4), after
every parent alignment and collision.

Ordinary \(D_s\)-transversality is insufficient: the selected Dyck state
must be an endpoint port in (2.1). Likewise, an integral degree
\(b\)-factor is insufficient unless its components pair each
\(P\) with \(J\setminus P\); this marked monodromy condition can fail
even when both ownership matchings exist.

## 3. The exact port-core completion normal form

The authoritative statement is made globally, because separate exact
local packets need not remain jointly exact when their parent slabs
overlap or nest. A mesoscopic construction from
\(D_{s(m)}\)-port packets, with \(s(m)\to\infty\), qualifies precisely
when its reconstructed global rows provide the certificate below. No
rate for \(s(m)\) is used after that certificate has been obtained.

The normal form itself does not certify that such a mesoscopic
construction was used: it permits an empty core. Accordingly, it is a
precise implication theorem, not by itself the missing growing-factor
construction. Section 8 states the required nonvacuity clause.

### Hypothesis GPC\(_A\) (quota-safe growing-port completion)

For every fixed \(A>0\) and all sufficiently large \(m\), there are:

1. an integral family \(\mathcal M\) of vertex-disjoint rooted complement
   paths of the form
   \[
   P=X_0\subset Y_0\supset\cdots\subset Y_{m-1}
       \supset X_m=[2m]\setminus P,\qquad P\in G,
                                                               \tag{3.1}
   \]
   for some \(G\subseteq D_m\);
2. one integral rooted completion \(\mathcal C\), indexed by
   \(D_m\setminus G\), such that
   \[
                           F=\mathcal M\mathbin{\dot\cup}\mathcal C
                                                               \tag{3.2}
   \]
   partitions both global shores and hence reconstructs one exact
   \(D_m\)-port-transversal middle wreath factor;
3. balanced quota vectors \(b_q\in\mathcal B_q\), one for every
   \(q\le H_A\), such that the literal rows reconstructed from
   \(\mathcal M\) are quota-safe:
   \[
                         \mu_q^{\mathcal M}(S)\le b_q(S)
                         \quad\text{for all }S;         \tag{3.3}
   \]
4. with residual capacities
   \[
                         s_q(S)=b_q(S)-\mu_q^{\mathcal M}(S)\ge0,
                                                               \tag{3.4}
   \]
   the **same** completion \(\mathcal C\) satisfies
   \[
   \boxed{
    \sum_{q=1}^{H_A}\frac1{c_q}
      \sum_S\bigl(\mu_q^{\mathcal C}(S)-s_q(S)\bigr)_+
                              =o_A(W).}                \tag{3.5}
   \]

All objects may depend jointly on \(A,m\). One common integral
completion and one common factor must serve every depth in the window.
The local port paths may be fixed-layer Chung--Feller paths or general
paths (2.1); approximate ownership, fractional completion, and separate
depthwise completions do not satisfy the hypothesis.

### Theorem 3.1 (GPC\(_A\) implies fixed-window MWB)

If GPC\(_A\) holds, then its completed factor satisfies
\[
             \sum_{q=1}^{H_A}\frac{O_q(F)}{c_q}=o_A(W).
                                                               \tag{3.6}
\]

#### Proof

For the chosen quota \(b_q\), (3.2)--(3.4) give pointwise
\[
 \mu_q^F-b_q
   =\mu_q^{\mathcal M}+\mu_q^{\mathcal C}-b_q
   =\mu_q^{\mathcal C}-s_q.                            \tag{3.7}
\]
Hence
\[
 \sum_S(\mu_q^F(S)-b_q(S))_+
   =\sum_S(\mu_q^{\mathcal C}(S)-s_q(S))_+.           \tag{3.8}
\]
The minimum in (1.5) is no larger than its value at this \(b_q\).
Multiply by \(1/c_q\), sum, and use (3.5). \(\square\)

For the exhibited quota-safe core and the exhibited quota \(b_q\), (3.5)
is exactly its weighted completion spill. It is not logically necessary
for the completed factor: a different balanced quota may give smaller
overload. Indeed, taking \(\mathcal M=\varnothing\) makes this normal form
the direct port-restricted fixed-window overload assertion. Thus direct
(0.1), not (3.5), is the logically minimal unlabelled hypothesis.

## 4. Completion and uniform-envelope corollaries

### Corollary 4.1 (quota-safe near-factor rate)

In GPC\(_A\), put
\[
                         R=|\mathcal C|=|D_m\setminus G|.       \tag{4.1}
\]
If
\[
                         R\,S_A(m)=o_A(B),                      \tag{4.2}
\]
then (3.5) holds without any further information about the shallow
shadows of the completion. On a fixed Gaussian window, (4.2) is
equivalent to
\[
                         R=o_A(B/\sqrt m).                       \tag{4.3}
\]

#### Proof

Every cyclic row contributes exactly \(n\) pointed depth-\(q\)
intervals, so
\[
                         \sum_S\mu_q^{\mathcal C}(S)=nR.         \tag{4.4}
\]
Since \(s_q\ge0\),
\[
 \sum_S(\mu_q^{\mathcal C}(S)-s_q(S))_+
 \le\sum_S\mu_q^{\mathcal C}(S)=nR.                            \tag{4.5}
\]
The left side of (3.5) is therefore at most
\[
                         nR S_A(m)=W\,\frac{R S_A(m)}B=o_A(W).
\]
Lemma 1.1 proves the equivalence with (4.3). \(\square\)

The rate (4.3) is the universal envelope obtained from the number \(R\)
of uncontrolled rows alone: each such row has \(n\) occurrences at every
one of \(\Theta_A(\sqrt m)\) depths. No admissible port completion is
claimed to attain this bound simultaneously at all depths. A larger
completion may still work, but its structured residual spill must then be
bounded directly by (3.5).

There is a second useful form for a growing phase-layer construction which
first produces a full \(B\)-row family and then repairs exact ownership.
The provisional family need not itself be an exact middle factor.
For this comparison, define \(O_q\) for any full \(B\)-row family by the
same balanced-distance formula (1.5).

### Lemma 4.2 (row-replacement stability)

Let \(F,F'\) be two families of \(B\) cyclic rows which differ by at most
\(R\) row replacements. Then, at every depth,
\[
                         \|\mu_q^F-\mu_q^{F'}\|_1\le2nR,         \tag{4.6}
\]
and
\[
                         |O_q(F)-O_q(F')|\le nR.                 \tag{4.7}
\]

#### Proof

Deleting one row removes a nonnegative histogram of mass \(n\), and
inserting one row adds another such histogram. This proves (4.6).
Distance to a fixed set in a normed space is one-Lipschitz. Apply this to
(1.6):
\[
\begin{aligned}
 |O_q(F)-O_q(F')|
 &\le\frac12\|\mu_q^F-\mu_q^{F'}\|_1\\
 &\le nR.
\end{aligned}
\]
\(\square\)

Consequently a provisional growing phase design with
\[
 \max_{q\le H_A}\frac{O_q(F)}{c_q}
        =o_A(W/\sqrt m)                                \tag{4.8}
\]
survives any exact literal port completion using
\[
                         R=o_A(W/(n\sqrt m))            \tag{4.9}
\]
row replacements.

More generally, for a completed exact factor define
\[
                         D_A(F)=
       \max_{1\le q\le H_A}\frac{O_q(F)}{c_q}.          \tag{4.10}
\]
Then
\[
 \sum_{q\le H_A}\frac{O_q(F)}{c_q}\le H_A D_A(F).      \tag{4.11}
\]
Thus (4.8) for the completed factor is a convenient sufficient condition.
Because \(1\le c_q\le C_A\), it is equivalent, up to \(A\)-dependent
constants, to
\[
                         \max_{q\le H_A}O_q(F)
                         =o_A(W/\sqrt m).              \tag{4.12}
\]
The vanishing factor is necessary for this max-to-sum argument:
\(O(W/\sqrt m)\) at each of \(\Theta(\sqrt m)\) depths gives only an
\(O(W)\) bound.

## 5. The stronger common-labelled port theorem

Let \(\mathcal X=\binom{[n]}m\) be the middle-owner set. A balanced
nested resolution through \(H_A\) is a family
\[
 P_q:\mathcal X\longrightarrow\binom{[n]}{m-q}
\]
such that \(P_0(X)=X\), each \(P_{q+1}(X)\) deletes one coordinate from
\(P_q(X)\), and
\[
                         |P_q^{-1}(S)|\in\{c_q,c_q+1\}.           \tag{5.1}
\]
For the unique pointed occurrence of \(X\) in an exact factor \(F\), let
\(L_q^F(X)\) be its literal length-\((m-q)\) interval and put
\[
 e_q(F,P)=|\{X:L_q^F(X)\ne P_q(X)\}|.                 \tag{5.2}
\]

### Proposition 5.1 (labelled mismatch dominates overload)

For every exact factor and every common balanced nested resolution,
\[
                         O_q(F)\le e_q(F,P).            \tag{5.3}
\]
Consequently the fixed-window labelled assertion
\[
 \boxed{
 \sum_{q\le H_A}\frac{e_q(F_{A,m},P_{A,m})}{c_q}
                              =o_A(W)}                 \tag{5.4}
\]
implies (0.1).

#### Proof

Let
\[
 \beta_q(S)=|P_q^{-1}(S)|\in\{c_q,c_q+1\}.
\]
The two histograms \(\mu_q^F\) and \(\beta_q\) are obtained from the same
\(W\) labelled owners. Every agreeing owner contributes zero to their
difference, while a disagreeing owner moves one unit from one cell to
another. Hence
\[
                         \|\mu_q^F-\beta_q\|_1\le2e_q(F,P).       \tag{5.5}
\]
Since \(\beta_q\in\mathcal B_q\), (1.6) and (5.5) give (5.3).
Summation proves the last assertion. \(\square\)

The same \(P\) must be nested and integral through all depths. Independent
balanced quota vectors do not yield (5.4), although they are legitimate
in the weaker unlabelled theorem (0.1). No converse from small unlabelled
overload to a nearby common labelled resolution is known.

## 6. Fixed windows diagonalize exactly to MWB

### Theorem 6.1 (fixed-window growing-port theorem implies MWB)

Assume GPC\(_A\), or merely (0.1), for every fixed positive integer
\(A\) and every sufficiently large \(m\). Then there are
\(\omega(m)\to\infty\), with \(\omega(m)=o(\sqrt m)\), depths
\[
                         H_m=\lceil\sqrt m\,\omega(m)\rceil=o(m),       \tag{6.1}
\]
and one exact factor \(F_m\) at each \(m\) such that
\[
 \boxed{
 \sum_{q=1}^{H_m}\frac{O_q(F_m)}{c_q}=o(W).}           \tag{6.2}
\]
Thus MWB holds.

#### Proof

For every integer \(j\ge1\), choose \(T_j\) so large that whenever
\(m\ge T_j\), a fixed-window witness \(F_{j,m}\) satisfies
\[
 \sum_{q\le\lceil j\sqrt m\rceil}
          \frac{O_q(F_{j,m})}{c_q}\le\frac Wj.         \tag{6.3}
\]
Increase the thresholds so that \(T_j\ge j^8\) and \(T_j<T_{j+1}\).
Define
\[
 a(m)=\max\{j:T_j\le m\},\qquad
 \omega(m)=a(m),\qquad
 F_m=F_{a(m),m}.                                      \tag{6.4}
\]
Then \(a(m)\to\infty\), while \(T_{a(m)}\le m\) gives
\[
                         a(m)\le m^{1/8}.              \tag{6.5}
\]
Therefore
\[
 H_m\le m^{5/8}+1=o(m),\qquad
 \omega(m)=o(\sqrt m).                                \tag{6.6}
\]
Equation (6.3) with \(j=a(m)\) gives (6.2). The factor chosen for this
one moving window is common to all its depths. \(\square\)

No uniformity in \(A\) is required before diagonalization. Conversely,
one construction for a single fixed \(A\) does not prove MWB.

## 7. Complete implication from MWB to coefficient one

Let
\[
 M_q(F)=|\{S\in\binom{[n]}{m-q}:\mu_q^F(S)=0\}|.      \tag{7.1}
\]

### Lemma 7.1 (overload pays for holes)

For every exact factor,
\[
                         M_q(F)\le\frac{O_q(F)}{c_q}.  \tag{7.2}
\]

#### Proof

Choose a minimizing quota \(b_q\). Equality of the total masses of
\(\mu_q^F\) and \(b_q\) makes total underload equal total overload
\(O_q(F)\). Every hole has quota at least \(c_q\), so the holes contribute
at least \(c_qM_q(F)\) to the underload. \(\square\)

For the diagonal factors of Theorem 6.1,
\[
                         \sum_{q\le H_m}M_q(F_m)=o(W). \tag{7.3}
\]

### Lemma 7.2 (literal central-band word)

For every exact factor \(F\) and \(1\le H<m\), there is a literal
contiguous-OR word covering every target of sizes
\[
                         m-H,\ldots,m+H+1             \tag{7.4}
\]
in length at most
\[
 W+\frac{2H+1}{n}W+2\sum_{q=1}^{H}M_q(F).             \tag{7.5}
\]

#### Proof

For one row \(\pi\), put
\[
                         E_j=I_\pi(j,m-H).
\]
Emit
\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.       \tag{7.6}
\]
The OR of \(t\) consecutive emitted letters beginning at \(E_j\) is
\[
 \bigvee_{u=0}^{t-1}E_{j+u}
                  =I_\pi(j,m-H+t-1)                  \tag{7.7}
\]
for \(1\le t\le2H+2\). Thus the row block literally realizes every
cyclic interval in (7.4). There are \(B=W/n\) rows, and each block has
\(n+2H+1\) letters.

At lower size \(m-q\), append every target missed by the factor as one
literal letter. Complementation sends a missed lower interval bijectively
to a missed upper interval of size \(m+1+q\), so the two sides require
exactly \(2M_q(F)\) repairs. This proves (7.5). \(\square\)

We use the audited product-SCD tail lemma in its exact form:

### Lemma 7.3 (product-SCD two-tail word)

There is an explicit literal word of length at most
\[
                         2L_m(m-H-1)                  \tag{7.8}
\]
covering every remaining odd-dimensional target, where
\[
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
       A_m(a)w_m(a)C_m(r-a),                          \tag{7.9}
\]
\[
 A_m(a)=\binom ma-\binom m{a-1},\qquad
 w_m(a)=
 \begin{cases}m,&a=0,\\m-2a+1,&a>0,\end{cases}        \tag{7.10}
\]
and
\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}                                          \tag{7.11}
\]
Uniformly whenever
\[
                         H/\sqrt m\longrightarrow\infty,\qquad
                         H\le m/2,                     \tag{7.12}
\]
one has
\[
                         L_m(m-H-1)=o\binom{2m}m.      \tag{7.13}
\]

#### Proof

Take symmetric-chain decompositions of two disjoint \(m\)-cubes. Pair
chains whose minimum ranks \(a,b\) satisfy \(a+b\le m-H-1\), and write
the reverse increment word of the first chain followed by the forward
increment word of the second. A crossing interval realizes every member
of the corresponding lower product-chain tail; the symmetric upper
endpoints realize the upper tail without complementing an OR witness.
There are \(A_m(a)\) first chains of minimum rank \(a\), \(w_m(a)\)
usable positions on such a chain, and
\[
 \sum_{b\le r-a}A_m(b)=C_m(r-a)
\]
choices of the second chain. This gives (7.9), and the audited
one-coordinate tail lift gives the factor two in (7.8).

For (7.13), write \(x=\lfloor m/2\rfloor-a\). After normalization by
\(2^m\), the
weights \(A_m(a)w_m(a)\) form a tight family on the scale
\(x=O(\sqrt m)\); this follows directly from
\[
 A_m(a)=\binom ma\,\frac{m-2a+1}{m-a+1}               \tag{7.14}
\]
and the standard central-binomial ratio bound, for an absolute constant
\(C\),
\[
 \frac{\binom m{\lfloor m/2\rfloor-x}}
      {\binom m{\lfloor m/2\rfloor}}
                              \le C e^{-2x^2/m}.       \tag{7.15}
\]
For every fixed \(K\), the contribution from \(x>K\sqrt m\) is bounded
by a constant multiple of
\(\int_K^\infty(1+u^2)e^{-2u^2}\,du\), uniformly in \(m\).
On \(x\le K\sqrt m\), (7.11) and (7.15), with
\(H/\sqrt m\to\infty\), make
\[
 \frac{C_m(m-H-1-a)}
      {\binom m{\lfloor m/2\rfloor}}\longrightarrow0
\]
uniformly. First let \(m\to\infty\), then \(K\to\infty\). Since
\[
 2^m\binom m{\lfloor m/2\rfloor}
                         =\Theta\!\binom{2m}m,         \tag{7.16}
\]
equation (7.13) follows. \(\square\)

Combining Lemmas 7.1--7.3 gives the exact finite inequality
\[
\boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 W+\frac{2H_m+1}{2m+1}W\\
 &+2\sum_{q\le H_m}M_q(F_m)
  +2L_m(m-H_m-1).
\end{aligned}}                                        \tag{7.17}
\]
The second term is \(o(W)\) because \(H_m=o(m)\), the third is \(o(W)\)
by (7.3), and the last is \(o(W)\) by
\(H_m/\sqrt m=\omega(m)\to\infty\). Hence
\[
                         \nu(2m+1)\le W+o(W).          \tag{7.18}
\]

The standard one-coordinate lift gives
\[
                         \nu(2m+2)\le2\nu(2m+1),       \tag{7.19}
\]
while
\[
                         \binom{2m+2}{m+1}
                         =2\binom{2m+1}m.             \tag{7.20}
\]
Together with the width lower bound, (7.18)--(7.20) prove (0.2) in both
parities.

If a future port theorem holds only when \(2m+1\) is prime, the
preceding-prime theorem and repeated one-coordinate lifts still imply
coefficient one in all dimensions. Such a prime-subsequence theorem does
not, however, prove MWB at composite odd dimensions.

## 8. Adversarial audit and the exact unproved boundary

### 8.1 Exactness gates which cannot be weakened

1. **Ports, not ordinary transversality.** The distinguished \(D_s\)-set
   must be an endpoint of the infinity-cut path. An internal Dyck state
   does not glue to the ordered parent collar.
2. **Both ownership shores.** Phase balance controls the \(X\)-shore
   only. Exact aggregate \(Y\)-ownership is also necessary.
3. **Pointwise complement monodromy.** Two incidence matchings may satisfy
   every degree equation and still join the wrong endpoint pairs or leave
   alternating cycles.
4. **Joint ambient completion.** Separately exact local packets can fail
   when protected windows meet more than one packet. Overlapping or nested
   choices must be completed jointly before their shadows are counted.
5. **Literal full-word profiles.** First-edge diversity, layer marginals,
   and adjacent-union colours do not determine length-\((m-q)\) cyclic
   intervals. Equations (2.4) and (2.7), with all carriers and collars,
   are the relevant data.
6. **One factor for the whole window.** Factors or completions chosen
   independently at different depths cannot be summed.

### 8.2 Why hole/PCap control does not imply MWB

The PPR statistic from the earlier synthesis uses overload above the
translation-orbit cap \(n=2m+1\) and then controls actual holes after a
phase assignment. On a fixed Gaussian window, by contrast,
\(c_q=O_A(1)\).

The gap is real even for an abstract full-mass histogram. At a depth with
\(c_q\ge2\), put load one on half the \(N_q\) targets and distribute the
remaining mass as evenly as possible over the other half. Then there are
no holes, every load is \(O_A(1)\ll n\), and hence the cap-\(n\)
overload is zero. But the first half alone contributes
\[
                         \frac{c_q-1}{2}N_q=\Theta_A(W)            \tag{8.1}
\]
to the balanced underload, so \(O_q=\Theta_A(W)\).
Thus
\[
 \text{actual holes }o(W)
 \quad\not\Longrightarrow\quad
 \text{balanced overload }o(W).                       \tag{8.2}
\]
PPR remains a valid route to coefficient one; the claim that it implies
fixed-window MWB requires an additional theorem and must not be used.

### 8.3 What is proved and what remains open

Proved here:

* GPC\(_A\) implies fixed-window MWB exactly, with all floor baselines
  retained.
* A quota-safe completable port core may leave
  \(o_A(\operatorname {Cat}_m/\sqrt m)\) arbitrary rows.
* The same rate is the universal row-count stability envelope for
  repairing a full growing phase design by row replacements.
* The common-labelled theorem (5.4) is stronger and also sufficient.
* Fixed-window witnesses diagonalize to MWB with no uniformity in \(A\),
  and MWB gives the literal coefficient-one word.

The logically minimal remaining statement is direct (0.1) for one
completed exact factor; this is precisely fixed-window MWB and contains
no constructive information.

The clean nonvacuous theorem for the growing-port route is still unproved:

> **Growing-port near-completion theorem.** For every fixed \(A\), choose
> a scale \(s=s_A(m)\to\infty\), construct a globally compatible core
> from audited parent-aligned \(D_s\)-port path packets, and prove that it
> is quota-safe through \(H_A\) and admits one exact marked-monodromy
> completion leaving
> \[
>                  o_A(\operatorname {Cat}_m/\sqrt m)
> \]
> rooted rows.

More generally the completion may be larger only if the same construction
proves the structured weighted spill (3.5). The row-count-only target is
a quota-safe exact-completable core leaving
\[
                         o_A(\operatorname {Cat}_m/\sqrt m)            \tag{8.3}
\]
rooted rows. Mere existence of a noncanonical growing \(D_s\)-port
factor, fixed-layer Chung--Feller balance, marginal Hall feasibility, or
an \(o(\operatorname {Cat}_m)\) completion leave does not establish
(3.5).

No current July 26 construction proves this nonvacuous near-completion
theorem or the more general structured-spill version. Therefore this
report does not prove MWB or coefficient one; it identifies and proves
the exact remaining implication for the growing-port lane.

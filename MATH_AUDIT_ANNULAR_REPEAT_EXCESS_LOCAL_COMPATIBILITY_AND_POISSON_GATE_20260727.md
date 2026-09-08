# Annular repeat excess: compatible collision tuples and the Poisson gate

Date: 2026-07-27

Scope: the ordinary cyclic-packet hypergraph at the first Gaussian-annulus
rank. This note attacks only the implication

\[
 \text{rank-}q_0\text{ packet matching with leave }O(N_{q_0}/\sqrt m)
 \quad\Longrightarrow\quad
 \sum_{q\ge q_0}\widetilde E_q=o(W).
\]

## 0. Verdict

Put

\[
 n=2m,\qquad R=m-q_0,\qquad s=R-d,
 \qquad q_0=a\sqrt m+O(1),
\]

where \(1\le d\le (b-a)\sqrt m+O(1)\). The following facts are rigorous.

1. If two independently uniform cyclic packets are conditioned to contain
   the same depth-\((q_0+d)\) target \(S\in\binom{[n]}s\), then their
   expected number of common entrance-rank \(R\)-targets is

   \[
   \Xi_d=
   \frac{(d+1)^2}{\binom{n-s}{d}}
   +4\sum_{k=1}^{s-1}
      \frac1{\binom sk\binom{n-s}{d+k}}
   +\frac{(n-2R+d+1)^2}{\binom{n-s}{R}}.                 \tag{0.1}
   \]

   Consequently

   \[
   \Xi_1=\frac4{n-R+1}+O(m^{-2})=\frac{4+o(1)}m,
   \qquad
   \Xi_d=O(m^{-2})\quad(d\ge2),                         \tag{0.2}
   \]

   uniformly in the displayed annular range.

2. Hence, for every fixed deeper target \(S\), two packets through \(S\)
   have disjoint entrance traces with probability \(1-O(1/m)\). More
   generally, for \(j=o(\sqrt m)\), a \(j\)-tuple of independent packets
   through \(S\) is already an entrance matching with probability

   \[
   1-O(j^2/m).                                           \tag{0.3}
   \]

   In particular, for every \(j=o(\sqrt m)\) there exist \(j\) genuinely
   entrance-disjoint packets all repeating one prescribed deeper target.
   This is a literal matching, not a fractional example.

3. Summed over all deeper targets, the catalogue of entrance-compatible
   packet pairs carries asymptotically the same common-\(s\)-interval mass
   as the unrestricted packet-pair catalogue. Entrance disjointness is
   therefore not a local decorrelation mechanism for deeper colours.

4. If an entrance matching is locally pseudorandom in the standard
   factorial-moment sense at one macroscopic deeper depth
   \(d=c\sqrt m+O(1)\), \(c>0\), then its deeper load is asymptotically
   Poisson and it has

   \[
   H_{q_0+d}=(e^{-\lambda_c}+o(1))N_{q_0+d}=\Theta_{a,c}(W),
   \qquad
   \lambda_c=e^{2ac+c^2}.                                \tag{0.4}
   \]

   Thus \(\widetilde E_{q_0+d}=\Theta(W)\). A slow bite which merely
   regenerates the entrance links and treats every compatible packet
   symmetrically is expected to fail the hereditary-repeat gate, not prove
   it. A successful process must be explicitly colour-biased or
   compensated across depths.

What is **not** proved is a near-spanning integral counterexample. The
local compatible tuples in (0.3) do not by themselves extend to a matching
with leave \(O(N_{q_0}/\sqrt m)\). Accordingly the universal deterministic
implication remains open. What is refuted is the proposed route from
entrance matching plus ordinary local pseudorandomness to the repeat bound.

## 1. Conditional entrance-overlap energy

Work with directed cyclic orders modulo rotation; the same probabilities
hold after quotienting by reversal. For \(1\le u<n\), the number of
packets containing a fixed \(u\)-set as a cyclic interval is

\[
 D_u=u!(n-u)!.
\]

Fix \(S\in\binom{[n]}s\), and choose a packet \(P\) uniformly conditional
on \(S\in E_s(P)\). For \(A\in\binom{[n]}R\), put

\[
 p_A=\Pr(A\in E_R(P)\mid S\in E_s(P)).                    \tag{1.1}
\]

Write

\[
 M=n-s=n-R+d,\qquad c=M-R=n-2R+d=2q_0+d.
\]

### Lemma 1.1 (all conditional probabilities)

If \(S\subset A\), then

\[
 p_A=\frac{d+1}{\binom Md}.                                \tag{1.2}
\]

If \(|S\setminus A|=k\), \(1\le k\le s-1\), then

\[
 p_A=\frac{2}{\binom sk\binom M{d+k}}.                    \tag{1.3}
\]

If \(A\cap S=\varnothing\), then

\[
 p_A=\frac{c+1}{\binom MR}.                                \tag{1.4}
\]

#### Proof

Use the exact unequal-interval codegree formula. In the containment case,

\[
 \frac{(R-d)!(d+1)!(n-R)!}{(R-d)!(n-R+d)!}
 =\frac{d+1}{\binom{n-R+d}{d}}.
\]

For \(|S\setminus A|=k\), the partially overlapping block count divided by
\(D_s=s!M!\) is

\[
 \frac{2(d+k)!(s-k)!k!(M-d-k)!}{s!M!}
 =\frac2{\binom sk\binom M{d+k}}.
\]

The disjoint block count similarly gives

\[
 \frac{R!(c+1)!}{M!}=\frac{c+1}{\binom MR}.
\]

This proves the three formulas. \(\square\)

### Theorem 1.2 (exact conditional collision energy)

For independent packets \(P,P'\), both conditioned to contain \(S\),

\[
 \mathbb E\,|E_R(P)\cap E_R(P')|=\Xi_d,                 \tag{1.5}
\]

where \(\Xi_d\) is (0.1).

#### Proof

By independence, the left side is \(\sum_Ap_A^2\). There are
\(\binom Md\) containing \(R\)-sets. For \(1\le k\le s-1\), there are
\(\binom sk\binom M{d+k}\) sets with \(|S\setminus A|=k\). Finally there
are \(\binom MR\) disjoint \(R\)-sets. Substitution of Lemma 1.1 gives
(0.1). \(\square\)

### Corollary 1.3 (uniform annular estimate)

Uniformly for \(1\le d\le (b-a)\sqrt m+O(1)\), equations (0.2) hold.

#### Proof

For \(d=1\), the containment term is \(4/M\). The first partially
overlapping term is \(O(m^{-3})\), and the remaining terms form a
geometrically decreasing binomial tail up to reversal of the binomial
coefficients. The disjoint term is

\[
 \exp[-\Omega_a(\sqrt m\log m)].
\]

For \(d\ge2\), the containment term is at most
\(9/\binom M2=O(m^{-2})\) (and then decreases superpolynomially in \(d\)
on the annular scale). The partial-overlap sum is \(O(m^{-3})\), by the
same ratio estimate, and the disjoint term remains superpolynomially
small. \(\square\)

## 2. Compatible collision tuples

Call packets entrance-compatible when their rank-\(R\) traces are disjoint.

### Theorem 2.1 (local collision tuples survive the matching constraint)

Let \(P_1,\ldots,P_j\) be independent uniform packets conditioned to
contain the same \(s\)-target \(S\). Then

\[
 \Pr\big(E_R(P_i)\cap E_R(P_{i'})=\varnothing
          \text{ for all }i\ne i'\big)
 \ge 1-\binom j2\Xi_d.                                    \tag{2.1}
\]

Consequently (0.3) holds, and for every \(j=o(\sqrt m)\) there is a
literal \(j\)-packet entrance matching whose depth-\((q_0+d)\) load at
\(S\) is \(j\).

#### Proof

For one pair, Markov's inequality and Theorem 1.2 give

\[
 \Pr(E_R(P_i)\cap E_R(P_{i'})\ne\varnothing)\le\Xi_d.
\]

Take a union bound over the \(\binom j2\) pairs. If the right side tends
to one, at least one compatible tuple exists. \(\square\)

This theorem makes the limitation of the immediate-extension argument
exact. At \(d=1\), two packets through \(S\) use two entrance extensions
each, but the probability of an extension collision is only \(4/m+o(1/m)\).
At \(d\ge2\) even that loss drops to \(O(m^{-2})\).

### Corollary 2.2 (global compatible-pair census)

Let \(\Omega_n\) be the directed packet catalogue. Then

\[
 \sum_{S\in\binom{[n]}s}
 \#\{(P,P'):\ S\in E_s(P)\cap E_s(P'),\
                   E_R(P)\cap E_R(P')=\varnothing\}
 =(1-O(m^{-1}))N_sD_s^2.                                  \tag{2.2}
\]

Moreover, two independent unrestricted packets have disjoint entrance
traces with probability \(1-O(n^2/N_{q_0})=1-o(1)\). Hence the mean
number of common \(s\)-intervals of a uniformly chosen compatible packet
pair is

\[
 (1-o(1))\frac{n^2}{N_s}.                                  \tag{2.3}
\]

#### Proof

For each \(S\), Theorem 2.1 with \(j=2\) leaves a
\(1-O(m^{-1})\) fraction of the \(D_s^2\) ordered packet pairs. Sum over
\(S\). For the second assertion, the expected number of common entrance
targets of two unrestricted packets is exactly \(n^2/N_{q_0}\); Markov's
inequality gives the compatibility probability. Finally use

\[
 \frac{D_s}{|\Omega_n|}=\frac n{N_s}.
\]

\(\square\)

Thus neither maximum codegree nor the complete pair profile supplies the
desired deterministic repeat estimate. Compatible collision pairs occur
at their unrestricted first-order density.

## 3. An exact twin packet with linear first-deeper overlap

The preceding collision supply can be made macroscopic inside one
two-packet matching.

Fix a cyclic order

\[
 P=(x_0,x_1,\ldots,x_{n-1})
\]

and partition its positions into the consecutive dominoes
\(\{0,1\},\{2,3\},\ldots,\{n-2,n-1\}\). Define

\[
 P^\tau=(x_1,x_0,x_3,x_2,\ldots,x_{n-1},x_{n-2}).          \tag{3.1}
\]

### Theorem 3.1 (domino twin)

For every \(2\le \ell\le n-2\),

\[
 |E_\ell(P)\cap E_\ell(P^\tau)|
 =
 \begin{cases}
 n/2,&\ell\text{ even},\\
 0,&\ell\text{ odd}.
 \end{cases}                                               \tag{3.2}
\]

In particular, on every parameter subsequence for which \(R\) is odd,
\[
 E_R(P)\cap E_R(P^\tau)=\varnothing,\qquad
 |E_{R-1}(P)\cap E_{R-1}(P^\tau)|=n/2.                     \tag{3.3}
\]

#### Proof

Identify positions with \(\mathbb Z_n\), and let \(\tau\) exchange the two
positions of every domino. A \(P^\tau\)-interval with position set \(J\)
has label set equal to the \(P\)-position set \(\tau(J)\).

If \(\ell\) is even and \(J\) starts at an even position, then \(J\) is a
union of whole dominoes, so \(\tau(J)=J\). These are the \(n/2\) common
intervals. If an even-length \(J\) starts at an odd position, its two
boundary dominoes are cut. Swapping their singleton positions creates two
gaps, so \(\tau(J)\) is not a cyclic interval.

If \(\ell\) is odd, exactly one of the two boundary dominoes contributes
an unmatched singleton on each side. Swapping those singleton positions
again creates a gap, so \(\tau(J)\) is not a cyclic interval. The excluded
lengths \(1,n-1\) are precisely the singleton/complement exceptions. This
proves (3.2), and (3.3) follows. \(\square\)

Call
\[
 Q(P)=E_R(P)\,\dot\cup\,E_R(P^\tau)
\]
a domino-twin superpacket. When \(R\) is odd it is a legitimate
\(2n\)-set on the entrance shore.

### Corollary 3.2 (conditional near-factor counterexample)

Suppose the domino-twin superpacket hypergraph has a matching of \(T\)
superpackets. Regard its members as \(2T\) ordinary cyclic packets. Then

\[
 E_{q_0+1}\ge \frac{nT}{2}.                                \tag{3.4}
\]

If the superpacket matching covers
\[
 2nT=N_{q_0}-O(N_{q_0}/\sqrt m),
\]
then
\[
 \boxed{\widetilde E_{q_0+1}\ge(1/4-o(1))N_{q_0}
        =\Theta_a(W).}                                     \tag{3.5}
\]

#### Proof

Each twin contributes two occurrences on each of its \(n/2\) common
\((R-1)\)-targets. Adding those two occurrences raises ordinary repeat
excess by at least one, regardless of occurrences supplied by earlier
twins. Hence (3.4). The forced floor at this rank is at most
\[
 N_{q_0}-N_{q_0+1}+O(N_{q_0}/\sqrt m)=O_a(W/\sqrt m).
\]
Substitute \(T=(1+o(1))N_{q_0}/(2n)\) into (3.4). \(\square\)

The superpacket catalogue is invariant under relabelling, so its uniform
weight is an exact fractional entrance cover, and every one of its columns
already contains the linear-overlap twin. This is a fractionally saturated
catalogue-level counterarchitecture, not yet a fractional counterexample
to the nonlinear repeat objective. What remains unproved is an integral
near-factor of this \(2n\)-uniform superpacket hypergraph. Establishing one
would refute the universal deterministic implication outright. Conversely,
any claimed black-box entrance matching theorem broad enough to cover this
paired catalogue would automatically produce the counterexample (3.5).

This twin construction is stronger than the one-target tuples of
Theorem 2.1: it repeats a positive fraction of every packet's deeper
occurrences while preserving exact entrance disjointness inside the pair.

## 4. The exact deterministic pair-energy certificate

For an entrance matching \(\mathcal M\) of \(K\) packets, write

\[
 \mu_s(T)=|\{P\in\mathcal M:T\in E_s(P)\}|,
 \qquad G=nK,
\]

and define

\[
 \mathcal P_s(\mathcal M)
 =\sum_T\binom{\mu_s(T)}2
 =\sum_{\{P,P'\}\subseteq\mathcal M}|E_s(P)\cap E_s(P')|. \tag{4.1}
\]

Let \(\mathcal P_s^{\min}(G)\) be the minimum of
\(\sum_T\binom{x_T}2\) over nonnegative integer vectors of length \(N_s\)
and total mass \(G\); it is attained by the two adjacent values
\(\lfloor G/N_s\rfloor,\lceil G/N_s\rceil\).

### Lemma 4.1 (pair energy dominates repeat excess above the floor)

\[
 \boxed{
 \widetilde E_{q_0+d}(\mathcal M)
 \le \mathcal P_s(\mathcal M)-\mathcal P_s^{\min}(G).}       \tag{4.2}
\]

#### Proof

If \(G\le N_s\), then \(\mathcal P_s^{\min}=0\) and
\((x-1)_+\le\binom x2\) coordinatewise. If \(G>N_s\), fill each zero
coordinate by transferring a unit from a coordinate of load at least two.
The number of transfers is the hole count, which equals
\(\widetilde E_{q_0+d}\). Every transfer lowers pair energy by at least
one. The resulting positive vector still has pair energy at least the
balanced minimum. \(\square\)

Equation (4.2) is a valid deterministic sufficient inequality, but it does
not follow from entrance disjointness. Corollary 2.2 shows that the
available compatible-pair catalogue has the full generic common-interval
mass. Any proof through (4.2) must deliberately select a highly
non-generic set of compatible pairs.

## 5. Why an unbiased regenerated bite gives the wrong answer

The preceding census admits a precise conditional no-go.

Fix \(d=c\sqrt m+O(1)\), where \(0<c<b-a\), and put

\[
 \lambda_m=\frac{nK}{N_s}.
\]

For a matching with entrance leave \(O(N_{q_0}/\sqrt m)\),

\[
 \lambda_m=e^{2ac+c^2+o(1)}=: \lambda_c>1.                \tag{5.1}
\]

### Definition 5.1 (secondary local pseudorandomness)

A sequence of entrance matchings is factorial-moment pseudorandom at
depth \(s\) if for some \(J=J(m)\to\infty\), \(J=o(\sqrt m)\),

\[
 \frac1{N_s}\sum_T(\mu_s(T))_j=(1+o(1))\lambda_m^j
 \quad\text{uniformly for }0\le j\le J,                  \tag{5.2}
\]

where \((x)_j=x(x-1)\cdots(x-j+1)\).

### Theorem 5.2 (Poisson obstruction)

Under (5.2),

\[
 \#\{T:\mu_s(T)=0\}=(e^{-\lambda_c}+o(1))N_s.             \tag{5.3}
\]

In particular,

\[
 \widetilde E_{q_0+d}=\Theta_{a,c}(W),                    \tag{5.4}
\]

so the annular aggregate repeat criterion fails already at this one depth.

#### Proof

Bonferroni's inequalities give, for every odd/even truncation index \(J\),

\[
 \sum_{j=0}^{J_-}(-1)^j\frac1{j!}
   \frac1{N_s}\sum_T(\mu_s(T))_j
 \le \frac1{N_s}\#\{T:\mu_s(T)=0\}
 \le
 \sum_{j=0}^{J_+}(-1)^j\frac1{j!}
   \frac1{N_s}\sum_T(\mu_s(T))_j.
\]

Use (5.2), then let \(J\to\infty\). The two truncated exponential sums
converge to \(e^{-\lambda_c}\), proving (5.3). Since (5.1) is bounded
strictly above one, \(nK>N_s\) for large \(m\). The exact conservation
identity therefore identifies the hole count with
\(\widetilde E_{q_0+d}\). Finally \(N_s=\Theta_{a,c}(W)\). \(\square\)

The tuple range in Theorem 2.1 is exactly large enough to support all the
fixed-order factorial moments in (5.2). Thus an ACLE/MDLE theorem which
only proves that the unbiased slow bite follows the uniform compatible
catalogue will naturally lead to (5.2), and hence to the wrong coloured
outcome. The desired process must include a drift term which reacts to
the deeper path-colour loads.

## 6. Consequences for the annular programme

The present gate separates into two genuinely different tasks.

1. **Entrance matching:** regenerate the rank-\(R\) link hierarchy down to
   leave \(O(N_{q_0}/\sqrt m)\).
2. **Colour compensation:** at the same time, bias packet acceptance so
   that the common-interval pair energy in (4.2), or a weaker one-sided
   surrogate, approaches its integer floor at every deeper rank.

The first task alone does not make the second automatic. In fact, if the
first task is proved in a form asserting secondary uniformity, Theorem 5.2
shows that it makes the second false.

The exact open deterministic question remains:

> Does every sufficiently large annular entrance catalogue contain a
> near-perfect packet matching which is deliberately non-Poisson in all
> of its sliding-intersection colours, with
> \(\sum_q\widetilde E_q=o(W)\)?

No near-spanning counterexample is constructed here, so this note does not
refute that existence statement. It does close the local-rigidity and
ordinary-unbiased-nibble approaches to it.

# From dependent mixed-frame Hall to nested flags: adversarial audit and the exact Hoffman patch

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

There are two distinct conclusions.

First, the dependent owner-frame Hall-quarantine theorem is correct. For a
polynomial uniform frame catalogue, one common integral owner-frame
assignment, respecting any feasible rounded type-bin quota vector, satisfies

\[
 \boxed{
 \sum_{q=1}^H
 \bigl(\operatorname {def}G_q^-+
       \operatorname {def}G_q^+\bigr)
 \le O(W/\sqrt m)+O(WH\varepsilon)+o(W)=o(W).}
 \tag{0.1}
\]

The proof needs no independence across targets or depths. For one frozen
state assignment, the deterministic inequality

\[
 |\mathcal Z|-|\Gamma(\mathcal Z)|
 \le\sum_T(1-Z_{T,q}^\pm)_+
 \tag{0.2}
\]

controls every Hall family simultaneously. Independence is used only
between the frame choices of distinct middle owners when estimating the
expectation of the right side.

Second, (0.1) does **not** by itself imply a nested Hoffman flow. The
depthwise matchings may choose incompatible target frames and incompatible
prefixes. The target-frame linking matrix has a determinant-two minor at
depths one and two. Thus the proposed direct composition has a genuine
gap.

The gap can be patched, without assuming cycle bundling, by augmenting the
polynomial catalogue to

\[
 J_{\rm flag}
 \le C m\,4^H\exp(CH^2/m).
 \tag{0.3}
\]

Fix a Boolean symmetric-chain decomposition first. The augmented catalogue
contains, for every middle owner, one balanced frame literalizing its
complete lower and upper truncated SCD flags. These flags give an explicit
integral flow in the fixed-target-frame Hoffman networks. In fact the
patched nested theorem has zero target error:

\[
 \boxed{
 \operatorname {def}G_q^-=
 \operatorname {def}G_q^+=0
 \quad(1\le q\le H),}
 \tag{0.4}
\]

with exact nested target ownership and no prefix incompatibility.

In the calibrated range \(H\le C_0\sqrt{m\log m}\),

\[
 J_{\rm flag}=W^{o(1)},\qquad HJ_{\rm flag}=o(W).
 \tag{0.5}
\]

The exact logical boundary is therefore:

\[
 \boxed{
 \begin{array}{c}
 \text{polynomial catalogue: one common owner assignment and }o(W)
 \text{ depthwise Hall quarantine};\\
 \text{\(W^{o(1)}\) augmented catalogue: exact integral nested flags and
 Hoffman flow};\\
 \text{complete isometric-cycle bundling: not used and not proved.}
 \end{array}}
 \tag{0.6}
\]

The augmentation is essential to the proof given here. No polynomial
fixed-flag literalization theorem is asserted.

## 1. First-principles setup for dependent owner rounding

Let

\[
 \mathcal M=\binom{[2m]}m,\qquad W=|\mathcal M|,
 \qquad
 \mathcal L_q^\pm=\binom{[2m]}{m\pm q},
 \qquad
 N_q=|\mathcal L_q^\pm|,
 \qquad
 \rho_q={N_q\over W}.
 \tag{1.1}
\]

Let \(\mathscr P=(P_1,\ldots,P_J)\) be a polynomial mixed-frame catalogue.
For a balanced type interval \(\mathcal B\), put

\[
 I(X)=\{j:f_{P_j}(X)\in\mathcal B\},
 \qquad
 a_X=|I(X)|,
 \qquad
 \alpha=J(1-\tau).
 \tag{1.2}
\]

Assume

\[
 (1-\varepsilon)\alpha\le a_X\le(1+\varepsilon)\alpha
 \tag{1.3}
\]

for every owner. For a lower target, let \(g_j^-(T)\) count full
\(P_j\)-pairs; for an upper target let \(g_j^+(T)\) count empty pairs. The
uniform target estimate is

\[
 {1-\varepsilon\over\rho_q}\alpha
 \le
 \sum_{\substack{j\\g_j^\pm(T)\in\mathcal B}}
 \lambda_{g_j^\pm(T),q}
 \le
 {1+\varepsilon\over\rho_q}\alpha,
 \tag{1.4}
\]

where

\[
 \lambda_{f,q}
 ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.
 \tag{1.5}
\]

Equation (1.4) follows from

\[
 \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f)
 \tag{1.6}
\]

and polynomial concentration. Choose the owner states independently:

\[
 A(X)\ \text{ is uniform on }I(X).
 \tag{1.7}
\]

The choice (1.7) is made once and is shared by all depths and both signs.
Write

\[
 f_X=f_{P_{A(X)}}(X),\qquad
 s_X=m-2f_X,\qquad
 d_X(q)=\binom{s_X}{q}.
 \tag{1.8}
\]

Let

\[
 s_*=\min_{f\in\mathcal B}(m-2f)
 ={m\over2}-O(\sqrt{m\log m}).
 \tag{1.9}
\]

## 2. Exact expectation and variance audit

For a lower target \(T\), define

\[
 Z_{T,q}^-=
 \sum_{X:T\sim^-_{A(X)}X}{\rho_q\over d_X(q)}.
 \tag{2.1}
\]

Define \(Z_{T,q}^+\) by the complementary upper incidence.

### Lemma 2.1 (expectation with every conditioning exposed)

For every \(T,q,\pm\),

\[
 {1-\varepsilon\over1+\varepsilon}
 \le\mathbb E Z_{T,q}^\pm
 \le {1+\varepsilon\over1-\varepsilon}.
 \tag{2.2}
\]

#### Proof

We prove the lower statement. Fix a frame \(j\) in which \(T\) has type
\(f\in\mathcal B\). The literal face graph in this frame is biregular with
source and target degrees

\[
 d^{\rm src}_{f,q}=\binom{m-2f}{q},
 \qquad
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}.
 \tag{2.3}
\]

Every compatible source \(X\) has the same type \(f\), hence \(j\in I(X)\)
and

\[
 \Pr(A(X)=j)={1\over a_X}.
 \tag{2.4}
\]

Therefore the contribution of frame \(j\) to the expectation is

\[
 \sum_{X:T\sim_j^-X}{1\over a_X}
       {\rho_q\over d^{\rm src}_{f,q}}.
 \tag{2.5}
\]

Using (1.3), this lies between

\[
 {\rho_q\over(1+\varepsilon)\alpha}
 {d^{\rm tar}_{f,q}\over d^{\rm src}_{f,q}}
 \quad\text{and}\quad
 {\rho_q\over(1-\varepsilon)\alpha}
 {d^{\rm tar}_{f,q}\over d^{\rm src}_{f,q}}.
 \tag{2.6}
\]

The degree ratio is \(\lambda_{f,q}\). Sum (2.6) over all allowed frames
and use (1.4). This proves (2.2). The upper calculation is its complement.
\(\square\)

For fixed \(T,q,\pm\), write

\[
 Z_{T,q}^\pm=\sum_XY_X.
 \tag{2.7}
\]

One owner variable \(Y_X\) already includes all of that owner's possible
frame states. Thus no false independence among frames of one owner is used.
Distinct \(Y_X\)'s are independent because (1.7) is ownerwise independent.

### Lemma 2.2 (variance with owner-state dependence retained)

Let

\[
 \beta_q={\rho_q\over\binom{s_*}{q}},
 \qquad
 M_\varepsilon={1+\varepsilon\over1-\varepsilon}.
 \tag{2.8}
\]

Then

\[
 \operatorname {Var}Z_{T,q}^\pm
 \le\beta_q\,\mathbb E Z_{T,q}^\pm
 \le M_\varepsilon\beta_q.
 \tag{2.9}
\]

#### Proof

For every state of owner \(X\),

\[
 0\le Y_X\le{\rho_q\over d_X(q)}
 \le\beta_q.
 \tag{2.10}
\]

Hence \(Y_X^2\le\beta_qY_X\). Using independence only across owners,

\[
\begin{aligned}
 \operatorname {Var}Z
 &=\sum_X\operatorname {Var}Y_X\\
 &\le\sum_X\mathbb EY_X^2\\
 &\le\beta_q\sum_X\mathbb EY_X
 =\beta_q\mathbb EZ.
\end{aligned}
\]

Apply (2.2). \(\square\)

## 3. The positive-part expectation and simultaneous-depth audit

The elementary pointwise inequality

\[
 (1-z)_+\le(1-\mu)_++|z-\mu|
 \tag{3.1}
\]

holds for every real \(z,\mu\). Take \(z=Z_{T,q}^\pm\) and
\(\mu=\mathbb EZ_{T,q}^\pm\). Lemmas 2.1--2.2 and
Cauchy--Schwarz give

\[
\begin{aligned}
 \mathbb E(1-Z_{T,q}^\pm)_+
 &\le(1-\mathbb EZ_{T,q}^\pm)_+
       +\mathbb E|Z_{T,q}^\pm-\mathbb EZ_{T,q}^\pm|\\
 &\le {2\varepsilon\over1-\varepsilon}
       +\sqrt{M_\varepsilon\beta_q}.
\end{aligned}
\tag{3.2}
\]

This step is sometimes misstated as a concentration theorem. It is only
the first absolute-moment bound

\[
 \mathbb E|Z-\mathbb EZ|\le\sqrt{\operatorname {Var}Z}.
 \tag{3.3}
\]

No tail estimate is needed.

All sums below are finite and nonnegative. Tonelli's theorem, or simply
repeated finite summation, therefore gives

\[
 \mathbb E
 \sum_{q=1}^H\sum_{\pm}\sum_T(1-Z_{T,q}^\pm)_+
 =
 \sum_{q=1}^H\sum_{\pm}\sum_T
       \mathbb E(1-Z_{T,q}^\pm)_+.
 \tag{3.4}
\]

Thus no independence across \(q\), signs, or targets is required. The same
single realization \(A\) occurs inside every term.

Since \(N_q=W\rho_q\le W\), (3.2) gives

\[
 \mathbb E D_q^\pm
 \le W\left(
 {2\varepsilon\over1-\varepsilon}
 +{\sqrt{M_\varepsilon}\over
       \sqrt{\binom{s_*}{q}}}\right),
 \tag{3.5}
\]

where

\[
 D_q^\pm=\sum_T(1-Z_{T,q}^\pm)_+.
 \tag{3.6}
\]

For \(a_q=\binom{s_*}{q}^{-1/2}\),

\[
 {a_{q+1}\over a_q}
 =\sqrt{{q+1\over s_*-q}}
 \le\sqrt{{H+1\over s_*-H}}=o(1).
 \tag{3.7}
\]

Therefore

\[
 \sum_{q=1}^Ha_q
 ={1+o(1)\over\sqrt{s_*}}
 ={\sqrt2+o(1)\over\sqrt m}.
 \tag{3.8}
\]

Summing (3.5) yields

\[
 \boxed{
 \mathbb E\sum_{q=1}^H(D_q^-+D_q^+)
 \le{(2\sqrt2+o(1))W\over\sqrt m}
 +{4WH\varepsilon\over1-\varepsilon}.}
 \tag{3.9}
\]

This is the audited expectation bound.

## 4. One deterministic shortfall controls every Hall cut

Fix a realization \(A\). In the frozen literal graph at depth \(q\),
one owner \(X\) has exactly \(d_X(q)\) incident targets. Hence, for every
target family \(\mathcal Z\),

\[
\begin{aligned}
 \sum_{T\in\mathcal Z}Z_{T,q}^\pm
 &=
 \sum_{X\in\Gamma_A(\mathcal Z)}
 {\rho_q\over d_X(q)}
 |\{T\in\mathcal Z:T\sim^\pm_{A(X)}X\}|\\
 &\le\rho_q|\Gamma_A(\mathcal Z)|
 \le|\Gamma_A(\mathcal Z)|.
\end{aligned}
\tag{4.1}
\]

Consequently,

\[
\begin{aligned}
 |\mathcal Z|-|\Gamma_A(\mathcal Z)|
 &\le\sum_{T\in\mathcal Z}(1-Z_{T,q}^\pm)\\
 &\le\sum_T(1-Z_{T,q}^\pm)_+=D_q^\pm.
\end{aligned}
\tag{4.2}
\]

Taking the maximum over \(\mathcal Z\) gives

\[
 \operatorname {def}G_q^\pm(A)\le D_q^\pm(A).
 \tag{4.3}
\]

Equations (3.9) and (4.3) prove the Hall-quarantine theorem before exact
quota repair.

## 5. Adversarial quota-repair audit

Let \(\mathcal R\) be the set of allowed frame/type bins,
\(R=|\mathcal R|=m^{O(1)}\). The fractional bin count is

\[
 B_r=\sum_{X\to r}{1\over a_X}.
 \tag{5.1}
\]

Let \(n_r\) be the random integral bin count under (1.7). Then

\[
 \mathbb En_r=B_r,\qquad
 \operatorname {Var}n_r\le B_r.
 \tag{5.2}
\]

Therefore

\[
 \mathbb E\sum_r|n_r-B_r|
 \le\sum_r\sqrt{B_r}
 \le\sqrt{R\sum_rB_r}
 =\sqrt{RW}.
 \tag{5.3}
\]

By applying Markov's inequality with threshold four times the expectation
to (3.9) and (5.3), there is one realization \(A_0\) such that

\[
 \sum_{q,\pm}D_q^\pm(A_0)
 =O(W/\sqrt m+WH\varepsilon),
 \tag{5.4}
\]

\[
 Q(A_0):=\sum_r|n_r-B_r|=O(\sqrt{RW}).
 \tag{5.5}
\]

Fix any feasible rounded quota vector \(b\), meaning that

\[
 |b_r-B_r|<1
 \tag{5.6}
\]

and some allowed owner assignment \(\Psi\) has bin counts \(b\).

### Lemma 5.1 (path-swap repair)

There is an allowed assignment \(A_1\) with exact bin counts \(b\), differing
from \(A_0\) on at most

\[
 r_0\le {R\over2}\sum_r|n_r-b_r|
 \le {R\over2}(Q(A_0)+R)
 \tag{5.7}
\]

owners.

#### Proof

For each owner on which \(A_0\) and \(\Psi\) differ, draw a directed arc
from its \(A_0\)-bin to its \(\Psi\)-bin. At bin \(r\), outdegree minus
indegree is \(n_r-b_r\).

Decompose the directed multigraph into directed cycles and unit paths from
surplus bins to deficit bins. Discard the cycles. Remove internal cycles
from the paths, so each retained path is simple and has at most \(R\)
arcs. There are exactly

\[
 {1\over2}\sum_r|n_r-b_r|
\]

path units. Reassign the owner labelling every retained path arc to its
\(\Psi\)-bin. Internal path bins lose and gain one owner, while the
endpoints correct one unit of surplus and deficit. Every reassignment is
allowed because it is an edge used by \(\Psi\). This proves (5.7).
\(\square\)

Because \(R,H\) are polynomial and \(W\) is exponential,

\[
 r_0=O(R^{3/2}\sqrt W+R^2)=o(W/H).
 \tag{5.8}
\]

### Lemma 5.2 (exact Lipschitz cost)

Changing the assigned frames of \(r\) owners changes every one-depth Hall
deficiency by at most \(r\). Hence its total two-sided cost through depth
\(H\) is at most \(2Hr\).

#### Proof

Delete the \(r\) changed owner vertices from the two frozen graphs. What
remains is identical. Deleting or restoring \(r\) owner vertices changes a
maximum matching number by at most \(r\); target cardinality is unchanged,
so deficiency changes by at most \(r\). Sum over \(H\) depths and two
signs. \(\square\)

Combining (5.4), (5.8), and Lemma 5.2 gives

\[
 \boxed{
 \sum_{q,\pm}\operatorname {def}G_q^\pm(A_1)
 \le
 O(W/\sqrt m+WH\varepsilon)+2Hr_0=o(W).}
 \tag{5.9}
\]

This completes the adversarial re-proof of (0.1).

## 6. Why depthwise Hall does not imply Hoffman feasibility

Fixing the owner frames makes each one-depth graph bipartite, but a nested
flag must use one common prefix path through all depths. Choosing the
target frame independently at every depth adds linking rows which are not
a directed incidence matrix.

The failure appears with two depths. There are literal path columns
\(p_1,p_2,p_3\) whose restrictions to one owner row \(X\), one depth-one
target row \(A\), and one depth-two target row \(B\) are

\[
 \begin{array}{c|ccc}
  &p_1&p_2&p_3\\ \hline
  X&1&0&1\\
  A&1&1&0\\
  B&0&1&1
 \end{array}.
 \tag{6.1}
\]

Its determinant is two. With one additional private path \(p_4\), the
equations

\[
 p_1+p_3=1,\qquad
 p_1+p_2=1,\qquad
 p_2+p_3=1,\qquad
 p_2+p_4=1
 \tag{6.2}
\]

have the fractional solution \(p_i=1/2\) and no integral solution.
Every displayed finite deletion path can be embedded literally by pairing
its deleted coordinates with distinct coordinates outside its root owner.

Thus neither separate Hall matchings nor a fractional linked path solution
can be rounded by a bare total-unimodularity claim. A fixed integral
target-frame partition is required before the Hoffman network becomes a
single-commodity flow.

## 7. The exact fixed-target-frame patch

Fix a symmetric-chain decomposition of \(2^{[2m]}\). Each chain contains
one middle owner \(X\) and has a radius \(d_X\). Put

\[
 r_X=\min\{d_X,H\}.
 \tag{7.1}
\]

Write its lower and upper truncated flags as

\[
 X\setminus\{a_1(X)\},
 \ldots,
 X\setminus\{a_1(X),\ldots,a_{r_X}(X)\},
 \tag{7.2}
\]

\[
 X\cup\{b_1(X)\},
 \ldots,
 X\cup\{b_1(X),\ldots,b_{r_X}(X)\}.
 \tag{7.3}
\]

Extend each list arbitrarily to \(H\) distinct elements of \(X\), respectively
\(X^c\), only for the frame-existence argument.

For one owner, let \(E_X\) be the event that a random perfect matching pairs
all marked \(a_i\)'s into \(X^c\setminus\{b_1,\ldots,b_H\}\), and all marked
\(b_i\)'s into \(X\setminus\{a_1,\ldots,a_H\}\). Then the lower and upper
marked directions are split at \(X\), distinct within each side, and
disjoint between the two sides.

The exact probability is

\[
 p_H
 ={((m-H)_{\underline H})^2
   \over\prod_{i=0}^{2H-1}(2m-2i-1)}.
 \tag{7.4}
\]

Uniformly for \(H\le m/4\),

\[
 p_H\ge4^{-H}\exp(-CH^2/m).
 \tag{7.5}
\]

Choose

\[
 J_{\rm flag}=\left\lceil{4m\over p_H}\right\rceil
 \tag{7.6}
\]

independent random frames. The probability that a fixed owner has no
successful frame is at most \(e^{-2m}\). Since \(W\le4^m\), a union bound
shows that a deterministic catalogue exists in which every owner has a
successful frame.

Under \(H\le C_0\sqrt{m\log m}\), the same catalogue may require the
successful frame to have balanced owner type. Conditional on \(E_X\), the
remaining matching is uniform on \(m-2H\) vertices on each shore. The
conditional mean number of full pairs is

\[
 {(m-2H)(m-2H-1)\over2(2m-4H-1)}
 ={m-2H\over4}+O(1).
 \tag{7.7}
\]

It differs from the unconditional central value by at most \(H/2+O(1)\).
Exposing the remaining matching gives a martingale with bounded
increments, hence

\[
 \Pr(|f_P(X)-\mathbb Ef_P(X)|>t\mid E_X)
 \le2e^{-ct^2/m}.
 \tag{7.8}
\]

After enlarging the constant width of the balanced band, the conditional
success probability is at least \(1/2\), uniformly in \(X\). This changes
(7.6) by at most an absolute factor.

Assign one successful frame \(\phi(X)\) to every owner. For each lower or
upper target in the truncated band, assign its target frame to be the frame
of the middle owner in its unique SCD chain.

### Theorem 7.1 (explicit integral nested-flag theorem)

The assignments above have the following properties.

1. Every middle owner uses exactly one balanced frame.
2. Every physical lower and upper target through depth \(H\) occurs on
   exactly one truncated SCD flag.
3. Every flag is a legal pair-flip prefix in its owner's assigned frame.
4. The lower and upper direction families at one owner are disjoint.
5. The fixed-target-frame lower and upper Hoffman networks have explicit
   integral feasible flows.

#### Proof

Symmetric chains partition every Boolean rank. Hence every target through
the band lies on exactly one chain and therefore on exactly one flag
(7.2) or (7.3). Event \(E_X\) makes every displayed step a legal distinct
pair direction in frame \(\phi(X)\).

Give the layered network a terminal arc at every level. In the lower
Hoffman network, send one unit from owner \(X\) down its path (7.2) and
terminate it after \(r_X\) steps. Owners with \(r_X=0\) terminate at the
root. Because the SCD chains are disjoint, every lower target node
through depth \(H\) has throughput exactly one. All transitions are legal
and all root supplies are one.

Do the same independently on the upper path (7.3), using the same owner
frame. This gives two explicit integral flows. Summing conservation over
an arbitrary vertex set proves every Hoffman inequality

\[
 \ell(\delta^-(S))\le u(\delta^+(S)).
 \tag{7.9}
\]

Thus the fixed-target-frame networks are feasible, and their displayed
flows already supply the required integral nested flags. \(\square\)

No arbitrary extension beyond the end of an SCD chain is sent through the
network. This point prevents spurious duplicate target incidences.

## 8. Exact error ledger

Let \(\mathscr P_{\rm poly}\) be the polynomial catalogue from Sections
1--5 and \(\mathscr P_{\rm flag}\) the augmented catalogue from Section 7.
Their union has size \(J_{\rm flag}+m^{O(1)}=W^{o(1)}\) in the calibrated
range.

The two verified integral outputs are:

| Ledger item | Polynomial dependent rounding | Augmented nested flags |
|---|---:|---:|
| Middle owners assigned twice or omitted | \(0\) | \(0\) |
| Type-bin quota error | \(0\) for any feasible rounded \(b\) | no prescribed bin vector; every chosen type is balanced |
| Aggregate lower/upper Hall quarantine | \(O(W/\sqrt m+WH\varepsilon)+o(W)\) | \(0\) |
| Nonliteral face assignments | \(0\) outside quarantine | \(0\) |
| Nonnested selected flags | not controlled | \(0\) |
| Hoffman cut violation | not asserted | \(0\) |
| Duplicate SCD target throughput | not applicable | \(0\) |
| Frame catalogue size | \(m^{O(1)}\) | \(Cm4^H\exp(CH^2/m)=W^{o(1)}\) |
| Frame-group interface toll at \(O(H)\) per group | \(m^{O(1)}H=o(W)\) | \(O(HJ_{\rm flag})=o(W)\) |
| Complete-cycle bundling | not proved | not assumed |

The table is deliberately two-column. The exact prescribed polynomial-bin
quotas and the augmented fixed-SCD flag assignment are not proved
simultaneously. Claiming both for one assignment would reintroduce the
target-frame linking gap of Section 6.

## 9. Final theorem and exact boundary

Combining the verified parts gives the following rigorous constant-one
statement before cycle bundling.

### Theorem 9.1 (integral nested flags with explicit interface cost)

If \(H\le C_0\sqrt{m\log m}\), there is a
\(W^{o(1)}\)-size pair-frame catalogue, one integral frame per middle
owner, and exact two-sided nested pair-flip flags through depth \(H\) such
that:

\[
 \begin{aligned}
 &\text{middle-owner error}=0,\\
 &\text{lower target error}=0,\\
 &\text{upper target error}=0,\\
 &\text{nested-prefix error}=0,\\
 &\text{Hoffman-flow error}=0,
 \end{aligned}
 \tag{9.1}
\]

and grouping by selected frame incurs at most

\[
 O(HJ_{\rm flag})=o(W)
 \tag{9.2}
\]

frame-interface toll.

This last quantity counts only changes of pair frame between frame groups.
It does not claim that the separate owner-rooted flags have already been
joined into \(o(W)\) contiguous pieces; that is part of the unproved cycle
or path-bundling stage.

The construction uses no whole-cycle assumption. It supplies owner-rooted
paths, not a partition into isometric \(2h\)-cycles.

For the original polynomial catalogue, the strongest proved common-frame
statement remains the audited \(o(W)\) literal Hall quarantine (5.9).
Turning that particular quota-preserving assignment into nested flags
would require a new adaptive target-frame Hoffman theorem. The
determinant-two minor shows why it does not follow from total unimodularity
alone.

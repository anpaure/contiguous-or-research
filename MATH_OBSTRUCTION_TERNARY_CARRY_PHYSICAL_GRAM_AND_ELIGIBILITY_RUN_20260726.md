# The phase-dense ternary carry has exponential physical Gram excess

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

Consider the phase-dense ternary-carry factor on the canonical
first-\(t\)-eligible-block macrocells from thread H. Write

\[
 W=\binom{2m}{m},\qquad
 N_q^-=\binom{2m}{m-q},\qquad
 N_q^+=\binom{2m}{m+q}=N_q^-,
 \qquad G=W-e^{-\Omega(m)}W.                           \tag{0.1}
\]

Let \(t=o(m)\), let \(h=2t\), and assume \(q\le H\le t\). In every
macrocell the carry factor has block-index word

\[
 1,2,\ldots,t
 \quad\text{repeated four times per \(2h\)-phase lap}.             \tag{0.2}
\]

The base-three carry changes the row matching at selected ports, but it
does not change (0.2). Consequently every depth-\(q\) lower or upper
shadow touches one cyclic interval of \(q\) positions in the ordered
first-\(t\) eligible list.

This forces an eligibility-free run in the physical target. If
\(\mathscr H_q^\epsilon\) is the set of physical rank-\((m+\epsilon q)\)
targets hit by the deterministic carry atlas, then, uniformly for
\(q=O(\sqrt m)\),

\[
 \boxed{
 {|\mathscr H_q^\epsilon|\over N_q^\epsilon}
 \le
 \delta_q:=
 O(m^{3/2})
 \left({29\over32}+o(1)\right)^{q/2},
 \qquad\epsilon\in\{-,+\}.}                           \tag{0.3}
\]

Hence \(\delta_q=o(1)\) whenever \(q/\log m\to\infty\). In particular,
for \(q=x\sqrt m+O(1)\), \(x>0\),

\[
 \boxed{
 M_q^\epsilon
 :=N_q^\epsilon-|\mathscr H_q^\epsilon|
 =(1-o(1))N_q^\epsilon=\Theta_x(W).}                  \tag{0.4}
\]

Thus the labelled-shadow gate

\[
 \sum_{q\le H}(M_q^-+M_q^+)=o(W)                     \tag{0.5}
\]

is false for the deterministic ternary-carry factor as soon as the
protected band contains one positive Gaussian depth.

The physical Gram excess can also be evaluated at the scale requested in
the preceding Gram theorem. Assume the asserted local macrocell shadow
injectivity. A macrocell then contributes a target set
\(\mathcal S_{a,j}\) of size

\[
                         K=24^t                       \tag{0.6}
\]

at every signed depth \(j=(q,\epsilon)\), and the number of macrocells is

\[
                         P={G\over K}.                 \tag{0.7}
\]

Put

\[
 d_j(T)=\#\{a:T\in\mathcal S_{a,j}\},                 \tag{0.8}
\]

\[
 R_j=\sum_{a\ne b}
 \left(
 |\mathcal S_{a,j}\cap\mathcal S_{b,j}|-{K^2\over N_j}
 \right),                                             \tag{0.9}
\]

and

\[
 \eta_j={N_j(R_j)_+\over P(P-1)K^2}.                 \tag{0.10}
\]

These are the actual deterministic carry quantities; no packetwise
independence is introduced. Since all \(G\) occurrences lie on at most
\(\delta_qN_j\) targets, Cauchy--Schwarz gives

\[
 \boxed{
 R_j\ge
 {G^2\over\delta_qN_j}
 -G-{G^2\over N_j}+{GK\over N_j}.}                    \tag{0.11}
\]

Therefore

\[
 \boxed{
 \eta_j\ge
 {G/\delta_q-G-N_j+K\over G-K}.}                      \tag{0.12}
\]

At \(q=x\sqrt m+O(1)\),

\[
 {G\over N_j}=e^{x^2+o(1)},\qquad {K\over G}=e^{-\Theta(m)},
                                                               \tag{0.13}
\]

so

\[
 \boxed{
 \eta_j\ge(1-o(1))\delta_q^{-1}
 \ge
 m^{-3/2}
 \left({32\over29}-o(1)\right)^{q/2}.}                \tag{0.14}
\]

In particular,

\[
 \sqrt{\eta_j}
 \ge
 m^{-3/4}
 \exp\left(
 {q\over4}\log{32\over29}-o(q)
 \right)\longrightarrow\infty                        \tag{0.15}
\]

at every positive Gaussian depth. Thus

\[
 \boxed{\sum_j\sqrt{\eta_j}\ne o(1);}                 \tag{0.16}
\]

indeed one summand diverges exponentially in \(\sqrt m\).

The obstruction is not caused by imperfect ternary mixing. The carry is
perfectly transitive on its \(3^t\) digit states after complete laps. The
problem is that all those states retain the same ordered macroblock
interval support. Base-three phase density mixes fine row labels inside
one forbidden quotient column; it does not mix the quotient columns.

## 1. Canonical macrocells and the invariant block word

Partition all but at most seven ground coordinates into labelled
eight-blocks

\[
                         B_1,\ldots,B_B,\qquad B=\Theta(m).         \tag{1.1}
\]

In each block use the 24-state associator support

\[
 \mathcal V=
 \left\{
 X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,\quad
 Y\in\{uw,ux,vw,vx\}
 \right\}.                                             \tag{1.2}
\]

A block is eligible for a set when its local restriction belongs to
\(\mathcal V\). Every member of \(\mathcal V\) has size four.

For a good middle owner \(X\), let

\[
                         I(X)=(i_1<\cdots<i_t)          \tag{1.3}
\]

be its first \(t\) eligible blocks. The canonical macrocell varies the
restrictions on these blocks through \(\mathcal V^t\) and freezes the
exterior. Thus every owner in the macrocell has the same ordered selected
list (1.3), and the macrocell has \(24^t\) owners.

In the ternary-carry factor the two cube directions in every selected
block occur in the Hamming order

\[
 \alpha_1,\ldots,\alpha_t,\,
 \beta_1,\ldots,\beta_t
 \quad\text{twice}.                                    \tag{1.4}
\]

Hence the block-index word is (0.2). The carry predicate changes which of
the two common-owner row matchings is used at a port. It never changes
the active block. Therefore every \(q\le t\) consecutive transitions
touch \(q\) distinct selected blocks forming a cyclic interval

\[
                         J=[s,s+q)\pmod t.             \tag{1.5}
\]

The conclusion holds for every syndrome \(k\), binary orbit vector \(b\),
and base-three state \(z\). It is an invariant of the deterministic
carry, not an averaged statement.

## 2. The forced eligibility-free run

Let \(T^-\) be the intersection of a \(q+1\)-vertex carry window starting
at \(X\). For a selected block position \(r\notin J\), that block is
untouched, so

\[
                         T^-\cap B_{i_r}
 =X\cap B_{i_r}\in\mathcal V.                         \tag{2.1}
\]

For \(r\in J\), exactly one selected coordinate is deleted in the block.
Consequently

\[
                         |T^-\cap B_{i_r}|=3,          \tag{2.2}
\]

and the block is ineligible for \(T^-\).

Every unselected physical block before \(i_t\) is ineligible for \(X\),
by the first-\(t\) convention. It is frozen throughout the window and
remains ineligible for \(T^-\). If \(J\) does not cross the cyclic cut,
its \(q\) selected blocks and every physical block between them form one
eligibility-free linear run. If \(J\) crosses the cut, its two linear
pieces have total length \(q\), so one has length at least
\(\lceil q/2\rceil\). The intervening unselected physical blocks are again
ineligible. Thus:

### Lemma 2.1

Every lower target hit by the carry at depth \(q<t\) contains a linear
run of at least \(\lceil q/2\rceil\) consecutive physical eight-blocks
which are all ineligible for that target.

The upper proof is identical. A touched block contributes the union of
two adjacent local middle states and therefore has size five rather than
four:

\[
                         |T^+\cap B_{i_r}|=5.          \tag{2.3}
\]

It is ineligible, while every untouched or frozen block has the same
eligibility status as before. Hence Lemma 2.1 holds for upper targets as
well.

The proof uses only the block-index word. The old/new row edge chosen by
the ternary predicate may alter which local three-set or five-set occurs,
but cannot alter (2.2) or (2.3).

## 3. Density of targets with the forced run

Fix a sign and generate a random target \(\mathbf T\) by taking every
coordinate independently with probability

\[
                         p_\pm={m\pm q\over2m},         \tag{3.1}
\]

then conditioning on \(|\mathbf T|=m\pm q\).

Before conditioning, the block eligibility indicators are independent,
with common probability

\[
\begin{aligned}
 \pi_q^\pm
 &=24p_\pm^4(1-p_\pm)^4\\
 &={3\over32}\left(1+O(q^2/m^2)\right)
 ={3\over32}+o(1)                                    \tag{3.2}
\end{aligned}
\]

uniformly for \(q=o(m)\).

Put \(L=\lceil q/2\rceil\). A union bound over \(B=O(m)\) possible
linear runs gives

\[
 \Pr(\text{an eligibility-free run of length }L)
 \le
 O(m)(1-\pi_q^\pm)^L.                                 \tag{3.3}
\]

For \(q=O(\sqrt m)\), the conditioning event in (3.1) has probability
\(\Theta(m^{-1/2})\), uniformly on every fixed Gaussian band, by the
elementary central-binomial estimate. Conditioning therefore multiplies
(3.3) by at most \(O(\sqrt m)\), proving

\[
 \Pr(\text{such a run}\mid|\mathbf T|=m\pm q)
 \le
 O(m^{3/2})
 \left({29\over32}+o(1)\right)^{q/2}.                 \tag{3.4}
\]

Lemma 2.1 proves (0.3). Formula (0.4) follows because

\[
 {N_q^\pm\over W}
 =\exp(-q^2/m+o(1))                                   \tag{3.5}
\]

at \(q=O(\sqrt m)\).

## 4. Exact deterministic Gram calculation

Assume local packet injectivity at the signed depth under discussion.
For macrocell \(a\), let \(\mathcal S_{a,j}\) be its actual deterministic
carry-shadow set. Then

\[
 |\mathcal S_{a,j}|=K=24^t,\qquad
 \sum_Td_j(T)=PK=G.                                   \tag{4.1}
\]

Expanding ordered macrocell pairs gives the exact identity

\[
\begin{aligned}
 \sum_{a\ne b}
 |\mathcal S_{a,j}\cap\mathcal S_{b,j}|
 &=\sum_Td_j(T)(d_j(T)-1),\\
 R_j
 &=\sum_Td_j(T)(d_j(T)-1)
   -{P(P-1)K^2\over N_j}.                             \tag{4.2}
\end{aligned}
\]

Let

\[
                         S_j=|\{T:d_j(T)>0\}|.          \tag{4.3}
\]

By (0.3), \(S_j\le\delta_qN_j\). Cauchy--Schwarz gives

\[
 \sum_Td_j(T)^2\ge {G^2\over S_j}
 \ge {G^2\over\delta_qN_j}.                           \tag{4.4}
\]

Since

\[
 \sum_Td_j(T)(d_j(T)-1)=\sum_Td_j(T)^2-G             \tag{4.5}
\]

and

\[
 {P(P-1)K^2\over N_j}
 ={G^2-GK\over N_j},                                  \tag{4.6}
\]

substitution proves (0.11).

If the right side of (0.11) is positive, multiply it by \(N_j\), divide
by \(G^2-GK\), and obtain

\[
\begin{aligned}
 \eta_j
 &\ge
 {G^2/\delta_q-N_jG-G^2+GK\over G^2-GK}\\
 &=
 {G/\delta_q-G-N_j+K\over G-K},                       \tag{4.7}
\end{aligned}
\]

which is (0.12).

At \(q=x\sqrt m+O(1)\), Stirling's formula gives

\[
 {G\over N_j}=e^{x^2+o(1)}.                           \tag{4.8}
\]

Also \(t=O(\sqrt m)\), so

\[
 {K\over G}
 ={24^t\over\binom{2m}{m}}(1+o(1))
 =e^{-\Theta(m)}.                                     \tag{4.9}
\]

The \(G/\delta_q\) term dominates the numerator of (4.7), giving
(0.14)--(0.15).

If local packet injectivity were to fail for the fused carry, the direct
missing-target obstruction (0.4) would remain valid and same-macrocell
duplicates would only make the labelled-shadow failure stronger. Local
injectivity is needed only to identify the cross-macrocell \(R_j\) with
the simple-set formula (4.2).

## 5. Why base-three equidistribution cannot help

For fixed binary orbit label \(b\) and syndrome \(k\), one full
\(2h\)-phase lap maps

\[
                         z\longmapsto z+1
 \quad\text{on }\mathbb Z/3^t\mathbb Z.               \tag{5.1}
\]

This proves perfect transitivity on the base-three states. But the active
block word during every lap remains (0.2). Thus all \(3^t\) carry states
repeat the same family of cyclic interval supports; they only change the
fine local row decoration attached to those supports.

After quotienting a physical target by the binary eligibility word of its
eight-blocks, the entire carry macrocell has support only on words
containing a zero-run of length at least \(q/2\). The density of this
quotient support is \(\delta_q\), which is exponentially small at
Gaussian depth. The base-three action is vertical inside these quotient
fibres and has no horizontal action on the eligibility words.

This is the exact macrocell quotient obstruction requested in the problem.
The smallest possible repair is not a different carry on the row digits.
It must alter the block-index order itself—by owner-dependent nonlinear
orders, many cross-macrocell order frames, or a construction abandoning
the canonical ordered first-\(t\) packet list.

## 6. Audit of the Gram criterion

There is also a normalization point. For actual deterministic carry
shadows, every owner contributes one target at a signed depth, so the
all-shuffle face-selection probability is effectively \(p=1\). The
physical variance is

\[
 V_j=G\left(1-{K\over N_j}\right)+R_j.                \tag{6.1}
\]

Thus even the hypothetical estimate \(R_j\le0\), or
\(\eta_j=0\), would not by itself prove a small actual-shadow hole count:
the diagonal term is \(\Theta(W)\). A Poisson multiplicity vector has
\(\eta_j=o(1)\) but still has a positive density of holes.

For the ternary carry this logical issue is secondary, because (0.14)
shows that its actual \(R_j\) is not small: it is exponentially above the
independent-packet baseline.

The balanced collision potential is the correct deterministic statistic.
Writing

\[
 \lambda_j={G\over N_j}=c_j+\theta_j,\qquad
 c_j=\lfloor\lambda_j\rfloor,\quad0\le\theta_j<1,      \tag{6.2}
\]

one has

\[
 2\Delta_j
 =V_j-N_j\theta_j(1-\theta_j)
 =G\left(1-{K\over N_j}\right)+R_j
   -N_j\theta_j(1-\theta_j).                          \tag{6.3}
\]

Every hole costs at least \(\binom{c_j+1}{2}\) units of \(\Delta_j\).
For the carry, however, (0.4) already gives the sharper exact conclusion:
almost the entire Gaussian target layer is missing.


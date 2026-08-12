# Charged crossing windows for the pair-omission spine

Date: 2026-07-25

Method: pure mathematics only. No search, finite computation, solver, or
external literature is used.

## 1. Statement of the result

Put

\[
 n=2m+1,\qquad L=2m-1,\qquad W={n\choose m},
 \qquad A_m={L\choose m-1},\qquad N_1={n\choose m-1}.
\]

Partition all but one coordinate into ordered pairs
\(P_1,\ldots ,P_m\), put \(Q_j=[n]\setminus P_j\), and use the
first-avoided-pair selection rule.  Let \(F\) be any exact central cyclic
wreath factor on an \(L\)-set.  For \(t\geq0\), define its distinct upper
interval deficit

\[
 d_t(F)={L\choose m+t}-|\mathcal I_{m+t}(F)|.                 \tag{1.1}
\]

Exactness at the middle gives \(d_0(F)=0\).

For each phase, take an independently relabelled copy of \(F\) on
\(Q_j\).  Let \(\widehat M_q^-\) and \(\widehat M_q^+\) denote the
numbers of global rank-\((m-q)\) and rank-\((m+q)\) targets outside the
union of the complete physical Pascal corridors of all selected owners.

### Theorem 1.1 (all crossing loss is negligible at the Gaussian depth)

There is an absolute constant \(C\) with the following property.  If
\(1\leq H\leq m/4\), the phase relabellings can be chosen simultaneously
so that their selected-row run count is \(J=O(W/m)\) and

\[
 \boxed{
 \sum_{q=1}^{H}(\widehat M_q^-+\widehat M_q^+)
 \leq
 C\sum_{t=1}^{H}d_t(F)
 +CW\left({H\over m}+{H^3\over m^2}\right)
 +e^{-\Omega(m)}W.}                                      \tag{1.2}
\]

The last term is uniform whenever \(H=o(m)\).  Conversely, for every
choice of the phase relabellings,

\[
 \boxed{
 \sum_{q=1}^{H}\widehat M_q^+
 \geq \sum_{t=1}^{H}d_t(F).}                              \tag{1.3}
\]

Consequently, if

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\longrightarrow\infty,\qquad
 \omega(m)^3=o(\sqrt m),                                 \tag{1.4}
\]

then

\[
 \inf_{\text{phase relabellings}}
 \sum_{q\leq H}(\widehat M_q^-+\widehat M_q^+)=o(W)
 \quad\Longleftrightarrow\quad
 \sum_{t\leq H}d_t(F)=o(W).                              \tag{1.5}
\]

In particular (1.4) includes
\(H=\lceil\alpha\sqrt{m\log m}\rceil\) for every fixed \(\alpha\); taking
\(\alpha>1/\sqrt2\) also kills the factor-independent outer binomial tail.
Thus, at the depth needed for that Gaussian tail, the
first-avoided-pair crossing and selection loss is unconditionally
\(o(W)\).  The exact residual is the multidepth interval-support deficit
already visible in phase one.

The rest of the note proves the theorem.

The fixed-base formulation has the following architecture-level
consequence.  For \(H=o(m^{2/3})\), there exist arbitrary exact local
factors \(F_1,\ldots,F_m\) and a first-avoided expanded-collar spine with

\[
 \sum_{q\le H}(\widehat M_q^-+\widehat M_q^+)=o(W)
\]

if and only if there exists one exact factor \(F\) on \(2m-1\) coordinates
with

\[
 \sum_{q\le H}d_q(F)=o(W).
\tag{1.6}
\]

Necessity follows by applying the phase-one argument proving (1.3) to
\(F_1\); sufficiency
follows by using relabelled copies of the factor in (1.6) in Theorem 1.1.
Thus allowing unrelated factors in later phases does not weaken the exact
residual gate.

For the tail-killing choice
\(H=\lceil\alpha\sqrt{m\log m}\rceil\),
\(\alpha>1/\sqrt2\), condition (1.6) would therefore imply

\[
 \nu(2m+1)\le W+o(W).
\tag{1.7}
\]

Indeed the expanded collars have length
\(N_1+3HJ+O(1)=W+o(W)\), Theorem 1.1 leaves only \(o(W)\) targets in
the signed band, and the outer binomial tails contain \(o(W)\) nonempty
targets.  Appending every remaining target gives (1.7); the standard
one-coordinate doubled lift gives the even dimensions as well.

## 2. The deterministic charged crossing-window lemma

Fix a phase \(j\), a cyclic row \(\pi\) of its local factor, and an upper
interval occurrence

\[
 U=I_\pi(s,m+q),\qquad 1\leq q\leq m-2.                   \tag{2.1}
\]

Its \(q+1\) candidate selected owners start at \(s+r\),
\(0\leq r\leq q\).  Their selection tests are

\[
 S_r=I_\pi(s+r,m-1).                                      \tag{2.2}
\]

Define the common core, crossing shell, and terminal point by

\[
 C=\bigcap_{r=0}^{q}S_r=I_\pi(s+q,m-q-1),
 \qquad D=U\setminus C,
 \qquad \tau=\pi_{s+m+q-1}.                              \tag{2.3}
\]

Then

\[
 |D|=2q+1,\qquad
 \bigcup_{r=0}^{q}S_r=U\setminus\{\tau\}.                \tag{2.4}
\]

Suppose that \(U\) has category \(j\): it avoids \(P_j\) and meets
every \(P_h\), \(h<j\).  For an earlier pair put

\[
 B_h=\{r\in\{0,\ldots,q\}:S_r\cap P_h=\varnothing\}.
                                                                    \tag{2.5}
\]

### Lemma 2.1 (terminal-or-double-shell charge)

If none of the \(q+1\) candidate owners is selected, then at least one of
the following holds.

1. There is a unique \(h<j\) such that
   \(P_h\cap U=\{\tau\}\).
2. The shell \(D\) meets two distinct earlier pairs.

Equivalently, pointwise,

\[
\begin{split}
 \mathbf1_{\{\kappa(U)=j,\;S_0,\ldots,S_q\text{ all unselected}\}}
 &\leq
 \sum_{h<j}\mathbf1_{\{P_h\cap U=\{\tau\}\}}\\
 &\quad+
 \sum_{h<g<j}
 \mathbf1_{\{D\cap P_h\ne\varnothing,\ D\cap P_g\ne\varnothing\}}.
                                                               \tag{2.6}
\end{split}
\]

#### Proof

The failure of candidate \(r\) means that \(r\in B_h\) for at least one
\(h<j\).  Hence complete failure says

\[
 \bigcup_{h<j}B_h=\{0,\ldots,q\}.                         \tag{2.7}
\]

If one \(B_h\) is the entire candidate set, then \(P_h\) misses the
union in (2.4).  Since the category assumption says \(P_h\cap U\ne
\varnothing\), necessarily

\[
 P_h\cap U=\{\tau\}.
\]

The pair is unique because the pair blocks are disjoint.

Otherwise (2.7) requires at least two distinct nonempty sets \(B_h\).
If \(r\in B_h\), then \(P_h\) meets \(U\), misses \(S_r\), and the core
\(C\) is contained in \(S_r\).  Thus \(P_h\cap D\ne\varnothing\).
The two distinct nonempty \(B_h\)'s therefore give two distinct earlier
pairs meeting \(D\).  This proves (2.6). \(\square\)

This is a deterministic charge, not a marginal-balance assertion.  A
failed occurrence is charged canonically to its terminal pair if case 1
holds; otherwise it is charged to the two least earlier pairs with
nonempty \(B_h\).  Every charged object is a literal crossing of the
specified physical occurrence.

## 3. Quantitative cost of the charges

Relabel the coordinates of a fixed local factor uniformly on \(Q_j\).
For every fixed row and start, the labels in the positions of \(U\) are a
uniformly ordered \((m+q)\)-subset of the \(L\) labels.  Put

\[
 r_0=j-1,\qquad k=m+q,\qquad d=2q+1.                    \tag{3.1}
\]

For all sufficiently large \(m\) and \(q\leq m/4\), there is an absolute
\(\rho<1\) such that a uniform subset of any of the universes below, of
the displayed sizes, meets each member of a collection of disjoint pairs
with joint probability at most \(\rho\) per pair.  Indeed the exact
single-pair meeting probability is

\[
 1-{(N-a)(N-a-1)\over N(N-1)},                            \tag{3.2}
\]

where \(a\) is the subset size; here the omitted fraction is bounded
below by an absolute positive constant.  The disjoint-pair
negative-association lemma then multiplies these marginal bounds.

For a specified earlier pair \(P_h\), the probability of the terminal
event in Lemma 2.1 is exactly

\[
 {2\over L}{L-k\over L-1}\leq {2\over L}.                \tag{3.3}
\]

Conditional on this event, the remaining \(k-1\) members of \(U\) form a
uniform subset of the remaining \(L-2\) labels.  The other \(r_0-1\)
earlier pairs must all meet \(U\).  Therefore the total terminal charge
probability is at most

\[
 {2r_0\over L}\rho^{r_0-1}.                              \tag{3.4}
\]

For two specified distinct earlier pairs, a union bound over their four
ordered choices of one endpoint gives

\[
 \Pr(D\text{ meets both pairs})
 \leq {4d(d-1)\over L(L-1)}.                             \tag{3.5}
\]

Conditional on the two designated endpoints lying in \(D\), the remaining
\(k-2\) members of \(U\) form a uniform subset of the remaining \(L-2\)
labels.  All other earlier pairs must meet \(U\).  Thus the double-shell
charge probability, including the category condition, is at most

\[
 {r_0\choose2}{4d(d-1)\over L(L-1)}\rho^{r_0-2}.          \tag{3.6}
\]

Combining (2.6), (3.4), and (3.6), a fixed upper occurrence is
category-\(j\) and selection-bad with probability at most

\[
 O\left({r_0\over m}\rho^{r_0-1}
       +{r_0^2(q+1)^2\over m^2}\rho^{r_0-2}\right).       \tag{3.7}
\]

Every local factor has exactly \(A_m\) interval occurrences at every
length.  Summing (3.7) over all phases, and using convergence of
\(\sum r\rho^{r-1}\) and \(\sum r^2\rho^{r-2}\), proves

\[
 \boxed{
 \mathbb E B_q^+
 =O\left({W\over m}+{W(q+1)^2\over m^2}\right),}          \tag{3.8}
\]

where \(B_q^+\) is the number of category upper occurrences locally
present but incident with no selected candidate owner.  Therefore

\[
 \sum_{q=1}^{H}\mathbb E B_q^+
 =O\left(W{H\over m}+W{H^3\over m^2}\right).             \tag{3.9}
\]

Notice that using only one of the \(q+1\) candidates would cost
\(O(q/m)\) per occurrence and would lose a factor \(q\).  Lemma 2.1 is
exactly the all-candidate gain: complete failure is either a one-point
terminal event of order \(m^{-1}\), or two shell crossings of order
\(q^2m^{-2}\).

## 4. Separating local absence from crossing failure

For any rank \(r\), write

\[
 \delta_r(F)={L\choose r}-|\mathcal I_r(F)|.              \tag{4.1}
\]

Under a uniform relabelling, a fixed \(r\)-set of \(Q_j\) is absent from
the interval support with probability

\[
 {\delta_r(F)\over {L\choose r}}.                         \tag{4.2}
\]

For \(m-H\leq r\leq m+H\) and \(H\leq m/4\),

\[
 {{n\choose r}\over {L\choose r}}
 ={n(n-1)\over(n-r)(n-1-r)}\leq 8.                       \tag{4.3}
\]

Every lower target \(T\) of rank \(m-q\) has a first avoided pair
\(j=\kappa(T)\).  If \(T\) occurs as an interval in \(F_j\), then the
same-start selection set \(S=I(s,m-1)\) contains \(T\), hence meets every
earlier pair, and its owner is selected.  Thus lower loss has no crossing
term:

\[
 \mathbb E\widehat M_q^-\leq 8\delta_{m-q}(F).            \tag{4.4}
\]

An upper target which avoids at least one pair also has a category.  If it
is locally present in its category factor but absent from the full
corridor, every one of its occurrences is selection-bad; choosing one
occurrence charges the target injectively to a term counted by \(B_q^+\).
Hence

\[
 \mathbb E\widehat M_q^+
 \leq 8\delta_{m+q}(F)+\mathbb E B_q^++R_q,               \tag{4.5}
\]

where \(R_q\) is the number of rank-\((m+q)\) targets meeting all \(m\)
pairs and therefore having no category.

There is an exact formula

\[
 R_q={m\choose q}2^{m-q}
     +{m\choose q-1}2^{m-q+1}.                            \tag{4.6}
\]

The two terms correspond respectively to omitting or including the
unpaired coordinate.  If \(H=o(m)\), the elementary bound
\({m\choose q}\leq(em/q)^q\), uniformly for \(q\leq H\), and
\(W\geq2^{2m}/(m+1)\) give

\[
 \sum_{q=1}^{H}R_q=e^{-\Omega(m)}W,                       \tag{4.7}
\]

where the notation permits an \(o(m)\) correction in the exponent.

Complementing a cyclic interval inside its \(L\)-coordinate row is a
cyclic interval of the complementary length.  Consequently

\[
 \delta_{m-q}(F)=\delta_{m+q-1}(F)=d_{q-1}(F).            \tag{4.8}
\]

Equations (3.9), (4.4), (4.5), and (4.8) now give the expectation in
(1.2).  The sharp run theorem has \(\mathbb EJ=O(W/m)\) under the same
random relabellings.  Applying Markov's inequality to the two nonnegative
random variables, with threshold three times their expectations, gives a
single deterministic set of relabellings satisfying both (1.2) and
\(J=O(W/m)\).

## 5. Phase one is the exact residual obstruction

All phase-one owners are selected.  Their rank-\((m+q)\) full-corridor
support is exactly \(\mathcal I_{m+q}(F_1)\), so phase one misses precisely
\(d_q(F)\) targets inside \({Q_1\choose m+q}\).

No later phase can cover one of these targets.  Indeed every selected
owner in phase \(j>1\) contains its selected rank-\((m-1)\) set, which
meets \(P_1\).  Every upper corridor target containing that owner therefore
meets \(P_1\), whereas every target contained in \(Q_1\) avoids \(P_1\).
Thus

\[
 \widehat M_q^+\geq d_q(F)                                \tag{5.1}
\]

for every \(q\), proving (1.3).

If (1.4) holds, then

\[
 {H\over m}+{H^3\over m^2}
 ={\omega\over\sqrt m}+{\omega^3\over\sqrt m}=o(1).      \tag{5.2}
\]

The upper and lower bounds (1.2)--(1.3) prove (1.5).

## 6. Adversarial audit and exact proved boundary

1. The shell has size \(2q+1\), not \(2q+2\): the common core has length
   \(m-q-1\), while \(|U|=m+q\).
2. The union of the selection windows omits exactly the terminal point.
   This is why a singleton at that point is the only one-pair explanation
   for failure of every candidate.
3. Merely meeting the shell is not asserted sufficient to spoil a
   candidate.  It is used only as a necessary condition, so the
   double-shell probability is an upper bound in the safe direction.
4. Equation (3.8) counts occurrences, not distinct targets.  A missing
   category target which is locally present has at least one bad
   occurrence, so occurrences legitimately upper-bound target holes.
5. Lower targets and upper targets are asymmetric.  Local presence alone
   covers a lower category target; upper targets require Lemma 2.1.
6. The all-pair-meeting targets in (4.6) have no category and are kept as
   a separate term.
7. No claim about common-owner balanced Hall flow is made.  The theorem is
   exactly about the full physical corridor support used by the expanded
   collar.
8. The result does not prove \(\sum d_t(F)=o(W)\).  In fact (1.3) proves
   that this local multidepth interval-support statement is necessary for
   this pair-omission architecture.  What is now proved is that there is no
   additional Gaussian-window loss from pair crossings, phase selection,
   row ordering, or collar chronology.

## 7. A concrete obstruction to any factor-blind spine theorem

The local residual in (1.6) is genuine.  For the explicit canonical exact
factor \(F^{\rm can}\) on \(2m-1\) coordinates, the algebraic marked-gap
construction gives

\[
 K_m=(2m-5)\operatorname{Cat}_{m-3}
\]

collision pairs of length-\((m-2)\) interval occurrences, with no pointed
occurrence used twice.  If \(A_m=\binom{2m-1}{m-1}\) and \(h\) is the
number of missing length-\((m-2)\) targets, then its duplicate excess is

\[
 A_m-\left(\binom{2m-1}{m-2}-h\right)
 =\frac{2A_m}{m+1}+h.
\]

Disjoint collision pairs force this excess to be at least \(K_m\).
Therefore

\[
 \boxed{
 d_1(F^{\rm can})=h
 \ge (2m-5)\operatorname{Cat}_{m-3}
      -\frac{2A_m}{m+1}
 =(1/64-o(1))W.}
\tag{7.1}
\]

The complete insertion--erasure proof of the marked-gap family and its
row-stability strengthening are recorded in
`MATH_ATTACK_A_PHASE_ONE_MULTIDEPTH_SHADOW_BARRIER_20260725.md`.
Coordinate relabelling preserves (7.1), while the same factors admit the
proved \(J=O(W/m)\) relabellings.  Hence a pair spine can have
\(HJ=o(W)\) and still have \(\widehat M_1^+=\Omega(W)\).

Thus Theorem 1.1 is sharp in scope: the pair-crossing charge is \(o(W)\),
but no factor-blind estimate can delete the term \(\sum_qd_q(F)\).  This
does not rule out a genuinely noncanonical exact factor satisfying (1.6).

# Dynamic TRP: LLL-distribution audit and the exact multiround boundary

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web input, or
black-box growing-uniformity theorem is used.

## 0. Verdict

The exact transition identities, the two Hall systems, the balanced-quota
ledger, the common upper-star obstruction, and the fresh-round LLL theorem
in DYNAMIC_TRP_ROUND_HALL_AND_FLAG_OBSTRUCTION_20260725.md all pass audit.

Two textual corrections were needed in that note and have been made.

1. The simultaneous arrival problem is an intersection of \(2Q+1\), not
   \(2Q+2\), partition matroids: one carrier partition and \(2Q\)
   arrival-controlled rank partitions.
2. Corollary 5.2 needs the intended hypothesis
   \[
     Q^2/m=(1+o(1))\log\log m,
   \]
   which is what gives \(\lambda_Q=(\log m)^{1+o(1)}\).

This audit proves three new results.

* A deterministic quota-filtered round theorem is controlled by one exact
  parameter
  \[
    \Gamma=\frac{2CA}{Ns^3},                                      \tag{0.1}
  \]
  where \(N\) is the number of carrier parts, \(s\) their minimum viable
  size, \(A=(m-Q)(H-Q)\) the raw maximum size, and \(C\) the total number
  of option-conflict edges. If \(s\to\infty\) and \(\Gamma=o(1)\), an
  independent transversal exists on
  \[
    (1-O(\Gamma^{1/3}))N
  \]
  carriers.

* The same theorem has an LLL-resampling distribution. For every event
  depending on \(h\) carrier choices, its probability is at most
  \[
    \exp(O(h\Gamma^{1/3}))
  \]
  times its product-measure probability on the pre-pruned viable option
  sets. This is a genuine one-round marginal theorem.

* There is a chronology-preserving path theorem. Put
  \[
   \eta_m=
   \frac{1+2\sum_{q=1}^{Q}\lambda_q}{\lambda_H}.                   \tag{0.2}
  \]
  Independent stationary rotor paths of length \(R\), one at every top,
  admit an LLL choice with no same-time collision in any controlled row
  whenever \(R\eta_m\le1/8\). The LLL law distorts an event on \(h\)
  carrier paths by at most \(\exp(O(hR\eta_m))\).

Neither theorem reaches coefficient one. The first compares the chosen
option only with the outgoing options of an already fixed current state,
not with a fresh uniform state. Its per-round errors are not summable over
\(M\) rounds. The path theorem has

\[
 \eta_m=(1+o(1))\frac{\lambda_Q}{Q},
 \qquad R=O(Q/\lambda_Q)=o(M),                       \tag{0.3}
\]

so it covers only \(RN_H=o(W)\) state occurrences.

For exact all-\(M\)-round completion there is also a sharp endpoint warning
against residual independence from the carrier fibres. Before the last
round, exactly \(N_H\) owner-quota targets remain, a density

\[
 \frac{N_H}{W}=\frac1{\lambda_H}\sim\frac1m.         \tag{0.4}
\]

A carrier has only \(H-Q\) distinct arrival owners. If the residual owner
set were uniformly mixed relative to those candidates, the probability of
even one legal arrival would be at most

\[
 \frac{H-Q}{\lambda_H}=o(1).                        \tag{0.5}
\]

Thus exact completion cannot use an ambient-uniform residual independently
of the carrier fibres. It needs a structured common-owner release/Hall
reserve aligned with those fibres. This is not by itself an obstruction to
coefficient one: Section 5 proves that a coefficient-safe construction may
stop \(\ell\) rounds early and repair the remaining targets literally.

## 1. Audit of the original exact statements

Write

\[
 a=H-Q,\qquad b=m-Q,\qquad A=ab.
\]

The successor formulas

\[
 X'=A_0+y,\qquad
 L'_q=A^-_q+y\ (q<Q),\qquad
 U'_q=A^+_q+y\ (q\le Q),\qquad
 L'_Q=L-x+y
\]

are correct. Hence the arrival \(y\) controls the owner and every flag
except the deepest lower flag; the delayed departure \(x\) controls that
last row only. The owner and deepest-lower systems are therefore literal
capacitated Hall systems.

The balanced-quota implication is also exact. Every rank emits total mass
\(T=MN_H\). If an integral evolution never exceeds an integral quota
vector of the same total mass, then it attains every quota coordinate
exactly. The scalar holes over the calibrated band sum to \(o(W)\).

The common-upper-star construction is legitimate. Its carrier states
partition their tops correctly, their owner candidate families are
pairwise disjoint, and all depth-\(Q\) upper candidates lie in the same
\(a\)-target family. Delayed departures cannot change this row.

Finally, the fresh-round conflict expectation is correctly normalized:

\[
 \mathbb E C_r
 \le \frac{A^2N_H^2}{2\binom{2m}{r}},               \tag{1.1}
\]

and therefore

\[
 \frac{2\mathbb EC}{AN_H}
 \le A\eta_m.                                       \tag{1.2}
\]

The pruning argument needs the average conflict degree to be \(o(A)\);
(1.2) supplies exactly that. There is no missing factor \(A\).

## 2. A sharp deterministic theorem for one filtered round

Consider any option-conflict graph whose vertex set is partitioned into
\(N\) carrier parts. Assume every part has between \(s\) and \(A\)
currently viable options, and let \(C\) be the total number of conflict
edges. Define \(\Gamma\) by (0.1).

### Theorem 2.1 (filtered-round transversal)

If \(s\to\infty\) and \(\Gamma=o(1)\), then, after discarding at most

\[
 \Gamma^{1/3}N                                      \tag{2.1}
\]

carrier parts, the remaining conflict graph has an independent
transversal.

#### Proof

If \(C=0\), there are no conflict edges and any one choice per carrier is
already an independent transversal. Assume henceforth that \(C>0\).
Put

\[
 \theta=\Gamma^{1/3},\qquad
 \Delta_0=\theta\frac{s^2}{A}.                      \tag{2.2}
\]

Delete every option vertex whose conflict degree exceeds \(\Delta_0\).
Since the total degree is \(2C\), the number of deleted options is at most

\[
 \frac{2C}{\Delta_0}
 =\frac{2CA}{\theta s^2}
 =\frac{\Gamma}{\theta}Ns
 =\theta^2Ns.                                       \tag{2.3}
\]

Discard a carrier part if it loses more than \(\theta s\) options. By
(2.3), at most \(\theta N\) parts are discarded. Every surviving part
has size at least

\[
 (1-\theta)s,                                       \tag{2.4}
\]

and every surviving option has conflict degree at most \(\Delta_0\).

Choose one option independently and uniformly from every surviving part.
For a conflict edge \(e\), let \(B_e\) be the event that both endpoints
are chosen. Then

\[
 \Pr(B_e)\le\frac1{(1-\theta)^2s^2}.                \tag{2.5}
\]

The event \(B_e\) uses two carrier variables. A carrier part is incident
with at most \(A\Delta_0\) conflict edges, so the dependency degree is at
most

\[
 2A\Delta_0=2\theta s^2.                            \tag{2.6}
\]

Consequently

\[
 e\,\Pr(B_e)(d+1)
 \le\frac{2e\theta}{(1-\theta)^2}+o(1)<1            \tag{2.7}
\]

for all sufficiently large \(m\). The symmetric local lemma supplies an
assignment avoiding every \(B_e\), which is the required independent
transversal. \(\square\)

The theorem is deterministic once the filtered conflict graph is given.
In the fresh-round setting \(s=A\), and (1.2) gives

\[
 \Gamma=\frac{2C}{N_HA^2}\le\eta_m                 \tag{2.8}
\]

for a suitable realization of the fresh states. Thus the exceptional
carrier fraction can be sharpened from an unparameterized \(o(1)\) to
\(O(\eta_m^{1/3})\).

## 3. The corresponding LLL distribution

The following elementary form of the resampling-distribution inequality is
used.

### Lemma 3.1 (local resampling marginal)

Let independent variables support bad events \(\mathcal B\), and suppose
numbers \(x_B\in(0,1)\) satisfy

\[
 \Pr(B)\le x_B\prod_{B'\sim B}(1-x_{B'}).           \tag{3.1}
\]

Run the variable-resampling algorithm until no bad event remains. If an
event \(E\) depends on a set of variables, then its output probability
satisfies

\[
 \Pr_{\mathrm{MT}}(E)
 \le \Pr_{\mathrm{prod}}(E)
    \prod_{B\sim E}(1-x_B)^{-1}.                    \tag{3.2}
\]

#### Proof

If \(E\) occurs in the final assignment, expose the last resamplings in
reverse chronological order and attach to a root labelled \(E\) every bad
event which can influence a variable of the current tree. This gives a
proper witness tree rooted at \(E\). Independence bounds the probability
of a fixed tree by the product of the probabilities of its labels.
Summing the child subtrees recursively and applying (3.1) bounds the total
weight contributed at a bad-event node by \(x_B\), while the children
adjacent to the root contribute
\(\prod_{B\sim E}(1-x_B)^{-1}\). Multiplication by the root probability
\(\Pr(E)\) gives (3.2). \(\square\)

### Theorem 3.2 (filtered-round marginal control)

Under Theorem 2.1, the independent transversal may be sampled from a
resampling distribution such that every event \(E\) depending on at most
\(h\) retained carrier variables obeys

\[
 \boxed{
 \Pr_{\mathrm{MT}}(E)
 \le
 \Pr_{\mathrm{viable}}(E)\exp(O(h\Gamma^{1/3}))}    \tag{3.3}
\]

Here \(\Pr_{\mathrm{viable}}\) is the product of the uniform distributions
on the option sets before the high-degree pruning.

#### Proof

On the pruned parts take

\[
 x=\frac{2}{(1-\theta)^2s^2}.                       \tag{3.4}
\]

Equations (2.5)--(2.6) show that (3.1) holds for all sufficiently small
\(\theta\). An event on \(h\) carrier variables is adjacent to at most

\[
 hA\Delta_0=h\theta s^2                             \tag{3.5}
\]

bad events. Lemma 3.1 and (3.4) therefore give a factor

\[
 \exp(O(h\theta)).                                  \tag{3.6}
\]

A retained carrier lost at most \(\theta s\) options, which is at most a
\(\theta\)-fraction of its pre-pruning viable part. Conditioning its
uniform variable on the retained subset costs another factor
\((1-\theta)^{-1}\). For \(h\) variables this is
\(\exp(O(h\theta))\). Since \(\theta=\Gamma^{1/3}\), (3.3) follows.
\(\square\)

In particular, every one-carrier marginal has total-variation distortion
\(O(\Gamma^{1/3})\) relative to the uniform law on its currently viable
options; the two-carrier upper distortion is also
\(1+O(\Gamma^{1/3})\).

This conclusion requires a vanishing cutoff. With a fixed
\(\delta>0\), one option may conflict with one specified option in each of
\(\lfloor\delta A\rfloor\) other parts while all its sibling options are
conflict-free. Conditioning on no conflict then gives

\[
 A\Pr(u\mid\text{no conflict})\longrightarrow e^{-\delta},       \tag{3.7}
\]

so a fixed-cutoff LLL has a genuine constant marginal bias.

There is a second, more important scope boundary. Theorem 3.2 compares the
chosen transition with the outgoing options of the already fixed current
state. One fixed state has only \(A\) successors inside an enormous rotor
state catalogue. It does **not** compare the successor with a fresh
uniform rotor state. Consequently (3.3) cannot simply be fed back into
the fresh-state calculation (1.1).

## 4. A genuine chronology-preserving short path theorem

The state-freezing problem can be avoided for a bounded horizon by choosing
whole rotor paths at once.

For a top \(U\), sample a stationary rotor path

\[
 \gamma_U=(\omega_U(0),\ldots,\omega_U(R))
\]

by taking \(\omega_U(0)\) uniformly from its radius-\(Q\) state catalogue
and, at each step, taking a uniform outgoing transition. The regularity of
the rotor makes every \(\omega_U(t)\) uniform. Sample these paths
independently for different tops.

For \(r=m\) and \(r=m\pm q\), \(1\le q\le Q\), let
\(F_r(\omega)\) denote the corresponding owner or flag. Introduce the bad
event

\[
 B_{U,V,t,r}=\{F_r(\omega_U(t))=F_r(\omega_V(t))\},
 \qquad U\ne V,\quad 1\le t\le R.                    \tag{4.1}
\]

### Theorem 4.1 (short simultaneous rotor paths)

If

\[
 R\eta_m\le\frac18,                                  \tag{4.2}
\]

then there are physical length-\(R\) rotor paths at every top such that,
at each emitted time \(t=1,\ldots,R\) and in every controlled rank, all
emitted targets are pairwise distinct across the tops.

Moreover the path-variable resampling law satisfies

\[
 \Pr_{\mathrm{MT}}(E)
 \le\Pr_{\mathrm{prod}}(E)\exp(O(hR\eta_m))          \tag{4.3}
\]

for every event depending on \(h\) carrier paths.

#### Proof

Fix \(U,t,r\). Since the path is stationary, its rank-\(r\) flag is
uniform in \(\binom Ur\). Independence of different carrier paths gives

\[
\begin{aligned}
 \sum_{V\ne U}\Pr(B_{U,V,t,r})
 &=\frac{\binom{2m-r}{M-r}-1}{\binom Mr}\\
 &=\frac{N_H}{\binom{2m}{r}}-\frac1{\binom Mr}.
                                                               \tag{4.4}
\end{aligned}
\]

For \(r=m\pm q\), the first term in (4.4) is
\(\lambda_q/\lambda_H\). Summing over all \(R\) times and all controlled
rows shows that the total probability mass of bad events involving one
fixed carrier-path variable is at most

\[
 R\eta_m.                                           \tag{4.5}
\]

Set \(x_B=2\Pr(B)\). A bad event uses two carrier variables, so the sum of
the \(x\)-weights in its dependency neighborhood is at most

\[
 4R\eta_m\le\frac12.                                \tag{4.6}
\]

Since \(\prod_i(1-x_i)\ge1-\sum_i x_i\), equations
(4.6) and \(x_B=2\Pr(B)\) verify the asymmetric LLL criterion. This proves
existence. Applying Lemma 3.1, an event on \(h\) path variables sees total
\(x\)-weight \(O(hR\eta_m)\), proving (4.3). \(\square\)

The uniform probability measure on all good path tuples is invariant under
coordinate permutations. The stabilizer of a fixed top is transitive on
its rotor states. Therefore, under that invariant good-path measure, the
one-carrier state marginal at every fixed time is exactly uniform. This is
a different measure from the MT output law in (4.3), and the symmetry does
not make two carriers independent.

### Proposition 4.2 (the path horizon is subcritical)

Under

\[
 Q^2/m=(1+o(1))\log\log m,
\]

one has

\[
 \eta_m=(1+o(1))\frac{\lambda_Q}{Q}
        =\frac{(\log m)^{1+o(1)}}{Q}.               \tag{4.7}
\]

Consequently Theorem 4.1 permits only

\[
 R=O(Q/\lambda_Q)=o(M),                             \tag{4.8}
\]

and its paths contain only \(RN_H=o(W)\) state occurrences.

#### Proof

Uniformly for \(q\le Q\),

\[
 \lambda_q=\exp(q^2/m+o(1)).
\]

Endpoint integration gives

\[
 \sum_{q=0}^{Q}\lambda_q
 =(1+o(1))\frac{m}{2Q}\lambda_Q.                    \tag{4.9}
\]

Since \(\lambda_H=(1+o(1))m\), substitution in (0.2) gives (4.7).
Equation (4.8) follows from (4.2). Finally
\(N_H=(1+o(1))W/m\), so \(RN_H=o(W)\). \(\square\)

These occurrences are distinct only within each time slice. They are not
certified quota-distinct across different times and hence are not, by
themselves, a valid partial balanced-quota filling.

Adding cross-time owner-collision events between distinct carrier paths
does not repair the scale. Their dependency-neighborhood probability mass
is of order

\[
 \frac{R^2}{\lambda_H}.                             \tag{4.10}
\]

At \(R\asymp M\), this is \(\Theta(m)\), not \(o(1)\). Thus global owner
distinctness is not a sparse-LLL consequence of independent stationary
paths. Same-carrier returns are not included in (4.10); controlling them
would require additional chronology estimates and cannot improve this
already divergent cross-carrier term.

There is also no compatible short mixing reset. If a marked coordinate
starts in the arrival reservoir of size \(a=H-Q\), then under uniform
transitions it remains there for \(t\) steps with probability at least

\[
 (1-1/a)^t.                                         \tag{4.11}
\]

Hence the one-carrier chain has mixing time \(\Omega(a)\). But

\[
 a\eta_m\sim\frac{H\lambda_Q}{Q}\longrightarrow\infty.            \tag{4.12}
\]

No block length is simultaneously long enough to erase this memory by a
black-box worst-case total-variation estimate and short enough to satisfy
\(R\eta_m=o(1)\). This does not exclude contraction on a more specialized
structured class of histories.

## 5. Exact residual-quota evolution

Let \(b_r(S)\) be a balanced integral quota of total mass \(T=MN_H\).
After \(t\) complete rounds put

\[
 c_{t,r}(S)=b_r(S)-\#\{\text{uses of }S\text{ in rounds }<t\}.
                                                               \tag{5.1}
\]

If no quota has been exceeded, then exactly

\[
 \sum_S c_{t,r}(S)=(M-t)N_H                       \tag{5.2}
\]

slots remain in every controlled rank. Thus the mean residual capacity is

\[
 \frac{(M-t)N_H}{N_q}
 =\left(1-\frac tM\right)\rho\lambda_q             \tag{5.3}
\]

at either signed depth \(q\).

### Lemma 5.1 (half-time low-depth support)

Let \(L=\lfloor\sqrt H\rfloor\). Uniformly for \(0\le q\le L\),

\[
 \rho\lambda_q=1+O(H/m)=1+o(1).                    \tag{5.4}
\]

After \(t=\lfloor M/2\rfloor\) successful rounds, the number of targets
with positive residual capacity in each such signed row is

\[
 \left(\frac12+o(1)\right)N_q.                     \tag{5.5}
\]

#### Proof

For \(q\le\sqrt H\), the central expansion gives
\(\log\lambda_q=O(H/m)\), while calibration gives
\(\rho=1-O(H/m)\). This proves (5.4).

A balanced quota at this mean has entries \(0,1\), or \(2\), and the total
number of zero or extra second-capacity slots is

\[
 |T-N_q|=o(N_q).                                    \tag{5.6}
\]

By half time the row has emitted \(tN_H=T/2+o(N_q)\) occurrences.
The residual mass is therefore \(T/2+o(N_q)\). A residual coordinate can
have value two only if its initial quota was two, and there are
\((T-N_q)_+=o(N_q)\) such coordinates. Hence residual support differs
from residual mass by only \(o(N_q)\). Since \(T/N_q=1+o(1)\), this proves
(5.5).
\(\square\)

Lemma 5.1 rules out independent rowwise quasirandomness as the desired
invariant. There are \(2\lfloor\sqrt H\rfloor+1\) such owner/flag rows.
If, for a fixed transition option, membership of its targets in their
positive residual sets factored across these rows up to
\(\exp(o(\sqrt H))\), its probability of being legal would be

\[
 \exp(-\Theta(\sqrt H)).                            \tag{5.7}
\]

Since \(A\) is polynomial in \(m\),

\[
 A\exp(-\Theta(\sqrt H))=o(1).                      \tag{5.8}
\]

Thus almost every carrier would have no complete legal column. The
residual rows must instead have strong positive alignment along the actual
nested transition columns.

### Lemma 5.2 (terminal owner reserve)

Immediately before the last round, exactly \(N_H\) middle-owner targets
have positive residual quota.

#### Proof

Because \(T\le W\), the balanced middle quota is a \(0/1\) vector with
exactly \(T\) ones. The first \(M-1\) rounds use
\((M-1)N_H\) distinct quota-one owners. Hence the remaining support has
size

\[
 T-(M-1)N_H=N_H.                                    \tag{5.9}
\]

\(\square\)

For a carrier, the next-owner candidates \(A_0+y\), \(y\in R\), are
\(a=H-Q\) distinct owners. If the terminal support in Lemma 5.2 were a
uniform \(N_H\)-subset independent of this fibre, then

\[
 \Pr(\text{at least one legal arrival})
 \le \frac{aN_H}{W}
 =\frac{H-Q}{\lambda_H}=o(1).                      \tag{5.10}
\]

Therefore uniform residual mixing would block \(1-o(1)\) of the carriers
at the last round. The factor \(b=m-Q\) of delayed departures only
duplicates each arrival at the full-option level and cannot repair the
absence of a legal \(y\).

This is an obstruction to exact last-round completion, not to coefficient
one itself.

### Lemma 5.3 (coefficient-safe early stopping)

Suppose the dynamic construction completes the first \(M-\ell\) rounds
without exceeding the original balanced quotas, where
\(\ell\) is an integer and

\[
 \ell=o(m/Q).                                        \tag{5.11}
\]

Then all remaining controlled-rank coverage holes can be appended literally
at total cost \(o(W)\). This repairs support and intentionally abandons
completion of the unused quota multiplicities.

#### Proof

At every controlled rank, the residual quota mass after \(M-\ell\) rounds
is exactly \(\ell N_H\). A target with positive prescribed quota which has
not yet appeared consumes at least one of these residual slots, so there
are at most \(\ell N_H\) such targets. Targets with prescribed quota zero
contribute exactly the scalar floor

\[
 \left(\binom{2m}{r}-T\right)_+.
\]

Summing over the \(2Q+1\) controlled rows, the total missing-target count
is at most

\[
 (2Q+1)\ell N_H
 +\sum_{\text{controlled }r}
   \left(\binom{2m}{r}-T\right)_+.                  \tag{5.12}
\]

The second term is \(o(W)\) by the calibrated scalar-hole estimate in the
source note. Since \(N_H=(1+o(1))W/m\), the first is

\[
 O(Q\ell W/m)=o(W)                                  \tag{5.13}
\]

by (5.11). \(\square\)

Because \(Q=o(H)\), one may choose

\[
 \frac mH\ll\ell\ll\frac mQ.                        \tag{5.14}
\]

The remaining owner-quota support then has size \(\ell N_H\). If it were
ambient-uniform relative to one carrier's \(H-Q\) arrival candidates, the
expected number of legal arrivals would be

\[
 \frac{(H-Q)\ell}{\lambda_H}
 =(1+o(1))\frac{H\ell}{m}\longrightarrow\infty.     \tag{5.15}
\]

Thus early stopping removes that particular sparse terminal-fibre warning
at coefficient-safe cost. It does not prove multiround feasibility and
does not remove the half-time common-column obstruction (5.7)--(5.8).

## 6. Why the one-round LLL marginal does not iterate

In the fresh round, Theorem 3.2 has error

\[
 \theta_m=\eta_m^{1/3}.                             \tag{6.1}
\]

A direct product-law iteration would accumulate a distortion bounded only
by

\[
 \exp\left(O\left(h\sum_{t<M}\theta_t\right)\right). \tag{6.2}
\]

Even if every round retained the fresh value, one has

\[
 M\eta_m^{1/3}\longrightarrow\infty.                \tag{6.3}
\]

Using a different pruning balance cannot make the errors summable from the
fresh average-degree estimate alone. To guarantee deletion of only
\(o(A)\) options using only that estimate, a maximum-degree cutoff
\(\delta_mA\) must have \(\delta_m\gg\eta_m\); but

\[
 M\eta_m\sim \frac{m\lambda_Q}{Q}\longrightarrow\infty.           \tag{6.4}
\]

More fundamentally, (3.3) is relative to a fixed current-state option
set. It gives no contraction toward the fresh state law. The rotor kernel
is non-expansive in total variation but, by (4.11), has long-lived modes.
Thus no missing elementary summation turns the fresh theorem into \(M\)
rounds.

For exact all-round completion, the terminal owner support must be strongly
correlated with the current carrier fibres; globally uniform one-point
marginals can coexist with that alignment. Lemma 5.3 shows that coefficient
one may instead stop before the sparse endpoint. The enduring obstruction
to a rowwise-product invariant is the half-time vertical extinction in
(5.7)--(5.8).

## 7. The exact surviving multiround invariant

At round \(t\), delete every transition option which hits a zero residual
quota. On the remaining full options let

* \(N_t\) be the number of active carriers;
* \(s_t\) be the minimum viable full-option count;
* \(C_t\) be the total conflict-edge count;
* \(A=(m-Q)(H-Q)\) be the raw maximum part size.

Define

\[
 \boxed{\Gamma_t=\frac{2C_tA}{N_ts_t^3}}           \tag{7.1}
\]

Theorem 2.1 proves a round extension, with
\(O(\Gamma_t^{1/3})N_t\) exceptional carriers, whenever

\[
 s_t\to\infty,\qquad \Gamma_t=o(1).                \tag{7.2}
\]

This is not yet sufficient at the endpoint, because \(s_t\) can conceal
the factor \(b\) of delayed departures above one arrival. One must also
control the distinct arrival fibres

\[
 Y_i(t)=
 \{y\in R_i:\text{some }x\in L_i
       \text{ gives a quota-legal full column}\}.                  \tag{7.3}
\]

For exact \(M\)-round quota completion, the minimal live theorem is:

> **Quota-filtered nested release.** Through all \(M\) rounds, preserve
> a capacitated Hall reserve for the families \(Y_i(t)\), preserve
> \(\Gamma_t=o(1)\) after filtering, and align the positive residual
> targets across ranks along common nested transition columns.

For coefficient one, Lemma 5.3 permits the same assertion only through
\(M-\ell\) rounds, for any \(\ell\) satisfying (5.14), followed by literal
repair. This invariant is deliberately not called quasirandom. Lemma 5.1
shows that independent rowwise quasirandomness is already incompatible
with continuation at half time.

## 8. Audit ledger

### Proved

1. All substantive theorems in the source note pass audit.
2. The corrected partition-matroid count and the needed \(Q\)-regime.
3. The exact filtered-round parameter \(\Gamma\) and Theorem 2.1.
4. The one- and bounded-carrier LLL-resampling bound, Theorem 3.2.
5. The physical short-path LLL, Theorem 4.1, with its exact horizon.
6. Exact residual quota mass, half-time support density, terminal owner
   support, and coefficient-safe early stopping.
7. Uniform/product-like residuals are quantitatively incompatible with
   full-depth and terminal continuation.

### Open

1. Quota-filtered nested release (7.3) through \(M-\ell\) rounds for some
   \(m/H\ll\ell\ll m/Q\) (or through all \(M\) rounds for exact TRP).
2. Uniform control of \(\Gamma_t\) after quota exhaustion.
3. Exact completion of all balanced quotas, and hence TRP and coefficient
   one by this route.

The fresh-round LLL is therefore strengthened but not promoted to a full
multiround theorem. Its correct durable output is the filtered-round
criterion (7.1), while the remaining coefficient-one gate is a structured
common-owner/common-flag release theorem rather than an LLL marginal
estimate.

# Catalan facet-endpoint support: exact mean four, dispersion, and the branching gate

Date: 2026-08-01  
Lane: R / resident facet-socket extraction  
Status: unconditional endpoint and random-model theorems; exact typed
lower-colour/component formula; sharp scope obstruction to an automatic
absorbing argument.  No protected extraction or contiguous-OR construction
is claimed.

## 1. Catalan forest notation

Assume `m>=3`, and put

\[
 X=[2m-1],\qquad
 \mathcal V={X\choose m},\qquad
 \mathcal U={X\choose m+1},\qquad
 \mathcal L={X\choose m-1}.
\]

Write

\[
 W=|\mathcal V|=|\mathcal L|,\qquad
 D=|\mathcal U|={m-1\over m+1}W,\qquad
 C=W-D={2W\over m+1}=\operatorname {Cat}_m.       \tag{1.1}
\]

Let `F` be a spanning linear forest on `\mathcal V` with `D` edges.  Assume
that its edge unions are all distinct and exhaust `\mathcal U`, while its
edge intersections are distinct elements of `\mathcal L`.  Thus `F` has
exactly `C` path components and exactly `C` missing lower colours.

An isolated component has two endpoint **slots** at the same owner.  A
nontrivial component has its two usual distinct endpoint owners.  Let `E`
be the resulting endpoint-slot multiset, so

\[
                         |E|=2C.                       \tag{1.2}
\]

When no component is isolated, `E` is an ordinary set.  All assertions
about two distinct facet owners below use this no-isolate hypothesis.  With
isolates, the mean-four identity remains true for slots, but two coincident
slots do not form a socket.

For `R\in\mathcal U`, define

\[
 K_R=|\{e\in E:e\subset R\}|,                         \tag{1.3}
\]

with slot multiplicity.  Call `R` **raw two-endpoint supported** when it
contains two distinct endpoint owners.

## 2. The exact mean-four law

### Theorem 2.1 (endpoint mean four)

For every Catalan forest as above,

\[
                     \sum_{R\in\mathcal U}K_R=4D.     \tag{2.1}
\]

Consequently the average value of `K_R` is exactly four.  If the endpoint
bank has no repeated slot, then

\[
 \bigl|\{R:K_R\ge2\}\bigr|\ge {3D\over m},            \tag{2.2}
\]

and

\[
 \bigl|\{R:K_R\ge3\}\bigr|\ge {2D\over m-1}.          \tag{2.3}
\]

Every target counted in (2.3) has endpoints in two different components.

#### Proof

Every rank-`m` owner is contained in exactly `m-1` rank-`m+1` sets.
Therefore

\[
 \sum_RK_R=|E|(m-1)=2C(m-1)=4D,
\]

where the last equality is (1.1).  If `S_2=|{R:K_R>=2}|`, then

\[
 4D=\sum_RK_R\le(D-S_2)+S_2(m+1)=D+mS_2,
\]

which proves (2.2).  Similarly, if `S_3=|{R:K_R>=3}|`, then

\[
 4D\le2(D-S_3)+(m+1)S_3=2D+(m-1)S_3.
\]

A path component has at most two distinct endpoint owners, so three
endpoint facets cannot all belong to one component.  This proves (2.3).
\(\square\)

The bounds (2.2)--(2.3) are only `Theta(1/m)` fractions.  At the level of
the sole constraints `0<=K_R<=m+1` and mean four, (2.2) is sharp: put
`K_R=m+1` on a `3/m` fraction and `K_R=1` elsewhere.  Thus the mean-four
law alone cannot prove a positive supported fraction.

Under the same no-isolate hypothesis there is nevertheless a large raw pair
count.  Convexity gives

\[
 \sum_R {K_R\choose2}\ge 6D.                          \tag{2.4}
\]

At most one endpoint pair per component is a same-component pair, so at
least

\[
                         6D-C                         \tag{2.5}
\]

raw endpoint pairs join different components.  This is a ticket-count
statement, not a dispersion statement: many tickets may belong to the same
target.

### Corollary 2.2 (full compact sockets are sparse from endpoints alone)

For any `h>=1`,

\[
 { |\{R:K_R\ge h+1\}| \over D}\le {4\over h+1}.       \tag{2.6}
\]

Thus if the compact resident socket is required to find all its `h+1`
facets already exposed as forest endpoints, the direct endpoint reservoir
has density at most `O(1/h)`.  The useful interpretation of mean four is
therefore a two-facet seed followed by a protected extraction theorem, not
an already present `h+1`-facet socket.

## 3. Uniform-random endpoint support

Temporarily forget forest realizability and choose an `e=2C` element
endpoint set uniformly from the `W` owners.  For a fixed
`R\in\mathcal U`,
`K_R` is hypergeometric:

\[
 \Pr(K_R=j)=
 { {m+1\choose j}{W-m-1\choose e-j}\over {W\choose e}}.       \tag{3.1}
\]

In particular

\[
 p_m:=\Pr(K_R\ge2)
 =1-{ {W-m-1\choose e}+(m+1){W-m-1\choose e-1}
       \over {W\choose e}}.                            \tag{3.2}
\]

Since `e/W=4/(m+1)` and `W` is exponential in `m`,

\[
 K_R\Longrightarrow\operatorname {Poisson}(4),\qquad
 p_m\longrightarrow1-5e^{-4}=0.908421\ldots.          \tag{3.3}
\]

The expected number of raw pairs at one target is

\[
 \mathbb E {K_R\choose2}
 ={m+1\choose2}{(e)_2\over(W)_2}\longrightarrow8.     \tag{3.4}
\]

If, after choosing `E`, its elements are paired uniformly into `C`
component-endpoint pairs, then

\[
 \Pr(R\hbox{ has a cross-component endpoint pair})
 =p_m-{\Pr(K_R=2)\over e-1}.                           \tag{3.5}
\]

Hence the component condition alone is asymptotically free in this random
model.

More generally, the random probability of finding all `h+1` compact-socket
facets is

\[
 1-\sum_{j=0}^{h}
 { {m+1\choose j}{W-m-1\choose e-j}\over {W\choose e}},       \tag{3.6}
\]

which tends, for fixed `h`, to the corresponding Poisson-four tail.  More
generally, factorial-moment Markov gives, for `t=h+1`,

\[
 \Pr(K_R\ge t)\le
 { (m+1)_t(e)_t\over (W)_t t!}
 \le {4^t\over t!}\le\left({4\mathrm e\over t}\right)^t. \tag{3.7}
\]

Thus the direct full-socket probability decays superpolynomially whenever
`h` grows.

Equations (3.2)--(3.6) concern a uniformly random endpoint set, not a
uniformly random double-rainbow Catalan forest.  No such forest measure is
constructed here.

## 4. Transitivity and the sharp dispersion warning

If a deterministic typed forest automorphism group preserves its endpoint
slots and acts transitively on `\mathcal U`, then (2.1) forces

\[
                              K_R=4                    \tag{4.1}
\]

for every target.  In a no-isolate forest, every target is then raw
two-endpoint supported.  This strong target-transitivity is sufficient.

Coordinate transitivity, equal one-point marginals, or exchangeability in
law is not sufficient.  Here is an exact endpoint-ledger obstruction.
Choose the largest integer `s` for which

\[
             {2m-1-s\choose m-s}\ge e.                \tag{4.2}
\]

Fix an `s`-set `T`, and choose any `e` endpoint owners from the star

\[
                    \{F\in\mathcal V:T\subset F\}.     \tag{4.3}
\]

Every target with even one endpoint facet must contain `T`.  Hence its raw
supported fraction is at most

\[
 { {2m-1-s\choose m+1-s}\over {2m-1\choose m+1}}
 ={(m+1)_s\over(2m-1)_s}=\Theta(1/m),                 \tag{4.4}
\]

because (4.2) gives `s=log_2 m+O(1)`.  Randomizing `T` uniformly and then
the `e`-subset in (4.3) gives a fully `Sym(X)`-exchangeable law with the
correct endpoint count and equal one-point marginals, while (4.4) remains
vanishing.

This is a counterexample to every inference using only endpoint count and
transitivity in law.  It is not asserted to be the endpoint bank of an
exact upper/lower-rainbow Catalan forest.  Indeed a genuine forest also
satisfies the coordinate endpoint-hole cocycle

\[
 E_x=H_x+2\operatorname {Cat}_{m-1},                  \tag{4.5}
\]

where `H_x` is the number of missing lower colours containing `x`.  The
single-star ledger (4.3) does violate (4.5): for `x\in T` it has
`E_x=2C`, which would require

\[
 H_x=2C-2\operatorname {Cat}_{m-1}>C\qquad(m\ge3),
\]

impossible for a `C`-element missing bank.  For completeness, the cocycle
follows by
writing

\[
 E_x=2\binom{2m-2}{m-1}
 -\sum_{FG\in E(F)}
   \bigl(\mathbf1_{x\in F}+\mathbf1_{x\in G}\bigr).   \tag{4.6}
\]

On a Johnson edge `FG`, the summand equals the indicator of `x` in the
intersection plus the indicator of `x` in the union.  Upper unions exhaust
`\mathcal U`, while lower intersections exhaust
`\mathcal L\setminus\mathcal M`.  Therefore (4.6) equals

\[
 2\binom{2m-2}{m-1}-\binom{2m-2}{m}
 -\binom{2m-2}{m-2}+H_x
 =2\operatorname {Cat}_{m-1}+H_x.
\]

Proving that upper/lower exactness plus
(4.5) forbids every balanced high-order version of (4.3) is precisely a
new dispersion theorem, not a consequence of mean four.

## 5. The exact lower-colour and component ticket formula

This section concerns the direct Johnson connector available **after** two
facets have been exposed.  It is not the resource ledger of the full
`h+1`-facet socket, whose ordered facets contribute `h` internal lower
colours and two guard intervals.  In particular, (5.3)--(5.5) must not be
substituted for the probability that a compact socket can be extracted.

Assume again that there are no isolated components.  Let
`\mathcal M\subset\mathcal L` be the `C` missing lower colours.  For
`L\in\mathcal M`, put

\[
 A_L=\{x\in X\setminus L:L+x\in E\},\qquad a_L=|A_L|. \tag{5.1}
\]

Let `b_L` count components whose two distinct endpoints have intersection
exactly `L`.  A **direct legal ticket** for `R` is a pair of endpoint owners
`F,G` such that

\[
 F\cup G=R,\qquad F\cap G\in\mathcal M,\qquad
 \operatorname {comp}(F)\ne\operatorname {comp}(G).   \tag{5.2}
\]

The first condition restores the demanded upper colour, the second spends
one actually unused lower colour, and the third merges rather than cycles
components.

### Theorem 5.1 (typed ticket census)

The total number `T_dir` of direct legal tickets is exactly

\[
             T_{\rm dir}=
             \sum_{L\in\mathcal M}\left({a_L\choose2}-b_L\right).     \tag{5.3}
\]

#### Proof

For fixed `L`, every pair `x\ne y` in `A_L` gives the unique endpoint pair
`L+x,L+y`, with lower colour `L` and upper target `L+x+y`.  Conversely every
ticket of lower colour `L` has this form.  The only forbidden pairs are the
two endpoints of one component, counted by `b_L`.  Summing over the
distinct lower colours proves (5.3).  \(\square\)

There is no positive **uniform asymptotic** lower bound for (5.3) from
`|E|=2C` and `|\mathcal M|=C` alone: for all sufficiently large `m`, put
the endpoints in the star (4.3) and choose the missing lowers among sets
`L` with `|T-L|>=2`; then every `a_L` is zero.  (At `m=3` the endpoint
bank is forced and this unrestricted sentence would be false.)  This is
the first exact correlation needed from a protected Catalan reservoir.

For calibration, choose `E` uniformly, pair its endpoints uniformly, and
choose `\mathcal M` as an independent uniform `C`-subset of `\mathcal L`.
Then

\[
 \mathbb E T_{\rm dir}
 =C{m\choose2}{e(e-2)\over W(W-1)},                   \tag{5.4}
\]

and therefore

\[
 {\mathbb E T_{\rm dir}\over D}
 =m{e(e-2)\over W(W-1)}
 ={16+o(1)\over m}.                                   \tag{5.5}
\]

By Markov's inequality, the expected fraction of targets with even one
direct legal ticket is at most `(16+o(1))/m`.  Thus the raw constant
`1-5e^-4` in (3.3) collapses to zero if lower colours are treated as an
independent missing palette.  Any positive theorem must correlate endpoint
pairs with missing lower colours, or allow a controlled lower-debt relay
instead of insisting on (5.2).

The same random model separates target sparsity from token pressure.  If
`N_R` is the number of tickets at a fixed target, `N_F` the number incident
to a fixed selected endpoint, and `N_L` the number using a fixed selected
missing lower, then

\[
\begin{aligned}
 \mathbb E N_R
   &=m{e(e-2)\over W(W-1)}\sim {16\over m},\\
 \mathbb E(N_F\mid F\in E)
   &=m(m-1){e-2\over W-1}{C\over W}\longrightarrow8,\\
 \mathbb E(N_L\mid L\in\mathcal M)
   &={m\choose2}{e(e-2)\over W(W-1)}\longrightarrow8.
\end{aligned}                                                   \tag{5.6}
\]

The mean degree of the contracted-component ticket graph tends to `16`.
These are averages; maximum loads, tails and graphic cycles remain
uncontrolled.

For several simultaneous sockets, tickets also consume two endpoint owners
and one missing lower colour each.  Their contracted component edges must
be graphic-independent.  The exact finite selection rows are therefore:

1. one ticket for every demanded upper target;
2. endpoint-owner capacity one;
3. missing-lower-colour capacity one; and
4. no cycle after contracting the current forest components.

This is a pair-ticket hypergraph with a graphic row; ordinary bipartite
Hall on targets versus endpoints does not characterize it.

If a used lower colour is permitted, adding `FG` relocates rather than
closes the lower defect.  Deleting terminal forest edges may release one or
two lower colours, but those released occurrence labels must appear in the
state.  Set equality of lower masks without occurrence and component data
is insufficient.

## 6. The exact subcritical-branching hypothesis

There is one valid probabilistic closure statement.  Suppose an adaptive
extraction procedure processes active upper demands one at a time.  Assume
as an additional oracle hypothesis that a raw two-endpoint-supported demand
can be completed to the full ordered facet socket with all lower and guard
resources, without children.  An unsupported extraction creates at most two
child immediate-upper demands.  Assume that after every finite residual
history, including all previous resource deletions, the conditional chance
of such a legal full closure is uniformly at least `p_0>1/2`.  Then the expected number
of children of a processed demand is at most

\[
                         \rho=2(1-p_0)<1,               \tag{6.1}
\]

and `H` initial demands have expected total exploration size at most

\[
                         {H\over1-\rho}
                         ={H\over2p_0-1}.               \tag{6.2}
\]

This is the standard first-moment proof: if `Z_j` is the number of demands
in generation `j`, then
`E(Z_(j+1)|history)<=rho Z_j`; sum the resulting geometric series.
With a finite state space and genuinely fresh legal tickets, extinction is
almost sure.

The uniform raw endpoint-and-pairing model has finite cross-component
marginal (3.5), tending to

\[
 1-5e^{-4}>1/2.                                        \tag{6.3}
\]

so, **if the oracle hypothesis held**, it would suggest a subcritical binary
exploration.  But (3.2) is only an unconditional one-target raw marginal.
It proves neither the ordered `h+1`-facet extraction nor a lower/guard
assignment, and gives no lower bound after an adaptive history.  The star
mixture in Section 4 has equal one-point
marginals but reveals a latent set `T`; after that revelation some targets
have conditional support probability zero.  More decisively, the direct
lower-safe random model has probability at most `O(1/m)` by (5.5), far
below the threshold `1/2`.

Thus a protected extraction theorem needs the following hereditary form,
not merely mean four:

> **Hereditary protected-socket dispersion.**  After every finite legal
> residual history, every exposed child target has conditional mass greater
> than `1/2` on complete zero-child socket closures, including its ordered
> facets, guards, endpoint/lower resources and graphic effect.

A more general deterministic sufficient condition (not an equivalent
rephrasing of the scalar `p_0` hypothesis) is this.  In every residual
state, a jointly realizable selection oracle supplies a distribution
`mu_R` on complete legal packets and a positive target potential `w` such
that

\[
 \sum_p\mu_R(p)\sum_{R'\in\partial p}w(R')
       \le\rho w(R),\qquad \rho<1,                     \tag{6.4}
\]

through every residual state, together with the four selection rows after
(5.5).  Here `\partial p` is the multiset of unique immediate-upper witnesses
destroyed by installing `p`.  Formula (6.4) contracts total potential.  To
deduce a dimension-uniform `O(H)` packet/collar count one additionally
needs a uniform normalization such as `1<=w(R)<=K`; positivity alone is
only a fixed-finite-state termination statement.  Formula (6.4), not the
scalar endpoint average, is the exact subcritical/absorbing gate.

## 7. Scoped conclusion

The Catalan endpoint reservoir has three sharply different levels.

* **Raw:** mean exactly four; a uniform endpoint set supports a fixed target
  with limiting probability `1-5e^-4`, and the component condition is
  asymptotically negligible.
* **Direct post-extraction connector:** exact supply is (5.3); under an
  independent missing-lower palette its available-target fraction is only
  `O(1/m)`.  This is not the full socket's ordered lower/guard ledger.
* **Recursive protected:** subcriticality follows from the hereditary
  conditional inequality (6.4), but neither mean four nor transitivity in
  law proves it.

Accordingly, the compact resident facet socket supplies the correct local
accepting block.  The missing all-`m` theorem is a correlated endpoint--
missing-lower dispersion and regenerative graphic-selection theorem for an
actual double-rainbow Catalan forest.  This note neither proves nor refutes
that stronger physical statement.
